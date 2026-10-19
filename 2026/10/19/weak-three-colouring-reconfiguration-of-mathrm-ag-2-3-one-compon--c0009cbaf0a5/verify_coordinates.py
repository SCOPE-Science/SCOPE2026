#!/usr/bin/env python3
"""Exhaustive independent-coordinate verification of weak three-colouring moves on AG(2,3)."""
import hashlib
import itertools
import json
from collections import Counter, deque

P = list(itertools.product(range(3), repeat=2))
INDEX = {p: i for i, p in enumerate(P)}
DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2))
LINES = set()
for x, y in P:
    for u, v in DIRECTIONS:
        LINES.add(tuple(sorted(INDEX[((x + k*u) % 3, (y + k*v) % 3)] for k in range(3))))
LINES = sorted(LINES)
assert len(LINES) == 12 and len(set(itertools.chain.from_iterable(LINES))) == 9

def valid(c):
    return all(not (c[a] == c[b] == c[d]) for a, b, d in LINES)

colors = [c for c in itertools.product(range(3), repeat=9) if valid(c)]
ids = {c: i for i, c in enumerate(colors)}
adj = []
for c in colors:
    neighbours = set()
    for p in range(9):
        for v in range(3):
            if v == c[p]:
                continue
            nc = c[:p] + (v,) + c[p+1:]
            j = ids.get(nc)
            if j is not None:
                neighbours.add(j)
    adj.append(tuple(sorted(neighbours)))
assert all(i in adj[j] for i, a in enumerate(adj) for j in a)
degree = Counter(map(len, adj))
composition = Counter(tuple(sorted(Counter(c).values())) for c in colors)
edge_pairs = [(i, j) for i, a in enumerate(adj) for j in a if i < j]
ecc = Counter()
ecc_by_kind = Counter()
pair_dist = Counter()
bis = [i for i, c in enumerate(colors) if tuple(sorted(Counter(c).values())) == (1, 4, 4)]
first_far = None
for source in range(len(colors)):
    distance = [-1] * len(colors)
    distance[source] = 0
    todo = deque([source])
    while todo:
        x = todo.popleft()
        for y in adj[x]:
            if distance[y] == -1:
                distance[y] = distance[x] + 1
                todo.append(y)
    assert all(d >= 0 for d in distance)
    rad = max(distance)
    ecc[rad] += 1
    k = tuple(sorted(Counter(colors[source]).values()))
    ecc_by_kind[(k, rad)] += 1
    if first_far is None and rad == 10:
        first_far = (colors[source], colors[distance.index(10)])
    if source in bis:
        for target in bis:
            if target > source:
                pair_dist[distance[target]] += 1

def sha_vertices(V):
    return hashlib.sha256(('\n'.join(''.join(map(str, c)) for c in V)+'\n').encode()).hexdigest()

def sha_edges(E):
    return hashlib.sha256(('\n'.join(f'{a},{b}' for a,b in E)+'\n').encode()).hexdigest()
report = {
    'lines': len(LINES), 'valid_two_colorings': sum(valid(c) for c in itertools.product(range(2), repeat=9)),
    'valid_three_colorings': len(colors), 'edges': len(edge_pairs),
    'degrees': {str(k): v for k, v in sorted(degree.items())},
    'color_class_sizes': {'-'.join(map(str,k)):v for k,v in sorted(composition.items())},
    'eccentricities': {str(k): v for k, v in sorted(ecc.items())},
    'eccentricity_by_type': {'-'.join(map(str,k))+'|'+str(d):v for (k,d),v in sorted(ecc_by_kind.items())},
    'bicoloring_distances': {str(k):v for k,v in sorted(pair_dist.items())},
    'radius': min(ecc), 'diameter': max(ecc), 'connected_components': 1,
    'diameter_witness': [''.join(map(str, c)) for c in first_far],
    'vertices_sha256': sha_vertices(colors), 'edges_sha256': sha_edges(edge_pairs)
}
assert report['valid_two_colorings']==0 and len(colors)==3762 and len(edge_pairs)==16848
assert degree==Counter({8:162,9:3600})
assert composition==Counter({(1,4,4):162,(2,3,4):2592,(3,3,3):1008})
assert ecc==Counter({9:3456,10:306})
assert sum(pair_dist.values())==162*161//2
print(json.dumps(report,sort_keys=True,separators=(',',':')))
print('VERIFY_OK')
