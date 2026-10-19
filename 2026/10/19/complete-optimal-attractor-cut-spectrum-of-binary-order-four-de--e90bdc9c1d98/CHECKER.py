#!/usr/bin/env python3
"""Exact binary de Bruijn order-four attractor cut-profile verifier.

Pure Python 3, no packages or external data. Verifies a finite complete
classification by enumerating every binary sixteen-letter word, normalizing
cyclic shifts, and checking certificates at all cuts.
"""

from __future__ import annotations
import csv
from collections import Counter
from itertools import combinations
from pathlib import Path

LENGTH, ORDER = 16, 4
COMPULSORY = (3, 7, 11, 15)  # zero-indexed positions in a 19-letter unfolding


def rotations(word):
    return [word[j:] + word[:j] for j in range(LENGTH)]


def is_de_bruijn(word):
    extended = word + word[:ORDER - 1]
    return len({extended[i:i + ORDER] for i in range(LENGTH)}) == 2**ORDER


def cycles_by_direct_enumeration():
    return sorted({min(rotations(w)) for number in range(2**LENGTH)
                   if is_de_bruijn(w := format(number, '016b'))})


def cycles_by_euler_enumeration():
    # The edges of the de Bruijn digraph are precisely the four-bit words.
    used = [False]*16
    outgoing = []
    circuits = set()

    def walk(state):
        if len(outgoing) == 16:
            if state == 0:
                cyclic = ('000' + ''.join(str(i) for i in outgoing))[:16]
                assert is_de_bruijn(cyclic)
                circuits.add(min(rotations(cyclic)))
            return
        for bit in (0, 1):
            edge = (state << 1) | bit
            if not used[edge]:
                used[edge] = True
                outgoing.append(bit)
                walk(edge & 7)
                outgoing.pop()
                used[edge] = False

    walk(0)
    return sorted(circuits)


def factor_cover_masks(word):
    # Each bit is one DISTINCT factor. A position's mask records all factors
    # for which an occurrence crosses that position.
    distinct = {}
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            f = word[i:j]
            distinct.setdefault(f, []).append((i, j))
    positions = [0]*len(word)
    for bit, occurrences in enumerate(distinct.values()):
        for i, j in occurrences:
            for p in range(i, j):
                positions[p] |= 1 << bit
    return positions, (1 << len(distinct)) - 1


def hits_all(positions, full, chosen):
    result = 0
    for p in chosen:
        result |= positions[p]
    return result == full


def optimum_with_witness(word):
    positions, all_factors = factor_cover_masks(word)
    if hits_all(positions, all_factors, COMPULSORY):
        return 4, COMPULSORY
    for chosen in combinations(range(len(word)), 5):
        if hits_all(positions, all_factors, chosen):
            return 5, chosen
    raise AssertionError('The asserted upper bound 5 fails')


def classify():
    direct = cycles_by_direct_enumeration()
    euler = cycles_by_euler_enumeration()
    assert direct == euler, 'Independent Euler and word-space enumerators disagree'
    assert len(direct) == 16, 'Incorrect number of binary order-four cycles'
    results = []
    histogram = Counter()
    for cycle in direct:
        profile = []
        for cut in range(LENGTH):
            shifted = cycle[cut:] + cycle[:cut]
            unfolded = shifted + shifted[:ORDER - 1]
            assert len(unfolded) == 19
            assert is_de_bruijn(shifted)
            minimum, witness = optimum_with_witness(unfolded)
            profile.append(minimum)
            histogram[minimum] += 1
            results.append((cycle, cut, minimum,
                            ','.join(str(pos + 1) for pos in witness)))
        assert profile.count(4) in (8, 12, 16)
    assert histogram == {4:192, 5:64}
    return results


def write_certificate(path):
    with open(path, 'w', newline='', encoding='utf-8') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(('canonical_cycle', 'cut_zero_based', 'gamma',
                         'witness_positions_one_based'))
        writer.writerows(classify())


def verify_certificate(path):
    actual = classify()  # independently rebuild every cyclic class and minimum
    with open(path, 'r', newline='', encoding='utf-8') as stream:
        read = csv.reader(stream, delimiter='\t')
        header = next(read)
        assert header == ['canonical_cycle', 'cut_zero_based', 'gamma',
                          'witness_positions_one_based']
        packaged = [(row[0], int(row[1]), int(row[2]), row[3]) for row in read]
    assert actual == packaged, 'Certificate differs from direct enumeration'
    cycle_histogram = Counter()
    for j in range(0, len(actual), 16):
        block = actual[j:j + 16]
        cycle_histogram[sum(row[2] == 4 for row in block)] += 1
    assert cycle_histogram == {8: 4, 12: 8, 16: 4}
    print('ORDER4_DEBRUIJN_ATTRACTOR_PASS cycles=16 cuts=256 min4=192 min5=64')
    print('cycle_robustness={8:4,12:8,16:4} exhaustive_words=65536')


if __name__ == '__main__':
    import sys
    path = Path(__file__).with_name('CUT_CERTIFICATE.tsv')
    if len(sys.argv) > 1 and sys.argv[1] == '--generate':
        write_certificate(path)
    else:
        verify_certificate(path)
