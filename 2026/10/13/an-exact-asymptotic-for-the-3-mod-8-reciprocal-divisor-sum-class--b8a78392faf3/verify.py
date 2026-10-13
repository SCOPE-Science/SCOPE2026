#!/usr/bin/env python3
import math

DIRECT_LIMIT = 30000
COUNT_LIMIT = 1_000_000

def sieve(limit):
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            is_prime[p*p:limit+1:p] = b"\x00" * (((limit - p*p) // p) + 1)
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return is_prime, primes

is_prime, primes = sieve(COUNT_LIMIT)

# Direct reciprocal over F_2 through DIRECT_LIMIT.
a_pos = sorted(
    {m*m for m in range(1, math.isqrt(DIRECT_LIMIT) + 1)}
    | {2*m*m for m in range(1, math.isqrt(DIRECT_LIMIT // 2) + 1)}
)
b = bytearray(DIRECT_LIMIT + 1)
b[0] = 1
for n in range(1, DIRECT_LIMIT + 1):
    parity = 0
    for a in a_pos:
        if a > n:
            break
        parity ^= b[n-a]
    b[n] = parity

def structural_member(n):
    # Factor n; the structural class has exactly one odd exponent.
    m = n
    odd_prime = None
    odd_exp = None
    for p in primes:
        if p*p > m:
            break
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            if e & 1:
                if odd_prime is not None:
                    return False
                odd_prime, odd_exp = p, e
    if m > 1:
        if odd_prime is not None:
            return False
        odd_prime, odd_exp = m, 1
    if odd_prime is None:
        return False
    return odd_prime % 8 == 3 and odd_exp % 4 == 1

checked = 0
members_direct = 0
for n in range(3, DIRECT_LIMIT + 1, 8):
    expected = structural_member(n)
    actual = bool(b[n])
    assert actual == expected, (n, actual, expected)
    checked += 1
    members_direct += int(actual)

# Exact structural count through COUNT_LIMIT from the unique p^(4j+1) k^2 representation.
count = 0
higher_layers = 0
for p in primes:
    if p % 8 != 3:
        continue
    pe = p
    exponent = 1
    while pe <= COUNT_LIMIT:
        K = math.isqrt(COUNT_LIMIT // pe)
        odd_k = (K + 1) // 2
        multiples_p = ((K // p) + 1) // 2
        add = odd_k - multiples_p
        count += add
        if exponent >= 5:
            higher_layers += add
        p4 = p**4
        if pe > COUNT_LIMIT // p4:
            break
        pe *= p4
        exponent += 4

constant = math.pi**2 / 32
scaled = count * math.log(COUNT_LIMIT) / COUNT_LIMIT

assert count == 26460
print(
    "VERIFY_OK",
    f"direct_mod8_cases={checked}",
    f"direct_members={members_direct}",
    f"count_1e6={count}",
    f"higher_layers_1e6={higher_layers}",
    f"scaled_1e6={scaled:.12f}",
    f"constant={constant:.12f}",
)
