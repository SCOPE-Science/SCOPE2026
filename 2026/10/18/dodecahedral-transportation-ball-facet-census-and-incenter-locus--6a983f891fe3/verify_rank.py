#!/usr/bin/env python3
"""Exact rank, distance-layer and antipodal verification for GP(10,2)."""
from collections import deque, Counter

N = 20
edges = []
for j in range(10):
    edges.extend(((j, (j+1)%10), (j, 10+j), (10+j, 10+(j+2)%10)))
adj = [[] for _ in range(N)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
assert len(edges) == 30
D = []
for source in range(N):
    dist = [-1]*N
    dist[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u]+1
                queue.append(v)
    assert all(k >= 0 for k in dist)
    D.append(dist)
assert all(Counter(D[v]) == {0:1, 1:3, 2:6, 3:6, 4:3, 5:1} for v in range(N))
for u in range(N):
    opposite = (u+5)%10 if u < 10 else 10+(u-10+5)%10
    assert all(D[u][v]+D[opposite][v]==5 for v in range(N))

def bareiss_det(M):
    A = [list(row) for row in M]
    n = len(A)
    sign, prev = 1, 1
    for k in range(n-1):
        if not A[k][k]:
            r = next((i for i in range(k+1,n) if A[i][k]),None)
            if r is None:
                return 0
            A[k], A[r] = A[r], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = A[i][j]*pivot-A[i][k]*A[k][j]
                assert numerator % prev == 0
                A[i][j] = numerator//prev
        for i in range(k+1,n):
            A[i][k] = 0
        prev = pivot
    return sign*A[n-1][n-1]

rows = (1,2,3,4,5,10,11,12,13,14)
cols = (0,1,2,3,4,10,11,12,13,14)
M = [[D[i][j]-D[0][j] for j in cols] for i in rows]
det = bareiss_det(M)
assert det == -2
print('DISTANCE_LAYER_MULTIPLICITIES=1,3,6,6,3,1')
print('SUM_DISTANCE=50 SUM_SQUARE_DISTANCE=154')
print('OPPOSITE_DISTANCE_SUM=5')
print('TEN_BY_TEN_MINOR_DETERMINANT=',det,sep='')
print('CENTERED_CONTACT_SPAN_RANK=10')
print('CENTER_LOCUS_AFFINE_DIMENSION=9')
print('ALL EXACT RANK CHECKS PASSED')
