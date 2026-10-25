"""Exact short-cycle torus-lattice verification for the Nauru graph.

Run: python verify.py. Requires networkx and sympy (see requirements.txt).
All indexing, orientations, matrices and witnesses are built anew from GP(12,5).
"""
from collections import Counter, defaultdict
from itertools import combinations

import networkx as nx
import sympy as sp
from networkx.algorithms.isomorphism import GraphMatcher
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# 0,...,11 are outer vertices; 12,...,23 are inner vertices.
G = nx.Graph()
G.add_nodes_from(range(24))
for i in range(12):
    G.add_edge(i, (i + 1) % 12)
    G.add_edge(i, 12 + i)
    G.add_edge(12 + i, 12 + (i + 5) % 12)
E = sorted(tuple(sorted(edge)) for edge in G.edges())
ei = {edge: j for j, edge in enumerate(E)}
assert len(G) == 24 and len(E) == 36
assert sorted(dict(G.degree()).values()) == [3] * 24
adj = {v: sorted(G[v]) for v in G}

# Every undirected simple cycle exactly once: its least vertex is first,
# all other vertices are greater and the second vertex is less than last.
cycles = []
for root in range(24):
    def visit(path, seen):
        for w in adj[path[-1]]:
            if w == root and len(path) >= 3:
                if path[1] < path[-1]:
                    cycles.append(tuple(path))
            elif w > root and w not in seen:
                visit(path + [w], seen | {w})
    visit([root], {root})
cycle_counts = Counter(map(len, cycles))
assert len(cycles) == 5442
assert cycle_counts == {6: 12, 8: 54, 10: 108, 12: 246,
                        14: 612, 16: 1062, 18: 1296, 20: 1386,
                        22: 648, 24: 18}

# The unordered, closure-disjoint cubical model for two graph particles.
# A 1-cell is (oriented edge, remote vertex), a 2-cell is an unordered
# pair of disjoint edges, oriented as increasing edge indices.
c0 = {pair: k for k, pair in enumerate(combinations(range(24), 2))}
c1 = {(j, w): k for k, (j, w) in enumerate(
    (j, w) for j, edge in enumerate(E) for w in range(24) if w not in edge)}
c2 = {pair: k for k, pair in enumerate(
    (i, j) for i in range(36) for j in range(i + 1, 36)
    if set(E[i]).isdisjoint(E[j]))}
assert (len(c0), len(c1), len(c2)) == (276, 792, 558)
b1 = []
for (j, w) in c1:
    u, v = E[j]
    b1.append({c0[tuple(sorted((v, w)))]: 1,
               c0[tuple(sorted((u, w)))]: -1})
b2 = []
for (i, j) in c2:
    u, v = E[i]
    s, t = E[j]
    column = {c1[(j, v)]: 1, c1[(j, u)]: -1,
              c1[(i, t)]: -1, c1[(i, s)]: 1}
    # Independently check d1*d2 for every 2-cell.
    boundary = defaultdict(int)
    for r, a in column.items():
        for q, d in b1[r].items():
            boundary[q] += a * d
    assert all(d == 0 for d in boundary.values())
    b2.append(column)

# Exact finite-field Gaussian elimination: a nonzero maximal minor over
# F_101 also gives a nonzero integer minor (and a rational rank bound).
def modular_rank(columns, p):
    pivots = {}
    for col in columns:
        if p == 2:
            bits = sum(1 << i for i, x in col.items() if x % 2)
            while bits:
                k = bits.bit_length() - 1
                if k not in pivots:
                    pivots[k] = bits
                    break
                bits ^= pivots[k]
        else:
            row = {i: x % p for i, x in col.items() if x % p}
            while row:
                k, a = max(row), row[max(row)]
                if k not in pivots:
                    inv = pow(a, -1, p)
                    pivots[k] = {i: x * inv % p for i, x in row.items()}
                    break
                for i, x in pivots[k].items():
                    new = (row.get(i, 0) - a * x) % p
                    if new:
                        row[i] = new
                    else:
                        row.pop(i, None)
    return len(pivots)

assert modular_rank(b1, 101) == 275
assert modular_rank(b2, 101) == 504
assert modular_rank(b2, 3) == 504
assert modular_rank(b2, 2) == 503

# A disjoint pair of oriented graph cycles gives an embedded product torus.
def edge_chain(cycle):
    return {ei[tuple(sorted((u, v)))]: 1 if u < v else -1
            for u, v in zip(cycle, cycle[1:] + cycle[:1])}
edge_chains = {c: edge_chain(c) for c in cycles if len(c) <= 8}

def product_torus(c, d):
    chain = defaultdict(int)
    for i, a in edge_chains[c].items():
        for j, b in edge_chains[d].items():
            key = tuple(sorted((i, j)))
            chain[c2[key]] += a * b * (1 if i < j else -1)
    ans = {i: a for i, a in chain.items() if a}
    boundary = defaultdict(int)
    for k, a in ans.items():
        for r, b in b2[k].items():
            boundary[r] += a * b
    assert all(val == 0 for val in boundary.values())
    return ans

