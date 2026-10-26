#!/usr/bin/env python3
"""Exact-rational verification of two cut/cycle projection norm formulas for prism graphs.

Runs over finite sizes only. The accompanying mathematical proof establishes
all-parameter results; this script is an independent finite consistency test.
"""
from fractions import Fraction as F


def inverse(a):
    n = len(a)
    m = [[F(x) for x in row] + [F(int(i == j)) for j in range(n)]
         for i, row in enumerate(a)]
    for i in range(n):
        j = next(j for j in range(i, n) if m[j][i])
        m[j], m[i] = m[i], m[j]
        pivot = m[i][i]
        m[i] = [v / pivot for v in m[i]]
        for j in range(n):
            if j == i:
                continue
            pivot = m[j][i]
            if pivot:
                m[j] = [u - pivot * v for u, v in zip(m[j], m[i])]
    return [row[n:] for row in m]


def expected(n):
    a = [[4 * (i == j) - (j == (i - 1) % n) - (j == (i + 1) % n)
          for j in range(n)] for i in range(n)]
    inv = inverse(a)
    h = [2 * inv[i][0] for i in range(n)]
    assert all(v > 0 for v in h) and sum(h) == 1
    hmin = min(h)
    t = sum(max(F(1, n) - x, F(0)) for x in h[1:])
    qr = 2 - F(1, n) - hmin + t
    qv = 1 + 2 * (h[0] - hmin)
    cr = 1 + h[0] - hmin + t
    cv = 2 - 2 * hmin
    return qr, qv, cr, cv


def direct(n):
    vertices = 2 * n
    edges = [(s * n + i, s * n + (i + 1) % n)
             for s in range(2) for i in range(n)]
    edges += [(i, n + i) for i in range(n)]
    l = [[0 for _ in range(vertices)] for _ in range(vertices)]
    for u, v in edges:
        l[u][u] += 1
        l[v][v] += 1
        l[u][v] -= 1
        l[v][u] -= 1
    # Removing the last row/column fixes a potential gauge.
    inv = inverse([row[:-1] for row in l[:-1]])
    projected = []
    complementary = []
    for j, (u, v) in enumerate(edges):
        b = [int(k == u) - int(k == v) for k in range(vertices - 1)]
        p = [sum(inv[k][z] * b[z] for z in range(vertices - 1))
             for k in range(vertices - 1)] + [F(0)]
        column = [p[x] - p[y] for x, y in edges]
        projected.append(sum(map(abs, column)))
        complementary.append(sum(abs(int(k == j) - q)
                                 for k, q in enumerate(column)))
    return (projected[0], projected[2 * n],
            complementary[0], complementary[2 * n],
            projected, complementary)


def main():
    columns = 0
    for n in range(3, 19):
        qr, qv, cr, cv, qcols, ccols = direct(n)
        assert (qr, qv, cr, cv) == expected(n)
        assert all(x == qr for x in qcols[:2 * n])
        assert all(x == qv for x in qcols[2 * n:])
        assert all(x == cr for x in ccols[:2 * n])
        assert all(x == cv for x in ccols[2 * n:])
        if n == 3:
            assert qr < qv and cr > cv
        elif n == 4:
            assert qr == qv and cr == cv
        else:
            assert qr > qv and cr > cv
        assert max(qr, qv) > max(cr, cv)
        columns += 3 * n
    assert columns == sum(3 * n for n in range(3, 19))
    print(f'PASS: sizes 3..18; all {columns} edge columns; exact rational identities, orbit comparisons, cut dominance')


if __name__ == '__main__':
    main()
