#!/usr/bin/env python3
"""Exact-rational face calculation for a five-site convex least-squares sensitivity theorem."""
from fractions import Fraction as F
from itertools import combinations


def identity(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def dot(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def inverse(A):
    n = len(A)
    aug = [list(A[i]) + identity(n)[i] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        t = aug[k][k]
        aug[k] = [v / t for v in aug[k]]
        for i in range(n):
            if i != k:
                t = aug[i][k]
                aug[i] = [aug[i][j] - t * aug[k][j] for j in range(2 * n)]
    return [r[n:] for r in aug]


def matvec(A, v):
    return [sum(a * b for a, b in zip(row, v)) for row in A]


def diff(n):
    return [[F((1 if j == i or j == i + 2 else -2 if j == i + 1 else 0))
             for j in range(n)] for i in range(n - 2)]


def projector(n, selected):
    I = identity(n)
    if not selected:
        return I
    B = [diff(n)[i] for i in selected]
    H = dot(dot(transpose(B), inverse(dot(B, transpose(B)))), B)
    return [[I[i][j] - H[i][j] for j in range(n)] for i in range(n)]


def rowsums(A):
    return [sum(map(abs, row)) for row in A]


def face_table(n):
    out = {}
    for k in range(n - 1):
        for active in combinations(range(n - 2), k):
            out[active] = rowsums(projector(n, active))
    return out


def verify():
    small = {2: F(1), 3: F(4, 3), 4: F(7, 5), 5: F(11, 7)}
    exact5 = {
        (): [1, 1, 1, 1, 1],
        (0,): [F(4, 3), 1, F(4, 3), 1, 1],
        (1,): [1, F(4, 3), 1, F(4, 3), 1],
        (2,): [1, 1, F(4, 3), 1, F(4, 3)],
        (0, 1): [F(7, 5), 1, 1, F(7, 5), 1],
        (0, 2): [F(7, 5), F(39, 35), F(11, 7), F(39, 35), F(7, 5)],
        (1, 2): [1, F(7, 5), 1, 1, F(7, 5)],
        (0, 1, 2): [F(7, 5), 1, 1, 1, F(7, 5)],
    }
    assertions = 0
    for n in range(2, 6):
        tab = face_table(n)
        assert max(max(v) for v in tab.values()) == small[n]
        assertions += 1
        for active, v in tab.items():
            P = projector(n, active)
            assert dot(P, P) == P
            assert transpose(P) == P
            assertions += 2
            for j in range(n):
                assert v[j] == sum(abs(P[j][k]) for k in range(n))
                assertions += 1
        if n == 5:
            assert tab == {a: list(map(F, v)) for a, v in exact5.items()}
            assertions += 1
            assert [(a, j) for a, vals in tab.items() for j, z in enumerate(vals)
                    if z == F(11, 7)] == [((0, 2), 2)]
            assertions += 1
    D = diff(5)
    B = [D[0], D[2]]
    P = projector(5, (0, 2))
    x = list(map(F, [0, 0, 0, 1, 2]))
    lam = [F(1), F(1)]
    y = [x[i] - matvec(transpose(B), lam)[i] for i in range(5)]
    assert y == list(map(F, [-1, 2, -2, 3, 1]))
    assert matvec(D, x) == list(map(F, [0, 1, 0]))
    h = list(map(F, [-1, 1, 1, 1, -1]))
    eps = F(1, 10)
    delta = matvec(P, h)
    x2 = [x[i] + eps * delta[i] for i in range(5)]
    y2 = [y[i] + eps * h[i] for i in range(5)]
    lam2 = [lam[i] - eps * matvec(inverse(dot(B, transpose(B))), matvec(B, h))[i]
            for i in range(2)]
    assert delta == [F(-5, 7), F(3, 7), F(11, 7), F(3, 7), F(-5, 7)]
    assert x2 == [F(-1, 14), F(3, 70), F(11, 70), F(73, 70), F(27, 14)]
    assert y2 == [F(-11, 10), F(21, 10), F(-19, 10), F(31, 10), F(9, 10)]
    assert lam2 == [F(36, 35), F(36, 35)]
    assert matvec(D, x2) == [F(0), F(27, 35), F(0)]
    assert all(t > 0 for t in lam2)
    assert y2 == [x2[i] - matvec(transpose(B), lam2)[i] for i in range(5)]
    assert max(map(abs, [x2[i] - x[i] for i in range(5)])) / (
        eps * max(map(abs, h))) == F(11, 7)
    assertions += 9
    # Localized face projects independently of further unconstrained vertices.
    for n in range(5, 14):
        Pn = projector(n, (0, 2))
        for i in range(5):
            for j in range(5):
                assert Pn[i][j] == P[i][j]
                assertions += 1
            assert all(Pn[i][j] == 0 for j in range(5, n))
            assertions += 1
    # Alternating constraints: independent closed-form inverse of Gram tridiagonal.
    def continuants(k):
        t = [F(1), F(6)]
        for j in range(2, k + 1):
            t.append(6 * t[-1] - t[-2])
        return t
    for m in range(2, 14):
        t = continuants(m)
        Ginv = [[(-1) ** (i + j) * t[min(i, j)] * t[m - max(i, j) - 1] / t[m]
                 for j in range(m)] for i in range(m)]
        G = [[F(6 if i == j else 1 if abs(i-j) == 1 else 0)
              for j in range(m)] for i in range(m)]
        assert dot(G, Ginv) == identity(m)
        assertions += 1
        n = 2*m + 1
        B = [diff(n)[2*j] for j in range(m)]
        P = identity(n)
        H = dot(dot(transpose(B), Ginv), B)
        P = [[P[i][j] - H[i][j] for j in range(n)] for i in range(n)]
        if m <= 6:
            assert P == projector(n, tuple(2*j for j in range(m)))
            assertions += 1
        r = m // 2
        chosen = 2*r
        row = sum(abs(t) for t in P[chosen])
        assert row > F(3, 2) and row < F(7, 4)
        assertions += 2
    # The exact infinite-Green-kernel l1 calculation is in RESULT.md.
    print('PASS: exact face classification and KKT witness; rational assertions:', assertions)
    print('L2,L3,L4,L5 = 1, 4/3, 7/5, 11/7; unique maximizing face (0,2), coordinate 2')


if __name__ == '__main__':
    verify()
