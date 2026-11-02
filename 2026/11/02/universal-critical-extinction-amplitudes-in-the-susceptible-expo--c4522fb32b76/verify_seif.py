"""Symbolic identities and finite-time diagnostics for an SEIF critical profile."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

s, e, i, f, r, b1, bf, g, m, rho, om = sp.symbols(
    "s e i f r b1 bf g m rho om", positive=True
)
force = b1 * i + bf * f
flow = (
    r * (s + e) * (1 - s - e - i) - s * force,
    s * force - g * e,
    g * e - m * i,
    rho * i - om * f,
)
weighted = e + i + bf * f / om
identity = sp.factor(
    sum(sp.diff(weighted, x) * dx for x, dx in zip((s, e, i, f), flow))
    + (1 - s) * force
    - (b1 + bf * rho / om - m) * i
)
assert identity == 0
A = sp.Matrix([[-g, b1, bf], [g, -m, 0], [0, rho, -om]])
v = sp.Matrix([m / g, 1, rho / om])
ell = sp.Matrix([[1, 1, bf / om]])
Ac = A.subs(b1, m - bf * rho / om)
assert all(sp.simplify(t) == 0 for t in Ac * v)
assert all(sp.simplify(t) == 0 for t in ell * Ac)
assert sp.simplify((ell * v)[0] - (1 + m / g + bf * rho / om ** 2)) == 0
print("PASS: exact drift and both critical eigenvectors")

cases = [
    (0.11, 0.5, 0.1, 0.4, 0.01, 0.5),
    (0.5, 0.7, 0.2, 1.0, 0.4, 0.1),
    (1.3, 0.8, 0.4, 0.25, 0.3, 0.25),
]
for R, G, M, O, P, BF in cases:
    B1 = M - BF * P / O
    assert B1 >= 0
    D = 1 + M / G + BF * P / O ** 2
    K = 1 + M / G + M / R
    target_i = D / (M * K)
    target_u = D / M

    def vector_field(_, z):
        S, E, I, F = z
        infection = S * (B1 * I + BF * F)
        return [R * (S + E) * (1 - S - E - I) - infection,
                infection - G * E, G * E - M * I, P * I - O * F]

    for initial in ([0.8, 0.1, 0.05, 0.04], [0.15, 0.4, 0.25, 0.1]):
        solution = solve_ivp(vector_field, (0, 200_000), initial,
                             method="DOP853", rtol=1e-10, atol=1e-12)
        assert solution.success
        S, E, I, F = solution.y[:, -1]
        assert math.isclose(200_000 * I, target_i, rel_tol=0.003)
        assert math.isclose(200_000 * (1 - S), target_u, rel_tol=0.003)
        print("PASS: finite-time critical profile", (R, G, M, O, P, BF),
              "tI", 200_000 * I, "theory", target_i)
print("All symbolic and finite-time checks completed.")
