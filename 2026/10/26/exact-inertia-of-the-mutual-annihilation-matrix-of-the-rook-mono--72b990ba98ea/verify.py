#!/usr/bin/env python3
"""Finite crosschecks of the mutual-zero-product bilinear form on partial permutations.
Pure Python standard library; no downloaded files or third-party packages.
"""
from itertools import combinations, permutations
from math import comb, factorial
from fractions import Fraction

def maps(n):
    for r in range(n+1):
        for dom in combinations(range(n),r):
            for image in combinations(range(n),r):
                for im in permutations(image):
                    yield tuple(zip(dom,im))

def annihilate(f,g):
    f,g=dict(f),dict(g)
    return all(v not in g for v in f.values()) and all(v not in f for v in g.values())

def pairs(n):
    return [(d,r) for a in range(n+1) for d in combinations(range(n),a)
            for r in combinations(range(n),a)]

def kernel(pp):
    return [[int(not set(r)&set(e) and not set(d)&set(f))
             for e,f in pp] for d,r in pp]

def inertia_exact(input_matrix):
    a=[[Fraction(v) for v in row] for row in input_matrix]
    plus=minus=0
    while a:
        n=len(a)
        i=next((i for i in range(n) if a[i][i]),None)
        if i is not None:
            piv=a[i][i]; plus+=piv>0; minus+=piv<0
            keep=[j for j in range(n) if j!=i]
            a=[[a[u][v]-a[u][i]*a[i][v]/piv for v in keep] for u in keep]
        else:
            match=next(((i,j) for i in range(n) for j in range(i+1,n) if a[i][j]),None)
            assert match is not None,'unexpected singular compressed matrix'
            i,j=match;b=a[i][j];plus+=1;minus+=1
            keep=[k for k in range(n) if k not in (i,j)]
            a=[[a[u][v]-(a[u][i]*a[j][v]+a[u][j]*a[i][v])/b
                for v in keep] for u in keep]
    return plus,minus

def det_mod(matrix,prime):
    a=[[x%prime for x in row] for row in matrix]
    ans=1;n=len(a)
    for i in range(n):
        j=next((j for j in range(i,n) if a[j][i]),None)
        if j is None:return 0
        if j!=i:a[j],a[i]=a[i],a[j];ans=-ans
        p=a[i][i];ans=ans*p%prime;inv=pow(p,-1,prime)
        for r in range(i+1,n):
            c=a[r][i]*inv%prime
            if c:
                for s in range(i+1,n):a[r][s]=(a[r][s]-c*a[i][s])%prime
            a[r][i]=0
    return ans%prime

for n in range(1,5):
    pp=pairs(n); k=kernel(pp)
    order=sum(comb(n,a)**2*factorial(a) for a in range(n+1))
    m=comb(2*n,n); f=comb(n,n//2) if n%2==0 else 0
    pos,neg=(m+f)//2,(m-f)//2
    assert len(pp)==m
    assert len(k)==m
    for p in (101,1009):assert det_mod(k,p)==(-1 if neg%2 else 1)%p
    if n<=3:
        mm=list(maps(n));assert len(mm)==order
        lookup={v:i for i,v in enumerate(pp)}
        for a in mm:
            da=tuple(sorted(x for x,_ in a));ra=tuple(sorted(y for _,y in a))
            x=lookup[(da,ra)]
            for b in mm:
                db=tuple(sorted(x for x,_ in b)); rb=tuple(sorted(y for _,y in b))
                y=lookup[(db,rb)]
                assert int(annihilate(a,b))==k[x][y]
        assert inertia_exact(k)==(pos,neg)
    print('n=',n,'order=',order,'inertia=',(pos,neg,order-m),'exact/mod checks passed')
print('VERIFY_OK_ROOK_MUTUAL_ANNIHILATION_INERTIA')
