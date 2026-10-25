#!/usr/bin/env python3
"""Exact rational homology-character checks for the 32-vertex categorical product graph.

Usage: python verify_character.py
Only the standard library and the adjacent character_table.json are required.
"""
import itertools
import json
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

DATA = json.loads(Path(__file__).with_name('character_table.json').read_text(encoding='utf-8'))
n = 4
n_cells = n * n
n_vertices = 2 * n_cells
cellmask = (1 << n_cells) - 1
vertices = [(a, i, j) for a in range(2) for i in range(n) for j in range(n)]
vertex_index = {v: i for i, v in enumerate(vertices)}
neighbor = [0] * n_vertices
for u, (a, i, j) in enumerate(vertices):
    for ii in range(n):
        for jj in range(n):
            if i != ii and j != jj:
                neighbor[u] |= 1 << vertex_index[(1 - a, ii, jj)]

def act(a, b, layer, exchange):
    return tuple(vertex_index[(t ^ layer, a[j], b[i])] if exchange
                 else vertex_index[(t ^ layer, a[i], b[j])]
                 for t, i, j in vertices)

def cycle_type(p):
    seen = set()
    sizes = []
    for i in range(n):
        if i in seen:
            continue
        j = i
        size = 0
        while j not in seen:
            seen.add(j)
            size += 1
            j = p[j]
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))

def product(a, b):
    return tuple(a[b[i]] for i in range(n))

def trace_orbit_graph(g):
    """Independence polynomial at -1 on the graph of admissible vertex orbits."""
    unvisited = set(range(n_vertices))
    cycles = []
    orbit_id = [0] * n_vertices
    while unvisited:
        start = min(unvisited)
        c = []
        j = start
        while j in unvisited:
            unvisited.remove(j)
            c.append(j)
            j = g[j]
        assert j == start
        k = len(cycles)
        cycles.append(c)
        for j in c:
            orbit_id[j] = k
    conflict = [0] * len(cycles)
    loopmask = 0
    for k, c in enumerate(cycles):
        for i in c:
            neighbors = neighbor[i]
            while neighbors:
                bit = neighbors & -neighbors
                neighbors -= bit
                j = bit.bit_length() - 1
                h = orbit_id[j]
                if k == h:
                    loopmask |= 1 << k
                else:
                    conflict[k] |= 1 << h
    @lru_cache(None)
    def evaluate(mask):
        if not mask:
            return 1
        i = max((k for k in range(len(cycles)) if mask >> k & 1),
                key=lambda k: (conflict[k] & mask).bit_count())
        removed = mask & ~(1 << i)
        return evaluate(removed) - evaluate(removed & ~conflict[i])
    return evaluate(((1 << len(cycles)) - 1) & ~loopmask)

def exhaustive_faces():
    """Independent enumeration by two-layer compatibility, not orbit-graph recursion."""
    compatible = []
    for i in range(n):
        for j in range(n):
            allowed = 0
            for ii in range(n):
                for jj in range(n):
                    if i == ii or j == jj:
                        allowed |= 1 << (n * ii + jj)
            compatible.append(allowed)
    allowed = [cellmask] * (1 << n_cells)
    for A in range(1, 1 << n_cells):
        low = A & -A
        allowed[A] = allowed[A ^ low] & compatible[low.bit_length() - 1]
    faces = []
    for A in range(1 << n_cells):
        B = allowed[A]
        while True:
            faces.append(A | (B << n_cells))
            if B == 0:
                break
            B = (B - 1) & allowed[A]
    return faces

def trace_by_faces(g, faces):
    """Count invariant faces and their signed oriented-simplex contributions."""
    value = 0
    for F in faces:
        transformed = 0
        remaining = F
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            transformed |= 1 << g[bit.bit_length() - 1]
        if transformed != F:
            continue
        remaining = F
        orbits = 0
        while remaining:
            j = (remaining & -remaining).bit_length() - 1
            orbits += 1
            while remaining >> j & 1:
                remaining ^= 1 << j
                j = g[j]
        value += (-1) ** orbits
    return value

