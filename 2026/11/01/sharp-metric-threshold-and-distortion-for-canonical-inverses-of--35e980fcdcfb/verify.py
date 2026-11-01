#!/usr/bin/env python3
"""Supplementary finite tests of rank-one canonical inverses; standard library only.
These calculations are not proofs of infinite-dimensional statements.
"""
import cmath
import math
from fractions import Fraction


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def adj(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]


def minus(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def nrm(A):
    return math.sqrt(sum(abs(z)**2 for row in A for z in row))


I = [[1+0j, 0j], [0j, 1+0j]]
checks = 0
for numerator in range(0, 40):
    s = Fraction(numerator, 20)
    if s >= 2:
        continue
    L = Fraction(1, 1) / (2-s)
    b2 = (s-1)**2 / (2-s)
    assert L-s == b2
    checks += 1
    for k in range(8):
        sf = float(s)
        a = math.sqrt(sf) * cmath.exp(2j*math.pi*k/8)
        b = (sf-1)/math.sqrt(2-sf)
        T = [[a, 0j], [b, 0j]]
        Tst = adj(T)
        S = minus([[2*v for v in row] for row in Tst], mul(mul(Tst, Tst), T))
        beta = minus(minus(mul(mul(Tst, Tst), mul(T,T)), [[2*v for v in row] for row in mul(Tst,T)]),
                     [[-v for v in row] for row in I])
        assert nrm(mul(T,beta)) < 2e-11
        assert nrm(minus(mul(mul(T,S),T),T)) < 2e-11
        assert nrm(minus(mul(mul(S,T),S),S)) < 2e-11
        P, Q = mul(S,T),mul(T,S)
        assert nrm(minus(mul(P,P),P)) < 2e-11
        assert nrm(minus(mul(Q,Q),Q)) < 2e-11
        checks += 5
        if float(L) < 2:
            G = [[2-float(L), 0], [0, 2.]]
            assert nrm(minus(mul(G,P),mul(adj(P),G))) < 2e-11
            assert nrm(minus(mul(G,Q),mul(adj(Q),G))) < 2e-11
            checks += 2
        elif sf > 1.5:
            assert sf * (2-float(L)) < 0
            checks += 1
        else:
            assert nrm(mul(Q,P)) < 2e-11 and nrm(mul(P,Q)) > .1
            checks += 1
print(f"PASS: {checks} finite exact-fraction/numerical checks; proof is analytic.")
