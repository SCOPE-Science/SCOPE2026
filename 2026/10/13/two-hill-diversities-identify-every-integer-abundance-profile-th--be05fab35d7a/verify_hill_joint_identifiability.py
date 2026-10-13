#!/usr/bin/env python3
from collections import defaultdict

def partitions(total):
    def rec(rem, low, prefix):
        if rem == 0:
            yield tuple(prefix)
            return
        for x in range(low, rem + 1):
            yield from rec(rem - x, x, prefix + (x,))
    yield from rec(total, 1, ())

def qprod(profile):
    out = 1
    for x in profile:
        out *= x ** x
    return out

def s2(profile):
    return sum(x*x for x in profile)

def pnum(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for k in range(1,n+1):
        for s in range(k,n+1):
            dp[s] += dp[s-k]
    return dp[n]

pair_collisions = {}
triple_collisions = {}
profile_counts = {}

for N in range(1,31):
    profiles = list(partitions(N))
    profile_counts[N] = len(profiles)
    assert len(profiles) == pnum(N)

    b2 = defaultdict(list)
    b3 = defaultdict(list)
    for x in profiles:
        b2[(qprod(x),s2(x))].append(x)
        b3[(len(x),qprod(x),s2(x))].append(x)

    pair_collisions[N] = [
        tuple(v) for v in b2.values() if len(v) > 1
    ]
    triple_collisions[N] = [
        tuple(v) for v in b3.values() if len(v) > 1
    ]

for N in range(1,24):
    assert pair_collisions[N] == [], (N,pair_collisions[N])

expected24 = [
    (
        (1,1,1,1,1,1,3,3,4,4,4),
        (2,2,2,2,2,2,2,2,2,6),
    ),
    (
        (1,1,1,1,4,4,6,6),
        (2,2,3,3,3,3,8),
    ),
]
assert pair_collisions[24] == expected24, pair_collisions[24]

for N in range(1,30):
    assert triple_collisions[N] == [], (N,triple_collisions[N])

expected30 = [
    (
        (1,4,4,4,4,4,9),
        (2,2,3,3,6,6,8),
    )
]
assert triple_collisions[30] == expected30, triple_collisions[30]

# Exact invariant checks.
a,b = expected24[0]
assert (qprod(a),s2(a),len(a)) == (12230590464,72,11)
assert (qprod(b),s2(b),len(b)) == (12230590464,72,10)

a,b = expected24[1]
assert (qprod(a),s2(a),len(a)) == (142657607172096,108,8)
assert (qprod(b),s2(b),len(b)) == (142657607172096,108,7)

a,b = expected30[0]
assert (qprod(a),s2(a),len(a)) == (425973332494163902464,162,7)
assert (qprod(b),s2(b),len(b)) == (425973332494163902464,162,7)

assert sum(profile_counts.values()) == 28628

print("VERIFY_OK")
print("profiles_checked_through_30", sum(profile_counts.values()))
print("first_H_C2_collision_total", 24)
print("first_H_C2_collision_pairs", expected24)
print("first_richness_H_C2_collision_total", 30)
print("first_richness_H_C2_collision_pair", expected30[0])
