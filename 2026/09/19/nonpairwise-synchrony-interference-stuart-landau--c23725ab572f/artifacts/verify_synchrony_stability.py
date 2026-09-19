"""Symbolic checks for the synchrony-stability formulas in RESULT.md."""

import sympy as sp

th1, th2, th3, rho, xi = sp.symbols("th1 th2 th3 rho xi", real=True)
a, eps, eta = sp.symbols("a eps eta", positive=True, real=True)

# Unit-weight second-order pairwise phase term from arXiv:2609.20632v1, Eq. (8).
C1221 = sp.sin(2 * rho) + sp.sin(2 * (th2 - th1))
C1223 = sp.sin(th3 - th1 + 2 * rho) + sp.sin(2 * th2 - th3 - th1)
C1331 = sp.sin(2 * rho) + sp.sin(2 * (th3 - th1))
C1332 = sp.sin(th2 - th1 + 2 * rho) + sp.sin(2 * th3 - th2 - th1)
D1212 = sp.sin(2 * (th2 - th1) + 2 * rho)
D1213 = sp.sin(th2 + th3 - 2 * th1 + 2 * rho)
D1313 = sp.sin(2 * (th3 - th1) + 2 * rho)

f2 = (
    C1221 + C1223 + C1331 + C1332
    - D1212 - 2 * D1213 - D1313
) / (4 * a)

f_pair = sp.sin(th2 - th1 + rho) + sp.sin(th3 - th1 + rho)
f_pn = (
    sp.sin(2 * th2 - th3 - th1 + xi)
    + sp.sin(2 * th3 - th2 - th1 + xi)
)

sync = {th1: 0, th2: 0, th3: 0}


def row_derivatives(expr):
    return [sp.trigsimp(sp.diff(expr, x).subs(sync)) for x in (th1, th2, th3)]


def transverse_rate(expr):
    d = row_derivatives(expr)
    return sp.trigsimp(d[0] - d[1]), d

mixed = eps * f_pair + eps**2 * f2 + eta * f_pn
lam_mixed, d_mixed = transverse_rate(mixed)
expected_mixed = (
    -3 * eps * sp.cos(rho)
    - sp.Rational(9, 2) * eps**2 * sp.sin(rho)**2 / a
    - 3 * eta * sp.cos(xi)
)

# Engineered physical-nonpairwise phase term from Eqs. (20)--(21), unit weights.
f_engineered = (
    -sp.sin(2 * th2 - th3 - th1)
    - sp.sin(2 * th3 - th2 - th1)
    + sp.sin(th2 + th3 - 2 * th1 + 2 * rho)
)
engineered = eps * f_pair + eps**2 * f2 + eta * f_engineered
lam_engineered, d_engineered = transverse_rate(engineered)
expected_engineered = (
    -3 * eps * sp.cos(rho)
    - sp.Rational(9, 2) * eps**2 * sp.sin(rho)**2 / a
    + 6 * eta * sp.sin(rho)**2
)

checks = {
    "mixed_transverse_residual": sp.trigsimp(sp.expand_trig(lam_mixed - expected_mixed)),
    "mixed_phase_shift_row_sum": sp.trigsimp(sum(d_mixed)),
    "engineered_transverse_residual": sp.trigsimp(sp.expand_trig(lam_engineered - expected_engineered)),
    "engineered_phase_shift_row_sum": sp.trigsimp(sum(d_engineered)),
    "paper_design_residual_rate": sp.factor(lam_engineered.subs(eta, eps**2 / (4 * a))),
    "stability_neutral_design_rate": sp.factor(lam_engineered.subs(eta, 3 * eps**2 / (4 * a))),
}

assert checks["mixed_transverse_residual"] == 0
assert checks["mixed_phase_shift_row_sum"] == 0
assert checks["engineered_transverse_residual"] == 0
assert checks["engineered_phase_shift_row_sum"] == 0
assert sp.trigsimp(checks["paper_design_residual_rate"] + 3 * eps * sp.cos(rho) + 3 * eps**2 * sp.sin(rho)**2 / a) == 0
assert sp.trigsimp(checks["stability_neutral_design_rate"] + 3 * eps * sp.cos(rho)) == 0

print("mixed_transverse_rate =", lam_mixed)
print("engineered_transverse_rate =", lam_engineered)
for name, value in checks.items():
    print(f"{name} = {value}")
print("all_symbolic_checks_passed = True")
