#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import prod, log2

def type_data(qs, ss):
    r=len(qs)
    S=prod(ss)
    weights=[]
    for A in range(1<<r):
        w=S
        for i,q in enumerate(qs):
            if (A>>i)&1:
                w*=q-1
        weights.append(w)
    return S,weights

def quotient(r):
    m=1<<r
    return [[1 if (A|B)==m-1 else 0 for B in range(m)] for A in range(m)]

def blowup(qs,ss):
    r=len(qs)
    S,w=type_data(qs,ss)
    cls=[]
    for t,a in enumerate(w):
        cls += [t]*a
    N=[set() for _ in cls]
    full=(1<<r)-1
    for i in range(len(cls)):
        for j in range(i+1,len(cls)):
            ti,tj=cls[i],cls[j]
            if (ti|tj)==full:
                N[i].add(j);N[j].add(i)
    return w,cls,N

def zero_forces(S,N):
    blue=set(S)
    while True:
        if len(blue)==len(N):
            return True
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=next(iter(W)); break
        if move is None:
            return False
        blue.add(move)

def polynomial(N):
    out={}
    n=len(N)
    for k in range(n+1):
        c=sum(1 for S in combinations(range(n),k) if zero_forces(S,N))
        if c:
            out[k]=c
    return out

def predicted(qs,ss):
    _,w=type_data(qs,ss)
    N=sum(w); m=len(w)
    P={0:1}
    for a in w:
        Q={}
        for d,c in P.items():
            Q[d+1]=Q.get(d+1,0)+c
            Q[d]=Q.get(d,0)+c*a
        P=Q
    return {N-m+d:c for d,c in P.items() if c}

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=c=0
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

def profile_forces(r,W):
    full=(1<<r)-1
    W=set(W)
    while W:
        T=max(W, key=lambda x:(x.bit_count(),x))
        # choose an inclusion-maximal white type, not merely max cardinality tie
        candidates=[x for x in W if not any(x!=y and (x|y)==y for y in W)]
        T=candidates[0]
        source=full^T
        white_neighbors=[U for U in W if (source|U)==full]
        assert white_neighbors==[T] or (len(white_neighbors)==1 and white_neighbors[0]==T)
        W.remove(T)
    return True

def recover(rootweights):
    m=len(rootweights)
    r=round(log2(m))
    assert 1<<r==m
    S=min(rootweights)
    norm=[x//S for x in rootweights]
    assert all(S*x==w for x,w in zip(norm,rootweights))
    c=Counter(norm)
    one_mult=c[1]
    t=round(log2(one_mult))
    assert 1<<t==one_mult
    scale=1<<t
    reduced=Counter()
    for x,n in c.items():
        assert n%scale==0
        reduced[x]=n//scale
    assert reduced[1]==1
    reduced[1]-=1
    if reduced[1]==0: del reduced[1]
    generated=[1]
    factors=[]
    for _ in range(r-t):
        x=min(reduced)
        factors.append(x)
        new=[g*x for g in generated]
        for y in new:
            assert reduced[y]>0
            reduced[y]-=1
            if reduced[y]==0: del reduced[y]
        generated += new
    assert not reduced
    a=sorted([1]*t+factors)
    return S, sorted(x+1 for x in a)

# Quotient matrix has full rank for several ranks.
for r in range(1,6):
    Q=quotient(r)
    rk=rank_fraction(Q)
    assert rk==(1<<r)
    print(f"quotient r={r}: rank={rk}")

# Exhaust every type profile through r=4.
for r in range(1,5):
    m=1<<r
    for mask in range(1<<m):
        W=[t for t in range(m) if (mask>>t)&1]
        assert profile_forces(r,W)
    print(f"profiles r={r}: {1<<m} forcing profiles")

# Full graph polynomial checks in realizable nonfield local-factor examples.
tests=[
    ((2,),(2,)),       # Z/4
    ((3,),(3,)),       # Z/9
    ((2,2),(2,2)),     # Z/4 x Z/4
]
for qs,ss in tests:
    w,cls,N=blowup(qs,ss)
    brute=polynomial(N)
    pred=predicted(qs,ss)
    assert brute==pred,(qs,ss,brute,pred)
    z=min(brute)
    assert z==len(N)-(1<<len(qs))
    print(f"q={qs}, s={ss}: weights={w}, N={len(N)}, Z={z}, min_sets={brute[z]}")

# Direct quotient-pattern check for a mixed product Z/4 x Z/9.
qs=(2,3); ss=(2,3)
w,cls,N=blowup(qs,ss)
assert w==[6,6,12,12]
assert rank_fraction(quotient(2))==4
print(f"mixed q={qs}, s={ss}: weights={w}, predicted_Z={len(N)-4}")

# Parameter recovery, including residue-field order 2 factors.
for qs,ss in [
    ((2,),(2,)),
    ((2,3),(2,3)),
    ((2,2,5),(2,4,5)),
    ((3,4,7),(3,8,7)),
    ((2,3,3,5),(2,3,9,5)),
]:
    S,w=type_data(qs,ss)
    gotS,gotq=recover(sorted(w))
    assert gotS==S and gotq==sorted(qs),(qs,ss,gotS,gotq)
    print(f"recover q={qs}, S={S} -> q={tuple(gotq)}, S={gotS}")

print("VERIFY_OK")
