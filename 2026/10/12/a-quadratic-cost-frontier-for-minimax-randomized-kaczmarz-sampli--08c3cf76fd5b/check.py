"""Reproduce rational primal/dual certificates for cost-aware simplex sampling.

Python 3 standard library only. This checker tests finite rational instances;
the all-dimensional theorem is proved separately in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations


def matrices(d):
    n = d + 1
    P = [[F(int(i == j)) - F(1, n) for j in range(n)] for i in range(n)]
    Q = []
    for k in range(n):
        h = [F(int(i == k)) - F(1, n) for i in range(n)]
        Q.append([[F(n, d) * h[i] * h[j] for j in range(n)] for i in range(n)])
    return P, Q


def add(A, B, a=F(1), b=F(1)):
    return [[a * A[i][j] + b * B[i][j] for j in range(len(A))]
            for i in range(len(A))]


def weighted(Q, z):
    n = len(z)
    return [[sum((z[k] * Q[k][i][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def trace_product(A, B):
    n = len(A)
    return sum((A[i][j] * B[j][i] for i in range(n)
                for j in range(n)), F(0))


def trace(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def det(A):
    n = len(A)
    if n == 0:
        return F(1)
    B = [list(row) for row in A]
    out = F(1)
    for j in range(n):
        k = next((k for k in range(j, n) if B[k][j] != 0), None)
        if k is None:
            return F(0)
        if k != j:
            B[k], B[j] = B[j], B[k]
            out = -out
        pivot = B[j][j]
        out *= pivot
        for k in range(j + 1, n):
            ratio = B[k][j] / pivot
            for h in range(j + 1, n):
                B[k][h] -= ratio * B[j][h]
            B[k][j] = 0
    return out


def psd(A):
    n = len(A)
    for r in range(1, n + 1):
        for subset in combinations(range(n), r):
            M = [[A[i][j] for j in subset] for i in subset]
            if det(M) < 0:
                return False
    return True


def equal(A, B):
    return all(x == y for row_a, row_b in zip(A, B)
               for x, y in zip(row_a, row_b))


def check(d, t):
    P, Q = matrices(d)
    n = d + 1
    # The columns represent unit regular-simplex rows in the sum-zero subspace.
    assert trace(Q[0]) == 1
    assert all(trace_product(Q[i], Q[j]) == F(1, d*d)
               for i in range(n) for j in range(n) if i != j)
    assert equal(weighted(Q, [F(d, n)] * n), P)
    threshold = d*d
    if t < threshold:
        eta = F(d+1, d) / (t + d)
        w = [F(1) / (t + d)] * n
        alpha = (F(threshold) - t) / (threshold - 1)
        beta = F(threshold) * (t - 1) / (threshold - 1)
        Z = add(P, Q[0], alpha, beta)
        assert alpha > 0 and t > 0
        assert equal(weighted(Q, w), [[eta * x for x in row] for row in P])
    else:
        eta = F(1, threshold)
        w = [F(0)] + [F(1, d)] * d
        Z = [[threshold * x for x in row] for row in Q[0]]
    c = [t] + [F(1)] * d
    assert sum((wi * ci for wi, ci in zip(w, c)), F(0)) == 1
    assert psd(Z)
    assert trace(Z) == 1 / eta
    assert all(trace_product(Q[i], Z) <= c[i] for i in range(n))
    z = [x / eta for x in w]
    assert sum((zi * ci for zi, ci in zip(z, c)), F(0)) == trace(Z)
    assert psd(add(weighted(Q, z), P, F(1), F(-1)))
    if t > threshold:
        assert trace_product(Q[0], Z) < c[0]
    if t == threshold:
        # Every exact threshold optimizer has one freely varying special weight.
        for r in (F(0), F(1, 4), F(1, 2), F(d, d+1)):
            z0 = r
            zo = d * (1-r)
            cand = [z0] + [zo] * d
            assert all(x >= 0 for x in cand)
            assert psd(add(weighted(Q, cand), P, F(1), F(-1)))
            assert sum((ci*zi for ci, zi in zip(c, cand)), F(0)) == threshold
    return 1


if __name__ == '__main__':
    tests = 0
    for d in range(2, 9):
        threshold = d * d
        cases = [F(1, 4), F(1), F(d), F(threshold) - F(1, 7),
                 F(threshold), F(threshold) + F(1, 7),
                 F(threshold + 1), F(2 * threshold)]
        for t in cases:
            tests += check(d, t)
    print(f'VERIFY_OK {tests} exact simplex primal-dual cases; all principal minors checked')
