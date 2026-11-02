#!/usr/bin/env python3
"""Independent exact finite verification of Tribonacci 4-power order spectra.

Python standard library only. Run: python3 verify.py
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent
PAIRS = ('00', '01', '02', '10', '20')
MAX_ORDER = 1705
CUTOFFS = {
    7: (2, 2), 13: (5, 4), 24: (8, 7), 44: (13, 11),
    81: (28, 22), 149: (49, 41), 274: (88, 72),
    504: (169, 136), 927: (311, 250), 1705: (579, 462),
}


def substitution(level):
    images = {'0': '0', '1': '1', '2': '2'}
    for _ in range(level):
        images = {
            '0': images['0'] + images['1'],
            '1': images['0'] + images['2'],
            '2': images['0'],
        }
    return images


def cover(level):
    im = substitution(level)
    blocks = []
    for pair in PAIRS:
        w = im[pair[0]] + im[pair[1]]
        p0 = [0]
        p1 = [0]
        for letter in w:
            p0.append(p0[-1] + int(letter == '0'))
            p1.append(p1[-1] + int(letter == '1'))
        blocks.append((pair, len(im[pair[0]]), p0, p1))
    return blocks


def predicates(p0, p1, i, d):
    counts = []
    for j in range(4):
        lo = i + j*d
        hi = lo + d
        counts.append((p0[hi]-p0[lo], p1[hi]-p1[lo]))
    is_abelian = all(c == counts[0] for c in counts[1:])
    is_additive = len({2*a+b for a,b in counts}) == 1
    return is_additive, is_abelian


def read_csv(relative_path):
    with (ROOT / relative_path).open('r', encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == MAX_ORDER
    assert all(set(r) == {'d', 'pair', 'index'} for r in rows)
    assert [int(r['d']) for r in rows] == list(range(1, MAX_ORDER+1))
    assert all((r['pair'] in PAIRS and int(r['index']) >= 0)
               or (r['pair'] == 'none' and r['index'] == '-1') for r in rows)
    return rows


def verify():
    additive = read_csv('data/additive_orders.csv')
    abelian = read_csv('data/abelian_orders.csv')
    true_add = [r['pair'] != 'none' for r in additive]
    true_abel = [r['pair'] != 'none' for r in abelian]
    assert all(not b or a for a,b in zip(true_add, true_abel))

    # Directly check the claimed positive witnesses at the published level.
    full = {pair: (firstlen, p0, p1)
            for pair, firstlen, p0, p1 in cover(16)}
    assert [len(x) for x in substitution(16).values()] == [19513,16377,10609]
    assert min(len(x) for x in substitution(16).values()) >= 4*MAX_ORDER
    for is_abelian_class, rows in ((False, additive), (True, abelian)):
        for d, r in enumerate(rows, start=1):
            if r['pair'] == 'none':
                continue
            firstlen, p0, p1 = full[r['pair']]
            index = int(r['index'])
            assert 0 <= index < firstlen
            flags = predicates(p0, p1, index, d)
            assert flags[1 if is_abelian_class else 0], ('bad witness', d, r)

    # Independently recompute the yes/no classification at the smallest
    # substitution depth sufficient for each value of d. This is distinct
    # from the fixed-depth computation used to generate the CSV tables.
    blocks = {}
    level = 0
    im = substitution(level)
    for d in range(1, MAX_ORDER+1):
        while min(map(len, im.values())) < 4*d:
            level += 1
            im = substitution(level)
        if level not in blocks:
            blocks[level] = cover(level)
        has_add = has_abel = False
        for pair, firstlen, p0, p1 in blocks[level]:
            for i in range(firstlen):
                a0 = p0[i+d]-p0[i]
                b0 = p1[i+d]-p1[i]
                weighted = 2*a0+b0
                add_possible = True
                abel_possible = True
                for z in (1,2,3):
                    lo = i+z*d
                    hi = lo+d
                    ax = p0[hi]-p0[lo]
                    bx = p1[hi]-p1[lo]
                    if 2*ax+bx != weighted:
                        add_possible = False
                    if ax != a0 or bx != b0:
                        abel_possible = False
                    if not add_possible and not abel_possible:
                        break
                has_add = has_add or add_possible
                has_abel = has_abel or abel_possible
                if has_add and has_abel:
                    break
            if has_add and has_abel:
                break
        assert has_add == true_add[d-1], ('additive disagreement', d)
        assert has_abel == true_abel[d-1], ('abelian disagreement', d)

    assert sum(true_add) == 579
    assert sum(true_abel) == 462
    assert sum(a and not b for a,b in zip(true_add,true_abel)) == 117
    assert [i+1 for i,(a,b) in enumerate(zip(true_add,true_abel)) if a and not b][0] == 10
    assert [i+1 for i,(a,b) in enumerate(zip(true_add,true_abel)) if a][0] == 6
    for bound, expected in CUTOFFS.items():
        assert (sum(true_add[:bound]), sum(true_abel[:bound])) == expected, bound
    print('VERIFY_OK additive=579 abelian=462 additive_only=117 cutoff=1705')


if __name__ == '__main__':
    verify()
