#!/usr/bin/env python3
"""Exact checks for partition-transfer clique counting and homology series.

No optional packages or external files. All arithmetic is integral.
"""
from functools import lru_cache
from math import comb

MAX_N = 65

@lru_cache(None)
def partitions(n, ceiling):
    if n == 0:
        return ((),)
    return tuple((k,) + tail
                 for k in range(min(n, ceiling), 0, -1)
                 for tail in partitions(n-k, k))

def young_cells(part):
    return frozenset((i, j) for i, width in enumerate(part) for j in range(width))

def direct_clique_profile(n):
    parts = partitions(n, n)
    cells = [young_cells(a) for a in parts]
    # Two Ferrers diagrams differ by an admissible unit transfer iff
    # the symmetric difference has exactly two cells.
    later = [set() for _ in parts]
    for i in range(len(parts)):
        for j in range(i+1, len(parts)):
            if len(cells[i] ^ cells[j]) == 2:
                later[i].add(j)
    profile = [0] * (n+2)
    def extend(size, candidates):
        for j in sorted(candidates):
            profile[size] += 1
            extend(size+1, candidates.intersection(later[j]))
    extend(0, set(range(len(parts))))
    while profile and profile[-1] == 0:
        profile.pop()
    return profile

def partition_numbers(N):
    p = [0] * (N+1)
    p[0] = 1
    for k in range(1, N+1):
        for n in range(k, N+1):
            p[n] += p[n-k]
    return p

def convolution(a, b, N):
    return [sum(a[k]*b[n-k] for k in range(n+1)) for n in range(N+1)]

def clique_profiles(N):
    p=partition_numbers(N+1)
    # h_r = P(t) / ((1-t)(1-t^2)...(1-t^r)); generated successively.
    h=p[:N+1]
    counts=[[0]*(N+1) for _ in range(N+2)]
    counts[1]=p[:N+1]
    for r in range(1, N+1):
        h=h[:]
        for n in range(r, N+1):
            h[n]+=h[n-r]
        if r<2: continue
        first=comb(r,2)+1
        second=comb(r+1,2)-1
        if first>N:break
        for n in range(first,N+1):
            counts[r][n]+=h[n-first]
        if r>=3:
            for n in range(second,N+1):
                counts[r][n]+=h[n-second]
    return counts, p

def direct_corner_profile(n, r):
    def ch(d,k):return comb(d,k) if d>=k else 0
    lower=sum(ch(len(set(p))+1,r) for p in partitions(n-1,n-1))
    upper=sum(ch(len(set(p)),r) for p in partitions(n+1,n+1))
    return lower if r==2 else lower+upper

def run():
    N=MAX_N
    counts,p=clique_profiles(N)
    chi=[0]*(N+1)
    b=[0]*(N+1)
    for n in range(1,N+1):
        chi[n]=sum((-1)**(r-1)*counts[r][n] for r in range(1,N+2))
        b[n]=chi[n]-1
    # Full source-published n<=25 Betti values (2603.26656, Table 1).
    source_b=[0,0,0,0,0,0,0,0,1,2,5,10,19,32,55,87,137,207,
              310,451,652,921,1293,1787,2453,3324]
    for n in range(1,26):
        assert b[n]==source_b[n],('published_b',n,b[n],source_b[n])
    # Published n>=26 clique profiles through 60, Table 3.
    for n, target in {26:(2436,18105,32465,16064,4257),
                      27:(3010,23286,42947,22059,6150),
                      29:(4565,38028,73856,40578,12424),
                      30:(5604,48297,96070,54438,17402)}.items():
        assert tuple(counts[r][n] for r in range(1,6))==target,('published_low_cliques',n)
    checked=0
    faces=0
    for n in range(1,17):
        actual=direct_clique_profile(n)
        predicted=[counts[r][n] for r in range(1,len(actual)+1)]
        assert actual==predicted,('direct_graph_cliques',n,actual,predicted)
        checked+=1
        faces+=sum(actual)
    # Independent Young-cover counts for a separate range (non-graph method).
    check_pairs=0
    for n in range(2,19):
        for r in range(2,11):
            observed=direct_corner_profile(n,r)
            assert observed==counts[r][n],('corner_counts',n,r,observed,counts[r][n])
            check_pairs+=1
    # General threshold and unique first maximum simplex tested through rank 10.
    for r in range(2,11):
        first=comb(r,2)+1
        assert counts[r][first]==1 and counts[r][first-1]==0,('first_threshold',r)
    # Closed rational Euler-Betti generating identity:
    # t*(1-t)^2*(1+t)*B(t) = (1-t-2t^2+t^3+t^4+t^5)*P(t) -(1-t^2)
    # The left multiplier has coefficients [0,1,-1,-1,1].
    L=[0,1,-1,-1,1]
    R=[1,-1,-2,1,1,1]
    for n in range(0,N+1):
        lhs=sum(L[k]*b[n-k] for k in range(min(n,4)+1))
        rhs=sum(R[k]*p[n-k] for k in range(min(n,5)+1))-(int(n==0)-int(n==2))
        assert lhs==rhs,('euler_identity',n,lhs,rhs)
    print('DIRECT_GRAPH_RANGE=1..16')
    print('DIRECT_GRAPH_COUNTS_CHECKED=%d'%checked)
    print('DIRECT_GRAPH_FACES_TOTAL=%d'%faces)
    print('INDEPENDENT_CORNER_CHECKS=%d'%check_pairs)
    print('PUBLISHED_HOMOLOGY_RANGE=1..25')
    print('PUBLISHED_CLIQUE_CHECKS=26,27,29,30 (sizes 1..5)')
    print('RATIONAL_BETTI_IDENTITY_RANGE=0..65')
    print('BETTI_CONSISTENCY_COUNTS_26..40='+repr({n:b[n] for n in range(26,41)}))
    print('FIRST_MAX_CLIQUE_THRESHOLDS='+repr([(r,comb(r,2)+1) for r in range(2,11)]))
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
