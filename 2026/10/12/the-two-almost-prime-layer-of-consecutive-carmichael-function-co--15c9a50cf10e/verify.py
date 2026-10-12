#!/usr/bin/env python3
from math import gcd, isqrt

LIMIT = 2_000_000
spf = list(range(LIMIT + 2))
for p in range(2, isqrt(LIMIT + 1) + 1):
    if spf[p] == p:
        for m in range(p*p, LIMIT + 2, p):
            if spf[m] == m:
                spf[m] = p

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        out.append((p,a))
    return out

def omega_big(n):
    return sum(a for _,a in factor(n))

def lcm(a,b):
    return a // gcd(a,b) * b

def carmichael(n):
    if n == 1:
        return 1
    L = 1
    for p,a in factor(n):
        if p == 2 and a >= 3:
            v = 1 << (a-2)
        else:
            v = (p-1) * p**(a-1)
        L = lcm(L,v)
    return L

low = []
all_hits = []
for n in range(2, LIMIT + 1):
    if carmichael(n) == carmichael(n+1):
        all_hits.append(n)
        if omega_big(n) <= 2 and omega_big(n+1) <= 2:
            low.append(n)

assert low == [3]
assert all_hits[:10] == [3,15,90,104,495,665,702,740,836,975]
print('VERIFY_OK', f'limit={LIMIT}', f'low_layer={low}', f'equal_count={len(all_hits)}', f'first_equal={all_hits[:10]}')
