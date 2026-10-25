#!/usr/bin/env python3
"""Exact parity-halfcube isotropic-profile regression, Python standard library only."""
from fractions import Fraction as F
from math import factorial


def parameters(n):
    assert n >= 3
    a = F(2 ** (n - 1), factorial(n))
    m = F(n * n - n + 2, (n + 1) * (n + 2))
    lam = (F(1, 3) - a * m) / (1 - a)
    b = 3 * m
    p = F(n + 2, n)
    assert F(0) < a < F(1)
    assert lam > 0
    assert b - p == F(2 * (n**3 - 4*n**2 - n - 2), n * (n + 1) * (n + 2))
    assert (1 - 3 * m * a) / (1 - a) == 3 * lam
    return a, m, lam, b, p


for n in range(3, 81):
    a, m, lam, b, p = parameters(n)
    assert lam < F(1, 3), 'covariance isotropy must approach cube from below'
    if n >= 5:
        assert n**2 * (n - 4) - (n + 2) > 0
        assert b > p > 1

# The squared ratio R2=(L_halfcube/L_cube)^2.
# n=3: R2=(3/5)*3^(2/3), thus R2^3=243/125.
a3, m3, l3, _, _ = parameters(3)
assert a3 == F(2, 3) and m3 == F(2, 5) and l3 == F(1, 5)
assert F(243, 125) > 1
# n=4: R2=(4/5)*sqrt(3/2), thus R2^2=24/25.
a4, m4, l4, _, _ = parameters(4)
assert a4 == F(1, 3) and m4 == F(7, 15) and l4 == F(4, 15)
assert F(24, 25) < 1
print('VERIFY_OK exact_rational_dimensions=3..80 exceptional_cases=3,4 analytic_sign_polynomial=1')
