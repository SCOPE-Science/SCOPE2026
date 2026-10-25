#!/usr/bin/env python3
"""Exact certificates for cyclic prefix-normal representative obstruction.
No third-party dependencies. Run with Python 3.9+ in the same directory as witnesses.csv.
"""
from collections import Counter
from csv import DictReader
from itertools import combinations
from pathlib import Path

EXPECTED = ('00010101011', '00011001011', '00110110111')

def rotations(w):
    return (w[j:] + w[:j] for j in range(len(w)))

def necklace(w):
    return min(rotations(w))

def direct_pn(w):
    n = len(w)
    prefix = [0]
    for x in w:
        prefix.append(prefix[-1] + (x == '1'))
    for length in range(1, n + 1):
        first = prefix[length]
        for start in range(1, n - length + 1):
            if prefix[start + length] - prefix[start] > first:
                return False
    return True

def direct_witness(w):
    n = len(w)
    prefix = [0]
    for x in w:
        prefix.append(prefix[-1] + (x == '1'))
    for length in range(1, n + 1):
        for start in range(1, n - length + 1):
            a = prefix[length]
            b = prefix[start + length] - prefix[start]
            if b > a:
                return (length, start, a, b)
    return None

def gap_condition(g):
    """Criterion on the gaps between 1s, for a linear rotation starting in 1.
    Last gap reaches the end of the circular word and is ignored.
    """
    d = len(g)
    for k in range(1, d - 1):
        p = sum(g[:k])
        for j in range(1, d - k):
            if p > sum(g[j:j+k]):
                return False
    return True

def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for sep in combinations(range(1, total), parts-1):
        ys = (0,) + sep + (total,)
        yield tuple(ys[i+1]-ys[i] for i in range(parts))

def from_gaps(g):
    return ''.join('1' + '0'*(q-1) for q in g)

def gap_bad_necklaces(n):
    bad = set()
    for d in range(1, n+1):
        seen = set()
        for g in compositions(n, d):
            canonical = min(g[i:]+g[:i] for i in range(d))
            if canonical in seen: continue
            seen.add(canonical)
            if not any(gap_condition(canonical[i:]+canonical[:i]) for i in range(d)):
                bad.add(necklace(from_gaps(canonical)))
    return bad

def bit_bad_necklaces(n):
    bad=set()
    for t in range(1<<n):
        w=format(t, f'0{n}b')
        if not any(direct_pn(v) for v in rotations(w)):
            bad.add(necklace(w))
    return bad

def check_witness_file():
    with (Path(__file__).parent / 'witnesses.csv').open(newline='', encoding='utf-8') as f:
        rows = list(DictReader(f))
    assert len(rows) == 33
    seen=set()
    for row in rows:
        canon=row['necklace']; index=int(row['cut']); length=int(row['length']); start=int(row['factor_start'])
        first=int(row['prefix_ones']); later=int(row['factor_ones'])
        assert canon in EXPECTED and 0<=index<11 and (canon,index) not in seen
        seen.add((canon,index))
        v=canon[index:]+canon[:index]
        assert 1<=length<=11 and 1<=start<=11-length and later>first
        assert v[:length].count('1')==first and v[start:start+length].count('1')==later
    assert len(seen)==33
    return len(rows)

def main():
    counts=[]
    for n in range(1,12):
        one=bit_bad_necklaces(n)
        two=gap_bad_necklaces(n)
        assert one==two, (n,one,two)
        if n<=10: assert not one
        else: assert tuple(sorted(one))==EXPECTED
        counts.append(len(one))
    checks=check_witness_file()
    for n in range(11,121):
        s=EXPECTED[0] + '0'*(n-11)
        # These five 1 starts are the only possible prefix-normal cuts.
        for i in (3,5,7,9,10):
            v=s[i:]+s[:i]
            if i in (3,5,7):
                assert v[:2]=='10' and '11' in v
            elif i==9:
                assert v[:5]=='11000' and '10101' in v
            else:
                assert v[:3]=='100' and '101' in v
    print('VERIFY_OK direct_bit_and_independent_gap_enumerations=1..11')
    print('VERIFY_OK bad_necklaces_by_length='+','.join(f'{n}:{cnt}' for n,cnt in enumerate(counts,1)))
    print('VERIFY_OK n11_representatives='+','.join(EXPECTED))
    print(f'VERIFY_OK witness_rows={checks} all_length_obstruction=11..120_checked')

if __name__=='__main__':
    main()
