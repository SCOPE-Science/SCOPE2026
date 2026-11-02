#!/usr/bin/env python3
"""Exact independent Fano-triple construction of the 28-vertex Coxeter graph.
No external libraries or network access required. The analytic exponent proof is in RESULT.md.
"""
from itertools import combinations
from collections import Counter, deque
from math import sqrt, log

N = 28
lines = {frozenset((i, (i + 1) % 7, (i + 3) % 7)) for i in range(7)}
triples = [frozenset(t) for t in combinations(range(7), 3) if frozenset(t) not in lines]
assert len(lines) == 7 and len(triples) == N
adj = [set() for _ in range(N)]
for i, j in combinations(range(N), 2):
    if triples[i].isdisjoint(triples[j]):
        adj[i].add(j)
        adj[j].add(i)
assert all(len(z) == 3 for z in adj)
assert sum(len(z) for z in adj) == 84
D = []
for src in range(N):
    dist = [-1] * N
    dist[src] = 0
    queue = deque([src])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    assert sorted(Counter(dist).items()) == [(0, 1), (1, 3), (2, 6), (3, 12), (4, 6)]
    D.append(dist)
assert all(D[i][j] == D[j][i] for i in range(N) for j in range(N))

A = [[int(j in adj[i]) for j in range(N)] for i in range(N)]
I = [[int(i == j) for j in range(N)] for i in range(N)]
def add(M, T, a=1, b=1):
    return [[a*M[i][j]+b*T[i][j] for j in range(N)] for i in range(N)]
def mult(M, T):
    return [[sum(M[i][k]*T[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
A2 = mult(A, A)
A3 = mult(A2, A)
A4 = mult(A3, A)
assert [sum(M[i][i] for i in range(N)) for M in (I, A, A2, A3)] == [28, 0, 84, 0]
# Confirm the entire degree-five square-free annihilator exactly.
# m(X)=(X-3)(X-2)(X+1)(X^2+2X-1)
B = add(A, I, b=-3)
B = mult(B, add(A, I, b=-2))
B = mult(B, add(A, I))
Q = add(add(A2, A, b=2), I, b=-1)
B = mult(B, Q)
assert not any(v for row in B for v in row)
# Confirm each distance adjacency matrix agrees entrywise with its polynomial.
P = [I, A, add(A2, I, b=-3), add(A3, A, b=-5)]
P4_num = add(add(add(add(A4, A3, b=-1), A2, b=-7), A, b=5), I, b=6)
assert all(v % 2 == 0 for row in P4_num for v in row)
P.append([[v//2 for v in row] for row in P4_num])
for r in range(5):
    assert all(P[r][i][j] == int(D[i][j] == r) for i in range(N) for j in range(N))
# Characteristic polynomial spectral multiplicities follow uniquely from
# the degree-five annihilator and integer trace moments 0,1,2,3:
# eigenvalues: 3^1, 2^8, (-1)^7, (-1 +/- sqrt(2))^6 each.
for q in (0., 0.35, 0.5, 0.5704063373205722, 0.75, 1., 2.):
    val = [sum((r**q if r else 0.0)*P[r][i][j] for r in range(1,5)) for i in range(N) for j in range(N)]
    assert all(abs(val[i*N+j]-val[j*N+i]) < 1e-10 for i in range(N) for j in range(N))

def f(p):
    u = sqrt(2)
    return (-1+u)-2*u*2**p-2*3**p+(2+u)*4**p
lo, hi = 0.0, 1.0
assert f(lo) < 0 < f(hi)
for _ in range(90):
    mid = (lo+hi)/2
    if f(mid) > 0: hi=mid
    else: lo=mid
root = (lo+hi)/2
assert 0.57040 < root < 0.57042
for p in (0., .25, .5, root-1e-5):
    z = 2**p; w=3**p; y=4**p; u=sqrt(2)
    E2=2+z-2*w-2*y
    Eminus=-1-2*z+4*w-2*y
    Elower=-1-u+2*u*z-2*w+(2-u)*y
    assert max(E2,Eminus,Elower) < 0
    assert f(p) < 0
print('COXETER_EXACT_GRAPH_AND_DISTANCE_SPECTRUM_OK vertices=28 edges=42 shells=1,3,6,12,6')
print('COXETER_SHARP_EXPONENT_NUMERIC_CHECK_OK alpha=%.15f' % root)
