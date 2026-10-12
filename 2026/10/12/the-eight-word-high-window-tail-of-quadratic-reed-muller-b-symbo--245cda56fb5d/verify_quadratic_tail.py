#!/usr/bin/env python3
"""Reproduce the large-window b-symbol spectrum of lex-ordered binary RM(2,m)."""
from collections import Counter


def exhaustive_quadratic_code(m):
    n = 1 << m
    masks = [(1 << n) - 1]
    linear = [sum(1 << i for i in range(n) if (i >> j) & 1) for j in range(m)]
    masks.extend(linear)
    masks.extend(linear[i] & linear[j] for i in range(m) for j in range(i + 1, m))
    K = len(masks)
    assert K == 1 + m + m * (m - 1) // 2
    counts = {b: Counter() for b in range((5 * n) // 8 + 1, n + 1)}
    x = 0
    for step in range(1 << K):
        if step:
            x ^= masks[(step & -step).bit_length() - 1]
        doubled = x | (x << n)
        for b, hist in counts.items():
            block = (1 << b) - 1
            zero_windows = sum(not ((doubled >> i) & block) for i in range(n))
            hist[n - zero_windows] += 1
    Q = n // 4
    for b, hist in counts.items():
        expected = Counter({0: 1})
        if b <= 3 * Q:
            expected[b + Q - 1] = 8
            expected[n] = (1 << K) - 9
        else:
            expected[n] = (1 << K) - 1
        assert hist == expected, (m, b, hist, expected)
    print(f"RM_CHECK_OK m={m} n={n} dimension={K} codewords={1 << K} widths={len(counts)}", flush=True)


def affine_geometry(m):
    n = 1 << m
    Q = n // 4
    dual_basis = []
    for a in range(1, n):
        for b in range(a + 1, n):
            triple = sorted((a, b, a ^ b))
            if (a, b) == (triple[0], triple[1]):
                dual_basis.append((a, b))
    short_spans = Counter()
    total = 0
    for a, b in dual_basis:
        for c in range(4):
            supp = [i for i in range(n) if ((a & i).bit_count() & 1) == (c & 1)
                    and ((b & i).bit_count() & 1) == ((c >> 1) & 1)]
            assert len(supp) == Q
            largest_gap = max([supp[i + 1] - supp[i] - 1 for i in range(Q - 1)]
                              + [supp[0] + n - supp[-1] - 1])
            span = n - largest_gap
            if span < 3 * n // 8:
                short_spans[span] += 1
            total += 1
    assert short_spans == Counter({Q: 8}), (m, short_spans)
    expected = ((n - 1) * (n - 2) // 6) * 4
    assert total == expected, (total, expected)
    print(f"AFFINE_CHECK_OK m={m} codim_two_cosets={total} short_spans={dict(short_spans)}", flush=True)


def main():
    for m in range(3, 6):
        exhaustive_quadratic_code(m)
    for m in range(3, 9):
        affine_geometry(m)
    print("VERIFY_OK quadratic_tail_m3_to_m5 affine_flats_m3_to_m8")


if __name__ == '__main__':
    main()
