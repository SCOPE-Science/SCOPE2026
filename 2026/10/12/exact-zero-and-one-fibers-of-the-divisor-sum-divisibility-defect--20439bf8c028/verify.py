#!/usr/bin/env python3
from math import isqrt

LIMIT = 1_000_000

# Independent exact sum-of-divisors sieve, without external packages.
sigma = [0] * (LIMIT + 1)
for d in range(1, LIMIT + 1):
    for n in range(d, LIMIT + 1, d):
        sigma[n] += d

spf = list(range(LIMIT + 1))
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for n in range(p*p, LIMIT + 1, p):
            if spf[n] == n:
                spf[n] = p

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            a += 1
            n //= p
        out.append((p, a))
    return out

def divisors(fac):
    out = [1]
    for p, a in fac:
        out = [d * p**j for d in out for j in range(a+1)]
    return out

def tau(n):
    v = 0
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            v += 1 if d*d == n else 2
    return v

def predicted_class(fac):
    repeated = [(p, a) for p, a in fac if a > 1]
    if not repeated:
        return 0, None
    if len(repeated) != 1:
        return 2, None
    p, a = repeated[0]
    if a not in (2, 3):
        return 2, None
    modulus = (p + 1) if a == 2 else (p*p + p + 1)
    if not all((q+1) % modulus == 0 for q, b in fac if q != p):
        return 2, None
    return 1, p

counts = [0, 0, 0]
first_one = []
for n in range(1, LIMIT + 1):
    fac = factor(n)
    bad = [d for d in divisors(fac) if sigma[n] % sigma[d] != 0]
    observed = len(bad)
    counts[min(observed, 2)] += 1
    claimed, repeated_p = predicted_class(fac)
    assert (observed == 0) == (claimed == 0), (n, fac, bad, claimed)
    assert (observed == 1) == (claimed == 1), (n, fac, bad, claimed)
    if observed == 1:
        assert bad == [n // repeated_p], (n, fac, bad, repeated_p)
        if len(first_one) < 30:
            first_one.append(n)
    bound = sum((a+1)-tau(a+1) for p, a in fac)
    assert observed >= bound, (n, fac, observed, bound)
    if len(fac) == 1:
        assert observed == bound, (n, fac, observed, bound)

# Independent finite test of the prime-power divisibility criterion.
local_cases = 0
for p in range(2, 102):
    if p > LIMIT or spf[p] != p:
        continue
    for a in range(1, 13):
        S_a = (p**(a+1)-1)//(p-1)
        for j in range(a+1):
            S_j = (p**(j+1)-1)//(p-1)
            assert (S_a % S_j == 0) == ((a+1)%(j+1) == 0), (p,a,j)
            local_cases += 1

assert first_one[:16] == [4,8,9,20,25,27,44,49,63,68,92,99,104,116,121,125]
assert counts[0] + counts[1] + counts[2] == LIMIT
print(
    'VERIFY_OK',
    f'limit={LIMIT}',
    f'zero_count={counts[0]}',
    f'one_count={counts[1]}',
    f'higher_count={counts[2]}',
    f'prime_power_local_cases={local_cases}',
    f'first_one={first_one[:16]}',
)
