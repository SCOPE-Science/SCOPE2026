#!/usr/bin/env python3
"""Standalone numerical/algebraic checks for the published three-point envelope."""
from fractions import Fraction
import math


def A(p):
    return p**3


def B(p):
    return (p + 1) * (p - Fraction(1, 2))**2


def int_w(p):
    return p - Fraction(1, 3)


def int_abs_w(p):
    if p <= 0:
        return Fraction(1, 3) - p
    if p <= Fraction(1, 2):
        return (1 - 3*p + 8*p**3) / 3
    return p - Fraction(1, 3)


def C(p):
    return int_abs_w(p) / 16

# Exact rational checks in all three regimes.
for p in [Fraction(-2,3), Fraction(0), Fraction(1,5), Fraction(1,3),
          Fraction(1,2), Fraction(3,4)]:
    assert int_w(p) == p - Fraction(1,3)
    if 0 < p < Fraction(1,2):
        Iplus = Fraction(4,3) * p**3
        Iminus = Fraction(4,3) * B(p)
        assert Iplus - Iminus == int_w(p)
        assert (A(p) - B(p)) / 12 == (3*p - 1) / 48
        assert (A(p) + B(p)) / 12 == C(p)

# Simpson point: center vanishes and the sharp oscillation constant is 1/162.
p_simpson = Fraction(1,3)
assert (3*p_simpson - 1) == 0
assert C(p_simpson) == Fraction(1,162)

# The centered minimax weight and constant.
p_star = 1.0 / (2.0 * math.sqrt(2.0))
C_star = (1.0 - 1.0 / math.sqrt(2.0)) / 48.0
assert abs((1 - 3*p_star + 8*p_star**3)/48.0 - C_star) < 1e-15
assert C_star < 1.0/162.0

# A dense numerical check confirms the global minimum of the piecewise C(p).
def C_float(p):
    if p <= 0:
        return (1 - 3*p)/48.0
    if p <= 0.5:
        return (1 - 3*p + 8*p**3)/48.0
    return (3*p - 1)/48.0

lo, hi, n = -2.0, 2.0, 400000
best_p, best_c = None, float('inf')
for k in range(n + 1):
    p = lo + (hi-lo)*k/n
    c = C_float(p)
    if c < best_c:
        best_p, best_c = p, c
assert abs(best_p - p_star) < 2e-5
assert abs(best_c - C_star) < 1e-10

print('p_star =', format(p_star, '.15f'))
print('C_star =', format(C_star, '.15f'))
print('C_Simpson =', format(1.0/162.0, '.15f'))
print('all checks passed')
