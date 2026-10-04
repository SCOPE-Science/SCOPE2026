#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

def vertices(r):
    return [frozenset(c) for k in range(1,r) for c in combinations(range(r),k)]

def graph(r):
    V=vertices(r)
    N=[set() for _ in V]
    for i,a in enumerate(V):
        for j in range(i+1,len(V)):
            b=V[j]
            if a & b:
                N[i].add(j); N[j].add(i)
    return V,N

def zero_forces(S,N):
    blue=set(S)
    trace=[]
    while True:
        move=None
        for v in sorted(blue):
            white=N[v]-blue
            if len(white)==1:
                move=(v,next(iter(white)))
                break
        if move is None:
            break
        v,u=move
        blue.add(u)
        trace.append((v,u))
    return len(blue)==len(N), trace

def claimed_white_family(r):
    W=[frozenset({0,1})]
    for j in range(1,r):
        W.append(frozenset(range(j,r)))
    return W

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    rank=0; col=0
    while rank<m and col<n:
        pivot=next((i for i in range(rank,m) if A[i][col]),None)
        if pivot is None:
            col+=1; continue
        A[rank],A[pivot]=A[pivot],A[rank]
        p=A[rank][col]
        A[rank]=[x/p for x in A[rank]]
        for i in range(m):
            if i!=rank and A[i][col]:
                q=A[i][col]
                A[i]=[A[i][j]-q*A[rank][j] for j in range(n)]
        rank+=1; col+=1
    return rank

def gram_matrix(V):
    return [[len(a & b) for b in V] for a in V]

def brute_z(r):
    V,N=graph(r)
    n=len(V)
    for k in range(n+1):
        count=0
        for C in combinations(range(n),k):
            ok,_=zero_forces(C,N)
            if ok:
                count+=1
        if count:
            return k,count
    return None,0

for r in range(3,11):
    V,N=graph(r)
    idx={v:i for i,v in enumerate(V)}
    W=claimed_white_family(r)
    assert len(W)==r and len(set(W))==r
    assert all(w in idx for w in W)
    blue=set(range(len(V)))-{idx[w] for w in W}
    ok,trace=zero_forces(blue,N)
    assert ok, (r,W)
    assert len(trace)==r, (r,len(trace))
    G=gram_matrix(V)
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            assert ((G[i][j] != 0) == (j in N[i]))
    if r<=6:
        assert rank_fraction(G)==r
    print(f"r={r}: n={len(V)}, constructed ZFS size={len(blue)}, forces={len(trace)}, Gram pattern OK")

for r in (3,4):
    z,c=brute_z(r)
    expected=(2**r-2)-r
    assert z==expected, (r,z,expected)
    print(f"r={r}: exhaustive Z={z}, minimum ZFS count={c}")

print("VERIFY_OK")
