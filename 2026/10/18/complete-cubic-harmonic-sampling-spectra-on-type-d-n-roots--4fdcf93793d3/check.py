#!/usr/bin/env python3
"""Exact integer/rational corroboration of cubic harmonic sampling on type-D roots.
Requires only the Python 3 standard library. Run: python3 check.py
The infinite-family proof is algebraic; finite cases below are additional checks.
"""
from fractions import Fraction as F
from itertools import combinations, product


def roots(n):
    out = []
    for i, j in combinations(range(n), 2):
        for a, b in product((-1, 1), repeat=2):
            v = [0] * n
            v[i], v[j] = a, b
            out.append(tuple(v))
    return out


def rank_mod(A, p=1000003):
    a = [[int(x) % p for x in r] for r in A]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        k = next((k for k in range(r, m) if a[k][c]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        inv = pow(a[r][c], -1, p)
        pivot = [(v * inv) % p for v in a[r][c:]]
        for k in range(r + 1, m):
            factor = a[k][c]
            if factor:
                tail = a[k]
                tail[c:] = [(z - factor * w) % p for z, w in zip(tail[c:], pivot)]
        r += 1
    return r


def run(n):
    V = roots(n)
    m = len(V)
    assert m == 2 * n * (n - 1)
    neg = {tuple(-z for z in v): i for i, v in enumerate(V)}
    anti = [neg[v] for v in V]
    assert all(anti[anti[i]] == i and i != anti[i] for i in range(m))
    assert all(sum(V[i][j] * V[i][k] for i in range(m)) ==
               (4 * (n - 1) if j == k else 0)
               for j in range(n) for k in range(n))
    B = []
    for i in range(m):
        row = []
        for j in range(m):
            u = sum(a * b for a, b in zip(V[i], V[j]))
            assert u in (-2, -1, 0, 1, 2)
            val = (n + 2) * u**3 - 12 * u
            assert val == (6 * (n + 2) * ((i == j) - (anti[i] == j)) +
                           (n - 10) * u)
            row.append(val)
        B.append(row)
    for i in range(m):
        for j in range(n):
            assert sum(B[i][k] * V[k][j] for k in range(m)) == 4 * (n - 4)**2 * V[i][j]
    if n == 10:
        assert all(B[i][j] == 8 * (n - 1) * ((i == j) - (anti[i] == j))
                   for i in range(m) for j in range(m))
    # Arbitrary antipodally odd data, then project off coordinates at n=4.
    y = [F(0)] * m
    for i in range(m):
        if i < anti[i]:
            y[i] = F((i * 7 + 3) % 11 - 5)
            y[anti[i]] = -y[i]
    coords = [sum(F(V[i][k]) * y[i] for i in range(m)) for k in range(n)]
    yc = [sum(F(V[i][k]) * coords[k] for k in range(n)) / (4 * (n - 1))
          for i in range(m)]
    y = [y[i] - yc[i] if n == 4 else y[i] for i in range(m)]
    l0 = F((n - 4)**2, 2 * (n - 1))
    l1 = F(3 * (n + 2), 2 * (n - 1))
    if n == 4:
        c = [yi / l1 for yi in y]
    else:
        c = [y[i] / l1 + (1 / l0 - 1 / l1) * yc[i] for i in range(m)]
    assert all(sum(F(B[i][j]) * c[j] for j in range(m)) ==
               F(8 * (n - 1)) * y[i] for i in range(m))
    expected = n * (n - 2) if n == 4 else n * (n - 1)
    actual = rank_mod(B)
    assert actual == expected, (n, actual, expected)
    print(f'n={n}: |X|={m}, rank={actual}, '
          f'coordinate={l0}, complementary={l1}, interpolation=PASS')


if __name__ == '__main__':
    for dimension in (4, 5, 6, 7, 8, 9, 10, 12):
        run(dimension)
    print('All exact cubic-kernel, spectral and interpolation checks passed.')
