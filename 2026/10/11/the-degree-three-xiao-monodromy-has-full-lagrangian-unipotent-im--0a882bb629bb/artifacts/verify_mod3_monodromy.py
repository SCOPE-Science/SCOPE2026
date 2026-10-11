#!/usr/bin/env python3
from itertools import combinations_with_replacement, product

p=3
reps=[(1,0),(0,1),(1,1),(1,2)]

def outer(v):
    a,b=v
    return ((a*a)%p,(a*b)%p,(b*b)%p)
M=[outer(v) for v in reps]

def add(A,B): return tuple((x+y)%p for x,y in zip(A,B))
def scale(c,A): return tuple((c*x)%p for x in A)
Z=(0,0,0)

sol=[]
for inds in combinations_with_replacement(range(4),4):
    s=Z
    for i in inds: s=add(s,M[i])
    if s==Z: sol.append(inds)
assert sol==[(0,1,2,3)], sol

span=set()
for coeffs in product(range(3), repeat=4):
    s=Z
    for c,A in zip(coeffs,M): s=add(s,scale(c,A))
    span.add(s)
assert len(span)==27

def T(B):
    a,b,c=B
    return ((1,0,a,b),(0,1,b,c),(0,0,1,0),(0,0,0,1))

def mm(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return tuple(tuple(sum(A[i][t]*B[t][j] for t in range(k))%p for j in range(m)) for i in range(n))
I=tuple(tuple(1 if i==j else 0 for j in range(4)) for i in range(4))
prodM=I
for B in M: prodM=mm(prodM,T(B))
assert prodM==I
G={T(B) for B in span}
assert len(G)==27
for A in G:
    for B in G:
        assert mm(A,B)==mm(B,A)
print('VERIFY_OK projective_lines=4 unique_zero_sum_multiset=true span_dim=3 group_order=27')
