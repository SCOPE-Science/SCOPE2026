#!/usr/bin/env python3
"""Exact finite calculations for binary scattered-pair profile collisions.

Uses two independent enumeration methods (direct word enumeration for small n,
and a length/composition/inversion dynamic program for larger n).
No external packages or services are required.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb, sqrt, pi


def profile(word):
    """2-binomial profile: number of ones and of ordered 10 subsequences."""
    ones = inv = 0
    for bit in word:
        if bit:
            ones += 1
        else:
            inv += ones
    return ones, inv


def complete_deck(word):
    # Independently enumerate every length-one and length-two subsequence.
    counts = [0] * 6
    n = len(word)
    for i in range(n):
        counts[word[i]] += 1
        for j in range(i+1,n):
            counts[2+2*word[i]+word[j]] += 1
    return tuple(counts)


def brute(n):
    counts = Counter()
    for mask in range(2 ** n):
        bits = [(mask >> j) & 1 for j in range(n)]
        counts[profile(bits)] += 1
    return counts


def get_dp_rows(ns):
    ns = set(ns)
    nmax = max(ns)
    hist = [{0: 1}]
    for n in range(1, nmax + 1):
        newer = [defaultdict(int) for _ in range(n + 1)]
        for k, items in enumerate(hist):
            for inv, count in items.items():
                newer[k][inv+k] += count        # append zero
                newer[k+1][inv] += count        # append one
        hist = [dict(h) for h in newer]
        if n in ns:
            yield n, hist


def cross_collision(hist, n, p, q):
    total = 0.0
    for k, inv_counts in enumerate(hist):
        sq = sum(v * v for v in inv_counts.values())
        # Multiplies exact profile-pair counts by the two word probabilities.
        term = sq * ((p*q)**k) * (((1-p)*(1-q)) ** (n-k))
        total += term
    return total


def predicted(n, p, q):
    a = sqrt(p*q)
    b = sqrt((1-p)*(1-q))
    affinity = a+b
    theta = a/affinity
    return (affinity ** (2*n)) * sqrt(3)/(2*pi*theta*(1-theta)*n*n)


def main():
    test_ns = [2,3,4,5,6,7,8,9,10,12,15,20,30,40,60,80,120,160]
    cases = [(0.5,0.5),(0.25,0.25),(0.3,0.65),(0.1,0.8)]
    for n, hist in get_dp_rows(test_ns):
        d = Counter({(k,inv):v for k,row in enumerate(hist) for inv,v in row.items()})
        if n<=12:
            assert d==brute(n), f'dp disagrees with direct enumeration at n={n}'
        if n<=10:
            by_deck = defaultdict(set)
            by_profile = defaultdict(set)
            for mask in range(2**n):
                word = [(mask >> i) & 1 for i in range(n)]
                by_deck[complete_deck(word)].add(mask)
                by_profile[profile(word)].add(mask)
            assert set(map(frozenset, by_deck.values())) == set(map(frozenset, by_profile.values()))
        assert sum(sum(row.values()) for row in hist)==2**n
        assert sum(sum(row.values()) for row in hist if True)==2**n
        for k,row in enumerate(hist):
            assert sum(row.values())==comb(n,k)
        if n in (10,20,40,80,120,160):
            for p,q in cases:
                c = cross_collision(hist,n,p,q)
                a = predicted(n,p,q)
                print(f'n={n:3d} p={p:.2f} q={q:.2f} collision={c:.10g} ratio_to_asymptotic={c/a:.8f}')
        if n<=10:
            # Exact rational independent weighting of profile counts.
            p=Fraction(1,4);q=Fraction(3,4)
            direct = sum(c*c * (p*q)**k * ((1-p)*(1-q))**(n-k) for (k,iv),c in brute(n).items())
            dp = sum(c*c * (p*q)**k * ((1-p)*(1-q))**(n-k) for (k,iv),c in d.items())
            assert direct==dp
    print('Independent full-deck comparison for n <= 10 and profile counting for n <= 12: PASS')
    print('All exact DP, binomial composition, rational weighting checks passed.')

if __name__=='__main__':main()
