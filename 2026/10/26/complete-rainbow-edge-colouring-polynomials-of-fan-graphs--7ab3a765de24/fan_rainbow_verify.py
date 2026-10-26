#!/usr/bin/env python3
"""Independent checks for palette-sensitive rainbow-diamond colorings of fans.

The finite tests here corroborate, but do not replace, the stated proof.
"""
from itertools import combinations, product
from math import factorial


def fan_edges(n):
    return [(0, i) for i in range(1, n + 1)] + [(i, i + 1) for i in range(1, n)]


def conflict_D(n):
    edges = fan_edges(n)
    graph = {frozenset(e) for e in edges}
    ans = set()
    for a, b in combinations(range(len(edges)), 2):
        x, y = edges[a]
        z, w = edges[b]
        if len({x, y, z, w}) < 4:
            ans.add((a, b))
        elif sum(frozenset(t) in graph for t in [(x,z),(x,w),(y,z),(y,w)]) >= 3:
            ans.add((a, b))
    return ans


def conflict_B(n):
    edges = fan_edges(n)
    positions = {frozenset(e): i for i, e in enumerate(edges)}
    ans = set()
    for a, b in combinations(range(len(edges)), 2):
        if set(edges[a]) & set(edges[b]):
            ans.add((a,b))
    for verts in combinations(range(n+1), 4):
        for cycle in [(verts[0],verts[i],verts[j],verts[k]) for i,j,k in [(1,2,3),(1,3,2),(2,1,3)]]:
            pairs = [frozenset((cycle[i],cycle[(i+1)%4])) for i in range(4)]
            if all(pair in positions for pair in pairs):
                for a,b in combinations(sorted(positions[p] for p in pairs),2):
                    ans.add((a,b))
    return ans


def brute_normalized(n, q, conflicts):
    # Spokes fixed to 1,...,n; every fully named coloring has (q)_n choices of spokes.
    edges = fan_edges(n)
    adj = [set() for _ in edges]
    for a,b in conflicts:
        adj[a].add(b)
        adj[b].add(a)
    colors = list(range(1,n+1)) + [0]*(n-1)
    def rec(i):
        if i == len(edges):
            return 1
        total = 0
        for c in range(1,q+1):
            if any(colors[j] == c for j in adj[i] if j < i):
                continue
            colors[i] = c
            total += rec(i+1)
        colors[i] = 0
        return total
    return rec(n)


def inclusion_exclusion(n,q):
    # A block [a,b] represents equality of rim edge colors for indices a..b.
    def rec(a):
        if a == n:
            return 1
        result = 0
        for b in range(a,n):
            lo = max(1,a-1)
            hi = min(n,b+2)
            available = q - (hi-lo+1)
            result += (-1)**(b-a)*available*rec(b+1)
        return result
    return rec(1)


def state_dp(n,q):
    states={None:1}
    for i in range(1,n):
        forb=set(range(max(1,i-1),min(n,i+2)+1))
        choices=set(range(1,q+1))-forb
        states={c:sum(v for old,v in states.items() if old != c) for c in choices}
    return sum(states.values())


def constructive(n):
    assert n >= 5
    c=list(range(1,n+1)) + [i+3 for i in range(1,n-2)]+[1,2]
    assert len(c)==2*n-1
    for a,b in conflict_D(n):
        assert c[a] != c[b]


def main():
    cnt=0
    for n in range(2,9):
        d=conflict_D(n)
        b=conflict_B(n)
        assert d==b, (n,d^b)
        for q in range(n,min(n+3,10)):
            by_graph=brute_normalized(n,q,d)
            by_ie=inclusion_exclusion(n,q)
            by_dp=state_dp(n,q)
            assert by_graph==by_ie==by_dp, (n,q,by_graph,by_ie,by_dp)
            cnt+=1
    for n in range(5,80):
        constructive(n)
    for n in range(2,16):
        for q in range(n,n+3):
            assert inclusion_exclusion(n,q)==state_dp(n,q)
            cnt+=1
    assert [state_dp(n,n) for n in (5,6,7,8,9)] == [1,16,333,7040,162150]
    for n in range(2,9):
        def q_min():
            for q in range(1,11):
                if q<n: continue
                if state_dp(n,q)>0: return q
        assert q_min() == (3 if n==2 else max(n,5))
    print('VERIFY_OK independent_cases='+str(cnt)+' explicit_constructions=75', flush=True)

if __name__=='__main__':
    main()
