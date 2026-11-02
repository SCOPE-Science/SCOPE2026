#!/usr/bin/env python3
"""Exact finite certificate for length-504 Tribonacci string attractors.

Uses integer bitsets and exhaustive, finite loops only. Python 3.10+.
"""
from collections import Counter
from itertools import combinations, product
from math import comb
import hashlib

MORPHISM = {'0': '01', '1': '02', '2': '0'}
A = (80, 82, 93, 95)
B = (148, 152, 172, 176)
C = (229, 231, 242, 244)
D = (273, 274, 280, 281, 317, 318, 324, 325)
E = (354, 356, 367, 369)
F = (422, 426, 446, 450)
BOXES = ((A, B, D), (B, C, D), (B, D, E), ((229,), D, F))
EXPECTED_MINIMAL_FACTORS = (
    '1010201001020101',
    '00102010010201010201001020102010010201010201001020100',
    '20102010010201010201001020102',
    '001020100',
    '20102',
    '101',
    '2',
    '20102010010201010201001020102010010201010201001020100102010102010010201020100102010',
    '00',
    '1',
    '201020100102010',
    '001020100102010102010010201020100102010',
)
WITNESSES = (
    (12, 148, 273),
    (43, 80, 148),
    (23, 229, 273),
    (80, 148, 293),
    (80, 155, 277),
    (84, 150, 273),
    (80, 149, 273),
    (80, 273, 422),
    (80, 148, 275),
    (81, 148, 273),
)


def tribonacci_word(iterations=10):
    word = '0'
    for _ in range(iterations):
        word = ''.join(MORPHISM[ch] for ch in word)
    return word


def factor_position_masks(word):
    """For each distinct nonempty factor, all crossed positions, zero-based."""
    supports = {}
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            factor = word[i:j]
            interval = ((1 << (j - i)) - 1) << i
            supports[factor] = supports.get(factor, 0) | interval
    return supports


def inclusion_minimal_masks(supports):
    distinct = sorted(set(supports.values()), key=lambda x: (x.bit_count(), x))
    minimal = []
    for mask in distinct:
        if not any((m & mask) == m for m in minimal):
            minimal.append(mask)
    return minimal


def size_three_count(masks, n):
    """Count every increasing triple by its coverage-signature class."""
    frequency = Counter()
    for p in range(n):
        signature = sum(1 << i for i, m in enumerate(masks) if (m >> p) & 1)
        frequency[signature] += 1
    classes = sorted(frequency.items())
    full = (1 << len(masks)) - 1
    total = 0
    for a, (s1, n1) in enumerate(classes):
        for b in range(a, len(classes)):
            s2, n2 = classes[b]
            for c in range(b, len(classes)):
                s3, n3 = classes[c]
                if (s1 | s2 | s3) != full:
                    continue
                if a == b == c:
                    total += comb(n1, 3)
                elif a == b:
                    total += comb(n1, 2) * n3
                elif b == c:
                    total += n1 * comb(n2, 2)
                else:
                    total += n1 * n2 * n3
    return total, len(classes)


def main():
    word = tribonacci_word()
    assert len(word) == 504
    assert set(word) == {'0', '1', '2'}
    supports = factor_position_masks(word)
    assert len(supports) == 80559
    assert len(set(supports.values())) == 79983
    smallest = inclusion_minimal_masks(supports)
    assert len(smallest) == 12
    expected_masks = [supports[f] for f in EXPECTED_MINIMAL_FACTORS]
    assert smallest == expected_masks, 'The listed factors represent the 12 minimal supports.'
    core = expected_masks[:10]
    all_count, all_classes = size_three_count(smallest, len(word))
    core_count, core_classes = size_three_count(core, len(word))
    assert (all_count, core_count, all_classes, core_classes) == (416, 416, 133, 65)
    boxes = set()
    for block in BOXES:
        for triple in product(*block):
            assert triple[0] < triple[1] < triple[2]
            boxes.add(triple)
    assert len(boxes) == 416
    for triple in boxes:
        assert all(any((mask >> p) & 1 for p in triple) for mask in core)
    for i, triple in enumerate(WITNESSES):
        assert triple not in boxes
        assert all((any((mask >> p) & 1 for p in triple)) == (j != i)
                   for j, mask in enumerate(smallest))
    # The ten exact factors suffice for all 80,559 factors, and ten are
    # necessary: each witness misses a different inclusion-minimal support.
    print('word_length:', len(word))
    print('word_sha256:', hashlib.sha256(word.encode('ascii')).hexdigest())
    print('distinct_nonempty_factors:', len(supports))
    print('distinct_factor_supports:', len(set(supports.values())))
    print('minimal_supports:', len(smallest))
    print('core_factor_count:', len(core))
    print('support_signature_classes:', all_classes, core_classes)
    print('all_three_attractors:', all_count)
    print('four_box_sizes:', [len(x)*len(y)*len(z) for x,y,z in BOXES])
    print('minimality_witnesses:', len(WITNESSES))
    print('PASS')

if __name__ == '__main__':
    main()
