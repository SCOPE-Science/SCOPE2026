#!/usr/bin/env python3
"""Exact finite checks for the all-degree harmonic spectrum on 56 Gosset points.
Only Python's standard library is needed. The infinite-degree bound is proven in
RESULT.md; this script checks its rational input and finite spectral identities.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

EDGES = tuple(combinations(range(8),2))
N = len(EDGES)
assert N == 28
S = [[(0 if a==b else (1 if len(set(e)&set(f))==1 else -1))
      for b,f in enumerate(EDGES)] for a,e in enumerate(EDGES)]
# Every equiangular pair has the stipulated dot product.
for i in range(N):
    assert S[i][i] == 0
    for j in range(N):
        if i != j:
            overlap = len(set(EDGES[i])&set(EDGES[j]))
            assert F(S[i][j],3) == F(2*overlap-1,3)
# Exact Seidel minimal polynomial (x-9)(x+3) and trace.
for i in range(N):
    for j in range(N):
        lhs = sum(S[i][h]*S[h][j] for h in range(N)) - 6*S[i][j] - (27 if i==j else 0)
        assert lhs == 0
assert sum(S[i][i] for i in range(N))==0
# Hence eigenvalue 9 with mult.7 and -3 with mult.21.

def gegenbauer_values(maxdegree):
    out = [F(1),F(1,3)]
    for k in range(2,maxdegree+1):
        out.append((F(2*k+3,3)*out[-1]-(k-1)*out[-2])/(k+4))
    return out[:maxdegree+1]

values = gegenbauer_values(30)
assert values[:10]==[F(1),F(1,3),F(-1,27),F(-1,9),F(-1,27),F(23,729),F(25,729),F(1,2187),F(-389,19683),F(-215,19683)]
assert all(abs(values[k]) < F(1,27) for k in range(5,10))
# Gegenbauer integral: U^2 ~ Beta(1/2,5/2).
# B10=E(1/9+8U^2/9)^5; for every degree >=10, |P_k(1/3)| <= B10.
B10 = sum(F(comb(5,j)*8**j,9**5) *
          __import__('math').prod(F(2*i+1,2*i+6) for i in range(j))
          for j in range(6))
assert B10 == F(965,59049) and B10 < F(1,27)

def matrix_rank(A):
    A = [list(map(F,row)) for row in A]
    rows,cols=len(A),len(A[0])
    pivot_row=0
    for col in range(cols):
        idx=next((r for r in range(pivot_row,rows) if A[r][col]!=0),None)
        if idx is None: continue
        A[pivot_row],A[idx]=A[idx],A[pivot_row]
        t=A[pivot_row][col]
        A[pivot_row]=[z/t for z in A[pivot_row]]
        for r in range(pivot_row+1,rows):
            t=A[r][col]
            if t:
                A[r]=[z-t*w for z,w in zip(A[r],A[pivot_row])]
        pivot_row+=1
        if pivot_row==rows:break
    return pivot_row

ranks = []
for k,c in enumerate(values[:13]):
    K = [[F(1) if i==j else (c if k%2==0 else c*S[i][j])
          for j in range(N)] for i in range(N)]
    actual = matrix_rank(K)
    if k%2==0:
        eig=[(1+27*c,1),(1-c,27)]
    else:
        eig=[(1+9*c,7),(1-3*c,21)]
    assert all(e>=0 for e,m in eig)
    predicted = sum(m for e,m in eig if e)
    assert actual==predicted,(k,actual,predicted)
    ranks.append(actual)
assert ranks==[1,7,27,21,27,28,28,28,28,28,28,28,28]
assert ranks[4]+ranks[5]==55
assert ranks[5]+ranks[6]==56
print('GOSSET_HARMONIC_EXACT_CHECK_OK',len(EDGES),len(values),str(B10),ranks)
