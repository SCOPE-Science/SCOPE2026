"""Exact finite diagnostics for maximal simplices in simplex-square products.

Mathematical all-dimensional proof uses barycentric row elimination; this checker
independently enumerates every vertex subset in dimensions n=1,2,3,4.
Only Python 3 standard library is required.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def det_int(matrix):
    """Determinant by exact fraction-free Bareiss elimination."""
    a = [row[:] for row in matrix]
    size = len(a)
    previous = 1
    parity = 1
    for k in range(size - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, size) if a[i][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            parity = -parity
        pivot = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0, (k, i, j, numerator, previous)
                a[i][j] = numerator // previous
        for i in range(k + 1, size):
            a[i][k] = 0
        previous = pivot
    return parity * a[-1][-1]


def observed(n):
    # Standard simplex {0,e_1,...,e_n} crossed with the square {0,1}^2.
    vertices = []
    for layer in range(n + 1):
        vector = [int(i == layer) for i in range(1, n + 1)]
        for u, v in product((0, 1), repeat=2):
            vertices.append((1, *vector, u, v))
    counts = Counter()
    for chosen in combinations(vertices, n + 3):
        delta = abs(det_int([list(row) for row in chosen]))
        assert delta <= 2, (n, chosen, delta)
        counts[delta] += 1
    return counts


def predicted(n):
    N = n + 1
    high = N * (N - 1) * 4 ** (N - 2)
    unit = N * 4 ** N + 12 * N * (N - 1) * 4 ** (N - 2)
    low = comb(4 * N, N + 2) - unit - high
    return {0: low, 1: unit, 2: high}


def main():
    for n in range(1, 5):
        got = observed(n)
        expected = predicted(n)
        assert dict(got) == expected, (n, dict(got), expected)
        assert sum(got.values()) == comb(4 * (n + 1), n + 3)
        print('DIM', n + 2, 'COUNTS', ','.join(str(got[j]) for j in (0, 1, 2)))
    print('VERIFY_OK n=1..4 integer_determinants_and_spectrum')


if __name__ == '__main__':
    main()
