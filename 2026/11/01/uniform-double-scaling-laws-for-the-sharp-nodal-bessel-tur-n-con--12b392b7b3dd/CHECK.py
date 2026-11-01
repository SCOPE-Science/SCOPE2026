"""Supplementary numerical and exact-coefficient checks for the accompanying theorem.

Run with Python 3 and SciPy; no finite collection of examples establishes the
uniform theorem. The mathematical proof uses differentiated Debye expansions.
"""
from fractions import Fraction
from math import acos, pi, sqrt
from scipy.optimize import brentq
from scipy.special import jv, jvp


def eta(t):
    return sqrt(t * t - 1) - acos(1 / t)


def coefficients(t):
    d = -t * (9 * t * t + 22) / (24 * (t * t - 1) ** 2)
    c = -(9 * t * t + 10) / (12 * t * t * (t * t - 1) ** 2)
    return d, c


def stationary_derivative(nu, x):
    ratio = jvp(nu, x) / jv(nu, x)
    riccati = -ratio**2 - ratio / x - 1 + nu**2 / x**2
    return 2 * ratio * riccati + 2 * nu**2 / x**3


assert Fraction(-2 * (9 * 4 + 22), 24 * 9) == Fraction(-29, 54)
assert Fraction(-(9 * 4 + 10), 12 * 4 * 9) == Fraction(-23, 216)
assert Fraction(2, 8) * Fraction(-29, 54) + Fraction(1, 36) == Fraction(-23, 216)

checks = 3
for nu, n in [(40, 20), (80, 40), (80.7, 40), (120.5, 60), (80, 8), (80, 80)]:
    t = brentq(lambda tt: eta(tt) - pi * (n + 0.25) / nu, 1.000001, 20)
    d, c = coefficients(t)
    # Phase-center proximity follows analytically from the theorem.
    x = brentq(lambda xx: stationary_derivative(nu, xx), nu * t - 1.0, nu * t + 1.0)
    ratio = jvp(nu, x) / jv(nu, x)
    beta = 1 + ratio * ratio - nu * nu / (x * x)
    d_actual = nu * nu * (x / nu - t)
    c_actual = nu * nu * (beta - (1 - 1 / (t * t)))
    assert abs(d_actual - d) < 3e-3, (nu, n, d_actual, d)
    assert abs(c_actual - c) < 3e-3, (nu, n, c_actual, c)
    assert 0 < beta < 1, (nu, n, beta)
    checks += 3

print(f"CHECK_OK {checks}")
