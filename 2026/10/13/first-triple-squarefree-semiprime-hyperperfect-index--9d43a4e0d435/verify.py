#!/usr/bin/env python3
from math import isqrt

def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def semiprime_pairs(k):
    K = k*k + 1
    out = []
    for d in range(1, k + 1):
        if K % d:
            continue
        e = K // d
        p = k + d
        q = k + e
        if p >= q:
            continue
        if isprime(p) and isprime(q):
            assert p*q == 1 + k*(p+q)
            out.append((p, q, p*q, d, e))
    return out

expected = {
    1: [(2,3)],
    2: [(3,7)],
    6: [(7,43)],
    12: [(13,157),(17,41)],
    18: [(23,83),(31,43)],
    30: [(47,83)],
    48: [(53,509)],
    60: [(73,337)],
    66: [(67,4423)],
    78: [(79,6163)],
    108: [(113,2441)],
    132: [(137,3617),(157,829),(173,557)],
}

nonzero = {}
tested_divisors = 0
for k in range(1, 133):
    K = k*k + 1
    tested_divisors += sum(1 for d in range(1, k+1) if K % d == 0)
    got = semiprime_pairs(k)
    if got:
        nonzero[k] = [(p,q) for p,q,_,_,_ in got]

assert nonzero == expected, (nonzero, expected)
assert max(len(semiprime_pairs(k)) for k in range(1,132)) == 2
assert [k for k in range(1,132) if len(semiprime_pairs(k)) == 2] == [12,18]
assert len(semiprime_pairs(132)) == 3

pairs132 = semiprime_pairs(132)
assert [(p,q,n) for p,q,n,_,_ in pairs132] == [
    (137,3617,495529),
    (157,829,130153),
    (173,557,96361),
]

# Explicit factorization/candidate check at the terminal layer.
K = 132*132 + 1
ds = [d for d in range(1,133) if K % d == 0]
assert K == 17425
assert ds == [1,5,17,25,41,85]
assert 1157 == 13*89

print(
    "VERIFY_OK",
    "k=1..132",
    f"tested_divisors={tested_divisors}",
    f"double_layers={[12,18]}",
    f"M132={len(pairs132)}",
    f"pairs132={[(p,q) for p,q,_,_,_ in pairs132]}",
)
