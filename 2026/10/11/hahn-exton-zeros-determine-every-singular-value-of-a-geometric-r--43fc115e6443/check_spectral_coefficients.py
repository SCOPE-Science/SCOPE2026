"""Exact arithmetic spot checks of the geometric Rhaly Gram determinant.

This is finite validation, not a proof of the infinite spectral theorem.
"""
from fractions import Fraction
from itertools import combinations
from math import prod


def determinant(matrix):
    a = [list(row) for row in matrix]
    size = len(a)
    out = Fraction(1)
    for j in range(size):
        pivot = next((r for r in range(j, size) if a[r][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        p = a[j][j]
        out *= p
        for r in range(j + 1, size):
            ratio = a[r][j] / p
            for c in range(j + 1, size):
                a[r][c] -= ratio * a[j][c]
    return out


def assert_case(t, n, max_k):
    k_gram = [[t ** (i + j) * (min(i, j) + 1)
               for j in range(n)] for i in range(n)]
    for k in range(1, max_k + 1):
        finite_coefficient = Fraction(0)
        for choice in combinations(range(n), k):
            direct = determinant([[k_gram[i][j] for j in choice]
                                  for i in choice])
            increments = [choice[0] + 1] + [choice[r] - choice[r - 1]
                                               for r in range(1, k)]
            predicted = t ** (2 * sum(choice)) * prod(increments)
            assert direct == predicted, (t, n, choice, direct, predicted)
            finite_coefficient += direct
        whole_coefficient = t ** (k * (k - 1)) / prod(
            (1 - t ** (2 * j)) ** 2 for j in range(1, k + 1))
        assert 0 < finite_coefficient < whole_coefficient
        print(f't={t} k={k}: finite e_k={finite_coefficient}; '
              f'infinite e_k={whole_coefficient}')


if __name__ == '__main__':
    assert_case(Fraction(1, 2), 8, 4)
    assert_case(Fraction(2, 3), 7, 3)
    print('Exact finite principal-minor checks passed. Infinite claim rests on proof.')
