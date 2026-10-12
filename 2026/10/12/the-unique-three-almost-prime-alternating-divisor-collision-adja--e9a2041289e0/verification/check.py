#!/usr/bin/env python3
"""Integer-only consistency checks for the alternating divisor-sum classification."""
from math import isqrt, gcd

LIMIT = 600000
spf = list(range(LIMIT + 1))
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for v in range(p*p, LIMIT+1, p):
            if spf[v] == v:
                spf[v] = p


def factor(n):
    ans = []
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        ans.append((p, a))
    return ans


def beta(n):
    v = 1
    for p, a in factor(n):
        v *= (p ** (a + 1) + (-1) ** a) // (p + 1)
    return v


def omega(n):
    return sum(a for _, a in factor(n))


def liouville(n):
    return (-1) ** omega(n)


def from_convolution(n):
    return sum(d * liouville(n // d) for d in range(1, n + 1) if n % d == 0)

assert beta(194) == beta(195) == 96
assert omega(195) == 3
assert all(beta(n) == from_convolution(n) for n in range(1, 451))
hits = []
candidates = 0
for p in range(2, (LIMIT-1)//2 + 1):
    if spf[p] != p:
        continue
    for m in (2*p-1, 2*p+1):
        if m > LIMIT:
            continue
        if omega(m) <= 3:
            candidates += 1
            if beta(m) == beta(2*p):
                hits.append((p, m))
assert hits == [(97, 195)], hits
# Independent interpretation: beta(n) counts k in [1,n] for which gcd(k,n) is square.
def is_square(n):
    a = isqrt(n)
    return a*a == n
for n in (3, 5, 97, 194, 195):
    assert beta(n) == sum(is_square(gcd(k,n)) for k in range(1,n+1))
print('EXACT_CONSISTENCY_OK', 'prime_bound='+str((LIMIT-1)//2),
      'tested_neighbors='+str(candidates), 'hits='+repr(hits),
      'collision_value=96')
