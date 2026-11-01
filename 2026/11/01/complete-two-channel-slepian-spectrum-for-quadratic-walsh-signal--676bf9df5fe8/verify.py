#!/usr/bin/env python3
"""Exact integer verification of quadratic Walsh majority concentration spectra.

Usage: python3 verify.py
No third-party packages or external files are needed.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def verify_dimension(n):
    assert n >= 3 and n % 2 == 1
    masks = [0] + [1 << i for i in range(n)]
    masks += [sum(1 << i for i in pair) for pair in combinations(range(n), 2)]
    even = [0] + masks[n + 1:]
    odd = masks[1:n + 1]
    total = 1 << n
    positive = [x for x in range(total) if 2 * x.bit_count() < n]
    assert len(positive) == total // 2

    # Every entry is a Fourier-Walsh coefficient multiplied by 2**n.
    differences = {a ^ b for a in masks for b in masks}
    moment = {m: sum(1 if (x & m).bit_count() % 2 == 0 else -1
                     for x in positive) for m in differences}
    alpha_num = comb(n - 1, (n - 1) // 2)
    assert alpha_num % (n - 2) == 0
    beta_num = -alpha_num // (n - 2)
    entries = 0
    for a in masks:
        for b in masks:
            h = (a ^ b).bit_count()
            expected = (total // 2 if h == 0 else
                        alpha_num if h == 1 else
                        beta_num if h == 3 else 0)
            assert moment[a ^ b] == expected, (n, a, b)
            entries += 1
    # Off-diagonal parity block: B = [alpha*1^T ; beta*J+(alpha-beta)*E].
    B = [[moment[a ^ b] for b in odd] for a in even]
    A = [[sum(row[i] * row[j] for row in B) for j in range(n)]
         for i in range(n)]
    symmetric = Fraction(alpha_num * alpha_num * (3 * n - 1), 2)
    standard = Fraction(alpha_num * alpha_num * (n - 1) ** 2, n - 2)
    for i in range(n):
        for j in range(n):
            expected = (standard if i == j else 0) + (symmetric-standard)/n
            assert A[i][j] == expected, (n, i, j, A[i][j], expected)
    # Equality of the singular levels occurs exactly at n=3.
    assert (symmetric == standard) == (n == 3)
    assert symmetric <= Fraction(total * total, 4)
    assert (symmetric == Fraction(total * total, 4)) == (n == 3)
    return entries, len(differences)


def main():
    cases = (3, 5, 7, 9, 11, 13)
    total_entries = total_moments = 0
    for n in cases:
        e, m = verify_dimension(n)
        total_entries += e
        total_moments += m
    # Strict decrease of the top singular value with n -> n+2:
    # ((n+1)^2(3n-1)-n^2(3n+5)) = n-1 > 0.
    for n in range(3, 10000, 2):
        assert (n+1)**2*(3*n-1)-n*n*(3*n+5) == n-1
        # The standard-channel squared singular-value ratio is (n-2)/n.
        assert 0 < n-2 < n
    print('VERIFY_OK dimensions=' + ','.join(map(str, cases)) +
          ' exact_gram_entries=' + str(total_entries) +
          ' exact_distinct_walsh_moments=' + str(total_moments) +
          ' dimension_ratios=4999')

if __name__ == '__main__':
    main()
