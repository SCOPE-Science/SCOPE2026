#!/usr/bin/env python3
"""Exhaustive certificate for the induced-forest complex of KG(5,2).

Uses only Python's standard library. Run: python3 VERIFY.py
"""
from collections import Counter, deque
from itertools import combinations, permutations
from math import factorial

POINTS = tuple(combinations(range(5), 2))
N = len(POINTS)
EDGES = tuple((i, j) for i in range(N) for j in range(i + 1, N)
              if set(POINTS[i]).isdisjoint(POINTS[j]))
ADJ = tuple(tuple(j for a, b in EDGES for j in
                  ([b] if a == i else [a] if b == i else [])) for i in range(N))


def is_forest_union_find(mask):
    parents = list(range(N))
    def root(v):
        while parents[v] != v:
            v = parents[v]
        return v
    for u, v in EDGES:
        if (mask >> u) & (mask >> v) & 1:
            a, b = root(u), root(v)
            if a == b:
                return False
            parents[a] = b
    return True


def is_forest_dfs(mask):
    vertices = {i for i in range(N) if (mask >> i) & 1}
    visited = set()
    components = 0
    for start in vertices:
        if start in visited:
            continue
        components += 1
        visited.add(start)
        queue = [start]
        while queue:
            u = queue.pop()
            for v in ADJ[u]:
                if v in vertices and v not in visited:
                    visited.add(v)
                    queue.append(v)
    edges = sum((mask >> u) & (mask >> v) & 1 for u, v in EDGES)
    return edges == len(vertices) - components


def gf2_rank(columns):
    pivots = {}
    for x in columns:
        while x:
            pivot = x.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = x
                break
            x ^= pivots[pivot]
    return len(pivots)


def cycles_of_permutation(perm):
    seen = set()
    result = []
    for i in range(len(perm)):
        if i in seen:
            continue
        length, j = 0, i
        while j not in seen:
            seen.add(j)
            length += 1
            j = perm[j]
        result.append(length)
    return tuple(sorted(result, reverse=True))


def oriented_sign(permutation, mask):
    images = [permutation[i] for i in range(N) if (mask >> i) & 1]
    inversions = sum(images[i] > images[j]
                     for i in range(len(images)) for j in range(i + 1, len(images)))
    return 1 if inversions % 2 == 0 else -1


def oriented_sign_by_cycles(permutation, mask):
    support = [i for i in range(N) if (mask >> i) & 1]
    remaining = set(support)
    cycle_count = 0
    while remaining:
        cycle_count += 1
        j = next(iter(remaining))
        while j in remaining:
            remaining.remove(j)
            j = permutation[j]
    return -1 if (len(support) - cycle_count) % 2 else 1


def permute_mask(permutation, mask):
    new = 0
    for i in range(N):
        if (mask >> i) & 1:
            new |= 1 << permutation[i]
    return new


