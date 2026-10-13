#!/usr/bin/env python3
"""Reproducible checks for the Roman-domination polynomial of triangular graphs.
Only standard-library Python is required. Finite checks supplement the proof.
"""
from collections import Counter
from itertools import product, combinations
from math import comb, factorial


def nonisolated_graph_count(c, k):
    return sum((-1)**j * comb(c, j) * comb(comb(c-j, 2), k)
               for j in range(c+1) if k <= comb(c-j, 2))


def polynomial(n):
    m=comb(n,2)
    a=Counter({m:1}) # no label-2 vertices forces all-one
    for c in range(2,n+1):
        r=n-c
        a1=comb(r,2)
        for k in range(1, comb(c,2)+1):
            q=nonisolated_graph_count(c,k)
            if q==0:continue
            for j in range(m-k-a1+1):
                a[2*k+a1+j]+=comb(n,c)*q*comb(m-k-a1,j)
    return {k:v for k,v in a.items() if v}


def brute(n):
    edges=list(combinations(range(n),2))
    neighborhoods=[set(j for j,f in enumerate(edges) if j!=i and (set(e)&set(f))) for i,e in enumerate(edges)]
    result=Counter()
    for vals in product((0,1,2),repeat=len(edges)):
        twos={i for i,v in enumerate(vals) if v==2}
        if all(vals[i]!=0 or (neighborhoods[i]&twos) for i in range(len(vals))):
            result[sum(vals)]+=1
    return dict(result)


def by_label2_subsets(n):
    edges=list(combinations(range(n),2)); m=len(edges)
    total=Counter()
    for mask in range(1<<m):
        k=mask.bit_count()
        if not k:
            total[m]+=1
            continue
        support=set()
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:support.update((u,v))
        forced=comb(n-len(support),2)
        for i in range(m-k-forced+1):
            total[2*k+forced+i]+=comb(m-k-forced,i)
    return dict(total)


def odd_double_factorial(j):
    prod=1
    while j>0:
        prod*=j; j-=2
    return prod

checks=0
for n in range(0,6):
    p=polynomial(n)
    b=brute(n)
    assert p==b,(n,p,b)
    checks+=sum(b.values())
    print('brute n',n,'Roman labels',sum(b.values()),'minimum',min(b) if b else None)
for n in range(0,7):
    p=polynomial(n)
    q=by_label2_subsets(n)
    assert p==q,n
    print('support-subset n',n,'count',sum(q.values()))
for n in range(3,19):
    p=polynomial(n)
    expected=(n*odd_double_factorial(n-2) if n%2 else comb(n,2)*odd_double_factorial(n-3))
    assert min(p)==n-1 and p[n-1]==expected,(n,min(p),p[n-1],expected)
print('OK exhaustive labelings through n=5:',checks)
print('OK independent label-2-subset enumeration through n=6')
print('OK minimum weight and multiplicity for n=3..18')
