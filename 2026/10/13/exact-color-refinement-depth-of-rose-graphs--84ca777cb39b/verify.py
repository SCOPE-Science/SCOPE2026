#!/usr/bin/env python3
from collections import defaultdict
import itertools

def rose(lengths):
    adj = [set()]
    petals = []
    for L in lengths:
        verts = list(range(len(adj), len(adj) + L - 1))
        adj.extend(set() for _ in verts)
        cyc = [0] + verts + [0]
        for u, v in zip(cyc, cyc[1:]):
            adj[u].add(v); adj[v].add(u)
        petals.append(verts)
    return adj, petals

def partition(colors):
    cells = defaultdict(set)
    for v, c in enumerate(colors):
        cells[c].add(v)
    return frozenset(frozenset(s) for s in cells.values())

def stable_partition_and_depth(adj):
    colors = [0] * len(adj)
    old = partition(colors)
    for r in range(len(adj) + 5):
        sig = [(colors[v], tuple(sorted(colors[w] for w in adj[v])))
               for v in range(len(adj))]
        names = {}
        new = [names.setdefault(s, len(names)) for s in sig]
        newpart = partition(new)
        if newpart == old:
            return r, old
        colors, old = new, newpart
    raise RuntimeError("no stabilization")

def formula(lengths):
    distinct = sorted(set(lengths))
    if len(distinct) == 1:
        return distinct[-1] // 2
    return max(distinct[-1] // 2, distinct[-2])

def orbit_partition(lengths, petals):
    cells = [{0}]
    for L in sorted(set(lengths)):
        indices = [j for j, x in enumerate(lengths) if x == L]
        for d in range(1, L // 2 + 1):
            cell = set()
            for j in indices:
                verts = petals[j]
                for pos, v in enumerate(verts, start=1):
                    if min(pos, L - pos) == d:
                        cell.add(v)
            if cell:
                cells.append(cell)
    return frozenset(frozenset(c) for c in cells)

depth_checks = orbit_checks = 0
for t in range(2, 6):
    for lengths in itertools.combinations_with_replacement(range(3, 13), t):
        adj, petals = rose(lengths)
        depth, stable = stable_partition_and_depth(adj)
        assert depth == formula(lengths), (lengths, depth, formula(lengths))
        assert stable == orbit_partition(lengths, petals), lengths
        depth_checks += 1
        orbit_checks += 1

print(f"VERIFY_OK depth_checks={depth_checks} orbit_checks={orbit_checks} petals=2..5 lengths=3..12")
