#!/usr/bin/env python3
"""Finite checks for dyadic two-binomial profiles of the binary paperfolding word.

The algorithm is standalone and uses only Python's standard library. The
infinite result is established by the accompanying proof, not this checker.
"""

def folding_bit(t):
    assert t >= 1
    while t % 2 == 0:
        t //= 2
    return int(t % 4 == 1)


def template(k, alpha, beta):
    n = 1 << k
    return tuple(alpha if i == 0 else beta if i == n // 2
                 else folding_bit(i) for i in range(n))


def profile(word):
    ones = zeros = pairs = 0
    for bit in word:
        if bit == 0:
            zeros += 1
        else:
            ones += 1
            pairs += zeros
    return ones, pairs


def family_profiles(k):
    n = 1 << k
    result = set()
    for a in (0, 1):
        for b in (0, 1):
            word = template(k, a, b)
            for shift in range(n):
                result.add(profile(word[shift:] + word[:shift]))
    return result


def prefix_profiles(k):
    n = 1 << k
    data = tuple(folding_bit(i) for i in range(1, 32*n+1))
    # Independent rolling update for the positional moment of the one bits.
    ones = sum(data[:n])
    moment = sum((j+1)*v for j,v in enumerate(data[:n]))
    result = {(ones, moment - ones*(ones+1)//2)}
    for s in range(len(data)-n):
        left, right = data[s], data[s+n]
        moment = moment - ones + n*right
        ones = ones - left + right
        result.add((ones, moment - ones*(ones+1)//2))
    return result


def direct_profiles(k):
    n = 1 << k
    data = tuple(folding_bit(i) for i in range(1, 8*n+1))
    return {profile(data[s:s+n]) for s in range(len(data)-n+1)}


def verify():
    for k in range(2, 11):
        n = 1 << k
        profiles = family_profiles(k)
        actual = prefix_profiles(k)
        assert profiles == actual, (k, profiles - actual, actual - profiles)
        if k <= 7:
            assert direct_profiles(k) == profiles
        low = {q for r,q in profiles if r == n//2-1}
        mid = {q for r,q in profiles if r == n//2}
        high = {q for r,q in profiles if r == n//2+1}
        assert len(profiles) == 2*n + k+1
        assert len(low) == len(high) == n and low == high
        assert mid == {n*(n-2*k)//8+(n//2)*j for j in range(k+1)}
        assert {r for r,q in profiles} == {n//2-1,n//2,n//2+1}
        print(f"k={k}, n={n}, distinct_profiles={len(profiles)}, "
              f"outer_counts=({len(low)},{len(high)}), central={len(mid)}: PASS")
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    verify()
