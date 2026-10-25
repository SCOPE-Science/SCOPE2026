#!/usr/bin/env python3
"""Exact, dependency-free finite verification for the Petersen nonagon complex.

Run: python3 verify.py
Every graph-edge subset and every face incidence is processed exhaustively.
"""
from collections import Counter, deque
from itertools import combinations


def edges_of_petersen():
    # Outer vertices 0,...,4; inner vertices 5,...,9.
    # The inner step has increment 2 modulo 5.
    outer = [(i, (i + 1) % 5) for i in range(5)]
    spokes = [(i, i + 5) for i in range(5)]
    inner = [(i + 5, ((i + 2) % 5) + 5) for i in range(5)]
    result = sorted(tuple(sorted(pair)) for pair in outer + spokes + inner)
    assert len(result) == 15 and len(set(result)) == 15
    assert Counter(vertex for a, b in result for vertex in (a, b)) == Counter({i: 3 for i in range(10)})
    return result


def is_simple_cycle(edge_mask, edge_list):
    """Characterization: nonempty connected 2-regular spanning support."""
    adjacency = [[] for _ in range(10)]
    for j, (a, b) in enumerate(edge_list):
        if edge_mask & (1 << j):
            adjacency[a].append(b)
            adjacency[b].append(a)
    used = [i for i in range(10) if adjacency[i]]
    if len(used) < 3 or any(len(adjacency[i]) != 2 for i in used):
        return False
    seen = {used[0]}
    stack = [used[0]]
    while stack:
        for neighbor in adjacency[stack.pop()]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return len(seen) == len(used)


def all_nonempty_faces(facets):
    faces = set()
    for facet in facets:
        sub = facet
        while sub:
            faces.add(sub)
            sub = (sub - 1) & facet
    return faces


def toggle_matching(faces, number_of_vertices):
    """Successive face-poset matchings by toggling one simplex vertex."""
    unmatched = set(faces)
    pair_upper = {}
    for index in range(number_of_vertices):
        bit = 1 << index
        for lower in sorted(unmatched):
            if lower not in unmatched or lower & bit:
                continue
            upper = lower | bit
            if upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pair_upper[lower] = upper
    return pair_upper, unmatched


def acyclic_hasse_check(faces, matching, edge_count):
    """Match arcs point up; all other cover arcs point down."""
    adjacent = {face: [] for face in faces}
    indegree = dict.fromkeys(faces, 0)
    incidences = matched_arcs = 0
    for upper in faces:
        for j in range(edge_count):
            bit = 1 << j
            if not upper & bit:
                continue
            lower = upper ^ bit
            if lower == 0:
                continue  # The empty simplex is not a CW cell.
            incidences += 1
            assert lower in faces
            if matching.get(lower) == upper:
                adjacent[lower].append(upper)
                indegree[upper] += 1
                matched_arcs += 1
            else:
                adjacent[upper].append(lower)
                indegree[lower] += 1
    work = deque(sorted(face for face in faces if indegree[face] == 0))
    visited = 0
    while work:
        face = work.popleft()
        visited += 1
        for neighbor in adjacent[face]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                work.append(neighbor)
    return incidences, matched_arcs, visited


def ranks_over_f2(faces):
    """Independent simplicial chain-complex check by bitset elimination."""
    ranks = {0: 0}
    faces_by_size = {r: sorted(face for face in faces if face.bit_count() == r)
                     for r in range(1, 10)}
    for r in range(2, 10):
        row_indices = {face: i for i, face in enumerate(faces_by_size[r - 1])}
        echelon = {}
        for face in faces_by_size[r]:
            column = 0
            for j in range(15):
                if face & (1 << j):
                    column ^= 1 << row_indices[face ^ (1 << j)]
            while column:
                pivot = column.bit_length() - 1
                if pivot in echelon:
                    column ^= echelon[pivot]
                else:
                    echelon[pivot] = column
                    break
        ranks[r - 1] = len(echelon)
    betti = {d: len(faces_by_size[d + 1]) - ranks[d] - ranks.get(d + 1, 0)
             for d in range(9)}
    return ranks, betti


def minimal_missing_face_profile(faces, number_of_vertices):
    counts = Counter()
    for mask in range(1, 1 << number_of_vertices):
        if mask in faces:
            continue
        if all((mask ^ (1 << i)) in faces
               for i in range(number_of_vertices) if mask & (1 << i)):
            counts[mask.bit_count()] += 1
    return counts


def independent_kneser_cycle_profile():
    """Independent construction on the pairs of a five-element set."""
    pair_vertices = list(combinations(range(5), 2))
    graph_edges = [(a, b) for a, b in combinations(range(10), 2)
                   if set(pair_vertices[a]).isdisjoint(pair_vertices[b])]
    assert len(graph_edges) == 15
    return Counter(mask.bit_count() for mask in range(1, 1 << 15)
                   if is_simple_cycle(mask, graph_edges))


def main():
    graph_edges = edges_of_petersen()
    cycles = [mask for mask in range(1, 1 << 15)
              if is_simple_cycle(mask, graph_edges)]
    by_length = Counter(mask.bit_count() for mask in cycles)
    expected_cycles = {5: 12, 6: 10, 8: 15, 9: 20}
    assert dict(by_length) == expected_cycles
    assert dict(independent_kneser_cycle_profile()) == expected_cycles
    longest = [mask for mask in cycles if mask.bit_count() == 9]
    assert len(longest) == 20
    faces = all_nonempty_faces(longest)
    f_vector = [sum(face.bit_count() == r for face in faces) for r in range(1, 10)]
    assert f_vector == [15, 105, 445, 1215, 2010, 1610, 720, 180, 20]
    assert len(faces) == 6320

    matching, critical = toggle_matching(faces, len(graph_edges))
    critical_dimensions = Counter(face.bit_count() - 1 for face in critical)
    assert len(matching) == 3110
    assert dict(critical_dimensions) == {0: 1, 4: 99}
    assert 2 * len(matching) + len(critical) == len(faces)
    incidences, paired_arcs, visited = acyclic_hasse_check(
        faces, matching, len(graph_edges))
    assert (incidences, paired_arcs, visited) == (32775, 3110, 6320)

    ranks, betti = ranks_over_f2(faces)
    assert [ranks[d] for d in range(9)] == [0, 14, 91, 354, 861, 1050, 560, 160, 20]
    assert [betti[d] for d in range(9)] == [1, 0, 0, 0, 99, 0, 0, 0, 0]
    profile = minimal_missing_face_profile(faces, len(graph_edges))
    assert dict(profile) == {3: 10, 4: 30, 5: 48, 6: 40}

    print('graph_vertices=10 graph_edges=15')
    print('simple_cycles_by_length=' + str(sorted(by_length.items())))
    print('independent_kneser_cycle_enumeration=agree')
    print('nonagon_facets=20 simplices=6320')
    print('f_vector=' + str(f_vector))
    print('matched_pairs=3110 critical_cells=' + str(sorted(critical_dimensions.items())))
    print('hasse_incidences=32775 directed_acyclic_vertices=6320')
    print('simplicial_F2_boundary_ranks=' + str([ranks[d] for d in range(9)]))
    print('simplicial_F2_betti=' + str([betti[d] for d in range(9)]))
    print('minimal_nonfaces_by_size=' + str(sorted(profile.items())))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
