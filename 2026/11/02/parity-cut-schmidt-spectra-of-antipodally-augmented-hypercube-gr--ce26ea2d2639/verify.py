#!/usr/bin/env python3
"""Exact binary cut-rank and small-state spectral checks for antipodal cube graph states."""
from itertools import combinations
from math import comb


def binary_rank(rows):
    pivots = {}
    for row in rows:
        x = row
        while x:
            j = x.bit_length() - 1
            if j in pivots:
                x ^= pivots[j]
            else:
                pivots[j] = x
                break
    return len(pivots)


def expected(n, mask):
    t = mask.bit_count()
    assert n >= 3 and 1 <= t <= n
    if t == n and n % 2:
        return 2 ** (n - 2) - 2 ** ((n - 3) // 2)
    return 2 ** (n - 2)


def cut_rows(n, mask):
    all_bits = (1 << n) - 1
    left = [u for u in range(1 << n) if (u & mask).bit_count() % 2 == 0]
    right = [v for v in range(1 << n) if (v & mask).bit_count() % 2]
    column = {v: j for j, v in enumerate(right)}
    out = []
    for u in left:
        row = 0
        for i in range(n):
            v = u ^ (1 << i)
            if v in column:
                row ^= 1 << column[v]
        v = u ^ all_bits
        if v in column:
            row ^= 1 << column[v]
        out.append(row)
    return out


def direct_spectrum(n, mask):
    import numpy as np
    N = 1 << n
    all_bits = N - 1
    left = [u for u in range(N) if (u & mask).bit_count() % 2 == 0]
    right = [u for u in range(N) if (u & mask).bit_count() % 2]
    a_dim = 1 << len(left)
    b_dim = 1 << len(right)
    if N > 16:
        raise ValueError('Use n=3 or n=4 for full state-vector verification')
    edges = set()
    for u in range(N):
        for i in range(n):
            v = u ^ (1 << i)
            edges.add(tuple(sorted((u, v))))
        v = u ^ all_bits
        edges.add(tuple(sorted((u, v))))
    edges = sorted(edges)
    left_bits = [1 << v for v in left]
    right_bits = [1 << v for v in right]
    amplitudes = np.zeros((a_dim, b_dim), dtype=np.float64)
    scale = 2.0 ** (-N / 2)
    for config in range(1 << N):
        a = sum(1 << j for j, bit in enumerate(left_bits) if config & bit)
        b = sum(1 << j for j, bit in enumerate(right_bits) if config & bit)
        parity = sum(bool(config & (1 << u)) and bool(config & (1 << v)) for u, v in edges) % 2
        amplitudes[a, b] = -scale if parity else scale
    rho = amplitudes @ amplitudes.T
    spectrum = np.linalg.eigvalsh(rho)
    r = expected(n, mask)
    positive = spectrum[spectrum > 1e-8]
    assert len(positive) == (1 << r), (n, mask, len(positive), r)
    target = 1.0 / (1 << r)
    error = float(max(np.max(np.abs(positive - target)), np.max(np.abs(spectrum[spectrum <= 1e-8]))))
    assert error < 1e-10, (n, mask, error)
    return len(positive), error


def main():
    tested = 0
    for n in range(3, 10):
        for mask in range(1, 1 << n):
            rank = binary_rank(cut_rows(n, mask))
            want = expected(n, mask)
            assert rank == want, (n, mask, rank, want)
            tested += 1
    for n in (10, 11):
        for t in range(1, n + 1):
            mask = (1 << t) - 1
            rank = binary_rank(cut_rows(n, mask))
            want = expected(n, mask)
            assert rank == want, (n, mask, rank, want)
            tested += 1
    print(f'EXACT GF(2) CUT-RANK CHECKS PASSED: {tested} cases, n=3..11')
    for n, mask in ((3, 1), (3, 3), (3, 7), (4, 1), (4, 7), (4, 15)):
        nonzero, error = direct_spectrum(n, mask)
        print(f'DIRECT STATE TRACE PASSED: n={n}, t={mask.bit_count()}, nonzero={nonzero}, max_abs_error={error:.3e}')
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    main()
