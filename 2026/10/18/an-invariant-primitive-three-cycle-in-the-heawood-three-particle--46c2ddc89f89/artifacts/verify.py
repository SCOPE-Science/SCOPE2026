#!/usr/bin/env python3
"""Exact combinatorial verification for a Heawood three-configuration cycle.

Only Python's standard library is required. Cubical orientations order each
edge by increasing endpoint and order distinct edge factors lexicographically.
All modular reductions are exact over F_3. No numerical eigensolvers are used.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product

P = 3
LINES = tuple(frozenset({j, (j + 1) % 7, (j + 3) % 7}) for j in range(7))
EDGES = tuple(sorted((i, 7 + j) for j, line in enumerate(LINES) for i in line))
assert len(EDGES) == 21 and len(set(LINES)) == 7


def top_cubes(edges):
    endpoints = [set(e) for e in edges]
    return tuple(c for c in combinations(range(len(edges)), 3)
                 if len(endpoints[c[0]] | endpoints[c[1]] | endpoints[c[2]]) == 6)


def boundary_rows(edges, cubes):
    """Return exact sparse 3->2 boundary, indexed by (vertex,edge,edge)."""
    rows = defaultdict(dict)
    for j, c in enumerate(cubes):
        for k, eidx in enumerate(c):
            remaining = c[:k] + c[k+1:]
            for v, sg in ((edges[eidx][0], -1), (edges[eidx][1], 1)):
                rows[(v,) + remaining][j] = sg * (-1 if k % 2 else 1)
    assert sum(len(r) for r in rows.values()) == 6 * len(cubes)
    return rows


def rank_and_kernel_mod3(rows, columns, kernel=True):
    """Exact sparse modular row elimination with one free-column backsolve."""
    pivot = {}
    for inp in rows.values():
        row = {j: a % P for j, a in inp.items() if a % P}
        while row:
            lead = min(row)
            a = row[lead]
            if lead not in pivot:
                pivot[lead] = {j: (a * b) % P for j, b in row.items()}
                break
            for j, b in pivot[lead].items():
                residue = (row.get(j, 0) - a * b) % P
                if residue:
                    row[j] = residue
                else:
                    row.pop(j, None)
    if not kernel:
        return len(pivot), None
    free = [j for j in range(columns) if j not in pivot]
    assert len(free) == 1, (len(free), len(pivot), columns)
    x = [0] * columns
    x[free[0]] = 1
    for j in sorted(pivot, reverse=True):
        x[j] = (-sum(b * x[k] for k, b in pivot[j].items() if k != j)) % P
    integral = [0 if a == 0 else (1 if a == 1 else -1) for a in x]
    first = next(a for a in integral if a)
    if first < 0:
        integral = [-a for a in integral]
    return len(pivot), integral


def is_integral_cycle(rows, coeffs):
    return all(sum(a * coeffs[j] for j, a in r.items()) == 0
               for r in rows.values())


def graph_automorphisms():
    """Enumerate 168 Fano collineations and their 168 point-line duals."""
    line_lookup = {l: j for j, l in enumerate(LINES)}
    preserve = []
    for perm in permutations(range(7)):
        dest_lines = [line_lookup.get(frozenset(perm[i] for i in l))
                      for l in LINES]
        if any(j is None for j in dest_lines):
            continue
        preserve.append(tuple(perm) + tuple(7 + j for j in dest_lines))
    duality = tuple(7 + (-i) % 7 for i in range(7)) + tuple(
        (-j) % 7 for j in range(7))
    result = preserve + [tuple(duality[i] for i in g) for g in preserve]
    assert len(preserve) == 168 and len(set(result)) == 336
    edge_set = set(EDGES)
    for g in result:
        assert set(tuple(sorted((g[a], g[b]))) for a, b in EDGES) == edge_set
    return result


def transformed_cell(cell, g, edges, edge_index, cube_index):
    dest = []
    sign = 1
    for eidx in cell:
        a, b = edges[eidx]
        x, y = g[a], g[b]
        if x > y:
            x, y = y, x
            sign = -sign
        dest.append(edge_index[(x, y)])
    for i in range(3):
        for j in range(i + 1, 3):
            if dest[i] > dest[j]:
                sign = -sign
    return cube_index[tuple(sorted(dest))], sign


def extra_edge_signature(cell):
    chosen = {EDGES[i] for i in cell}
    occupied = set().union(*(set(e) for e in chosen))
    extra = [e for e in EDGES if e not in chosen and set(e) <= occupied]
    is_nonempty_matching = bool(extra) and len(set().union(*(set(e) for e in extra))) == 2 * len(extra)
    return len(extra), is_nonempty_matching


def lift_to_bisection(coeffs, old_cubes, subdiv_edges, sub_index):
    parent_halves = {}
    for old_idx, (u, v) in enumerate(EDGES):
        w = 14 + old_idx
        # Natural original-edge orientation u -> v; canonical subdivided
        # orientation is increasing endpoint at each half-edge.
        halves = []
        for x, y in ((u, w), (w, v)):
            sg = 1 if x < y else -1
            halves.append((sub_index[tuple(sorted((x, y)))], sg))
        parent_halves[old_idx] = halves
    lifted = defaultdict(int)
    for cube, coefficient in zip(old_cubes, coeffs):
        if coefficient == 0:
            continue
        for halves in product((0, 1), repeat=3):
            idxs = [parent_halves[e][h][0] for e, h in zip(cube, halves)]
            sgn = coefficient
            for e, h in zip(cube, halves):
                sgn *= parent_halves[e][h][1]
            for i in range(3):
                for j in range(i+1, 3):
                    if idxs[i] > idxs[j]:
                        sgn = -sgn
            lifted[tuple(sorted(idxs))] += sgn
    return dict(lifted)


def run():
    base_cells = top_cubes(EDGES)
    base_boundary = boundary_rows(EDGES, base_cells)
    assert len(base_cells) == 644 and len(base_boundary) == 1680
    rk, z = rank_and_kernel_mod3(base_boundary, len(base_cells))
    assert rk == 643 and is_integral_cycle(base_boundary, z)
    assert Counter(z) == Counter({0: 252, -1: 196, 1: 196})

    # A graph-theoretic characterization independent of cellular orientations.
    signature_counts = Counter()
    for cell, coeff in zip(base_cells, z):
        num_extra, qualifies = extra_edge_signature(cell)
        assert (coeff != 0) == qualifies
        signature_counts[(num_extra, bool(coeff))] += 1
    assert signature_counts == {(0, False): 84, (1, True): 168,
                                (2, False): 168, (2, True): 168,
                                (3, True): 56}

    autos = graph_automorphisms()
    edge_lookup = {e: i for i, e in enumerate(EDGES)}
    cube_lookup = {cell: i for i, cell in enumerate(base_cells)}
    for g in autos:
        for i, cell in enumerate(base_cells):
            dest, sign = transformed_cell(cell, g, EDGES, edge_lookup, cube_lookup)
            assert z[i] * sign == z[dest]
    unvisited = set(range(len(base_cells)))
    orbits = []
    while unvisited:
        c = min(unvisited)
        orbit = {transformed_cell(base_cells[c], g, EDGES,
                                  edge_lookup, cube_lookup)[0] for g in autos}
        unvisited.difference_update(orbit)
        orbits.append((len(orbit), bool(z[c]), base_cells[c]))
    assert Counter((size, active) for size, active, _ in orbits) == Counter(
        {(168, True): 2, (56, True): 1, (168, False): 1,
         (56, False): 1, (28, False): 1})

    # Bisect every original edge. Then every path between essential vertices
    # has >=2 edges, and every essential cycle has >=12 edges. The standard
    # Abrams discrete-configuration deformation-retraction theorem applies.
    bisected = tuple(sorted(tuple(sorted(edge)) for i, (u, v) in enumerate(EDGES)
                            for edge in ((u, 14+i), (14+i, v))))
    assert len(bisected) == 42
    bisected_lookup = {e: i for i, e in enumerate(bisected)}
    bisection_cells = top_cubes(bisected)
    assert len(bisection_cells) == 9072
    bisected_cell_index = {cell: i for i, cell in enumerate(bisection_cells)}
    lift = lift_to_bisection(z, base_cells, bisected, bisected_lookup)
    assert len(lift) == 3136 and set(lift.values()) <= {-1, 1}
    subdivided_z = [0] * len(bisection_cells)
    for cell, coeff in lift.items():
        subdivided_z[bisected_cell_index[cell]] = coeff
    assert Counter(subdivided_z)[0] == 5936
    bisection_boundary = boundary_rows(bisected, bisection_cells)
    assert len(bisection_boundary) == 24654
    assert is_integral_cycle(bisection_boundary, subdivided_z)
    bisected_rank, _ = rank_and_kernel_mod3(bisection_boundary,
                                             len(bisection_cells), kernel=False)
    assert bisected_rank == 9071
    # Rank >=9071 over Q from reduction modulo 3; primitive nonzero integral
    # kernel vector forces rank <=9071 and primitive rank-one integral kernel.
    print('VERIFY_OK HEAWOOD_14_21_FULL_AUT_336')
    print('RAW_CUBES_644 RANK_F3_643 UNIQUE_PRIMITIVE_392_UNITS')
    print('SUPPORT_IFF_NONEMPTY_EXTRA_EDGE_MATCHING_168_168_56')
    print('RAW_CELL_AUTOMORPHISM_ORBITS_168_56_168_168_56_28')
    print('ALL_336_AUTOMORPHISMS_FIX_INTEGRAL_TOP_GENERATOR')
    print('BISECTED_CUBES_9072 RANK_F3_9071')
    print('PRIMITIVE_LIFT_3136_UNIT_CUBES INTEGER_BOUNDARY_ZERO')
    print('HEAWOOD_THREE_CONFIGURATION_THEOREM_VERIFIED')


if __name__ == '__main__':
    run()
