#!/usr/bin/env python3
"""Arithmetic check for the six published non-core-case linear bounds.

The mathematical proof for every n>=17 uses g(n+1)-g(n)=n-b>0
when a bound has the form b*n+a and b<=7, together with g(17)>0.
"""
from math import comb

BOUNDS={
    'noncore_intersection_at_least_three':(4,32),
    'noncore_exact_intersection_two':(6,25),
    'common_pair_matching_two':(4,22),
    'common_pair_triangle':(4,26),
    'common_pair_small_star':(4,17),
    'common_pair_large_star':(7,-11),
}
for name,(b,a) in BOUNDS.items():
    gap = 1+comb(17,2)-(b*17+a)
    assert gap>0
    assert all(1+comb(n,2)>b*n+a for n in range(17,201))
    assert all(n-b>0 for n in range(17,201))
    print(f'{name}: bound={b}n{a:+d}, gap_at_17={gap}, delta_gap_at_n=n-{b}>0_for_n>=17')
