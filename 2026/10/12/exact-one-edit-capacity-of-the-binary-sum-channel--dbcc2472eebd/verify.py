#!/usr/bin/env python3
"""Reproducible finite checks of the sum-channel one-edit fiber theorem.

This script does not replace the proof for arbitrary row and frame counts.
All algorithms use Python's standard library and integer bit arithmetic.
"""
from itertools import combinations, product

CODE8 = (0, 7, 25, 42, 63, 85, 90, 99, 109, 112,
         142, 147, 161, 182, 184, 194, 201, 220, 228, 251)


def parity(x):
    return x.bit_count() % 2


def hamming(x, y):
    return (x ^ y).bit_count()


def verify_classical_code(code, length):
    assert len(code) == len(set(code))
    assert all(0 <= x < 1 << length for x in code)
    assert all(hamming(x, y) >= 3 for x, y in combinations(code, 2))


def max_one_error_code(length):
    """Exact backtracking independent number for length <= 4."""
    N = 1 << length
    adj = [0] * N
    for i in range(N):
        adj[i] = sum(1 << j for j in range(N) if j != i and hamming(i, j) <= 2)

    def dfs(candidates, size):
        nonlocal best
        if size + candidates.bit_count() <= best:
            return
        if not candidates:
            best = max(best, size)
            return
        v = (candidates & -candidates).bit_length() - 1
        rest = candidates & ~(1 << v)
        dfs(rest & ~adj[v], size + 1)
        dfs(rest, size)

    best = 0
    dfs((1 << N) - 1, 0)
    return best


def plus_matrix(input_rows, n):
    last = 0
    for row in input_rows:
        last ^= row
    return tuple(input_rows) + (last,)


def code_matrices(length, frame, code):
    for rows in product(range(1 << frame), repeat=length):
        bits = 0
        for i, row in enumerate(rows):
            bits |= parity(row) << i
        if bits in code:
            yield rows


def edit_outcomes(aug_rows, frame):
    """Explicit words with at most one substitution/insertion/deletion."""
    rows = tuple(tuple((x >> j) & 1 for j in range(frame)) for x in aug_rows)
    outputs = {rows}
    for i, row in enumerate(rows):
        for j in range(frame):
            new = list(rows)
            r = list(row)
            r[j] ^= 1
            new[i] = tuple(r)
            outputs.add(tuple(new))
        for j in range(frame):
            new = list(rows)
            new[i] = row[:j] + row[j+1:]
            outputs.add(tuple(new))
        for j in range(frame + 1):
            for b in (0, 1):
                new = list(rows)
                new[i] = row[:j] + (b,) + row[j:]
                outputs.add(tuple(new))
    return outputs


def verify_one_edit_code(length, frame, c0):
    verify_classical_code(c0, length)
    seen = {}
    count = 0
    for rows in code_matrices(length, frame, c0):
        count += 1
        for outcome in edit_outcomes(plus_matrix(rows, frame), frame):
            prior = seen.get(outcome)
            assert prior is None or prior == rows, (length, frame, rows, prior)
            seen[outcome] = rows
    assert count == len(c0) * 2 ** (length * (frame - 1))
    return count, len(seen)


def verify_fiber(length):
    for a in range(1 << length):
        for b in range(1 << length):
            if a != b:
                wt = hamming(a, b)
                augmented_wt = wt + parity(a ^ b)
                assert (augmented_wt == 2) == (wt in (1, 2))


def main():
    for ell in range(2, 9):
        verify_fiber(ell)
    small = {2: (0,), 3: (0, 7), 4: (0, 7)}
    for ell, C0 in small.items():
        assert max_one_error_code(ell) == len(C0)
    for ell, n, C0 in ((2, 3, small[2]), (3, 4, small[3]), (4, 2, small[4])):
        nwords, noutcomes = verify_one_edit_code(ell, n, C0)
        print('EDIT_BALLS', ell, n, nwords, noutcomes)
    verify_classical_code(CODE8, 8)
    assert len(CODE8) == 20
    assert len(CODE8) > 2 ** (8 - 4)
    print('NONLINEAR_GAIN', len(CODE8), 'versus', 16)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
