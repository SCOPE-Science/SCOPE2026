#!/usr/bin/env python3
"""Standalone small-field checks for commuting tuples in the strictly upper-triangular 4-by-4 Lie algebra.

No external Python packages are required. Running this program does not establish geometric
irreducibility or the general symbolic theorem; those require the accompanying proof.
"""
from itertools import product
import random


def mul(u, v, q):
    if q == 4:
        a, b = (u & 1), (u >> 1)
        c, d = (v & 1), (v >> 1)
        constant = (a & c) ^ (b & d)
        linear = (a & d) ^ (b & c) ^ (b & d)
        return constant | (linear << 1)
    return (u * v) % q


def add(u, v, q):
    return u ^ v if q == 4 else (u + v) % q


def neg(u, q):
    return u if q == 4 else (-u) % q


def mat_mul(A, B, q):
    out = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for k in range(i + 1, 4):
            for j in range(k + 1, 4):
                out[i][j] = add(out[i][j], mul(A[i][k], B[k][j], q), q)
    return out


def comm(A, B, q):
    p, s = mat_mul(A, B, q), mat_mul(B, A, q)
    return [[add(p[i][j], neg(s[i][j], q), q) for j in range(4)] for i in range(4)]


def matrix(x):
    a, b, c, d, e, f = x
    return [[0, a, d, f], [0, 0, b, e], [0, 0, 0, c], [0, 0, 0, 0]]


def rank(A, q):
    A = [row[:] for row in A]
    piv = 0
    for col in range(len(A[0])):
        i = next((j for j in range(piv, len(A)) if A[j][col]), None)
        if i is None:
            continue
        A[piv], A[i] = A[i], A[piv]
        if q == 4:
            v = A[piv][col]
            inv = {1: 1, 2: 3, 3: 2}[v]
        else:
            inv = pow(A[piv][col], -1, q)
        A[piv] = [mul(z, inv, q) for z in A[piv]]
        for j in range(piv + 1, len(A)):
            scalar = A[j][col]
            if scalar:
                A[j] = [add(x, neg(mul(scalar, y, q), q), q) for x, y in zip(A[j], A[piv])]
        piv += 1
        if piv == len(A):
            break
    return piv


def count_by_adjoint(q):
    E = [matrix(tuple(int(j == i) for j in range(6))) for i in range(6)]
    count = 0
    for x in product(range(q), repeat=6):
        X = matrix(x)
        cols = [comm(X, Y, q) for Y in E]
        M = [[C[i][j] for C in cols] for i, j in [(0, 1), (1, 2), (2, 3), (0, 2), (1, 3), (0, 3)]]
        count += q ** (6 - rank(M, q))
    return count


def predicted(q, r):
    Q = q ** r
    L = (q + 1) * (q*q + 1)
    isotropic = 1 + (q**3 + q*q + q + 1) * (Q - 1) + L * (Q - 1) * (Q - q)
    nonzero_b = (Q - 1) * (q ** (2*r) + (q*q - 1) * q ** (r+1))
    return Q * (isotropic + nonzero_b)


def count_tuple_rows(q, r):
    vectors = list(product(range(q), repeat=r))
    count = 0
    for b in vectors:
        for a in vectors:
            for c in vectors:
                if any((a[i]*b[j]-a[j]*b[i])%q or (b[i]*c[j]-b[j]*c[i])%q
                       for i in range(r) for j in range(i+1, r)):
                    continue
                for d in vectors:
                    for e in vectors:
                        if all((a[i]*e[j]-a[j]*e[i]+d[i]*c[j]-d[j]*c[i])%q == 0
                               for i in range(r) for j in range(i+1, r)):
                            count += q ** r  # the top-right entries are arbitrary
    return count


def verify_coefficient_equations():
    rng = random.Random(190713)
    for q in (2, 3, 4, 5):
        for _ in range(500):
            x = [rng.randrange(q) for _ in range(6)]
            y = [rng.randrange(q) for _ in range(6)]
            got = comm(matrix(x), matrix(y), q)
            expected13 = add(mul(x[0], y[1], q), neg(mul(y[0], x[1], q), q), q)
            expected24 = add(mul(x[1], y[2], q), neg(mul(y[1], x[2], q), q), q)
            expected14 = 0
            for u, v, sg in ((x[0], y[4], 1), (y[0], x[4], -1),
                             (x[3], y[2], 1), (y[3], x[2], -1)):
                z = mul(u, v, q)
                expected14 = add(expected14, z if sg == 1 else neg(z, q), q)
            assert got[0][2] == expected13
            assert got[1][3] == expected24
            assert got[0][3] == expected14
            assert all(got[i][j] == 0 for i in range(4) for j in range(4)
                       if (i, j) not in ((0, 2), (1, 3), (0, 3)))


def main():
    verify_coefficient_equations()
    print('PASS 2000 literal commutator coefficient comparisons over F2,F3,F4,F5')
    for q, r in ((2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (5, 1)):
        got, want = count_tuple_rows(q, r), predicted(q, r)
        assert got == want, (q, r, got, want)
        print('PASS direct tuple enumeration', q, r, got)
    for q in (2, 3, 4, 5):
        got, want = count_by_adjoint(q), predicted(q, 2)
        assert got == want, ('adjoint', q, got, want)
        print('PASS independent adjoint rank enumeration', q, 2, got)
    print('VERIFY_OK_UT4_COMMUTING_TUPLES')


if __name__ == '__main__':
    main()
