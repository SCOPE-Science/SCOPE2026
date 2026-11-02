#!/usr/bin/env python3
"""Independent finite checks for an exact algebraic-immunity/nonlinearity law.

Only Python's standard library is needed. Truth-table bit i is the value at
input i in little-endian binary coordinates. All assertions are exact.
"""
from collections import Counter
from itertools import combinations

NUM_Y = 16
NUM_X = 32
FOUR_AFFINES = tuple(sum((((c ^ ((a & i).bit_count() & 1)) & 1) << i) for i in range(16)) for c in (0, 1) for a in range(16))
MONOMIALS = tuple(m for m in range(32) if m.bit_count() <= 2)
CUBIC_QUARTIC = (7, 11, 13, 14, 15)


def linear_rank(rows):
    basis = {}
    for value in rows:
        while value:
            bit = value.bit_length() - 1
            if bit in basis:
                value ^= basis[bit]
            else:
                basis[bit] = value
                break
    return len(basis)


def nl4(truth):
    return min((truth ^ affine).bit_count() for affine in FOUR_AFFINES)


def truth_of_s(points):
    return sum(1 << p for p in points)


def anf_coefficients(truth):
    coeffs = [(truth >> i) & 1 for i in range(16)]
    for b in range(4):
        for mask in range(16):
            if mask & (1 << b):
                coeffs[mask] ^= coeffs[mask ^ (1 << b)]
    return coeffs


def reduced_matrix(truth):
    mat = []
    for mon in CUBIC_QUARTIC:
        row = 0
        for j, b in enumerate((None, 0, 1, 2, 3)):
            values = truth if b is None else sum(((truth >> x) & 1) * ((x >> b) & 1) << x for x in range(16))
            row |= anf_coefficients(values)[mon] << j
        mat.append(row)
    return mat


def graph_restriction_rank(truth, graph_one):
    rows = []
    for y in range(16):
        x0 = ((truth >> y) & 1) ^ graph_one
        state = (y << 1) | x0
        rows.append(sum((1 << j) for j, mon in enumerate(MONOMIALS) if (state & mon) == mon))
    return linear_rank(rows)


def full_cycle(truth):
    current = 0
    visited = 0
    for _ in range(32):
        if visited & (1 << current):
            return False
        visited |= 1 << current
        y = current >> 1
        current = y | ((((current & 1) ^ ((truth >> y) & 1))) << 4)
    return current == 0


def main():
    reps = ((0,), (0, 1, 2), (0, 1, 2, 4, 8))
    expected_rows = (
        (0b00001, 0b00001, 0b00001, 0b00001, 0b00001),
        (0b00111, 0b00111, 0b00010, 0b00100, 0b00111),
        (0b01110, 0b10110, 0b11010, 0b11100, 0b11111),
    )
    for k, pts in enumerate(reps):
        rows = reduced_matrix(truth_of_s(pts))
        assert tuple(rows) == expected_rows[k], (pts, rows, expected_rows[k])
        assert linear_rank(rows) == len(pts), (pts, rows)

    # Independent definition-level comparison at all 32768 odd-weight truth tables.
    joint = Counter()
    maxcycle = Counter()
    for truth in range(1 << 16):
        if truth.bit_count() % 2 == 0:
            continue
        nonlinearity = nl4(truth)
        z = graph_restriction_rank(truth, 0)
        o = graph_restriction_rank(truth, 1)
        assert z == o == 11 + nonlinearity, (truth, nonlinearity, z, o)
        reduced = reduced_matrix(truth)
        assert linear_rank(reduced) == nonlinearity
        joint[(nonlinearity, 16-z)] += 1
        if full_cycle(truth):
            maxcycle[(2 * nonlinearity, 16-z)] += 1

    assert joint == {(1, 4): 512, (3, 2): 17920, (5, 0): 14336}, joint
    assert maxcycle == {(2, 4): 24, (6, 2): 1128, (10, 0): 896}, maxcycle
    print('ODD_FEEDBACK_NL_ANNIHILATOR', sorted(joint.items()))
    print('DEBRUIJN_5_NL_ANNIHILATOR', sorted(maxcycle.items()))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
