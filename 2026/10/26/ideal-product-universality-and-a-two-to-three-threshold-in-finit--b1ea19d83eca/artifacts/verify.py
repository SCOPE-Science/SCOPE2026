#!/usr/bin/env python3
"""Independent exhaustive checks for the ideal-product law in small prime fields."""
from itertools import combinations, product
from math import comb


def rref_subspaces(n, p):
    """Enumerate all subspaces via unique row-reduced echelon generating bases."""
    for d in range(n+1):
        for pivots in combinations(range(n), d):
            free = [(i,j) for i,pi in enumerate(pivots) for j in range(pi+1,n) if j not in pivots]
            for vals in product(range(p), repeat=len(free)):
                rows = [[0]*n for _ in range(d)]
                for i,pi in enumerate(pivots): rows[i][pi]=1
                for (i,j),v in zip(free, vals): rows[i][j]=v
                yield tuple(tuple(row) for row in rows)


def rank(rows, p):
    if not rows:return 0
    a=[list(map(lambda x:x%p,row)) for row in rows]
    piv=0
    for col in range(len(a[0])):
        ix=next((i for i in range(piv,len(a)) if a[i][col]),None)
        if ix is None:continue
        a[piv],a[ix]=a[ix],a[piv]
        inv=pow(a[piv][col],-1,p)
        a[piv]=[(z*inv)%p for z in a[piv]]
        for k in range(len(a)):
            if k!=piv and a[k][col]:
                f=a[k][col]
                a[k]=[(z-f*t)%p for z,t in zip(a[k],a[piv])]
        piv+=1
        if piv==len(a):break
    return piv


def prod(a,b,p,B):
    r=len(B)
    zz=(a[0]*b[-1]+b[0]*a[-1])%p
    for i in range(r):
        for j in range(r):zz=(zz+a[i+1]*B[i][j]*b[j+1])%p
    return tuple([a[0]*b[0]%p]+[(a[0]*b[i+1]+b[0]*a[i+1])%p for i in range(r)]+[zz])


def qbinom(n,k,q):
    numerator=1;denominator=1
    for j in range(k):
        numerator*=q**(n-j)-1;denominator*=q**(j+1)-1
    return numerator//denominator


def check(p,B):
    r=len(B);n=r+2
    ambient=rref_subspaces(n,p)
    unit=tuple([1]+[0]*(n-1)); gens=[tuple(1 if j==i+1 else 0 for j in range(n)) for i in range(r)];gens.append(tuple(1 if j==n-1 else 0 for j in range(n)))
    ideals=[]
    for basis in ambient:
        d=len(basis)
        if all(rank(basis+(prod(g,v,p,B),),p)==d for v in basis for g in gens):ideals.append(basis)
    T=sum(qbinom(r,d,p) for d in range(r+1));N=T+2
    assert len(ideals)==N,(p,B,len(ideals),N)
    C=sum(qbinom(r,d,p)*sum(qbinom(r-d,j,p) for j in range(r-d+1)) for d in range(r+1))
    z2=0; nonzero2=0
    for a in ideals:
        for b in ideals:
            if not any(any(prod(x,y,p,B)) for x in a for y in b):z2+=1
            else:nonzero2+=1
    predicted=N*N-(1+2*T+(T*T-C))
    assert z2==predicted,(p,B,z2,predicted)
    z3=0
    for a in ideals:
        for b in ideals:
            for c in ideals:
                if not any(any(prod(prod(x,y,p,B),z,p,B)) for z in c for x in a for y in b):z3+=1
    predicted3=N**3-(1+3*T+3*(T*T-C))
    assert z3==predicted3,(p,B,z3,predicted3)
    return (p,r,N,z2,z3)


def main():
    cases=[(2,[[0,1],[1,0]]),(2,[[1,0],[0,1]]),(3,[[0,1],[1,0]]),(3,[[1,0],[0,1]]),(5,[[0,1],[1,0]]),(2,[[1,0,0],[0,1,0],[0,0,1]])]
    for p,B in cases:
        print('p,r,ideals,zero_pairs,zero_triples=',*check(p,B),flush=True)
    print('VERIFY_OK',flush=True)

if __name__=='__main__':main()
