#!/usr/bin/env python3
"""Exact homological check for four-cut complexes of two 16-vertex graphs.

Requires only Python 3.10+ standard library; no numerical approximations.
Vertex labels: 4*a+b for a,b in {0,1,2,3}.
"""
from itertools import combinations
from collections import Counter, defaultdict, deque

N = 16
K = 4
ALL = (1 << N) - 1
EXPECTED = {
    'rook': {
        'bad4': 1200,
        'dual_f': (16, 120, 560, 620, 288, 48),
        'pairs': 767,
        'critical': {0: 1, 2: 96, 3: 21},
        'morse_rank': {3: 0},
        'mod2_ranks': (15, 105, 359, 240, 48),
        'dual_betti': {2: 96, 3: 21},
        'cut_betti': {10: 21, 11: 96},
        'euler_cut_reduced': -75,
    },
    'shrikhande': {
        'bad4': 1152,
        'dual_f': (16, 120, 560, 668, 288),
        'pairs': 776,
        'critical': {0: 1, 2: 69, 3: 12, 4: 18},
        'morse_rank': {3: 4, 4: 6},
        'mod2_ranks': (15, 105, 390, 276),
        'dual_betti': {2: 65, 3: 2, 4: 12},
        'cut_betti': {9: 12, 10: 2, 11: 65},
        'euler_cut_reduced': -75,
    },
}


