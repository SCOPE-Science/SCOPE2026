#!/usr/bin/env python3
"""Exhaustive distance certification for token slides of crown near-perfect matchings.

States are derangements of {0,...,n}; distinguished symbol 0 encodes two holes.
One BFS per stabilizer-conjugacy orbit is exhaustive by equivariance.
Requires only the Python standard library. Usage: python verify_permutations.py
"""
import collections
import itertools
import json
import math


def cycle_key(p):
    used = set()
    marked = None
    other = []
    for start in range(len(p)):
        if start in used:
            continue
        cyc = []
        x = start
        while x not in used:
            used.add(x)
            cyc.append(x)
            x = p[x]
        assert x == start
        if 0 in cyc:
            marked = len(cyc)
        else:
            other.append(len(cyc))
    assert marked is not None and marked >= 2
    return (marked, tuple(sorted(other)))


def subfactorial(k):
    if k == 0: return 1
    if k == 1: return 0
    a,b=1,0
    for j in range(2,k+1): a,b=b,(j-1)*(a+b)
    return b

def sign(p):
    inversions=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return 1 if inversions%2==0 else -1

def graph(n):
    m = n + 1
    states = [p for p in itertools.permutations(range(m))
              if all(p[i] != i for i in range(m))]
    ids = {p: i for i, p in enumerate(states)}
    adj = []
    for p in states:
        hole_row = p.index(0)
        neighbors = []
        for a in (0, hole_row):
            for b in range(1, m):
                if b == hole_row or b == a:
                    continue
                if p[a] == b or p[b] == a:
                    continue
                q = list(p)
                q[a], q[b] = q[b], q[a]
                neighbors.append(ids[tuple(q)])
        assert len(neighbors) == len(set(neighbors))
        adj.append(tuple(neighbors))
    for i, ns in enumerate(adj):
        for j in ns:
            assert i in adj[j]
    return states, adj


def distances(adj, source):
    dist = [-1] * len(adj)
    dist[source] = 0
    todo = collections.deque([source])
    while todo:
        v = todo.popleft()
        for w in adj[v]:
            if dist[w] == -1:
                dist[w] = dist[v] + 1
                todo.append(w)
    assert -1 not in dist
    return collections.Counter(dist)


def verify(n):
    states, adj = graph(n)
    reps = {}
    mult = collections.Counter()
    for i, p in enumerate(states):
        key = cycle_key(p)
        reps.setdefault(key, i)
        mult[key] += 1
    hist = collections.Counter(len(ns) for ns in adj)
    assert len(states) == subfactorial(n+1)
    assert hist[2*n-2] == n*subfactorial(n-1)
    assert hist[2*n-4] == subfactorial(n+1) - n*subfactorial(n-1)
    parity = [sign(p) for p in states]
    assert sum(parity) == (-1)**n*n
    assert all(parity[v] != parity[w] for v, neighbors in enumerate(adj) for w in neighbors)
    for (marked,other),size in mult.items():
        counts=collections.Counter(other)
        z=math.prod(j**a*math.factorial(a) for j,a in counts.items())
        assert size == math.factorial(n)//z
    pair_dist = collections.Counter()
    eccentricities = collections.Counter()
    orbit_data = []
    for key in sorted(reps):
        dist = distances(adj, reps[key])
        ecc = max(dist)
        size = mult[key]
        eccentricities[ecc] += size
        for d, count in dist.items():
            pair_dist[d] += size * count
        orbit_data.append(dict(marked_cycle=key[0],other_cycles=list(key[1]),
                               orbit_size=size,eccentricity=ecc,
                               spheres=[dist[d] for d in range(ecc + 1)]))
    assert pair_dist[0] == len(states)
    assert all(pair_dist[d] % 2 == 0 for d in pair_dist if d)
    result = dict(n=n, vertices=len(states), edges=sum(map(len,adj))//2,
                  orbit_count=len(reps), degree_histogram=dict(sorted(hist.items())),
                  radius=min(eccentricities),diameter=max(eccentricities),
                  eccentricity_histogram=dict(sorted(eccentricities.items())),
                  unordered_pair_distances=[pair_dist[d]//2 for d in range(1,max(eccentricities)+1)],
                  orbit_data=orbit_data)
    assert sum(result['unordered_pair_distances']) == len(states)*(len(states)-1)//2
    assert result['unordered_pair_distances'][0] == result['edges']
    return result

if __name__ == '__main__':
    for n in range(3,9):
        print(json.dumps(verify(n),sort_keys=True,separators=(',',':')))
