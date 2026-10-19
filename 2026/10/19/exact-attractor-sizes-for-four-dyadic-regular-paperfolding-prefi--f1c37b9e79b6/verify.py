#!/usr/bin/env python3
"""Exact, standard-library verification of regular-paperfolding attractor certificates.

Run from the directory containing certificates.json: python3 verify.py
All substring comparisons are exact; no probabilistic hashing or optimizer is used.
"""
import json
from pathlib import Path


def paperfolding(length):
    result = []
    for j in range(1, length + 1):
        odd = j
        while odd % 2 == 0:
            odd //= 2
        result.append('0' if odd % 4 == 1 else '1')
    return ''.join(result)


def verify_case(case):
    n = case['length']
    word = paperfolding(n)
    positions = case['attractor_positions_0_based']
    assert positions == sorted(set(positions))
    assert all(0 <= p < n for p in positions)
    expected = {128: 5, 256: 6, 512: 6, 1024: 7}[n]
    assert len(positions) == expected
    assert word[:16] == '0010011000110110'

    # Upper bound. For each factor length, compare ALL distinct factors with
    # the factors having at least one occurrence crossed by the proposed set.
    distinct_total = 0
    for width in range(1, n + 1):
        all_factors = set()
        crossed_factors = set()
        for start in range(n - width + 1):
            value = word[start:start + width]
            all_factors.add(value)
            if any(start <= p < start + width for p in positions):
                crossed_factors.add(value)
        assert crossed_factors == all_factors, (n, width, list(all_factors-crossed_factors)[:3])
        distinct_total += len(all_factors)
    assert distinct_total == case['expected_distinct_factor_count']

    # Lower bound. For every listed factor, take the union of ALL of its
    # occurrence spans; each attractor position has bounded total load.
    denominator = case['lower_certificate_denominator']
    loads = [0] * n
    numerator_total = 0
    factors_seen = set()
    for row in case['lower_certificate_factors']:
        factor = row['factor']
        numerator = row['numerator']
        assert set(factor) <= {'0', '1'} and factor not in factors_seen
        assert numerator > 0 and isinstance(numerator, int)
        factors_seen.add(factor)
        numerator_total += numerator
        found = False
        for start in range(n - len(factor) + 1):
            if word.startswith(factor, start):
                found = True
        assert found, (n, factor)
        for p in range(n):
            if any(word.startswith(factor, start) and start <= p < start + len(factor)
                   for start in range(max(0, p-len(factor)+1), min(p, n-len(factor)) + 1)):
                loads[p] += numerator
    assert numerator_total == case['expected_lower_numerator_sum']
    assert max(loads) == case['expected_max_position_load']
    assert max(loads) <= denominator
    assert (numerator_total + denominator - 1) // denominator == expected
    print('CASE_OK length=%d distinct_factors=%d gamma=%d lower=%d/%d factors=%d max_load=%d' %
          (n, distinct_total, expected, numerator_total, denominator, len(factors_seen), max(loads)))


def main():
    data = json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf8'))
    assert len(data['cases']) == 4
    assert [c['length'] for c in data['cases']] == [128, 256, 512, 1024]
    for case in data['cases']:
        verify_case(case)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
