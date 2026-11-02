#!/usr/bin/env python3
"""Exact symbolic/finite verification for one-step cyclic Rule 54 preimage extrema."""
from itertools import product

def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))
def add(a,b):
    return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def sub(a,b):
    return tuple(tuple(x-y for x,y in zip(r,s)) for r,s in zip(a,b))
def tr(a): return sum(a[i][i] for i in range(len(a)))
def ge(a,b): return all(x>=y for r,s in zip(a,b) for x,y in zip(r,s))
def mat(xs): return tuple(tuple(row) for row in xs)
I=mat([[int(i==j) for j in range(4)] for i in range(4)])
A=mat([[1,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,1,1]])
B=mat([[0,1,0,0],[0,0,1,0],[1,1,0,0],[0,0,0,0]])
U=mat([[1,0],[0,1],[0,0],[0,1]])
V=mat([[1,0,0,0],[0,0,1,1]])
assert mm(A,A)==mm(A,mm(A,A))
assert mm(mm(A,A),I)==mm(U,V)
assert mm(V,U)==mat([[1,0],[0,1]])
assert mm(mm(B,B),mm(B,B))==add(mm(B,B),B)
assert ge(mm(mm(B,B),B),mm(mm(B,A),B))
BP=[I]
for n in range(1,31): BP.append(mm(BP[-1],B))
C=[mm(mm(V,m),U) for m in BP]
assert C[:8]==list(map(mat,[ [[1,0],[0,1]],[[0,1],[1,1]],[[0,0],[0,1]],[[1,1],[1,1]],[[0,1],[1,2]],[[1,1],[1,2]],[[1,2],[2,3]],[[1,2],[2,4]] ]))
# pair merge, base 1..6; one exceptional pair (1,1)
for a in range(1,7):
    for b in range(1,7):
        D=sub(C[a+b+2],mm(C[a],C[b]))
        if (a,b)!=(1,1):
            assert ge(D,((0,0),(0,0))), (a,b,D)
            assert tr(D)>0,(a,b,D)
assert ge(C[7],mm(mm(C[1],C[1]),C[1]))
assert tr(C[7])>tr(mm(mm(C[1],C[1]),C[1]))
# the g(a,b) strict singleton elimination when one double-zero run remains
for a in range(1,7):
    for b in range(1,7):
        if a+b>=5:
            gap=tr(mm(mm(A,A), BP[a+b+1]))-tr(mm(mm(mm(mm(A,A),BP[a]),A),BP[b]))
            assert gap>0,(a,b,gap)
# sequence comparisons and short-word exceptions, recurrence carries forward.
P=[1,1,1]
for k in range(3,30):P.append(P[k-2]+P[k-3])
R=[3,0,2]
for k in range(3,30):R.append(R[k-2]+R[k-3])
for n in range(3,26):assert tr(C[n-2])==P[n-2],(n,tr(C[n-2]),P[n-2])
for n in range(8,23):
    assert tr(BP[n])==R[n]>P[n-2]
    assert tr(mm(A,BP[n-1]))<P[n-2]
# equality occurs only n rotations of 00 11..1; exhaustive independent rule simulation
for n in range(8,17):
    counts=[0]*(1<<n)
    for x in range(1<<n):
        y=0
        for i in range(n):
            a=(x>>((i-1)%n))&1; b=(x>>i)&1; c=(x>>((i+1)%n))&1
            if b^(a|c):y|=1<<i
        counts[y]+=1
    maxv=max(counts)
    runner=max(v for j,v in enumerate(counts) if j!=(1<<n)-1)
    winners={j for j,v in enumerate(counts) if v==runner and j!=(1<<n)-1}
    target={((1<<n)-1)^((3<<i | 3>>(n-i))&((1<<n)-1)) for i in range(n)}
    assert maxv==R[n] and counts[(1<<n)-1]==R[n]
    assert runner==P[n-2]
    assert winners==target,(n,len(winners),len(target),winners^target)
print('VERIFY_OK')
