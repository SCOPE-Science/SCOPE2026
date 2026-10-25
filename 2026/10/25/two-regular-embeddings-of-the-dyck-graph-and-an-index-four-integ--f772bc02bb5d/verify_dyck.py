"""Exact integral second-homology and short-cycle torus-lattice verification.

Usage: python verify_dyck.py
Requires SymPy 1.14 and NetworkX 3.6 (compatible releases may also work).
All graph, chain, torus, and lattice data are reconstructed in this file.
"""
from collections import Counter, defaultdict
from itertools import combinations

import networkx as nx
from sympy import Matrix, ZZ, eye
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form


N = 32
LCF = [-13, 5, -5, 13] * 8


def modular_rank(columns, p):
    """Exact sparse column rank over the prime field of order p."""
    pivots = {}
    for col in columns:
        remainder = {i: v % p for i, v in col.items() if v % p}
        while remainder:
            q = max(remainder)
            if q not in pivots:
                scale = pow(remainder[q], -1, p)
                pivots[q] = {i: (v * scale) % p for i, v in remainder.items()}
                break
            multiplier = remainder[q]
            for i, v in pivots[q].items():
                new = (remainder.get(i, 0) - multiplier * v) % p
                if new:
                    remainder[i] = new
                else:
                    remainder.pop(i, None)
    return len(pivots)


def simple_cycles(adjacency, lengths=(6, 8)):
    """Enumerate every undirected simple cycle of each listed length once."""
    output = set()
    maximum = max(lengths)
    for start in range(len(adjacency)):
        def visit(path):
            length = len(path)
            if length in lengths and start in adjacency[path[-1]]:
                backward = (start,) + tuple(reversed(path[1:]))
                forward = tuple(path)
                output.add(min(backward, forward))
            if length == maximum:
                return
            for v in sorted(adjacency[path[-1]]):
                # The least vertex of a simple cycle is its unique start.
                if v > start and v not in path:
                    visit(path + [v])
        visit([start])
    return sorted(output)


def smith_nonunits(matrix):
    result = smith_normal_form(matrix, domain=ZZ)
    values = [abs(int(result[i, i])) for i in range(min(result.rows, result.cols))]
    return [x for x in values if x > 1], sum(x > 0 for x in values)


