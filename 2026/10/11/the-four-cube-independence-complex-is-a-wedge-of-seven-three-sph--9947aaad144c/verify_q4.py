#!/usr/bin/env python3
"""Exact independent-set, discrete-Morse, and mod-two chain checks for Q4.

Run: python3 verify_q4.py morse_certificate.json
Requires only Python 3 standard library; all arithmetic is exact.
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

VERTICES = 16
ADJ = [sum(1 << j for j in range(VERTICES)
           if (i ^ j).bit_count() == 1) for i in range(VERTICES)]


def all_faces():
    return {s for s in range(1, 1 << VERTICES)
            if all(not (ADJ[i] & s) for i in range(VERTICES) if (s >> i) & 1)}


def pivot_matching(faces):
    left = set(faces)
    pairs = []
    counts = []
    for v in range(VERTICES):
        bit = 1 << v
        chosen = [(a, a | bit) for a in sorted(left)
                  if not (a & bit) and (a | bit) in left]
        for a, b in chosen:
            assert a in left and b in left
            left.remove(a)
            left.remove(b)
        pairs.extend(chosen)
        counts.append(len(chosen))
    return pairs, sorted(left), counts


def mod2_rank(vectors):
    pivots = {}
    for v in vectors:
        while v:
            lead = v.bit_length() - 1
            if lead not in pivots:
                pivots[lead] = v
                break
            v ^= pivots[lead]
    return len(pivots)


def main(cert_path):
    c = json.loads(Path(cert_path).read_text(encoding='utf-8'))
    assert c['graph'] == 'Q4' and c['vertex_encoding'] == 'integers 0..15, four-bit binary'
    faces = all_faces()
    assert len(faces) == 742
    by_dim = defaultdict(list)
    for s in sorted(faces):
        by_dim[s.bit_count() - 1].append(s)
    fvector = [len(by_dim[d]) for d in range(8)]
    assert fvector == [16, 88, 208, 228, 128, 56, 16, 2] == c['f_vector']
    pairs, critical, counts = pivot_matching(faces)
    assert c['pivot_order'] == list(range(VERTICES))
    assert c['pairs'] == [[a, b] for a, b in pairs]
    assert c['critical_faces'] == critical
    assert c['pair_counts_by_pivot'] == counts
    assert len(pairs) == 367 and len(critical) == 8
    assert sorted(s.bit_count() - 1 for s in critical) == [0] + [3] * 7
    assert len({x for p in pairs for x in p}) == 734

    # Independently check all cover relations of the full face poset.
    matched = set(pairs)
    arcs = []
    for upper in sorted(faces):
        for v in range(VERTICES):
            if (upper >> v) & 1:
                lower = upper ^ (1 << v)
                if lower in faces:
                    arcs.append((lower, upper) if (lower, upper) in matched
                                else (upper, lower))
    assert len(arcs) == c['hasse_cover_count']
    ordering = c['topological_order']
    assert len(ordering) == len(faces) and set(ordering) == faces
    position = {v: k for k, v in enumerate(ordering)}
    assert all(position[u] < position[v] for u, v in arcs)

    # Independent exact GF(2) boundary ranks.
    ranks = {}
    for dim in range(1, 8):
        index = {s: i for i, s in enumerate(by_dim[dim - 1])}
        columns = []
        for upper in by_dim[dim]:
            column = 0
            for v in range(VERTICES):
                if (upper >> v) & 1:
                    column ^= 1 << index[upper ^ (1 << v)]
            columns.append(column)
        ranks[dim] = mod2_rank(columns)
    assert [ranks[d] for d in range(1, 8)] == [15, 73, 135, 86, 42, 14, 2]
    betti = [fvector[d] - ranks.get(d, 0) - ranks.get(d + 1, 0)
             for d in range(8)]
    assert betti == [1, 0, 0, 7, 0, 0, 0, 0]
    print('VERIFY_OK independent_sets=743 nonempty_faces=742 pairs=367 '
          'critical=1x0+7x3 acyclic_edges=%s mod2_b3=7' % len(arcs))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: python3 verify_q4.py morse_certificate.json')
    main(sys.argv[1])
