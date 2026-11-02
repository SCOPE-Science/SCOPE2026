#!/usr/bin/env python3
"""Standalone integer verification of dyadic Thue--Morse multiplication statistics."""

MIXED = ((1, 1, 0), (-1, 0, -1), (0, 1, 1))
SINGLE = ((1, -1, 0), (-1, 0, 1), (0, 1, -1))
TERMINAL = (1, -1, -1)


def multiply_row(row, matrix):
    return tuple(sum(row[i] * matrix[i][j] for i in range(3)) for j in range(3))


def evaluate(row):
    return sum(x * y for x, y in zip(row, TERMINAL))


def sign(x):
    return 1 if x.bit_count() % 2 == 0 else -1


def main():
    row_mixed = row_single = (1, 0, 0)
    mixed_values = []
    single_values = []
    sample_count = 0
    for r in range(18):
        c = evaluate(row_mixed)
        u = evaluate(row_single)
        mixed_values.append(c)
        single_values.append(u)
        direct_c = sum(sign(n) * sign(3*n) for n in range(1 << r))
        direct_u = sum(sign(3*n) for n in range(1 << r))
        assert (c, u) == (direct_c, direct_u), (r, c, u, direct_c, direct_u)
        sample_count += 1 << r
        if r:
            assert u == (2 * 3 ** ((r-1)//2) if r%2 else 4 * 3 ** (r//2-1))
            direct = {(a,b):0 for a in (1,-1) for b in (1,-1)}
            for n in range(1 << r):
                direct[sign(n), sign(3*n)] += 1
            for a in (1,-1):
                for b in (1,-1):
                    assert direct[a,b] == ((1 << r) + b*u + a*b*c)//4
                    assert ((1 << r) + b*u + a*b*c) % 4 == 0
        if r >= 3:
            assert c == 2*mixed_values[-2] - 3*mixed_values[-3] + 2*mixed_values[-4]
        if r >= 3:
            assert u == 3*single_values[-3]
        row_mixed = multiply_row(row_mixed, MIXED)
        row_single = multiply_row(row_single, SINGLE)
    print('PASS: 18 dyadic levels,', sample_count, 'complete input evaluations, all four parity cells.')
    print('PASS: mixed recurrence, rarefied sum formulas, and two-step recurrence.')
    print('C_r=', mixed_values)
    print('U_r=', single_values)


if __name__ == '__main__':
    main()