permutations = list(itertools.permutations(range(n)))
conjugacy = defaultdict(list)
representatives = {}
for a, b, layer, exchange in itertools.product(permutations, permutations, range(2), range(2)):
    if exchange:
        label = ('S', cycle_type(product(a, b)))
    else:
        label = ('U',) + tuple(sorted((cycle_type(a), cycle_type(b))))
    key = (layer, label)
    g = act(a, b, layer, exchange)
    assert len(set(g)) == n_vertices
    for v in range(n_vertices):
        transformed_neighbors = 0
        mask = neighbor[v]
        while mask:
            bit = mask & -mask
            mask -= bit
            transformed_neighbors |= 1 << g[bit.bit_length() - 1]
        assert transformed_neighbors == neighbor[g[v]]
    value = trace_orbit_graph(g)
    conjugacy[key].append(value)
    representatives.setdefault(key, (g, value))
assert len(conjugacy) == 40
assert sum(map(len, conjugacy.values())) == 2304
assert all(len(set(v)) == 1 for v in conjugacy.values())
actual_rows = {}
for key, values in conjugacy.items():
    layer, label = key
    description = (layer, 'swap' if label[0] == 'S' else 'unswapped',
                   tuple(label[1]), tuple(label[2]) if label[0] == 'U' else None)
    actual_rows[description] = (len(values), values[0])
expected_rows = {
    (r['layer'], r['type'], tuple(r['lambda1']), tuple(r['lambda2']) if r['lambda2'] is not None else None):
        (r['count'], r['trace']) for r in DATA['classes']
}
assert actual_rows == expected_rows
assert DATA['group_order'] == 2304 and DATA['dimension'] == 63
assert conjugacy[(0, ('U', (1, 1, 1, 1), (1, 1, 1, 1)))][0] == 63
assert sum(sum(v) for v in conjugacy.values()) == 0
I = tuple(range(n))
assert trace_orbit_graph(act(I, I, 1, 0)) == DATA['layer_flip_trace'] == 9

faces = exhaustive_faces()
assert len(faces) == DATA['total_independent_faces'] == 136063
for key, (g, value) in representatives.items():
    assert trace_by_faces(g, faces) == value, key

# Irreducibles of S_4 wr C_2, inflated or twisted by the layer flip.
cycle_types = [(1,1,1,1), (2,1,1), (2,2), (3,1), (4,)]
partitions = ['4', '31', '22', '211', '1111']
s4 = {'4': [1,1,1,1,1], '31': [3,1,-1,0,-1],
      '22': [2,0,2,-1,0], '211': [3,-1,-1,0,1],
      '1111': [1,-1,1,1,-1]}
dimensions = {'4':1, '31':3, '22':2, '211':3, '1111':1}
def character_value(row, lam, mu, extension, layer_sign):
    p = tuple(row['lambda1'])
    q = tuple(row['lambda2']) if row['lambda2'] is not None else None
    sign = layer_sign if row['layer'] else 1
    if q is None:
        return sign * extension * s4[lam][cycle_types.index(p)] if lam == mu else 0
    val = s4[lam][cycle_types.index(p)] * s4[mu][cycle_types.index(q)]
    if lam != mu:
        val += s4[mu][cycle_types.index(p)] * s4[lam][cycle_types.index(q)]
    return sign * val
actual_components = []
for lam, mu in itertools.combinations_with_replacement(partitions, 2):
    for extension in ([1, -1] if lam == mu else [1]):
        for layer_sign in (1, -1):
            numerator = sum(r['count'] * r['trace'] *
                            character_value(r, lam, mu, extension, layer_sign)
                            for r in DATA['classes'])
            assert numerator % 2304 == 0
            multiplicity = numerator // 2304
            assert multiplicity >= 0
            if multiplicity:
                actual_components.append(dict(lambda1=lam, lambda2=mu,
                                              ext=extension, layer=layer_sign,
                                              mult=multiplicity,
                                              dimension=dimensions[lam] * dimensions[mu] *
                                              (1 if lam == mu else 2)))
assert actual_components == DATA['irreducibles']
assert len(actual_components) == 8
assert sum(c['mult'] * c['dimension'] for c in actual_components) == 63
assert sum(c['mult'] * c['dimension'] for c in actual_components if c['layer'] == 1) == 36
assert sum(c['mult'] * c['dimension'] for c in actual_components if c['layer'] == -1) == 27
assert DATA['invariant_dimension'] == 0
print('TRIPLE_COMPLETE_GRAPH_INDEPENDENCE_EQUIVARIANT_CHARACTER_VERIFIED',
      'faces=', len(faces), 'elements=', 2304, 'classes=', 40, 'constituents=', 8)
