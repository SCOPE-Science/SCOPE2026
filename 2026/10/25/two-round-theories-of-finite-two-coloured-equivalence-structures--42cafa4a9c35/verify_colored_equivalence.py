#!/usr/bin/env python3
"""Exact two-round theories of finite equivalence structures with one unary colour."""
import csv
import itertools
import collections
from pathlib import Path

TYPES = tuple((r, b) for r in range(3) for b in range(3) if r+b)
assert TYPES == ((0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2))


def five_bit_characters(profile):
    red = sum(r*m for (r,b),m in zip(TYPES,profile))
    blue = sum(b*m for (r,b),m in zip(TYPES,profile))
    out = set()
    for (r,b), count in zip(TYPES,profile):
        if not count:
            continue
        ext_red = int(red > r)
        ext_blue = int(blue > b)
        if r:
            out.add((1, int(r >= 2), int(b >= 1), ext_red, ext_blue))
        if b:
            out.add((0, int(r >= 1), int(b >= 2), ext_red, ext_blue))
    return tuple(sorted(out))


def explicit_quantifier_free_extensions(profile):
    block = []
    colour = []
    for (r,b),multiplicity in zip(TYPES,profile):
        for _ in range(multiplicity):
            block_id = len(set(block))
            block.extend([block_id]*(r+b))
            colour.extend([1]*r+[0]*b)
    n = len(colour)
    one_types = set()
    for x in range(n):
        binary_patterns = set()
        for y in range(n):
            binary_patterns.add((colour[y], int(x == y), int(block[x] == block[y])))
        one_types.add((colour[x], tuple(sorted(binary_patterns))))
    return tuple(sorted(one_types))


def classify():
    entries = collections.defaultdict(list)
    independent_entries = collections.defaultdict(list)
    for profile in itertools.product(range(3),repeat=8):
        if not any(profile):
            continue
        size = sum((r+b)*m for (r,b),m in zip(TYPES,profile))
        entries[five_bit_characters(profile)].append((size,profile))
        independent_entries[explicit_quantifier_free_extensions(profile)].append((size,profile))

    # A separate, element-by-element computation must give the same partition.
    signature_partition = {
        frozenset(profile for _,profile in items) for items in entries.values()
    }
    direct_partition = {
        frozenset(profile for _,profile in items) for items in independent_entries.values()
    }
    assert signature_partition == direct_partition
    assert len(entries) == 207
    assert sum(map(len,entries.values())) == 3**8-1

    distribution=collections.Counter(min(size for size,_ in v) for v in entries.values())
    expected = {1:2,2:6,3:10,4:17,5:22,6:28,7:30,
                8:29,9:26,10:18,11:12,12:5,13:2}
    assert dict(distribution)==expected
    assert sum(distribution.values())==207
    extrema = []
    rows=[]
    for signature,items in entries.items():
        minimum, p = min(items, key=lambda z:(z[0],z[1]))
        if minimum==13:
            extrema.append(p)
        rows.append((minimum, signature, p, len(items)))
    assert sorted(extrema)==[
        (1,1,1,0,0,1,1,1),
        (1,1,1,0,1,1,0,1),
    ]
    rows.sort(key=lambda row:(row[0],row[1]))
    with (Path(__file__).parent/'CLASSIFICATION.csv').open('w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f,lineterminator='\n')
        writer.writerow(['class_index','minimum_size','five_bit_character_set','least_profile','canonical_profiles_in_class'])
        for index,(minimum,signature,profile,multiplicity) in enumerate(rows,1):
            writer.writerow([index,minimum,';'.join(''.join(map(str,x)) for x in signature),
                             ''.join(map(str,profile)),multiplicity])
    print('CANONICAL_PROFILES',3**8-1)
    print('RANK_TWO_THEORIES',len(entries))
    print('OPTIMAL_REPRESENTATIVE_DISTRIBUTION',sorted(distribution.items()))
    print('SHARP_MAXIMUM',max(distribution))
    print('EXTREMAL_PROFILES',sorted(extrema))
    print('TWO_INDEPENDENT_SIGNATURE_FORMULATIONS_AGREE',True)
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    classify()
