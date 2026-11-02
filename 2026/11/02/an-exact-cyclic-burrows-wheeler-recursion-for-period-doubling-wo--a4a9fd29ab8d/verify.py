#!/usr/bin/env python3
"""Reproduce finite tests of a cyclic BWT transformation identity.

Only Python 3 standard library is required. The all-length results are proved
mathematically in RESULT.md; these computations are consistency checks.
"""
from itertools import product


def morphism(word):
    return ''.join('01' if symbol == '0' else '00' for symbol in word)


def direct_bwt(word):
    n = len(word)
    positions = sorted(range(n), key=lambda i: word[i:] + word[:i])
    return ''.join(word[(i - 1) % n] for i in positions)


def doubling_bwt(word):
    """Independent cyclic rank doubling, valid for nonprimitive words too."""
    n = len(word)
    positions = list(range(n))
    ranks = [ord(c) for c in word]
    width = 1
    while width < n:
        positions.sort(key=lambda i: (ranks[i], ranks[(i + width) % n]))
        new_rank = [0] * n
        level = 0
        for t in range(1, n):
            i, j = positions[t-1], positions[t]
            if (ranks[i], ranks[(i + width) % n]) != (ranks[j], ranks[(j + width) % n]):
                level += 1
            new_rank[j] = level
        ranks = new_rank
        width *= 2
    return ''.join(word[(i - 1) % n] for i in positions)


def flip(word):
    return word.translate(str.maketrans('01', '10'))


def run_count(word):
    return sum(i == 0 or word[i-1] != word[i] for i in range(len(word)))


def bwt_formula(word, old_bwt):
    zeros, ones = word.count('0'), word.count('1')
    return '1'*ones + '0'*ones + flip(old_bwt[:zeros][::-1]) + '0'*zeros


def check():
    checked_short = 0
    for n in range(2, 13):
        for symbols in product('01', repeat=n):
            word = ''.join(symbols)
            if '0' not in word or '1' not in word or '11' in word + word[0]:
                continue
            old_bwt = direct_bwt(word)
            new_bwt = direct_bwt(morphism(word))
            assert new_bwt == bwt_formula(word, old_bwt), (word, old_bwt, new_bwt)
            assert new_bwt == doubling_bwt(morphism(word)), word
            checked_short += 1

    word = '0'
    original_bwt = None
    checked_iterates = 0
    for m in range(1, 14):
        old = word
        word = morphism(word)
        assert len(word) == 2**m
        bwt = doubling_bwt(word)
        if m <= 10:
            assert bwt == direct_bwt(word)
        if m == 1:
            assert bwt == '10'
        else:
            assert bwt == bwt_formula(old, original_bwt)
            assert run_count(bwt) == 2*m-2
            prefix = bwt[:word.count('0')]
            assert prefix.startswith('1') and prefix.endswith('0')
            checked_iterates += 1
        original_bwt = bwt

    # Independently build exactly the BWT via its proved block recursion well
    # beyond feasible direct sorting: 20 substitution rounds, length 2**20.
    word = '01'
    current_bwt = '10'
    for m in range(2, 21):
        current_bwt = bwt_formula(word, current_bwt)
        word = morphism(word)
        assert len(current_bwt) == 2**m
        assert run_count(current_bwt) == 2*m-2
    print(f'VERIFY_OK cyclic_words={checked_short} sorted_iterates={checked_iterates} max_round=20')


if __name__ == '__main__':
    check()
