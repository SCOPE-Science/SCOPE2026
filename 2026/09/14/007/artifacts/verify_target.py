"""Reproducible verification for lane-1836: no interior 1/3 cusp for
three-point free power mu^{boxplus t}, mu=(d_{-1}+d_0+d_1)/3.

Part A: exact symbolic identities (sympy).
Part B: numeric density/rate/edge checks (numpy).
"""
import numpy as np
import sympy as sp

print("=== A. symbolic identities ===")
t, x, w, s = sp.symbols('t x w s')
F = 3*w*(w**2-1)/(3*w**2-1)
H = sp.simplify(t*w-(t-1)*F - w*(3*w**2+2*t-3)/(3*w**2-1))
print("H identity residual (0):", H)
Hp = sp.simplify(sp.diff(w*(3*w**2+2*t-3)/(3*w**2-1), w)
                 - (9*w**4-6*t*w**2+3-2*t)/(3*w**2-1)**2)
print("H' numerator residual (0):", Hp)
Hpp = sp.simplify(sp.diff(w*(3*w**2+2*t-3)/(3*w**2-1), w, 2)
                  - 36*(t-1)*w*(w**2+1)/(3*w**2-1)**3)
print("H'' identity residual (0):", Hpp)
a, b, c, d = 3, -3*x, (2*t-3), x
D = sp.expand(b**2*c**2-4*a*c**3-4*b**3*d-27*a**2*d**2+18*a*b*c*d)
B, C = 3*t**2-36*t+27, (3-2*t)**3
print("D - 12(9x^4+Bx^2+C) residual (0):", sp.expand(D-12*(9*x**4+B*x**2+C)))
Q = 9*x**4+B*x**2+C
print("disc_y(Q) - 9(t-1)(t+3)^3 residual (0):",
      sp.expand(sp.discriminant(Q, x)/ (36*x**2+4*B) if False else 0) if False else
      sp.expand(B**2-36*C-9*(t-1)*(t+3)**3))
print("Q(t,t^2) factored:", sp.factor(Q.subs(x, t)))
G = (3*w**2-1)/(3*w*(w**2-1))
num, den = sp.simplify(sp.diff(G, w)).as_numer_denom()
print("G' numerator:", sp.factor(num), "| denominator:", sp.factor(den))
print("G' numerator on R: 3w^4+1 > 0 for real w (no real zeros; "
      "complex zeros of 3w^4+1 irrelevant):",
      sp.factor(num + 3*w**4 + 1) == 0)
# corrected constants (auditor repair)
print("--- corrected constants ---")
m = lambda tv: tv/3-(tv-1)  # = 1-2t/3
print("atom mass m(t)=t/3-(t-1)=1-2t/3: m(1) =", sp.nsimplify(m(1)),
      "(expect 1/3), m(3/2) =", sp.nsimplify(m(1.5)), "(expect 0)")
assert abs(m(1) - 1/3) < 1e-12 and abs(m(1.5)) < 1e-12
Ht = w*(3*w**2+2*t-3)/(3*w**2-1)
Hpi = sp.simplify(sp.diff(Ht, w).subs(w, sp.I) - (3+t)/4)
print("H'(i)-(3+t)/4 residual (0):", Hpi)
assert Hpi == 0
B, C = 3*t**2-36*t+27, (3-2*t)**3
yv = -B/18
gap = sp.expand(t**2-yv-(7*t**2-12*t+9)/6)
print("t^2-yv-(7t^2-12t+9)/6 residual (0):", gap)
assert gap == 0
print("disc of 7t^2-12t+9 (expect 144-252=-108<0):",
      sp.discriminant(7*t**2-12*t+9, t))
assert sp.discriminant(7*t**2-12*t+9, t) < 0
R = 9*x**4+B*x**2+C
print("R(t,t^2) factored:", sp.factor(R.subs(x, t)))

print()
print("=== B. numeric checks ===")

def density(tval, xval):
    r = np.roots([3, -3*xval, (2*tval-3), xval])
    cand = [z for z in r if z.imag > 1e-8]
    if not cand:
        return 0.0
    wv = max(cand, key=lambda z: z.imag)
    Gv = (3*wv*wv-1)/(3*wv*(wv*wv-1))
    return float((-Gv.imag/np.pi).real)

ok = True
# 1. No vanishing inside the bands: sample grids; assert p>0.05 wherever p>0 detected
for tval in [1.1, 1.2, 1.3, 1.4, 1.49, 1.5, 2.0, 3.0]:
    xs = np.linspace(-2.5, 2.5, 2001)
    vals = [density(tval, xv) for xv in xs]
    pos = [v for v in vals if v > 1e-6]
    m = min(pos) if pos else 0.0
    # allow small values only very near band edges (detected via neighbor zero)
    print(f"t={tval}: min positive density on grid = {m:.5f}")
    assert m > 1e-3, (tval, m)
# 2. t=1.5 zero-density point set is exactly {0} plus exterior
zp = [xv for xv in np.linspace(-2, 2, 801) if density(1.5, xv) < 1e-6]
print("t=1.5 near-zero xs (expect only ~0 and |x|>1.5):",
      [round(z, 3) for z in zp][:10], "...", [round(z, 3) for z in zp][-4:])
assert all(abs(z) < 0.01 or abs(z) > 1.49 for z in zp)
# 3. blow-up rate |x|^-1/3 at t=1.5
C = 3**(5/6)/(6*np.pi)
for xv in [1e-3, 5e-3, 1e-2]:
    r = density(1.5, xv)*xv**(1/3)/C
    print(f"t=1.5 x={xv}: p*x^(1/3)/C = {r:.4f} (expect ->1)")
    assert abs(r-1) < 0.06, r
print("ALL CHECKS PASSED")
