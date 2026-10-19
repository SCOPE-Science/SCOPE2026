#!/usr/bin/env python3
"""Independent finite-field subspace enumeration for normalizer strata.

Run with Python 3. Uses only the standard library. All tested fields are prime.
The theorem itself covers every prime-power field.
"""
from itertools import combinations, product
from collections import Counter
from math import prod


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(k-i)-1 for i in range(k))


def predicted(d, q):
    N = d*(d-1)//2
    k = d-1
    out=Counter()
    for b in range(N+1):
        for t in range(k+1):
            val=gaussian(d,1,q)*gaussian(k,t,q)*gaussian(N-k,b-t,q)
            val*=q**((k-t)*(b-t)+N-b) if b>=t else 0
            if val:out[(b,t)]=val
    return out


def subspaces(n, q):
    for rank in range(n+1):
        for pivots in combinations(range(n),rank):
            free = [(r,c) for r,p in enumerate(pivots) for c in range(p+1,n) if c not in pivots]
            for values in product(range(q),repeat=len(free)):
                rows=[[0]*n for _ in pivots]
                for r,p in enumerate(pivots):rows[r][p]=1
                for (r,c),x in zip(free,values):rows[r][c]=x
                yield tuple(tuple(row) for row in rows)


def rank(rows,q):
    M=[list(row) for row in rows]
    if not M:return 0
    n=len(M[0]); p=0
    for c in range(n):
        pivot=next((r for r in range(p,len(M)) if M[r][c]%q),None)
        if pivot is None:continue
        M[p],M[pivot]=M[pivot],M[p]
        inv=pow(M[p][c],-1,q)
        M[p]=[x*inv%q for x in M[p]]
        for r in range(p+1,len(M)):
            s=M[r][c]
            if s:
                M[r]=[(a-s*b)%q for a,b in zip(M[r],M[p])]
        p+=1
        if p==len(M):break
    return p


def bracket(u, v, d, q):
    c=[]
    for i in range(d):
        for j in range(i+1,d):
            c.append((u[i]*v[j]-u[j]*v[i])%q)
    return tuple([0]*d+c)


def wedge(e, h, d, q):
    c=[]
    for i in range(d):
        for j in range(i+1,d):
            c.append(((1 if i==e else 0)*h[j] -(1 if j==e else 0)*h[i])%q)
    return tuple([0]*d+c)


def residue_mod_subspace(v,H,q):
    out=list(v)
    for row in H:
        pivot=next((c for c,z in enumerate(row) if z),None)
        if pivot is not None and out[pivot]:
            factor=out[pivot]
            out=[(x-factor*y)%q for x,y in zip(out,row)]
    return tuple(out)


def exhaustive(d,q):
    D=d+d*(d-1)//2
    observed=Counter()
    examined=0
    for H in subspaces(D,q):
        examined+=1
        projrank=rank([row[:d] for row in H],q)
        if projrank!=1:continue
        u=next(row for row in H if any(row[:d]))
        augmented=list(H)+[wedge(e,u,d,q) for e in range(d)]
        b=len(H)-1
        # Normalizer as the kernel of L -> Hom(H,L/H). Its codimension
        # is the increase of the span when basic commutators are appended.
        codim=rank(augmented,q)-len(H)
        t=d-1-codim
        observed[(b,t)]+=1
    want=predicted(d,q)
    assert observed==want,(d,q,observed,want)
    assert sum(observed.values())==gaussian(d,1,q)*sum(
        gaussian(D-d,b,q)*q**(D-d-b) for b in range(D-d+1))
    print('DIRECT_LIE_SUBSPACE_CHECK',d,q,'ambient_subspaces',examined,
          'selected',sum(observed.values()),'strata',sorted(observed.items()))


def center_geometry(d,q):
    N=d*(d-1)//2
    K=set(range(d-1))  # Wedge with e_0, first (d-1) basis bivectors.
    observed=Counter()
    for W in subspaces(N,q):
        b=len(W)
        # intersection dimension = dim W - rank(image under Z -> Z/K)
        t=b-rank([[row[c] for c in range(N) if c not in K] for row in W],q)
        observed[(b,t)]+=1
    want=Counter()
    for b in range(N+1):
        for t in range(d):
            v=gaussian(d-1,t,q)*gaussian(N-d+1,b-t,q)
            if b>=t:v*=q**((d-1-t)*(b-t))
            else:v=0
            if v:want[(b,t)]=v
    assert observed==want,(observed,want)
    print('CENTER_INTERSECTION_CHECK',d,q,'subspaces',sum(observed.values()),
          'strata',sorted(observed.items()))

if __name__=='__main__':
    for d,q in [(2,2),(2,3),(2,5),(3,2),(3,3)]:
        exhaustive(d,q)
    center_geometry(4,2)
    for q in (2,3):
        d=3; D=6; C=3; g=q*q+q+1
        expected=Counter()
        for b in range(C+1):
            expected[(b,0)]+=gaussian(C,b,q)  # central subalgebras
        for (b,t),num in predicted(d,q).items():
            expected[(b+1,d-1-t)]+=num
        expected[(3,1)]+=g*q**4
        expected[(4,1)]+=g*(q+1)*q**2
        expected[(5,0)]+=g
        expected[(6,0)]+=1
        observed=Counter()
        for H in subspaces(D,q):
            h=len(H)
            products=[bracket(a,b,d,q) for a,b in combinations(H,2)]
            if rank(list(H)+products,q)!=h:
                continue
            constraints=[sum((residue_mod_subspace(wedge(e,u,d,q),H,q)
                               for u in H),()) for e in range(d)]
            codim=rank(constraints,q)
            observed[(h,codim)]+=1
        assert observed==expected, (q,expected,observed)
        print('COMPLETE_SUBALGEBRA_NORMALIZER_CHECK',q,
              'total',sum(observed.values()),'strata',sorted(observed.items()))
    print('ALL_NORMALIZER_STRATA_VERIFIED')
