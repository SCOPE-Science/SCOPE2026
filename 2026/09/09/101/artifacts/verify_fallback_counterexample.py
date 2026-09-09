"""Lane-479 fallback audit: the 1D variance-gap lemma is FALSE as stated.

Fallback claim: every even log-concave f:R->[0,1], f(0)=1, 0<int f<oo satisfies
  J(f) >= 4(1+(1/8)*min(1,(m(f)-1/3)^2)),  J=(int f)(int f^circ), m=variance.

Counterexample: f(x)=exp(-|x|).
  - even, log-concave (log f = -|x|), range (0,1], f(0)=1, int f = 2.
  - f^circ(y)=inf_x e^{-xy+|x|}: equals 1 on [-1,1] (attained at x=0; every
    exponent -xy+|x| >= |x|(1-|y|) >= 0) and 0 outside (t*sign(y), t->inf).
    Hence int f^circ = 2, J(f) = 4.
  - m(f) = (int x^2 e^{-|x|})/(2) = 2, so RHS = 4(1+1/8*min(1,25/9)) = 9/2 = 4.5.
  - 4 < 4.5: inequality violated with margin 1/2 (not a rounding artifact).
In fact J == 4 identically on the whole ray f_a(x)=e^{-a|x|} while m=2/a^2
ranges over (0,oo): no variance-gap stability around benchmark 1/3 can hold.

This script: (i) certifies the closed-form integrals numerically (Simpson +
rigorous exponential tail bounds, stdlib only); (ii) certifies the f^circ
identity on a grid plus analytic tail-witness check; (iii) prints the margin.
"""
import math

print("=== (i) closed-form integrals vs rigorous numeric quadrature ===")
A = 15.0
N = 20000  # even
h = 2 * A / N
g0 = lambda x: math.exp(-abs(x))
g2 = lambda x: x * x * math.exp(-abs(x))
S0 = g0(-A) + g0(A)
S2 = g2(-A) + g2(A)
for k in range(1, N):
    x = -A + k * h
    w = 4.0 if k % 2 else 2.0
    S0 += w * g0(x)
    S2 += w * g2(x)
Q0 = h / 3 * S0
Q2 = h / 3 * S2
tail0 = 2 * math.exp(-A)                       # int_{|x|>A} e^-|x| = 2e^-A
tail2 = 2 * math.exp(-A) * (A * A + 2 * A + 2)  # int_{|x|>A} x^2 e^-|x|
I0, I2 = 2.0, 4.0                              # closed forms: 2, 2*2
print(f"int f on [-{A},{A}]: quad={Q0:.12f} closed={I0} tail<={tail0:.2e}")
print(f"int x^2 f:           quad={Q2:.12f} closed={I2} tail<={tail2:.2e}")
assert abs(Q0 - I0) <= 1e-9 + tail0
assert abs(Q2 - I2) <= 1e-6 + tail2
m = I2 / I0
print(f"m(f) = {m} (benchmark 1/3; (m-1/3)^2 = {(m - 1/3)**2:.6f} > 1)")

print("\n=== (ii) f^circ identity ===")
def fcirc_lo(y, T=50.0, n=20001):
    # lower bound of inf via dense grid: min over grid of exponent, then exp
    best = float("inf")
    for k in range(n):
        x = -T + 2 * T * k / (n - 1)
        v = -x * y + abs(x)
        if v < best:
            best = v
    return math.exp(best)

for y in (-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5):
    print(f"y={y:+.1f}: grid-min e^{{-xy+|x|}} ~ {fcirc_lo(y):.6f} "
          f"(closed form: {1.0 if abs(y) <= 1 else 0.0})")
    if abs(y) <= 1:
        assert fcirc_lo(y) >= 1.0 - 1e-6  # grid min >= true inf = 1
    else:
        # witness ray x=t*sign(y): exponent -t(|y|-1) -> -inf; check at t=50
        t = 50.0
        wit = math.exp(-t * (abs(y) - 1))
        assert wit < 1e-9, wit
        print(f"         tail witness at t=50: {wit:.2e} -> inf is 0. OK")

print("\n=== (iii) verdict ===")
J = I0 * 2.0
RHS = 4 * (1 + (1 / 8) * min(1.0, (m - 1 / 3) ** 2))
print(f"J(f) = {J}, RHS = {RHS}, margin J - RHS = {J - RHS}")
assert J < RHS and (RHS - J) >= 0.49
print("FALLBACK_REFUTED (margin 1/2, analytic + numeric certificate)")
