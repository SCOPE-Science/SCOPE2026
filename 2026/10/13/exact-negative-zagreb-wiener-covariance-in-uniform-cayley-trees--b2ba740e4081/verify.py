#!/usr/bin/env python3
"""Reproduce finite exact combinatorial checks for the labeled-tree Zagreb/Wiener identity.
This is finite corroboration; the all-n proof is in RESULT.md.
"""
from collections import deque
from fractions import Fraction
from itertools import product
from math import comb
from heapq import heapify, heappush, heappop


def prufer_tree(code, n):
    deg = [1] * n
    for x in code:
        deg[x] += 1
    leaves = [i for i in range(n) if deg[i] == 1]
    heapify(leaves)
    adj = [[] for _ in range(n)]
    for x in code:
        leaf = heappop(leaves)
        adj[leaf].append(x)
        adj[x].append(leaf)
        deg[leaf] -= 1
        deg[x] -= 1
        if deg[x] == 1:
            heappush(leaves, x)
    a, b = sorted(leaves)
    adj[a].append(b)
    adj[b].append(a)
    return adj


def invariants(adj):
    n = len(adj)
    z = sum(len(neighbors)**2 for neighbors in adj)
    parent = [-1] * n
    parent[0] = 0
    order = [0]
    for v in order:
        for w in adj[v]:
            if w != parent[v]:
                parent[w] = v
                order.append(w)
    assert len(order) == n
    sizes = [1] * n
    wiener = 0
    for v in reversed(order[1:]):
        a = sizes[v]
        wiener += a * (n - a)
        sizes[parent[v]] += a
    q = deque([0]); seen = {0}; depths={0:0}
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); depths[w]=depths[v]+1; q.append(w)
    distance = depths[1]
    return z, wiener, distance


def path_weight(n, k):
    falling = 1
    for j in range(k - 1):
        falling *= (n - 2 - j)
    return Fraction((k+1)*falling, n**k)


def expected_z(n):
    return Fraction(5*n-11,1)+Fraction(6,n)


def delta(n,k):
    return Fraction((k-1)*(2*n-k*(k+1)), n*(k+1))


def run(max_n=8):
    aggregate_cases=0; conditional_cases=0; checked_trees=0
    for n in range(2,max_n+1):
        N = n**(n-2)
        sZ=sW=sZW=0
        by_k={k:[0,0] for k in range(1,n)}
        for code in product(range(n),repeat=n-2):
            z,w,k = invariants(prufer_tree(code,n))
            sZ+=z; sW+=w; sZW+=z*w
            by_k[k][0]+=1; by_k[k][1]+=z
            checked_trees += 1
        ez=Fraction(sZ,N);ew=Fraction(sW,N)
        cov=Fraction(sZW,N)-ez*ew
        theoretical_ew=comb(n,2)*sum((k*path_weight(n,k) for k in range(1,n)), Fraction())
        theoretical_cov=2*n*(n-1)-Fraction(n+6,n)*theoretical_ew
        assert ez == expected_z(n),(n,'EZ',ez,expected_z(n))
        assert ew == theoretical_ew,(n,'EW',ew,theoretical_ew)
        assert cov == theoretical_cov,(n,'COV',cov,theoretical_cov)
        assert (cov < 0 if n>=4 else cov==0),(n,'SIGN',cov)
        aggregate_cases += 4
        for k, (count,s) in by_k.items():
            assert Fraction(count,N)==path_weight(n,k),(n,k,'DIST')
            assert Fraction(s,count)==expected_z(n)+delta(n,k),(n,k,'COND')
            conditional_cases +=2
        print(f'n={n} trees={N} E[Z]={ez} E[W]={ew} Cov(Z,W)={cov}')
    print(f'PASS total_trees={checked_trees} aggregate_checks={aggregate_cases} conditional_checks={conditional_cases}')

if __name__=='__main__':
    run()
