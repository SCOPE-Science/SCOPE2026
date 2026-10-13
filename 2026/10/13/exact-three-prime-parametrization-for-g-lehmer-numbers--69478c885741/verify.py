#!/usr/bin/env python3
from math import isqrt

LIMIT = 5_000_000

# Prime sieve.
is_prime = bytearray(b"\x01") * (LIMIT + 1)
is_prime[0:2] = b"\x00\x00"
for p in range(2, isqrt(LIMIT) + 1):
    if is_prime[p]:
        start = p * p
        is_prime[start:LIMIT+1:p] = b"\x00" * (((LIMIT - start) // p) + 1)
primes = [p for p in range(3, LIMIT + 1, 2) if is_prime[p]]


def beta(p):
    return 1 if p % 4 == 1 else -1


def phi_gaussian_squarefree3(p, q, r):
    return (p - beta(p)) * (q - beta(q)) * (r - beta(r))


def f_odd(n):
    return n - (1 if n % 4 == 1 else -1)


def parametrized(p, q, r):
    vals = (p, q, r)
    plus = [x for x in vals if x % 4 == 1]
    minus = [x for x in vals if x % 4 == 3]
    if len(minus) == 1:
        t = minus[0]
        a, b = plus
        return (a - t - 1) > 0 and (b - t - 1) > 0 and (a - t - 1) * (b - t - 1) == t*t + t + 1
    if len(plus) == 1:
        s = plus[0]
        a, b = minus
        return (a - s + 1) > 0 and (b - s + 1) > 0 and (a - s + 1) * (b - s + 1) == s*s - s + 1
    return False

# Check the elementary quotient anchor used in the proof.
assert 125 * (105 + 1) < 128 * 105

hits = []
triples = 0
L = len(primes)
for i, p in enumerate(primes):
    if p * (p + 2) * (p + 4) > LIMIT:
        break
    for j in range(i + 1, L):
        q = primes[j]
        if p * q * (q + 2) > LIMIT:
            break
        max_r = LIMIT // (p * q)
        for k in range(j + 1, L):
            r = primes[k]
            if r > max_r:
                break
            n = p * q * r
            triples += 1
            Phi = phi_gaussian_squarefree3(p, q, r)
            F = f_odd(n)
            direct = (F % Phi == 0)
            param = parametrized(p, q, r)
            assert direct == param, (n, p, q, r, Phi, F, direct, param)
            if direct:
                assert F == Phi, (n, Phi, F)
                hits.append(n)

hits.sort()
expected = [255, 385, 34561, 195841, 1034881, 4070401, 4746241]
assert hits == expected, hits
print('VERIFY_OK', f'limit={LIMIT}', f'triples={triples}', f'hits={hits}', 'all_quotients=1')
