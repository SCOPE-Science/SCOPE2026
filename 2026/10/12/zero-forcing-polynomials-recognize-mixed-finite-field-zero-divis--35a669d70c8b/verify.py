#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import prod

def weights(qs):
    r=len(qs)
    a=[q-1 for q in qs]
    return {
        S:prod(a[i] for i in range(r) if (S>>i)&1)
        for S in range(1,(1<<r)-1)
    }

def blowup(qs):
    w=weights(qs)
    types=[]
    for S,c in w.items():
        types += [S]*c
    N=[set() for _ in types]
    for i in range(len(types)):
        for j in range(i+1,len(types)):
            if types[i]&types[j]==0:
                N[i].add(j); N[j].add(i)
    return w,types,N

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

def brute_poly(N):
    out={}
    n=len(N)
    for k in range(n+1):
        c=sum(1 for S in combinations(range(n),k) if zero_forces(S,N))
        if c: out[k]=c
    return out

def predicted(qs):
    w=weights(qs)
    N=sum(w.values()); h=len(w)
    P={0:1}
    for c in w.values():
        Q={}
        for d,a in P.items():
            Q[d+1]=Q.get(d+1,0)+a
            Q[d]=Q.get(d,0)+a*c
        P=Q
    return {N-h+d:a for d,a in P.items() if a}

def profile_forces(qs,W):
    w=weights(qs)
    W=set(W)
    while W:
        move=None
        for source in w:
            # A blue representative exists unless the source class is
            # a white singleton.
            if w[source]==1 and source in W:
                continue
            white_neighbors=[T for T in W if source&T==0]
            if len(white_neighbors)==1:
                move=white_neighbors[0]
                break
        if move is None:
            return False
        W.remove(move)
    return True

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
        r+=1; c+=1
    return r

def quotient(r):
    T=list(range(1,(1<<r)-1))
    return [[1 if (S&T)==0 else 0 for T in T] for S in T]

def recover(rootweights):
    h=len(rootweights)
    r=1
    while (1<<r)-2<h: r+=1
    assert (1<<r)-2==h
    e=(1<<(r-1))-1
    total=prod(rootweights)
    # exact positive e-th root
    lo,hi=1,max(2,total)
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**e<=total: lo=mid
        else: hi=mid
    P=lo if lo**e==total else hi
    assert P**e==total

    allprod=Counter(rootweights)
    allprod[1]+=1
    allprod[P]+=1

    one_mult=allprod[1]
    t=0
    while (1<<t)<one_mult: t+=1
    assert (1<<t)==one_mult and 1<=t<r

    scale=1<<t
    reduced=Counter()
    for x,c in allprod.items():
        assert c%scale==0
        reduced[x]=c//scale
    # reduced is the complete subset-product multiset of factors >1
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
    qs=sorted([2]*t+[x+1 for x in factors])
    return r,t,P,qs

# Every one-white-per-support profile forces in representative mixed cases.
for qs in [(2,3),(2,2,3),(2,3,3),(2,2,2,3),(2,2,3,5)]:
    T=list(weights(qs))
    for mask in range(1<<len(T)):
        W=[T[i] for i in range(len(T)) if (mask>>i)&1]
        assert profile_forces(qs,W),(qs,W)
    print(f"profile theorem {qs}: {1<<len(T)} profiles")

# Exact quotient ranks.
for r in range(2,7):
    Q=quotient(r)
    assert rank_fraction(Q)==(1<<r)-2
    print(f"quotient rank r={r}: {len(Q)}")

# Exhaustive full graph polynomials in small mixed cases.
for qs in [(2,3),(2,2,3),(2,3,3),(2,2,5)]:
    w,types,N=blowup(qs)
    brute=brute_poly(N)
    pred=predicted(qs)
    assert brute==pred,(qs,brute,pred)
    print(f"full polynomial {qs}: N={len(N)}, Z={min(brute)}, coeff_min={brute[min(brute)]}")

# Direct ring construction over prime fields for two representative products.
for qs in [(2,3),(2,2,3),(2,3,5)]:
    elems=list(__import__('itertools').product(*[range(q) for q in qs]))
    verts=[x for x in elems if any(a==0 for a in x) and any(a!=0 for a in x)]
    support=[sum((1<<i) for i,a in enumerate(x) if a!=0) for x in verts]
    for i,x in enumerate(verts):
        for j in range(i+1,len(verts)):
            prodzero=all((x[k]*verts[j][k])%qs[k]==0 for k in range(len(qs)))
            assert prodzero==(support[i]&support[j]==0)
    print(f"direct product {qs}: vertices={len(verts)}")

# Root multiset recovery including repeated and unequal field orders.
for qs in [(2,3),(2,2,3),(2,3,5),(2,2,3,4),(2,2,2,3,5)]:
    rootweights=sorted(weights(qs).values())
    r,t,P,got=recover(rootweights)
    assert got==sorted(qs),(qs,got)
    print(f"recover {qs}: r={r}, binary={t}, unit_product={P}, fields={tuple(got)}")

# Sharp all-binary failure at the smallest boundary.
w,types,N=blowup((2,2))
brute=brute_poly(N)
assert brute=={1:2,2:1}
assert predicted((2,2))!={1:2,2:1}
print("pure binary boundary F2xF2:",brute)

print("VERIFY_OK")
