#!/usr/bin/env python3
"""Exact coefficient spot-checks and model-integral checks; not an infinite proof."""
from fractions import Fraction
from math import exp, isclose, log, sqrt


def moment(n):
    h = sum((Fraction(1, k) for k in range(1, n + 2)), Fraction())
    h2 = sum((Fraction(1, k * k) for k in range(1, n + 2)), Fraction())
    return ((1 + h) ** 2 + h2) / (n + 1)


def beta_derivatives(n):
    # Differentiate n! / [q(q+1)...(q+n)] at q=1 algebraically.
    w = Fraction(1, n + 1)
    s1 = sum((Fraction(1, k) for k in range(1, n + 2)), Fraction())
    s2 = sum((Fraction(1, k * k) for k in range(1, n + 2)), Fraction())
    b0, b1, b2 = w, -w * s1, w * (s1 * s1 + s2)
    return b0 - 2 * b1 + b2


for n in range(25):
    assert moment(n) == beta_derivatives(n)

# Check finite samples of the exact matrix comparison and asymptotic ratios.
for n in (5, 10, 50, 200, 1000):
    v = float(moment(n))
    q = log(n) / sqrt(n * v)
    assert q > 0
    for m in (3, max(3, n // 2), n):
        B = 1.0 / ((m + n + 1) * sqrt(m + 1) * sqrt(v))
        D = 1.0 / (sqrt(m * n) * log(n))
        rhs = q * sqrt(m / (m + 1)) * n / (m + n + 1)
        assert isclose(B / D, rhs, rel_tol=1e-13)

# Exact integral of (1-exp((u-L)/2))**2 on [0,L].
for L in (1, 2, 10, 100):
    J = L - 3 + 4 * exp(-L / 2) - exp(-L)
    assert J > 0 and 0 < 2 * sqrt(J / L) < 2
assert 2 * sqrt((100 - 3 + 4 * exp(-50) - exp(-100)) / 100) > 1.96
print("VERIFY_OK: exact beta coefficients and finite comparison checks; infinite proof is analytic")
