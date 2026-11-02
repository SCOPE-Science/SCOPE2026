"""Exact finite checks for peak counts and zero-return counts in Bernoulli bridges.

Run with: python3 bridge_peak_verifier.py
Requires only the Python standard library. The theorems for all n are analytical;
these finite checks exercise definitions, boundary cases, and algebraic formulas.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def return_count_and_peaks(ups, n):
    ups = set(ups)
    increments = [1 if i in ups else -1 for i in range(2*n)]
    height, returns = 0, 0
    for i, inc in enumerate(increments, 1):
        height += inc
        if i < 2*n and height == 0:
            returns += 1
    assert height == 0
    peaks = sum(a == 1 and b == -1 for a, b in zip(increments, increments[1:]))
    return returns, peaks, frozenset(i for i in range(1, n) if sum(increments[:2*i]) == 0)


def bridge_count_with_returns(n, r):
    return Fraction(r+1,n) * 2**(r+1) * comb(2*n-r-2,n-r-1)


def regression(n, r):
    assert n >= 2 and 0 <= r < n
    return Fraction(n-1, 2) + Fraction(r*(r+2), 4*(2*n-r-2))


def verify():
    checks = 0
    paths_checked = 0
    for n in range(1, 10):
        table = defaultdict(lambda: [0, 0])
        subset_counts = defaultdict(lambda: [0,0])
        for ups in combinations(range(2*n),n):
            r, p, zero_set = return_count_and_peaks(ups,n)
            paths_checked += 1
            table[r][0] += 1
            table[r][1] += p
            if n <= 7:
                for subset_size in range(len(zero_set)+1):
                    for subset in combinations(sorted(zero_set), subset_size):
                        subset_counts[subset][0] += 1
                        subset_counts[subset][1] += p
        total=comb(2*n,n)
        assert sum(v[0] for v in table.values()) == total
        checks += 1
        assert sum(v[1] for v in table.values()) == total*n//2 or Fraction(sum(v[1] for v in table.values()),total) == Fraction(n,2)
        checks += 1
        for r in range(n):
            count, peak_sum = table[r]
            assert count == bridge_count_with_returns(n,r)
            checks += 1
            if n >= 2:
                assert Fraction(peak_sum,count) == regression(n,r)
                checks += 1
        if n >= 3:
            for r in range(n-2):
                assert regression(n,r+1) > regression(n,r)
                checks += 1
            for r in range(n-3):
                assert regression(n,r+2)-regression(n,r+1) > regression(n,r+1)-regression(n,r)
                checks += 1
        mean_returns = sum(r*v[0] for r,v in table.items())
        assert Fraction(mean_returns,total) == Fraction(4**n,total)-2
        checks += 1
        mean_peaks = Fraction(sum(v[1] for v in table.values()),total)
        assert mean_peaks == Fraction(n,2)
        checks += 1
        mixed = Fraction(sum(r*v[1] for r,v in table.items()),total)
        cov = mixed-mean_peaks*Fraction(mean_returns,total)
        assert cov == Fraction(mean_returns,4*total)
        checks += 1
        if n <= 7:
            for subset,(count, peak_sum) in subset_counts.items():
                assert Fraction(peak_sum,count) == Fraction(n,2) + Fraction(len(subset),4)
                checks += 1
    # Independently exercise the full closed-form return count for larger sizes.
    for n in range(2,81):
        coeffs=[bridge_count_with_returns(n,r) for r in range(n)]
        assert sum(coeffs) == comb(2*n,n)
        checks += 1
        assert sum(r*coeffs[r] for r in range(n)) == 4**n - 2*comb(2*n,n)
        checks += 1
        for r in range(n):
            nxt=coeffs[r+1] if r+1<n else 0
            palm_mean=Fraction(n,2)+Fraction(r*coeffs[r]-(r+1)*nxt,4*coeffs[r])
            assert palm_mean == regression(n,r)
            checks += 1
    print('PASS: exact assertions =',checks)
    print('PASS: enumerated bridges =',paths_checked)
    print('PASS: all prescribed-return subsets through n=7; unconditional and conditional moments through n=9; closed-form identities through n=80')


if __name__ == '__main__':
    verify()
