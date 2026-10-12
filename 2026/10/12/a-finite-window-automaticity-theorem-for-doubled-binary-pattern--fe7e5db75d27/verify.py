#!/usr/bin/env python3
"""Finite cross-checks for a binary pattern-counting theorem."""
from itertools import product


def occurrence_parity(pattern, n):
    assert n >= 0
    word = format(n, 'b')
    zeros = len(pattern) - len(pattern.lstrip('0'))
    if '1' in pattern:
        word = '0' * zeros + word
    return sum(word[i:i+len(pattern)] == pattern for i in range(len(word)-len(pattern)+1)) % 2


def scan_parity(pattern, n):
    # Independent, least-significant-bit-first pattern matcher.
    rev = pattern[::-1]
    s = format(n, 'b')[::-1]
    if '1' in pattern:
        s += '0' * (len(pattern) - len(pattern.lstrip('0')))
    count = 0
    for i in range(len(s)-len(rev)+1):
        count ^= int(s[i:i+len(rev)] == rev)
    return count


def first_failure(pattern, d, max_steps=8192):
    base = occurrence_parity(pattern, 0)
    for j in range(1, max_steps+1):
        if occurrence_parity(pattern, j*d) != base:
            return j
    return None


def shortcut(pattern, d):
    m = len(pattern)-1
    mod = 1 << m
    r = int(pattern[:-1], 2) if m else 0
    t = next((j for j in range(1, mod+1) if j*d % mod == r), None)
    if t is None:
        return True
    base = occurrence_parity(pattern, 0)
    return any(occurrence_parity(pattern, j*d) != base for j in range(1, t))


def main():
    tests = 0
    appends = 0
    for k in range(2, 7):
        for head in product('01', repeat=k-1):
            v = ''.join(head)+'0'
            if '1' not in v:
                continue
            for n in range(1, 513):
                x = occurrence_parity(v, n)
                assert x == scan_parity(v, n)
                delta = int(n % (1 << (k-1)) == int(v[:-1], 2))
                assert occurrence_parity(v, 2*n) == (x ^ delta)
                appends += 1
            for d in range(1, 160):
                a = first_failure(v, d)
                b = first_failure(v, 2*d)
                assert a is not None and b is not None
                assert shortcut(v, d) == (a == b), (v, d, a, b)
                tests += 1
    assert all(shortcut('10', d) == (d % 2 == 0) for d in range(1, 1001))
    for d in range(1, 1001):
        b = (d % 4 == 0) or (d % 2 == 1 and occurrence_parity('100', d) == 1)
        assert shortcut('100', d) == b
    print(f'VERIFY_OK positive_pattern_doubling_cases={tests} append_checks={appends} two_explicit_families=2000')

if __name__ == '__main__':
    main()
