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

def omega(n):
    w = 0
    p = 2
    while p*p <= n:
        if n % p == 0:
            w += 1
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        w += 1
    return w

def v2(n):
    e = 0
    while n % 2 == 0:
        e += 1
        n //= 2
    return e, n

def r2(e):
    if e == 0:
        return 1
    if e == 1:
        return 2
    if e == 2:
        return 3
    return 5

def direct_pairs(b):
    return sorted(
        (a,c)
        for a in range(1,b)
        for c in range(b)
        if a**3 + c**3 == a*b + c
    )

def predicted_pairs_for_base(b):
    out = []
    for a in range(1,b):
        for c in range(b):
            if c in (0,1):
                if a >= 2 and b == a*a:
                    out.append((a,c))
            else:
                N = c**3-c
                if N % a == 0 and b == a*a + N//a:
                    out.append((a,c))
    return sorted(out)

base_hits = 0
for b in range(2,501):
    got = direct_pairs(b)
    want = predicted_pairs_for_base(b)
    assert got == want, (b, got, want)
    base_hits += len(got)

for c in range(2,251):
    N = c**3-c
    ds = divisors(N)
    assert len(ds) >= 1
    for a in ds:
        b = a*a + N//a
        assert b > a and b > c
        assert a**3 + c**3 == a*b + c
    assert len(ds) == len(divisors(N))

for a in range(2,501):
    got = sum(1 for c in range(a) if (c*(c-1)*(c+1)) % a == 0)
    e,m = v2(a)
    want = r2(e) * (3 ** omega(m))
    assert got == want, (a, got, want)

for a in range(2,1001):
    b = a*a
    assert a**3 == a*b
    assert a**3 + 1 == a*b + 1
    assert a < b

# Published finite-base comparison points.
assert (1,2) in direct_pairs(7)
assert (2,2) in direct_pairs(7)
assert (3,2) in direct_pairs(11)

print(
    "VERIFY_OK",
    "bases=2..500",
    f"base_hits={base_hits}",
    "trailing_c=2..250",
    "leading_a=2..500",
    "boundary_a=2..1000",
    "examples=b7:(1,2),(2,2);b11:(3,2)",
)
