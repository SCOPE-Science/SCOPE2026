"""Enumerate all six-vertex tight-5-cycle-free 3-graphs and their S6 orbits."""
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
import json
import sys

triples = list(combinations(range(6), 3))
bit = {edge: 1 << i for i, edge in enumerate(triples)}
cycles = {
    sum(bit[tuple(sorted(v[(i+j) % 5] for j in range(3)))] for i in range(5))
    for v in permutations(range(6), 5)
}
assert len(cycles) == 72
full = (1 << len(triples)) - 1
forbidden = bytearray(full + 1)
for c in cycles:
    complement = full ^ c
    y = complement
    while True:
        forbidden[c | y] = 1
        if y == 0:
            break
        y = (y-1) & complement

actions = [[bit[tuple(sorted(p[i] for i in edge))] for edge in triples]
           for p in permutations(range(6))]
seen = bytearray(full + 1)
labeled = Counter(mask.bit_count() for mask in range(full + 1) if not forbidden[mask])
types, extremal, near = {}, {}, []
by_edges = Counter()
for mask in range(full + 1):
    if forbidden[mask] or seen[mask]:
        continue
    ids = [i for i in range(len(triples)) if mask >> i & 1]
    m = len(ids)
    orbit = {sum(action[i] for i in ids) for action in actions}
    assert min(orbit) == mask and all(not forbidden[x] and not seen[x] for x in orbit)
    for x in orbit:
        seen[x] = 1
    types[mask] = (m, len(orbit))
    by_edges[m] += 1
    if m == 13:
        extremal[mask] = [''.join(map(str, triples[i])) for i in ids]
    if m == 12:
        near.append(len(orbit))

assert sum(seen) == sum(labeled.values()) == 371229 and len(types) == 835
assert [labeled[i] for i in range(21)] == [1,20,190,1140,4845,15432,37680,70140,95820,88220,46336,10280,1065,60]+[0]*7
assert [by_edges[i] for i in range(21)] == [1,1,3,7,21,42,91,146,195,176,111,33,7,1]+[0]*7
assert extremal == {131056: '023 024 025 034 035 045 123 124 125 134 135 145 234'.split()}
assert near == [90,45,15,180,360,360,15]
if len(sys.argv) == 2:
    catalog = json.loads(Path(sys.argv[1]).read_text())
    assert catalog['E6'] == 13 and catalog['n_types'] == len(types) == len(catalog['types'])
    assert catalog['n_labeled_free'] == sum(labeled.values())
    assert catalog['edge_dist_free'] == [labeled[i] for i in range(21)]
    assert len({t['canon'] for t in catalog['types']}) == len(types)
    for t in catalog['types']:
        assert sum(bit[tuple(e)] for e in t['rep']) == t['canon']
        assert types[t['canon']] == (t['edges_n'], t['count'])
    print('All catalogue rows agree.')
print('PASS: 371229 labeled graphs, 835 types; unique 13-edge orbit of size 60.')
