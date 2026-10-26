#!/usr/bin/env python3
"""Reproduce the exact local abelian-square spectrum of the Rudin--Shapiro word."""
from collections import Counter, defaultdict
from pathlib import Path
import csv

PHI = ((0, 1), (0, 2), (3, 1), (3, 2))
PAIR_SET = {(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1), (3, 2)}
COUNTS = {1: 128, 2: 32, 3: 72, 4: 8, 8: 4, 11: 4, 12: 4, 13: 4}
UNIQUE_COUNTS = {1: 104, 2: 20, 3: 56, 4: 8, 8: 2, 11: 4, 12: 4, 13: 2}


def morph(word):
    return tuple(y for x in word for y in PHI[x])


def words(k):
    out = {}
    for c in range(4):
        w = (c,)
        for _ in range(k):
            w = morph(w)
        out[c] = w
    return out


def canonical_pair_language():
    s = {(0, 1)}
    while True:
        t = set(s)
        for a, b in s:
            t.add(PHI[a])
            t.add((PHI[a][1], PHI[b][0]))
            t.add(PHI[b])
        if s == t:
            return s
        s = t


def root_from_counts(bits):
    pref = [0]
    for bit in bits:
        pref.append(pref[-1] + bit)
    for m in range(1, 14):
        if pref[m] == pref[2*m] - pref[m]:
            return m
    return None


def root_from_direct(bits):
    for m in range(1, 14):
        left = bits[:m]
        right = bits[m:2*m]
        if left.count(0) == right.count(0) and left.count(1) == right.count(1):
            return m
    return None


def build_rows():
    blocks = words(5)
    for a, b in sorted(PAIR_SET):
        coded = tuple(x // 2 for x in blocks[a] + blocks[b])
        for off in range(32):
            window = coded[off:off+26]
            x = root_from_counts(window)
            assert x == root_from_direct(window)
            yield (a, b, off, ''.join(map(str, window)), x)


def check():
    assert canonical_pair_language() == PAIR_SET
    rows = list(build_rows())
    assert len(rows) == 256
    assert Counter(r[4] for r in rows) == Counter(COUNTS)
    assert None not in [r[4] for r in rows]
    uniq = {r[3] for r in rows}
    assert len(uniq) == 200
    unique_dist = {w: root_from_counts(tuple(map(int, w))) for w in uniq}
    assert Counter(unique_dist.values()) == Counter(UNIQUE_COUNTS)
    hard = [(a,b,off) for a,b,off,word,m in rows if m == 13]
    assert hard == [(1,0,5),(1,3,5),(2,0,5),(2,3,5)]
    witnesses = sorted({word for a,b,off,word,m in rows if m == 13})
    assert witnesses == ['01000011101111011010001110', '10111100010000100101110001']
    path = Path(__file__).with_name('templates.csv')
    with path.open(newline='', encoding='utf-8') as f:
        data = list(csv.DictReader(f))
    assert len(data) == len(rows)
    for got, row in zip(data, rows):
        assert got == dict(zip(('source_a','source_b','offset','binary_factor','minimal_root'),
                               [str(row[0]),str(row[1]),str(row[2]),row[3],str(row[4])]))
    # Independent digit-recursion generator, not the four-letter morphism.
    n = 1 << 16
    ar = bytearray(n)
    for i in range(1, n):
        ar[i] = ar[i//2] ^ ((i & 1) & ((i//2) & 1))
    factors = {bytes(ar[i:i+26]) for i in range(n-25)}
    assert factors == {bytes(map(int, w)) for w in uniq}
    sample = Counter()
    for i in range(n-26):
        found = root_from_counts(ar[i:i+26])
        sample[found] += 1
    assert set(sample) == set(COUNTS)
    assert abs(sample[13]/sum(sample.values())-1/64)<0.001
    print('VERIFY_OK source_pairs=8 dyadic_templates=256 distinct_length26_factors=200')
    print('VERIFY_OK template_minimal_root_counts=' + str(dict(sorted(Counter(r[4] for r in rows).items()))))
    print('VERIFY_OK distinct_factor_minimal_root_counts=' + str(dict(sorted(Counter(unique_dist.values()).items()))))
    print('VERIFY_OK root13_templates=' + str(hard))
    print('VERIFY_OK root13_factor_strings=' + ','.join(witnesses))
    print('VERIFY_OK independent_binary_recursion_prefix_length=65536 complete_factor_language=yes')
    print('VERIFY_OK csv_rows=256 two_root_tests_agree=yes')


if __name__ == '__main__':
    check()
