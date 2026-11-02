#!/usr/bin/env python3
"""Exact finite verification of Abelian-border-free cyclic rotations.

Run with Python 3: python verify.py
No third-party modules or input files.
"""
from collections import Counter
from math import gcd

MAX_N = 16
EXPECTED = (
    '0010101100110011',
    '0010101100110101',
    '0010101101010011',
    '0010110011001101',
    '0010110100110011',
    '0011001100110101',
)


def conjugates(w):
    return (w[i:] + w[:i] for i in range(len(w)))


def is_primitive(w):
    n = len(w)
    return all(w != w[:d] * (n // d)
               for d in range(1, n) if n % d == 0)


def unbordered_by_slices(u):
    n = len(u)
    return all(u[:k].count('1') != u[-k:].count('1')
               for k in range(1, n // 2 + 1))


def no_abelian_unbordered_rotation_by_slices(w):
    return all(not unbordered_by_slices(u) for u in conjugates(w))


def no_abelian_unbordered_rotation_by_height(w):
    """Independent circular-height formulation, with centered differences."""
    n = len(w)
    ones = w.count('1')
    h = [0]
    for j, letter in enumerate(w, 1):
        h.append(h[-1] + n * (letter == '1') - ones)
    assert h[-1] == 0
    for start in range(n):
        exists_border = False
        for k in range(1, n // 2 + 1):
            if h[(start + k) % n] + h[(start - k) % n] == 2 * h[start]:
                exists_border = True
                break
        if not exists_border:
            return False
    return True


def canonical_rotation(w):
    return min(conjugates(w))


def first_border_lengths(w):
    result = []
    for v in conjugates(w):
        witnesses = [k for k in range(1, len(w) // 2 + 1)
                     if v[:k].count('1') == v[-k:].count('1')]
        result.append(min(witnesses) if witnesses else None)
    return result


def main():
    count_by_n = {}
    classes = set()
    counts_by_content = Counter()
    for n in range(1, MAX_N + 1):
        count = 0
        for integer in range(1 << n):
            word = f'{integer:0{n}b}'
            if not is_primitive(word):
                continue
            direct = no_abelian_unbordered_rotation_by_slices(word)
            height = no_abelian_unbordered_rotation_by_height(word)
            assert direct == height, ('independent disagreement', n, word)
            if direct:
                count += 1
                assert gcd(n, word.count('1')) > 1
                if n == MAX_N:
                    classes.add(canonical_rotation(word))
                    counts_by_content[word.count('1')] += 1
        count_by_n[n] = count
    assert all(count_by_n[n] == 0 for n in range(1, MAX_N))
    assert count_by_n[MAX_N] == 96
    assert tuple(sorted(classes)) == EXPECTED
    assert counts_by_content == Counter({8: 96})
    assert len(classes) == 6
    for w in EXPECTED:
        assert is_primitive(w)
        assert all(v is not None for v in first_border_lengths(w))
        assert len(set(conjugates(w))) == MAX_N
    print('FIRST_LENGTH', MAX_N)
    print('PRIMITIVE_LABELED', count_by_n[MAX_N])
    print('CYCLIC_CLASSES', len(classes))
    print('BIT_COUNTS', dict(counts_by_content))
    print('ZERO_COUNTS_1_TO_15', [count_by_n[n] for n in range(1, MAX_N)])
    for w in EXPECTED:
        print(w, 'MINIMAL_BORDER_LENGTHS', ' '.join(map(str, first_border_lengths(w))))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
