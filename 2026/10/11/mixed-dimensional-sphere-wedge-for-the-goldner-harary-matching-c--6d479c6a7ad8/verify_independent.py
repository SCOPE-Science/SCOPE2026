#!/usr/bin/env python3
"""Independent exact combinatorial enumeration and mod-2 chain calculation.
Standard-library only. Does not read the discrete-Morse certificate.
"""
from itertools import combinations
from collections import defaultdict, Counter


def main():
    # An independently defined Kleetope of the triangular dipyramid.
    bottom = {frozenset(pair) for pair in combinations((0, 1, 2), 2)}
    bottom |= {frozenset((u, v)) for u in range(3) for v in (3, 4)}
    triangular_faces = ((0, 1, 3), (1, 2, 3), (0, 2, 3),
                        (0, 1, 4), (1, 2, 4), (0, 2, 4))
    for i, face in enumerate(triangular_faces):
        bottom |= {frozenset((5 + i, old)) for old in face}
    E = sorted(tuple(sorted(pair)) for pair in bottom)
    assert len(E) == 27
    simplices = defaultdict(list)
    for k in range(1, 6):
        for S in combinations(range(27), k):
            endpts = [w for index in S for w in E[index]]
            if len(set(endpts)) == 2 * k:
                simplices[k].append(S)
    counts = tuple(len(simplices[i]) for i in range(1, 6))
    assert counts == (27, 219, 613, 510, 72)
    ranks = []
    for k in range(2, 6):
        lower_idx = {face: i for i, face in enumerate(simplices[k - 1])}
        pivots = {}
        rank = 0
        for upper in simplices[k]:
            column = 0
            for i in range(k):
                column ^= 1 << lower_idx[upper[:i] + upper[i + 1:]]
            while column:
                position = column.bit_length() - 1
                if position in pivots:
                    column ^= pivots[position]
                else:
                    pivots[position] = column
                    rank += 1
                    break
        ranks.append(rank)
    assert ranks == [26, 193, 390, 72]
    f0, f1, f2, f3, f4 = counts
    assert f0 - f1 + f2 - f3 + f4 == -17
    assert f2 - ranks[1] - ranks[2] == 30
    assert f3 - ranks[2] - ranks[3] == 48
    print('VERIFIED independently: face vector', counts)
    print('Boundary ranks mod 2:', tuple(ranks))
    print('Reduced mod-2 Betti numbers: 30 in degree 2, 48 in degree 3.')


if __name__ == '__main__':
    main()
