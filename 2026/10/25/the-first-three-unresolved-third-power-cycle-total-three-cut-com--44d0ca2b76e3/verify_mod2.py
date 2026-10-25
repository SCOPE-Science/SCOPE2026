#!/usr/bin/env python3
"""Independent GF(2) simplicial homology computation for the three cases.

This implementation does not read the Morse certificate, uses a different
facet/subface construction, and independently forms exact boundary columns.
It checks all dimensions rather than sampling random boundary maps.
"""
from itertools import combinations


def construct(n):
    levels = {}
    for candidate in combinations(range(n), 3):
        disjoint_in_graph = all(min((x - y) % n, (y - x) % n) > 3
                                for x, y in combinations(candidate, 2))
        if not disjoint_in_graph:
            continue
        facet = tuple(v for v in range(n) if v not in candidate)
        for cardinality in range(1, len(facet) + 1):
            levels.setdefault(cardinality - 1, set()).update(combinations(facet, cardinality))
    return {degree: sorted(faces) for degree, faces in levels.items()}


def rank_gf2(columns):
    leading = {}
    for column in columns:
        while column:
            pivot = column.bit_length() - 1
            if pivot not in leading:
                leading[pivot] = column
                break
            column ^= leading[pivot]
    return len(leading)


def homology(n):
    levels = construct(n)
    ranks = {}
    counts = {degree: len(faces) for degree, faces in levels.items()}
    for degree in range(1, max(levels) + 1):
        rows = {face: j for j, face in enumerate(levels[degree - 1])}
        columns = []
        for face in levels[degree]:
            column = 0
            for omitted in range(len(face)):
                boundary_face = face[:omitted] + face[omitted + 1:]
                column ^= 1 << rows[boundary_face]
            columns.append(column)
        ranks[degree] = rank_gf2(columns)
    reduced = {degree: len(levels[degree]) - ranks.get(degree, 0) - ranks.get(degree + 1, 0)
               for degree in levels}
    # In reduced homology of a connected complex, reduce the H_0 rank by one.
    reduced[0] -= 1
    return counts, {degree: rank for degree, rank in reduced.items() if rank}


def main():
    expected = {13: {5: 1}, 14: {6: 1}, 15: {8: 2}}
    expected_counts = {13: 5434, 14: 13106, 15: 28803}
    for n in [13, 14, 15]:
        counts, betti = homology(n)
        assert sum(counts.values()) == expected_counts[n]
        assert betti == expected[n], (n, betti)
        print(f"n={n}: f_vector={counts}; nonzero_reduced_GF2_betti={betti}")
    print("ALL THREE INDEPENDENT MOD-TWO HOMOLOGY CHECKS PASSED")


if __name__ == "__main__":
    main()
