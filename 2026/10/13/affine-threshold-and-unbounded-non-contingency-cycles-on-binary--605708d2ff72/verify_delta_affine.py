#!/usr/bin/env python3
"""Finite, independently reproducible checks for the stated non-contingency dynamics.
The mathematical assertions for all finite frames are established in RESULT.md,
not by extrapolating this finite regression.
"""
from itertools import combinations, product


def successors(n):
    return tuple(r for r in range(1 << n) if r.bit_count() <= 2)


def direct_delta(rows, valuation):
    output = 0
    for w, row in enumerate(rows):
        y = valuation & row
        if y == 0 or y == row:
            output |= 1 << w
    return output


def b_rows(rows):
    return tuple(row if row.bit_count() == 2 else 0 for row in rows)


def action(B, valuation):
    return sum(((row & valuation).bit_count() & 1) << w
               for w, row in enumerate(B))


def product_matrix(A, B):
    return tuple(__import__("functools").reduce(int.__xor__, (B[j] for j in range(len(B)) if (r >> j) & 1), 0) for r in A)


def rank(matrix):
    basis = {}
    for r in matrix:
        while r:
            j = r.bit_length() - 1
            if j in basis:
                r ^= basis[j]
            else:
                basis[j] = r
                break
    return len(basis)


def fitting_index(B):
    n = len(B)
    k = 1
    current = B
    while True:
        nxt = product_matrix(current, B)
        if rank(current) == rank(nxt):
            return k
        current, k = nxt, k + 1
        assert k <= n


def repeated_powers(B):
    seen = {}
    current = B
    k = 1
    while current not in seen:
        seen[current] = k
        current = product_matrix(current, B)
        k += 1
        assert k <= 2 ** (len(B) ** 2) + 1
    return seen[current], k - seen[current]


def local_normal_degree(r):
    # Mobius-transform truth table of non-contingency, on r distinct successors.
    truth = [int(x == 0 or x == (1 << r) - 1) for x in range(1 << r)]
    for j in range(r):
        for x in range(1 << r):
            if x & (1 << j):
                truth[x] ^= truth[x ^ (1 << j)]
    return max((x.bit_count() for x, c in enumerate(truth) if c), default=-1)


def test_all_frames():
    frames = 0
    valuation_tests = 0
    for n in range(1, 5):
        for rows in product(successors(n), repeat=n):
            frames += 1
            B = b_rows(rows)
            a, p = repeated_powers(B)
            assert a == fitting_index(B), (n, rows, a, p)
            for x in range(1 << n):
                valuation_tests += 1
                assert direct_delta(rows, x) == ((1 << n) - 1) ^ action(B, x)
                state = x
                matrix = B
                for k in range(1, a + 2 * p + 2):
                    state = direct_delta(rows, state)
                    assert state == (((1 << n) - 1) ^ action(matrix, x)), (n, rows, x, k)
                    matrix = product_matrix(matrix, B)
        print(f"all_frames_n={n} passed")
    assert frames == sum(len(successors(n)) ** n for n in range(1, 5))
    print(f"frame_count={frames} valuation_count={valuation_tests}")


def test_sharpness_and_long_cycles():
    for r in range(7):
        expected = 0 if r <= 1 else r - 1
        assert local_normal_degree(r) == expected, (r, local_normal_degree(r))
    for n in (1, 2):
        for rows in product(successors(n), repeat=n):
            _, period = repeated_powers(b_rows(rows))
            assert period == 1
    exact_periods = {3: 3, 5: 15, 7: 7, 9: 63}
    for n, period in exact_periods.items():
        cycle = tuple((1 << i) | (1 << ((i + 1) % n)) for i in range(n))
        a, p = repeated_powers(cycle)
        assert (a, p) == (1, period)
        assert p >= n - 1
        print(f"odd_cycle_n={n} preperiod={a} period={p}")


if __name__ == '__main__':
    test_all_frames()
    test_sharpness_and_long_cycles()
    print('VERIFY_OK')
