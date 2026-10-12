#!/usr/bin/env python3
"""Exact rational checks for the scalar two-curvature loopless-SVRG theorem.

Run: python3 verify.py
Requires only Python 3's standard library. Algebraic proofs appear in RESULT.md;
finite checks here guard the moment-map and polynomial identities.
"""
from fractions import Fraction as F


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def scale(z, A):
    return [[z * A[i][j] for j in range(2)] for i in range(2)]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def tr(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]


def determinant(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def T(C, h, v, p):
    r = 1 - h
    Z = [[F(0), F(0)], [F(0), F(0)]]
    for s in (-1, 1):
        for refresh, weight in ((True, p / 2), (False, (1 - p) / 2)):
            if not weight:
                continue
            B = [[r - h * s * v, h * s * v],
                 [F(1), F(0)] if refresh else [F(0), F(1)]]
            Z = add(Z, scale(weight, mul(mul(B, C), tr(B))))
    return Z


def matrices(h, v, p):
    r = 1 - h
    d = p + (1 - p) * h
    y = p * r / d
    P = [[F(1), y], [y, F(1)]]
    E = [[F(1), F(0)], [F(0), F(0)]]
    K = add(E, T(E, h, v, p))
    Q = (p - 1 - 2 * v * v) * h * h + (2 - 3 * p) * h + 2 * p
    delta = h * Q / d
    return P, E, K, Q, delta


def test_case(h, v, p):
    P, E, K, Q, delta = matrices(h, v, p)
    assert determinant(P) > 0 and P[0][0] > 0
    assert determinant(K) > 0 and K[0][0] > 0
    assert T(P, h, v, p) == add(P, scale(-delta, E))
    assert T(T(P, h, v, p), h, v, p) == add(P, scale(-delta, K))
    C = [[F(1), F(1)], [F(1), F(1)]]
    for _ in range(3):
        C = T(C, h, v, p)
        assert C[0][0] >= 0 and C[1][1] >= 0 and determinant(C) >= 0
    # At positive heterogeneity and h != 0, the physical initial vector
    # generates a positive-definite second-moment matrix by step three.
    assert determinant(C) > 0
    return 1


def test_witness():
    h, v = F(5, 4), F(1, 2)
    assert matrices(h, v, F(1, 4))[3] == F(7, 64)
    assert matrices(h, v, F(1))[3] == -F(1, 32)
    c0 = [[F(1), F(1)], [F(1), F(1)]]
    result = {}
    for p in (F(1, 4), F(1)):
        c = c0
        for _ in range(40):
            c = T(c, h, v, p)
        result[p] = c[0][0]
    assert result[F(1, 4)] < F(1, 5)
    assert result[F(1)] > F(1)
    # At the p=1/2 slice, the earlier fixed-probability boundary is recovered.
    for v in (F(1, 5), F(1, 2), F(4, 5)):
        p = F(1, 2)
        for h in (F(1, 5), F(7, 10), F(6, 5)):
            q = matrices(h, v, p)[3]
            assert 2 * q == 2 + h - (1 + 4 * v * v) * h * h
    return result


def run():
    count = 0
    for hn in range(1, 20):
        h = F(hn, 10)
        for vn in range(1, 10):
            v = F(vn, 10)
            for pn in range(1, 11):
                count += test_case(h, v, F(pn, 10))
    witness = test_witness()
    print(f"PASS: {count} exact rational transition/positivity/identity cases")
    print("PASS: exact witness and fixed-probability specialization")
    print("Witness E[x_40^2]: p=1/4 ->", witness[F(1, 4)])
    print("Witness E[x_40^2]: p=1   ->", witness[F(1)])


if __name__ == '__main__':
    run()
