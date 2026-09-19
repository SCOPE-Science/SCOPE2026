"""Scientific checks for the quadratic anisotropy-slaving formulas.

The script verifies the closed-form coefficient identities symbolically and
integrates one covariance eigenvalue system as a numerical sanity check.
"""
from math import comb, factorial
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

# Generic coefficient identities.  Write b = C(d-2,n-2) and reduce all
# neighboring binomial coefficients to rational multiples of b.
d, n, L, c, b = sp.symbols("d n L c b", positive=True)
A = (d - 1) * b / (n - 1)          # C(d-1,n-1)
P = (d - n) * b / (n - 1)          # C(d-2,n-1)
D = d * (d - 1) * b / (n * (n - 1))  # C(d,n)

alpha_perp = 4 * c * P * L ** (n - 1)
alpha_parallel = 4 * c * n * A * L ** (n - 1)
B = 2 * c * n * b * L ** (n - 2) / d

den = sp.factor(alpha_parallel - 2 * alpha_perp)
C_recoil = sp.factor(B / den)
C_expected = n * (n - 1) / (2 * d * L * (d * (n - 2) + n))
assert sp.simplify(C_recoil - C_expected) == 0

K_from_expansion = sp.factor(D * n * L ** (n - 1) * C_recoil - sp.Rational(1, 2) * b * L ** (n - 2))
K_expected = b * L ** (n - 2) * (d - n) / (d * (n - 2) + n)
assert sp.simplify(K_from_expansion - K_expected) == 0

rate_gap_factor = sp.factor((alpha_parallel - 2 * alpha_perp) / (4 * c * b * L ** (n - 1)))
assert sp.simplify(rate_gap_factor - (d * (n - 2) + n) / (n - 1)) == 0

# Check the centered elementary-symmetric expansion in several finite cases.
for dd in range(3, 7):
    xs = sp.symbols(f"x0:{dd}")
    r = sp.symbols("r")
    centered = list(xs[:-1]) + [-sum(xs[:-1])]
    for nn in range(2, dd):
        lhs = sum(sp.prod(r + centered[i] for i in I)
                  for I in __import__('itertools').combinations(range(dd), nn))
        e2 = sum(centered[i] * centered[j]
                 for i in range(dd) for j in range(i + 1, dd))
        quad = sp.binomial(dd, nn) * r ** nn + sp.binomial(dd - 2, nn - 2) * r ** (nn - 2) * e2
        # Difference has total centered degree >= 3 (or vanishes for n=2).
        poly = sp.Poly(sp.expand(lhs - quad), *xs[:-1])
        if poly.as_dict():
            assert min(sum(mon) for mon in poly.as_dict()) >= 3

# Numerical sanity check: d=5, n=4, gamma=1.
dd, nn, gamma = 5, 4, 1.0
cn = (nn + 1) / factorial(nn)
lstar = (gamma * factorial(nn) / (2 * (nn + 1) * comb(dd - 1, nn - 1))) ** (1 / nn)
ap = 4 * cn * comb(dd - 2, nn - 1) * lstar ** (nn - 1)
al = 4 * cn * nn * comb(dd - 1, nn - 1) * lstar ** (nn - 1)
Cpred = nn * (nn - 1) / (2 * dd * lstar * (dd * (nn - 2) + nn))
Kpred = comb(dd - 2, nn - 2) * lstar ** (nn - 2) * (dd - nn) / (dd * (nn - 2) + nn)

def elementary(vals, k):
    total = 0.0
    for I in __import__('itertools').combinations(range(len(vals)), k):
        p = 1.0
        for i in I:
            p *= vals[i]
        total += p
    return total

def rhs(t, lam):
    out = np.empty(dd)
    for i in range(dd):
        rest = np.delete(lam, i)
        out[i] = -4 * cn * lam[i] * elementary(rest, nn - 1) + 2 * gamma
    return out

lam0 = np.array([1.30, 1.10, 0.95, 0.80, 0.65])
sol = solve_ivp(rhs, (0.0, 16.0), lam0, rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.02)
assert sol.success

print("symbolic_coefficient_checks=True")
print("centered_expansion_checks=True")
print(f"d={dd} n={nn} lambda_star={lstar:.15g}")
print(f"alpha_perp={ap:.15g} alpha_parallel={al:.15g} ratio={al/ap:.15g}")
print(f"predicted_recoil_ratio={Cpred:.15g}")
print(f"predicted_interaction_ratio={Kpred:.15g}")
for t in (8.0, 12.0, 16.0):
    lam = sol.sol(t)
    mean = lam.mean()
    delta = lam - mean
    s2 = float(delta @ delta)
    recoil_ratio = (mean - lstar) / s2
    en = elementary(lam, nn)
    enstar = comb(dd, nn) * lstar ** nn
    interaction_ratio = (en - enstar) / s2
    print(f"t={t:.1f} recoil_ratio={recoil_ratio:.12g} interaction_ratio={interaction_ratio:.12g} anisotropy_sq={s2:.12g}")
