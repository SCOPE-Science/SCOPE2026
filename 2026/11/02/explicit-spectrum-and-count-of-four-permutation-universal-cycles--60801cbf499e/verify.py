"""Exact verification of four-permutation universal-cycle enumeration.

Standard-library-only. Independent matrix-tree determinants are computed
by integer-preserving fraction-free Gaussian elimination (Bareiss).
Run: python3 verify.py
"""
from itertools import permutations
from math import factorial


def det_bareiss(a):
    a = [list(row) for row in a]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            p = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        top = a[k]
        for i in range(k + 1, n):
            row = a[i]
            aik = row[k]
            for j in range(k + 1, n):
                numerator = row[j] * pivot - aik * top[j]
                assert numerator % previous == 0
                row[j] = numerator // previous
            row[k] = 0
        previous = pivot
    return sign * a[-1][-1]


def adjacency(n):
    vertices = list(permutations(range(n), 3))
    index = {v: i for i, v in enumerate(vertices)}
    N = len(vertices)
    A = [[0] * N for _ in range(N)]
    for i, (a, b, c) in enumerate(vertices):
        for d in range(n):
            if d not in (a, b, c):
                A[i][index[(b, c, d)]] += 1
    assert all(sum(row) == n - 3 for row in A)
    assert all(sum(A[i][j] for i in range(N)) == n - 3 for j in range(N))
    return A


def factors(n):
    N = n * (n - 1) * (n - 2)
    E = N // 3 - (n - 1) ** 2
    s = n * (n - 3) // 2
    t = (n - 1) * (n - 2) // 2
    assert E >= 0
    assert 3 * E + 3 + 3 * (n - 1) + 3 * s + 3 * t == N
    return N, E, s, t


def chi_formula(n, x):
    N, E, s, t = factors(n)
    d = n - 3
    return ((x ** 3 + 1) ** E * (x - d) * (x * x - x + 1)
            * (x ** 3 + x * x + d * x + d * d) ** (n - 1)
            * (x ** 3 + x * x - x - d) ** s
            * (x ** 3 - x * x + x - d) ** t)


def arborescences_formula(n):
    N, E, s, t = factors(n)
    d = n - 3
    product_nonzero = ((d + 1) ** E * (d * d - d + 1) ** (E + 1)
                       * (n * d * d) ** (n - 1)
                       * (d * (d + 2) * (d - 1)) ** s
                       * (d * d * (d - 1)) ** t)
    assert product_nonzero % N == 0
    return product_nonzero // N


def test():
    expected_5 = 7044820107264000
    expected_6 = 2 ** 171 * 3 ** 43 * 5 ** 8 * 7 ** 16
    for n in range(5, 9):
        N, E, s, t = factors(n)
        A = adjacency(n)
        d = n - 3
        Lap = [[(d if i == j else 0) - A[i][j]
                for j in range(N - 1)] for i in range(N - 1)]
        direct = det_bareiss(Lap)
        formula = arborescences_formula(n)
        assert direct == formula, (n, direct, formula)
        cycles = direct * factorial(n - 4) ** N
        if n == 5:
            assert cycles == expected_5
        if n == 6:
            assert cycles == expected_6
        print(f'n={n} vertices={N} arborescence_digits={len(str(direct))} '
              f'cycle_digits={len(str(cycles))}')
        if n <= 7:
            for x in (-3, -2, -1, 0, 1, d, d + 1):
                M = [[(x if i == j else 0) - A[i][j]
                      for j in range(N)] for i in range(N)]
                assert det_bareiss(M) == chi_formula(n, x), (n, x)
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