def main():
    edges = {(min(i, (i + 1) % N), max(i, (i + 1) % N)) for i in range(N)}
    edges |= {(min(i, (i + d) % N), max(i, (i + d) % N)) for i, d in enumerate(LCF)}
    edges = sorted(edges)
    adjacency = [set() for _ in range(N)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    assert len(edges) == 48 and all(len(neighbors) == 3 for neighbors in adjacency)

    graph = nx.Graph()
    graph.add_nodes_from(range(N))
    graph.add_edges_from(edges)
    assert nx.is_connected(graph) and nx.is_bipartite(graph)
    assert len(simple_cycles(adjacency, (3, 4, 5))) == 0
    cycles = simple_cycles(adjacency)
    assert Counter(map(len, cycles)) == {6: 16, 8: 12}
    cycle_index = {frozenset(cyc): i for i, cyc in enumerate(cycles)}

    # The unordered deleted-product cubical model. A square is ordered
    # by the indices of its two geometrically disjoint oriented edges.
    zeros = list(combinations(range(N), 2))
    zero_index = {pair: i for i, pair in enumerate(zeros)}
    ones = [(ei, v) for ei, (a, b) in enumerate(edges)
            for v in range(N) if v not in (a, b)]
    one_index = {cell: i for i, cell in enumerate(ones)}
    boundary1 = []
    for ei, v in ones:
        a, b = edges[ei]
        boundary1.append({zero_index[tuple(sorted((b, v)))]: 1,
                          zero_index[tuple(sorted((a, v)))]: -1})
    twos, boundary2 = [], []
    square_index = {}
    for i, (a, b) in enumerate(edges):
        for j in range(i + 1, len(edges)):
            c, d = edges[j]
            if len({a, b, c, d}) < 4:
                continue
            square_index[(i, j)] = len(twos)
            twos.append((i, j))
            boundary2.append({one_index[(j, b)]: 1, one_index[(j, a)]: -1,
                              one_index[(i, d)]: -1, one_index[(i, c)]: 1})
    assert (len(zeros), len(ones), len(twos)) == (496, 1440, 1032)
    for col in boundary2:
        total = defaultdict(int)
        for r, v in col.items():
            for s, w in boundary1[r].items():
                total[s] += v * w
        assert not any(total.values())
    assert modular_rank(boundary2, 101) == 928

    edge_index = {edge: i for i, edge in enumerate(edges)}
    cycle_coefficients = []
    for cyc in cycles:
        coefficients = {}
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            ei = edge_index[tuple(sorted((a, b)))]
            coefficients[ei] = 1 if a < b else -1
        assert len(coefficients) == len(cyc)
        cycle_coefficients.append(coefficients)

    pairs, tori = [], []
    for a, cyc_a in enumerate(cycles):
        for b in range(a + 1, len(cycles)):
            cyc_b = cycles[b]
            if not set(cyc_a).isdisjoint(cyc_b):
                continue
            cross_edges = sum(v in adjacency[u] for u in cyc_a for v in cyc_b)
            pairs.append((a, b, cross_edges))
            torus = {}
            for i, vi in cycle_coefficients[a].items():
                for j, vj in cycle_coefficients[b].items():
                    q = (min(i, j), max(i, j))
                    torus[square_index[q]] = vi * vj * (1 if i < j else -1)
            assert len(torus) == len(cyc_a) * len(cyc_b)
            boundary = defaultdict(int)
            for q, v in torus.items():
                for r, w in boundary2[q].items():
                    boundary[r] += v * w
            assert not any(boundary.values())
            tori.append(torus)

    def kind(i):
        a, b, _ = pairs[i]
        return tuple(sorted((len(cycles[a]), len(cycles[b]))))

    counts = Counter(kind(i) for i in range(len(pairs)))
    assert counts == {(6, 6): 72, (6, 8): 96, (8, 8): 18}
    assert len(tori) == 186
    rows = [[0] * len(tori) for _ in twos]
    for j, col in enumerate(tori):
        for i, v in col.items():
            rows[i][j] = v

    # Find 104 coordinate rows independent over F2. These fixed rows
    # represent a homology-coordinate projection after generation is proved.
    pivots, selected_rows = {}, []
    for i, row in enumerate(rows):
        bitvector = sum(1 << j for j, x in enumerate(row) if x & 1)
        while bitvector:
            leading = bitvector.bit_length() - 1
            if leading not in pivots:
                pivots[leading] = bitvector
                selected_rows.append(i)
                break
            bitvector ^= pivots[leading]
        if len(selected_rows) == 104:
            break
    assert len(selected_rows) == 104
    projection = Matrix([rows[i] for i in selected_rows])
    assert projection.shape == (104, 186)
    assert hermite_normal_form(projection) == eye(104)

    short = [i for i in range(len(tori)) if kind(i) == (6, 6)]
    hex_based = [i for i in range(len(tori)) if kind(i) != (8, 8)]
    short_smith, short_rank = smith_nonunits(projection[:, short])
    assert (short_smith, short_rank) == ([], 72)
    h = hermite_normal_form(projection[:, hex_based])
    assert h.shape == (104, 104) and abs(int(h.det())) == 4
    factors, rank = smith_nonunits(h)
    assert (factors, rank) == ([2, 2], 104)
    assert modular_rank([tori[i] for i in hex_based], 101) == 104
    assert modular_rank([tori[i] for i in hex_based], 2) == 102
    assert modular_rank(tori, 2) == 104

    # Geometry-only automorphism orbits of disjoint-cycle pairs.
    automorphisms = list(nx.algorithms.isomorphism.GraphMatcher(graph, graph).isomorphisms_iter())
    assert len(automorphisms) == 192
    pair_index = {tuple(sorted((a, b))): i for i, (a, b, _) in enumerate(pairs)}
    orbits, seen = [], set()
    for i, (a, b, _) in enumerate(pairs):
        if i in seen:
            continue
        orbit = set()
        for perm in automorphisms:
            a1 = cycle_index[frozenset(perm[v] for v in cycles[a])]
            b1 = cycle_index[frozenset(perm[v] for v in cycles[b])]
            orbit.add(pair_index[tuple(sorted((a1, b1)))])
        assert not orbit & seen
        seen |= orbit
        orbits.append(sorted(orbit))
    orbit_types = sorted((kind(orbit[0]), len(orbit)) for orbit in orbits)
    assert orbit_types == [((6, 6), 24), ((6, 6), 48), ((6, 8), 96),
                           ((8, 8), 6), ((8, 8), 12)]
    for orbit in orbits:
        if kind(orbit[0]) == (8, 8):
            completion = hermite_normal_form(projection[:, hex_based + orbit])
            assert completion == eye(104)

    print('VERIFY_OK_DYCK_SHORT_CYCLE_TORUS_LATTICES')
    print('GRAPH_VERTICES_EDGES_AUTOMORPHISMS', N, len(edges), len(automorphisms))
    print('UNORDERED_CELLS', len(zeros), len(ones), len(twos))
    print('BOUNDARY1_BOUNDARY2_ZERO; RANK_BOUNDARY2_MOD_101', 928)
    print('H2_IS_FREE_RANK', 104)
    print('SIX_EIGHT_CYCLE_COUNTS', 16, 12)
    print('TORI_BY_LENGTH', sorted(counts.items()))
    print('SHORT_ONLY_LATTICE_RANK', short_rank, 'FREE_QUOTIENT_RANK', 32)
    print('HEX_BASED_INDEX', 4, 'SMITH_FACTORS', factors)
    print('ALL_186_TORI_GENERATE_INTEGRALLY', True)
    print('SYMMETRY_ORBITS', orbit_types)
    print('EITHER_OCTAGON_PAIR_ORBIT_COMPLETES_INTEGRAL_GENERATION', True)
    print('SELECTED_SQUARE_ROW_INDICES', tuple(selected_rows))


if __name__ == '__main__':
    main()
