#!/usr/bin/env python3
from math import isqrt

def divisors(n):
    out = []
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return sorted(out)

def tau(n):
    return len(divisors(n))

def isprime(n):
    if n < 2:
        return False
    for p in range(2, isqrt(n)+1):
        if n % p == 0:
            return False
    return True

def direct_pairs(b):
    out = []
    for a in range(1, b):
        for c in range(1, b):
            if (a*b+c) % (a*c) == 0:
                out.append((a,c))
    return sorted(out)

def predicted_pairs(b):
    out = []
    for d in divisors(b):
        if d < 2:
            continue
        k = b//d
        for a in divisors(d+1):
            if a < d:
                c = a*k
                assert 1 <= c < b
                out.append((a,c))
    return sorted(out)

samples = []
equality = []
prime_checks = 0

for b in range(2, 501):
    direct = direct_pairs(b)
    predicted = predicted_pairs(b)
    assert direct == predicted, (b, direct, predicted)

    formula = sum(tau(d+1)-1 for d in divisors(b) if d >= 2)
    assert len(direct) == formula
    assert formula >= tau(b)-1

    if b >= 3:
        eq = formula == tau(b)-1
        assert eq == (b == 4), (b, formula, tau(b)-1)
        if eq:
            equality.append(b)

    if isprime(b):
        assert formula == tau(b+1)-1
        prime_checks += 1

    if b <= 20:
        samples.append((b, formula))

decimal_values = [a*10+c for a,c in direct_pairs(10)]
assert decimal_values == [11,12,15,24,36]

print(
    "VERIFY_OK",
    "bases=2..500",
    f"sample={samples}",
    f"equality_bases={equality}",
    f"prime_bases_checked={prime_checks}",
    f"base10={decimal_values}",
)
