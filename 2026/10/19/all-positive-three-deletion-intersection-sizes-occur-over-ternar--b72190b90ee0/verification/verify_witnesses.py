#!/usr/bin/env python3
"""Exact, independent descendant-set verification using subsequence indices."""
from itertools import combinations
from pathlib import Path
import csv

HERE = Path(__file__).resolve().parent.parent

def deleted(s, t):
    """Return each *distinct* subsequence after deleting exactly t indices."""
    n = len(s)
    return {''.join(s[i] for i in indices)
            for indices in combinations(range(n), n-t)}

with (HERE / 'certificates' / 'witnesses.tsv').open(encoding='utf-8') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
assert len(rows) == 20
assert {int(row['m']) for row in rows} == set(range(1, 21))
for row in rows:
    m, q, n = map(int, [row['m'], row['alphabet'], row['length']])
    x, y = row['x'], row['y']
    assert len(x) == len(y) == n and x != y and n >= 3
    assert q == (3 if m == 18 else 2)
    assert set(x+y) <= set('012'[:q])
    assert not (deleted(x, 2) & deleted(y, 2)), (m, 'radius-two overlap')
    common = deleted(x, 3) & deleted(y, 3)
    assert len(common) == m, (m, 'got', len(common))
    if m == 18:
        expected = set("""001010 001020 001021 001101 001120 001121
011010 011020 011021 100101 100120 100121
101010 101020 101021 101101 101120 101121""".split())
        assert common == expected, ('radius-three certificate', common ^ expected)
print('VERIFY_OK 20 exact witness pairs; radius-two disjoint; radius-three counts 1..20')
