#!/usr/bin/env python3
"""Exhaustive independent adjacency verification for matching deletion."""
from collections import Counter
from math import comb


def analyze(n,t):
    N=2*n; k=n-2
    adj=[]
    for v in range(N):
        adj.append(sum(1<<w for w in range(N) if (v<n)!=(w<n) and not(v%n==w%n<t)))
    counts=Counter()
    for D in range(1<<N):
        O=((1<<N)-1)^D
        if all(((adj[v]&O).bit_count()<=k if (D>>v)&1 else bool(adj[v]&D)) for v in range(N)):
            counts[D.bit_count()]+=1
    return min(counts),counts[min(counts)], sum(counts.values())


def expected(n,t):
    if 2<=t<n:
        return 3,2*(n-t)*comb(t,2)
    return 4,comb(n,2)**2


def run():
    subsets=0;cases=0
    for n in range(3,9):
        for t in range(n+1):
            result=analyze(n,t)
            assert result[:2]==expected(n,t), (n,t,result,expected(n,t))
            print(f'n={n},t={t}, minimum={result[0]}, minimizers={result[1]}, feasible_total={result[2]}')
            subsets+=1<<(2*n);cases+=1
    print(f'VERIFIED {cases} graph profiles and {subsets} labeled candidate sets')
    print('ALL_MINIMA_AND_MULTIPLICITIES_PASS')
if __name__=='__main__':run()
