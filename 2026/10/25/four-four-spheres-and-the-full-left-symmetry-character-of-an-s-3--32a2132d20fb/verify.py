#!/usr/bin/env python3
"""Exact finite proof checks for the directed-forest complex of a six-element group.

Requires only the Python 3 standard library. All simplices, matching arrows,
acyclicity, and equivariant Lefschetz numbers are checked by integer arithmetic.
"""
from collections import Counter, deque


def group_elements():
    return [(a, b) for b in range(2) for a in range(3)]


def right_product(g, generator):
    a, b = g
    if generator == 'r':
        return ((a + (1 if b == 0 else -1)) % 3, b)
    assert generator == 's'
    return (a, 1 - b)


def left_product(g, h):
    a, b = g
    c, d = h
    return ((a + (c if b == 0 else -c)) % 3, b ^ d)


def construction():
    vertices = group_elements()
    vertex_index = {g: i for i, g in enumerate(vertices)}
    arcs = [(vertex_index[g], vertex_index[right_product(g, z)], z)
            for g in vertices for z in ('r', 's')]
    assert len(arcs) == 12 and len(set(arcs)) == 12
    return vertices, vertex_index, arcs


def face_by_predecessors(mask, arcs):
    """A directed forest has at most one incoming arc per vertex, no cycles."""
    predecessor = {}
    for e, (u, v, _) in enumerate(arcs):
        if mask & (1 << e):
            if v in predecessor:
                return False
            predecessor[v] = u
    for v in predecessor:
        seen = set()
        while v in predecessor:
            if v in seen:
                return False
            seen.add(v)
            v = predecessor[v]
    return True


def face_by_topological_sort(mask, arcs):
    """Independent criterion for the same 12-bit masks."""
    degree = [0] * 6
    indeg = [0] * 6
    outgoing = [[] for _ in range(6)]
    for e, (u, v, _) in enumerate(arcs):
        if mask & (1 << e):
            degree[v] += 1
            if degree[v] > 1:
                return False
            indeg[v] += 1
            outgoing[u].append(v)
    q = deque(v for v in range(6) if indeg[v] == 0)
    visits = 0
    while q:
        u = q.popleft()
        visits += 1
        for v in outgoing[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return visits == 6


def list_faces(arcs):
    choices = 1 << len(arcs)
    faces = set()
    for mask in range(choices):
        first = face_by_predecessors(mask, arcs)
        second = face_by_topological_sort(mask, arcs)
        assert first == second, ('independent face predicates disagree', mask)
        if first:
            faces.add(mask)
    assert len(faces) == 432
    assert Counter(f.bit_count() for f in faces) == {
        0: 1, 1: 12, 2: 57, 3: 134, 4: 156, 5: 72
    }
    return faces


def lexicographic_matching(faces, edge_count):
    """Toggle the smallest currently usable arc; do not pair the empty face."""
    unmatched = faces - {0}
    pairs = []
    for e in range(edge_count):
        bit = 1 << e
        for lower in sorted(tuple(unmatched)):
            if lower not in unmatched or lower & bit:
                continue
            upper = lower | bit
            if upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower, upper))
    assert len(pairs) == 213
    assert 0 not in unmatched
    assert Counter(f.bit_count() for f in unmatched) == {1: 1, 5: 4}
    return pairs, unmatched


def acyclic_gradient(faces, pairs, n_arcs):
    reversed_arrows = {upper: lower for lower, upper in pairs}
    indeg = {f: 0 for f in faces if f}
    successors = {f: [] for f in indeg}
    incidence_count = 0
    for upper in indeg:
        for bit_index in range(n_arcs):
            bit = 1 << bit_index
            if not upper & bit:
                continue
            lower = upper ^ bit
            if not lower:  # Empty simplex is not a cell of the realization.
                continue
            incidence_count += 1
            if reversed_arrows.get(upper) == lower:
                src, dst = lower, upper
            else:
                src, dst = upper, lower
            successors[src].append(dst)
            indeg[dst] += 1
    frontier = deque(f for f, v in indeg.items() if v == 0)
    removed = 0
    while frontier:
        current = frontier.popleft()
        removed += 1
        for nxt in successors[current]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                frontier.append(nxt)
    assert removed == len(indeg), (removed, len(indeg))
    assert incidence_count == sum(m.bit_count() for m in faces) - 12
    assert len(indeg) == 431
    return incidence_count


def permutation_sign(sequence):
    inversions = sum(a > b for i, a in enumerate(sequence) for b in sequence[i + 1:])
    return -1 if inversions & 1 else 1


def action_on_arc_indices(g, vertices, vertex_index, arcs):
    edge_index = {arc: i for i, arc in enumerate(arcs)}
    permutation = []
    for u, v, z in arcs:
        gu = vertex_index[left_product(g, vertices[u])]
        gv = vertex_index[left_product(g, vertices[v])]
        permutation.append(edge_index[(gu, gv, z)])
    assert sorted(permutation) == list(range(len(arcs)))
    return permutation


