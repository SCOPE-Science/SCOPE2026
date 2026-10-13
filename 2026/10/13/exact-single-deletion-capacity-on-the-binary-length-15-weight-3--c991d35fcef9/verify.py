#!/usr/bin/env python3
"""Standalone exact certificate checker for binary length-15 weight-three one-deletion codes.
Run from the directory containing code_triples.csv: python3 verify.py
Only the Python standard library is needed.
"""
from collections import Counter
from itertools import combinations
import csv

N = 15
SPECIAL = {1, 3, 5, 7, 9, 11, 12}


def word_from_positions(positions):
    x = ['0'] * N
    for p in positions:
        assert 1 <= p <= N
        x[p - 1] = '1'
    return ''.join(x)


def descendants_string(positions):
    s = word_from_positions(positions)
    return {s[:j] + s[j + 1:] for j in range(N)}


def descendants_positions(positions):
    out = set()
    for deleted in range(1, N + 1):
        out.add(tuple(p - (p > deleted) for p in positions if p != deleted))
    return out


def positions_from_string(s):
    return tuple(i + 1 for i, b in enumerate(s) if b == '1')


def triple_weight(y):
    """Return THREE TIMES the fractional dual weight of a length-14 output."""
    loc = positions_from_string(y)
    if len(loc) == 2:
        return 2 if loc[1] == loc[0] + 1 else 1
    if len(loc) == 3 and loc[1] == loc[0] + 1 and loc[2] == loc[0] + 2:
        return int(loc[0] in SPECIAL)
    return 0


def main():
    with open('code_triples.csv', newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    code = [tuple(int(row[k]) for k in ('position1', 'position2', 'position3')) for row in rows]
    assert len(code) == 37 and len(set(code)) == len(code)
    assert all(p == tuple(sorted(p)) and len(set(p)) == 3 for p in code)
    all_words = list(combinations(range(1, N + 1), 3))
    assert len(all_words) == 455
    seen = set()
    cover_minimum = 10**9
    for x in all_words:
        descendants_a = descendants_string(x)
        descendants_b = descendants_positions(x)
        assert {positions_from_string(z) for z in descendants_a} == descendants_b
        cover = sum(triple_weight(y) for y in descendants_a)
        assert cover >= 3, ('dual cover failure', x, cover)
        cover_minimum = min(cover_minimum, cover)
        if x in code:
            assert seen.isdisjoint(descendants_a), ('deletion ambiguity', x)
            seen.update(descendants_a)
    assert cover_minimum == 3
    all_outputs = {
        ''.join('1' if j in z else '0' for j in range(1, N))
        for w in (2, 3) for z in combinations(range(1, N), w)
    }
    dual_numerator = sum(triple_weight(y) for y in all_outputs)
    assert dual_numerator == 111
    assert sum(triple_weight(y) for y in all_outputs if y.count('1') == 2) == 104
    assert sum(triple_weight(y) for y in all_outputs if y.count('1') == 3) == 7
    bins = Counter(sum(x) % 13 for x in all_words)
    assert len(bins) == 13 and set(bins.values()) == {35}
    print('VERIFY_OK N=15 W=3 candidates=455 selected=37 dual_weight=37')
    print('All one-deletion output sets disjoint; both descendant representations agree')
    print('Exact dual feasibility for every candidate; modified-VT residues all have 35 words')


if __name__ == '__main__':
    main()
