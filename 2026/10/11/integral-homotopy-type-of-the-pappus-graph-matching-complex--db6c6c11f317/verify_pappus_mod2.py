#!/usr/bin/env python3
"""Independent mod-2 chain check for the Pappus matching complex.
Only the Python standard library is used. This check does not prove the
integral homotopy type; that is handled by verify_pappus_integral.py.
"""
from collections import Counter


def main():
    n = 18
    jumps = [5, 7, -7, 7, -7, -5] * 3
    edges = set(tuple(sorted((i, (i+1) % n))) for i in range(n))
    edges.update(tuple(sorted((i, (i+j) % n))) for i, j in enumerate(jumps))
    edges = sorted(edges)
    groups = [[] for _ in range(9)]
    def enumerate_subsets(first, used_vertices, simplex):
        if simplex:
            groups[len(simplex)-1].append(sum(1 << i for i in simplex))
        for i in range(first, len(edges)):
            u, v = edges[i]
            if not (used_vertices & ((1 << u) | (1 << v))):
                enumerate_subsets(i+1, used_vertices | (1 << u) | (1 << v), simplex+[i])
    enumerate_subsets(0, 0, [])
    counts = [len(x) for x in groups]
    assert counts == [27, 297, 1719, 5643, 10557, 10737, 5319, 1026, 42]
    # Direct binary rank using exact Python arbitrary-precision bit vectors.
    ranks = [1]
    for dimension in range(1, 9):
        row_number = {cell: i for i, cell in enumerate(groups[dimension-1])}
        pivots = {}
        for cell in groups[dimension]:
            bits = cell
            vector = 0
            while bits:
                bit = bits & -bits
                vector ^= 1 << row_number[cell ^ bit]
                bits ^= bit
            while vector:
                leading = vector.bit_length() - 1
                if leading not in pivots:
                    pivots[leading] = vector
                    break
                vector ^= pivots[leading]
        ranks.append(len(pivots))
    assert ranks == [1,26,271,1448,4195,6362,4335,984,42], ranks
    betti = [counts[i] - ranks[i] - (ranks[i+1] if i < 8 else 0)
             for i in range(9)]
    assert betti == [0,0,0,0,0,40,0,0,0], betti
    assert sum((-1)**i * counts[i] for i in range(9)) == -39
    print('MOD2_VERIFY_OK faces_nonempty={} ranks={} reduced_betti={}'.format(
          sum(counts), ranks, betti))

if __name__ == '__main__':
    main()
