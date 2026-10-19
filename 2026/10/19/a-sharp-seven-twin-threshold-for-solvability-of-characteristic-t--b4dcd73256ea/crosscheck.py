#!/usr/bin/env python3
"""Independent matrix-multiplication check of finite derived-series dimensions.

Run: python3 crosscheck.py
The matrices are symmetric, with every row summing to zero over F_2.
"""
from itertools import combinations

WANTED = {2:(1,0), 3:(3,1,0), 4:(6,3,2,0),
          5:(10,6,5,1,0), 6:(15,10,9,5,4,0), 7:(21,15,14,14)}

def reduced(vectors, n):
    rows = [list(r) for r in vectors]
    basis = {}
    for row in rows:
        for col in range(n):
            if row[col] and col in basis:
                row = [a ^ b for a,b in zip(row,basis[col])]
            elif row[col]:
                basis[col] = row
                break
    return list(basis.values())

def product(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%2
             for j in range(n)] for i in range(n)]

def comm(A,B):
    X=product(A,B);Y=product(B,A)
    return [[x ^ y for x,y in zip(u,v)] for u,v in zip(X,Y)]

def as_matrix(weights, n, pairs):
    A=[[0]*n for _ in range(n)]
    for k,(i,j) in enumerate(pairs):
        if weights[k]:
            A[i][j] ^= 1; A[j][i] ^= 1
            A[i][i] ^= 1; A[j][j] ^= 1
    return A

def series(n):
    pairs=list(combinations(range(n),2));dim=len(pairs)
    V=[[int(k==j) for k in range(dim)] for j in range(dim)]
    ds=[len(V)]
    for _ in range(8):
        brackets=[]
        mats=[as_matrix(v,n,pairs) for v in V]
        for i,A in enumerate(mats):
            for B in mats[i+1:]:
                C=comm(A,B)
                assert all(C[r][c]==C[c][r] for r in range(n) for c in range(n))
                assert all(sum(row)%2==0 for row in C)
                brackets.append([C[a][b] for a,b in pairs])
        W=reduced(brackets,dim)
        ds.append(len(W))
        if not W or len(W)==len(V):break
        V=W
    return tuple(ds)

for n, expected in WANTED.items():
    observed=series(n)
    assert observed==expected,(n,observed,expected)
print('INDEPENDENT_MATRIX_BRACKET_CHECK_OK')
