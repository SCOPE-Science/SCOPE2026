"""Check the two matching certificates independently of degree-balance algebra.

The base is a multigraph. Random permutation covers are only experimental
witnesses; existence for arbitrary girth requires the separate covering proof.
"""

import itertools
import random
from collections import Counter, deque


def template(d):
    groups = {}
    n = 0
    for name, size in [('A0', 2), ('A1', 2*(d-1)), ('AD', 2*(d-1)),
                       ('B0', 2*(d-1)), ('B1', 2*(d-1)**2),
                       ('BD', 2*(d-1)**2)]:
        groups[name] = list(range(n, n+size))
        n += size
    edges, bad, good = [], [], []

    def add(u, v, which=''):
        i = len(edges)
        edges.append((u, v))
        if 'b' in which:
            bad.append(i)
        if 'g' in which:
            good.append(i)

    add(*groups['A0'], 'bg')
    for u, v in zip(groups['A1'], groups['AD']):
        add(u, v, 'b')
    for u, v in zip(groups['A1'], groups['B0']):
        add(u, v, 'g')
    for i, u in enumerate(groups['AD']):
        for v in groups['B1'][i*(d-1):(i+1)*(d-1)]:
            add(u, v)
    for u, v in zip(groups['B1'][::2], groups['B1'][1::2]):
        add(u, v, 'g')
    stubs = [u for u in groups['A0'] for _ in range(d-1)]
    stubs += [u for u in groups['A1'] for _ in range(d-2)]
    for u, v in zip(stubs, groups['BD']):
        add(u, v)
    capacity = {v: d-1 for v in groups['BD']}
    for u in groups['B0'] + groups['B1']:
        need = d-1 if u in groups['B0'] else d-2
        targets = sorted(capacity, key=lambda v: (-capacity[v], v))[:need]
        for v in targets:
            assert capacity[v] > 0
            add(u, v)
            capacity[v] -= 1
    assert not any(capacity.values())
    return n, edges, bad, good


def cover(n, edges, bad, good, sheets, rng):
    # First take the bipartite double cover; then a permutation cover.
    result, b, g = [], [], []
    for j, (u, v) in enumerate(edges):
        for side in range(2):
            perm = list(range(sheets))
            rng.shuffle(perm)
            for i, p in enumerate(perm):
                k = len(result)
                result.append(((2*u+side)*sheets+i,
                               (2*v+1-side)*sheets+p))
                if j in bad:
                    b.append(k)
                if j in good:
                    g.append(k)
    return 2*n*sheets, result, b, g


def verify(n, edges, bad, good, d):
    adj = [set() for _ in range(n)]
    degree = Counter(v for edge in edges for v in edge)
    assert all(degree[v] == d for v in range(n))
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen = set()
    components = []
    for start in range(n):
        if start in seen:
            continue
        reached = {start}
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u] - reached:
                reached.add(v)
                queue.append(v)
        seen.update(reached)
        components.append(reached)
    for comp in components:
        nb = sum(edges[i][0] in comp for i in bad)
        ng = sum(edges[i][0] in comp for i in good)
        assert 2*d*nb == len(comp)
        assert ng*(2*d-1) == nb*d*d
    simple = len({tuple(sorted(e)) for e in edges}) == len(edges)
    assert all(u != v for u, v in edges)

    def conflict(i, j):
        a, b = edges[i]
        c, e = edges[j]
        return (len({a, b, c, e}) < 4 or c in adj[a] or e in adj[a]
                or c in adj[b] or e in adj[b])

    for matching in [bad, good]:
        assert all(not conflict(i, j)
                   for i, j in itertools.combinations(matching, 2))
    # An independent global-optimum certificate: every edge intersects exactly
    # one good matching edge. This attains the universal incident-edge bound.
    owner = {}
    for i in good:
        for v in edges[i]:
            assert v not in owner
            owner[v] = i
    assert all(len({owner[v] for v in e if v in owner}) == 1 for e in edges)

    if simple and girth(n, edges) >= 6:
        # Explicitly enumerate the complete possible 1-for-2 replacement pool.
        for removed in bad:
            others = set(bad) - {removed}
            pool = [j for j in range(len(edges)) if j not in bad
                    and all(not conflict(j, i) for i in others)]
            assert all(conflict(i, j) for i, j in itertools.combinations(pool, 2))
        assert all(any(conflict(i, j) for i in bad) for j in range(len(edges)))
        assert len(good)*(2*d-1) == len(edges)
    assert len(bad)*2*d == n
    assert len(good)*(2*d-1) == len(bad)*d*d
    return simple, len(components)


def girth(n, edges):
    if len({tuple(sorted(e)) for e in edges}) != len(edges):
        return 2
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    best = n+1
    for start in range(n):
        dist, parent = {start: 0}, {start: None}
        queue = deque([start])
        while queue:
            u = queue.popleft()
            if 2*dist[u] >= best:
                continue
            for v in adj[u]:
                if v not in dist:
                    dist[v], parent[v] = dist[u]+1, u
                    queue.append(v)
                elif parent[u] != v and parent[v] != u:
                    best = min(best, dist[u]+dist[v]+1)
    return best


if __name__ == '__main__':
    for d in range(3, 9):
        data = template(d)
        verify(*data, d)
        print('base', d, 'vertices', data[0], 'edges', len(data[1]),
              'bad', len(data[2]), 'good', len(data[3]))
    rng = random.Random(108007)
    for trial in range(1000):
        data = cover(*template(3), 8, rng)
        if girth(data[0], data[1]) >= 6:
            simple, components = verify(*data, 3)
            # Independently check the double-cover bipartition.
            assert all((u//8) % 2 != (v//8) % 2 for u, v in data[1])
            print('verified cover', 'trial', trial, 'n', data[0],
                  'girth', girth(data[0], data[1]),
                  'components', components,
                  'bad', len(data[2]), 'optimum', len(data[3]),
                  'ratio', len(data[3])/len(data[2]))
            break
    else:
        raise RuntimeError('No high-girth experimental witness found')
