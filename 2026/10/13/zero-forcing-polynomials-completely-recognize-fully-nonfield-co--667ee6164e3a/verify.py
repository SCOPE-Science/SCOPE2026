#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import prod

def type_masks(r):
    return list(range(1,(1<<r)-1))

def type_weights(lams):
    r=len(lams)
    ans=[]
    for S in type_masks(r):
        w=1
        for i,a in enumerate(lams):
            if (S>>i)&1:
                w*=a
        ans.append(w)
    return ans

def type_adjacency(r):
    T=type_masks(r)
    return [[1 if (S&T)==0 else 0 for T in T] for S in T]

def bareiss_det(A):
    A=[row[:] for row in A]
    n=len(A)
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k]==0:
            p=next(i for i in range(k+1,n) if A[i][k])
            A[k],A[p]=A[p],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n):
            A[i][k]=0
    return sign*A[-1][-1]

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=c=0
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
        r+=1;c+=1
    return r

def profile_forces(r,W):
    T=type_masks(r)
    W=set(W)
    while W:
        forced=None
        for S in T:
            nbr=[U for U in W if (S&U)==0]
            if len(nbr)==1:
                forced=nbr[0]
                break
        if forced is None:
            return False
        W.remove(forced)
    return True

def blowup_graph(lams):
    r=len(lams)
    T=type_masks(r)
    W=type_weights(lams)
    cls=[]
    for j,w in enumerate(W):
        cls += [j]*w
    N=[set() for _ in cls]
    for x in range(len(cls)):
        for y in range(x+1,len(cls)):
            if (T[cls[x]] & T[cls[y]])==0:
                N[x].add(y);N[y].add(x)
    return T,W,cls,N

def zero_forces(S,N):
    blue=set(S)
    while True:
        if len(blue)==len(N):
            return True
        move=None
        for v in sorted(blue):
            w=N[v]-blue
            if len(w)==1:
                move=next(iter(w)); break
        if move is None:
            return False
        blue.add(move)

def brute_polynomial(N):
    out={}
    n=len(N)
    for k in range(n+1):
        c=sum(1 for S in combinations(range(n),k) if zero_forces(S,N))
        if c:
            out[k]=c
    return out

def predicted_polynomial(lams):
    w=type_weights(lams)
    N=sum(w); m=len(w)
    q={0:1}
    for a in w:
        nq={}
        for d,c in q.items():
            nq[d+1]=nq.get(d+1,0)+c
            nq[d]=nq.get(d,0)+c*a
        q=nq
    return {N-m+d:c for d,c in q.items() if c}

def recover_lambdas(rootweights,r):
    e=(1<<(r-1))-1
    P=prod(rootweights)
    lo,hi=1,P
    while lo<=hi:
        mid=(lo+hi)//2
        z=mid**e
        if z==P:
            fullprod=mid
            break
        if z<P:
            lo=mid+1
        else:
            hi=mid-1
    else:
        raise AssertionError("non-power product")
    assert fullprod**e==P
    rem=Counter(rootweights)
    rem[1]+=1
    rem[fullprod]+=1
    rem[1]-=1
    if rem[1]==0: del rem[1]
    generated=Counter({1:1})
    out=[]
    for _ in range(r):
        x=min(rem)
        out.append(x)
        add=Counter()
        for y,c in generated.items():
            add[y*x]+=c
        for y,c in add.items():
            assert rem[y]>=c
            rem[y]-=c
            if rem[y]==0: del rem[y]
        generated += add
    assert not rem
    return sorted(out)

# Quotient Boolean matrices are unimodular.
for r in range(2,6):
    A=type_adjacency(r)
    d=bareiss_det(A)
    assert d==-1,(r,d)
    print(f"B_{r}: types={len(A)}, determinant={d}")

# Exhaust all white-type profiles through r=4.
for r in range(2,5):
    T=type_masks(r)
    for mask in range(1<<len(T)):
        W=[T[i] for i in range(len(T)) if (mask>>i)&1]
        assert profile_forces(r,W),(r,mask)
    print(f"B_{r}: all {1<<len(T)} at-most-one-white profiles force")

# Complete graph-level polynomial checks in small nonfield cases.
for lams in [(2,2),(2,3),(2,2,2)]:
    T,W,cls,N=blowup_graph(lams)
    brute=brute_polynomial(N)
    pred=predicted_polynomial(lams)
    assert brute==pred,(lams,brute,pred)
    z=min(brute)
    m=(1<<len(lams))-2
    assert z==len(N)-m
    e=(1<<(len(lams)-1))-1
    assert brute[z]==prod(lams)**e
    print(f"lambda={lams}: N={len(N)}, Z={z}, minimum_sets={brute[z]}")

# Exact rank of representative blow-up adjacency matrices.
for lams in [(2,3),(2,2,2),(2,2,2,2)]:
    T,W,cls,N=blowup_graph(lams)
    M=[[1 if j in N[i] else 0 for j in range(len(N))] for i in range(len(N))]
    rk=rank_fraction(M)
    assert rk==(1<<len(lams))-2,(lams,rk)
    print(f"lambda={lams}: adjacency_rank={rk}")

# Recover local proper-ideal counts from the nonzero root multiset.
tests=[
    (2,2),(2,5),(2,2,2),(2,3,4),(2,2,3,5),
    (2,3,3,4,7)
]
for lams in tests:
    roots=type_weights(lams)
    got=recover_lambdas(roots,len(lams))
    assert got==sorted(lams),(lams,got)
    print(f"recovery {lams} -> {tuple(got)}")

print("VERIFY_OK")
