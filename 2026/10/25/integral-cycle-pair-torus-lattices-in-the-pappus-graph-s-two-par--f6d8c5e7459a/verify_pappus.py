#!/usr/bin/env python3
"""Exact finite certificate for two-point configuration homology of the Pappus graph.

Requires Python 3.11+, networkx 3.6.1, sympy 1.14.0.
All calculations are exact (integers and finite fields); no floating-point ranks.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

import networkx as nx
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 18
LCF = (5, 7, -7, 7, -7, -5) * 3
EDGE_SET = {
    tuple(sorted((i, (i + d) % N))) for i, d in enumerate(LCF)
} | {
    tuple(sorted((i, (i + 1) % N))) for i in range(N)
}
E = sorted(EDGE_SET)
G = nx.Graph()
G.add_nodes_from(range(N))
G.add_edges_from(E)
assert len(E) == 27 and set(dict(G.degree()).values()) == {3}
assert nx.is_isomorphic(G, nx.pappus_graph())
EDGE_NUMBER = {edge: i for i, edge in enumerate(E)}

# The regular unordered deleted-product CW complex: disjoint vertex pairs,
# disjoint edge--vertex pairs, and unordered disjoint edge pairs.
C0 = list(combinations(range(N), 2))
C0_INDEX = {a: i for i, a in enumerate(C0)}
C1 = [(e, v) for e in E for v in range(N) if v not in e]
C1_INDEX = {a: i for i, a in enumerate(C1)}
C2 = [(E[i], E[j]) for i in range(len(E)) for j in range(i+1, len(E))
      if not set(E[i]) & set(E[j])]
C2_INDEX = {a: i for i, a in enumerate(C2)}
assert (len(C0), len(C1), len(C2)) == (153, 432, 297)

# All graph edges, and all product cells, are oriented from the smaller
# numbered endpoint/edge to the larger. The quotient's product orientation
# uses increasing edge numbers.
BOUNDARY1 = []
for e, v in C1:
    a, b = e
    BOUNDARY1.append({C0_INDEX[tuple(sorted((b, v)))]: 1,
                      C0_INDEX[tuple(sorted((a, v)))]: -1})
BOUNDARY2 = []
for e, f in C2:
    a, b = e
    c, d = f
    BOUNDARY2.append({C1_INDEX[(f, b)]: 1,
                      C1_INDEX[(f, a)]: -1,
                      C1_INDEX[(e, d)]: -1,
                      C1_INDEX[(e, c)]: 1})
for col in BOUNDARY2:
    acc = defaultdict(int)
    for i, value in col.items():
        for j, a in BOUNDARY1[i].items():
            acc[j] += value * a
    assert all(v == 0 for v in acc.values())

# H_0 has rank one: verify connectivity of the one-skeleton.
neighbor = [set() for _ in C0]
for col in BOUNDARY1:
    a, b = col
    neighbor[a].add(b)
    neighbor[b].add(a)
seen = {0}
q = deque([0])
while q:
    i = q.popleft()
    for j in neighbor[i] - seen:
        seen.add(j)
        q.append(j)
assert len(seen) == len(C0)

# DFS gives every simple undirected cycle exactly once: its smallest vertex
# starts the word, and its second vertex is less than its final vertex.
adj = {v: sorted(G.neighbors(v)) for v in G.nodes}
CYCLES = []
def visit(root, path):
    for nxt in adj[path[-1]]:
        if nxt == root:
            if len(path) >= 3 and path[1] < path[-1]:
                CYCLES.append(tuple(path))
        elif nxt > root and nxt not in path:
            visit(root, path + [nxt])
for v in range(N):
    visit(v, [v])
assert len(CYCLES) == 783
assert Counter(map(len, CYCLES)) == {6: 18, 8: 54, 10: 54, 12: 243,
                                      14: 162, 16: 216, 18: 36}
CYCLE_BY_SUPPORT = {tuple(sorted(c)): i for i, c in enumerate(CYCLES)}
CYCLEDATA = []
for path in CYCLES:
    signs = {}
    for a, b in zip(path, path[1:] + path[:1]):
        signs[EDGE_NUMBER[tuple(sorted((a, b)))]] = 1 if a < b else -1
    CYCLEDATA.append((sum(1 << v for v in path), signs))

def torus_chain(i, j):
    terms = defaultdict(int)
    for e, s in CYCLEDATA[i][1].items():
        for f, t in CYCLEDATA[j][1].items():
            a, b = sorted((e, f))
            terms[C2_INDEX[(E[a], E[b])]] += s*t*(1 if e < f else -1)
    assert all(v in (-1, 1) for v in terms.values())
    return dict(terms)

def boundary_of(chain):
    out = defaultdict(int)
    for col, coeff in chain.items():
        for row, a in BOUNDARY2[col].items():
            out[row] += coeff*a
    return {row: a for row, a in out.items() if a}

PAIR_BY_TYPE = defaultdict(list)
TORI = {}
for i in range(len(CYCLES)):
    for j in range(i+1, len(CYCLES)):
        if CYCLEDATA[i][0] & CYCLEDATA[j][0]:
            continue
        pair = (i, j)
        chain = torus_chain(i, j)
        assert not boundary_of(chain)
        TORI[pair] = chain
        PAIR_BY_TYPE[tuple(sorted((len(CYCLES[i]), len(CYCLES[j]))))].append(pair)
assert {k: len(v) for k, v in PAIR_BY_TYPE.items()} == {
    (6, 6): 45, (6, 8): 108, (6, 10): 54, (8, 8): 27}

def rank_over_prime(vectors, p):
    pivots = {}
    independent = []
    for j, v in enumerate(vectors):
        row = {k: a % p for k, a in v.items() if a % p}
        while row:
            lead = min(row)
            if lead not in pivots:
                inv = pow(row[lead], -1, p)
                pivots[lead] = {k: a*inv % p for k, a in row.items()}
                independent.append(j)
                break
            factor = row[lead]
            for k, a in pivots[lead].items():
                value = (row.get(k, 0) - factor*a) % p
                if value:
                    row[k] = value
                else:
                    row.pop(k, None)
    return len(pivots), independent, list(pivots)

rank_d2_101 = rank_over_prime(BOUNDARY2, 101)[0]
rank_d2_2 = rank_over_prime(BOUNDARY2, 2)[0]
assert (rank_d2_101, rank_d2_2) == (270, 269)

HEX = PAIR_BY_TYPE[(6, 6)]
HEX_VECTORS = [TORI[pair] for pair in HEX]
rank, selected_columns, selected_rows = rank_over_prime(HEX_VECTORS, 2)
assert rank == 27
assert selected_columns == [0, 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15,
                            16, 17, 18, 20, 21, 22, 23, 25, 26, 27, 30, 31, 33, 36]
assert selected_rows == [7, 9, 12, 16, 2, 4, 29, 31, 0, 26, 76, 80, 24,
                         34, 66, 68, 22, 71, 106, 109, 111, 114, 143, 145,
                         152, 179, 221]
minor = Matrix([[HEX_VECTORS[k].get(r, 0) for k in selected_columns]
                for r in selected_rows])
assert minor.det(method='domain-ge') == 1
inverse = minor.inv()
assert all(a.q == 1 for a in inverse)

# Since the cycles lie in the rank-27 kernel of d_2 and the selected 27
# chain vectors have a unit minor, they are an integral basis of H_2.
def integer_coordinates(pairs):
    X = Matrix([[TORI[pair].get(r, 0) for pair in pairs]
                for r in selected_rows])
    R = inverse * X
    assert all(a.q == 1 for a in R)
    # Substituting the extracted coordinates reconstructs every entire chain.
    for j, pair in enumerate(pairs):
        reconstructed = defaultdict(int)
        for k, idx in enumerate(selected_columns):
            coeff = int(R[k,j])
            if coeff:
                for r, a in HEX_VECTORS[idx].items():
                    reconstructed[r] += coeff*a
        assert all(reconstructed.get(r, 0) == TORI[pair].get(r, 0)
                   for r in set(reconstructed) | set(TORI[pair]))
    return R

def smith_profile(M):
    S = smith_normal_form(M, domain=ZZ)
    factors = [abs(int(S[i,i])) for i in range(min(M.shape)) if S[i,i]]
    return len(factors), tuple(x for x in factors if x != 1)

# A second enumeration independently discovers the full automorphism action.
AUTS = list(nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter())
assert len(AUTS) == 216
remaining = set(HEX)
HEX_ORBITS = []
while remaining:
    rep = min(remaining)
    orbit = {
        tuple(sorted(CYCLE_BY_SUPPORT[tuple(sorted(g[v] for v in CYCLES[i]))]
                     for i in rep))
        for g in AUTS
    }
    assert orbit <= remaining
    remaining -= orbit
    HEX_ORBITS.append(sorted(orbit))
HEX_ORBITS.sort(key=len)
assert [len(o) for o in HEX_ORBITS] == [18, 27]
assert [smith_profile(integer_coordinates(o)) for o in HEX_ORBITS] == [
    (17, ()), (27, (2, 2, 2, 2, 2))]

PROFILES = {}
for typ in ((6, 6), (6, 8), (6, 10), (8, 8)):
    PROFILES[typ] = smith_profile(integer_coordinates(PAIR_BY_TYPE[typ]))
assert PROFILES == {
    (6, 6): (27, ()),
    (6, 8): (27, ()),
    (6, 10): (27, (2, 2, 2, 2, 4)),
    (8, 8): (27, (2, 2, 2, 2, 2))}

print('VERIFY_OK_PAPPUS_TWO_POINT_HEXAGON_TORUS_LATTICES')
print('GRAPH',len(G),len(E),'LCF_AGREES_WITH_INDEPENDENT_STANDARD_GRAPH',True)
print('CELLS_C0_C1_C2',len(C0),len(C1),len(C2),'BOUNDARY_SQUARED_ZERO')
print('D2_RANK_MOD101',rank_d2_101,'MOD2',rank_d2_2)
print('INTEGRAL_H2_RANK',297-rank_d2_101)
print('GRAPH_SIMPLE_CYCLES',len(CYCLES),'DISJOINT_CYCLE_PAIRS',len(TORI))
print('HEXAGON_PAIR_BASIS_SIZE',len(selected_columns),'UNIT_MINOR',minor.det())
print('AUTOMORPHISMS',len(AUTS),'HEXAGON_TORUS_ORBITS',tuple(map(len,HEX_ORBITS)))
print('HEXAGON_ORBIT_SMITH',tuple(smith_profile(integer_coordinates(o)) for o in HEX_ORBITS))
for typ, value in PROFILES.items():
    print('LENGTH_TYPE',typ,'COUNT',len(PAIR_BY_TYPE[typ]),'RANK_NONUNIT_SMITH',value)
