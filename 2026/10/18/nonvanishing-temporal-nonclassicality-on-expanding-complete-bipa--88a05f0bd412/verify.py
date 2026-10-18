#!/usr/bin/env python3
"""Exact rational checks for the complete-bipartite Laplacian walk formula.

Run: python3 verify.py. Uses the Python standard library only.
These finite computations corroborate the separately stated all-size proof.
"""
from fractions import Fraction as Q
from math import isclose


def matrices(m, n):
    assert isinstance(m, int) and isinstance(n, int) and m >= 1 and n >= 1
    N = m + n
    z = Q(0)
    P0 = [[Q(1, N) for j in range(N)] for i in range(N)]
    Ptop = []
    PA = []
    PB = []
    for i in range(N):
        rt, ra, rb = [], [], []
        for j in range(N):
            if i < m and j < m:
                rt.append(Q(n, m * N))
                ra.append(Q(int(i == j)) - Q(1, m))
                rb.append(z)
            elif i >= m and j >= m:
                rt.append(Q(m, n * N))
                ra.append(z)
                rb.append(Q(int(i == j)) - Q(1, n))
            else:
                rt.append(-Q(1, N))
                ra.append(z)
                rb.append(z)
        Ptop.append(rt)
        PA.append(ra)
        PB.append(rb)
    groups = {0: P0, N: Ptop}
    for val, P in ((n, PA), (m, PB)):
        if val in groups:
            groups[val] = [[groups[val][i][j] + P[i][j] for j in range(N)] for i in range(N)]
        else:
            groups[val] = P
    return list(groups.values())


def product(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(A[0]))), Q(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def exact(m, n):
    N = m + n
    P = matrices(m, n)
    for idx, QP in enumerate(P):
        assert product(QP, QP) == QP, ('idempotence', m, n, idx)
        for j, RP in enumerate(P):
            if idx != j:
                assert not any(any(row) for row in product(QP, RP)), ('orthogonality', m, n)
    assert all(sum(Px[i][j] for Px in P) == int(i == j)
               for i in range(N) for j in range(N)), ('resolution', m, n)
    F = [[sum((Px[i][j] ** 2 for Px in P), Q(0))
          for j in range(N)] for i in range(N)]
    assert all(sum(row) == 1 for row in F), ('stochastic', m, n)
    FF = product(F, F)
    delta = [F[i][0] - FF[i][0] for i in range(N)]
    R = sum((abs(x) for x in delta), Q(0)) / 2
    A = Q(2 * (m - 2), m * m) if m >= 2 else Q(0)
    B = Q(2 * (N - 2), N * N)
    expected_delta = [A * Q(m - 1, m) + B * Q(n, m * N)]
    expected_delta += [-A / m + B * Q(n, m * N)] * (m - 1)
    expected_delta += [-B / N] * n
    assert delta == expected_delta, ('entry-profile', m, n, delta, expected_delta)
    if m <= 2:
        expected_R = Q(2 * n * (N - 2), N ** 3)
    else:
        expected_R = Q(2 * (m - 1) * (m - 2), m ** 3) + Q(2 * n * (N - 2), m * N ** 3)
    assert R == expected_R, ('closed form', m, n, R, expected_R)
    return R


def main():
    checks = 0
    for m in range(1, 9):
        for n in range(1, 9):
            exact(m, n)
            checks += 1
    for m, n in ((1, 19), (2, 19), (3, 19), (5, 19), (9, 13), (13, 9)):
        exact(m, n)
        checks += 1
    for m in range(3, 100):
        f = Q(2 * (m - 1) * (m - 2), m ** 3)
        assert f <= Q(24, 125)
        if m == 5:
            assert f == Q(24, 125)
    print('VERIFY_OK', checks, 'exact projector/rational-residual cases;',
          'limiting optimum', str(Q(24, 125)))


if __name__ == '__main__':
    main()
