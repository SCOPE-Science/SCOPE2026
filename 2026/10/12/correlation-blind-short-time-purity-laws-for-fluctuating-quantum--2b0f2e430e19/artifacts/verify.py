#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def exchange(n, e):
    i, j = e
    A = [[0 for _ in range(n)] for _ in range(n)]
    A[i][j] = 1
    A[j][i] = 1
    return A


def local_expect(A, v):
    return A[v][v]

for n in range(2, 9):
    edges = list(combinations(range(n), 2))
    V = [exchange(n, e) for e in edges]

    # Hilbert--Schmidt Gram matrix.
    for a, A in enumerate(V):
        for b, B in enumerate(V):
            got = trace(matmul(A, B))
            want = 2 if a == b else 0
            assert got == want, (n, a, b, got, want)

    # Exact localized K_v.
    for v in range(n):
        for a, A in enumerate(V):
            ma = local_expect(A, v)
            assert ma == 0
            for b, B in enumerate(V):
                mb = local_expect(B, v)
                anti = add(matmul(A, B), matmul(B, A))
                K = Fraction(local_expect(anti, v), 2) - ma * mb
                want = 1 if (a == b and v in edges[a]) else 0
                assert K == want, (n, v, a, b, K, want)

    # Homogeneous coefficient simplifications after factoring J^2 Delta t xi(1-xi).
    local_coeff = 2 * (n - 1)
    haar_coeff_from_trace = Fraction(4, n + 1) * Fraction(n * (n - 1), 2)
    haar_coeff_closed = Fraction(2 * n * (n - 1), n + 1)
    assert haar_coeff_from_trace == haar_coeff_closed
    assert local_coeff == 2 * (n - 1)

print('VERIFY_OK')
