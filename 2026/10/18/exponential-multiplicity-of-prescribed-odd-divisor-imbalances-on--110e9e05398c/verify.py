#!/usr/bin/env python3
"""Exact finite checks for signed divisor-partition multiplicity theorem."""
from collections import Counter

BASE = sorted(3**i * 5**j for i in range(3) for j in range(3))
assert BASE == [1, 3, 5, 9, 15, 25, 45, 75, 225]
assert sum(BASE) == 403

def signed_counts(weights):
    counts = {0: 1}
    for d in weights:
        nxt = Counter()
        for s, c in counts.items():
            nxt[s+d] += c
            nxt[s-d] += c
        counts = nxt
    return counts

b_counts = signed_counts(BASE)
assert len(b_counts) > 0 and sum(b_counts.values()) == 512
assert b_counts[47] >= 1 and b_counts[-47] >= 1
zero_pairs = sorted((s, b_counts[s], -s//7, b_counts[-s//7], b_counts[s]*b_counts[-s//7])
                    for s in b_counts if s % 7 == 0 and -s//7 in b_counts)
assert zero_pairs == [
    (-385,2,55,1,2), (-371,1,53,1,1),(-343,2,49,1,2),(-329,1,47,1,1),
    (329,1,-47,1,1), (343,2,-49,1,2),(371,1,-53,1,1),(385,2,-55,1,2)
]
assert sum(row[-1] for row in zero_pairs) == 12

coins = sorted(BASE + [7*d for d in BASE])
assert sum(coins) == 3224
# Small-coin coverage argument with four-coin base [1,3,5,7].
assert coins[:4] == [1,3,5,7]
W = 16
for d in coins[4:]:
    assert d <= W-5
    W += d
assert W == 3224

T = {s+7*t for s in b_counts for t in b_counts}
assert all(t in T for t in range(-3218,3219,2))
assert all(k-2303 in T or k+2303 in T for k in range(-5521,5522,2))

# Finite modular-subset-sum check for a=2; not part of proof.
for a in (1,2):
    divisors = sorted(3**i*5**j*7**t for t in range(2*a+1) for i in range(3) for j in range(3))
    bits = 1
    for d in divisors:
        bits |= bits << d
    sigma=sum(divisors)
    Q=49**a
    L=3218*(Q-1)//48
    K=47*Q + L
    assert K < sigma
    assert all((bits >> ((sigma+k)//2)) & 1 for k in range(-K,K+1,2))
print('VERIFY_OK: 12 zero-block assignments, dyadic coin interval, complete seed interval, a=1,2 direct subset-sum checks')
