#!/usr/bin/env python3
"""Finite, independent checks for the paperfolding-prefix universality theorem.

The infinite theorem is proved symbolically in RESULT.md.  This checker tests
its block mechanism and independent direct prefix computations.
"""
from itertools import product


def paperfold(n: int) -> int:
    """The specified one-indexed regular paperfolding coding."""
    assert n >= 1
    odd = n // (n & -n)
    return int(odd % 4 == 3)


def predicted(n: int) -> int:
    """Closed formula in the theorem (U(0)=0)."""
    assert n >= 0
    t, r = divmod(n, 8)
    if r == 0:
        return 3 * t - (paperfold(t) if t else 0)
    if r <= 2:
        return 3 * t
    if r <= 4:
        return 3 * t + 1
    if r == 5:
        return 3 * t + 1 + t % 2
    return 3 * t + 2


def advance(state, symbols):
    """Count greedy binary arches, retaining the incomplete arch's bitset."""
    count = 0
    for x in symbols:
        state |= (1 << x)
        if state == 3:
            count += 1
            state = 0
    return count, state


def has_subsequence(bits, target):
    j = 0
    for x in bits:
        if j < len(target) and x == target[j]:
            j += 1
    return j == len(target)


def test_direct_subsequence(n):
    bits = [paperfold(i) for i in range(1, n + 1)]
    index = predicted(n)
    # Independent exhaustive definition: every binary length-index word occurs.
    for v in product((0, 1), repeat=index):
        assert has_subsequence(bits, v), (n, index, v)
    # At least one length-(index+1) word is absent.
    assert any(not has_subsequence(bits, v)
               for v in product((0, 1), repeat=index + 1)), n


def main():
    # All 8 symbolic end-of-block transitions; no infinite sampling here.
    transitions = 0
    partial_cases = 0
    for before, parity, last in product((0, 1), repeat=3):
        block = (0, 0, 1, parity, 0, 1, 1, last)
        assert advance(2 if before else 0, block) == (
            3 + before - last, 2 if last else 0)
        transitions += 1
        delta = [0, before, before, before + 1, before + 1,
                 before + 1 + parity, before + 2, before + 2]
        for r in range(8):
            got, _ = advance(2 if before else 0, block[:r])
            assert got == delta[r], (before, parity, last, r, got, delta[r])
            partial_cases += 1

    # The binary valuation formula is independent of the proposed U formula.
    block_checks = 20000
    for t in range(block_checks):
        direct = tuple(paperfold(8 * t + i) for i in range(1, 9))
        expected = (0, 0, 1, t % 2, 0, 1, 1, paperfold(t + 1))
        assert direct == expected, t

    # A direct running greedy process verifies all prefixes, including phases.
    size = 1 << 19
    count = 0
    state = 0
    hist = {v: 0 for v in range(-8, 2)}
    assert predicted(0) == 0
    for n in range(1, size + 1):
        x = paperfold(n)
        state |= 1 << x
        if state == 3:
            state = 0
            count += 1
        assert count == predicted(n), (n, count, predicted(n))
        error = 8 * count - 3 * n
        assert -8 <= error <= 1
        hist[error] += 1
    assert all(hist[v] > 0 for v in range(-8, 2))

    # Exhaustive defining condition on short prefixes, distinct from arches.
    for n in range(0, 30):
        test_direct_subsequence(n)

    # Dyadic closed form and end-of-prefix state at sampled levels.
    for m in range(3, 20):
        assert predicted(1 << m) == 3 * (1 << (m - 3))

    print('VERIFY_OK',
          f'symbolic_end_transitions={transitions}',
          f'symbolic_partial_transitions={partial_cases}',
          f'block_identity_T=0..{block_checks-1}',
          f'direct_prefixes_1..{size}',
          'defining_subsequence_test_N=0..29',
          'dyadic_levels_m=3..19',
          'discrepancy_range=-8..1',
          'all_10_discrepancies_seen=yes')


if __name__ == '__main__':
    main()
