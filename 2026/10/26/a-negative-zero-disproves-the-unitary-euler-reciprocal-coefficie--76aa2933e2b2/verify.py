#!/usr/bin/env python3
"""Exact-rational checks for a Lambert-series negative-zero certificate."""
from fractions import Fraction

partial = sum((Fraction(3, 2 ** (j + 1) + 3) for j in range(1, 7)), Fraction(0))
assert partial == Fraction(65011734, 64203755)
assert partial - 1 == Fraction(807979, 64203755) > 0

# An independent bound: the positive even partial sum of the decreasing
# alternating Taylor series at -3/2 exceeds its infinite sum.
truncated = Fraction(1)
for n in range(1, 11):
    truncated += Fraction((-3) ** n, (2 ** n) * (2 ** n - 1))
assert truncated == Fraction(-22519890247, 1926184494080) < 0

# Formal power-series inversion confirms the coefficients quoted in the source.
a = [Fraction(1)] + [Fraction(1, 2 ** n - 1) for n in range(1, 5)]
b = [Fraction(1)]
for n in range(1, 5):
    b.append(-sum((a[k] * b[n-k] for k in range(1, n + 1)), Fraction(0)))
assert b == [Fraction(1), Fraction(-1), Fraction(2,3), Fraction(-10,21), Fraction(104,315)]
print('CERTIFICATE_OK six_term_gap=807979/64203755 taylor_upper=-22519890247/1926184494080 published_coefficients=5')
