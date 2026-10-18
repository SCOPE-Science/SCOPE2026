#!/usr/bin/env python3
"""Optional exact integer Smith cross-check for three small rectangular boards.

Requires SymPy. The theorem itself is proved for every board via cohomology,
so this finite integer check is corroborative rather than a proof for all cases.
"""
from itertools import combinations
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def check_board(m, n):
    N = m*n
    neighbors = [
        {x*n+y for x in range(m) for y in range(n) if (x == i) != (y == j)}
        for i in range(m) for j in range(n)
    ]
    triangles = sorted({tuple(t) for subset in neighbors for t in combinations(sorted(subset), 3)})
    edges = list(combinations(range(1, N), 2))
    edge_index = {edge:i for i, edge in enumerate(edges)}
    entries = {}
    for column, (a,b,c) in enumerate(triangles):
        for pair, sign in (((b,c),1), ((a,c),-1), ((a,b),1)):
            if pair[0] != 0:
                entries[edge_index[pair], column] = sign
    matrix = SparseMatrix(len(edges), len(triangles), entries)
    smith = smith_normal_form(matrix, domain=ZZ)
    invariants = [abs(int(smith[i,i])) for i in range(min(matrix.shape)) if smith[i,i]]
    torsion = [x for x in invariants if x > 1]
    free = len(edges) - len(invariants)
    expected = {(3,3):(2,[]), (3,4):(1,[]), (4,4):(0,[2])}[(m,n)]
    assert (free, torsion) == expected
    print(f'{m}x{n}: rank={len(invariants)}, free={free}, torsion_factors={torsion}, verified')


if __name__ == '__main__':
    for board in [(3,3),(3,4),(4,4)]:
        check_board(*board)
    print('ROOK_INTEGRAL_SMITH_CHECK_OK')