def action_on_face(mask, perm):
    image = 0
    for e, target in enumerate(perm):
        if mask & (1 << e):
            image |= 1 << target
    return image


def reduced_lefschetz(g, vertices, vertex_index, arcs, faces):
    """Compute the alternating trace of the reduced simplicial chain complex."""
    perm = action_on_arc_indices(g, vertices, vertex_index, arcs)
    by_size = Counter()
    for mask in faces:
        if action_on_face(mask, perm) != mask:
            continue
        indices = [e for e in range(len(arcs)) if mask & (1 << e)]
        induced_image = [perm[e] for e in indices]
        by_size[len(indices)] += permutation_sign(induced_image)
    return sum(((-1 if size % 2 == 0 else 1) * value)
               for size, value in by_size.items()), dict(sorted(by_size.items()))


def finite_field_boundary_rank(faces, n_arcs, size, prime=101):
    rows = sorted(f for f in faces if f.bit_count() == size - 1)
    cols = sorted(f for f in faces if f.bit_count() == size)
    ri = {f: i for i, f in enumerate(rows)}
    basis = {}
    for face in cols:
        edges = [i for i in range(n_arcs) if face & (1 << i)]
        vector = {ri[face ^ (1 << e)]: (1 if j % 2 == 0 else prime - 1)
                  for j, e in enumerate(edges)}
        while vector:
            pivot = min(vector)
            if pivot not in basis:
                factor = pow(vector[pivot], prime - 2, prime)
                basis[pivot] = {idx: (val * factor) % prime
                                for idx, val in vector.items()}
                break
            factor = vector[pivot]
            for idx, value in basis[pivot].items():
                update = (vector.get(idx, 0) - factor * value) % prime
                if update:
                    vector[idx] = update
                else:
                    vector.pop(idx, None)
    return len(basis)


def main():
    vertices, vertex_index, arcs = construction()
    faces = list_faces(arcs)
    pairs, critical = lexicographic_matching(faces, len(arcs))
    incidences = acyclic_gradient(faces, pairs, len(arcs))
    assert critical == {1, 1444, 1620, 2392, 3968}, critical
    print('GROUP: order 6, vertices r^a s^b for a=0,1,2 and b=0,1')
    print('GENERATORS: right multiplication by r, s; r^3=s^2=1, srs=r^-1')
    print('ARCS:', len(arcs))
    print('INDEPENDENT FACE TESTS: ALL 4096 SUBSETS AGREE')
    print('FACES INCLUDING EMPTY: 432; COUNTS BY CARDINALITY: 1,12,57,134,156,72')
    print('MORSE PAIRS:', len(pairs), 'CRITICAL MASKS:', sorted(critical))
    print('MATCHED HASSE GRAPH ACYCLIC: YES; NONEMPTY CELLS:', len(faces) - 1,
          'NONEMPTY CODIMENSION-ONE INCIDENCES:', incidences)
    assert len(pairs) * 2 + len(critical) == len(faces) - 1
    print('MORSE DIMENSIONS: ONE ZERO-CELL, FOUR FOUR-CELLS')
    char = {}
    for g in vertices:
        perm = action_on_arc_indices(g, vertices, vertex_index, arcs)
        assert {action_on_face(face, perm) for face in faces} == faces
        value, counts = reduced_lefschetz(g, vertices, vertex_index, arcs, faces)
        char[g] = value
        print('LEFT ACTION CHARACTER', g, value, 'FIXED ORIENTED CHAIN TRACES', counts)
    assert char == {(0, 0): 4, (1, 0): 1, (2, 0): 1,
                    (0, 1): -2, (1, 1): -2, (2, 1): -2}
    # Irreducible character rows for S3 on identity, transpositions, 3-cycles.
    e, t, c = char[(0, 0)], char[(0, 1)], char[(1, 0)]
    triv = (e + 3 * t + 2 * c) // 6
    sign = (e - 3 * t + 2 * c) // 6
    standard = (2 * e - 2 * c) // 6
    assert (triv, sign, standard) == (0, 2, 1)
    print('IRREDUCIBLE RATIONAL S3 MULTIPLICITIES: TRIVIAL=0, SIGN=2, STANDARD=1')
    expected_ranks = {1: 1, 2: 11, 3: 46, 4: 88, 5: 68}
    for prime in (101, 103):
        ranks = {k: finite_field_boundary_rank(faces, len(arcs), k, prime)
                 for k in range(1, 6)}
        assert ranks == expected_ranks, ranks
        print('INDEPENDENT SIMPLICIAL BOUNDARY RANKS MOD', prime, ranks)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
