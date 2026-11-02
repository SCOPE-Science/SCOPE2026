"""Exact finite certificate for the perfect-matching complex of the 3-by-4 grid.

Usage: python CHECK.py  (with COLLAPSE.json in the same directory).
The certificate is a sequence of elementary free-face collapses; all
simplices, all automorphism actions, and the terminal five-cycle are rebuilt.
"""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

ROWS, COLS = 3, 4
edges = []
for row in range(ROWS):
    for col in range(COLS):
        if row + 1 < ROWS:
            edges.append(((row, col), (row + 1, col)))
        if col + 1 < COLS:
            edges.append(((row, col), (row, col + 1)))
edge_index = {frozenset(e): i for i, e in enumerate(edges)}

def perfect_matchings(unused, chosen=()):
    if not unused:
        yield tuple(chosen)
        return
    first = min(unused)
    for second in sorted(unused):
        if first == second:
            continue
        pair = frozenset(((first // COLS, first % COLS),
                          (second // COLS, second % COLS)))
        if pair in edge_index:
            yield from perfect_matchings(unused - {first, second},
                                         chosen + (edge_index[pair],))

facets = list(perfect_matchings(set(range(ROWS * COLS))))
faces = {0}
for facet in facets:
    for size in range(len(facet) + 1):
        for subset in combinations(facet, size):
            faces.add(sum(1 << edge for edge in subset))

assert len(edges) == 17 and len(facets) == 11 and len(faces) == 495
assert Counter(s.bit_count() - 1 for s in faces) == {
    -1: 1, 0: 17, 1: 85, 2: 164, 3: 151, 4: 66, 5: 11}

def build_certificate():
    remaining = set(faces) - {0}
    pairs = []
    while True:
        found = None
        for face in sorted(remaining, key=lambda m: (m.bit_count(),
                                                    [i for i in range(17) if m >> i & 1])):
            if face.bit_count() == 6:
                continue
            upward = []
            for vertex in range(len(edges)):
                if not face >> vertex & 1 and face | (1 << vertex) in remaining:
                    upward.append(face | (1 << vertex))
                    if len(upward) > 1:
                        break
            if len(upward) == 1:
                found = (face, upward[0])
                break
        if found is None:
            break
        pairs.append(found)
        remaining.difference_update(found)
    return pairs, remaining

def verify():
    certificate = json.loads((Path(__file__).resolve().parent / 'COLLAPSE.json').read_text())
    pairs = certificate['pairs']
    remaining = set(faces) - {0}
    assert len(pairs) == 242
    for low, high in pairs:
        assert low in remaining and high in remaining
        assert high.bit_count() == low.bit_count() + 1
        assert low & high == low
        actual_cofaces = {low | (1 << i) for i in range(len(edges))
                          if not low >> i & 1 and low | (1 << i) in remaining}
        assert actual_cofaces == {high}, (low, high, actual_cofaces)
        remaining.difference_update((low, high))
    vertices = {10, 13, 14, 15, 16}
    cycle_edges = {(10, 15), (10, 16), (13, 14), (13, 15), (14, 16)}
    target = {1 << u for u in vertices} | {(1 << u) | (1 << v) for u, v in cycle_edges}
    assert remaining == target, (len(remaining), remaining ^ target)
    def orientation(vals):
        return (-1) ** sum(vals[i] > vals[j]
                           for i in range(len(vals)) for j in range(i+1, len(vals)))
    chars = []
    for op in (
        lambda x, y: (ROWS - 1 - x, y),
        lambda x, y: (x, COLS - 1 - y),
        lambda x, y: (ROWS - 1 - x, COLS - 1 - y),
    ):
        perm = {i: edge_index[frozenset((op(*e[0]), op(*e[1])))] for i,e in enumerate(edges)}
        lef = 0
        for mask in faces - {0}:
            originals = [i for i in range(len(edges)) if mask >> i & 1]
            mapped = [perm[i] for i in originals]
            if set(mapped) == set(originals):
                lef += (-1) ** (len(originals) - 1) * orientation(mapped)
        chars.append(1 - lef)  # Connected S^1: Lefschetz number = 1 - trace on H_1.
    assert chars == [-1, 1, -1], chars
    assert sum(chars) + 1 == 0  # full Klein-four H_1 invariant rank = 0
    print('GRID34_COMPLETE_COLLAPSE_AND_SYMMETRY_OK')
    print('facets=11 faces=495 collapses=242 residual_cycle_length=5')
    print('H1 traces: row=-1 column=+1 half_turn=-1')

if __name__ == '__main__':
    verify()
