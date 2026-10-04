#!/usr/bin/env python3
from itertools import product, combinations
from fractions import Fraction

def ideals(lengths):
    V=[]
    for a in product(*[range(L+1) for L in lengths]):
        if all(x==0 for x in a):
            continue
        if all(a[i]==lengths[i] for i in range(len(lengths))):
            continue
        V.append(a)
    return V

def support(a,lengths):
    return frozenset(i for i,x in enumerate(a) if x<lengths[i])

def graph(lengths):
    V=ideals(lengths)
    N=[set() for _ in V]
    for i,a in enumerate(V):
        sa=support(a,lengths)
        for j in range(i+1,len(V)):
            if sa & support(V[j],lengths):
                N[i].add(j); N[j].add(i)
    return V,N

def zero_forces(C,N):
    blue=set(C)
    trace=[]
    while True:
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=(v,next(iter(W)))
                break
        if move is None:
            return len(blue)==len(N),trace
        v,u=move
        blue.add(u)
        trace.append((v,u))

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=0; c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1
            continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1; c+=1
    return r

def gram(lengths,V):
    S=[support(a,lengths) for a in V]
    return [[len(S[i]&S[j]) for j in range(len(V))] for i in range(len(V))]

def claimed_blue(lengths):
    r=len(lengths)
    V,N=graph(lengths)
    idx={a:i for i,a in enumerate(V)}
    if r==1:
        if lengths[0]==2:
            return V,N,set(range(len(V))),[]
        # Clique: leave any one vertex white.
        W={0}
        return V,N,set(range(len(V)))-W,[]
    assert lengths[0]>=2
    whites=[]
    # W1 = maximal ideal in first factor times full rings in all others.
    w1=(1,)+tuple(0 for _ in range(r-1))
    whites.append(idx[w1])
    # W_j, j=2..r, has zero factors before j and full rings from j onward.
    for j in range(1,r):
        a=tuple(lengths[i] if i<j else 0 for i in range(r))
        whites.append(idx[a])
    blue=set(range(len(V)))-set(whites)
    return V,N,blue,whites

cases=[(2,),(3,),(4,),(2,1),(3,1),(2,2),(3,2),(2,1,1),(2,2,1),(2,1,1,1)]
for lengths in cases:
    V,N=graph(lengths)
    n=len(V); r=len(lengths)
    G=gram(lengths,V)
    for i in range(n):
        for j in range(i+1,n):
            assert ((G[i][j]!=0)==(j in N[i]))
    gr=rank_fraction(G) if n else 0

    if lengths==(2,):
        assert n==1
        ok,tr=zero_forces({0},N)
        assert ok and gr==1  # Gram witness is not minimum in this isolated boundary.
        print(f"lengths={lengths}: N={n}, boundary K1, Z=1, mr=0")
        continue

    # Reorder test cases so a nonfield factor is first; all listed cases already do this.
    V,N,blue,whites=claimed_blue(lengths)
    ok,tr=zero_forces(blue,N)
    assert ok
    expected=n-r
    assert len(blue)==expected
    assert gr==r

    # The rank-r Gram witness gives M>=N-r, hence Z>=N-r by M<=Z.
    # For moderate cases, also test directly that no set of size expected-1 forces.
    if n<=16 and expected>0:
        bad=0
        for C in combinations(range(n),expected-1):
            z,_=zero_forces(C,N)
            if z:
                bad+=1
                break
        assert bad==0

    print(f"lengths={lengths}: N={n}, r={r}, constructed_Z={expected}, forces={len(tr)}, Gram_rank={gr}")

print("VERIFY_OK")
