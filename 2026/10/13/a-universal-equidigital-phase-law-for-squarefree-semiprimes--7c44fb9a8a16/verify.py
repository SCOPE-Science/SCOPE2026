#!/usr/bin/env python3
from bisect import bisect_left
from math import log

def digits(n, B):
    d = 1
    p = B
    while n >= p:
        d += 1
        p *= B
    return d

def primes_upto(n):
    s = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        s[0] = 0
    if n >= 1:
        s[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if s[p]:
            s[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
    return [i for i in range(2, n + 1) if s[i]]

# Exact classification checks in several bases.
small_primes = primes_upto(5000)
checked = 0
for B in range(2, 17):
    for i, p in enumerate(small_primes[:180]):
        for q in small_primes[i+1:180]:
            a, b = digits(p, B), digits(q, B)
            factor_digits = a + b
            product_digits = digits(p*q, B)
            assert product_digits in (factor_digits - 1, factor_digits)
            equidigital = product_digits == factor_digits
            assert equidigital == (p*q >= B**(a+b-1))
            checked += 1

# Decimal equal-block proportions through six digits.
LIMIT = 1_000_000
P = primes_upto(LIMIT)
observed = []
for a in range(2, 7):
    lo, hi = 10**(a-1), 10**a
    block = [p for p in P if lo <= p < hi]
    total = len(block) * (len(block) - 1)
    threshold = 10**(2*a - 1)
    good = 0
    for p in block:
        qmin = (threshold + p - 1) // p
        j = bisect_left(block, qmin)
        good += len(block) - j
        if p*p >= threshold:
            good -= 1
    observed.append((a, len(block), good / total))

rho10 = 10 * (9 - log(10)) / 81
expected = [
    0.7333333333333333,
    0.7810499359795134,
    0.7980758629274626,
    0.8046159689682201,
    0.8080229362459068,
]
for (_, _, got), want in zip(observed, expected):
    assert abs(got - want) < 1e-12

assert abs(rho10 - 0.8268413465439449) < 1e-15
print(
    "VERIFY_OK",
    f"exact_pairs={checked}",
    f"rho10={rho10:.15f}",
    "observed=" + repr(observed),
)
