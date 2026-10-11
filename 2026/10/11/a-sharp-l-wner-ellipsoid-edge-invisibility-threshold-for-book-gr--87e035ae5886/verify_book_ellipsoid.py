#!/usr/bin/env python3
"""Exact rational checks for the book-graph symmetric-edge-polytope ellipsoid.

Dependencies: Python 3 standard library only. Run: python book_mvee_verifier.py
Finite checks supplement, rather than replace, the general proof.
"""
from fractions import Fraction as F


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def inverse(a):
    n = len(a)
    c = [list(row) + erow for row, erow in zip(a, eye(n))]
    for i in range(n):
        pivot = next((k for k in range(i, n) if c[k][i]), None)
        assert pivot is not None, 'singular matrix'
        c[i], c[pivot] = c[pivot], c[i]
        p = c[i][i]
        c[i] = [x / p for x in c[i]]
        for k in range(n):
            if k != i:
                p = c[k][i]
                if p:
                    c[k] = [a - p*b for a, b in zip(c[k], c[i])]
    return [row[n:] for row in c]


def quad(a, b):
    return sum(b[i]*a[i][j]*b[j] for i in range(len(b)) for j in range(len(b)))


def main():
    checked = 0
    for m in range(2, 13):
        n, d = m + 2, m + 1
        w = F(2, 3*(m+1)) if m <= 3 else F(1, 2*m)
        v = F(3-m, 3*(m+1)) if m <= 3 else F(0)
        assert 2*m*w + v == 1 and w > 0 and v >= 0
        edges = [(0, 1, v)] + [(h, j, w) for h in (0, 1) for j in range(2, n)]
        C = [[F(0) for _ in range(n)] for _ in range(n)]
        for h, j, weight in edges:
            C[h][h] += weight
            C[j][j] += weight
            C[h][j] -= weight
            C[j][h] -= weight
        ones_projection = [[F(1, n) for _ in range(n)] for _ in range(n)]
        K = [[C[i][j] + ones_projection[i][j] for j in range(n)] for i in range(n)]
        Ki = inverse(K)
        Ci = [[Ki[i][j] - ones_projection[i][j] for j in range(n)] for i in range(n)]
        u = [F(m), F(m)] + [F(-2) for _ in range(m)]
        a = [F(1), F(-1)] + [F(0) for _ in range(m)]
        Pa = [[a[i]*a[j]/2 for j in range(n)] for i in range(n)]
        Pc = [[u[i]*u[j]/(2*m*(m+2)) for j in range(n)] for i in range(n)]
        Pl = [[F(int(i == j)) - ones_projection[i][j] - Pa[i][j] - Pc[i][j]
               for j in range(n)] for i in range(n)]
        ll, la, lc = 2*w, m*w + 2*v, (m+2)*w
        for i in range(n):
            for j in range(n):
                assert C[i][j] == ll*Pl[i][j] + la*Pa[i][j] + lc*Pc[i][j]
                assert Ci[i][j] == Pl[i][j]/ll + Pa[i][j]/la + Pc[i][j]/lc
        contacts = []
        for h, j, _ in edges:
            b = [F(0) for _ in range(n)]
            b[h], b[j] = F(1), F(-1)
            leverage = quad(Ci, b)
            expected = F(2, la) if (h, j) == (0, 1) else F(1, 2*w) + F(1, 2*la)
            assert leverage == expected
            assert leverage <= d
            if leverage == d:
                contacts.append((h, j))
        assert len(contacts) == 2*m + (int(m <= 3))
        assert (0, 1) in contacts if m <= 3 else (0, 1) not in contacts
        assert (F(2, la) == d) if m <= 3 else (F(2, la) == 4 and 4 < d)
        checked += 1
        print(f'm={m:2d}: spoke_weight={w}, hub_weight={v}, '
              f'eigenvalues=({ll}, {la}, {lc}), touching_edge_pairs={len(contacts)}/{len(edges)}')
    print(f'EXACT_CHECKS_PASS: {checked} dimensions, all contact inequalities, '
          'all covariance/projector/inverse identities.')


if __name__ == '__main__':
    main()
