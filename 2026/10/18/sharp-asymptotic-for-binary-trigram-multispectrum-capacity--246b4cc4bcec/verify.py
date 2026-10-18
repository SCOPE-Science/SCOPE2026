#!/usr/bin/env python3
"""Independent exact checks for binary length-three contiguous multiset profiles.

Requires Python 3 standard library only; checks use integer arithmetic.
"""
from itertools import product


def direct_profiles(n):
    out = set()
    for word in product(range(2), repeat=n):
        counts = [0] * 8
        for j in range(n-2):
            idx = (word[j] << 2) | (word[j+1] << 1) | word[j+2]
            counts[idx] += 1
        out.add(tuple(counts))
    return out


def dynamic_profiles(n):
    if n < 3:
        raise ValueError("n must be >=3")
    empty = (0,) * 8
    states = {(ab, empty) for ab in range(4)}
    for _ in range(3, n+1):
        next_states = set()
        for pair, counts in states:
            for bit in range(2):
                edge = (pair << 1) | bit
                new = list(counts)
                new[edge] += 1
                next_states.add((((pair << 1) | bit) & 3, tuple(new)))
        states = next_states
    return {counts for pair, counts in states}


def balanced_coefficient(m):
    # Flow balance: 100=001=B, 110=011=D, 101=010+011-001.
    # Remaining nonnegative integer variables A,H,B,C,D satisfy
    #  A+H+B+2C+3D=m, 0<=B<=C+D.
    total = 0
    for c in range(m // 2 + 1):
        for d in range((m-2*c) // 3 + 1):
            r = m-2*c-3*d
            for b in range(min(c+d,r)+1):
                total += r-b+1
    return total


def rational_coefficients(max_m):
    # (1+z^3)/((1-z)^2(1-z^2)(1-z^3)(1-z^4))
    counts = [1] + [0] * max_m
    for step in (1,1,2,3,4):
        for j in range(step,max_m+1):
            counts[j] += counts[j-step]
    return [counts[j]+(counts[j-3] if j>=3 else 0) for j in range(max_m+1)]


def main():
    # Exhaustive direct word generation versus independent de Bruijn state DP.
    target = (8,15,28,52,92,151,240,363,532,757,1048,1416,1880)
    for n in range(3,16):
        direct = direct_profiles(n)
        via_dp = dynamic_profiles(n)
        assert direct == via_dp, (n, len(direct), len(via_dp))
        assert len(direct) == target[n-3], (n,len(direct))
    print('EXHAUSTIVE_DIRECT_VS_DP_OK lengths=3..15')
    # Longer nonexhaustive independent DP, no asymptotic inference.
    for n in range(16,25):
        dp_count = len(dynamic_profiles(n))
        assert dp_count > 0
        if n in (16,18,20,23):
            print(f'DP_COUNT n={n} Q={dp_count}')
    series = rational_coefficients(60)
    for m in range(61):
        assert balanced_coefficient(m) == series[m], (m,balanced_coefficient(m),series[m])
    print('BALANCED_GENERATING_FUNCTION_OK total_triples=0..60')
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
