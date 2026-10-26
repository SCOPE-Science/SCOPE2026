"""Exact finite consistency tests for cubic moment-curve power-sum fibres.

Run using Python 3: python verify.py
This finite checker is illustrative; the theorem is proved for all p>3
using Newton identities, Vandermonde rank and the Chinese remainder theorem.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def moment_collisions(modulus: int) -> int:
    points = [(t, pow(t, 2, modulus), pow(t, 3, modulus))
              for t in range(modulus)]
    fibers = Counter()
    for a in points:
        for b in points:
            ab = tuple((a[k] + b[k]) % modulus for k in range(3))
            for c in points:
                fiber = tuple((ab[k] + c[k]) % modulus for k in range(3))
                fibers[fiber] += 1
    return sum(m * m for m in fibers.values())


def prime_formula(p: int) -> int:
    return p * (6 * p * p - 9 * p + 4)


def prime_square_formula(p: int) -> int:
    return 16 * p**6 - 27 * p**5 + 12 * p**4


def by_rank_formula(p: int) -> int:
    return (6 * p * (p - 1) * (p - 2) * p**3
            + 9 * p * (p - 1) * p**4 + p * p**5)


if __name__ == '__main__':
    for p in (5, 7):
        for N, target in ((p, prime_formula(p)),
                          (p * p, prime_square_formula(p))):
            observed = moment_collisions(N)
            print(f'modulus={N} collisions={observed}, expected={target}')
            assert observed == target
        assert prime_square_formula(p) == by_rank_formula(p)
        factor = Fraction(prime_square_formula(p), p**6)
        assert factor == 16 - Fraction(27, p) + Fraction(12, p * p)
    # Independent CRT multiplicativity test for the 5*7 modulus.
    modulus = 35
    observed = moment_collisions(modulus)
    expected = prime_formula(5) * prime_formula(7)
    print(f'modulus={modulus} collisions={observed}, CRT={expected}')
    assert observed == expected
    print('All finite consistency checks passed.')
