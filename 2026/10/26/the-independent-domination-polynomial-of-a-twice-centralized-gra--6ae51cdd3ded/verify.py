#!/usr/bin/env python3
"""Reproducible exact enumeration for double-central-graph independent domination.
Only standard-library Python is used. Graphs are finite, simple and labelled.
"""
from collections import Counter
from itertools import combinations
from random import Random


def central(n, edges):
    edge_set = {tuple(sorted(e)) for e in edges}
    m = len(edge_set)
    ordered = sorted(edge_set)
    out = []
    for i, (u, v) in enumerate(ordered):
        out.extend([(u, n+i), (v, n+i)])
    for u in range(n):
        for v in range(u+1,n):
            if (u,v) not in edge_set:
                out.append((u,v))
    return n+m, out


def formula(n, edges):
    m = len(edges)
    M = m + n*(n-1)//2
    C = Counter({M:1})
    C[M-1] += m
    C[M-n+2] += 2*m
    edge_set = set(edges)
    for mask in range(1, 1<<n):
        k = mask.bit_count()
        if all(not ((mask>>u)&1 and (mask>>v)&1) for u,v in edge_set):
            C[M-(n-1)*k+k*(k+1)//2] += 1
    return +C


def find_all_maximal_independent_polynomial(n, edges):
    # A maximal independent set is exactly an independent dominating set.
    neighbor = [0]*n
    for u,v in edges:
        neighbor[u] |= 1<<v
        neighbor[v] |= 1<<u
    mask_all = (1<<n)-1
    comp = [mask_all & ~(neighbor[i] | (1<<i)) for i in range(n)]
    result = Counter()
    def visit(size, P, X):
        if not (P|X):
            result[size] += 1
            return
        domain = P|X
        # Standard Bron--Kerbosch pivoting on the complement adjacency.
        pivot = max((v for v in range(n) if (domain>>v)&1),
                    key=lambda v: (P & comp[v]).bit_count())
        candidates = P & ~comp[pivot]
        while candidates:
            vb = candidates & -candidates
            v = vb.bit_length()-1
            visit(size+1, P & comp[v], X & comp[v])
            P &= ~vb
            X |= vb
            candidates &= ~vb
    visit(0, mask_all, 0)
    return +result


def connected(n, edges):
    seen={0}
    while True:
        nxt=seen | {v for u,v in edges if u in seen} | {u for u,v in edges if v in seen}
        if len(nxt)==len(seen):
            return len(seen)==n
        seen=nxt


def verify(n, edges):
    host_edges = {tuple(sorted(e)) for e in edges}
    Hn, He = central(n, host_edges)
    Jn, Je = central(Hn, He)
    got = find_all_maximal_independent_polynomial(Jn, Je)
    want = formula(n, host_edges)
    assert got == want, (n, sorted(host_edges), got, want)
    # Optimizer classification: complete, star, or maximum independent sets.
    mini = min(got)
    Nmin = got[mini]
    alpha = max(k for mask in range(1<<n)
                if not any((mask>>u)&1 and (mask>>v)&1 for u,v in host_edges)
                for k in [mask.bit_count()])
    nummax = sum(1 for mask in range(1<<n)
                 if mask.bit_count()==alpha and
                    not any((mask>>u)&1 and (mask>>v)&1 for u,v in host_edges))
    if n == 3:
        pass
    elif alpha==1:
        assert Nmin==n*n, (n, Nmin)
    elif alpha==n-1:
        assert Nmin==n, (n, Nmin)
    else:
        assert Nmin==nummax, (n, Nmin, nummax)
    return len(got), sum(got.values())


def main():
    total=0; sums=0
    for n in (3,4,5):
        pairs=list(combinations(range(n),2))
        count=0
        for mask in range(1<<len(pairs)):
            edges={pair for i,pair in enumerate(pairs) if (mask>>i)&1}
            if not connected(n, edges):
                continue
            k,v=verify(n,edges)
            count+=1; sums+=v
        total+=count
        print(f'n={n} exhaustive connected labelled hosts={count}')
    random=Random(20261024)
    n=6
    pairs=list(combinations(range(n),2))
    count=0
    while count<100:
        edges={p for p in pairs if random.random()<0.53}
        if connected(n,edges):
            verify(n,edges)
            count+=1
    print(f'n=6 seeded connected labelled hosts={count}')
    print(f'VERIFY_OK host_graphs={total+count} independent_domination_sets_checked={sums}')

if __name__=='__main__':
    main()
