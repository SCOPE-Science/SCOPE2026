#!/usr/bin/env python3
"""Complete finite verification for cyclic scattered-subsequence coverage.

No dependencies beyond the Python standard library. Prints a deterministic summary.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def rotations(s):
    return (s[i:] + s[:i] for i in range(len(s)))


def normal(s):
    return min(rotations(s))


def necklaces(n):
    """Enumerate all length-n binary necklaces by complete word enumeration."""
    return sorted({normal(''.join(bits)) for bits in product('01', repeat=n)})


def subsequence(v, w):
    """True iff v is an ordinary (linear) scattered subsequence of w."""
    j = 0
    for c in w:
        if j < len(v) and c == v[j]:
            j += 1
    return j == len(v)


def scan_greedy(w, m):
    """Membership algorithm A: test all cyclic target classes against all cuts."""
    for v in necklaces(m):
        if not any(subsequence(v, cut) for cut in rotations(w)):
            return v
    return None


def scan_selection(w, m):
    """Independent algorithm B: enumerate all size-m index sets and rotate them."""
    if m > len(w):
        return '0' * m
    covered = set()
    for indices in combinations(range(len(w)), m):
        selected = ''.join(w[i] for i in indices)
        covered.update(rotations(selected))
        if len(covered) == 1 << m:
            return None
    for v in product('01', repeat=m):
        v = ''.join(v)
        if v not in covered:
            return v
    return None


def bound(w):
    n = len(w)
    assert set(w) == {'0', '1'}
    changes = sum(w[i] != w[(i + 1) % n] for i in range(n))
    return min(w.count('0'), w.count('1'), changes + 1)


def witness(w, v):
    """Return a cyclic embedding as one-based original positions."""
    n = len(w)
    ww = w + w
    for start in range(n):
        if w[start] != v[0]:
            continue
        indices = [start]
        j = start + 1
        for c in v[1:]:
            while j < start + n and ww[j] != c:
                j += 1
            if j >= start + n:
                break
            indices.append(j % n)
            j += 1
        if len(indices) == len(v):
            return tuple(i + 1 for i in indices)
    return None


def main():
    counts = []
    failures = []
    for n in range(2, 15):
        reps = necklaces(n)
        fresh_failures = []
        for w in reps:
            if len(set(w)) < 2:
                continue
            m = bound(w)
            miss_a = scan_greedy(w, m)
            miss_b = scan_selection(w, m)
            assert (miss_a is None) == (miss_b is None), (w, miss_a, miss_b)
            if miss_a is not None:
                fresh_failures.append((w, m, miss_a, miss_b))
        counts.append((n, len(reps), len(fresh_failures)))
        failures += fresh_failures
    assert failures == [('00000101111101', 7, '0010011', '0010011')], failures
    w = '00000101111101'
    assert scan_greedy(w, 6) is None
    assert scan_selection(w, 6) is None
    for a in (5, 6, 8, 12, 25):
        for b in (5, 7, 10, 13, 23):
            v = '0' * a + '10' + '1' * b + '01'
            assert bound(v) == 7
            assert scan_greedy(v, 7) == '0010011'
            assert scan_greedy(v, 6) is None
    print('ROTATIONAL_SUBSEQUENCE_BOUNDARY_PASS')
    print('n,necklaces,deficient:', counts)
    print('unique_deficient_necklace:', failures)
    print('witnesses_length6:')
    for v in necklaces(6):
        pos = witness(w, v)
        assert pos is not None, v
        print(v, ' '.join(map(str, pos)))
    print('two independent finite enumeration algorithms agreed')


if __name__ == '__main__':
    main()