def main():
    assert len(EDGES) == 15
    faces = {mask for mask in range(1 << N) if is_forest_union_find(mask)}
    assert all(is_forest_union_find(mask) == is_forest_dfs(mask)
               for mask in range(1 << N))
    assert len(faces) == 786
    vector = [sum(mask.bit_count() == k for mask in faces) for k in range(8)]
    assert vector == [1, 10, 45, 120, 210, 240, 140, 20]
    facets = [mask for mask in faces if not any(
        (mask | (1 << i)) in faces for i in range(N) if not (mask >> i) & 1)]
    assert Counter(mask.bit_count() for mask in facets) == {7: 20, 6: 15}

    minimal_nonfaces = [mask for mask in range(1 << N) if mask not in faces
                        and all((mask ^ (1 << i)) in faces
                                for i in range(N) if (mask >> i) & 1)]
    assert Counter(mask.bit_count() for mask in minimal_nonfaces) == {5:12, 6:10}
    maximal_independent_sets = [mask for mask in range(1 << N)
                                if mask.bit_count() == 4
                                and all(not ((mask >> u) & (mask >> v) & 1)
                                        for u, v in EDGES)]
    stars = [sum(1 << i for i, edge in enumerate(POINTS) if a in edge)
             for a in range(5)]
    assert set(maximal_independent_sets) == set(stars)
    assert all(sum(((stars[a] >> i) & (stars[b] >> i) & 1)
                       for i in range(N)) == 1
               for a in range(5) for b in range(a + 1, 5))

    remaining = set(faces)
    pairs = []
    for pivot in range(N):
        for face in sorted(remaining, key=lambda x: (x.bit_count(), x)):
            upper = face | (1 << pivot)
            if not (face >> pivot) & 1 and face in remaining and upper in remaining:
                pairs.append((face, upper))
                remaining.remove(face)
                remaining.remove(upper)
    # Remove the augmented empty-face pair; its singleton becomes the critical 0-cell.
    empty_pair = [pair for pair in pairs if pair[0] == 0]
    assert len(empty_pair) == 1
    base_vertex = empty_pair[0][1]
    pairs.remove(empty_pair[0])
    critical = remaining | {base_vertex}
    assert len(pairs) == 389
    assert Counter(mask.bit_count() - 1 for mask in critical) == {0: 1, 5: 6}

    # All cover relations of the nonempty face poset; reverse precisely matched edges.
    nonempty = faces - {0}
    pairs_set = set(pairs)
    outgoing = {face: [] for face in nonempty}
    indegree = {face: 0 for face in nonempty}
    edges_checked = 0
    for upper in nonempty:
        for i in range(N):
            if not (upper >> i) & 1:
                continue
            lower = upper ^ (1 << i)
            if not lower:
                continue
            assert lower in nonempty
            src, dst = (lower, upper) if (lower, upper) in pairs_set else (upper, lower)
            outgoing[src].append(dst)
            indegree[dst] += 1
            edges_checked += 1
    assert edges_checked == 3470
    queue = deque(face for face in nonempty if indegree[face] == 0)
    count = 0
    while queue:
        face = queue.popleft()
        count += 1
        for nxt in outgoing[face]:
            indegree[nxt] -= 1
            if not indegree[nxt]:
                queue.append(nxt)
    assert count == len(nonempty), 'Matched Hasse orientation contains a directed cycle'

    # Independent simplicial mod-2 boundary-rank check using the original face basis.
    groups = [[mask for mask in sorted(faces) if mask.bit_count() == k]
              for k in range(1, 8)]
    boundaries = []
    for dimension in range(1, 7):
        basis = {mask: i for i, mask in enumerate(groups[dimension - 1])}
        columns = []
        for face in groups[dimension]:
            col = 0
            for i in range(N):
                if (face >> i) & 1:
                    col ^= 1 << basis[face ^ (1 << i)]
            columns.append(col)
        boundaries.append(gf2_rank(columns))
    # rank ∂_i for dimensions i=1,...,6
    betti = []
    for dim in range(7):
        outgoing_rank = boundaries[dim-1] if dim >= 1 else 1
        incoming_rank = boundaries[dim] if dim < 6 else 0
        betti.append(len(groups[dim]) - outgoing_rank - incoming_rank)
    assert betti == [0, 0, 0, 0, 0, 6, 0], (boundaries, betti)

    char_by_class = {}
    group_size = 0
    for perm in permutations(range(5)):
        group_size += 1
        induced = tuple(POINTS.index(tuple(sorted((perm[a], perm[b]))))
                        for a, b in POINTS)
        assert len(set(induced)) == N
        assert {frozenset((induced[i], induced[j])) for i, j in EDGES} == {frozenset((i, j)) for i, j in EDGES}
        # Reduced Hopf trace: only H_5 survives, so chi_H5 = -L_reduced.
        reduced_lefschetz = -1  # empty simplex
        for face in nonempty:
            if permute_mask(induced, face) == face:
                sign = oriented_sign(induced, face)
                assert sign == oriented_sign_by_cycles(induced, face)
                reduced_lefschetz += (-1 if face.bit_count() % 2 == 0 else 1) * sign
        homology_trace = -reduced_lefschetz
        # ∧^2 of the standard representation of the five-point permutation module.
        fixed = sum(perm[i] == i for i in range(5)) - 1
        perm_squared = tuple(perm[perm[i]] for i in range(5))
        fixed_squared = sum(perm_squared[i] == i for i in range(5)) - 1
        expected = (fixed * fixed - fixed_squared) // 2
        assert homology_trace == expected, (perm, homology_trace, expected)
        key = cycles_of_permutation(perm)
        assert key not in char_by_class or char_by_class[key] == homology_trace
        char_by_class[key] = homology_trace
    assert group_size == 120
    assert char_by_class == {(1, 1, 1, 1, 1): 6,
                             (2, 1, 1, 1): 0,
                             (2, 2, 1): -2,
                             (3, 1, 1): 0,
                             (3, 2): 0,
                             (4, 1): 0,
                             (5,): 1}
    # The character has norm one; it is an irreducible rational character.
    sizes = {cyc: factorial(5) // __import__('math').prod(
             power ** count * factorial(count) for power, count in Counter(cyc).items())
             for cyc in char_by_class}
    assert sum(sizes[cyc] * val**2 for cyc, val in char_by_class.items()) == 120
    print('VERIFY_OK')
    print('faces_including_empty:',len(faces))
    print('f_vector:',vector[1:])
    print('maximal_faces_by_dimension:',{5:15,6:20})
    print('minimal_nonfaces_by_vertices:',{5:12,6:10})
    print('morse_pairs:',len(pairs),'critical_dimensions:',{0:1,5:6},
          'cover_relations:',edges_checked)
    print('boundary_ranks_mod2:',boundaries,'reduced_betti_mod2:',betti)
    print('S5_classes_and_H5_char:',sorted(char_by_class.items()))
    print('character_irreducible:',True)

if __name__ == '__main__':
    main()
