#!/usr/bin/env python3
"""Verify the complete cyclic-cut certificate and its McGee-graph symmetry orbits.
Requires Python 3.10+ and networkx >=3.0. Run: python verify_orbits.py.
With --write, regenerate cut_orbits.csv in the current directory.
"""
import csv
import sys
from collections import Counter
from pathlib import Path
import networkx as nx

N = 24
FULL = (1 << N) - 1
G = nx.Graph()
G.add_nodes_from(range(N))
shifts = (-12, 7, -7)
for i in range(N):
    G.add_edge(i, (i + 1) % N)
    G.add_edge(i, (i + shifts[i % 3]) % N)
assert G.number_of_edges() == 36
assert all(d == 3 for _, d in G.degree())


def mask_set(mask):
    return {i for i in range(N) if mask >> i & 1}


def induced(mask):
    return G.subgraph(mask_set(mask))


def canonical(mask):
    other = FULL ^ mask
    a, b = mask.bit_count(), other.bit_count()
    return mask if a < b or (a == b and mask < other) else other


def image(mask, permutation):
    return sum(1 << permutation[i] for i in mask_set(mask))


def suppressed_paths(H):
    """Replace every maximal internal-degree-two path with a weighted edge."""
    hubs = {v for v, d in H.degree() if d != 2}
    out = []
    seen = set()
    for v in sorted(hubs):
        for u in H.neighbors(v):
            a = frozenset((v, u))
            if a in seen:
                continue
            seen.add(a)
            prev, cur, length = v, u, 1
            while H.degree(cur) == 2:
                nxt = next(x for x in H[cur] if x != prev)
                seen.add(frozenset((cur, nxt)))
                prev, cur = cur, nxt
                length += 1
            out.append((v, cur, length))
    assert sum(length for _, _, length in out) == H.number_of_edges()
    return out


def twelve_type(H):
    assert H.number_of_nodes() == 12 and H.number_of_edges() == 14
    degrees = Counter(dict(H.degree()).values())
    assert degrees == {2: 8, 3: 4}
    paths = suppressed_paths(H)
    hubs = {v for v, d in H.degree() if d == 3}
    pairs = {frozenset((a, b)) for a, b, _ in paths}
    assert len(paths) == len(pairs) == 6
    assert pairs == {frozenset(t) for t in __import__('itertools').combinations(hubs, 2)}
    ls = sorted(length for _, _, length in paths)
    if ls == [1, 1, 3, 3, 3, 3]:
        matched = [(u, v) for u, v, length in paths if length == 1]
        assert len({x for e in matched for x in e}) == 4
        return 'A'
    if ls == [2, 2, 2, 2, 3, 3]:
        matched = [(u, v) for u, v, length in paths if length == 3]
        assert len({x for e in matched for x in e}) == 4
        return 'B'
    raise AssertionError('unexpected subdivided K4')


def shape(mask):
    H = induced(mask)
    v, e = len(H), H.number_of_edges()
    assert nx.is_connected(H)
    degrees = Counter(dict(H.degree()).values())
    if v == 7:
        assert e == 7 and degrees == {2: 7}
        return 'C7', ''
    if v == 8:
        assert e == 8
        if degrees == {2: 8}:
            return 'C8', ''
        assert degrees == {1: 1, 2: 6, 3: 1}
        leaf = next(x for x, d in H.degree() if d == 1)
        T = H.copy();T.remove_node(leaf)
        assert T.number_of_edges() == 7 and all(d == 2 for _, d in T.degree())
        return 'C7+leaf', ''
    if v == 10:
        assert e == 11 and degrees == {2: 8, 3: 2}
        paths = suppressed_paths(H)
        assert len(paths) == 3 and sorted(z for _, _, z in paths) == [3, 4, 4]
        return 'theta(3,4,4)', ''
    if v == 12:
        assert e == 14
        return 'K4-subdivisions', ''.join(sorted([twelve_type(H), twelve_type(induced(FULL ^ mask))]))
    raise AssertionError((v, e))


rows = list(csv.DictReader(Path('cut_masks.csv').open(newline='')))
allcuts = {}
for row in rows:
    m = int(row['mask'])
    assert m == canonical(m) and m not in allcuts
    assert int(row['cut']) in (7, 8)
    assert int(row['small_size']) == m.bit_count()
    assert int(row['small_edges']) == induced(m).number_of_edges()
    assert int(row['components_small']) == int(row['components_large']) == 1
    assert nx.is_connected(induced(FULL ^ m))
    typ, balanced = shape(m)
    allcuts[m] = (int(row['cut']), typ, balanced)

assert Counter(allcuts.values()) == Counter({
    (7, 'C7', ''): 32,
    (8, 'C8', ''): 34,
    (8, 'C7+leaf', ''): 224,
    (8, 'theta(3,4,4)', ''): 80,
    (8, 'K4-subdivisions', 'AA'): 6,
    (8, 'K4-subdivisions', 'AB'): 16,
    (8, 'K4-subdivisions', 'BB'): 2,
})

# Separately enumerate the cycles of length seven and eight.
cycles = set()
for start in range(N):
    def dfs(path, seen):
        for nxt in G[path[-1]]:
            if nxt == start and 7 <= len(path) <= 8:
                seq = tuple(path)
                cycles.add(min(seq, (seq[0],) + tuple(reversed(seq[1:]))))
            elif nxt > start and nxt not in seen and len(path) < 8:
                dfs(path + [nxt], seen | {nxt})
    dfs([start], {start})
assert Counter(map(len, cycles)) == {7: 32, 8: 34}

permutations = list(nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter())
assert len(permutations) == 32

remaining = set(allcuts)
orbits = []
while remaining:
    rep = min(remaining)
    orbit = {canonical(image(rep, p)) for p in permutations}
    assert orbit <= remaining and len(orbit) in (2, 4, 8, 16, 32)
    assert len({allcuts[m] for m in orbit}) == 1
    remaining -= orbit
    c, typ, balanced = allcuts[rep]
    orbits.append({
        'mask': rep, 'cut': c, 'small_size': rep.bit_count(),
        'topology': typ, 'balanced_K4_type': balanced,
        'orbit_size': len(orbit), 'stabilizer_size': 32 // len(orbit),
    })
assert len(orbits) == 23
assert Counter((o['cut'], o['topology']) for o in orbits) == {
    (7, 'C7'): 2, (8, 'C8'): 4, (8, 'C7+leaf'): 8,
    (8, 'theta(3,4,4)'): 5, (8, 'K4-subdivisions'): 4,
}
assert sum(o['orbit_size'] for o in orbits if o['cut'] == 8) == 362

fieldnames = ['mask', 'cut', 'small_size', 'topology', 'balanced_K4_type', 'orbit_size', 'stabilizer_size']
with Path('cut_orbits.csv').open('w' if '--write' in sys.argv else 'r', newline='') as f:
    if '--write' in sys.argv:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader();writer.writerows(orbits)
    else:
        stored = list(csv.DictReader(f))
        assert stored == [{k: str(r[k]) for k in fieldnames} for r in orbits]
print('VERIFY_ORBITS_OK graph=McGee_24_36 girth_cycles=7:32,8:34 automorphisms=32')
print('VERIFY_ORBITS_OK cut7=32,2_orbits cut8=362,21_orbits')
print('VERIFY_ORBITS_OK cut8_types=C8:34,C7+leaf:224,theta:80,balanced_K4:AA:6+AB:16+BB:2')
