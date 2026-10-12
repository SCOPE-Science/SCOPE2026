#!/usr/bin/env python3
"""Exact certificates for the binary single-deletion weight-three code sizes at lengths 14 and 15.

This script uses only Python's standard library. Positions in the input data are 1-based.
It independently evaluates full deletion outputs and an explicit weighted packing bound.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'witnesses.json').read_text(encoding='utf-8'))


def output_words(n, positions):
    """Remove each coordinate of the actual 0/1 word, deduplicating results."""
    x = tuple(int(p in positions) for p in range(1, n + 1))
    return {x[:j] + x[j+1:] for j in range(n)}


def outputs_by_index(n, positions):
    """Independent formula using the locations of the surviving ones."""
    ys = set()
    for deleted in range(1, n + 1):
        remaining = tuple(p - int(p > deleted) for p in positions if p != deleted)
        ys.add(remaining)
    return ys


def support(y):
    return tuple(i + 1 for i, b in enumerate(y) if b)


def weight3_scaled(m, supp):
    """Integer weight is three times the fractional dual weight."""
    if len(supp) == 2:
        a, b = supp
        w = 1 + int(b == a + 1)
        if m == 14 and (a, b) == (13, 14):
            w += 1
        return w
    if len(supp) == 3:
        a, b, c = supp
        if (b, c) == (a+1, a+2) and a % 2 == 1 and a <= 11:
            return 1
    return 0


def verify(n, positions_list, expected):
    m = n - 1
    assert n in (14, 15)
    assert len(positions_list) == expected
    assert len({tuple(t) for t in positions_list}) == expected
    code = set()
    for t in positions_list:
        assert len(t) == 3 and t == sorted(t) and 1 <= t[0] < t[1] < t[2] <= n
        ys = output_words(n, t)
        check_ys = outputs_by_index(n, t)
        assert {support(y) for y in ys} == check_ys
        assert code.isdisjoint(ys), ('overlapping deletion', n, t, code & ys)
        code.update(ys)
    dual = {}
    for a,b in combinations(range(1, m+1), 2):
        dual[(a,b)] = weight3_scaled(m,(a,b))
    for a in range(1, m-1, 2):
        dual[(a,a+1,a+2)] = weight3_scaled(m,(a,a+1,a+2))
    dual_sum = sum(dual.values())
    assert dual_sum == 3 * expected, (n, dual_sum, expected)
    slack = Counter()
    total = 0
    for t in combinations(range(1, n + 1), 3):
        ys = outputs_by_index(n, t)
        # Independently checked against physical deletions, for EVERY possible word.
        actual_ys = {support(y) for y in output_words(n, t)}
        assert ys == actual_ys
        cover = sum(weight3_scaled(m, y) for y in ys)
        assert cover >= 3, (n, t, cover)
        slack[cover-3] += 1
        total += 1
    assert total == (364 if n == 14 else 455)
    print('n', n, 'codewords', expected, 'distinct deletion outputs', len(code),
          'candidate triples', total, 'dual weight sum', f'{dual_sum}/3',
          'minimum coverage', min(slack)+3, 'slack histogram', sorted(slack.items()))


if __name__ == '__main__':
    assert sorted(DATA) == ['14', '15']
    verify(14, DATA['14'], 32)
    verify(15, DATA['15'], 37)
    print('VERIFY_OK max3(14)=32 max3(15)=37')
