#!/usr/bin/env python3
"""Reproducible finite checks for simultaneous ordinary/alternating cyclic minima.

All comparisons use explicit cyclic rotations. This program checks finite instances,
not the all-length theorem or asymptotic conclusions.
"""
from itertools import combinations
from math import comb, gcd


def alternate_key(word):
    """1-based odd positions use 0<1; even positions use 1<0."""
    return tuple((int(x) if i % 2 == 0 else 1-int(x))
                 for i, x in enumerate(word))


def all_orbits(n, k):
    """Iterate fixed-content necklaces, each as its sorted cyclic representatives."""
    seen = set()
    for holes in combinations(range(n), k):
        word = ''.join('0' if j in holes else '1' for j in range(n))
        rotations = {word[j:] + word[:j] for j in range(n)}
        rep = min(rotations)
        if rep not in seen:
            seen.add(rep)
            yield rotations


def cyclic_gaps(word):
    """Number of ones after each circular zero, ordered from word's first zero."""
    assert word[0] == '0'
    gaps = []
    count = 0
    for ch in word[1:] + '0':
        if ch == '1':
            count += 1
        else:
            gaps.append(count)
            count = 0
    return gaps


def primitive_count_formula(n, k):
    def mobius(d):
        ps = 0
        j = 2
        while j*j <= d:
            if d % j == 0:
                d //= j
                ps += 1
                if d % j == 0:
                    return 0
                while d % j == 0:
                    d //= j
            j += 1
        if d > 1:
            ps += 1
        return (-1)**ps
    return sum(mobius(d)*comb(n//d, k//d)
               for d in range(1, gcd(n,k)+1)
               if gcd(n,k) % d == 0) // n


def unique_odd_count_formula(n, k):
    """Coefficient of z^(3k-1)/((1-z)^(k-1)(1-z^(2k)))."""
    if n < 3*k-1:
        return 0
    return sum(comb(n-(3*k-1)-2*k*j+k-2, k-2)
               for j in range((n-(3*k-1))//(2*k)+1))


def coincident_k3_formula(n):
    return sum(max(n-6-6*j, 0) for j in range((n-1)//6+1))


def run():
    visited = 0
    for n in range(2, 25):
        for k in range(1, min(5, n-1)+1):
            primitive = agree = unique_odd = 0
            for rotations in all_orbits(n, k):
                if len(rotations) != n:
                    continue
                visited += 1
                primitive += 1
                ordinary = min(rotations)
                alternative = min(rotations, key=alternate_key)
                if ordinary == alternative:
                    agree += 1
                gaps = cyclic_gaps(ordinary)
                if k >= 2 and min(gaps) % 2 == 1 and gaps.count(min(gaps)) == 1:
                    unique_odd += 1
                    assert ordinary == alternative, (n, k, ordinary, gaps)
                if k >= 2 and (min(gaps) % 2 == 0 or min(gaps) == 0):
                    assert ordinary != alternative, (n, k, ordinary, gaps)
                if 2 <= k <= 3 and min(gaps) > 0:
                    assert (ordinary == alternative) == (min(gaps) % 2 == 1), (n, k, ordinary, gaps)
            assert primitive == primitive_count_formula(n, k), (n, k, primitive)
            if k >= 2:
                assert unique_odd == unique_odd_count_formula(n, k), (n,k,unique_odd)
            if k == 1:
                assert agree == 1
            if k == 2:
                assert agree == (n-1)//4, (n,k,agree)
            if k == 3:
                assert agree == coincident_k3_formula(n), (n,k,agree)
    # Count linear binary words with no adjacent zeros across the circular boundary.
    for n in range(3, 17):
        for k in range(1, n//2+1):
            actual = 0
            for zeros in combinations(range(n), k):
                if all((i+1) % n not in zeros for i in zeros):
                    actual += 1
            assert actual * (n-k) == n*comb(n-k,k), (n,k,actual)
    print('VERIFY_OK', 'primitive-necklace instances:', visited,
          'range: 2<=n<=24, 1<=k<=5; exact sparse and cyclic-avoidance formulas')


if __name__ == '__main__':
    run()
