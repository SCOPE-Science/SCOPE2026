#!/usr/bin/env python3
"""Exhaustive fixed-length alternating-cycle flip graphs of GP(12,5)."""
from collections import Counter, deque

N = 12
V = 2 * N
edges = sorted({tuple(sorted((a, b))) for i in range(N)
                for a, b in ((i, (i + 1) % N),
                             (i, i + N),
                             (i + N, (i + 5) % N + N))})
assert len(edges) == 36
edgeid = {e: i for i, e in enumerate(edges)}
neighbors = [set() for _ in range(V)]
for a, b in edges:
    neighbors[a].add(b)
    neighbors[b].add(a)
assert all(len(a) == 3 for a in neighbors)

# Every matching obtained by assigning a partner to the least unmatched vertex.
matchings = []
def enumerate_matching(free, chosen):
    if not free:
        matchings.append(frozenset(chosen))
        return
    a = min(free)
    for b in sorted(neighbors[a] & free):
        enumerate_matching(free - {a, b}, chosen + [edgeid[min(a, b), max(a, b)]])
enumerate_matching(set(range(V)), [])
matchings = sorted(set(matchings), key=lambda s:tuple(sorted(s)))
assert len(matchings) == 120
lookup = {m:i for i, m in enumerate(matchings)}

# Enumerate all simple unoriented 6- and 8-cycles in the underlying graph.
cycles = {4:set(), 6:set(), 8:set()}
for length in (4, 6, 8):
    for root in range(V):
        def dfs(path):
            cur = path[-1]
            if len(path) == length:
                if root in neighbors[cur] and path[1] < path[-1]:
                    ce = frozenset(edgeid[min(a,b), max(a,b)]
                                   for a,b in zip(path, path[1:]+[root]))
                    cycles[length].add(ce)
                return
            for b in neighbors[cur]:
                if b > root and b not in path:
                    dfs(path+[b])
        dfs([root])
print('CYCLES', {k:len(v) for k,v in cycles.items()})
assert len(cycles[4]) == 0

def build(length):
    adj = [set() for _ in matchings]
    for i, m in enumerate(matchings):
        for c in cycles[length]:
            # The cycle alternates precisely when half of its edges are selected.
            if len(m & c) != length//2:
                continue
            # Three or four matching edges in a simple 6- or 8-cycle can only
            # be an alternating perfect cycle-matching.
            other = m ^ c
            if other not in lookup:
                raise AssertionError('Flipped set not a perfect matching')
            j = lookup[other]
            adj[i].add(j)
    for i in range(len(adj)):
        for j in adj[i]:
            assert i != j and i in adj[j]
    return adj

def components(adj):
    unseen=set(range(len(adj)))
    sizes=[]
    while unseen:
        src=min(unseen)
        q=[src]
        unseen.remove(src)
        size=0
        while q:
            u=q.pop()
            size+=1
            for v in adj[u] & unseen:
                unseen.remove(v)
                q.append(v)
        sizes.append(size)
    return Counter(sizes)

def eccentricities(adj):
    ecc=[]
    shells=[]
    for src in range(len(adj)):
        dist={src:0}
        queue=deque([src])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v]=dist[u]+1
                    queue.append(v)
        assert len(dist)==len(adj)
        ecc.append(max(dist.values()))
        shells.append(tuple(Counter(dist.values())[i] for i in range(max(dist.values())+1)))
    return Counter(ecc), Counter(shells)

for length in (4,6,8):
    adj=build(length)
    ec=sum(map(len,adj))//2
    cc=components(adj)
    deg=Counter(map(len,adj))
    print('FLIP', length, 'vertices', len(adj), 'edges', ec, 'components', dict(sorted(cc.items())), 'degrees', dict(sorted(deg.items())))
    if length == 4:
        assert ec == 0 and cc == {1:120}
    elif length == 6:
        assert ec==192 and cc=={1:9,18:3,57:1}
    else:
        assert ec==414 and cc=={120:1}
        eccentricities_, shell_profiles = eccentricities(adj)
        print('METRIC', dict(sorted(eccentricities_.items())), 'shells',dict(sorted(shell_profiles.items())))
        assert eccentricities_=={4:72,5:42,6:6}
print('ALL_VERIFY_OK')
