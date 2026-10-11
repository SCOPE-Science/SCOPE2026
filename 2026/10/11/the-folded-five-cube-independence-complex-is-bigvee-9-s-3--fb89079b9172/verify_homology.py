#!/usr/bin/env python3
"""Independent face generator and mod-two simplicial homology check."""
from collections import Counter


def main():
    # Use even-weight binary five-tuples; edges connect distance-four pairs.
    labels = [x for x in range(32) if x.bit_count() % 2 == 0]
    faces = {k: [] for k in range(5)}

    def extend(chosen, candidates):
        if chosen:
            faces[len(chosen) - 1].append(tuple(chosen))
        for pos, v in enumerate(candidates):
            remaining = [w for w in candidates[pos+1:]
                         if (labels[w] ^ labels[v]).bit_count() != 4]
            extend(chosen + [v], remaining)

    extend([], list(range(16)))
    assert [len(faces[k]) for k in range(5)] == [16, 80, 160, 120, 16]
    assert len(set(sum(faces.values(), []))) == 392

    def binary_rank(columns):
        pivot = {}
        for x in columns:
            while x:
                high = x.bit_length() - 1
                if high not in pivot:
                    pivot[high] = x
                    break
                x ^= pivot[high]
        return len(pivot)

    ranks = []
    for k in range(1, 5):
        rows = {simplex: i for i, simplex in enumerate(faces[k-1])}
        columns = []
        for upper in faces[k]:
            col = 0
            for i in range(len(upper)):
                lower = upper[:i] + upper[i+1:]
                col ^= 1 << rows[lower]
            columns.append(col)
        ranks.append(binary_rank(columns))
    assert ranks == [15, 65, 95, 16]
    reduced_betti = [len(faces[0]) - 1 - ranks[0]]
    for k in range(1, 4):
        reduced_betti.append(len(faces[k]) - ranks[k-1] - ranks[k])
    reduced_betti.append(len(faces[4]) - ranks[3])
    assert reduced_betti == [0, 0, 0, 9, 0]
    assert sum((-1)**k * len(faces[k]) for k in range(5)) == -8
    print('CLEBSCH_HOMOLOGY_VERIFIED: face_vector=[16,80,160,120,16] '
          'boundary_ranks_F2=[15,65,95,16] reduced_Betti_F2=[0,0,0,9,0]')


if __name__ == '__main__':
    main()
