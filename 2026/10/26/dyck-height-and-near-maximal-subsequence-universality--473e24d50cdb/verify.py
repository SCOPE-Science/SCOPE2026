#!/usr/bin/env python3
"""Independent finite checks for Dyck-path subsequence universality statements."""
from itertools import product
from math import comb

def dyck_words(n):
    def visit(prefix, zeros, ones):
        if ones == n:
            yield prefix
            return
        if zeros < n:
            yield from visit(prefix + '0', zeros + 1, ones)
        if ones < zeros:
            yield from visit(prefix + '1', zeros, ones + 1)
    yield from visit('', 0, 0)

def greedy_index(w):
    seen = None
    count = 0
    for c in w:
        if seen is None:
            seen = c
        elif c != seen:
            count += 1
            seen = None
    return count

def embeds(source, target):
    cursor = 0
    for c in source:
        if cursor < len(target) and c == target[cursor]:
            cursor += 1
    return cursor == len(target)

def direct_index(w):
    value = 0
    for k in range(1, len(w)//2 + 2):
        if all(embeds(w, ''.join(t)) for t in product('01', repeat=k)):
            value = k
        else:
            break
    return value

def height(w):
    level = high = 0
    for c in w:
        level += 1 if c == '0' else -1
        assert level >= 0
        high = max(high, level)
    assert level == 0
    return high

def explicit_near_max(n):
    for a in range(n-1):
        b = n-2-a
        for choice in product(('01', '10'), repeat=b):
            yield '01'*a + '001' + ''.join(choice) + '1'

if __name__ == '__main__':
    cases = 0
    directly_compared = 0
    for n in range(1, 13):
        listed = set(dyck_words(n))
        assert len(listed) == comb(2*n, n)//(n+1)
        top = set()
        for w in listed:
            i = greedy_index(w)
            h = height(w)
            assert i <= n-h+1, (w, n, i, h)
            assert (i >= n-1) == (h <= 2), (w, n, i, h)
            if i >= n-1:
                top.add(w)
            if n <= 8:
                assert i == direct_index(w), (w, i, direct_index(w))
                directly_compared += 1
            cases += 1
        expected = set(explicit_near_max(n)) if n >= 2 else set()
        assert {w for w in top if greedy_index(w)==n-1} == expected
        assert len(top) == 2**(n-1)
        assert len(expected) == 2**(n-1)-1
        assert sum(greedy_index(w)==n for w in listed) == 1
        for h in range(1, n+1):
            witness = '0'*h+'1'*h+'01'*(n-h)
            assert height(witness)==h
            assert greedy_index(witness)==n-h+1
    print(f'DYCK_UNIVERSALITY_PASS dyck_cases={cases} direct_subsequence_crosschecks={directly_compared} semilengths=1..12 near_max_bijection=PASS sharp_height_bound=PASS')
