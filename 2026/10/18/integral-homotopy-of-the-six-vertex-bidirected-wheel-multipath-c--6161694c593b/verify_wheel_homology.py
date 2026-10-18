#!/usr/bin/env python3
"""Integral simplicial homology of fully bidirected wheels (rim 3..7).

Uses only Python standard library. Enumerates faces twice, constructs an
acyclic Hasse matching, computes signed Morse boundaries, and proves that
all nonzero Smith factors are units by exact unimodular elimination.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product
import json


def arcs_and_neighbours(n):
    # Hub 0; rim vertices 1,...,n; rim indices cyclic.
    edges = {(0, i) for i in range(1, n + 1)}
    edges |= {tuple(sorted((i, i % n + 1))) for i in range(1, n + 1)}
    arcs = sorted([(u, v) for u, v in edges] + [(v, u) for u, v in edges])
    neighbours = [[v for u, v in arcs if u == x] for x in range(n + 1)]
    return arcs, neighbours


def valid_extension(mask, arc, arcs):
    u, v = arc
    out = {}
    for i, (a, b) in enumerate(arcs):
        if mask & (1 << i):
            if a == u or b == v:
                return False
            out[a] = b
    z = v
    while z in out:
        if z == u:
            return False
        z = out[z]
    return z != u


def enumerate_by_extension(arcs):
    faces = {0}
    def rec(mask, first):
        for j in range(first, len(arcs)):
            if valid_extension(mask, arcs[j], arcs):
                new = mask | (1 << j)
                assert new not in faces
                faces.add(new)
                rec(new, j + 1)
    rec(0, 0)
    return faces


def enumerate_by_partial_injections(arcs, neighbours):
    # Independent construction: each vertex chooses at most one outgoing arc.
    # Distinct positive targets enforce indegree <= 1; directed cycles forbidden.
    lookup = {a: i for i, a in enumerate(arcs)}
    faces = set()
    for targets in product(*[(None,) + tuple(ns) for ns in neighbours]):
        positive = [t for t in targets if t is not None]
        if len(positive) != len(set(positive)):
            continue
        cyclic = False
        for start in range(len(neighbours)):
            seen = set()
            z = start
            while z is not None and z not in seen:
                seen.add(z)
                z = targets[z]
            if z is not None:
                cyclic = True
                break
        if not cyclic:
            mask = sum(1 << lookup[(u, v)] for u, v in enumerate(targets)
                       if v is not None)
            faces.add(mask)
    return faces


def greedy_matching(faces, n_arcs):
    unmatched = set(faces)
    pairs = []
    for j in range(n_arcs):
        bit = 1 << j
        for low in sorted((m for m in unmatched if not m & bit),
                          key=int.bit_count):
            high = low | bit
            if low in unmatched and high in unmatched:
                unmatched.remove(low)
                unmatched.remove(high)
                pairs.append((low, high))
    return pairs, unmatched


def oriented_boundary(face):
    vertices = [i for i in range(face.bit_length()) if face & (1 << i)]
    return [(face ^ (1 << j), (-1) ** k)
            for k, j in enumerate(vertices)]


def check_acyclicity(faces, pairs):
    lower_to_upper = dict(pairs)
    indegree = defaultdict(int)
    forward = defaultdict(list)
    edge_count = 0
    for high in faces:
        for low, _ in oriented_boundary(high):
            if lower_to_upper.get(low) == high:
                source, target = low, high
            else:
                source, target = high, low
            forward[source].append(target)
            indegree[target] += 1
            edge_count += 1
    stack = deque(f for f in faces if indegree[f] == 0)
    visited = 0
    while stack:
        v = stack.popleft()
        visited += 1
        for w in forward[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                stack.append(w)
    assert visited == len(faces), 'Matching is cyclic'
    return edge_count


def morse_chain_matrices(pairs, critical):
    lower_to_upper = dict(pairs)
    uppers = {high for _, high in pairs}
    by_degree = defaultdict(list)
    for x in critical:
        by_degree[x.bit_count() - 1].append(x)
    for degree in by_degree:
        by_degree[degree].sort()

    @lru_cache(None)
    def project_lower_cell(x):
        if x in uppers:
            return {}
        if x not in lower_to_upper:
            return {x: 1}
        y = lower_to_upper[x]
        s = dict(oriented_boundary(y))[x]
        out = defaultdict(int)
        for z, sign in oriented_boundary(y):
            if z == x:
                continue
            for target, coefficient in project_lower_cell(z).items():
                out[target] -= s * sign * coefficient
        return {target: v for target, v in out.items() if v}

    matrices = {}
    for k in sorted(by_degree):
        if k < 0:
            continue
        row_faces = by_degree.get(k - 1, [])
        col_faces = by_degree.get(k, [])
        row_index = {x: i for i, x in enumerate(row_faces)}
        matrix = [[0] * len(col_faces) for _ in row_faces]
        for col, face in enumerate(col_faces):
            coefficients = defaultdict(int)
            for low, s in oriented_boundary(face):
                for target, v in project_lower_cell(low).items():
                    coefficients[target] += s * v
            for target, v in coefficients.items():
                assert target in row_index
                matrix[row_index[target]][col] = v
        matrices[k] = matrix

    for k, matrix in matrices.items():
        lower = matrices.get(k - 1, [])
        if matrix and lower and lower[0]:
            for i in range(len(lower)):
                for j in range(len(matrix[0])):
                    assert sum(lower[i][h] * matrix[h][j]
                               for h in range(len(matrix))) == 0
    return by_degree, matrices


def exact_unit_smith_rank(matrix):
    if not matrix or not matrix[0]:
        return 0
    a = [row[:] for row in matrix]
    nr, nc = len(a), len(a[0])
    r = 0
    while r < min(nr, nc):
        pair = next(((i, j) for i in range(r, nr) for j in range(r, nc)
                     if abs(a[i][j]) == 1), None)
        if pair is None:
            break
        i, j = pair
        a[i], a[r] = a[r], a[i]
        for row in a:
            row[r], row[j] = row[j], row[r]
        if a[r][r] < 0:
            a[r] = [-v for v in a[r]]
        assert a[r][r] == 1
        for i in range(r + 1, nr):
            factor = a[i][r]
            if factor:
                for j in range(r, nc):
                    a[i][j] -= factor * a[r][j]
        for j in range(r + 1, nc):
            # Subtract a[r][j] times pivot column from column j.
            # Column r has exactly one nonzero entry in the active block.
            a[r][j] = 0
        r += 1
    assert all(a[i][j] == 0 for i in range(r, nr)
               for j in range(r, nc)), 'Unresolved Smith factors'
    # All operations are integral elementary unimodular operations, so the
    # matrix is equivalent to diagonal(1,...,1,0,...,0).
    return r


EXPECTED = {
    3: {'faces': 73, 'fvector': [1,12,36,24],
        'critical': {1:7, 2:6}, 'ranks': {}, 'betti': {1:7, 2:6}},
    4: {'faces': 261, 'fvector': [1,16,76,120,48],
        'critical': {2:19, 3:8}, 'ranks': {}, 'betti': {2:19, 3:8}},
    5: {'faces': 871, 'fvector': [1,20,130,330,310,80],
        'critical': {2:12, 3:33, 4:10}, 'ranks': {3:10},
        'betti': {2:2, 3:23, 4:10}},
    6: {'faces': 2783, 'fvector': [1,24,198,700,1080,660,120],
        'critical': {3:46, 4:43, 5:12}, 'ranks': {4:17},
        'betti': {3:29, 4:26, 5:12}},
    7: {'faces': 8597, 'fvector': [1,28,280,1274,2786,2842,1218,168],
        'critical': {3:12, 4:80, 5:55, 6:14},
        'ranks': {4:12, 5:25}, 'betti': {4:43, 5:30, 6:14}},
}


def main():
    output = {}
    for n in range(3, 8):
        arcs, nbrs = arcs_and_neighbours(n)
        faces = enumerate_by_extension(arcs)
        independently_generated = enumerate_by_partial_injections(arcs, nbrs)
        assert faces == independently_generated, f'Independent census differs n={n}'
        dimcounts = Counter(f.bit_count() for f in faces)
        fvector = [dimcounts[k] for k in range(n+1)]
        pairs, critical = greedy_matching(faces, len(arcs))
        incidence_count = check_acyclicity(faces, pairs)
        bydegree, matrices = morse_chain_matrices(pairs, critical)
        crit = {k:len(v) for k,v in sorted(bydegree.items())}
        ranks = {k:exact_unit_smith_rank(m) for k,m in matrices.items()}
        ranks = {k:v for k,v in sorted(ranks.items()) if v}
        betti = {k:crit.get(k,0)-ranks.get(k,0)-ranks.get(k+1,0)
                 for k in range(n)}
        betti = {k:v for k,v in betti.items() if v}
        expected = EXPECTED[n]
        assert len(faces)==expected['faces']
        assert fvector==expected['fvector']
        assert crit==expected['critical']
        assert ranks==expected['ranks']
        assert betti==expected['betti']
        assert 2*len(pairs)+len(critical)==len(faces)
        assert sum((-1)**(k-1)*fvector[k] for k in range(len(fvector))) == \
               sum((-1)**k*v for k,v in betti.items())
        output[str(n)] = {
            'arc_count':len(arcs), 'augmented_face_count':len(faces),
            'fvector_by_cardinality':fvector,
            'face_poset_cover_count':incidence_count,
            'matched_pairs':len(pairs), 'critical_by_degree':crit,
            'nonzero_morse_boundary_ranks_all_unit_smith_factors':ranks,
            'reduced_integral_betti_numbers':betti,
            'all_integral_torsion_absent':True,
            'independent_face_enumerations_agree':True,
        }
    print(json.dumps(output, indent=2, sort_keys=True))
    print('VERIFIED_BIDIRECTED_WHEEL_INTEGRAL_HOMOLOGY')


if __name__ == '__main__':
    main()
