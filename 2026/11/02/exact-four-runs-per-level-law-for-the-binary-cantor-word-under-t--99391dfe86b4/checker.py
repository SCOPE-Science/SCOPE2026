#!/usr/bin/env python3
"""Standalone finite corroboration of the binary Cantor BWT theorem.

Requires Python 3 and only standard-library modules. These tests corroborate,
but do not replace, the proof applying to all substitution levels.
"""
from itertools import groupby


def iterate(word):
    return ''.join('101' if ch == '1' else '000' for ch in word)


def bwt_doubling(word):
    """Cyclic suffix doubling: lexicographically sorted cyclic rotations."""
    n = len(word)
    inds = list(range(n))
    ranks = [int(ch) for ch in word]
    d = 1
    while d < n:
        inds.sort(key=lambda i: (ranks[i], ranks[(i+d) % n]))
        new = [0] * n
        for z in range(1, n):
            prev, curr = inds[z-1], inds[z]
            left = (ranks[prev], ranks[(prev+d) % n])
            right = (ranks[curr], ranks[(curr+d) % n])
            new[curr] = new[prev] + (left != right)
        ranks = new
        d *= 2
    return inds, ''.join(word[(i-1) % n] for i in inds)


def bwt_literal(word):
    return ''.join(word[(i-1) % len(word)] for i in
                   sorted(range(len(word)), key=lambda i: word[i:] + word[:i]))


def nruns(word):
    return sum(1 for _ in groupby(word))


def leading_zeros(word, i):
    n = len(word)
    t = 0
    while word[(i+t) % n] == '0':
        t += 1
    return t


def check():
    word = '1'
    checked_lengths = []
    for k in range(10):
        n = len(word)
        order, bw = bwt_doubling(word)
        assert len(order) == len(set(order)) == n
        assert n == 3**k and word.count('1') == 2**k
        assert nruns(bw) == (1 if k == 0 else 2 if k == 1 else 4*k), (k, bw)
        if k >= 1:
            assert nruns(word) == 2**(k+1)-1
        if k <= 5:
            assert bw == bwt_literal(word)
        if k >= 2:
            groups = {}
            for pos, ch in zip(order, bw):
                t = leading_zeros(word, pos)
                groups.setdefault(t, []).append(ch)
            for a in range(k):
                t = 3**a
                H = 2**(k-a-1)
                assert ''.join(groups[t]) == '1'*(H-1)+'0'*(H-1)+'1', (k, a)
            for t, chars in groups.items():
                if t > 0 and t not in {3**a for a in range(k)}:
                    assert set(chars) == {'0'}, (k, t)
            first = ''.join(groups[0])
            assert first.startswith('0') and first.endswith('0')
            assert first.count('1') == 1
        checked_lengths.append(n)
        word = iterate(word)
    print('CHECKS_PASS levels=0..9 lengths=', checked_lengths)
    print('exact_formula_and_blocks_verified_for_levels=2..9')
    print('independent_literal_BWT_verified_for_levels=0..5')


if __name__ == '__main__':
    check()
