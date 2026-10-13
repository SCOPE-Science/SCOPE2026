#!/usr/bin/env python3
"""Exact finite sanity checks for the shortest-edge quantum-graph rounding radius.
The unrestricted theorem follows from the proof, not from this bounded census.
"""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb


def tree_subsets(n,edges):
    for idx in combinations(range(len(edges)),n-1):
        par=list(range(n))
        def find(x):
            while par[x]!=x:
                x=par[x]
            return x
        good=True
        for k in idx:
            a,b=edges[k]; a,b=find(a),find(b)
            if a==b:good=False;break
            par[a]=b
        if good and len({find(v) for v in range(n)})==1:
            yield set(idx)


def cotree_stat(n,edges,weights):
    assert len(edges)==len(weights) and len(edges)>0
    tt=list(tree_subsets(n,edges))
    if not tt:return None
    bar=sum(weights,F(0))/len(weights)
    z=F(0)
    for subset in tt:
        term=F(1)
        for i,w in enumerate(weights):
            if i not in subset:term*=w
        z+=term
    return bar*z,len(tt)


def formula(n,u):
    e=comb(n,2);beta=e-n+1
    assert n>=3
    return F(n**(n-3),e)*u**(beta-1)*(2*u+n-2)*(1+(e-1)*u)


def det(a):
    n=len(a)
    if not n:return F(1)
    z=F(1);a=[[F(t) for t in row] for row in a]
    for k in range(n):
        piv=next((i for i in range(k,n) if a[i][k]),None)
        if piv is None:return F(0)
        if piv!=k:
            a[piv],a[k]=a[k],a[piv];z=-z
        t=a[k][k];z*=t
        for i in range(k+1,n):
            m=a[i][k]/t
            for j in range(k+1,n):a[i][j]-=m*a[k][j]
            a[i][k]=0
    return z


def weighted_tree(n,edges,weights):
    a=[[F(0) for _ in range(n)] for _ in range(n)]
    for (i,j),w in zip(edges,weights):
        h=1/w
        a[i][i]+=h;a[j][j]+=h;a[i][j]-=h;a[j][i]-=h
    return det([row[:-1] for row in a[:-1]])

u=F(5,4)
check_count=0
for n in range(3,6):
    ee=list(combinations(range(n),2))
    observed=cotree_stat(n,ee,[F(1)]+[u]*(len(ee)-1))[0]
    assert observed==formula(n,u)
    assert formula(n,F(1))==n**(n-2)
    assert formula(n,u)>n**(n-2)
    check_count+=1

for n in range(2,5):
    ee=list(combinations(range(n),2))
    E=len(ee)
    for bits in range(1,1<<E):
        indices=[i for i in range(E) if (bits>>i)&1]
        edges=[ee[i] for i in indices]
        if not list(tree_subsets(n,edges)):continue
        for short in range(len(edges)):
            weights=[u for _ in edges];weights[short]=F(1)
            val,trees=cotree_stat(n,edges,weights)
            assert val-trees>=0
            beta=len(edges)-n+1
            included=sum(short in t for t in tree_subsets(n,edges))
            exact_extremal=(F(1)+(len(edges)-1)*u)/len(edges) * (included*u**beta+(trees-included)*u**(beta-1))
            assert exact_extremal==val
            if n>=3:
                assert val-trees<=formula(n,u)-n**(n-2)
            # Weighted matrix-tree identity, in exact rational arithmetic.
            complement=F(0)
            for subset in tree_subsets(n,edges):
                prod=F(1)
                for i,w in enumerate(weights):
                    if i not in subset:prod*=w
                complement+=prod
            prod=F(1)
            for w in weights:prod*=w
            assert complement==prod*weighted_tree(n,edges,weights)
            check_count+=1

# At n=3 the exact critical value solves (1+2u)^2=21/2.
assert formula(3,F(11,10)) < F(7,2)
assert formula(3,F(9,8)) > F(7,2)
# For n=4 compare exact rational brackets to the halfway threshold 33/2.
assert formula(4,F(1009,1000)) < F(33,2)
assert formula(4,F(101,100)) > F(33,2)
print('VERIFY_OK finite_exact_cases=',check_count, 'K3_F(5/4)=',str(formula(3,u)), 'K4_F(5/4)=',str(formula(4,u)))
