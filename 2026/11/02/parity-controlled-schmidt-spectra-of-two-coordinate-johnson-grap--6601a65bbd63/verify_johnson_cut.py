#!/usr/bin/env python3
"""Exact GF(2) checker for two-coordinate parity cuts of Johnson graph states.
All calculations use integer bitsets and the Python standard library.
"""
from itertools import combinations
from math import comb


def rank_bits(rows):
    pivots = {}
    for row in rows:
        while row:
            lead = row.bit_length() - 1
            if lead in pivots:
                row ^= pivots[lead]
            else:
                pivots[lead] = row
                break
    return len(pivots)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def cut_matrix(n, k):
    vertices = [sum(1 << i for i in s) for s in combinations(range(n), k)]
    # Distinguished coordinates are positions zero and one.
    left = [v for v in vertices if (v & 3).bit_count() in (0, 2)]
    right = [v for v in vertices if (v & 3).bit_count() == 1]
    rows = []
    for a in left:
        row = 0
        for j, b in enumerate(right):
            if (a ^ b).bit_count() == 2:
                row |= 1 << j
        rows.append(row)
    return left, right, rows


def expected(n, k):
    N, r = n - 2, k - 1
    return choose(N, r) - (choose(N - 2, r - 1) if n % 2 == 0 else 0)


def check_ranks():
    total = 0
    for n in range(4, 14):
        for k in range(1, n):
            A, B, rows = cut_matrix(n, k)
            got, want = rank_bits(rows), expected(n, k)
            assert got == want, (n, k, got, want)
            assert len(A) == choose(n-2, k) + choose(n-2, k-2)
            assert len(B) == 2*choose(n-2, k-1)
            total += 1
    return total


def state_integer_density(n, k):
    """Build graph state amplitudes, trace out B directly, and check flat spectrum.

    A non-normalized reduced matrix R is computed directly from all signs of
    the circuit CZ gates. The normalized matrix is R / 2**|V|.
    """
    A, B, _ = cut_matrix(n, k)
    vertices = A + B
    size = len(vertices)
    edges = [(i, j) for i in range(size) for j in range(i+1, size)
             if (vertices[i] ^ vertices[j]).bit_count() == 2]
    na, nb = len(A), len(B)
    signs = []
    for x in range(1 << na):
        row = []
        for y in range(1 << nb):
            bits = x | (y << na)
            parity = 0
            for i, j in edges:
                parity ^= (bits >> i & 1) & (bits >> j & 1)
            row.append(-1 if parity else 1)
        signs.append(row)
    # Partial trace R_{xz} = sum_y psi(x,y) psi(z,y), without normalization.
    R = [[sum(signs[x][y]*signs[z][y] for y in range(1 << nb))
          for z in range(1 << na)] for x in range(1 << na)]
    rank = expected(n, k)
    # Verify R**2 = 2**(size-rank)*R, implying exact spectrum {0,2**-rank}.
    factor = 1 << (size-rank)
    for x in range(1 << na):
        for z in range(1 << na):
            lhs = sum(R[x][t]*R[t][z] for t in range(1 << na))
            assert lhs == factor * R[x][z], (n, k, x, z)
    assert sum(R[x][x] for x in range(1 << na)) == 1 << size
    return size, rank


def main():
    nr = check_ranks()
    checks = [(4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3), (5, 4)]
    stats = [(n, k, *state_integer_density(n, k)) for n,k in checks]
    print('CUT_RANK_TESTS', nr)
    print('EXACT_GRAPH_STATE_DENSITY_TESTS', len(stats))
    for n, k, nqubits, entropy in stats:
        print(f'  J({n},{k}): {nqubits} qubits, entropy {entropy} bits, spectrum flat')
    print('VERIFY_OK')

if __name__ == '__main__': main()
