"""Exact cellular verification for the Heawood two-point configuration space.

Run: python verify_heawood.py
Dependencies: networkx, sympy. All inputs are constructed within this file.
"""
from collections import Counter
from itertools import combinations

import networkx as nx
from sympy import Matrix, eye, zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# Labels 0,...,13 realize the LCF word [5,-5]^7.
N = 14
G = nx.Graph()
G.add_nodes_from(range(N))
G.add_edges_from((i, (i + 1) % N) for i in range(N))
G.add_edges_from((i, (i + 5) % N) for i in range(0, N, 2))
V = list(range(N))
E = sorted(tuple(sorted(e)) for e in G.edges())
assert len(E) == 21 and all(G.degree(v) == 3 for v in V)
assert nx.is_isomorphic(G, nx.heawood_graph())

# Fano point/line incidence gives a separately defined model of this graph.
F = nx.Graph()
F.add_nodes_from(range(14))
for a in range(1, 8):
    for b in range(1, 8):
        if (a & b).bit_count() % 2 == 0:
            F.add_edge(a - 1, 7 + b - 1)
assert nx.is_isomorphic(F, G)

# The unordered deleted cubical product, oriented using ascending edges.
C0 = list(combinations(V, 2))
C1 = [(v, e) for v in V for e, (a, b) in enumerate(E) if v not in (a, b)]
C2 = [(i, j) for i, j in combinations(range(len(E)), 2)
      if not (set(E[i]) & set(E[j]))]
I0 = {x: k for k, x in enumerate(C0)}
I1 = {x: k for k, x in enumerate(C1)}
I2 = {x: k for k, x in enumerate(C2)}
D1 = zeros(len(C0), len(C1))
D2 = zeros(len(C1), len(C2))
for j, (v, e) in enumerate(C1):
    a, b = E[e]
    D1[I0[tuple(sorted((v, b)))], j] += 1
    D1[I0[tuple(sorted((v, a)))], j] -= 1
for j, (i, k) in enumerate(C2):
    a, b = E[i]
    c, d = E[k]
    for cell, sign in [((b, k), 1), ((a, k), -1),
                       ((d, i), -1), ((c, i), 1)]:
        D2[I1[cell], j] += sign
assert (len(C0), len(C1), len(C2)) == (91, 252, 168)
assert D1 * D2 == zeros(D1.rows, D2.cols)

# Canonical cycles by vertex word, modulo rotation and reversal.
def canonical(path):
    path = tuple(path)
    orientations = [path, path[::-1]]
    return min(tuple(p[i:] + p[:i]) for p in orientations for i in range(len(p)))

cycles = set()
def dfs(path, visited):
    first, last = path[0], path[-1]
    if len(path) >= 3 and G.has_edge(last, first):
        cycles.add(canonical(path))
    for w in G.neighbors(last):
        if w >= first and w not in visited:
            dfs(path + [w], visited | {w})
for first in V:
    dfs([first], {first})
hexagons = sorted(c for c in cycles if len(c) == 6)
pairs = [(a, b) for a, b in combinations(hexagons, 2) if not set(a) & set(b)]
assert len(hexagons) == 28 and len(pairs) == 42

edge_id = {e: i for i, e in enumerate(E)}
def cycle_edge_chain(c):
    ans = {}
    for a, b in zip(c, c[1:] + c[:1]):
        edge = tuple(sorted((a, b)))
        ans[edge_id[edge]] = 1 if (a, b) == edge else -1
    return ans
T = zeros(len(C2), len(pairs))
for j, (a, b) in enumerate(pairs):
    for i, si in cycle_edge_chain(a).items():
        for k, sk in cycle_edge_chain(b).items():
            T[I2[tuple(sorted((i, k)))], j] += (1 if i < k else -1)*si*sk
assert D2 * T == zeros(D2.rows, T.cols)

# A fixed, fully explicit integral certificate (lexicographic ordering above).
ROWS = [0, 2, 4, 7, 10, 16, 18, 20, 23, 48, 50, 53, 76, 82]
COLS = [0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 24]
B = T.extract(ROWS, COLS)
assert B.det() == -1
basis = T[:, COLS]
B_inv = B.inv()

