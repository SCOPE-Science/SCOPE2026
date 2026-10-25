#!/usr/bin/env python3
"""Exact finite-coordinate consistency checks for a Hilbert evolution algebra.

The infinite-dimensional claims require the independent mathematical proof;
this program checks algebraic constraints on finite coordinate windows.
"""
from fractions import Fraction as F


def transpose(a):
    return [list(col) for col in zip(*a)]


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def householder(m):
    v = [F(i + 1) for i in range(m)]
    d = dot(v, v)
    return [[F(int(i == j))-2*v[i]*v[j]/d for j in range(m)] for i in range(m)]


def matrix_for_evolution(m, output_n):
    # Output e_1..e_n, input e_1..e_{m+n-1}.
    k = m+output_n-1
    L = [[F(0) for j in range(k)] for i in range(output_n)]
    for j in range(m):
        L[0][j] = F(1)
    for j in range(m, k):
        L[j-m+1][j] = F(1)
    return L


def rank(A):
    a = [row[:] for row in A]
    r = 0
    cols = len(a[0])
    for j in range(cols):
        pivot = next((i for i in range(r,len(a)) if a[i][j]), None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        v=a[r][j]
        a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][j]:
                w=a[i][j]
                a[i]=[a[i][c]-w*a[r][c] for c in range(cols)]
        r+=1
        if r==len(a): break
    return r


def check(m,n):
    k=m+n-1
    L=matrix_for_evolution(m,n)
    assert rank(L)==n
    assert k-rank(L)==m-1
    R=householder(m)
    assert all(dot(R[i],R[j])==int(i==j) for i in range(m) for j in range(m))
    U=[[F(int(i==j)) for j in range(k)] for i in range(k)]
    for i in range(m):
        for j in range(m):
            U[i][j]=R[i][j]
    # Check every cross-product in these k input coordinates vanishes.
    for j in range(k):
        for h in range(j+1,k):
            v=[U[i][j]*U[i][h] for i in range(k)]
            assert all(dot(row,v)==0 for row in L)
    assert any(sum(U[i][0]!=0 for i in range(m))>1 for _ in [0])
    print('m=',m,'output_n=',n,'rank=',n,'kernel=',m-1,'orthogonal_columns=',k,'ok')


if __name__=='__main__':
    for m in (2,3,4,5,6):
        check(m,m+4)
    print('VERIFY_OK')
