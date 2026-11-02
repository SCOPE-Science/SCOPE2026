#!/usr/bin/env python3
"""Independent exact-integer checks for cyclic path algebra Cartan matrices.
Run: python check_smith.py. Requires sympy.
"""
from math import gcd
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def concrete_matrix(n, L, a):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(L):
            C[i][(i + j) % n] += a ** j
    return Matrix(C)


def predicted(n, L, a):
    g = gcd(n, L)
    h = n * L // g
    D = a ** h - 1
    B = sum(a ** (n * j) for j in range(L // g))
    return [1] * (n - g) + [B] + [D] * (g - 1)


def nonzero_invariants(M):
    S = smith_normal_form(M, domain=ZZ)
    return [abs(int(S[i, i])) for i in range(M.rows)]


cases = 0
for n in range(1, 10):
    for L in range(2, 13):
        for a in range(1, 5):
            C = concrete_matrix(n, L, a)
            actual = nonzero_invariants(C)
            expected = predicted(n, L, a)
            assert actual == expected, (n, L, a, actual, expected)
            cases += 1
# Separate, larger and intentionally non-coprime parameter checks.
for n, L, a in [
    (12, 18, 2), (12, 8, 3), (14, 21, 2), (15, 10, 2),
    (16, 12, 2), (18, 24, 2), (9, 15, 5), (10, 16, 3),
    (20, 12, 2), (11, 25, 2)
]:
    assert nonzero_invariants(concrete_matrix(n, L, a)) == predicted(n, L, a), (n, L, a)
    cases += 1
# Direct rank checks modulo primes, independently of Smith routine.

def modrank(M, p):
    A = [[int(x) % p for x in row] for row in M.tolist()]
    n = len(A)
    r = 0
    for col in range(n):
        pivot = next((i for i in range(r, n) if A[i][col] % p), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][col], -1, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(n):
            if i == r:
                continue
            f = A[i][col]
            if f:
                A[i] = [(u - f * v) % p for u, v in zip(A[i], A[r])]
        r += 1
    return r

rank_checks = 0
for n in range(1, 10):
    for L in range(2, 11):
        for a in [1, 2, 3]:
            M = concrete_matrix(n, L, a)
            g = gcd(n, L)
            D = a ** (n * L // g) - 1
            B = sum(a ** (n * j) for j in range(L // g))
            for p in [2, 3, 5, 7, 11, 13]:
                nullity = (g - 1) * (D % p == 0) + (B % p == 0)
                assert modrank(M, p) == n - nullity, (n, L, a, p)
                rank_checks += 1
print(f'CYCLIC_NAKAYAMA_WEIGHTED_SMITH_OK {cases}_INTEGER_SNF {rank_checks}_DIRECT_MODULAR_RANK')
print('EXAMPLE n=6 L=4 a=2:', predicted(6, 4, 2))
print('EXAMPLE n=6 L=4 a=1:', predicted(6, 4, 1))
