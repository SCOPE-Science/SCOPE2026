#!/usr/bin/env python3
"""Reproducible checks for binary one-gap pair-deck profile growth."""
from itertools import product
from math import comb, gcd


def profile(word):
    """One-symbol counts followed by four exact ordered gapped-pair counts."""
    n = len(word)
    counts = [0, 0, 0, 0]
    for p in range(n):
        for q in range(p + 2, n):
            counts[2 * word[p] + word[q]] += 1
    return (word.count(0), word.count(1), *counts)


def compression(word):
    """The sufficient four-parameter statistics in the proof."""
    n = len(word)
    k = sum(word)
    runs = 1 + sum(word[i] != word[i + 1] for i in range(n - 1))
    first = word[0]
    zeros = 0
    ordinary01 = 0
    for bit in word:
        if bit == 0:
            zeros += 1
        else:
            ordinary01 += zeros
    return k, runs, first, ordinary01


def profile_via_compression(n, stat):
    k, runs, first, ordinary01 = stat
    zeros = n-k
    r0 = (runs + (1 if first == 0 else 0)) // 2
    r1 = runs-r0
    # Count transitions at alternating boundaries of constant runs.
    a01 = (runs//2) if first == 0 else ((runs-1)//2)
    a10 = (runs//2) if first == 1 else ((runs-1)//2)
    return (zeros, k, comb(zeros,2)-(zeros-r0), ordinary01-a01,
            k*zeros-ordinary01-a10, comb(k,2)-(k-r1))


def witness(m, n, s, h, a, d):
    b, c, A, B = 8*m, 8*m+1, 4*m, 4*m
    H0 = n-(24*m+1+2*s+h)
    assert H0 >= 1 and 1 <= a < A and 1 <= d < B
    w = (0,)*(H0+a) + (1,)*b + (0,)*(A-a)
    w += (1,0)*s
    w += (1,)*d + (0,)*c + (1,)*(h+B-d)
    assert len(w)==n
    return w


def main():
    seen = {}
    for n in range(1, 13):
        direct = set()
        compressed = {}
        for word in product((0,1), repeat=n):
            p = profile(word)
            stat = compression(word)
            assert p == profile_via_compression(n, stat), (n,word,p,stat)
            direct.add(p)
            assert stat not in compressed or compressed[stat] == p
            compressed[stat] = p
        assert len(direct) <= 2*n*(n+1)*(n*n//4+1)
        seen[n]=len(direct)
    assert {n:seen[n] for n in range(2,13)} == {
        2:3,3:8,4:16,5:32,6:61,7:118,8:202,9:356,
        10:559,11:874,12:1296}
    print('Exhaustive profiles and sufficient statistics through n=12:',seen)
    for m in range(1,6):
        n=100*m
        assert gcd(8*m,8*m+1)==1
        found=set()
        for s in range(m,2*m+1):
            for h in range(m,10*m+1):
                for a in range(1,4*m):
                    for d in range(1,4*m):
                        w=witness(m,n,s,h,a,d)
                        stat=compression(w)
                        expected_k=12*m+s+h
                        expected_r=2*s+6
                        assert stat[0] == expected_k and stat[1] == expected_r
                        found.add(stat)
                        if m <= 2:
                            assert profile(w)==profile_via_compression(n,stat)
        expected=(m+1)*(9*m+1)*(4*m-1)**2
        assert len(found)==expected, (m,len(found),expected)
        print('m,n,witnesses and distinct compressed decks:',m,n,len(found))
    print('All assertions passed. This finite check supplements, not replaces, the general proof.')


if __name__ == '__main__':
    main()
