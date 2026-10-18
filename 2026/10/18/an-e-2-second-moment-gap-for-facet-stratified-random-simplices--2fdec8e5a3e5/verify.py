"""Exact finite checks for facet-stratified random simplex volume moments.

This script is supplementary: the theorem is proven symbolically for all n.
"""
from itertools import permutations
from fractions import Fraction
from math import factorial


def parity(permutation):
    inversions = sum(permutation[i] > permutation[j]
                     for i in range(len(permutation))
                     for j in range(i + 1, len(permutation)))
    return -1 if inversions % 2 else 1


def signed_pair_sum(n):
    derangements = [p for p in permutations(range(n))
                    if all(p[i] != i for i in range(n))]
    signs = [parity(p) for p in derangements]
    total = 0
    for i, p in enumerate(derangements):
        for j, q in enumerate(derangements):
            fixed = sum(p[k] == q[k] for k in range(n))
            total += signs[i] * signs[j] * (1 << fixed)
    return total, len(derangements), set(signs)


def main():
    for n in range(2, 8):
        sum_value, count, parities = signed_pair_sum(n)
        expected = n * factorial(n)
        assert sum_value == expected, (n, sum_value, expected)
        second = Fraction(sum_value, (n * (n - 1)) ** n)
        formula_second = Fraction(factorial(n), n ** (n - 1) * (n - 1) ** n)
        assert second == formula_second
        first = Fraction((-1) ** (n - 1), (n - 1) ** (n - 1))
        interior = Fraction(factorial(n), n ** n * (n + 1) ** (n - 1))
        amplification = second / interior
        assert amplification == Fraction(n * (n + 1) ** (n - 1), (n - 1) ** n)
        assert (len(parities) == 2) == (n >= 4)
        print(f'n={n} derangements={count} signed_sum={sum_value} '
              f'mean={first} square={second} interior_square={interior} '
              f'amplification={amplification} orientation_signs={sorted(parities)}')
    print('PASS: all exact enumerations and independent formulas for n=2..7.')


if __name__ == '__main__':
    main()
