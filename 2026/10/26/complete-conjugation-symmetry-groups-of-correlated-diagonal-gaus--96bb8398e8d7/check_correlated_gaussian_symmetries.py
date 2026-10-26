#!/usr/bin/env python3
"""Exact-rational finite test cases for correlated-diagonal Gaussian covariance symmetries.

Run: python3 check_correlated_gaussian_symmetries.py
No nonstandard dependencies. These tests supplement (not replace) the analytic proof.
"""
from fractions import Fraction as F
from itertools import permutations


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(M):
    return list(map(list, zip(*M)))


def multiply(A, B):
    BT = transpose(B)
    return [[sum(x*y for x, y in zip(row, col)) for col in BT] for row in A]


def subtract(A, B):
    return [[x-y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]


def covariance(A, H):
    T = [row[:] for row in H]
    for i in range(len(T)):
        T[i][i] += sum(A[i][j] * H[j][j] for j in range(len(T)))
    return T


def rotated(n, a, b):
    R = eye(n)
    R[a][a], R[b][b] = F(3,5), F(3,5)
    R[a][b], R[b][a] = F(-4,5), F(4,5)
    assert multiply(R, transpose(R)) == eye(n)
    return R


def covariance_equivariant(A, U):
    n = len(A)
    B = []
    for i in range(n):
        H = [[F(0) for _ in range(n)] for _ in range(n)]
        H[i][i] = F(1)
        B.append(H)
    for i in range(n):
        for j in range(i+1,n):
            H = [[F(0) for _ in range(n)] for _ in range(n)]
            H[i][j], H[j][i] = F(1), F(1)
            B.append(H)
    for H in B:
        UHUt = multiply(multiply(U,H),transpose(U))
        lhs = covariance(A,UHUt)
        rhs = multiply(multiply(U,covariance(A,H)),transpose(U))
        if lhs != rhs:
            return False
    return True


def permutation(n,p):
    P = [[F(0) for _ in range(n)] for _ in range(n)]
    for j,i in enumerate(p):
        P[i][j] = F(1)
    return P


def classes(A):
    n = len(A)
    unseen = set(range(n)); out=[]
    while unseen:
        a=min(unseen)
        c=tuple(b for b in sorted(unseen) if A[a]==A[b])
        out.append(c); unseen.difference_update(c)
    return out


def run():
    checks=0
    # Four distinct positive-semidefinite perturbations of the identity.
    for A in [
        [[F(1,3) if i<2 and j<2 else F(2,5) if i>=2 and j>=2 else F(0) for j in range(4)] for i in range(4)],
        [[F(1,3) if i<2 and j<2 else F(1,3) if i>=2 and j>=2 else F(0) for j in range(4)] for i in range(4)],
        [[F(i+1)*F(j+1) for j in range(3)] for i in range(3)],
        [[F(-1,4) for _ in range(4)] for _ in range(4)],
    ]:
        n=len(A); C=classes(A)
        for c in C:
            for a in c:
                for b in c:
                    if a<b:
                        assert covariance_equivariant(A,rotated(n,a,b)); checks+=1
        for a in range(n):
            for b in range(a+1,n):
                if not any(a in c and b in c for c in C):
                    assert not covariance_equivariant(A,rotated(n,a,b)); checks+=1
        Sigma = [[F(i==j)+A[i][j] for j in range(n)] for i in range(n)]
        for p in permutations(range(n)):
            P=permutation(n,p)
            is_covariance_symmetry = multiply(multiply(P,Sigma),transpose(P)) == Sigma
            assert covariance_equivariant(A,P)==is_covariance_symmetry
            checks+=1
    # Explicit exceptional classification and critical negative perturbation case.
    assert classes([[F(1,3) if i<2 and j<2 else F(2,5) if i>=2 and j>=2 else F(0) for j in range(4)] for i in range(4)]) == [(0,1),(2,3)]
    checks+=1
    assert classes([[F(i+1)*F(j+1) for j in range(3)] for i in range(3)]) == [(0,),(1,),(2,)]
    checks+=1
    assert classes([[F(-1,4)]*4 for _ in range(4)]) == [(0,1,2,3)]
    checks+=1
    print(f"PASS: {checks} exact-rational covariance-equivariance and partition checks")

if __name__=='__main__':
    run()
