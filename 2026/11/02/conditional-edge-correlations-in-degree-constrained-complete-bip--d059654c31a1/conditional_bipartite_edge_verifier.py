#!/usr/bin/env python3
"""Finite exact independent enumeration for conditional edge dependencies in bipartite trees.

Only uses Python standard library. Directly enumerates edge subsets, checks they are trees,
then compares rational conditional frequencies against analytic formulae.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import factorial, prod
from itertools import combinations


def enumerate_trees(a, b):
    edges = tuple((i, a+j) for i in range(a) for j in range(b))
    groups = defaultdict(list)
    for subset in combinations(range(a*b), a+b-1):
        parent = list(range(a+b))
        def find(k):
            while parent[k] != k:
                k = parent[k]
            return k
        valid = True
        for t in subset:
            u, v = edges[t]
            ru, rv = find(u), find(v)
            if ru == rv:
                valid = False
                break
            parent[ru] = rv
        if not valid:
            continue
        d = [0]*(a+b)
        for t in subset:
            u, v = edges[t]
            d[u] += 1
            d[v] += 1
        groups[tuple(d)].append(frozenset(subset))
    return edges, groups


def pred(a,b,degree,e,f):
    assert a >= 2 and b >= 2
    m,p=b-1,a-1
    alpha=[v-1 for v in degree[:a]]
    beta=[v-1 for v in degree[a:]]
    i,j=e
    k,l=f
    Ai=F(alpha[i],m); Ak=F(alpha[k],m)
    Bj=F(beta[j],p); Bl=F(beta[l],p)
    aa=lambda u,v: F(alpha[u]*(alpha[v]-(u==v)),m*(m-1)) if m>=2 else F(0)
    bb=lambda u,v: F(beta[u]*(beta[v]-(u==v)),p*(p-1)) if p>=2 else F(0)
    pe=Ai+Bj-Ai*Bj
    pf=Ak+Bl-Ak*Bl
    if i==k:
        q=aa(i,i)*(1-Bj-Bl)+Ai*(Bj+Bl)
    elif j==l:
        q=bb(j,j)*(1-Ai-Ak)+Bj*(Ai+Ak)
    else:
        q=aa(i,k)*(1-Bj-Bl)+bb(j,l)*(1-Ai-Ak)+Ai*Bl+Ak*Bj
    return pe,pf,q


def check():
    tests=0
    table=[]
    for a,b in ((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4)):
        edges,groups=enumerate_trees(a,b)
        expected=a**(b-1)*b**(a-1)
        assert sum(map(len,groups.values()))==expected
        tests+=1
        for degree,trees in groups.items():
            N=len(trees)
            assert N>0
            alpha=[v-1 for v in degree[:a]]
            beta=[v-1 for v in degree[a:]]
            predicted_count=(factorial(b-1)*factorial(a-1))//(
                prod(factorial(v) for v in alpha+beta))
            assert N==predicted_count,(a,b,degree,N,predicted_count)
            tests+=1
            for eidx,fidx in combinations(range(a*b),2):
                (i,v),(k,w)=edges[eidx],edges[fidx]
                pe,pf,q=pred(a,b,degree,(i,v-a),(k,w-a))
                ne=sum(eidx in tree for tree in trees)
                nf=sum(fidx in tree for tree in trees)
                nef=sum(eidx in tree and fidx in tree for tree in trees)
                assert pe==F(ne,N),(a,b,degree,eidx,pe,ne,N)
                assert pf==F(nf,N),(a,b,degree,fidx,pf,nf,N)
                assert q==F(nef,N),(a,b,degree,eidx,fidx,q,nef,N)
                tests+=3
                cov=q-pe*pf
                if i==k or v==w:
                    assert cov<=0
                tests+=1
        table.append((a,b,len(groups),expected))
    # Smallest sharp positive covariance: two degree classes on K_{2,3}.
    a,b=2,3
    edges,groups=enumerate_trees(a,b)
    d=(2,2,2,1,1)
    es1=(0,3);es2=(1,4)
    P,Q,Pboth=pred(a,b,d,(0,1),(1,2))
    assert (P,Q,Pboth)==(F(1,2),F(1,2),F(1,2))
    assert Pboth-P*Q==F(1,4)
    tests+=2
    # Positive covariance persists without leaf endpoints, degree two at all four endpoints.
    a,b=4,4;d=(2,2,2,1,2,2,2,1)
    P,Q,Pboth=pred(a,b,d,(0,0),(1,1))
    assert (P,Q,Pboth)==(F(5,9),F(5,9),F(1,3))
    assert Pboth-P*Q==F(2,81)
    tests+=2
    print('PASSED',tests,'exact assertions over',table)
    print('K_2,3 sharp positive covariance = 1/4')
    print('K_4,4 four nonleaf endpoints positive covariance = 2/81')

if __name__=='__main__':
    check()
