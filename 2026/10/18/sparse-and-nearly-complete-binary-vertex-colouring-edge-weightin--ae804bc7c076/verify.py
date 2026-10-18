#!/usr/bin/env python3
"""Exact checks for support extrema of proper binary edge-weightings of bicliques.

A bit 1 on (i,j) gives edge weight 1, and the vertex color is its
incident weight sum.  No external libraries or data are required.
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def proper(m, n, support):
    r = [0] * m
    c = [0] * n
    for e in support:
        i, j = divmod(e, n)
        r[i] += 1
        c[j] += 1
    return set(r).isdisjoint(c)


def block_assignments(m, n):
    # Independent occupancy recursion: a right vertex is either unused,
    # or receives a subset of at least two left vertices.
    f = [[0]*(m+1) for _ in range(n+1)]
    f[0][0] = 1
    for k in range(1,n+1):
        for a in range(m+1):
            f[k][a] = f[k-1][a] + sum(comb(a,s)*f[k-1][a-s] for s in range(2,a+1))
    return f[n][m]


def expected_extrema(m,n):
    if m==n==1:
        return None
    if m==1:
        return (2,n,comb(n,2),1)
    a = block_assignments(m,n)
    if m==n:
        return (m,m*n-m,2*a,2*a)
    return (m,m*n,a,1)


def brute_all(m,n):
    N=m*n
    obs=Counter()
    edges=range(N)
    for mask in range(1<<N):
        rs=[0]*m;cs=[0]*n; s=0
        for i in edges:
            if (mask>>i)&1:
                a,b=divmod(i,n);rs[a]+=1;cs[b]+=1;s+=1
        if set(rs).isdisjoint(cs):
            obs[s]+=1
    pred=expected_extrema(m,n)
    if pred is None:
        assert not obs, (m,n,obs)
        return 1<<N,len(obs)
    low,high,low_count,high_count=pred
    assert (min(obs),max(obs),obs[low],obs[high])==(low,high,low_count,high_count), (m,n,obs,pred)
    if n==m+1:
        if m==1:
            assert obs[1]==0
        else:
            assert obs[m*n-1]==obs[m*n-2]==0
            assert obs[m*n-3]==m*comb(n,3), (m,n,obs)
    if n>=m+2:
        assert obs[m*n-1]==m*n
    return 1<<N,len(obs)


def sparse_and_dense(m,n):
    N=m*n
    pred=expected_extrema(m,n)
    if pred is None:return 0
    lo,hi,lo_count,hi_count=pred
    L=sum(proper(m,n,c) for c in combinations(range(N),lo))
    assert L==lo_count,(m,n,'sparse',L,lo_count)
    H=sum(proper(m,n,c) for c in combinations(range(N),hi))
    assert H==hi_count,(m,n,'dense',H,hi_count)
    if m>=2 and n==m+1:
        cc=[sum(proper(m,n,tuple(e for e in range(N) if e not in removed))
                for removed in combinations(range(N),h)) for h in (1,2,3)]
        assert cc==[0,0,m*comb(n,3)],(m,n,cc)
    return L+H


def orbit_partition_multiplicities(m,n):
    # Formula per multiset of star sizes: two sides are distinguished if m<n.
    def partitions(total, smallest=2):
        if total==0:
            yield ()
            return
        for k in range(smallest,total+1):
            for z in partitions(total-k,k):
                yield (k,)+z
    fact=factorial(m)
    counted=0; types=0
    for lam in partitions(m):
        mult=Counter(lam)
        den=1
        for x in lam:den*=factorial(x)
        for x in mult.values():den*=factorial(x)
        inject=factorial(n)//factorial(n-len(lam))
        counted+=inject*fact//den
        types+=1
    assert counted==block_assignments(m,n),(m,n,counted)
    return types

if __name__ == '__main__':
    comparisons=0; total_masks=0
    for m in range(1,5):
        for n in range(m,8):
            if m*n<=16:
                t,_=brute_all(m,n)
                total_masks+=t;comparisons+=1
    additional=0
    for m,n in ((3,6),(4,5),(5,5),(5,6)):
        additional+=sparse_and_dense(m,n)
    for m in range(2,12):
        for n in (m,m+1,m+3):
            orbit_partition_multiplicities(m,n)
    print('PASS exhaustive matrices:',comparisons,'tested masks:',total_masks)
    print('PASS additional sparse/dense configurations:',additional)
    print('PASS orbit multiplicity identities:',30)
    print('PASS sharp three-deletion boundary for tested near-square rectangles')
