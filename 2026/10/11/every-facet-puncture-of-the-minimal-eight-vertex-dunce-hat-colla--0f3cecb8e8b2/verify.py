#!/usr/bin/env python3
import json
from itertools import combinations
from collections import Counter, defaultdict
from pathlib import Path

FACETS = [
    (1,2,4),(1,2,7),(1,2,8),(1,3,4),(1,3,5),(1,3,6),(1,5,6),(1,7,8),
    (2,3,5),(2,3,7),(2,3,8),(2,4,5),(3,4,8),(3,6,7),(4,5,6),(4,6,8),(6,7,8)
]
FACETS = [tuple(sorted(t)) for t in FACETS]
VERTICES = set(range(1,9))
ALL_EDGES = set()
for t in FACETS:
    ALL_EDGES.update(tuple(sorted(e)) for e in combinations(t,2))

assert len(VERTICES) == 8
assert len(ALL_EDGES) == 24
assert len(FACETS) == 17
inc = Counter(e for t in FACETS for e in combinations(t,2))
assert Counter(inc.values()) == Counter({2:21, 3:3})
assert not [e for e,c in inc.items() if c == 1]

data = json.loads(Path(__file__).with_name("collapse_certificate.json").read_text(encoding="utf-8"))
assert [tuple(x) for x in data["facets"]] == FACETS
assert len(data["punctures"]) == 17
seen_deleted = set()
core_hist = Counter()

for entry in data["punctures"]:
    deleted = tuple(entry["deleted_facet"])
    assert deleted in FACETS and deleted not in seen_deleted
    seen_deleted.add(deleted)
    tris = set(FACETS)
    tris.remove(deleted)
    edges = set(ALL_EDGES)
    verts = set(VERTICES)

    for step in entry["steps"]:
        if step["kind"] == "2-1":
            e = tuple(step["free_edge"])
            t = tuple(step["triangle"])
            assert e in edges and t in tris and set(e).issubset(t)
            holders = [q for q in tris if set(e).issubset(q)]
            assert holders == [t] or (len(holders) == 1 and holders[0] == t)
            tris.remove(t)
            edges.remove(e)
        elif step["kind"] == "1-0":
            v = int(step["free_vertex"])
            e = tuple(step["edge"])
            assert not tris
            assert v in verts and e in edges and v in e
            incident = [q for q in edges if v in q]
            assert incident == [e] or (len(incident) == 1 and incident[0] == e)
            verts.remove(v)
            edges.remove(e)
        else:
            raise AssertionError("unknown step")

    assert not tris
    terminal_vertices = set(entry["terminal_cycle_vertices"])
    terminal_edges = {tuple(e) for e in entry["terminal_cycle_edges"]}
    assert verts == terminal_vertices
    assert edges == terminal_edges
    adj = {v:set() for v in verts}
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    assert len(edges) == len(verts) >= 3
    assert all(len(adj[v]) == 2 for v in verts)
    root = min(verts)
    reached = {root}
    stack = [root]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in reached:
                reached.add(w); stack.append(w)
    assert reached == verts
    core_hist[len(verts)] += 1

assert seen_deleted == set(FACETS)
assert core_hist == Counter({3:12,4:5})
print("VERIFY_OK f=8,24,17 full_free_edges=0 punctures=17 all_collapse_to_cycle=yes certificate_core_lengths=3:12,4:5")
