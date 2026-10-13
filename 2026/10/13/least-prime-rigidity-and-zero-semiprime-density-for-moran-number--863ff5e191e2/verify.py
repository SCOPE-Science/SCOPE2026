#!/usr/bin/env python3
from math import isqrt

LIMIT = 1_000_000

def digit_sum(n):
    return sum(int(c) for c in str(n))

# Exact exceptional cases from the proof.
assert [(r, digit_sum(r*r)) for r in (3,19,37)] == [(3,9),(19,10),(37,19)]
assert [(q, digit_sum(19*q)) for q in (23,29,31,37)] == [(23,14),(29,11),(31,22),(37,10)]
assert digit_sum(6) == 6

spf = list(range(LIMIT + 1))
spf[1] = 1
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for m in range(p*p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

def factor_mult(n):
    out = []
    x = n
    while x > 1 and len(out) <= 2:
        p = spf[x]
        out.append(p)
        x //= p
    return out

def is_prime(n):
    return n >= 2 and spf[n] == n

hits = []
for n in range(2, LIMIT + 1):
    fs = factor_mult(n)
    if len(fs) != 2 or fs[0] * fs[1] != n:
        continue
    s = digit_sum(n)
    if n % s:
        continue
    q = n // s
    if not is_prime(q):
        continue
    hits.append((n, fs[0], fs[1], s, q))
    assert fs[0] != fs[1]
    assert s == min(fs)
    assert q == max(fs)

assert len(hits) == 1617, len(hits)
assert hits[:5] == [
    (21,3,7,3,7),
    (111,3,37,3,37),
    (133,7,19,7,19),
    (201,3,67,3,67),
    (209,11,19,11,19),
]
print('VERIFY_OK', f'limit={LIMIT}', f'hits={len(hits)}', f'first={hits[:5]}', f'last={hits[-1]}')
