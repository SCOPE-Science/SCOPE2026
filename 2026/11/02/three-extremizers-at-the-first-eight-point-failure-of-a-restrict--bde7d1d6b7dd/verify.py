"""Exhaustive, exact certificate for eight-element restricted four-sumsets in [0,16].

Run using Python 3 standard library: python verify.py
"""
from itertools import combinations
from math import gcd
from collections import Counter

EXPECTED = {
    (0, 1, 2, 3, 13, 14, 15, 16),
    (0, 1, 5, 6, 10, 11, 15, 16),
    (0, 3, 6, 7, 9, 10, 13, 16),
}

def four_sums_direct(values):
    return {a + b + c + d for a, b, c, d in combinations(values, 4)}

def four_sums_bitset(values):
    # The coefficient support of prod_{a in A}(1 + t z^a), through degree t^4.
    dp = [1, 0, 0, 0, 0]
    for a in values:
        for j in range(4, 0, -1):
            dp[j] |= dp[j-1] << a
    return {n for n in range(65) if (dp[4] >> n) & 1}

def main():
    for L in range(7, 17):
        hist = Counter()
        minimizers = []
        all_cases = 0
        primitive_cases = 0
        for interior in combinations(range(1, L), 6):
            a = (0,) + interior + (L,)
            all_cases += 1
            if gcd(*a) != 1:
                continue
            primitive_cases += 1
            sums1 = four_sums_direct(a)
            sums2 = four_sums_bitset(a)
            assert sums1 == sums2, ('algorithms disagree', a)
            n = len(sums1)
            hist[n] += 1
            if L == 16 and n <= 25:
                minimizers.append(a)
        expected_min = 10 + L if L <= 15 else 25
        assert min(hist) == expected_min, (L, min(hist), expected_min)
        print('DIAMETER:', L, 'total:', all_cases, 'primitive:', primitive_cases,
              'minimum:', min(hist), 'optimal sets:', hist[min(hist)])
        if L == 16:
            assert all_cases == 5005
            assert primitive_cases == 4998
            assert set(minimizers) == EXPECTED
            assert len(minimizers) == 3
            assert hist[25] == 3 and hist[26] == 10
            for a in EXPECTED:
                assert tuple(sorted(16-x for x in a)) == a
            print('MINIMIZERS:', sorted(minimizers))
            print('HISTOGRAM:', sorted(hist.items()))
    print('VERIFY_OK: all diameters 7..16, first failure 16, exactly 3 distinct extremizers; independent direct/DP supports agree')

if __name__ == '__main__':
    main()
