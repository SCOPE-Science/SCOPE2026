#!/usr/bin/env python3
"""Reproduce the binary-arch transducer and Rudin--Shapiro prefix checks."""
from itertools import product

MORPH = ((0, 1), (0, 2), (3, 1), (3, 2))


def compose(left, right):
    """Weighted deterministic scanner: (arch counts, ending states)."""
    a, u = left
    b, v = right
    return (tuple(a[s] + b[u[s]] for s in range(3)),
            tuple(v[u[s]] for s in range(3)))


def single(letter):
    bit = letter // 2
    count, state = [], []
    for s in range(3):
        if s == 0:
            count.append(0)
            state.append(bit + 1)
        elif s == bit + 1:
            count.append(0)
            state.append(s)
        else:
            count.append(1)
            state.append(0)
    return tuple(count), tuple(state)


def block_formula(k, a):
    assert k >= 4 and a in range(4)
    if k % 2 == 0:
        b = 5 * (1 << (k - 4)) - 1
        offsets = ((0, 0, 1), (1, 1, 2),
                   (1, 2, 1), (0, 1, 0))
        endings = (2, 1, 2, 1)
    else:
        b = 5 * (1 << (k - 4))
        offsets = ((0, 0, 1), (-1, -1, 0),
                   (-1, 0, -1), (0, 1, 0))
        endings = (1, 2, 1, 2)
    return (tuple(b + d for d in offsets[a]), (endings[a],) * 3)


def morphic_prefix(k, a=0):
    word = [a]
    for _ in range(k):
        word = [b for x in word for b in MORPH[x]]
    return [x // 2 for x in word]


def rudin_shapiro_bit(n):
    return ((n & (n >> 1)).bit_count() & 1)


def greedy_count(word):
    arches = 0
    state = 0
    for bit in word:
        if state == 0:
            state = bit + 1
        elif state != bit + 1:
            arches += 1
            state = 0
    return arches


def subseq(word, pattern):
    j = 0
    for bit in word:
        if j < len(pattern) and bit == pattern[j]:
            j += 1
    return j == len(pattern)


def universality_by_definition(word):
    for j in range(len(word) // 2 + 1):
        if any(not subseq(word, pattern) for pattern in product((0, 1), repeat=j)):
            return j - 1
    return len(word) // 2


def verify():
    transforms = [single(a) for a in range(4)]
    for k in range(48):
        for a in range(4):
            for c in transforms[a][0]:
                assert abs(16 * c - 5 * (1 << k)) <= 16
        if k >= 4:
            for a in range(4):
                assert transforms[a] == block_formula(k, a), (k, a, transforms[a])
        if k <= 8:
            for a in range(4):
                bits = morphic_prefix(k, a)
                for s in range(3):
                    incoming = [] if s == 0 else [s - 1]
                    c = greedy_count(incoming + bits) - greedy_count(incoming)
                    assert c == transforms[a][0][s], (k, a, s)
        transforms = [compose(transforms[x], transforms[y]) for x, y in MORPH]
    print('VERIFY_OK 4_letter_weighted_transducers_k0_through_47_and_explicit_formulas_k_ge4')

    for k in range(1, 16):
        seq = morphic_prefix(k)
        assert seq == [rudin_shapiro_bit(n) for n in range(1 << k)], k
        expect = (0, 0, 1, 2)[k] if k <= 3 else (5 * (1 << (k - 4)) - (k % 2 == 0))
        assert greedy_count(seq) == expect, (k, expect)
    print('VERIFY_OK independent_dyadic_morphic_and_arithmetic_words_k1_through_15')

    for n in range(0, 13):
        for letters in product((0, 1), repeat=n):
            assert greedy_count(letters) == universality_by_definition(letters), letters
    print('VERIFY_OK defining_subsequence_universality_vs_arch_count_all_binary_words_n0_through_12')

    scans = 0
    missing = 0
    for n in range(1, 1 << 17):
        bit = rudin_shapiro_bit(n - 1)
        if missing == 0:
            missing = bit + 1
        elif missing != bit + 1:
            scans += 1
            missing = 0
        bound = n.bit_count()
        assert abs(16 * scans - 5 * n) <= 16 * bound, (n, scans)
        if n & (n - 1) == 0 and n >= 16:
            k = n.bit_length() - 1
            expected = 5 * (1 << (k - 4)) - (k % 2 == 0)
            assert scans == expected
    print('VERIFY_OK every_prefix_binary_weight_discrepancy_n1_through_131071')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
