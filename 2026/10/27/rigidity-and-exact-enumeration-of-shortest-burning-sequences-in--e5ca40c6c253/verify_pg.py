#!/usr/bin/env python3
"""Exact finite checks for optimal sequential burning in binary projective STS.
Run: python3 verify_pg.py. No external packages are required.
"""
from functools import lru_cache
from math import prod


def analytic_count(m):
    assert m >= 3
    return (2**(m-1)-1) * prod(2**m-2**j for j in range(m))


def brute_count(m):
    """Full dynamic enumeration of VALID source sequences, including redundant sources."""
    v = 2**m-1
    full = (1 << v)-1
    @lru_cache(maxsize=None)
    def propagate(s):
        elements = [x for x in range(1, v+1) if (s >> (x-1))&1]
        t = s
        for i,x in enumerate(elements):
            for y in elements[:i]:
                t |= 1 << ((x^y)-1)
        return t
    @lru_cache(maxsize=None)
    def count(s,r):
        if r == m+1:
            return int(s == full)
        p = propagate(s)
        total = 0
        for x in range(1,v+1):
            if not (s >> (x-1))&1:
                total += count(p | (1 << (x-1)),r+1)
        return total
    actual = count(0,0)
    assert actual == analytic_count(m), (m,actual,analytic_count(m))
    print(f'm={m}; order={v}; brute_optimal_sequences={actual}; expected={analytic_count(m)}; states={count.cache_info().currsize}')


def trajectory(m):
    srcs = [1<<j for j in range(m)]
    srcs.append(1 ^ (1 << (m-1)))  # Valid last source; propagation makes it redundant.
    s=set()
    profile=[]
    for x in srcs:
        assert x not in s
        prop={x^y for x in s for y in s if x!=y}
        s |= prop | {x}
        profile.append(len(s))
    assert len(s)==2**m-1
    assert profile == [2**j for j in range(m)] + [2**m-1],(m,profile)
    print(f'm={m}; verified_explicit_profile={profile}')

if __name__ == '__main__':
    for m in (3,4):brute_count(m)
    for m in (3,4,5,6):trajectory(m)
    print('analytic_sequence_counts_m3_to_m7', [(m,analytic_count(m)) for m in range(3,8)])
