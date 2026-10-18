#!/usr/bin/env python3
"""Definition-level checks of dual general-position sets in triangular graphs.

Reproducible with Python 3 standard library: python verify_dual_gp.py
"""
from itertools import combinations
from collections import Counter, deque
from random import Random


def make_graph(n):
    edges = list(combinations(range(n), 2))
    neighbors = [set() for _ in edges]
    for i, e in enumerate(edges):
        for j, f in enumerate(edges):
            if i != j and (e[0] in f or e[1] in f):
                neighbors[i].add(j)
    return edges, neighbors


def distances(adj):
    out = []
    for src in range(len(adj)):
        d = [-1] * len(adj)
        d[src] = 0
        q = deque([src])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] == -1:
                    d[v] = d[u] + 1
                    q.append(v)
        assert -1 not in d
        out.append(d)
    return out


def is_dual(mask, pairs):
    # A pair is checked exactly when its endpoints are on the same side
    # (both selected or both unselected), as in the definition.
    for a, b, mids in pairs:
        if (bool(mask & (1 << a)) == bool(mask & (1 << b))
                and mask & mids):
            return False
    return True


def check(n, exhaustive=True, samples=0):
    edges, adj = make_graph(n)
    ds = distances(adj)
    pairs = []
    for a, b in combinations(range(len(edges)), 2):
        mids = sum(1 << w for w in range(len(edges))
                   if w not in (a, b) and ds[a][w]+ds[w][b]==ds[a][b])
        if mids:
            pairs.append((a, b, mids))

    def predicted(mask):
        if n == 3:
            return True
        chosen = {edges[j] for j in range(len(edges)) if mask & (1 << j)}
        if not chosen:
            return True
        stars = [{e for e in edges if u in e} for u in range(n)]
        if chosen in stars:
            return True
        if n == 4:
            return any(chosen == set(combinations(t, 2))
                       for t in combinations(range(n), 3))
        return False

    total = 0
    count = Counter()
    size = len(edges)
    if exhaustive:
        masks = range(1 << size)
    else:
        rng = Random(20261015+n)
        masks = [0, (1 << size)-1]
        masks += [sum(1 << j for j, e in enumerate(edges) if u in e)
                  for u in range(n)]
        masks += [rng.randrange(1 << size) for _ in range(samples)]
    for m in masks:
        found = is_dual(m, pairs)
        assert found == predicted(m), (n, m, found, predicted(m))
        if found:
            count[m.bit_count()] += 1
        total += 1
    if exhaustive:
        target = ({k: __import__('math').comb(3,k) for k in range(4)} if n == 3
                  else {0:1,3:8} if n == 4 else {0:1,n-1:n})
        assert dict(count) == target, (n, dict(count), target)
    return total, dict(sorted(count.items()))


def main():
    examined=0
    for n in range(3,7):
        count, histogram=check(n)
        examined+=count
        print(f'EXHAUSTIVE n={n} tested={count} dual_size_counts={histogram}')
    randomized=0
    for n in (7,8):
        count,_=check(n,exhaustive=False,samples=5000)
        randomized+=count
        print(f'SAMPLED n={n} tested={count}')
    print(f'VERIFICATION_OK exhaustive_masks={examined} sampled_masks={randomized} n=3..8')

if __name__=='__main__':
    main()
