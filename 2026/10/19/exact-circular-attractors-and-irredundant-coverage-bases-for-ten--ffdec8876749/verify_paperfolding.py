#!/usr/bin/env python3
"""Literal exhaustive verifier for finite regular-paperfolding circular-attractor certificates.

The checker depends only on the Python 3 standard library. It independently
reconstructs every circular factor and its complete set of covering positions.
Run: python3 verify_paperfolding.py
"""

import json
from pathlib import Path


def word(n):
    """Length-n regular paperfolding prefix (one choice of global bit complement)."""
    return bytes(0 if (j // (j & -j)) % 4 == 1 else 1 for j in range(1, n + 1))


def factor_coverages(w):
    """Map every distinct circular factor of length 1..n to all crossing positions."""
    n = len(w)
    doubled = w + w
    all_positions = (1 << n) - 1
    covers = {}
    for length in range(1, n + 1):
        window = (1 << length) - 1
        for start in range(n):
            factor = doubled[start:start + length]
            interval = window << start
            covered = (interval & all_positions) | (interval >> n)
            covers[factor] = covers.get(factor, 0) | covered
    return covers


def verify(entry):
    k = entry['k']
    n = 1 << k
    assert n == entry['n']
    w = word(n)
    covers = factor_coverages(w)
    assert len(covers) == entry['factor_count'], (k, len(covers), entry['factor_count'])
    distinct_masks = sorted(set(covers.values()), key=lambda m: (m.bit_count(), m))
    minimal_masks = []
    for bits in distinct_masks:
        if not any((bits & old) == old for old in minimal_masks):
            minimal_masks.append(bits)
    assert len(minimal_masks) == entry['reduced_coverage_constraints'], (k, len(minimal_masks))

    upper = entry['upper_positions']
    target = entry['minimum']
    assert len(upper) == target and len(set(upper)) == target
    assert all(0 <= p < n for p in upper)
    mask = sum(1 << p for p in upper)
    missing = next((factor for factor, allowed in covers.items()
                    if not (allowed & mask)), None)
    assert missing is None, ('upper bound failed', k, missing)

    den = entry['dual_denominator']
    assert type(den) is int and den > 0
    loads = [0] * n
    num = 0
    doubled = w + w
    for length, start, weight_num in entry['dual_factor_weights']:
        assert 1 <= length <= n and 0 <= start < n and weight_num > 0
        factor = doubled[start:start + length]
        allowed = covers[factor]
        num += weight_num
        while allowed:
            lowest = allowed & -allowed
            p = lowest.bit_length() - 1
            loads[p] += weight_num
            allowed ^= lowest
    assert num == entry['total_dual_numerator']
    assert max(loads) <= den, ('dual infeasible', k, max(loads), den)
    assert den * (target - 1) < num <= den * target, ('dual gap insufficient', k, num, den, target)
    print(f"k={k:2d} n={n:4d} circular_factors={len(covers):6d} "
          f"minimum={target} dual={num}/{den} "
          f"weighted_factors={len(entry['dual_factor_weights']):2d} "
          f"minimal_coverage_sets={len(minimal_masks):2d} "
          f"max_dual_position_load={max(loads)}/{den} VERIFIED")


def main():
    cert = json.loads(Path(__file__).with_name('paperfolding_certificates.json').read_text(encoding='utf-8'))
    assert len(cert['entries']) == 10
    assert [e['k'] for e in cert['entries']] == list(range(1, 11))
    for entry in cert['entries']:
        verify(entry)
    print('ALL TEN EXACT CERTIFICATES VERIFIED')


if __name__ == '__main__':
    main()
