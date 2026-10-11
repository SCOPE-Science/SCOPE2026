"""Exact-arithmetic checks for a two-variable Hardy approximation bound.

This script verifies finite-degree instances. The asymptotic theorem rests on
an analytic Cauchy--Schwarz argument and a block-transport construction.
Run with: python3 check_approximation.py
"""
from fractions import Fraction
from math import isqrt


def solve(matrix, target):
    n = len(target)
    a = [[Fraction(x) for x in row] + [Fraction(v)]
         for row, v in zip(matrix, target)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        t = a[col][col]
        a[col] = [v / t for v in a[col]]
        for row in range(n):
            if row != col:
                t = a[row][col]
                a[row] = [x - t*y for x, y in zip(a[row], a[col])]
    return [row[-1] for row in a]


def exact_minimum(n):
    # Independent projection calculation using the full monomial Gramian.
    mon = [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]
    f = {(0, 0): 1, (1, 0): -1, (0, 1): -1, (1, 1): 1}
    shifts = []
    for i, j in mon:
        shifts.append({(i+a, j+b): c for (a, b), c in f.items()})
    gram = [[sum(c * shifts[v].get(k, 0) for k, c in shifts[u].items())
             for v in range(len(mon))] for u in range(len(mon))]
    b = [int(x == (0, 0)) for x in mon]
    c = solve(gram, b)
    return 1 - c[0]


def network_minimum(n):
    L = n + 2
    a = [[(L + 1 - i) * (i == j) + (j <= L - i)
          for j in range(L + 1)] for i in range(L + 1)]
    b = [int(i == 0) for i in range(L + 1)]
    return 2 * solve(a, b)[0]


def block_residual(n):
    L = n + 2
    B = isqrt(L)
    M = L - B
    blocks = [list(range(s, min(s + B, M + 1)))
              for s in range(1, M + 1, B)]
    r = {}
    for i in range(1, M + 1):
        r[(i, 0)] = Fraction(1, M)
        r[(0, i)] = Fraction(1, M)
    for block in blocks:
        for i in block:
            for k in block:
                j = M + 1 - k
                assert i + j <= L
                r[(i, j)] = -Fraction(1, M * len(block))
    for i in range(L + 1):
        assert sum(v for (a, b), v in r.items() if a == i) == (i == 0)
        assert sum(v for (a, b), v in r.items() if b == i) == (i == 0)
    # Divide 1-R by (1-z)(1-w) using prefix sums.
    q = {}
    for i in range(L + 1):
        for j in range(L + 1 - i):
            c = (i == 0 and j == 0) - r.get((i, j), 0)
            q[(i, j)] = (c + q.get((i - 1, j), 0)
                         + q.get((i, j - 1), 0)
                         - q.get((i - 1, j - 1), 0))
    assert all(v == 0 for (i, j), v in q.items() if i + j > n)
    energy = sum(v*v for v in r.values())
    expected = Fraction(2, M) + Fraction(len(blocks), M*M)
    assert energy == expected
    return energy, B, M, len(blocks)


def main():
    for n in range(8):
        g = exact_minimum(n)
        h = network_minimum(n)
        u, B, M, blocks = block_residual(n)
        assert g == h, (n, g, h)
        assert Fraction(2, n + 4) <= g <= u
        print(f'n={n}: exact_minimum={g}; lower={Fraction(2,n+4)}; '
              f'constructive_upper={u}; block=(B={B}, M={M}, blocks={blocks})')
    print('PASS: 8 independent Gram/network equalities, 8 polynomial divisibility, '
          '16 exact interval inequalities.')


if __name__ == '__main__':
    main()