def graph(which):
    edges = []
    for u in range(N):
        a, b = divmod(u, 4)
        for v in range(u + 1, N):
            c, d = divmod(v, 4)
            if which == 'rook':
                adjacent = (a == c or b == d)
            elif which == 'shrikhande':
                diff = ((c - a) % 4, (d - b) % 4)
                adjacent = diff in {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
            else:
                raise ValueError(which)
            if adjacent:
                edges.append((u, v))
    adj = [0] * N
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    assert len(edges) == 48
    assert all(x.bit_count() == 6 for x in adj)
    for u in range(N):
        for v in range(u + 1, N):
            assert (adj[u] & adj[v]).bit_count() == 2
    # The last check records (16,6,2,2), including equality of lambda and mu.
    return adj


def connected(vertices, adj):
    first = vertices & -vertices
    reached = first
    while True:
        grown = reached
        walk = reached
        while walk:
            b = walk & -walk
            walk -= b
            grown |= adj[b.bit_length() - 1] & vertices
        if grown == reached:
            return reached == vertices
        reached = grown


def construct_dual(adj):
    good4, bad4 = set(), set()
    for vs in combinations(range(N), K):
        mask = sum(1 << v for v in vs)
        (good4 if connected(mask, adj) else bad4).add(mask)
    assert len(good4) + len(bad4) == 1820
    # First construction: avoid any disconnected four-set.
    face1 = set()
    for mask in range(1, ALL + 1):
        if all((mask & bad) != bad for bad in bad4):
            face1.add(mask)
    # Independent construction: check every four-subset of the proposed face.
    face2 = set()
    for mask in range(1, ALL + 1):
        if mask.bit_count() < K:
            face2.add(mask)
            continue
        positions = [v for v in range(N) if (mask >> v) & 1]
        if all(sum(1 << v for v in subset) in good4
               for subset in combinations(positions, K)):
            face2.add(mask)
    assert face1 == face2
    for m in face1:
        if m.bit_count() > 1:
            assert all((m ^ (1 << v)) in face1 for v in range(N) if (m >> v) & 1)
    # Directly count facets and Euler characteristic of the ordinary cut complex.
    cut_count = Counter()
    for mask in range(1, ALL + 1):
        complement = ALL ^ mask
        if any((complement & bad) == bad for bad in bad4):
            cut_count[mask.bit_count() - 1] += 1
    cut_euler_reduced = -1 + sum((-1) ** d * c for d, c in cut_count.items())
    return face1, len(bad4), cut_count, cut_euler_reduced


def greedy_morse(faces):
    active = set(faces)
    pairs = []
    counts = []
    for v in range(N):
        bit = 1 << v
        stage = [(a, a | bit) for a in sorted(active)
                 if not (a & bit) and (a | bit) in active]
        for a, b in stage:
            assert a in active and b in active and b == (a | bit)
            active.remove(a)
            active.remove(b)
        counts.append(len(stage))
        pairs.extend(stage)
    assert 2 * len(pairs) + len(active) == len(faces)
    return pairs, active, counts


def acyclic_hasse(faces, pairs):
    faces = set(faces)
    matched = set(pairs)
    assert len(matched) == len(pairs)
    outgoing = {a: [] for a in faces}
    indegree = {a: 0 for a in faces}
    used = set()
    incidence = 0
    for hi in faces:
        if hi.bit_count() < 2:
            continue
        for v in range(N):
            if not (hi >> v) & 1:
                continue
            lo = hi ^ (1 << v)
            assert lo in faces
            forward = (lo, hi) if (lo, hi) in matched else (hi, lo)
            if (lo, hi) in matched:
                used.add((lo, hi))
            outgoing[forward[0]].append(forward[1])
            indegree[forward[1]] += 1
            incidence += 1
    assert len(used) == len(pairs)
    todo = deque(a for a in faces if indegree[a] == 0)
    nvisited = 0
    while todo:
        a = todo.popleft()
        nvisited += 1
        for b in outgoing[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                todo.append(b)
    assert nvisited == len(faces), 'non-acyclic gradient matching'
    return incidence


def simplicial_boundary(face, faces):
    if face.bit_count() == 1:
        return {}
    out = {}
    pos = 0
    for v in range(N):
        if (face >> v) & 1:
            subface = face ^ (1 << v)
            assert subface in faces
            out[subface] = (-1) ** pos
            pos += 1
    return out


def check_d_squared(boundaries):
    for face, bd in boundaries.items():
        total = defaultdict(int)
        for low, coeff in bd.items():
            for lower, coeff2 in boundaries[low].items():
                total[lower] += coeff * coeff2
        assert all(v == 0 for v in total.values()), (face, total)


def algebraic_cancellation(faces, pairs):
    remaining = set(faces)
    bd = {s: simplicial_boundary(s, remaining) for s in remaining}
    check_d_squared(bd)
    for low, high in pairs:
        assert low in remaining and high in remaining
        assert low.bit_count() + 1 == high.bit_count()
        coeff = bd[high].get(low, 0)
        assert abs(coeff) == 1, (low, high, coeff)
        # Exact integral elementary chain cancellation, with pivot ±1.
        for s in list(remaining):
            if s in (low, high):
                continue
            if low in bd[s]:
                quotient = bd[s][low] // coeff
                for row, c in bd[high].items():
                    value = bd[s].get(row, 0) - quotient * c
                    if value:
                        bd[s][row] = value
                    else:
                        bd[s].pop(row, None)
        remaining.remove(low)
        remaining.remove(high)
        bd.pop(low)
        bd.pop(high)
        for s in remaining:
            bd[s].pop(low, None)
            bd[s].pop(high, None)
    check_d_squared(bd)
    return remaining, bd


def unit_pivot_rank(matrix):
    if not matrix:
        return 0
    M = [list(row) for row in matrix]
    nrow, ncol = len(M), len(M[0])
    r = 0
    while r < min(nrow, ncol):
        found = next(((i, j) for i in range(r, nrow)
                      for j in range(r, ncol) if abs(M[i][j]) == 1), None)
        if found is None:
            assert all(M[i][j] == 0 for i in range(r, nrow)
                       for j in range(r, ncol)), 'nonunit Smith factor unresolved'
            break
        i, j = found
        M[r], M[i] = M[i], M[r]
        for row in M:
            row[r], row[j] = row[j], row[r]
        if M[r][r] == -1:
            M[r] = [-x for x in M[r]]
        for i in range(nrow):
            if i != r:
                a = M[i][r]
                if a:
                    M[i] = [x - a * y for x, y in zip(M[i], M[r])]
        for j in range(ncol):
            if j != r:
                a = M[r][j]
                if a:
                    for i in range(nrow):
                        M[i][j] -= a * M[i][r]
        assert M[r][r] == 1
        assert all(M[i][r] == 0 for i in range(nrow) if i != r)
        assert all(M[r][j] == 0 for j in range(ncol) if j != r)
        r += 1
    return r


def f2_rank(vectors):
    basis = {}
    for v in vectors:
        while v:
            lead = v.bit_length() - 1
            if lead not in basis:
                basis[lead] = v
                break
            v ^= basis[lead]
    return len(basis)


def original_mod2_boundary_ranks(faces):
    bydim = defaultdict(list)
    for face in sorted(faces):
        bydim[face.bit_count() - 1].append(face)
    ranks = []
    for d in range(1, max(bydim) + 1):
        idx = {s: j for j, s in enumerate(bydim[d - 1])}
        columns = []
        for hi in bydim[d]:
            col = 0
            for v in range(N):
                if (hi >> v) & 1:
                    col ^= 1 << idx[hi ^ (1 << v)]
            columns.append(col)
        ranks.append(f2_rank(columns))
    return tuple(ranks)


def run_case(which):
    exp = EXPECTED[which]
    adj = graph(which)
    faces, bad4, cut_f, cut_euler = construct_dual(adj)
    f = tuple(Counter(s.bit_count() - 1 for s in faces)[d]
              for d in range(max(s.bit_count() for s in faces)))
    assert bad4 == exp['bad4']
    assert f == exp['dual_f'], (which, f)
    assert cut_euler == exp['euler_cut_reduced']
    pairs, critical, stages = greedy_morse(faces)
    assert len(pairs) == exp['pairs'], (which, len(pairs))
    assert dict(Counter(s.bit_count() - 1 for s in critical)) == exp['critical']
    incidences = acyclic_hasse(faces, pairs)
    rest, bd = algebraic_cancellation(faces, pairs)
    assert rest == critical
    crit_dim = defaultdict(list)
    for s in sorted(rest):
        crit_dim[s.bit_count() - 1].append(s)
    ranks = {}
    for d in range(1, max(crit_dim) + 1):
        low = crit_dim[d - 1]
        high = crit_dim[d]
        M = [[bd[h].get(a, 0) for h in high] for a in low]
        ranks[d] = unit_pivot_rank(M)
    assert {d: v for d, v in ranks.items() if v} == {d: v for d, v in exp['morse_rank'].items() if v}
    betti = {d: len(rows) - ranks.get(d, 0) - ranks.get(d + 1, 0)
             for d, rows in crit_dim.items() if d > 0}
    betti = {d: b for d, b in betti.items() if b}
    assert betti == exp['dual_betti'], (which, betti)
    assert sum((-1)**d * b for d, b in betti.items()) == (
        -1 + sum((-1)**d*c for d,c in enumerate(f)))
    mod2 = original_mod2_boundary_ranks(faces)
    assert mod2 == exp['mod2_ranks'], (which, mod2)
    # Every exact differential has Smith factors 1 only, so integral homology
    # is torsion-free; cohomology has the same free ranks.
    cut_betti = {N - d - 3: b for d, b in betti.items()}
    assert cut_betti == exp['cut_betti']
    print(which.upper())
    print('  vertices=16 edges=48 SRG=(16,6,2,2) disconnected_quartets=', bad4)
    print('  Alexander_dual_nonempty_faces=', len(faces), 'dual_f_vector=', f)
    print('  ordinary_cut_f_vector=', tuple(cut_f[d] for d in sorted(cut_f)))
    print('  Morse_pairs=', len(pairs), 'stage_pairs=', tuple(stages))
    print('  Hasse_incidences=', incidences, 'critical_cells=', dict(sorted(exp['critical'].items())))
    print('  integral_nonzero_boundary_ranks=', {d:r for d,r in sorted(ranks.items()) if r})
    print('  all_integral_boundary_Smith_factors_are_units=TRUE')
    print('  independent_F2_boundary_ranks=', mod2)
    print('  integral_Alexander_dual_reduced_betti=', dict(sorted(betti.items())))
    print('  integral_four_cut_reduced_betti=', dict(sorted(cut_betti.items())))
    print('  ordinary_cut_reduced_Euler=', cut_euler)
    return exp['cut_betti']

if __name__ == '__main__':
    a = run_case('rook')
    b = run_case('shrikhande')
    assert a != b
    print('ROOK_SHRIKHANDE_FOUR_CUT_INTEGRAL_HOMOLOGY_VERIFIED')
