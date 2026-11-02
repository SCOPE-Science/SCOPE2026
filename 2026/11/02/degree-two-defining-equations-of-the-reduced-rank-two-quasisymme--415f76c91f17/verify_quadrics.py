#!/usr/bin/env python3
"""Exact degree-two coordinate-function rank checks for rank-two toric union."""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from collections import defaultdict
from math import comb


def plucker(a,b,cut):
    def col(j):
        if j == 1: return (1,0)
        if j <= cut: return (0,1)
        return (1,1)
    x,y=col(a); z,w=col(b)
    return x*w-y*z


def rank(matrix):
    if not matrix: return 0
    a=[[Fraction(t) for t in row] for row in matrix]
    r=0
    for j in range(len(a[0])):
        piv=next((i for i in range(r,len(a)) if a[i][j]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        c=a[r][j];a[r]=[v/c for v in a[r]]
        for i in range(len(a)):
            if i==r:continue
            c=a[i][j]
            if c:a[i]=[x-c*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r


def run(n):
    variables=list(combinations(range(1,n+1),2))
    weights=defaultdict(list)
    for p,q in combinations_with_replacement(variables,2):
        weight=tuple(sorted((*p,*q)))
        weights[weight].append((p,q))
    lost=0; counted=0; classification=defaultdict(int)
    for weight, mons in weights.items():
        mat=[[plucker(*p,cut)*plucker(*q,cut) for p,q in mons] for cut in range(2,n)]
        r=rank(mat)
        classified='pair_squared' if len(set(weight))==2 else ('one_shared' if len(set(weight))==3 else 'four_distinct')
        classification[(classified,1 in weight,r)]+=1
        counted+=r; lost+=len(mons)-r
        if classified=='pair_squared': assert r==1
        elif classified=='one_shared':
            a,b,c=sorted(set(weight))
            central=(weight.count(b)==2 and a>=2)
            assert r==(0 if central else 1), (n,weight,r)
        else:
            assert r==(2 if 1 in weight else 1),(n,weight,r)
    N=comb(n,2)
    assert sum(len(v) for v in weights.values())==N*(N+1)//2
    assert counted==N*(N+1)//2-2*comb(n,4)
    assert lost==comb(n,4)+comb(n-1,3)+comb(n-1,4)
    assert comb(n-1,3)+comb(n-1,4)==comb(n,4)
    print(f'n={n}: h2={counted}; total_quadratic_equations={lost}; extra={comb(n-1,4)}; verified weight classes={len(weights)}')

for n in range(4,11):run(n)
print('VERIFY_OK: exact component-orbit degree-two ranks for n=4..10')
