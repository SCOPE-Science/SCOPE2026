#!/usr/bin/env python3
"""Finite reproducibility checks for the edge-girth-four order theorem.
No external libraries or network access required.
"""
from itertools import combinations
from math import isqrt


def ceil_two_sqrt(m):
    k = isqrt(4 * m)
    return k if k*k == 4*m else k + 1


def make_witness(m):
    if m == 4:
        return 4, [(0,1),(1,2),(2,3),(0,3)]
    if m < 6:
        raise ValueError('no realization')
    n = ceil_two_sqrt(m)
    a, b = n//2, (n+1)//2
    d = a*b-m
    assert n >= 5 and 0 <= d <= a-1
    edges = [(i,a+j) for i in range(a) for j in range(b) if not (i==j and i<d)]
    return n, edges


def graph_check(n, edges):
    E = set(tuple(sorted(e)) for e in edges)
    assert len(E) == len(edges)
    assert all(0 <= x < n and 0 <= y < n and x != y for x,y in edges)
    nei = [set() for _ in range(n)]
    for u,v in edges:
        nei[u].add(v)
        nei[v].add(u)
    seen={0}; pending=[0]
    while pending:
        u=pending.pop()
        for v in nei[u]-seen:
            seen.add(v);pending.append(v)
    if len(seen)!=n:
        return False
    for u,v in edges:
        if nei[u] & nei[v]:
            return False   # Every triangle would give edge-girth 3.
        # Edge uv belongs to a 4-cycle iff there are u' and v' such that
        # u-v-u'-v'-u are four distinct vertices with all edges present.
        if not any(y in nei[x] for x in nei[v] - {u} for y in nei[u] - {v}):
            return False
    return True


def exhaustive_small():
    # Full labelled edge-subset enumeration, not graph-isomorphism sampling.
    cases=0; best={}
    for n in range(1,7):
        all_pairs=list(combinations(range(n),2))
        for mask in range(1<<len(all_pairs)):
            if not mask:
                continue
            edges=[e for i,e in enumerate(all_pairs) if (mask>>i)&1]
            cases+=1
            if graph_check(n,edges):
                m=len(edges)
                best[m]=min(best.get(m,n),n)
    assert best == {4:4,6:5,7:6,8:6,9:6},best
    return cases,best


def all_witnesses():
    tested=0
    for m in [4]+list(range(6,3001)):
        n,edges=make_witness(m)
        assert n == ceil_two_sqrt(m) and len(edges)==m
        assert m <= (n*n)//4
        assert (n-1)*(n-1)//4 < m or m==4
        assert graph_check(n, edges), (m,n)
        tested+=1
    return tested


if __name__ == '__main__':
    cases, best = exhaustive_small()
    tested = all_witnesses()
    print('EXHAUSTIVE_LABELED_GRAPH_CASES',cases)
    print('ALL_EDGE_GIRTH_4_ORDER_MINIMA_THROUGH_N6',sorted(best.items()))
    print('EXPLICIT_OPTIMUM_WITNESSES_CHECKED',tested)
    print('RANGE_M','4 and 6..3000')
    print('ALL_CHECKS_PASSED')
