#!/usr/bin/env python3
from itertools import product, combinations
from collections import Counter

points = list(product((0,1), repeat=3))
code = []
for a in product((0,1), repeat=3):
    for b in (0,1):
        word = tuple((sum(ai*xi for ai,xi in zip(a,x)) + b) % 2 for x in points)
        code.append(word)

assert len(code) == 16
assert len(set(code)) == 16
mind = min(sum(x != y for x,y in zip(u,v))
           for i,u in enumerate(code) for v in code[i+1:])
assert mind == 4

n, k, d, q = 8, 4, 4, 2
s = n-k+1-d
assert s == q-1 == 1
assert n == (s+1)*(q+1)+k-2

for cols in combinations(range(8), 3):
    ctr = Counter(tuple(w[i] for i in cols) for w in code)
    assert set(ctr.values()) == {2}
    assert len(ctr) == 8

# Finite consistency check only; the all-q identity is proved algebraically in RESULT.md.
for q in range(2, 1001):
    n = q*q + q + 2
    rao = 1 + n*(q-1) + (n-1)*(q-1)*(q-1)
    assert rao == q**4

print("VERIFY_OK")
