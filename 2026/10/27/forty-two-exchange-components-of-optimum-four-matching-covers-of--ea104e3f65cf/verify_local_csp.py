#!/usr/bin/env python3
"""Independent four-colour local-constraint enumeration of flower-snark covers."""
from itertools import combinations
from collections import Counter, defaultdict
import json

n = 5
V = [(i, t) for i in range(n) for t in 'WXYZ']
E = []
def edge(a, b):
    E.append((a, b))
for i in range(n):
    for t in 'XYZ':
        edge((i, 'W'), (i, t))
for i in range(n):
    edge((i, 'X'), ((i + 1) % n, 'X'))
long_cycle = [(i, 'Y') for i in range(n)] + [(i, 'Z') for i in range(n)]
for i in range(2*n):
    edge(long_cycle[i], long_cycle[(i + 1) % (2*n)])
assert len(E) == len(set(frozenset(x) for x in E)) == 30
incident = {v: [] for v in V}
for j, (u, v) in enumerate(E):
    incident[u].append(j)
    incident[v].append(j)
assert all(len(x) == 3 for x in incident.values())
local = {}
for v in V:
    cols = sorted(incident[v])
    choices = []
    for doubled in cols:
        others = [e for e in cols if e != doubled]
        for pair in combinations((1, 2, 4, 8), 2):
            doublemask = pair[0] | pair[1]
            remaining = [c for c in (1, 2, 4, 8) if c not in pair]
            for x, y in (remaining, remaining[::-1]):
                choices.append(((doubled, doublemask), (others[0], x), (others[1], y)))
    assert len(choices) == 36
    local[v] = choices

edge_colours = [0] * len(E)
visited_vertices = set()
coverings = set()
leaves = 0
nodes = 0

def rec():
    global leaves, nodes
    nodes += 1
    if len(visited_vertices) == len(V):
        leaves += 1
        matching = tuple(sorted(sum((1 << i) for i, mask in enumerate(edge_colours) if mask & c) for c in (1, 2, 4, 8)))
        assert all(m.bit_count() == 10 for m in matching)
        assert len(set(matching)) == 4
        assert all(sum(bool(m >> j & 1) for m in matching) >= 1 for j in range(30))
        coverings.add(matching)
        return
    # An incident edge already assigned constrains a frontier vertex.
    available = [v for v in V if v not in visited_vertices]
    pick = max(available, key=lambda v: (sum(edge_colours[e] != 0 for e in incident[v]), -V.index(v)))
    assigned = {e: edge_colours[e] for e in incident[pick] if edge_colours[e]}
    visited_vertices.add(pick)
    for state in local[pick]:
        if any(e in assigned and assigned[e] != m for e, m in state):
            continue
        fresh = []
        for e, m in state:
            if not edge_colours[e]:
                edge_colours[e] = m
                fresh.append(e)
        rec()
        for e in fresh:
            edge_colours[e] = 0
    visited_vertices.remove(pick)

# Fix the arbitrary permutation of four colours at the root, retaining only
# interchange of the two colours sharing its doubled edge.
root = V[0]
r0 = sorted(incident[root])
visited_vertices.add(root)
for doubled in r0:
    others = [e for e in r0 if e != doubled]
    edge_colours[doubled] = 3
    edge_colours[others[0]] = 4
    edge_colours[others[1]] = 8
    rec()
    for e in r0:
        edge_colours[e] = 0
visited_vertices.remove(root)
assert leaves == 400, leaves
assert len(coverings) == 200

# Define the exchange relation without enumerating perfect matchings separately.
covers = sorted(coverings)
triples = defaultdict(list)
for i, C in enumerate(covers):
    for triple in combinations(C, 3):
        triples[triple].append(i)
adj = [set() for _ in covers]
for group in triples.values():
    for i, j in combinations(group, 2):
        adj[i].add(j)
        adj[j].add(i)
components = []
remaining = set(range(len(covers)))
while remaining:
    seed = remaining.pop()
    stack = [seed]
    component = {seed}
    while stack:
        x = stack.pop()
        for y in adj[x] & remaining:
            remaining.remove(y)
            component.add(y)
            stack.append(y)
    components.append(component)

by_size_edges_degree = Counter()
for comp in components:
    degrees = tuple(sorted(Counter(len(adj[i]) for i in comp).items()))
    by_size_edges_degree[(len(comp), sum(len(adj[i]) for i in comp)//2, degrees)] += 1
expected = {
    (1, 0, ((0, 1),)): 10,
    (5, 5, ((1, 2), (2, 1), (3, 2))): 20,
    (7, 9, ((1, 1), (2, 2), (3, 3), (4, 1))): 10,
    (10, 15, ((2, 5), (4, 5))): 2,
}
assert by_size_edges_degree == expected
assert sum(len(x) for x in adj)//2 == 220
assert Counter(map(len, adj)) == {0: 10, 1: 50, 2: 50, 3: 70, 4: 20}
output = {
    'graph_vertices': len(V), 'graph_edges': len(E), 'minimum_cover_size': 4,
    'minimum_covers': len(covers), 'root_canonical_colourings': leaves,
    'exchange_edges': sum(map(len,adj))//2, 'exchange_components': len(components),
    'component_profiles': [{'size': k[0], 'edges': k[1], 'degrees': dict(k[2]), 'multiplicity': v}
                           for k,v in sorted(by_size_edges_degree.items())],
    'degree_distribution': dict(sorted(Counter(map(len, adj)).items())),
    'search_nodes': nodes,
}
print(json.dumps(output, sort_keys=True, separators=(',', ':')))
