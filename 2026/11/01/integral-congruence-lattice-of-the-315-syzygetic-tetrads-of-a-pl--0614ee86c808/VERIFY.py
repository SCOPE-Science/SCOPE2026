#!/usr/bin/env python3
"""Exact integer verifier for the syzygetic-tetrad incidence lattice.

Requires only Python 3's standard library.  Coordinates are integers 0..63:
low bits 0,1,2 represent one Lagrangian, high bits 3,4,5 the other.
The 28 odd theta characteristics and the 315 tetrads are lexicographic.
"""
from itertools import combinations


def q(v):
    return sum(((v >> i) & 1) * ((v >> (i + 3)) & 1)
               for i in range(3)) & 1


def determinant_bareiss(rows):
    """Exact fraction-free determinant with integral pivoting."""
    a = [list(row) for row in rows]
    n = len(a)
    assert all(len(row) == n for row in a)
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            aik = a[i][k]
            for j in range(k + 1, n):
                num = a[i][j] * pivot - aik * a[k][j]
                assert num % previous == 0
                a[i][j] = num // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[n - 1][n - 1]


def binary_rank(rows):
    pivots = {}
    for val in rows:
        while val:
            k = val.bit_length() - 1
            if k not in pivots:
                pivots[k] = val
                break
            val ^= pivots[k]
    return len(pivots)


def main():
    odd = tuple(v for v in range(64) if q(v))
    assert len(odd) == 28
    # Each four-set with XOR zero is an affine isotropic 2-plane consisting
    # of four odd characteristics, hence a syzygetic tetrad.
    tetrads = tuple(t for t in combinations(odd, 4)
                    if t[0] ^ t[1] ^ t[2] ^ t[3] == 0)
    assert len(tetrads) == 315
    counts = [sum(v in t for t in tetrads) for v in odd]
    assert set(counts) == {45}
    pair_counts = [sum((u in t and v in t) for t in tetrads)
                   for u, v in combinations(odd, 2)]
    assert set(pair_counts) == {5}
    print('ODD=28; SYZYGETIC_TETRADS=315; DESIGN=2-(28,4,5)')

    # The map from free bitangent vectors to Z/4 + (Z/2)^6 is
    # total mod 4 together with the six binary theta-coordinate moments.
    assert all(len(t) == 4 and (t[0] ^ t[1] ^ t[2] ^ t[3]) == 0
               for t in tetrads)
    augment = [1 | (v << 1) for v in odd]
    assert binary_rank(augment) == 7
    print('CONGRUENCES_OK: total modulo 4 and six independent modulo-2 moments')
    print('CONGRUENCE_INDEX=256')

    # Zero-based indices in lexicographically sorted combinations(odd,4),
    # with the XOR-zero restriction.  This is a 28-column integral witness.
    witness_indices = (122, 307, 8, 149, 220, 93, 262, 49,
                       259, 135, 256, 4, 187, 285, 201, 15,
                       69, 123, 227, 58, 240, 63, 218, 222,
                       51, 202, 46, 82)
    assert len(witness_indices) == len(set(witness_indices)) == 28
    witness = [[int(v in tetrads[j]) for j in witness_indices]
               for v in odd]
    det = determinant_bareiss(witness)
    assert det == -256, det
    print('EXPLICIT_28_BY_28_MINOR=-256')

    # Inclusion L <= kernel, a determinant-256 sublattice of L,
    # and kernel index 256 force equality of the two integral lattices.
    print('INTEGER_SPAN_EQUALS_CONGRUENCE_KERNEL')
    print('SMITH=1^21,2^6,4; COKERNEL=Z/4+(Z/2)^6')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
