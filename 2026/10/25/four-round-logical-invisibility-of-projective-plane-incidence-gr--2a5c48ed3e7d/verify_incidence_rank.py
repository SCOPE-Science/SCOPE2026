"""Exact finite EF-type checks for projective-plane incidence graphs.

Run: python verify_incidence_rank.py
Python standard library only. Finite checks corroborate the separate universal proof.
"""
import itertools
import json
from collections import Counter


def prime_plane(p):
    assert p in (2, 3)
    points = set()
    for vector in itertools.product(range(p), repeat=3):
        if not any(vector):
            continue
        first = next(a for a in vector if a)
        inv = pow(first, -1, p)
        points.add(tuple((a * inv) % p for a in vector))
    points = sorted(points)
    m = len(points)
    assert m == p * p + p + 1
    neighbors = [0] * (2 * m)
    for i, u in enumerate(points):
        for j, v in enumerate(points):
            if sum(x * y for x, y in zip(u, v)) % p == 0:
                neighbors[i] |= 1 << (m + j)
                neighbors[m + j] |= 1 << i
    assert all(mask.bit_count() == p + 1 for mask in neighbors)
    return neighbors


def atomic(t, neighbors, colored):
    m = len(neighbors) // 2
    sorts = tuple(int(v < m) for v in t) if colored else ()
    relations = tuple(
        1 if t[i] == t[j] else 2 if (neighbors[t[i]] >> t[j]) & 1 else 0
        for i in range(len(t)) for j in range(i)
    )
    return sorts, relations


def signatures(a, b, rank, colored):
    # This is the recursive rank-type computation: at each depth, retain the
    # atomic diagram and the SET of all one-point extension rank-types.
    graphs = (a, b)
    tables = [{t: atomic(t, g, colored)
               for t in itertools.product(range(len(g)), repeat=rank)}
              for g in graphs]
    counts = {}
    triple_cross = None
    for k in range(rank - 1, -1, -1):
        candidates = []
        for g, old in zip(graphs, tables):
            curr = {}
            for t in itertools.product(range(len(g)), repeat=k):
                curr[t] = (atomic(t, g, colored),
                           frozenset(old[t + (v,)] for v in range(len(g))))
            candidates.append(curr)
        intern = {}
        for curr in candidates:
            for key in curr.values():
                if key not in intern:
                    intern[key] = len(intern)
        tables = [{t: intern[key] for t, key in curr.items()}
                  for curr in candidates]
        counts[k] = [len(set(table.values())) for table in tables]
        if k == 3 and rank == 4:
            triple_cross = tables
    return tables[0][()], tables[1][()], counts, triple_cross


def geometric_triple(t, neighbors):
    if len(set(t)) == 1:
        return 'all_equal',
    if len(set(t)) == 2:
        same = next((i, j) for i in range(3) for j in range(i + 1, 3)
                    if t[i] == t[j])
        x, y = [t[i] for i in range(3) if i != same[0]]
        m = len(neighbors) // 2
        if (x < m) == (y < m):
            pair = 'same_side'
        else:
            pair = 'incident' if (neighbors[x] >> y) & 1 else 'nonincident'
        return 'two_equal', same, pair
    m = len(neighbors) // 2
    sides = tuple(v < m for v in t)
    if all(x == sides[0] for x in sides):
        common = any(all((neighbors[t[i]] >> v) & 1 for i in range(3))
                     for v in range(len(neighbors)))
        return 'same_side', 'collinear_or_concurrent' if common else 'triangle'
    minority = next(i for i in range(3) if sides.count(sides[i]) == 1)
    major = tuple(i for i in range(3) if i != minority)
    bits = tuple((neighbors[t[minority]] >> t[i]) & 1 for i in major)
    return 'mixed', minority, bits


def check_rank_four():
    a, b = prime_plane(2), prime_plane(3)
    roots, roots3, counts, triples = signatures(a, b, 4, False)
    assert roots == roots3, 'uncolored fourth-rank theories disagree'
    assert counts == {3: [24, 24], 2: [4, 4], 1: [1, 1], 0: [1, 1]}, counts
    profiles = []
    for graph, triple_rank_type in zip((a, b), triples):
        by_geo = {}
        by_logic = {}
        for t, rank_type in triple_rank_type.items():
            kind = geometric_triple(t, graph)
            by_geo.setdefault(kind, set()).add(rank_type)
            by_logic.setdefault(rank_type, set()).add(kind)
        assert len(by_geo) == len(by_logic) == 24
        assert all(len(v) == 1 for v in by_geo.values())
        assert all(len(v) == 1 for v in by_logic.values())
        profiles.append(set(by_geo))
    assert profiles[0] == profiles[1]
    s30, s31, sorted3counts, _ = signatures(a, b, 3, True)
    assert s30 == s31, 'colored third-rank theories disagree'
    s40, s41, sorted4counts, _ = signatures(a, b, 4, True)
    assert s40 != s41, 'colored fourth-rank witness was not detected'
    return {
        'finite_planes': [{'order': p, 'vertices': len(g),
                           'degree': p+1, 'number_of_lines': len(g)//2}
                          for p, g in ((2, a), (3, b))],
        'uncolored_rank4_equivalent': roots == roots3,
        'uncolored_rank4_type_count_by_tuple_length': counts,
        'geometric_three_tuple_type_count': 24,
        'geometric_three_tuple_type_sets_agree': profiles[0] == profiles[1],
        'colored_rank3_equivalent': s30 == s31,
        'colored_rank4_equivalent': s40 == s41,
        'colored_rank3_type_count_by_tuple_length': sorted3counts,
        'colored_rank4_type_count_by_tuple_length': sorted4counts,
        'uncolored_rank5_separator': 'existence of a vertex with four distinct neighbors',
        'finite_tests_are_not_a_proof_for_non_desarguesian_planes': True
    }


if __name__ == '__main__':
    data = check_rank_four()
    print(json.dumps(data, indent=2, sort_keys=True))