# Fast independent finite-field rank certificate; exact Smith invariant factors
# determine the integral first-homology torsion, not just mod-p dimensions.
def rank_mod_p(matrix, p):
    a = [[int(matrix[i, j]) % p for j in range(matrix.cols)]
         for i in range(matrix.rows)]
    rank = 0
    for col in range(matrix.cols):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x*inv) % p for x in a[rank]]
        for i in range(rank + 1, len(a)):
            coeff = a[i][col]
            if coeff:
                a[i] = [(u - coeff*v) % p for u, v in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank

assert rank_mod_p(D2, 101) == 154
# Because 14 independent columns of T lie in ker D2, rank D2 <= 154.
# Thus integral rank of D2 is exactly 154 and the 14 selected tori
# are an integral basis of its saturated kernel: determinant(B) = -1.
snf = smith_normal_form(D2, domain=ZZ)
factors = Counter(abs(int(snf[i, i])) for i in range(min(snf.shape)) if snf[i, i])
assert factors == Counter({1: 153, 2: 1})
assert rank_mod_p(D1, 101) == 90
# Hexagon cycles span the eight-dimensional graph cycle space, so the
# natural motion/sum map on first rational homology is surjective.
hex_graph_cycles = zeros(len(E), len(hexagons))
for j, cycle in enumerate(hexagons):
    for eid, sign in cycle_edge_chain(cycle).items():
        hex_graph_cycles[eid, j] = sign
assert rank_mod_p(hex_graph_cycles, 101) == 8

# Full graph automorphism enumeration, acting on the *oriented* integral
# cells; verify each translated torus has integral coordinates in basis.
automorphisms = list(nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter())
assert len(automorphisms) == 336
bipart = set(range(0, 14, 2))

def automorphism_order(g):
    image = dict(enumerate(V))
    for n in range(1, 337):
        image = {v: g[image[v]] for v in V}
        if all(image[v] == v for v in V):
            return n
    raise AssertionError('Automorphism order exceeds group order')

def map_two_cell(g, cell):
    i, j = cell
    a, b = E[i]
    c, d = E[j]
    mapped_i = tuple(sorted((g[a], g[b])))
    mapped_j = tuple(sorted((g[c], g[d])))
    ii, jj = edge_id[mapped_i], edge_id[mapped_j]
    s1 = 1 if (g[a], g[b]) == mapped_i else -1
    s2 = 1 if (g[c], g[d]) == mapped_j else -1
    return I2[tuple(sorted((ii, jj)))], s1*s2*(1 if ii < jj else -1)

counts = Counter()
for g in automorphisms:
    transformed = zeros(len(C2), len(COLS))
    for cell_id, cell in enumerate(C2):
        dest, sign = map_two_cell(g, cell)
        for j in range(len(COLS)):
            val = basis[cell_id, j]
            if val:
                transformed[dest, j] += sign*val
    rho = B_inv * transformed[ROWS, :]
    assert basis * rho == transformed
    assert all(x.q == 1 for x in rho)
    keep = 'preserve' if {g[v] for v in bipart} == bipart else 'exchange'
    counts[(keep, automorphism_order(g), int(rho.trace()))] += 1

expected = Counter({
    ('preserve', 1, 14): 1,
    ('preserve', 2, -2): 21,
    ('preserve', 3, -1): 56,
    ('preserve', 4, 2): 42,
    ('preserve', 7, 0): 48,
    ('exchange', 2, -2): 28,
    ('exchange', 6, 1): 56,
    ('exchange', 8, 0): 84,
})
assert counts == expected
assert sum(tr*n for (_, _, tr), n in counts.items()) == 0
print('VERIFY_OK_HEAWOOD_HEXAGON_TORUS_INTEGRAL_BASIS_AND_CHARACTER')
print('GRAPH', len(V), len(E), 'FANO_ISOMORPHIC', True)
print('CUBICAL_CELLS', len(C0), len(C1), len(C2), 'BOUNDARY_SQUARED_ZERO')
print('BOUNDARY2_RANK_MOD101', 154, 'SMITH_FACTORS', tuple(sorted(factors.items())))
print('INTEGRAL_H1_Z8_PLUS_Z2_H2_Z14')
print('HEXAGONS', len(hexagons), 'DISJOINT_PAIRS', len(pairs))
print('TORUS_INTEGRAL_BASIS_COLUMN_INDICES', COLS)
print('TORUS_INTEGRAL_BASIS_ROW_INDICES', ROWS)
print('UNIT_MINOR', int(B.det()))
print('AUTOMORPHISMS', len(automorphisms))
print('FULL_H2_CHARACTER', sorted(counts.items()))
# Independent fixed-cell Lefschetz check, using the graph's H1 character.
for g in automorphisms:
    tr_c0 = sum(tuple(sorted((g[u], g[v]))) == (u, v) for u, v in C0)
    tr_c1 = 0
    for v, eid in C1:
        a, b = E[eid]
        mapped = tuple(sorted((g[a], g[b])))
        if g[v] == v and mapped == E[eid]:
            tr_c1 += 1 if (g[a], g[b]) == mapped else -1
    tr_c2 = sum(sign for eid, cell in enumerate(C2)
                for dest, sign in [map_two_cell(g, cell)] if dest == eid)
    tr_eg = sum((1 if (g[a], g[b]) == E[eid] else -1)
                for eid, (a, b) in enumerate(E) if tuple(sorted((g[a], g[b]))) == (a, b))
    tr_vg = sum(g[v] == v for v in V)
    # graph H1 trace = tr_graph_C1 - tr_graph_C0 + 1.
    h2_pred = tr_c0 - tr_c1 + tr_c2 + tr_eg - tr_vg
    transformed = zeros(len(C2), len(COLS))
    for cell_id, cell in enumerate(C2):
        dest, sign = map_two_cell(g, cell)
        for j in range(len(COLS)):
            if basis[cell_id, j]:
                transformed[dest, j] += sign*basis[cell_id, j]
    assert h2_pred == (B_inv * transformed[ROWS, :]).trace()
print('INDEPENDENT_FIXED_CELL_LEFSCHETZ_CHECK_ALL_AUTOMORPHISMS')
print('GRAPH_HEXAGONS_SPAN_RATIONAL_FIRST_HOMOLOGY')
