#!/usr/bin/env python3
"""Exact rational spot checks for a sharp finite-element positivity threshold.

Finite tests corroborate, but do not establish, the all-size theorem; its proof
uses the explicit cyclic resolvent and analytic inequalities.
"""
from fractions import Fraction as F


def invert_times(A, B):
    n = len(A)
    T = [[A[i][j] for j in range(n)] + [B[i][j] for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if T[i][j])
        T[j], T[pivot] = T[pivot], T[j]
        z = T[j][j]
        T[j] = [c/z for c in T[j]]
        for i in range(n):
            if i == j:
                continue
            z = T[i][j]
            if z:
                T[i] = [u-z*v for u, v in zip(T[i], T[j])]
    return [row[n:] for row in T]


def matrices(n, a, b, tau):
    M = [[F(0) for _ in range(n)] for _ in range(n)]
    A = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        j = (i+1) % n
        k = a if i % 2 == 0 else b
        for T, v in ((M, F(1, 3)), (A, F(1, 3)+tau*k)):
            T[i][i] += v
            T[j][j] += v
        for T, v in ((M, F(1, 6)), (A, F(1, 6)-tau*k)):
            T[i][j] += v
            T[j][i] += v
    return A, M


def check():
    tested = 0
    for m in (3, 4, 5, 6):
        for a, b in ((1, 1), (1, 2), (1, 5), (2, 3), (1, 100)):
            a, b = F(a), F(b)
            t_small = F(1, 12*b)
            t_cross = F(1, 6*b)
            t_cut = F(1, 6*a)
            tests = [('zero', F(0)), ('low', t_small),
                     ('strong-cross', t_cross), ('cut', t_cut),
                     ('large', t_cut*2)]
            if a < b:
                tests.append(('mixed', (t_cross+t_cut)/2))
            for kind, tau in tests:
                A, M = matrices(2*m, a, b, tau)
                P = invert_times(A, M)
                row_sums = [sum(row) for row in P]
                assert all(z == 1 for z in row_sums)
                if kind in ('zero', 'cut', 'large'):
                    assert all(z >= 0 for row in P for z in row)
                elif kind in ('low', 'strong-cross'):
                    if a == b and kind == 'strong-cross':
                        assert all(z >= 0 for row in P for z in row)
                    else:
                        assert P[0][2] < 0
                else:
                    assert P[0][3] < 0
                tested += 1
    A, M = matrices(4, F(1), F(2), F(1, 8))
    P = invert_times(A, M)
    assert min(z for row in P for z in row) == F(9, 4004)
    assert P[0] == [F(2609,4004),F(537,4004),F(9,4004),F(849,4004)]
    print('VERIFY_OK', tested, 'six-or-more-node exact rational cases; four-node boundary witness')


if __name__ == '__main__':
    check()
