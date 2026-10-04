#!/usr/bin/env python3
from itertools import product
from collections import deque

def mat(t):
    a,b,c,d,e,f=t
    return ((a,b,c),(0,d,e),(0,0,f))

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) % 2
                       for j in range(3)) for i in range(3))

ZERO=((0,0,0),(0,0,0),(0,0,0))
I=((1,0,0),(0,1,0),(0,0,1))
ALL=[mat(t) for t in product((0,1), repeat=6)]

units=[]
for A in ALL:
    if any(mm(A,B)==I and mm(B,A)==I for B in ALL):
        units.append(A)

vertices=[A for A in ALL if A != ZERO and A not in units]

# Independently confirm the vertex definition by one-sided annihilation.
for A in vertices:
    assert any(B != ZERO and (mm(A,B)==ZERO or mm(B,A)==ZERO) for B in ALL)
for A in units:
    assert not any(B != ZERO and (mm(A,B)==ZERO or mm(B,A)==ZERO) for B in ALL)

edges=[]
adj=[set() for _ in vertices]
for i,A in enumerate(vertices):
    for j in range(i+1, len(vertices)):
        B=vertices[j]
        if mm(A,B)==ZERO or mm(B,A)==ZERO:
            edges.append((i,j))
            adj[i].add(j)
            adj[j].add(i)

diameter=0
for s in range(len(vertices)):
    d={s:0}
    q=deque([s])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v]=d[u]+1
                q.append(v)
    assert len(d)==len(vertices)
    diameter=max(diameter, max(d.values()))

# Diagonal criterion cross-check: over F_2 a triangular matrix is a unit
# exactly when all three diagonal entries are 1.
diag_units=[A for A in ALL if A[0][0]==A[1][1]==A[2][2]==1]
assert set(diag_units)==set(units)

assert len(ALL)==64
assert len(units)==8
assert len(vertices)==55
assert len(edges)==420
assert diameter==2

print("VERIFY_OK")
print("ring_elements=64")
print("units=8")
print("nonzero_zero_divisors=55")
print("underlying_simple_edges=420")
print("diameter=2")
