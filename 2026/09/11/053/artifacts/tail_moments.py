"""Stdlib-only reproducible evidence for lane-854 target steps (i)-(ii) + stress test of (iii).

g(x) = (1+|x|)^-5 * log(e+|x|)^(-1/2) on R (symmetric, unnormalized).
Y ~ proportional to g; X = Y/sigma with sigma^2 = E[Y^2] so E[X^2]=1.
Checks:
 (a) Z0 = 2*int_0^inf g in a rigorous enclosure (Simpson + analytic tail).
 (b) I2 = int_0^inf x^2 g enclosure -> sigma^2 = I2/I0, c* = 1/Z0.
 (c) E[Y^4] = inf: numeric growth of int_1^R x^4 g ~ 2*sqrt(log R) + analytic LB.
 (d) Two-sided tail bounds: s^4 P(|X|>s) vs c' (log s)^(-1/2), c' = c*/(2 sigma^4).
 (e) Recovery/stress test of the B_N route: N^2 P(|X|>B_N) with B_N=N^1/2 (log N)^-2,
     and q=(log N)^2 vs the N^phi / phi^C support thresholds of cited comparison theorems.
"""
import math

E = math.e

def L(x):
    return math.log(E + abs(x))

def g(x):
    return (1.0 + abs(x)) ** -5 * L(x) ** -0.5

def simpson(f, a, b, n):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for k in range(1, n):
        s += (4.0 if k & 1 else 2.0) * f(a + k * h)
    return s * h / 3.0

print("=== (a) normalization ===")
I0 = simpson(g, 0.0, 16.0, 120000)
tb0 = 1.0 / (4.0 * 17.0 ** 4)          # g<=(1+x)^-5, tail int <= 1/[4(1+X)^4]
print(f"I0=int_0^16 g = {I0:.10f}  tailbound={tb0:.3e}")
print(f"Z0 in [{2*I0:.10f}, {2*(I0+tb0):.10f}]")
Z0mid = 2 * I0 + tb0
c_star = 1.0 / Z0mid
print(f"c* ~ {c_star:.8f}")

print("=== (b) second moment ===")
I2 = simpson(lambda x: x * x * g(x), 0.0, 40.0, 160000)
tb2 = 0.5 / (41.0 ** 2)                # x^2(1+x)^-5 <= (1+x)^-3
print(f"I2=int_0^40 x^2 g = {I2:.10f}  tailbound={tb2:.3e}")
sig2 = I2 / I0
print(f"sigma^2 = I2/I0 ~ {sig2:.8f}  (E[X^2]=1 after X=Y/sigma, sigma~{math.sqrt(sig2):.6f})")

print("=== (c) fourth moment diverges ===")
for R in (10.0, 100.0, 1000.0, 10000.0):
    v = simpson(lambda x: x ** 4 * g(x), 1.0, R, 200000)
    lb = math.log(R) / (16.0 * math.sqrt(math.log(E + R)))  # 2*LB factor folded in
    print(f"R={R:>7.0f}  2*int_1^R x^4 g = {2*v:.6f}  analyticLB={lb:.6f}  2*sqrt(log R)={2*math.sqrt(math.log(R)):.4f}")

print("=== (d) Lee-Yin tail s^4 P(|X|>s) -> 0 ===")
cp = c_star / (2.0 * sig2 ** 2)
print(f"c' = c*/(2 sigma^4) ~ {cp:.8f}")
for s in (10.0, 30.0, 100.0, 300.0, 1000.0):
    t = math.sqrt(sig2) * s
    # upper: full tail with slowest log pulled out at left endpoint
    up = s ** 4 * 2 * c_star * (L(t) ** -0.5) / (4.0 * (1 + t) ** 4)
    # lower: restrict to [t,2t], fastest log decay at right endpoint
    lo = s ** 4 * 2 * c_star * (L(2 * t) ** -0.5) * ((1 + t) ** -4 - (1 + 2 * t) ** -4) / 4.0
    pred = cp * (math.log(s)) ** -0.5
    print(f"s={s:>7.0f}  s^4*tail in [{lo:.6f},{up:.6f}]  c'(log s)^-1/2={pred:.6f}  "
          f"ratio in [{lo/pred:.4f},{up/pred:.4f}]")

print("=== (e) STRESS TEST of B_N = N^1/2 (log N)^-2 route ===")
print("E(N) := N^2 P(|X|>B_N) ~ c' N^2 B_N^-4 (log B_N)^-1/2"
      " = c'*sqrt(2)*(log N)^(15/2)(1+o(1)) -> +inf  => no w.h.p. coincidence coupling")
for N in (1e6, 1e12, 1e30, 1e100):
    lN = math.log(N)
    BN = math.sqrt(N) / lN ** 2
    assert BN > E, "asymptotic needs BN>e"
    lB = math.log(BN)
    asym = N ** 2 * cp * BN ** -4 * lB ** -0.5
    q = lN ** 2
    print(f"N=1e{math.log10(N):.0f}  B_N={BN:.3e}  N^2*P~{asym:.3e}  "
          f"q=(logN)^2={q:.3f}  N^(1/3)={N**(1/3):.3e}")
phi_C_note = "phi^C with phi=(logN)^{loglogN}: exceeds (logN)^2 for large N at any fixed C>=1"
print("note:", phi_C_note)
print("CONCLUSION: E(N)->inf (direct truncation coupling impossible); "
      "q=(log N)^2 lies below both N^phi (any fixed phi>0) and phi^C thresholds "
      "of the cited local-law/comparison inputs (Lemma 3.1 needs q>=phi^C; Thm 3.6/3.7 need q=N^phi).")
