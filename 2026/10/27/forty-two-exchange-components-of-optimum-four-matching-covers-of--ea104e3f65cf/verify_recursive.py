#!/usr/bin/env python3
"""Exhaustive four-perfect-matching-cover exchange census of the five-petal flower snark."""
import collections
import itertools
import json
import sys

N = 5
vertices = [(t, i) for t in 'abcd' for i in range(N)]
index = {v: k for k, v in enumerate(vertices)}
E = set()
def add(a, b):
    E.add(tuple(sorted((index[a], index[b]))))
for i in range(N):
    for t in 'bcd':
        add(('a', i), (t, i))
    add(('b', i), ('b', (i + 1) % N))
ring = [('c', i) for i in range(N)] + [('d', i) for i in range(N)]
for i in range(2*N):
    add(ring[i], ring[(i + 1) % (2*N)])
edges = tuple(sorted(E))
assert len(edges) == 30
neighbors = [[] for _ in vertices]
for j, (a, b) in enumerate(edges):
    neighbors[a].append((b, j))
    neighbors[b].append((a, j))
assert all(len(x) == 3 for x in neighbors)

matchings = []
def match(free, mask):
    if not free:
        matchings.append(mask)
        return
    v = (free & -free).bit_length() - 1
    rest = free & ~(1 << v)
    for w, j in neighbors[v]:
        if rest & (1 << w):
            match(rest & ~(1 << w), mask | (1 << j))
match((1 << len(vertices)) - 1, 0)
matchings = tuple(sorted(matchings))
assert len(matchings) == len(set(matchings)) == 32
full_edge = (1 << len(edges)) - 1
assert all((matchings[a] | matchings[b] | matchings[c]) != full_edge
           for a, b, c in itertools.combinations(range(len(matchings)), 3))
covers = []
for idx in itertools.combinations(range(len(matchings)), 4):
    if (matchings[idx[0]] | matchings[idx[1]] |
        matchings[idx[2]] | matchings[idx[3]]) == full_edge:
        covers.append(idx)
assert len(covers) == 200

triples = collections.defaultdict(list)
for i, c in enumerate(covers):
    for three in itertools.combinations(c, 3):
        triples[three].append(i)
adj = [set() for _ in covers]
for clique in triples.values():
    for a, b in itertools.combinations(clique, 2):
        adj[a].add(b)
        adj[b].add(a)
components = []
unseen = set(range(len(covers)))
while unseen:
    seed = min(unseen)
    todo = [seed]
    unseen.remove(seed)
    comp = []
    while todo:
        v = todo.pop()
        comp.append(v)
        for w in adj[v] & unseen:
            unseen.remove(w)
            todo.append(w)
    components.append(tuple(sorted(comp)))

# Explicit finite graph-isomorphism check, with degrees as admissibility constraint.
def iso(component_a, component_b):
    if len(component_a) != len(component_b):
        return False
    da = {v: len(adj[v]) for v in component_a}
    db = {v: len(adj[v]) for v in component_b}
    if sorted(da.values()) != sorted(db.values()):
        return False
    aa = tuple(sorted(component_a, key=lambda v: (-da[v], v)))
    targets = {v: [w for w in component_b if db[w] == da[v]] for v in aa}
    f = {}
    used = set()
    def rec(depth):
        if depth == len(aa):
            return True
        v = aa[depth]
        for w in targets[v]:
            if w in used:
                continue
            if all((u in adj[v]) == (f[u] in adj[w]) for u in f):
                f[v] = w
                used.add(w)
                if rec(depth + 1):
                    return True
                used.remove(w)
                del f[v]
        return False
    return rec(0)

classes = []
for comp in components:
    for representative, members in classes:
        if iso(representative, comp):
            members.append(comp)
            break
    else:
        classes.append((comp, [comp]))

def comp_data(comp):
    return {'order': len(comp), 'edges': sum(len(adj[u]) for u in comp)//2,
            'degrees': dict(sorted(collections.Counter(len(adj[u]) for u in comp).items()))}
classification = [{'multiplicity': len(members), **comp_data(rep)} for rep, members in classes]
classification.sort(key=lambda x: (x['order'], x['edges']))
expected = [
    {'multiplicity': 10, 'order': 1, 'edges': 0, 'degrees': {0: 1}},
    {'multiplicity': 20, 'order': 5, 'edges': 5, 'degrees': {1: 2, 2: 1, 3: 2}},
    {'multiplicity': 10, 'order': 7, 'edges': 9, 'degrees': {1: 1, 2: 2, 3: 3, 4: 1}},
    {'multiplicity': 2, 'order': 10, 'edges': 15, 'degrees': {2: 5, 4: 5}},
]
assert classification == expected, (classification, expected)
assert sum(len(nbrs) for nbrs in adj)//2 == 220
assert len(components) == 42
assert collections.Counter(map(len, adj)) == {0: 10, 1: 50, 2: 50, 3: 70, 4: 20}

# The doubled-edge pattern of each four-cover must itself be a perfect matching.
repeat_counts = collections.Counter()
for c in covers:
    pattern = 0
    for j in range(len(edges)):
        mult = sum(bool(matchings[m] & (1 << j)) for m in c)
        assert mult in (1, 2)
        if mult == 2:
            pattern |= (1 << j)
    assert pattern in matchings
    repeat_counts[pattern] += 1
assert collections.Counter(repeat_counts.values()) == {5: 10, 6: 10, 7: 10, 10: 2}

summary = {
    'graph_vertices': 20, 'graph_edges': 30, 'perfect_matchings': len(matchings),
    'minimum_cover_size': 4, 'minimum_covers': len(covers),
    'exchange_edges': sum(map(len, adj))//2, 'exchange_components': len(components),
    'degree_distribution': dict(sorted(collections.Counter(map(len, adj)).items())),
    'component_isomorphism_classes': classification,
    'doubled_matching_extension_distribution': dict(sorted(collections.Counter(repeat_counts.values()).items()))
}
if '--certificate' in sys.argv:
    cert = {
        'graph_edges_zero_based': [[int(a), int(b)] for a, b in edges],
        'perfect_matching_bitmasks': [int(x) for x in matchings],
        'minimum_cover_matching_indices': [list(x) for x in covers],
        'exchange_edges_cover_indices': [[i, j] for i, ns in enumerate(adj) for j in sorted(ns) if i < j],
        'components_cover_indices': [list(c) for c in components],
        'summary': summary
    }
    print(json.dumps(cert, sort_keys=True, separators=(',', ':')))
else:
    print(json.dumps(summary, sort_keys=True, separators=(',', ':')))
