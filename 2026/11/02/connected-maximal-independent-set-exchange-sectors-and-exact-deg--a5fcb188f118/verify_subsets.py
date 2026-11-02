#!/usr/bin/env python3
"""Direct exhaustive validation of maximal-independent-set exchanges on cycles."""
from collections import Counter, deque
from math import comb


def prediction(n, k):
    a, b = 3 * k - n, n - 2 * k
    if a < 0 or b < 0:
        return Counter()
    if a == 0 or b == 0:
        return Counter({0: n // k})
    return Counter({2*r: n*comb(a-1, r-1)*comb(b-1, r-1)//r
                    for r in range(1, min(a,b)+1)})


def run(n):
    # Independent and dominating are checked separately, with no gap encoding.
    universe = range(n)
    feasible = []
    for mask in range(1 << n):
        if any(mask & (1 << v) and mask & (1 << ((v+1) % n)) for v in universe):
            continue
        if any(not (mask & (1 << v) or mask & (1 << ((v-1) % n)) or
                    mask & (1 << ((v+1) % n))) for v in universe):
            continue
        feasible.append(mask)
    look = set(feasible)
    by_k = {}
    for x in feasible:
        by_k.setdefault(x.bit_count(), []).append(x)
    for k, verts in by_k.items():
        actual = Counter()
        graph = {}
        for x in verts:
            neigh = set()
            for u in range(n):
                if not (x >> u & 1):
                    continue
                for v in range(n):
                    if x >> v & 1:
                        continue
                    y = x ^ (1 << u) ^ (1 << v)
                    if y in look:
                        assert min((u-v)%n,(v-u)%n)==1, (n,k,u,v)
                        neigh.add(y)
            graph[x] = neigh
            actual[len(neigh)] += 1
        expected = prediction(n,k)
        assert actual == expected, (n,k,actual,expected)
        remaining = set(verts)
        components=[]
        while remaining:
            seed=remaining.pop(); q=deque([seed]); num=0
            while q:
                x=q.popleft(); num+=1
                for y in graph[x]:
                    if y in remaining:
                        remaining.remove(y); q.append(y)
            components.append(num)
        a,b=3*k-n,n-2*k
        expected_sizes = [1]*(n//k) if a==0 or b==0 else [sum(expected.values())]
        assert sorted(components)==sorted(expected_sizes), (n,k,components,expected_sizes)
        assert sum(actual.values()) == n*comb(k,a)//k
        assert sum(d*mult for d,mult in actual.items())//2 == (
            n*comb(k-2,a-1) if a and b else 0)
    return len(feasible),sum(sum(d*mult for d,mult in prediction(n,k).items())//2
                             for k in by_k),len(by_k)

if __name__=='__main__':
    for n in range(4,19):
        states,edges,sectors=run(n)
        print(f'n={n} maximal_sets={states} legal_edges={edges} k_sectors={sectors}')
    print('DIRECT_SUBSET_ENUMERATION_PASS')
