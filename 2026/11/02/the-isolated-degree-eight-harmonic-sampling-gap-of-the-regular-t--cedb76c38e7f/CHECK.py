#!/usr/bin/env python3
"""Exact checks for spherical harmonic interpolation on the truncated octahedron.
Only Python's standard library is needed. The analytic high-degree argument
is proved separately; this checks finitely many exact rational determinants.
"""
from itertools import permutations, product
from fractions import Fraction

V = sorted({tuple(t*s for t,s in zip(p,sgn)) for p in set(permutations((0,1,2)))
            for sgn in product((-1,1), repeat=3)})
X = [x for x in V if x > tuple(-u for u in x)]
assert len(V)==24 and len(X)==12
D = [[sum(a*b for a,b in zip(x,y)) for y in X] for x in X]
assert all(D[i][i]==5 for i in range(12))
assert max(abs(D[i][j]) for i in range(12) for j in range(12) if i!=j)==4

def P_rat(k,t):
    if not k:return Fraction(1)
    a,b=Fraction(1),t
    for j in range(1,k):a,b=b,((2*j+1)*t*b-j*a)/(j+1)
    return b

def rank_fraction(A):
    a=[list(row) for row in A]
    i=0
    for j in range(len(a[0])):
        h=next((q for q in range(i,len(a)) if a[q][j]),None)
        if h is None: continue
        a[i],a[h]=a[h],a[i]
        q=a[i][j]
        a[i]=[v/q for v in a[i]]
        for r in range(i+1,len(a)):
            q=a[r][j]
            if q:a[r]=[v-q*w for v,w in zip(a[r],a[i])]
        i+=1
        if i==len(a):break
    return i

def rank_mod(A, p):
    a=[[int(v)%p for v in row] for row in A]; i=0
    for j in range(len(a[0])):
        h=next((q for q in range(i,len(a)) if a[q][j]%p),None)
        if h is None:continue
        a[i],a[h]=a[h],a[i]
        q=pow(a[i][j],-1,p);a[i]=[(q*v)%p for v in a[i]]
        for r in range(i+1,len(a)):
            q=a[r][j]
            if q:a[r]=[(v-q*w)%p for v,w in zip(a[r],a[i])]
        i+=1
        if i==len(a):break
    return i

def P_mod(k,t,p):
    if not k:return 1
    a,b=1,t%p
    for j in range(1,k):a,b=b,((2*j+1)*t*b-j*a)*pow(j+1,-1,p)%p
    return b

if __name__=='__main__':
    count=0
    for k in range(9):
        G=[[P_rat(k,Fraction(d,5)) for d in row] for row in D]
        expected=[1,3,5,6,9,9,10,12,11][k]
        assert rank_fraction(G)==expected,(k,rank_fraction(G),expected)
        if k==8:
            # The unique eighth-degree relation is the alternating
            # permutation character on the distinct absolute coordinates.
            def alt_weight(x):
                a=tuple(abs(t) for t in x)
                return -(-1)**sum(a[i]>a[j] for i in range(3) for j in range(i+1,3))
            w=[alt_weight(x) for x in X]
            assert set(w)=={-1,1} and sum(w)==0
            assert all(sum(v*u for v,u in zip(row,w))==0 for row in G)
            assert all(sum(row)==Fraction(72171,250000) for row in G)
        count+=12*12
    p=1000003
    assert p>135 and p%5
    for k in range(9,135):
        vals={d:P_mod(k,(d*pow(5,-1,p))%p,p) for row in D for d in row}
        G=[[vals[d] for d in row] for row in D]
        r=rank_mod(G,p)
        assert r==12,(k,r)
        count+=144
    print('TRUNCATED_OCTAHEDRON_RANK_CERTIFICATE_OK', count,
          'exact entries checked; finite degrees 0..134')
