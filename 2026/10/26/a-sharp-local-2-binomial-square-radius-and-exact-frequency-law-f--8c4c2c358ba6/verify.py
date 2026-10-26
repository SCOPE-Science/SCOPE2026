#!/usr/bin/env python3
"""Reproduce the complete Thue--Morse local 2-binomial square classification.

Run: python3 verify.py
Requires only Python's standard library and templates.csv alongside this file.
"""
import csv
from collections import Counter
from fractions import Fraction
from pathlib import Path

LEVEL = 7
BLOCK = 1 << LEVEL
BOUND = 36
WINDOW = 2 * BOUND
PAIR_ORDER = ('00', '01', '10', '11')
ROOT_ORDER = (1, 2, 3, 4, 6, 10, 12, 28, 36)
TABLE = {
    '00': (42, 22, 12, 32, 4, 6, 8, 0, 2),
    '01': (43, 21, 10, 32, 6, 5, 8, 2, 1),
    '10': (43, 21, 10, 32, 6, 5, 8, 2, 1),
    '11': (42, 22, 12, 32, 4, 6, 8, 0, 2),
}
DENSITY = {
    1: Fraction(1, 3), 2: Fraction(1, 6),
    3: Fraction(1, 12), 4: Fraction(1, 4),
    6: Fraction(1, 24), 10: Fraction(1, 24),
    12: Fraction(1, 16), 28: Fraction(1, 96),
    36: Fraction(1, 96),
}
PAIR_FREQUENCY = {'00': Fraction(1, 6), '01': Fraction(1, 3),
                  '10': Fraction(1, 3), '11': Fraction(1, 6)}


def morph(w, k):
    for _ in range(k):
        w = ''.join('01' if c == '0' else '10' for c in w)
    return w


def signature(w):
    return (w.count('1'), sum(j for j, c in enumerate(w) if c == '1'))


def explicit_subseq_signature(w):
    # [#0,#1,#00,#01,#10,#11], counting NONCONTIGUOUS subsequences.
    n0 = n1 = n00 = n01 = n10 = n11 = 0
    for c in w:
        if c == '0':
            n00 += n0
            n10 += n1
            n0 += 1
        else:
            n01 += n0
            n11 += n1
            n1 += 1
    return n0, n1, n00, n01, n10, n11


def least_root(w, comparison):
    assert len(w) == WINDOW
    for m in range(1, BOUND + 1):
        if comparison(w[:m]) == comparison(w[m:2*m]):
            return m
    return None


def generate():
    out = []
    for pair in PAIR_ORDER:
        two_blocks = morph(pair, LEVEL)
        assert len(two_blocks) == 2 * BLOCK
        for offset in range(BLOCK):
            w = two_blocks[offset:offset + WINDOW]
            assert len(w) == WINDOW
            root_fast = least_root(w, signature)
            root_independent = least_root(w, explicit_subseq_signature)
            assert root_fast == root_independent, (pair, offset)
            assert root_fast in ROOT_ORDER, (pair, offset, root_fast)
            out.append((pair, offset, root_fast))
    return out


def main():
    records = generate()
    csvpath = Path(__file__).resolve().with_name('templates.csv')
    with csvpath.open(newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        assert next(reader) == ['source_pair', 'offset', 'least_root']
        saved = [(row[0], int(row[1]), int(row[2])) for row in reader]
    assert saved == records

    assert len(records) == 4 * BLOCK == 512
    by_pair = {pair: Counter(root for p, _, root in records if p == pair)
               for pair in PAIR_ORDER}
    assert all(tuple(by_pair[p][r] for r in ROOT_ORDER) == TABLE[p]
               for p in PAIR_ORDER)
    assert all(sum(by_pair[p].values()) == BLOCK for p in PAIR_ORDER)

    distribution = {
        root: sum((PAIR_FREQUENCY[p] * by_pair[p][root] / BLOCK
                   for p in PAIR_ORDER), Fraction(0))
        for root in ROOT_ORDER
    }
    assert distribution == DENSITY
    assert sum(distribution.values()) == 1
    max_offsets = [(p, offset) for p, offset, root in records if root == BOUND]
    assert max_offsets == [('00', 19), ('00', 83), ('01', 19),
                           ('10', 19), ('11', 19), ('11', 83)]

    # Independent arithmetic construction: t(i) is parity of binary digit sum.
    prefix = ''.join(str(i.bit_count() % 2) for i in range((1 << 15) + WINDOW))
    assert prefix[:1 << 15] == morph('0', 15)
    factors = {prefix[i:i+WINDOW] for i in range(1 << 15)}
    two_block_factors = {
        morph(pair, LEVEL)[offset:offset+WINDOW]
        for pair in PAIR_ORDER for offset in range(BLOCK)
    }
    assert factors == two_block_factors
    assert len(factors) == 220
    seen_roots = Counter()
    for i in range(1 << 13):
        root = least_root(prefix[i:i + WINDOW], explicit_subseq_signature)
        # Obtain the source pair independently from digit-sum parity.
        p = ''.join(str(j.bit_count() % 2)
                    for j in (i // BLOCK, i // BLOCK + 1))
        stored = records[PAIR_ORDER.index(p) * BLOCK + i % BLOCK][2]
        assert root == stored, (i, root, stored)
        seen_roots[root] += 1

    # The sharpness witness is already at the nineteenth starting position.
    witness = prefix[19:19+WINDOW]
    assert least_root(witness, signature) == 36
    assert least_root(witness, explicit_subseq_signature) == 36
    assert signature(witness[:36]) == signature(witness[36:]) == (18, 297)

    print('VERIFY_OK 512_complete_aligned_templates=4_pairs_x_128_offsets')
    print('VERIFY_OK independent_2_binomial_subsequence_count_agrees_all_templates')
    print('VERIFY_OK root_levels=' + ','.join(map(str, ROOT_ORDER)))
    print('VERIFY_OK frequency_spectrum=' + ','.join(
        f'{r}:{DENSITY[r]}' for r in ROOT_ORDER))
    print('VERIFY_OK sharp_bound_36_occurs_at_six_aligned_templates')
    print('VERIFY_OK arithmetic_prefix_vs_morphism_and_8192_starting_positions')
    print('VERIFY_OK length72_factor_set=220, reconstructed_independently')
    print('VERIFY_OK witness_index19_root36_and_blocks_signature=(18,297)')


if __name__ == '__main__':
    main()
