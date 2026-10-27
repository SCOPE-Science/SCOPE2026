#!/usr/bin/env python3
"""Exact-arithmetic tests for the Legendre parity-boundary identity.
Uses only Python's standard library. The all-order theorem is analytic;
this script checks recurrence-based finite cases as a consistency test.
"""
from fractions import Fraction as F

def mats(n):
    # M is multiplication by theta compressed to P_0,...,P_{n-1}
    # U is multiplication by theta^2 compressed to the same basis.
    def t(k):
        return {k-1:F(k,2*k+1) if k>=1 else F(0), k+1:F(k+1,2*k+1)}
    T=[[F(0) for _ in range(n)] for _ in range(n)]
    U=[[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for i,a in t(j).items():
            if 0<=i<n:T[i][j]+=a
            for k,b in t(i).items():
                if 0<=k<n:U[k][j]+=a*b
    return T,U

for n in range(1,51):
    T,U=mats(n)
    D=[(-1)**j for j in range(n)]
    assert all(D[i]*T[i][j]*D[j] == -T[i][j] for i in range(n) for j in range(n))
    assert all(D[i]*U[i][j]*D[j] == U[i][j] for i in range(n) for j in range(n))
    for i in range(n):
        for j in range(n):
            val=sum(T[i][k]*T[k][j] for k in range(n))
            if i==n-1 and j==n-1: val+=F(n*n,4*n*n-1)
            assert U[i][j]==val, (n,i,j)
    trace=sum(D[i]*U[i][i] for i in range(n))
    expected=F((-1)**(n-1)*n*n,4*n*n-1)
    assert trace == expected, (n,trace,expected)
    for j in range(n):
        aj=F(j*j,4*j*j-1) if j else F(0)
        aj1=F((j+1)*(j+1),4*(j+1)*(j+1)-1)
        assert U[j][j]==aj+aj1
T,U=mats(2)
assert T==[[F(0),F(1,3)],[F(1),F(0)]]
assert U==[[F(1,3),F(0)],[F(0),F(3,5)]]
print('VERIFY_OK: exact Legendre recurrence, parity, telescoping trace, s=1..50; exact s=2 blocks')
