#!/usr/bin/env python3
"""Independent finite checks for binary strict-majority equilibria on prism graphs.

This program is finite evidence supplementing, not replacing, the analytic proof.
"""
from collections import Counter
from math import comb


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def independent_signed_cycle(n):
    # I(C_n,-1) follows period six: 2,1,-1,-2,-1,1,2,...
    return [2, 1, -1, -2, -1, 1][n % 6]


def total_formula(n):
    return 2 + lucas(n) + independent_signed_cycle(n)


def blue_mass_formula(n, m):
    if not (0 <= m <= 2*n):
        return 0
    ans = int(m == 0) + int(m == 2*n) + (2 if m == n else 0)
    if m % 2:
        return ans
    k = m // 2
    if 0 < k < n:
        for r in range(1, min(k//2, (n-k)//2) + 1):
            numerator = n * comb(k-r-1, r-1) * comb(n-k-r-1, r-1)
            assert numerator % r == 0
            ans += numerator // r
    return ans


def enumerate_fixed(n):
    counts = Counter()
    n2 = 2*n
    mask = (1 << n2) - 1
    for x in range(mask+1):
        stable = True
        for layer in range(2):
            for i in range(n):
                idx = layer*n + i
                me = (x >> idx) & 1
                same = 0
                for nb in (layer*n+(i-1)%n, layer*n+(i+1)%n, (1-layer)*n+i):
                    same += (((x >> nb) & 1) == me)
                if same < 2:
                    stable = False
                    break
            if not stable:
                break
        if stable:
            counts[x.bit_count()] += 1
    return counts


def test():
    comparisons = 0
    for n in range(3, 10):
        observed = enumerate_fixed(n)
        predicted = Counter({m: blue_mass_formula(n, m)
                             for m in range(2*n+1) if blue_mass_formula(n,m)})
        assert observed == predicted, (n, observed, predicted)
        comparisons += 2*n+1
        assert sum(observed.values()) == total_formula(n)
        comparisons += 1
        print('n=',n,'total=',sum(observed.values()),'mass_histogram=',sorted(observed.items()))
    for n in range(3,201):
        assert sum(blue_mass_formula(n,m) for m in range(2*n+1)) == total_formula(n)
        comparisons += 2*n+2
    print('PASS:',comparisons,'formula comparisons and complete brute-force fixed-point enumerations for n=3..9')


if __name__ == '__main__':
    test()
