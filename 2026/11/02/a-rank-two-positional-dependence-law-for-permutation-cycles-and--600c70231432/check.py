#!/usr/bin/env python3
"""Exact finite verification of cycle-count/consecutive-triple covariance."""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb, factorial

PATTERNS = ('123', '132', '213', '231', '312', '321')

def numerator(pattern, n, i):
    assert 1 <= i <= n-2
    return {
        '123': 3*n-2,
        '132': 9*n-14-12*i,
        '213': 12*i-3*n-2,
        '231': 12*i-9*n+10,
        '312': 3*n-2-12*i,
        '321': 10-3*n,
    }[pattern]

def small_cycle_count(perm):
    seen = set()
    cycles = 0
    for start in range(1, len(perm)+1):
        if start not in seen:
            cycles += 1
            x = start
            while x not in seen:
                seen.add(x)
                x = perm[x-1]
    return cycles

def rankword(vals):
    ranks = [0, 0, 0]
    for rank, j in enumerate(sorted(range(3), key=lambda j: vals[j]), start=1):
        ranks[j] = rank
    return ''.join(map(str, ranks))

def small_forced_cycle_counts(n, i, pattern):
    pos = [i, i+1, i+2]
    ranks = [int(z) for z in pattern]
    one = 0
    for p, rank in zip(pos, ranks):
        one += comb(p-1, rank-1) * comb(n-p, 3-rank)
    two = 0
    for a, b, u in ((0,1,2),(0,2,1),(1,2,0)):
        if ranks[a] > ranks[b]:
            if ranks[u] == 1:
                two += pos[a]-1
            elif ranks[u] == 2:
                two += pos[b]-pos[a]-1
            else:
                two += n-pos[b]
    three = int(pattern in ('231','312'))
    return one, two, three


def verify():
    assertions = 0
    for n in range(3, 121):
        falling = n*(n-1)*(n-2)
        common = (n-1)*(n-2) + n*(n-2) + n*(n-1)
        # E[K]-H_(n-3) = 1/(n-2)+1/(n-1)+1/n;
        # the identity below has denominator 6*(n)_3.
        for i in range(1, n-1):
            for pat in PATTERNS:
                f1, f2, f3 = small_forced_cycle_counts(n,i,pat)
                assert 6*(f1+f2+f3)-common == numerator(pat,n,i)
                assertions += 1
            assert sum(numerator(p,n,i) for p in PATTERNS) == 0
            assertions += 1
            assert numerator('132',n,i)+numerator('231',n,i) == -4
            assertions += 1
            assert numerator('213',n,i)+numerator('312',n,i) == -4
            assertions += 1
            assert numerator('132',n,i) == numerator('213',n,n-1-i)
            assertions += 1
            assert numerator('231',n,i) == numerator('312',n,n-1-i)
            assertions += 1
    for n in range(3,9):
        counts = defaultdict(int)
        cycle_sums = defaultdict(int)
        total_cycles = 0
        for perm in permutations(range(1,n+1)):
            cc = small_cycle_count(perm)
            total_cycles += cc
            for i in range(1,n-1):
                pat=rankword(perm[i-1:i+2])
                counts[i,pat] += 1
                cycle_sums[i,pat] += cc
        for i in range(1,n-1):
            for pat in PATTERNS:
                assert counts[i,pat]*6 == factorial(n)
                assertions += 1
                cov = Fraction(cycle_sums[i,pat], factorial(n)) - Fraction(total_cycles*counts[i,pat],factorial(n)**2)
                expected = Fraction(numerator(pat,n,i), 6*n*(n-1)*(n-2))
                assert cov == expected, (n,i,pat,cov,expected)
                assertions += 1
    print('PASS', assertions, 'exact assertions; direct all-permutation enumeration through n=8')
    return assertions

if __name__ == '__main__':
    verify()
