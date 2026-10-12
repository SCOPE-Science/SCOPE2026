#!/usr/bin/env python3
"""Reproduce optimal cyclic factor covers avoiding constant length-three runs."""
from collections import Counter, defaultdict


def admissible(s):
    return '000' not in s and '111' not in s


def blocks(n):
    return {format(x, '0%db' % n) for x in range(1 << n)
            if admissible(format(x, '0%db' % n))}


def graph_and_cover(n):
    assert n >= 3
    vertices = sorted(blocks(n-1))
    edges = [(s, s[1:]+b, s+b) for s in vertices for b in '01'
             if admissible(s+b)]
    indeg = Counter(v for _, v, _ in edges)
    outdeg = Counter(u for u, _, _ in edges)
    sources = [s for s in vertices if indeg[s]-outdeg[s] == 1]
    targets = [t for t in vertices if outdeg[t]-indeg[t] == 1]
    assert len(sources) == len(targets)
    endpoints = {}
    cost = 0
    for s in sources:
        d = next(i for i in range(1, n-2) if s[i] == s[i+1])
        current = s
        for _ in range(d):
            b = '1' if current[-1] == '0' else '0'
            nxt = current[1:] + b
            assert admissible(current+b)
            edges.append((current, nxt, current+b))
            current = nxt
        assert current in targets
        assert current not in endpoints.values(), ('non-bijective endpoint',n,s,current)
        endpoints[s] = current
        cost += d
    assert set(endpoints.values()) == set(targets)
    indeg = Counter(v for _, v, _ in edges)
    outdeg = Counter(u for u, _, _ in edges)
    assert all(indeg[x] == outdeg[x] for x in vertices)
    adj = defaultdict(list)
    for i, (u, _, _) in enumerate(edges):
        adj[u].append(i)
    stack = [(vertices[0], None)]
    tour = []
    while stack:
        u, incoming = stack[-1]
        if adj[u]:
            eid = adj[u].pop()
            stack.append((edges[eid][1], eid))
        else:
            stack.pop()
            if incoming is not None:
                tour.append(incoming)
    tour.reverse()
    assert len(tour) == len(edges)
    assert all(edges[tour[i]][1] == edges[tour[(i+1)%len(tour)]][0]
               for i in range(len(tour)))
    cycle = ''.join(edges[eid][2][-1] for eid in tour)
    observed = {''.join(cycle[(j+i) % len(cycle)] for i in range(n))
                for j in range(len(cycle))}
    assert observed == blocks(n)
    assert all(admissible(''.join(cycle[(j+i)%len(cycle)] for i in range(3)))
               for j in range(len(cycle)))
    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0+f1
    # On exit f0=F_(n-1), f1=F_n.
    assert len(blocks(n)) == 2*(f0+f1)
    assert cost == 2*f0-2
    assert len(cycle) == 2*(2*f0+f1-1)
    return len(blocks(n)), cost, len(cycle), len(sources), cycle


if __name__ == '__main__':
    for k in range(3, 15):
        count, extra, minimum, sources, word = graph_and_cover(k)
        print('n=%d admissible=%d repeated=%d optimal=%d imbalance=%d' %
              (k, count, extra, minimum, sources))
        if k <= 5:
            print('example=%s' % word)
    print('VERIFY_OK')