families = defaultdict(list)
pairs = defaultdict(list)
for c, d in combinations((c for c in cycles if len(c) <= 8), 2):
    if set(c).isdisjoint(d):
        typ = tuple(sorted((len(c), len(d))))
        pairs[typ].append((c, d))
        families[typ].append(product_torus(c, d))
assert {typ: len(z) for typ, z in families.items()} == {
    (6, 6): 30, (6, 8): 216, (8, 8): 171}
assert modular_rank(families[(6, 6)], 101) == 30
assert modular_rank(families[(6, 8)], 101) == 54
assert modular_rank(families[(8, 8)], 101) == 54
assert modular_rank(families[(6, 8)], 2) == 52
assert modular_rank(families[(8, 8)], 2) == 54

# Deterministic greedy 54 selected octagon/octagon tori and 54 coordinates.
# A unit minor supplies a genuine integral splitting, not a rational basis.
oct_tori = families[(8, 8)]
column_pivots, chosen_columns = {}, []
for j, col in enumerate(oct_tori):
    bits = sum(1 << i for i, val in col.items() if val % 2)
    while bits:
        k = bits.bit_length() - 1
        if k not in column_pivots:
            column_pivots[k] = bits
            chosen_columns.append(j)
            break
        bits ^= column_pivots[k]
    if len(chosen_columns) == 54:
        break
row_pivots, chosen_rows = {}, []
for i in range(len(c2)):
    bits = sum((oct_tori[j].get(i, 0) % 2) << k
               for k, j in enumerate(chosen_columns))
    while bits:
        k = bits.bit_length() - 1
        if k not in row_pivots:
            row_pivots[k] = bits
            chosen_rows.append(i)
            break
        bits ^= row_pivots[k]
    if len(chosen_rows) == 54:
        break
assert len(chosen_columns) == len(chosen_rows) == 54
Q = sp.Matrix([[oct_tori[j].get(i, 0) for j in chosen_columns]
               for i in chosen_rows])
unit_det = int(Q.det(method='domain-ge'))
assert unit_det == -1
Qinv = Q.inv()
assert all(x.q == 1 for x in Qinv)

# We have 54 independent integral cycles, so rank(d2) <= 558-54 = 504.
# Above we exhibited rank(d2 mod101)=504, hence rank(d2 over Q)=504.
# The 54-torus lattice is a direct summand of Z^558 due to its unit minor,
# and therefore equals the whole integer kernel(d2) of the same rank.

def homology_coordinates(columns):
    matrix = Qinv * sp.Matrix([[col.get(i, 0) for col in columns]
                              for i in chosen_rows])
    assert all(x.q == 1 for x in matrix)
    return matrix

for typ, expected_rank, expected_nonunits in [
    ((6, 6), 30, ()), ((6, 8), 54, (2, 2)), ((8, 8), 54, ())]:
    mat = homology_coordinates(families[typ])
    smith = smith_normal_form(mat, domain=ZZ)
    diag = [abs(int(smith[k, k])) for k in range(min(smith.rows, smith.cols))]
    nonzero = [x for x in diag if x]
    assert len(nonzero) == expected_rank
    assert tuple(x for x in nonzero if x != 1) == expected_nonunits
    # Coordinates reconstruct every actual top chain in the claimed basis.
    basis = [oct_tori[j] for j in chosen_columns]
    for col_idx, col in enumerate(families[typ]):
        recovered = defaultdict(int)
        for k, coefficient in enumerate(mat[:, col_idx]):
            if coefficient:
                for cell, a in basis[k].items():
                    recovered[cell] += int(coefficient) * a
        assert {k: v for k, v in recovered.items() if v} == col
    print('TORUS_TYPE', typ, 'COUNT', len(families[typ]),
          'RANK', len(nonzero), 'SMITH_NONUNITS', expected_nonunits)

# Complete graph automorphism group and its orbits on cycle-pair supports.
automorphisms = list(GraphMatcher(G, G).isomorphisms_iter())
assert len(automorphisms) == 144
for typ, expected_orbits in [
    ((6, 6), (12, 18)),
    ((6, 8), (72, 72, 72)),
    ((8, 8), (9, 18, 36, 36, 72))]:
    representatives = pairs[typ]
    names = {frozenset((frozenset(c), frozenset(d))): i
             for i, (c, d) in enumerate(representatives)}
    remaining = set(range(len(representatives)))
    orbit_sizes = []
    while remaining:
        c, d = representatives[min(remaining)]
        orbit = {names[frozenset((frozenset(mp[x] for x in c),
                                  frozenset(mp[x] for x in d)))]
                 for mp in automorphisms}
        assert orbit <= remaining
        remaining.difference_update(orbit)
        orbit_sizes.append(len(orbit))
    assert tuple(sorted(orbit_sizes)) == expected_orbits
    print('AUTOMORPHISM_ORBITS', typ, expected_orbits)

print('NAURU_GRAPH', len(G), len(E), 'AUTOMORPHISMS', len(automorphisms))
print('CUBICAL_CELLS', len(c0), len(c1), len(c2))
print('BOUNDARY2_RANK_Q', 504, 'H2_FREE_RANK', 54)
print('OCTAGON_PAIR_UNIT_MINOR', unit_det)
print('VERIFY_OK_NAURU_SHORT_CYCLE_TORUS_LATTICES')
