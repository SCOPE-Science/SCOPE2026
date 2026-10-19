#!/usr/bin/env python3
"""Exact factor-cover and independent digit-valuation tests for a word invariant.

Run: python3 verify_period_doubling.py [max_k]
The program checks a theorem at finitely many scales, not its induction proof.
"""
import sys
from collections import defaultdict


def morphism(word):
    return ''.join('01' if c == '0' else '00' for c in word)


def shifted_profiles(word, n):
    """(ones, weighted zero-based one-position sum) for each window."""
    if n > len(word):
        return set()
    bits = [int(c) for c in word]
    t = sum(bits[:n])
    j = sum(i * bits[i] for i in range(n))
    seen = set()
    for start in range(len(bits) - n + 1):
        seen.add((t, j))
        if start + n < len(bits):
            x, y = bits[start], bits[start + n]
            j = j - (t - x) + (n - 1) * y
            t = t - x + y
    return seen


def exact_cover(k):
    n = 3 << k
    # Each factor of length n lies in an image of one adjacent letter pair.
    r = k + 2
    zero, one = '0', '1'
    for _ in range(r):
        zero, one = morphism(zero), morphism(one)
    mapping = {'0': zero, '1': one}
    seen = set()
    for pair in ('00', '01', '10'):
        source = mapping[pair[0]] + mapping[pair[1]]
        seen.update(shifted_profiles(source, n))
    return seen, mapping


def expectation(k, signatures):
    center = 1 << k
    groups = defaultdict(set)
    for t, j in signatures:
        groups[t].add(j)
    assert sorted(groups) == [center - 1, center, center + 1], (k, sorted(groups))
    assert len(groups[center - 1]) == center
    assert len(groups[center + 1]) == center
    low = (center * (3 * center - k - 3)) // 2
    assert 3 * center - k - 3 >= 0
    assert groups[center] == set(range(low, low + (k + 3) * center, center))
    assert len(signatures) == 2 * center + k + 3
    return tuple((weight, len(groups[weight])) for weight in sorted(groups))


def v2_parity(n):
    n += 1
    degree = 0
    while n % 2 == 0:
        n //= 2
        degree += 1
    return degree % 2


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    assert 0 <= limit <= 16
    assert shifted_profiles('01000101', 3) == {(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)}
    for k in range(limit + 1):
        signatures, mapping = exact_cover(k)
        weights = expectation(k, signatures)
        if k <= 10:
            # This independently generates prefix symbols from the 2-adic valuation.
            L = len(mapping['0'])
            direct = ''.join(str(v2_parity(i)) for i in range(4 * L))
            assert direct[:8] == '01000101'
            source = '0'
            for _ in range(k + 4):
                source = morphism(source)
            assert direct == source
            assert shifted_profiles(direct, 3 << k) == signatures
        print(f'k={k:02d} n={3<<k:6d} classes={len(signatures):6d} groups={weights}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
