#!/usr/bin/env python3
"""Full finite certificates for third-power-cycle total three-cut complexes.

Run with Python >= 3.9: python verify_morse.py morse_certificate.json
Each nonempty simplex is encoded as the bitmask of its vertex labels.
The verification traverses EVERY face-poset Hasse covering relation,
not just matched edges or a bounded subcomplex.
"""
import collections
import itertools
import json
import sys


def independent_triples(n):
    triples = []
    for triple in itertools.combinations(range(n), 3):
        if all(min((a-b) % n, (b-a) % n) >= 4
               for a, b in itertools.combinations(triple, 2)):
            triples.append(sum(1 << v for v in triple))
    return triples


def nonempty_faces(n, triples):
    full = (1 << n) - 1
    faces = set()
    for triple in triples:
        facet = full ^ triple
        face = facet
        while face:
            faces.add(face)
            face = (face - 1) & facet
    return faces


def pivot_matching(faces, order):
    active = set(faces)
    pairs = set()
    for vertex in order:
        bit = 1 << vertex
        # Sorted order fixes the exact reproducible certificate.  Each pair
        # uses the same pivot, so within-stage order cannot affect survivors.
        for lower in sorted(active):
            upper = lower | bit
            if (lower & bit) == 0 and lower in active and upper in active:
                assert upper.bit_count() == lower.bit_count() + 1
                pairs.add((lower, upper))
                active.remove(lower)
                active.remove(upper)
    return active, pairs


def check_directed_hasse_acyclic(faces, pairs):
    indegree = dict.fromkeys(faces, 0)
    successors = collections.defaultdict(list)
    covers = 0
    for upper in faces:
        bits = upper
        while bits:
            bit = bits & -bits
            bits ^= bit
            lower = upper ^ bit
            if lower == 0:
                continue  # empty face is not in the nonempty face poset
            if lower not in faces:
                raise AssertionError("simplicial closure failure")
            # Matched cover is oriented upward; all other covers downward.
            source, target = (lower, upper) if (lower, upper) in pairs else (upper, lower)
            successors[source].append(target)
            indegree[target] += 1
            covers += 1
    queue = collections.deque(v for v, degree in indegree.items() if degree == 0)
    visited = 0
    while queue:
        source = queue.popleft()
        visited += 1
        for target in successors[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    if visited != len(faces):
        raise AssertionError("nonacyclic matching: directed Hasse cycle")
    return covers, visited


def main(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        package = json.load(infile)
    assert package["graph_family"] == "third_power_cycles"
    assert package["complex"] == "total_3_cut_complex"
    for entry in package["cases"]:
        n = entry["n"]
        order = entry["vertex_pivot_order"]
        assert sorted(order) == list(range(n))
        triples = independent_triples(n)
        faces = nonempty_faces(n, triples)
        critical, pairs = pivot_matching(faces, order)
        assert len(triples) == entry["independent_triples"]
        assert len(faces) == entry["nonempty_faces"]
        assert len(pairs) == entry["matched_pairs"]
        assert len(faces) == 2 * len(pairs) + len(critical)
        actual = sorted([{"mask": face, "dimension": face.bit_count() - 1}
                         for face in critical], key=lambda item: item["mask"])
        expected = sorted(entry["critical_faces"], key=lambda item: item["mask"])
        assert actual == expected, (n, actual, expected)
        covers, visited = check_directed_hasse_acyclic(faces, pairs)
        assert covers == entry["cover_relations"]
        dims = {dim: sum(face.bit_count() - 1 == dim for face in critical)
                for dim in {face.bit_count() - 1 for face in critical}}
        assert dims.get(0, 0) == 1
        assert set(dims).issubset({0, 5, 6, 8})
        assert {str(dim): count for dim, count in dims.items() if dim > 0} == entry["nonzero_reduced_betti"]
        print("n={}: triples={} nonempty_faces={} pairs={} directed_covers={} "
              "acyclic=True critical={}".format(n, len(triples), len(faces),
                                              len(pairs), covers, actual))
    print("ALL THREE COMPLETE MORSE CERTIFICATES PASSED")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python verify_morse.py morse_certificate.json")
    main(sys.argv[1])
