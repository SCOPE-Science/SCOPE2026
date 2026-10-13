#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

def partitions_fixed_sum_length(total, length):
    def rec(rem, k, low, prefix):
        if k == 0:
            if rem == 0:
                yield tuple(prefix)
            return
        for x in range(low, rem // k + 1):
            yield from rec(rem - x, k - 1, x, prefix + (x,))
    yield from rec(total, length, 1, ())

def compositions_positive(total, length):
    if length == 1:
        yield (total,)
        return
    # independent ordered generator; caller canonicalizes by sorting
    for first in range(1, total - length + 2):
        for rest in compositions_positive(total-first, length-1):
            yield (first,) + rest

def canonical_profiles(total, length):
    a = list(partitions_fixed_sum_length(total, length))
    b = sorted(set(tuple(sorted(c)) for c in compositions_positive(total, length)))
    assert a == b
    return a

def hhi_num(profile):
    return sum(x*x for x in profile)

def rank_sum(profile):
    d = sorted(profile, reverse=True)
    return sum((i+1)*x for i,x in enumerate(d))

def hti(profile):
    N = sum(profile)
    R = rank_sum(profile)
    return Fraction(N, 2*R - N)

def sign(x):
    return (x > 0) - (x < 0)

profile_counts = {}
pair_counts = {}
weak_counts = {}
strict_counts = {}
weak_pairs = {}
strict_pairs = {}

for N in range(2, 13):
    profiles_all = 0
    pairs_all = 0
    weak = []
    strict = []
    for k in range(2, N+1):
        ps = canonical_profiles(N, k)
        profiles_all += len(ps)
        pairs_all += len(ps)*(len(ps)-1)//2
        for a,b in combinations(ps, 2):
            dh = sign(hhi_num(a)-hhi_num(b))
            dt = sign(hti(a)-hti(b))
            # same weak ordering means signs agree exactly
            if dh != dt:
                weak.append((k,a,b))
            if dh*dt < 0:
                strict.append((k,a,b))
    profile_counts[N] = profiles_all
    pair_counts[N] = pairs_all
    weak_counts[N] = len(weak)
    strict_counts[N] = len(strict)
    weak_pairs[N] = weak
    strict_pairs[N] = strict

assert profile_counts == {2:1,3:2,4:4,5:6,6:10,7:14,8:21,9:29,10:41,11:55,12:76}
assert pair_counts == {2:0,3:0,4:1,5:2,6:7,7:13,8:30,9:56,10:109,11:190,12:354}
assert sum(pair_counts.values()) == 762
assert weak_counts == {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:1,11:5,12:9}
assert strict_counts == {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:1}

assert weak_pairs[10] == [(3,(1,4,5),(2,2,6))]
assert strict_pairs[12] == [(4,(1,2,4,5),(2,2,2,6))]

a=(1,4,5); b=(2,2,6)
assert hhi_num(a)==42 and hhi_num(b)==44
assert rank_sum(a)==16 and rank_sum(b)==16
assert hti(a)==Fraction(5,11) and hti(b)==Fraction(5,11)
assert Fraction(hhi_num(a),100)==Fraction(21,50)
assert Fraction(hhi_num(b),100)==Fraction(11,25)

a=(1,2,4,5); b=(2,2,2,6)
assert hhi_num(a)==46 and hhi_num(b)==48
assert rank_sum(a)==23 and rank_sum(b)==24
assert hti(a)==Fraction(6,17) and hti(b)==Fraction(1,3)
assert Fraction(hhi_num(a),144)==Fraction(23,72)
assert Fraction(hhi_num(b),144)==Fraction(1,3)

print("VERIFY_OK")
print("profile_counts", profile_counts)
print("pair_counts", pair_counts)
print("weak_counts", weak_counts)
print("strict_counts", strict_counts)
print("first_weak", weak_pairs[10])
print("first_strict", strict_pairs[12])
