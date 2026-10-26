#!/usr/bin/env python3
"""Finite checks for the rank-stratified type enumerator.

Run with Python 3; no third-party packages are required.
The checks compare direct labeled residue/tangent assignments with the
exponential-generating-function coefficient formula for small prime fields.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial, prod


def gaussian_binomial(n, k, q):
    if k < 0 or k > n:
        return 0
    numerator = prod(q ** (n - i) - 1 for i in range(k))
    denominator = prod(q ** (k - i) - 1 for i in range(k))
    return numerator // denominator


def rank_matrix(matrix, q):
    """Rank over the prime field F_q."""
    if not matrix:
        return 0
    a = [list(row) for row in matrix]
    height = len(a)
    width = len(a[0]) if height else 0
    pivot_row = 0
    for col in range(width):
        pivot = next((i for i in range(pivot_row, height)
                      if a[i][col] % q), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inverse = pow(a[pivot_row][col] % q, -1, q)
        a[pivot_row] = [(x * inverse) % q for x in a[pivot_row]]
        for i in range(height):
            if i != pivot_row and a[i][col] % q:
                factor = a[i][col] % q
                a[i] = [(x - factor * y) % q
                        for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == height:
            break
    return pivot_row


def rank_matrix_count(ell, m, s, q):
    if s < 0 or s > min(ell, m):
        return 0
    return gaussian_binomial(ell, s, q) * prod(q ** m - q ** j
                                                 for j in range(s))


def direct_type_counts(q, ell, r):
    """Enumerate all residue/tangent data and count abstract factor types."""
    residue_vectors = list(product(range(q), repeat=ell))
    tangent_vectors = list(product(range(q), repeat=ell))
    counts = Counter()
    for residues in product(residue_vectors, repeat=r):
        blocks = {}
        for i, residue in enumerate(residues):
            blocks.setdefault(residue, []).append(i)
        for tangents in product(tangent_vectors, repeat=r):
            type_counts = [0] * (ell + 1)
            for indices in blocks.values():
                matrix = [[tangents[i][j] for i in indices]
                          for j in range(ell)]
                s = rank_matrix(matrix, q)
                type_counts[s] += 1
            counts[tuple(type_counts)] += 1
    return counts


def egf_type_counts(q, ell, r):
    """Extract the coefficient of the product EGF using exact rationals."""
    zero_type = (0,) * (ell + 1)
    dp = {(0, zero_type): Fraction(1)}
    for _color in range(q ** ell):
        updated = {}
        for (used, counts), coefficient in dp.items():
            key = (used, counts)
            updated[key] = updated.get(key, Fraction(0)) + coefficient
            for m in range(1, r - used + 1):
                for s in range(min(ell, m) + 1):
                    number = rank_matrix_count(ell, m, s, q)
                    if not number:
                        continue
                    new_counts = list(counts)
                    new_counts[s] += 1
                    key = (used + m, tuple(new_counts))
                    updated[key] = (updated.get(key, Fraction(0))
                                    + coefficient * Fraction(number, factorial(m)))
        dp = updated
    return Counter({counts: int(coefficient * factorial(r))
                    for (used, counts), coefficient in dp.items()
                    if used == r and coefficient})


def check_case(q, ell, r):
    direct = direct_type_counts(q, ell, r)
    formula = egf_type_counts(q, ell, r)
    assert direct == formula, (q, ell, r, direct, formula)
    assert sum(direct.values()) == q ** (2 * ell * r)
    print(f"PASS q={q}, ell={ell}, r={r}: {sum(direct.values())} tuples")


def main():
    for parameters in ((2, 1, 4), (3, 1, 4), (2, 2, 3), (3, 2, 2)):
        check_case(*parameters)
    print("ALL_TYPE_EGF_CHECKS_PASSED")


if __name__ == "__main__":
    main()
