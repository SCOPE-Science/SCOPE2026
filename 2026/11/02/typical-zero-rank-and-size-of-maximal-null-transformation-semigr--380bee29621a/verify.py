#!/usr/bin/env python3
"""Independent finite verification for maximal null subsemigroups of full transformation monoids.
No external packages required. Run: python verify.py
"""
from collections import Counter
from itertools import product
from math import comb


def predicted(max_n, moment=0):
    b = [0]*(max_n+1)
    for k in range(1,max_n+1):
        if k<=2:
            b[k] = 1 if k==1 else 2
        else:
            b[k] = k*sum(comb(k-1,j-1)*(j**((k-j)*moment))
                         for j in range(2,k))
    dp = [[0]*(max_n+1) for _ in range(max_n+1)]
    dp[0][0] = 1
    for n in range(1,max_n+1):
        for r in range(1,n+1):
            dp[n][r] = sum(comb(n-1,k-1)*b[k]*dp[n-k][r-1] for k in range(1,n+1))
    return dp


def maximal_cliques(adjacency):
    # Maximal cliques in the graph of elements with fixed square and zero.
    def bk(R,P,X):
        if not P and not X:
            yield R
            return
        pivot = max(P|X, key=lambda p: len(P & adjacency[p])) if P|X else None
        options = set(P - adjacency[pivot]) if pivot is not None else set(P)
        for v in options:
            yield from bk(R|{v}, P & adjacency[v], X & adjacency[v])
            P.remove(v)
            X.add(v)
    vertices = set(adjacency)
    yield from bk(set(),vertices,set())


def direct(n):
    maps = list(product(range(n),repeat=n))
    def mul(f,g):
        return tuple(f[g[i]] for i in range(n))
    idempotents = [e for e in maps if mul(e,e)==e]
    counts = Counter()
    order_spectrum = Counter()
    for e in idempotents:
        cand = [f for f in maps if f!=e and mul(f,f)==e and mul(f,e)==e and mul(e,f)==e]
        adjacency = {f:set() for f in cand}
        for i,f in enumerate(cand):
            for g in cand[i+1:]:
                if mul(f,g)==e and mul(g,f)==e:
                    adjacency[f].add(g)
                    adjacency[g].add(f)
        for clique in maximal_cliques(adjacency):
            counts[len(set(e))] += 1
            order_spectrum[len(set(e)),len(clique)+1] +=1
    return counts,order_spectrum


def main():
    dp=predicted(12)
    known=[1,1,3,13,73,451,3211,26097,236433,2335123,24943171]
    for n,want in enumerate(known):
        got=sum(dp[n])
        assert got==want,(n,got,want)
    print('RECURRENCE_OK n=0..10',known)
    for n in range(1,5):
        actual,spectrum=direct(n)
        expected=Counter({r:dp[n][r] for r in range(1,n+1) if dp[n][r]})
        assert actual==expected,(n,actual,expected)
        print('DIRECT_OK n=',n,'zero_rank_spectrum=',dict(sorted(actual.items())), 'sizes=',dict(sorted(spectrum.items())))
    assert dp[4][1]==24 and dp[4][4]==1
    for moment in (1,2):
        weighted=predicted(4,moment=moment)
        for n in range(1,5):
            _,spectrum=direct(n)
            actual=Counter()
            for (r,order),cnt in spectrum.items():
                actual[r] += cnt*order**moment
            expected=Counter({r:weighted[n][r] for r in range(1,n+1) if weighted[n][r]})
            assert actual==expected,(n,moment,actual,expected)
        print('MOMENTS_OK',moment,'n=1..4')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
