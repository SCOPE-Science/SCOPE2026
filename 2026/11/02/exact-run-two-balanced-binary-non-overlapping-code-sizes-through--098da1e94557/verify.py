#!/usr/bin/env python3
"""Definition-level verification of finite cross-bifix-free code certificates.

Run: python3 verify.py
Dependencies: Python standard library only.
"""
from itertools import product
from pathlib import Path
import json


def eligible(length):
    """Generate every balanced, cyclic run-two, unbordered binary word."""
    output = []
    for digits in product('01', repeat=length):
        word = ''.join(digits)
        if word.count('1') != length // 2:
            continue
        if any(word[i] == word[(i + 1) % length] == word[(i + 2) % length]
               for i in range(length)):
            continue
        if any(word[:j] == word[-j:] for j in range(1, length)):
            continue
        output.append(word)
    return output


def compatible(word_a, word_b):
    """Return whether distinct words may coexist in a non-overlapping code."""
    if word_a == word_b:
        return False
    n = len(word_a)
    for j in range(1, n):
        if word_a[:j] == word_b[-j:] or word_b[:j] == word_a[-j:]:
            return False
    return True


def dyck(r, restricted=True):
    out = []
    for bits in product('01', repeat=2*r):
        s = ''.join(bits)
        if s.count('1') != r:
            continue
        balance = 0
        valid = True
        for ch in s:
            balance += 1 if ch == '1' else -1
            if balance < 0:
                valid = False
                break
        if not valid:
            continue
        if any(s[i] == s[i+1] == s[i+2] for i in range(len(s)-2)):
            continue
        if restricted and (s.startswith('11') or s.endswith('00')):
            continue
        out.append(s)
    return out


def restricted_dyck_construction_size(length):
    """Section 5, Construction 7 / Proposition 13, run cap two."""
    m = (length - 2) // 2
    total = 0
    for i in range((m + 1)//2 + 1):
        total += len(dyck(i, False)) * len(dyck(m - i, True))
    if m % 2:
        total -= len(dyck((m - 1)//2, True))**2
    return total


def main():
    blob = json.loads(Path(__file__).with_name('certificates.json').read_text('utf-8'))
    assert blob['schema_version'] == 1
    required_lengths = [4, 6, 8, 10, 12, 14]
    assert [e['length'] for e in blob['cases']] == required_lengths
    maxima, construction = [], []
    for case in blob['cases']:
        n = case['length']
        words = eligible(n)
        assert len(words) == case['word_count']
        labels = case['color_labels']
        k = case['maximum']
        assert len(labels) == len(words)
        assert all(type(c) is int and 0 <= c < k for c in labels)
        assert set(labels) == set(range(k))
        # Upper bound: every color class is an incompatible family.
        # Consequently a non-overlapping code meets each color at most once.
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if labels[i] == labels[j]:
                    assert not compatible(words[i], words[j]), (n,i,j)
        witness = case['witness_words']
        assert len(witness) == k == len(set(witness))
        assert set(witness).issubset(set(words))
        # Matching lower bound: each pair of witness words is compatible.
        for i in range(len(witness)):
            for j in range(i+1, len(witness)):
                assert compatible(witness[i], witness[j]), (n,i,j)
        lower = restricted_dyck_construction_size(n)
        maxima.append(k)
        construction.append(lower)
        print(f'length={n} candidates={len(words)} upper={k} '
              f'witness={len(witness)} restricted_Dyck={lower}')
    assert maxima == [1, 2, 3, 5, 11, 24]
    assert construction == [1, 2, 3, 5, 11, 20]
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
