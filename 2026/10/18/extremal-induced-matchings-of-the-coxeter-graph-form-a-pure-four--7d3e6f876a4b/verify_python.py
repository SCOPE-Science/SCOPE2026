#!/usr/bin/env python3
"""Exhaustive induced-matching and packing census for the Fano-triangle graph."""
import itertools
import json
import pathlib

POINTS = range(7)
FANO = {frozenset(((i) % 7, (i + 1) % 7, (i + 3) % 7)) for i in POINTS}
VERTICES = tuple(t for t in itertools.combinations(POINTS, 3) if frozenset(t) not in FANO)
EDGES = tuple((i, j) for i in range(len(VERTICES)) for j in range(i + 1, len(VERTICES))
              if not set(VERTICES[i]).intersection(VERTICES[j]))
assert len(VERTICES) == 28 and len(EDGES) == 42
ADJ = {(i, j) for i, j in EDGES}

def adjacent(i, j):
    return (min(i, j), max(i, j)) in ADJ and i != j

def compatible(e, f):
    a, b = e
    c, d = f
    return len({a, b, c, d}) == 4 and all(not adjacent(x, y) for x in (a, b) for y in (c, d))

# Ascending-order clique recursion counts each induced matching once.
NEXT = [sum(1 << j for j in range(i + 1, 42) if compatible(EDGES[i], EDGES[j])) for i in range(42)]
hist = [0] * 43
maximum = []
def enumerate_matchings(candidates, chosen):
    hist[len(chosen)] += 1
    if len(chosen) == 7:
        maximum.append(sum(1 << j for j in chosen))
    while candidates:
        bit = candidates & -candidates
        candidates ^= bit
        j = bit.bit_length() - 1
        enumerate_matchings(candidates & NEXT[j], chosen + (j,))

enumerate_matchings((1 << 42) - 1, ())
maximum.sort()
assert hist[:9] == [1, 42, 609, 3808, 10374, 11172, 4242, 84, 0]
assert all(x == 0 for x in hist[8:]) and len(maximum) == 84

# Pairwise disjoint packings, counted in strictly ascending maximum-set index.
disjoint_later = [sum(1 << j for j in range(i + 1, 84)
                      if maximum[i] & maximum[j] == 0) for i in range(84)]
pack_hist = [0] * 85

def enumerate_packings(candidates, depth):
    pack_hist[depth] += 1
    while candidates:
        bit = candidates & -candidates
        candidates ^= bit
        j = bit.bit_length() - 1
        enumerate_packings(candidates & disjoint_later[j], depth + 1)

enumerate_packings((1 << 84) - 1, 0)
assert pack_hist[:6] == [1, 84, 1092, 3528, 2478, 0]
assert all(x == 0 for x in pack_hist[5:])
# Every disjoint subfamily with fewer than four members extends to a larger one.
maximal_smaller = [0, 0, 0, 0]
degree_spectrum = {}
for i, item in enumerate(maximum):
    degree = sum(item & other == 0 for j, other in enumerate(maximum) if j != i)
    degree_spectrum[degree] = degree_spectrum.get(degree, 0) + 1
assert degree_spectrum == {26: 84}

def inspect_extensions(start, chosen):
    if chosen and len(chosen) < 4:
        if not any(all(maximum[j] & maximum[i] == 0 for i in chosen)
                   for j in range(84) if j not in chosen):
            maximal_smaller[len(chosen)] += 1
    if len(chosen) >= 3:
        return
    for j in range(start, 84):
        if all(maximum[j] & maximum[i] == 0 for i in chosen):
            inspect_extensions(j + 1, chosen + (j,))
inspect_extensions(0, ())
assert maximal_smaller == [0, 0, 0, 0]

# Explicit seven-color strong edge coloring in lexicographic edge order.
COLORS = (
    (0, 4, 19, 28, 33, 39),
    (1, 20, 22, 32, 35, 41),
    (3, 11, 14, 16, 26, 27, 34),
    (8, 13, 29, 30, 37, 38),
    (9, 17, 23, 25, 36),
    (2, 7, 10, 15, 18, 21),
    (5, 6, 12, 24, 31, 40),
)
assert sorted(itertools.chain.from_iterable(COLORS)) == list(range(42))
assert all(compatible(EDGES[a], EDGES[b]) for group in COLORS
           for a, b in itertools.combinations(group, 2))

# Enumerate the 168 labelled Fano-plane collineations and the orbit on maximum matchings.
vindex = {t: i for i, t in enumerate(VERTICES)}
eindex = {e: i for i, e in enumerate(EDGES)}
collineations = 0
orbit = set()
for permutation in itertools.permutations(POINTS):
    transformed = {frozenset(permutation[k] for k in line) for line in FANO}
    if transformed != FANO:
        continue
    collineations += 1
    new_vertices = tuple(vindex[tuple(sorted(permutation[k] for k in triple))] for triple in VERTICES)
    edge_map = tuple(eindex[tuple(sorted((new_vertices[a], new_vertices[b])))] for a, b in EDGES)
    s = maximum[0]
    orbit.add(sum(1 << edge_map[k] for k in range(42) if (s >> k) & 1))
assert collineations == 168 and orbit == set(maximum)

certificate = {
    'model': 'Fano nonline triples; disjointness edges; zero-based lex ordering',
    'vertices': [list(t) for t in VERTICES],
    'edges': [list(e) for e in EDGES],
    'induced_matching_counts_size_0_to_8': hist[:9],
    'maximum_induced_matching_masks_hex': [f'{m:011x}' for m in maximum],
    'disjoint_maximum_family_counts_size_0_to_5': pack_hist[:6],
    'maximal_disjoint_packings_of_size_below_4': maximal_smaller,
    'disjointness_graph_degree_spectrum': degree_spectrum,
    'fano_collineations': collineations,
    'orbit_of_first_maximum_size': len(orbit),
    'seven_strong_color_classes_edge_indices': [list(g) for g in COLORS],
}
output = pathlib.Path(__file__).with_name('certificate.json')
output.write_text(json.dumps(certificate, sort_keys=True, indent=2) + '\n', encoding='utf-8')
print('VERTICES=28 EDGES=42')
print('INDUCED_MATCHING_COUNTS=' + ','.join(map(str, hist[:9])))
print('MAXIMUM_SIZE=7 MAXIMUM_COUNT=84')
print('PAIRWISE_DISJOINT_PACK_COUNTS=' + ','.join(map(str, pack_hist[:6])))
print('MAX_DISJOINT_PACK=4')
print('FANO_COLLINEATIONS=168 ORBIT=84')
print('DISJOINTNESS_GRAPH=84_VERTICES_DEGREE_26_PURE_FACETS_2478')
print('SEVEN_COLOR_WITNESS=VALID')
