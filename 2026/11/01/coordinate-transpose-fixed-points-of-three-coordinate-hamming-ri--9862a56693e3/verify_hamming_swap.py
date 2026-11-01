"""Independent finite checks for the coordinate-swap fixed Rips complexes.

Run with Python 3, standard library only. This program computes all orbit
unions directly in the original Hamming metric, rather than assuming the
adjacency classification used in the proof. It independently computes
simplicial boundary ranks over the field of two elements.
"""
from collections import defaultdict
from itertools import product


def hamming(u, v):
    return sum(x != y for x, y in zip(u, v))


def orbits(q):
    points = list(product(range(q), repeat=3))
    remaining = set(points)
    answer = []
    while remaining:
        x = min(remaining)
        swapped = (x[1], x[0], x[2])
        orb = frozenset((x, swapped))
        remaining.difference_update(orb)
        answer.append(orb)
    return answer


def adjacency(q, radius):
    groups = [o for o in orbits(q) if all(hamming(x, y) <= radius for x in o for y in o)]
    n = len(groups)
    masks = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if all(hamming(x, y) <= radius for x in groups[i] for y in groups[j]):
                masks[i] |= 1 << j
                masks[j] |= 1 << i
    return groups, masks


def faces(neighbors):
    output = defaultdict(list)
    def visit(face, available):
        if face:
            output[face.bit_count()].append(face)
        while available:
            bit = available & -available
            available ^= bit
            visit(face | bit, available & neighbors[bit.bit_length() - 1])
    visit(0, (1 << len(neighbors)) - 1)
    return output


def rank_mod_two(columns):
    basis = {}
    for c in columns:
        while c:
            pivot = c.bit_length() - 1
            if pivot in basis:
                c ^= basis[pivot]
            else:
                basis[pivot] = c
                break
    return len(basis)


def reduced_betti_two(faces_by_size):
    largest = max(faces_by_size, default=0)
    ranks = {1: int(bool(faces_by_size.get(1)))}
    for k in range(2, largest + 1):
        previous = {face: idx for idx, face in enumerate(faces_by_size[k - 1])}
        columns = []
        for f in faces_by_size[k]:
            boundary = 0
            bits = f
            while bits:
                bit = bits & -bits
                bits -= bit
                boundary ^= 1 << previous[f ^ bit]
            columns.append(boundary)
        ranks[k] = rank_mod_two(columns)
    return {
        k - 1: len(faces_by_size[k]) - ranks[k] - ranks.get(k + 1, 0)
        for k in range(1, largest + 1)
        if len(faces_by_size[k]) - ranks[k] - ranks.get(k + 1, 0)
    }


def theoretical_edges(groups):
    typed = []
    for orb in groups:
        first = min(orb)
        z = first[2]
        letters = frozenset((first[0], first[1]))
        typed.append((z, letters))
    edges = []
    for i, (z, a) in enumerate(typed):
        for j, (w, b) in enumerate(typed):
            if i >= j:
                continue
            adj = (z == w or
                   (len(a) == len(b) == 1 and a == b) or
                   (len(a) != len(b) and bool(a & b)))
            if adj:
                edges.append((i, j))
    return set(edges)


def main():
    checked = {}
    for q in (2, 3, 4):
        groups, masks = adjacency(q, 2)
        n = q * q * (q + 1) // 2
        assert len(groups) == n
        direct = {(i, j) for i in range(n) for j in range(i + 1, n) if masks[i] >> j & 1}
        assert direct == theoretical_edges(groups)
        fs = faces(masks)
        betti = reduced_betti_two(fs)
        # Independently reconstruct the covering core as a union of metric-orbit
        # simplices and verify the bridge-triangle classification.
        core_masks = []
        for z in range(q):
            core_masks.append(sum(1 << i for i, orb in enumerate(groups)
                                  if min(orb)[2] == z))
        for a in range(q):
            for z in range(q):
                core_masks.append(sum(1 << i for i, orb in enumerate(groups)
                                      if (len(orb) == 1 and min(orb)[0] == a)
                                      or (len(orb) == 2 and min(orb)[2] == z
                                          and a in (min(orb)[0], min(orb)[1]))))
        core = defaultdict(list)
        outside = defaultdict(list)
        for size, members in fs.items():
            for face in members:
                if any(face & ~cm == 0 for cm in core_masks):
                    core[size].append(face)
                else:
                    outside[size].append(face)
        assert set(outside) == {3} and len(outside[3]) == q*q*(q-1)**2//2
        assert reduced_betti_two(core) == {1:(q-1)**2}
        expected = (q - 1)**2 * (q*q - 2) // 2
        assert betti == {2: expected}, (q, betti, expected)
        if q == 2:
            assert [len(fs[k]) for k in sorted(fs)] == [6, 12, 8]
        if q == 3:
            assert [len(fs[k]) for k in sorted(fs)] == [18, 90, 153, 90, 27, 3]
        if q == 4:
            assert [len(fs[k]) for k in sorted(fs)] == [40, 348, 1000, 1372, 1344, 952, 496, 180, 40, 4]
        for radius, expected_component_count in ((0, q*q), (1, q)):
            gg, nn = adjacency(q, radius)
            assert len(gg) == q*q
            fsmall = faces(nn)
            hom = reduced_betti_two(fsmall)
            assert hom == ({0: expected_component_count - 1})
        all_groups, complete_masks = adjacency(q, 3)
        assert len(all_groups) == n
        assert all(mask.bit_count() == n - 1 for mask in complete_masks)
        checked[q] = expected
    print('VERIFY_OK', checked)


if __name__ == '__main__':
    main()
