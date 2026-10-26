"""Finite exhaustive certificate for a hexagon-flip graph (stdlib only).

The bipartition is P={0,...,6} and L={0,...,6}; point i is
incident with line j exactly when (i-j) mod 7 lies in {0,1,3}.
"""
from itertools import permutations, combinations
from pathlib import Path
from collections import Counter
from hashlib import sha256
import json

D = {0, 1, 3}
lines = range(7)
inc = {(p, q) for p in lines for q in lines if (p - q) % 7 in D}
matchings = [tuple(f) for f in permutations(lines) if all((i, f[i]) in inc for i in lines)]
assert len(matchings) == 24 and len(set(matchings)) == 24
edges = {tuple(sorted((a, b))) for a, b in combinations(range(24), 2)
         if sum(matchings[a][i] != matchings[b][i] for i in lines) == 3}
assert len(edges) == 84
adj = [set() for _ in matchings]
for a, b in edges:
    adj[a].add(b)
    adj[b].add(a)
assert all(len(N) == 7 for N in adj)

def distances(root):
    dist = {root: 0}
    todo = [root]
    for a in todo:
        for b in sorted(adj[a]):
            if b not in dist:
                dist[b] = dist[a] + 1
                todo.append(b)
    assert len(dist) == 24
    return dist

all_dist = [distances(a) for a in range(24)]
assert all(Counter(d.values()) == {0: 1, 1: 7, 2: 14, 3: 2} for d in all_dist)
intersection = {}
for a in range(24):
    for b in range(24):
        t = all_dist[a][b]
        counts = tuple(sum(all_dist[a][c] == t + delta for c in adj[b])
                       for delta in (-1, 0, 1))
        if t in intersection:
            assert intersection[t] == counts, (a, b, t, counts)
        else:
            intersection[t] = counts
assert intersection == {0: (0, 0, 7), 1: (1, 2, 4),
                        2: (2, 4, 1), 3: (7, 0, 0)}

# Perfect one-factorizations are unlabelled triples partitioning all 21 edges.
fac = []
for a, b, c in combinations(range(24), 3):
    e1 = {(i, matchings[a][i]) for i in lines}
    e2 = {(i, matchings[b][i]) for i in lines}
    e3 = {(i, matchings[c][i]) for i in lines}
    if len(e1 | e2 | e3) == 21:
        assert (e1 | e2 | e3) == inc
        fac.append((a, b, c))
assert len(fac) == 8 and Counter(x for f in fac for x in f) == Counter({i: 1 for i in range(24)})
fiber = {x: j for j, triple in enumerate(fac) for x in triple}
for a in range(24):
    assert {b for b, d in all_dist[a].items() if d == 3} == (set(fac[fiber[a]]) - {a})
    assert Counter(fiber[b] for b in adj[a]) == Counter({j: 1 for j in range(8) if j != fiber[a]})
# Published 24-Klein adjacency data, saved alongside this certificate.
# Source: https://www.math.mun.ca/distanceregular/graphdata/klein.am
klein_rows = (Path(__file__).resolve().parent / 'klein_reference.am').read_text(encoding='ascii').splitlines()
assert len(klein_rows) == 24 and all(len(row) == 24 and set(row) <= {'0', '1'} for row in klein_rows)
assert all(klein_rows[i][i] == '0' and klein_rows[i][j] == klein_rows[j][i]
           for i in range(24) for j in range(24))
# Explicit vertex bijection to the published adjacency matrix; no graph
# isomorphism library, undocumented uniqueness classification, or network is used.
phi = (0, 11, 3, 4, 15, 6, 8, 19, 13, 9, 18, 21,
       7, 22, 17, 2, 1, 12, 14, 10, 16, 5, 23, 20)
assert sorted(phi) == list(range(24))
assert all((('1' if b in adj[a] else '0') == klein_rows[phi[a]][phi[b]])
           for a in range(24) for b in range(24))
triangle_count = sum(1 for a, b, c in combinations(range(24), 3) if b in adj[a] and c in adj[a] and c in adj[b])
assert triangle_count == 56
canonical = json.dumps({'matchings': matchings, 'edges': sorted(edges)}, separators=(',', ':'))
print('matchings=24; flips=84; degree=7; connected=yes; diameter=3; triangles=56')
print('intersection_counts_by_distance=' + repr(intersection))
print('one_factorizations=8; factorization_fibers_are_distance_3_triples=yes')
print('one_edge_per_distinct_fiber_per_vertex=yes')
print('explicit_isomorphism_to_klein_reference_adjacency=yes; entries_checked=576')
print('canonical_sha256=' + sha256(canonical.encode('utf-8')).hexdigest())
