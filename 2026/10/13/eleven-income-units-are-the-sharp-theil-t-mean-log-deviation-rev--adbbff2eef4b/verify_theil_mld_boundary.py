#!/usr/bin/env python3
from itertools import combinations
from math import prod

def parts(total, length):
    def rec(rem, k, low, prefix):
        if k == 0:
            if rem == 0:
                yield tuple(prefix)
            return
        for x in range(low, rem // k + 1):
            yield from rec(rem-x, k-1, x, prefix+[x])
    yield from rec(total, length, 1, [])

def q(profile):
    out = 1
    for x in profile:
        out *= x ** x
    return out

def p(profile):
    return prod(profile)

def sgn(x):
    return (x > 0) - (x < 0)

pair_counts = {}
disagreement_counts = {}
reversal_pairs = {}

for total in range(2, 12):
    pair_count = 0
    disagreements = []
    reversals = []
    for n in range(2, total + 1):
        profiles = list(parts(total, n))
        pair_count += len(profiles) * (len(profiles)-1) // 2
        for a,b in combinations(profiles, 2):
            dq = sgn(q(a)-q(b))
            dp = sgn(p(a)-p(b))
            # Theil T follows q; MLD is reverse p.
            if (dq == 0) != (dp == 0) or dq*dp > 0:
                disagreements.append((n,a,b))
            if dq*dp > 0:
                reversals.append((n,a,b))
    pair_counts[total] = pair_count
    disagreement_counts[total] = len(disagreements)
    reversal_pairs[total] = reversals

assert disagreement_counts == {
    2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:3
}
assert reversal_pairs[11] == [
    (3,(1,4,6),(2,2,7)),
    (3,(1,5,5),(2,2,7)),
    (4,(1,3,3,4),(2,2,2,5)),
]
assert sum(pair_counts.values()) == 408

expected = {
    (1,4,6):(11943936,24),
    (1,5,5):(9765625,25),
    (2,2,7):(13176688,28),
    (1,3,3,4):(186624,36),
    (2,2,2,5):(200000,40),
}
for profile,(qv,pv) in expected.items():
    assert q(profile) == qv
    assert p(profile) == pv

print("VERIFY_OK")
print("pair_counts", pair_counts)
print("disagreement_counts", disagreement_counts)
print("first_layer_pairs", reversal_pairs[11])
print("first_layer_exact_QP", expected)
