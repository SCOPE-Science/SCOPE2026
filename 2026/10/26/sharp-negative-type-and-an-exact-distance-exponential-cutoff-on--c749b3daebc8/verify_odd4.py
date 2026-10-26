#!/usr/bin/env python3
"""Exact arithmetic verification for the 35-point odd-graph metric.
Uses Python standard library. No external files or dependencies.
"""
from itertools import combinations
from math import comb, log, exp
from fractions import Fraction
from collections import deque

n, k = 7, 3
V = list(combinations(range(n), k))
N = len(V)
assert N == 35
sets = [set(v) for v in V]
A = [[[int(k - len(sets[a] & sets[b]) == i) for b in range(N)] for a in range(N)] for i in range(k+1)]
assert all(sum(A[i][0]) == [1,12,18,4][i] for i in range(4))
# BFS on disjointness adjacency, independently verifying the distance formula.
for a in range(N):
    d = [-1] * N
    d[a] = 0
    Q = deque([a])
    while Q:
        u = Q.popleft()
        for v in range(N):
            if A[3][u][v] and d[v] < 0:
                d[v] = d[u] + 1
                Q.append(v)
    for b in range(N):
        t = len(sets[a] & sets[b])
        assert d[b] == min(2*(3-t),2*t+1)

# All Eberlein character eigenvalues, with their dimensions.
def cb(x,y):
    return comb(x,y) if 0 <= y <= x else 0
pij = [[sum((-1)**t * cb(j,t) * cb(k-j,i-t) * cb(n-k-j,i-t)
            for t in range(j+1)) for i in range(4)] for j in range(4)]
assert pij == [[1,12,18,4], [1,5,-3,-3], [1,0,-3,2], [1,-3,3,-1]], pij
mult = [cb(n,j)-cb(n,j-1) for j in range(4)]
assert mult == [1,6,14,14]

# Check the spectral decomposition directly, without floating-point eigenvalues.
B = A[3]
I = [[int(i==j) for j in range(N)] for i in range(N)]
def mul(X,Y):
    return [[sum(X[a][b]*Y[b][c] for b in range(N)) for c in range(N)] for a in range(N)]
def mpoly(roots):
    coeff=[1]
    for r in roots:
        nxt=[0]*(len(coeff)+1)
        for q,v in enumerate(coeff):
            nxt[q] -= r*v
            nxt[q+1] += v
        coeff=nxt
    return coeff
powers=[I]
for j in range(1,4):powers.append(mul(powers[-1],B))
lambdas=[pij[j][3] for j in range(4)]
assert lambdas==[4,-3,2,-1]
num=[]; den=[]
for j in range(4):
    roots=[lambdas[h] for h in range(4) if h!=j]
    coeff=mpoly(roots)
    Q=[[sum(coeff[t]*powers[t][a][b] for t in range(4)) for b in range(N)] for a in range(N)]
    dj=1
    for r in roots:dj *= lambdas[j]-r
    assert sum(Q[a][a] for a in range(N)) == mult[j]*dj
    for i in range(4):
        C=mul(A[i],Q)
        assert all(C[a][b]==pij[j][i]*Q[a][b] for a in range(N) for b in range(N))
    num.append(Q); den.append(dj)
for a in range(N):
    for b in range(N):
        assert sum(Fraction(num[j][a][b],den[j]) for j in range(4)) == (a==b)

# Distance and ordinary covariance multipliers in the Eberlein sectors.
D1 = [pij[j][3]+2*pij[j][1]+3*pij[j][2] for j in range(4)]
assert D1 == [82,-2,-7,2]
# At x = exp(-t), K_t spectrum equals [1 + A_3*x + A_1*x**2 + A_2*x**3]
F = [[1,pij[j][3],pij[j][1],pij[j][2]] for j in range(4)]
assert F==[[1,4,12,18],[1,-3,5,-3],[1,2,0,-3],[1,-1,-3,3]]
for x in [Fraction(i,50) for i in range(51)]:
    values=[sum(coef*x**a for a,coef in enumerate(row)) for row in F]
    assert values[1] == (1-x)*(1-2*x+3*x*x)
    assert values[2] == (1-x)*(1+3*x+3*x*x)
    assert values[3] == (1-x)*(1-3*x*x)
    expected=(x==1 or (0<=x<1 and x*x<=Fraction(1,3)))
    assert (min(values)>=0)==expected
assert sum(mult)==35
# Analytical root uniqueness uses monotonicity of 3(3**p-2**p)-1.
lo, hi = 0., 1.
for _ in range(70):
    md=(lo+hi)/2
    if 3*(3**md - 2**md) - 1 < 0:lo=md
    else:hi=md
pstar=(lo+hi)/2
assert .5165<pstar<.5167
print('VERIFY_OK')
print('vertices',N,'sector_multiplicities',mult)
print('Eberlein_rows',pij)
print('distance_eigenvalues_p1',D1)
print('ordinary_heat_polynomials',F)
print('pstar_approx',format(pstar,'.15f'))
print('endpoint_squared_embedding_dimension',mult[1]+mult[2])
print('critical_heat_matrix_rank',1+mult[1]+mult[2])
