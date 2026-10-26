#!/usr/bin/env python3
"""Exact finite enumeration for a 4-dimensional spin factor over F_3.

S = F_3*1 + V, V=F_3^3, q(x,y,z)=x^2+y^2+z^2, B(u,v)=u dot v,
(a,u) o (b,v)=(ab+B(u,v), av+bu). No third-party packages are required.
"""
from itertools import product
from collections import Counter

P = 3

def q(u):
    return sum(x*x for x in u) % P

def b(u, v):
    return sum(x*y for x, y in zip(u, v)) % P

def jordan(x, y):
    a, *u = x
    c, *v = y
    return ((a*c + b(u, v)) % P,) + tuple((a*v[i] + c*u[i]) % P for i in range(3))

def word_value(word):
    value = word[0]
    for factor in word[1:]:
        value = jordan(value, factor)
    return value

ALL = set(product(range(P), repeat=4))
IDEMPOTENTS = {(0, 0, 0, 0), (1, 0, 0, 0)}
for u in product(range(P), repeat=3):
    if q(u) == 1:
        IDEMPOTENTS.add((2,) + u)

# Breadth-first closure under right multiplication by every idempotent.
# Every left-nested word is a shorter word followed by one idempotent, so BFS
# gives exact minimum lengths. Parent pointers provide explicit word witnesses.
length = {x: 1 for x in IDEMPOTENTS}
parent = {x: None for x in IDEMPOTENTS}
frontier = set(IDEMPOTENTS)
while frontier:
    nxt = set()
    for x in frontier:
        for e in IDEMPOTENTS:
            y = jordan(x, e)
            if y not in length:
                length[y] = length[x] + 1
                parent[y] = (x, e)
                nxt.add(y)
    frontier = nxt

def word_for(x):
    factors = []
    while parent[x] is not None:
        previous, factor = parent[x]
        factors.append(factor)
        x = previous
    factors.append(x)
    return list(reversed(factors))

# Verify every positive reachability certificate by replaying its word.
for x, ell in length.items():
    word = word_for(x)
    assert len(word) == ell
    assert all(e in IDEMPOTENTS for e in word)
    assert word_value(word) == x

missing = ALL - set(length)
expected_missing = {(2, 0, 0, 0)} | {
    (0, x, y, z) for x, y, z in product((1, 2), repeat=3)
}
counts = dict(sorted(Counter(length.values()).items()))
assert len(ALL) == 81
assert len(IDEMPOTENTS) == 8
assert len(length) == 72
assert missing == expected_missing
assert counts == {1: 8, 2: 12, 3: 14, 4: 18, 5: 12, 6: 8}
assert sum(counts.values()) + len(missing) == 81

print("field=F_3; dimension=4; total_elements=81")
print("idempotents=8; representable=72; nonrepresentable=9")
print("minimum_word_length_counts=" + repr(counts))
print("nonrepresentable=" + repr(sorted(missing)))
print("all_reachable_words_replayed=72")
print("VERIFY_OK")
