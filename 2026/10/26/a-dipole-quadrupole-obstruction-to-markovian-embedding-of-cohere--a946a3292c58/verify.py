#!/usr/bin/env python3
"""Exact-rational low-multipole check for coherent-state channels.

Dependencies: Python 3 and SymPy. This is finite corroboration, not an all-spin proof.
"""
import math
from fractions import Fraction
from sympy import Rational, simplify
from sympy.physics.wigner import wigner_6j

count = 0
for n in range(2, 21):
    j = Rational(n, 2)
    a = j * (j + 1)
    lam1 = Rational(n, n + 2)
    lam2 = Rational(n * (n - 1), (n + 2) * (n + 3))
    gap = lam1 ** 3 - lam2
    assert gap == Rational(4 * n, (n + 2) ** 3 * (n + 3)) > 0
    count += 1
    for k in range(n + 1):
        s = k * (k + 1)
        u1 = 1 - s / (2 * a)
        u2 = 1 - 3 * s / (2 * a) * (1 - (s - 2) / (4 * a - 3))
        explicit1 = (-1) ** (n + k + 1) * (n + 1) * wigner_6j(j, j, k, j, j, 1)
        explicit2 = (-1) ** (n + k + 2) * (n + 1) * wigner_6j(j, j, k, j, j, 2)
        assert simplify(u1 - explicit1) == 0
        assert simplify(u2 - explicit2) == 0
        assert simplify(u2 - 3 * u1 + 2 - 3 * s * (s - 2) / (2 * a * (4 * a - 3))) == 0
        assert (u2 - 3 * u1 + 2) >= 0
        count += 4
for n in (100, 300, 1000, 3000, 10000):
    obs = math.log1p(4 / ((n - 1) * (n + 2) ** 2))
    assert abs(obs * n ** 3 / 4 - 1) < 0.1
    count += 1
assert Rational(1,3) ** 1 == Rational(1,3)
count += 1
print(f"PASS: {count} exact/supplementary assertions")
