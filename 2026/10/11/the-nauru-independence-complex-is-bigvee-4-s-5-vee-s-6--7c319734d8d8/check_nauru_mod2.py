#!/usr/bin/env python3
"""Independent all-degree mod-two chain calculation for GP(12,5).

Enumerates independent subsets by include/exclude branching and computes
Gaussian-elimination ranks, including the reduced augmentation boundary.
"""
from collections import Counter, defaultdict

N = 24


def adjacent(a, b):
    if a == b:
        return False
    if a < 12 and b < 12:
        return (a - b) % 12 in (1, 11)
    if a >= 12 and b >= 12:
        return (a - b) % 12 in (5, 7)
    return a % 12 == b % 12


def independent_faces():
    neighbors = [sum((1 << j) for j in range(N) if adjacent(i, j)) for i in range(N)]
    assert all(x.bit_count() == 3 for x in neighbors)
    result = []

    def dfs(available, chosen):
        if available == 0:
            result.append(chosen)
            return
        bit = available & -available
        i = bit.bit_length() - 1
        dfs(available ^ bit, chosen)
        dfs((available ^ bit) & ~neighbors[i], chosen | bit)

    dfs((1 << N) - 1, 0)
    assert len(result) == 35219 and len(set(result)) == len(result)
    return result


def rank_two(columns):
    # Each integer encodes a column vector in the basis of lower-dimensional faces.
    pivots = {}
    for col in columns:
        while col:
            lead = (col & -col).bit_length() - 1
            if lead in pivots:
                col ^= pivots[lead]
            else:
                pivots[lead] = col
                break
    return len(pivots)


def main():
    faces = independent_faces()
    by_dimension = defaultdict(list)
    for face in faces:
        by_dimension[face.bit_count() - 1].append(face)
    for d in by_dimension:
        by_dimension[d].sort()
    expected = (24, 240, 1304, 4212, 8328, 10036,
                7176, 2964, 752, 156, 24, 2)
    assert tuple(len(by_dimension[d]) for d in range(12)) == expected
    expected_boundary_ranks = (1, 23, 217, 1087, 3125, 5203,
                               4829, 2346, 618, 134, 22, 2)
    ranks = {}
    for d in range(12):
        lower_index = {f: j for j, f in enumerate(by_dimension[d-1])}
        columns = []
        for f in by_dimension[d]:
            c = 0
            bits = f
            while bits:
                bit = bits & -bits
                bits -= bit
                c ^= 1 << lower_index[f ^ bit]
            columns.append(c)
        ranks[d] = rank_two(columns)
    assert tuple(ranks[d] for d in range(12)) == expected_boundary_ranks
    homology = {d:len(by_dimension[d]) - ranks[d] - ranks.get(d+1, 0) for d in range(12)}
    assert {d:r for d,r in homology.items() if r} == {5:4, 6:1}
    print('all-degree mod-two boundary ranks:', expected_boundary_ranks)
    print('reduced mod-two Betti ranks:', {5:4, 6:1})
    print('NAURU_MOD2_VERIFY_OK')


if __name__ == '__main__':
    main()
