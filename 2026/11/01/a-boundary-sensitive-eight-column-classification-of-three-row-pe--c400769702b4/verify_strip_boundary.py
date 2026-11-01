"""Exact finite simplicial Morse verification for P_3 square P_{2k} and C_3 square P_{2k}, k=1,2,3,4.

Standard Python 3, no external packages. All face sets and Hasse incidences
are enumerated, and the reversed matched Hasse digraph is topologically sorted.
"""
from collections import Counter, deque
from functools import lru_cache
import json


def graph_edges(length, periodic):
    """Vertices (row, column), row in {0,1,2}, column in range(length)."""
    verts = lambda r, c: r * length + c
    edge_set = set()
    for r in range(3):
        for c in range(length):
            for rr, cc in ((((r + 1) % 3) if periodic else r + 1, c), (r, c + 1)):
                if cc >= length or rr >= 3:
                    continue
                u, v = sorted((verts(r, c), verts(rr, cc)))
                edge_set.add((u, v))
    return sorted(edge_set)


def perfect_matchings(length, edges):
    adjacency = [[] for _ in range(3 * length)]
    for index, (u, v) in enumerate(edges):
        adjacency[u].append((v, index))
        adjacency[v].append((u, index))

    @lru_cache(None)
    def complete(remaining):
        if remaining == 0:
            return (0,)
        u = (remaining & -remaining).bit_length() - 1
        output = []
        for v, edge_index in adjacency[u]:
            if remaining & (1 << v):
                rest = remaining ^ (1 << u) ^ (1 << v)
                for suffix in complete(rest):
                    output.append(suffix | (1 << edge_index))
        return tuple(output)

    result = complete((1 << (3 * length)) - 1)
    assert len(result) == len(set(result)), 'duplicate perfect matchings'
    for matching in result:
        vertex_occupancy = 0
        assert matching.bit_count() == 3 * length // 2
        for i, (u, v) in enumerate(edges):
            if matching & (1 << i):
                assert not (vertex_occupancy & ((1 << u) | (1 << v)))
                vertex_occupancy |= (1 << u) | (1 << v)
        assert vertex_occupancy == (1 << (3 * length)) - 1
    return result


def simplices(matchings):
    faces = {0}
    for matching in matchings:
        subset = matching
        while True:
            faces.add(subset)
            if not subset:
                break
            subset = (subset - 1) & matching
    return faces


def staged_toggle_matching(faces, edge_count):
    remaining = set(faces)
    partners = {}
    counts_per_stage = []
    for i in range(edge_count):
        bit = 1 << i
        # Whole-stage parallel matching; the lower faces are pairwise distinct.
        lower = [face for face in remaining
                 if not (face & bit) and (face | bit) in remaining]
        for face in lower:
            upper = face | bit
            assert face in remaining and upper in remaining
            remaining.remove(face)
            remaining.remove(upper)
            partners[face] = upper
            partners[upper] = face
        counts_per_stage.append(len(lower))
    assert 2 * len(partners) // 2 + len(remaining) == len(faces)
    assert len(partners) + len(remaining) == len(faces)
    return partners, remaining, counts_per_stage


def check_hasse_acyclic(faces, partners, edge_count):
    """Reverse precisely the matched cover incidences and topologically sort."""
    mask_all = (1 << edge_count) - 1
    indegree = {}
    incidence_count = 0
    for face in faces:
        incoming = int(face in partners and partners[face].bit_count() == face.bit_count() - 1)
        addable = mask_all ^ face
        while addable:
            bit = addable & -addable
            addable -= bit
            upper = face | bit
            if upper in faces:
                incidence_count += 1
                if partners.get(face) != upper:
                    incoming += 1
        indegree[face] = incoming
    pending = deque(face for face, degree in indegree.items() if degree == 0)
    visited = 0
    oriented_incidence_count = 0
    while pending:
        face = pending.popleft()
        visited += 1
        mate = partners.get(face)
        if mate is not None and mate.bit_count() == face.bit_count() + 1:
            indegree[mate] -= 1
            oriented_incidence_count += 1
            assert indegree[mate] >= 0
            if indegree[mate] == 0:
                pending.append(mate)
        removed = face
        while removed:
            bit = removed & -removed
            removed -= bit
            lower = face ^ bit
            if lower == mate:
                continue
            indegree[lower] -= 1
            oriented_incidence_count += 1
            assert indegree[lower] >= 0
            if indegree[lower] == 0:
                pending.append(lower)
    assert visited == len(faces), f'directed Hasse cycle: visited {visited} / {len(faces)}'
    assert oriented_incidence_count == incidence_count
    assert all(value == 0 for value in indegree.values())
    return incidence_count


def verify(length, periodic):
    edges = graph_edges(length, periodic)
    assert len(edges) == (6 if periodic else 5) * length - 3
    facets = perfect_matchings(length, edges)
    faces = simplices(facets)
    f_vector = Counter(face.bit_count() - 1 for face in faces)
    partners, remaining, stages = staged_toggle_matching(faces, len(edges))
    assert len(partners) % 2 == 0
    assert all(((a ^ b).bit_count() == 1 and
                (a & b) == (a if a.bit_count() < b.bit_count() else b) and
                a in faces and b in faces and partners.get(b) == a)
               for a, b in partners.items())
    hasse = check_hasse_acyclic(faces, partners, len(edges))
    critical = Counter(face.bit_count() - 1 for face in remaining)
    expected_facets = ({2: 4, 4: 19, 6: 91, 8: 436} if periodic
                       else {2: 3, 4: 11, 6: 41, 8: 153})
    expected_faces = ({2: 26, 4: 817, 6: 25769, 8: 812758} if periodic
                      else {2: 20, 4: 495, 6: 12375, 8: 309480})
    expected_critical = ({2: {}, 4: {1: 3}, 6: {2: 3}, 8: {3: 12}} if periodic
                         else {2: {}, 4: {1: 1}, 6: {2: 1}, 8: {3: 2}})
    assert len(facets) == expected_facets[length]
    assert len(faces) == expected_faces[length]
    assert dict(critical) == expected_critical[length]
    assert sum((-1) ** dim * count for dim, count in f_vector.items()) == \
        sum((-1) ** dim * count for dim, count in critical.items())
    return {'length': length, 'periodic_transverse_boundary': periodic,
            'graph_vertices': 3 * length,
            'graph_edges': len(edges), 'perfect_matchings': len(facets),
            'total_faces_including_empty': len(faces),
            'f_vector_including_empty': {str(k): f_vector[k] for k in sorted(f_vector)},
            'toggle_pairs': len(partners) // 2,
            'critical_cells': {str(k): critical[k] for k in sorted(critical)},
            'hasse_cover_incidences': hasse,
            'all_hasse_orientation_acyclic': True,
            'paired_empty_face': 0 in partners,
            'stage_pair_count': stages}


def main():
    reports = [verify(n, periodic) for periodic in (False, True)
               for n in (2, 4, 6, 8)]
    print(json.dumps({'proof_checks': reports,
                      'marker': 'THREE_ROW_BOUNDARY_PERFECT_MATCHING_MORSE_OK'},
                     indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
