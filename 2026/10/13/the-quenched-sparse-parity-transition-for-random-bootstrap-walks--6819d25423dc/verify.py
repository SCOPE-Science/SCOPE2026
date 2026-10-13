"""Direct finite-parameter checks for sparse inclusion-induced bootstrap walks.

The limiting statements require the separate analytical argument; this script
checks the exact parity identities and conditional moment calculations only.
Run with Python 3.10+; uses the standard library exclusively.
"""
from fractions import Fraction
from itertools import product
from math import comb

checks = 0


def r_param(n, numerator, denominator):
    return Fraction(1, 2 ** (1 + (numerator * n) // denominator))


def parity_mean_direct(r, m):
    # Direct probability recurrence, independent of the closed-form formula.
    even, odd = Fraction(1), Fraction(0)
    for _ in range(m):
        even, odd = even * (1 - r) + odd * r, odd * (1 - r) + even * r
    return even - odd, even, odd


for num, den in [(0, 1), (1, 4), (1, 2), (3, 4), (1, 1)]:
    for n in range(1, 7):
        r = r_param(n, num, den)
        for negatives in range(n + 1):
            m = 2 ** negatives
            mean, even, odd = parity_mean_direct(r, m)
            closed = (1 - 2 * r) ** m
            assert mean == closed
            assert even == (1 + closed) / 2
            assert odd == (1 - closed) / 2
            assert Fraction(0) <= odd <= Fraction(1)
            checks += 4

# Enumerate all paths and verify that the exact parity expectation depends
# only on the number of negative increments and follows the binomial mixture.
for num, den in [(0, 1), (1, 2), (3, 4)]:
    for n in range(1, 9):
        r = r_param(n, num, den)
        direct = Fraction(0)
        for increments in product((-1, 1), repeat=n):
            negatives = increments.count(-1)
            direct += (1 - 2 * r) ** (2 ** negatives)
        direct /= 2 ** n
        mixture = sum((Fraction(comb(n, k), 2 ** n)
                       * (1 - 2 * r) ** (2 ** k))
                      for k in range(n + 1))
        assert direct == mixture
        checks += 1

# Independently enumerate small Bernoulli coefficient configurations.
for r in [Fraction(1, 2), Fraction(1, 4), Fraction(1, 8)]:
    for negatives in range(0, 4):
        m = 2 ** negatives
        direct = Fraction(0)
        for bits in product((0, 1), repeat=m):
            b = sum(bits)
            direct += (-1 if b % 2 else 1) * r ** b * (1 - r) ** (m - b)
        assert direct == (1 - 2 * r) ** m
        checks += 1

# Exact binary increment covariance given a prefix's negative count.
for num, den in [(0, 1), (1, 2), (3, 4), (1, 1)]:
    for n in range(1, 7):
        r = r_param(n, num, den)
        for negatives in range(n + 1):
            m = 2 ** negatives
            _, even, odd = parity_mean_direct(r, m)
            # Condition on prefix: the next fresh fair increment takes values
            # +/-1 and the reused one is parity * fresh increment.
            exy = sum(Fraction(1, 2) * prob * ((xi) * (z * xi))
                      for z, prob in [(1, even), (-1, odd)]
                      for xi in (-1, 1))
            assert exy == (1 - 2 * r) ** m
            checks += 1

print('VERIFY_OK:', checks, 'exact rational parity / covariance assertions')
