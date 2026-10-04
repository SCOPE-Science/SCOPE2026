#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

def layer_sizes(q, ell):
    return [(q-1)*(q**(ell-i-1)) for i in range(1,ell)]

def graph(q, ell):
    sizes=layer_sizes(q,ell)
    V=[]
    layer=[]
    for i,s in enumerate(sizes, start=1):
        for k in range(s):
            V.append((i,k))
            layer.append(i)
    N=[set() for _ in V]
    for a in range(len(V)):
        i=layer[a]
        for b in range(a+1,len(V)):
            j=layer[b]
            if i+j>=ell:
                N[a].add(b);N[b].add(a)
    return V,layer,N

def zero_forces(C,N):
    blue=set(C); trace=[]
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
        blue.add(u);trace.append((v,u))

def brute_z(N):
    n=len(N)
    for k in range(n+1):
        count=0
        for C in combinations(range(n),k):
            ok,_=zero_forces(C,N)
            if ok:
                count+=1
        if count:
            return k,count
    raise RuntimeError

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=0; c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1; continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1;c+=1
    return r

def witness(q,ell):
    V,layer,N=graph(q,ell)
    m=ell-1
    H=[[1 if (i+1)+(j+1)>=ell else 0 for j in range(m)] for i in range(m)]
    A=[[H[layer[a]-1][layer[b]-1] for b in range(len(V))] for a in range(len(V))]
    return V,layer,N,H,A

def constructed_set(q,ell):
    V,layer,N=graph(q,ell)
    n=len(V)
    if (q,ell)==(2,2):
        return set(range(n))
    # Leave one representative white in every layer.
    whites=set()
    for i in range(1,ell):
        whites.add(next(v for v in range(n) if layer[v]==i))
    return set(range(n))-whites

cases=[(2,2),(3,2),(5,2),(2,3),(3,3),(2,4),(3,4),(2,5)]
for q,ell in cases:
    V,layer,N,H,A=witness(q,ell)
    n=len(V)
    # Exact graph-pattern check.
    for i in range(n):
        for j in range(i+1,n):
            assert ((A[i][j]!=0)==(j in N[i]))
    if (q,ell)==(2,2):
        assert n==1
        bz,bc=brute_z(N)
        assert (bz,bc)==(1,1)
        print(f"q={q}, ell={ell}: K1 boundary, Z=1, mr=0")
        continue
    assert rank_fraction(H)==ell-1
    assert rank_fraction(A)==ell-1
    C=constructed_set(q,ell)
    ok,tr=zero_forces(C,N)
    assert ok
    predicted=n-(ell-1)
    assert len(C)==predicted
    if n<=15:
        bz,bc=brute_z(N)
        assert bz==predicted,(q,ell,bz,predicted)
        print(f"q={q}, ell={ell}: n={n}, exhaustive Z={bz}, min_sets={bc}, witness_rank={ell-1}, forces={len(tr)}")
    else:
        print(f"q={q}, ell={ell}: n={n}, constructed Z={predicted}, witness_rank={ell-1}, forces={len(tr)}")

print("VERIFY_OK")
