"""Verify the T-uniform 1/N disproof: symbolic master-equation check,
closed-form error growth, and Monte Carlo confirmation."""
import numpy as np
import sympy as sp

# ---- 1. Symbolic check of explicit master solution ----
t, T, m1 = sp.symbols('t T m1', real=True)
tau = T - t
delta = m1 - sp.Rational(1, 2)
phi = (1 - sp.exp(-4 * tau)) / 4
U1 = tau / 2 + delta * phi
U2 = tau / 2 - delta * phi
F1 = m1
F2 = 1 - m1
# Master eq (uncontrolled, rate 1 both ways):
# d_t U(x) + [U(3-x)-U(x)] + b(m1)*d_{m1}U(x) + F(x,m) = 0, b=1-2*m1
b = 1 - 2 * m1
for Ux, Fx, x in [(U1, F1, 1), (U2, F2, 2)]:
    other = U2 if x == 1 else U1
    residual = sp.diff(Ux, t) + (other - Ux) + b * sp.diff(Ux, m1) + Fx
    r = sp.simplify(residual)
    assert r == 0, (x, r)
    print(f"x={x}: master residual = {r}, terminal U(T)={sp.simplify(Ux.subs(t, T))}")
print("symbolic master-equation check PASSED")

# ---- 2. Closed-form scaled error ----
def scaled_error(N, Tval):
    return (Tval - (1 - np.exp(-4 * Tval)) / 4) / 2  # N * (V-U) at t=0

print("\nN*error (N=2 fixed, t=0, config (1,2)):")
for Tval in [1, 2, 5, 10, 20, 50, 100]:
    print(f"  T={Tval:>6}: N*err = {scaled_error(2, Tval):.6f}  (bound T/2-1/8 = {Tval/2-1/8:.6f})")
    assert scaled_error(2, Tval) >= Tval / 2 - 1 / 8 - 1e-12
# exceed any C: e.g. C=10 needs T>=21
C = 10.0
Tneed = 2 * C + 1
assert scaled_error(2, Tneed) > C
print(f"exceeds C={C} at T={Tneed}: N*err={scaled_error(2, Tneed):.6f} PASSED")

# ---- 3. Monte Carlo confirmation of the covariance formula ----
rng = np.random.default_rng(0)
N, Tval, npaths = 2, 3.0, 400000
dt = 0.002
nsteps = int(Tval / dt)
# initial config (1,2) encoded as 1/0; player 1 starts at 1
X = np.zeros((npaths, N), dtype=int)
X[:, 0] = 1
X[:, 1] = 0
acc_V = np.zeros(npaths)
acc_Udet = np.zeros(npaths)
m10 = 0.5
for k in range(nsteps):
    mN1 = X.mean(axis=1)
    acc_V += (X[:, 0] * mN1 + (1 - X[:, 0]) * (1 - mN1)) * dt
    s = k * dt
    m1det = 0.5 + (m10 - 0.5) * np.exp(-2 * s)
    p1 = 0.5 + 0.5 * np.exp(-2 * s)
    # mean-field integrand for player starting at 1: p*m + (1-p)*(1-m)
    acc_Udet += (p1 * m1det + (1 - p1) * (1 - m1det)) * dt
    jump = rng.random((npaths, N)) < (1 - np.exp(-dt))  # rate-1 jumps
    X[jump] = 1 - X[jump]
Vmc = acc_V.mean()
# exact values
exact_gap = (Tval - (1 - np.exp(-4 * Tval)) / 4) / (2 * N)
# exact U for x=1, m0=1/2: tau/2 (delta=0)
Uexact = Tval / 2
Vexact = Uexact + exact_gap
print(f"\nMonte Carlo: Vmc={Vmc:.5f} Vexact={Vexact:.5f} Uexact={Uexact:.5f}")
print(f"  MC gap={Vmc-Uexact:.5f} exact gap={exact_gap:.5f}")
assert abs(Vmc - Vexact) < 0.02
print("Monte Carlo check PASSED")
print("\nALL CHECKS PASSED")
