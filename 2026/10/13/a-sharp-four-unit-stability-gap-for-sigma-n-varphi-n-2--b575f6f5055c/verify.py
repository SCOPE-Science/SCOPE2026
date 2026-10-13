#!/usr/bin/env python3
from math import isqrt

LIMIT = 2_000_000
M = LIMIT + 2

spf = list(range(M + 1))
spf[0] = 0
spf[1] = 1
for p in range(2, isqrt(M) + 1):
    if spf[p] == p:
        for m in range(p*p, M + 1, p):
            if spf[m] == m:
                spf[m] = p

isprime = bytearray(b"\x01") * (M + 1)
isprime[0:2] = b"\x00\x00"
for p in range(2, isqrt(M) + 1):
    if isprime[p]:
        isprime[p*p:M+1:p] = b"\x00" * (((M - p*p) // p) + 1)

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p,e))
    return out

def sigma(n):
    ans = 1
    for p,e in factor(n):
        ans *= (p ** (e + 1) - 1) // (p - 1)
    return ans

def phi(n):
    ans = n
    for p,e in factor(n):
        ans = ans // p * (p - 1)
    return ans

exceptions = {2:1, 7:2, 9:3, 23:4}
low_nonzero = {}
twin_count = 0

for n in range(2, LIMIT + 1):
    a = sigma(n) - phi(n + 2)
    predicted = (
        (isprime[n] and isprime[n + 2])
        or n in exceptions
    )
    assert (a < 5) == predicted, (n, a, predicted)
    if isprime[n] and isprime[n + 2]:
        assert a == 0, (n, a)
        twin_count += 1
    elif n in exceptions:
        assert a == exceptions[n], (n, a)
        low_nonzero[n] = a

assert low_nonzero == exceptions
assert sigma(4) - phi(6) == 5

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"twin_starts={twin_count}",
    f"exceptions={sorted(low_nonzero.items())}",
    "boundary=(4,5)",
)
