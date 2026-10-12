#!/usr/bin/env python3
from itertools import combinations
from math import factorial

def partitions(n):
    def rec(rem, low, prefix):
        if rem == 0:
            yield tuple(prefix)
            return
        for x in range(low, rem + 1):
            yield from rec(rem - x, x, prefix + (x,))
    yield from rec(n, 1, ())

def partition_number(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for s in range(k, n + 1):
            dp[s] += dp[s-k]
    return dp[n]

def q(profile):
    out = 1
    for x in profile:
        out *= x ** x
    return out

def f(profile):
    out = 1
    for x in profile:
        out *= factorial(x)
    return out

def sign(x):
    return (x > 0) - (x < 0)

profile_counts = {}
weak = {}
strict = {}

for N in range(1, 9):
    profiles = list(partitions(N))
    profile_counts[N] = len(profiles)
    assert len(profiles) == partition_number(N)
    w = []
    s = []
    for a, b in combinations(profiles, 2):
        dq = sign(q(a)-q(b))
        df = sign(f(a)-f(b))
        if dq != df:
            w.append((a,b))
        if dq*df < 0:
            s.append((a,b))
    weak[N] = w
    strict[N] = s

assert profile_counts == {1:1,2:2,3:3,4:5,5:7,6:11,7:15,8:22}
for N in range(1,7):
    assert weak[N] == [] and strict[N] == []
assert weak[7] == [((1,1,1,4),(2,2,3))]
assert strict[7] == []
assert strict[8] == [
    ((1,1,1,5),(2,2,4)),
    ((1,1,6),(4,4)),
]

a,b=(1,1,1,4),(2,2,3)
assert (q(a),q(b),f(a),f(b)) == (256,432,24,24)
a,b=(1,1,1,5),(2,2,4)
assert (q(a),q(b),f(a),f(b)) == (3125,4096,120,96)
a,b=(1,1,6),(4,4)
assert (q(a),q(b),f(a),f(b)) == (46656,65536,720,576)

print("VERIFY_OK")
print("profile_counts", profile_counts)
print("weak_disagreements_N7", weak[7])
print("strict_reversals_N8", strict[8])
