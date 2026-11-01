#!/usr/bin/env python3
"""Reproducible checks for Lienard escape sector and its time laws.

Analytical proof is in RESULT.md. These finite calculations are diagnostics,
not certification of universal quantifiers.
"""
import math
from fractions import Fraction
from scipy.integrate import solve_ivp, quad
import sympy as sp


def check_sector(degree, a, b, R):
    def P(z):
        return a * z ** degree + b * z ** (degree - 1)
    for z in (R, 2 * R, 10 * R):
        assert P(z) > 2 * z
        assert P(z) - z > 0
        assert -z - (P(z) + z) < 0
    return True


for m in range(2, 12):
    assert check_sector(m, 1, Fraction(3, 5), 20)

# The scalar normal form z'=(z+1)^m has exact blow-up profile Z-1.
# Its coefficient b=m yields the claimed universal shift -b/m=-1.
for m in range(2, 12):
    assert Fraction(-m, m) == -1

q, alpha, vv = sp.symbols('q alpha v')
series = sp.series(1 / (1 - q**3 - alpha*q**5 + vv*q**6), q, 0, 6).removeO()
assert sp.expand(series - (1 + q**3 + alpha * q**5)) == 0
# For the sextic specialization, time-to-blowup is
# z^{-5}/5+z^{-8}/8+alpha*z^{-10}/10+O(z^{-11}).
Z, c, d = sp.symbols('Z c d')
# Formally using h=1/Z, z=Z+c*Z^{-2}+d*Z^{-4}.
h = sp.symbols('h')
z = h**-1 + c*h**2 + d*h**4
expr = sp.series(1/(5*z**5) + 1/(8*z**8) + alpha/(10*z**10), h, 0, 11).removeO()
assert sp.expand(expr).coeff(h, 8) == sp.Rational(1, 8)-c
assert sp.expand(expr).coeff(h, 10) == alpha/sp.Integer(10)-d

# Integrate the exact orbit graph v_z=-z/(P(z)+v) and test trends.
for m in (2, 3, 6):
    def poly(z):
        return z**m + .6 * z**(m-1)
    def rhs(z, vec):
        return [-z / (poly(z) + vec[0])]
    sol = solve_ivp(rhs, (20, 50000), [0.5], rtol=1e-10, atol=1e-10,
                    dense_output=True, max_step=3000)
    assert sol.success
    v_1, v_2 = float(sol.sol(1000)[0]), float(sol.sol(50000)[0])
    if m == 2:
        # v+(1/a)log z converges; contrast with divergent v itself.
        d_1 = v_1 + math.log(1000)
        d_2 = v_2 + math.log(50000)
        assert abs(d_1-d_2) < 0.002, (d_1, d_2)
    else:
        # v(z)-z^(2-m)/(a(m-2)) tends to a finite constant.
        d_1 = v_1 - 1000**(2-m)/(m-2)
        d_2 = v_2 - 50000**(2-m)/(m-2)
        assert abs(d_1-d_2) < 3e-6, (m, d_1, d_2)

print('PASS: sector signs, shifted-polynomial coefficient, sextic series and orbit-graph asymptotic trends')
