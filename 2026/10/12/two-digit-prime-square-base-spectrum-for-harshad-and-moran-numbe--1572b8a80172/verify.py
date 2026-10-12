#!/usr/bin/env python3
from math import isqrt

def primes_upto(n):
    s = bytearray(b"\x01") * (n + 1)
    s[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if s[p]:
            s[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return [i for i in range(2, n + 1) if s[i]]

def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return sorted(out)

checked_bases = 0
rows = []
for p in primes_upto(500):
    observed_moran = []
    observed_harshad = []
    for B in range(p + 1, p*p + 1):
        a, b = divmod(p*p, B)
        assert 1 <= a < B and 0 <= b < B
        s = a + b
        if (p*p) % s == 0:
            observed_harshad.append(B)
            q = (p*p) // s
            if q >= 2 and all(q % r for r in range(2, isqrt(q)+1)):
                observed_moran.append(B)
        checked_bases += 1

    ds = divisors(p - 1)
    predicted_moran = sorted(p*d + 1 for d in ds)
    predicted_harshad = sorted(predicted_moran + [p*p])

    assert observed_moran == predicted_moran, (p, observed_moran, predicted_moran)
    assert observed_harshad == predicted_harshad, (p, observed_harshad, predicted_harshad)

    for d in ds:
        B = p*d + 1
        a = (p - 1)//d
        b = p - a
        assert a*B + b == p*p
        assert a + b == p

    if p in (2, 3, 5, 7, 11, 13):
        rows.append((p, predicted_moran, p*p))

print("VERIFY_OK", f"primes={len(primes_upto(500))}", f"bases={checked_bases}", f"sample={rows}")
