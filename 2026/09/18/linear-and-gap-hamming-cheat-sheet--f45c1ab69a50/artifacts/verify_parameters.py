#!/usr/bin/env python3
"""Exact checks for the linear-AND Gap-Hamming cheat-sheet parameters."""

from math import log2, sqrt


def full_adder(a: int, b: int, c: int):
    s = a ^ b ^ c
    carry = (a & b) ^ (c & (a ^ b))
    return s, carry


def greater_than_constant(bits_msb_first, threshold: int):
    """Comparator recurrence used in the proof; returns int(value > threshold)."""
    L = len(bits_msb_first)
    tbits = [(threshold >> j) & 1 for j in range(L - 1, -1, -1)]
    eq = 1
    gt = 0
    for w, t in zip(bits_msb_first, tbits):
        if t == 0:
            gt = gt ^ (eq & w)
            eq = eq & (1 ^ w)
        else:
            eq = eq & w
    return gt


def gate_counts(k: int):
    m = 1 << k
    # Balanced tree of ripple-carry adders.
    add = sum((m // (1 << (j + 1))) * 2 * (j + 1) for j in range(k))
    assert add == 4 * m - 2 * k - 4
    L = k + 1
    # Two constant comparators, each with at most 2L AND gates, plus one OR.
    per_block_upper = add + 4 * L + 1
    # k-1 ANDs to combine validity bits and one final output AND.
    total_upper = k * per_block_upper + k
    padded = 5 * k * m
    return m, add, total_upper, padded


def construction_length(k: int):
    m, _, upper, d = gate_counts(k)
    assert upper < d
    # Same F_{2^{4k}} certificate encoding as in Wang--Wu.
    N = k * m + 4 * k * m * (2 * d - 1)
    return m, d, N


def check_components():
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                s, carry = full_adder(a, b, c)
                assert s + 2 * carry == a + b + c

    for L in range(1, 8):
        for threshold in range(1 << L):
            for value in range(1 << L):
                bits = [(value >> j) & 1 for j in range(L - 1, -1, -1)]
                assert greater_than_constant(bits, threshold) == int(value > threshold)


def main():
    check_components()
    rows = []
    for k in (12, 13, 16, 20):
        m, d, N = construction_length(k)
        soundness = (2 * d - 2) / (2 ** (4 * k))
        assert d < 2 ** (4 * k)
        assert soundness < 1 / 6
        assert N < 40 * k * k * m * m
        exponent = m / (8 * k)
        translated = sqrt(N) / (51 * (log2(N) ** 2))
        assert exponent > translated
        rows.append((k, m, d, N, soundness, exponent, translated))

    print("component_truth_tables: PASS")
    print("parameter_checks: PASS")
    for k, m, d, N, soundness, exponent, translated in rows:
        print(
            f"k={k} m={m} d={d} N={N} "
            f"pcp_soundness_bound={soundness:.6e} "
            f"rectangle_exponent={exponent:.6f} "
            f"translated_exponent={translated:.6f}"
        )


if __name__ == "__main__":
    main()
