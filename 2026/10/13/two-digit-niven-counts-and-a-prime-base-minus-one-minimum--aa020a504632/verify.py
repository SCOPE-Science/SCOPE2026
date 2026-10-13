#!/usr/bin/env python3
from math import gcd, isqrt

def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = isqrt(n)
    p = 3
    while p <= r:
        if n % p == 0:
            return False
        p += 2
    return True

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def direct_count(b):
    total = 0
    for a in range(1, b):
        for c in range(b):
            n = a*b + c
            if n % (a+c) == 0:
                total += 1
    return total

def formula_count(b):
    M = b - 1
    total = M
    for v in divisors(M):
        if v < 2:
            continue
        for u in range(1, v):
            if gcd(u, v) == 1:
                total += M // max(u, v-u)
    return total

rows = []
equality_bases = []
for b in range(2, 301):
    direct = direct_count(b)
    formula = formula_count(b)
    assert direct == formula, (b, direct, formula)
    assert direct >= 2*b - 3, (b, direct)

    if b >= 4:
        eq = direct == 2*b - 3
        assert eq == isprime(b-1), (b, direct, isprime(b-1))
        if eq:
            equality_bases.append(b)

        M = b - 1
        if not isprime(M):
            d = next(d for d in range(2, M) if M % d == 0)
            a, c = 1, d - 1
            n = a*b + c
            assert n % (a+c) == 0
            assert c > 0
            assert a+c != M

    if b <= 20:
        rows.append((b, direct))

assert direct_count(2) == 1
assert direct_count(3) == 4

print(
    "VERIFY_OK",
    "bases=2..300",
    f"sample={rows}",
    f"equality_count={len(equality_bases)}",
    f"last_equality_base={equality_bases[-1]}",
)
