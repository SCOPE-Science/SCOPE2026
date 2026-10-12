#!/usr/bin/env python3
from math import isqrt, sqrt

def primes_upto(n):
    sieve = bytearray(b"\x01")*(n+1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00"*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if sieve[i]]

def divisors(n):
    out = []
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return sorted(out)

def digit_sum(n, b):
    s = 0
    while n:
        n, r = divmod(n, b)
        s += r
    return s

def direct_spectrum(p, q):
    n = p*q
    return [
        b for b in range(q+1, n+1)
        if digit_sum(n,b) == digit_sum(p,b) + digit_sum(q,b)
    ]

def formula_spectrum(p, q):
    if p == 2:
        return []
    K = p*q-p-q
    D = (p+q)*(p+q)-4*K
    rho = (p+q-sqrt(D))/2
    return sorted(1 + K//a for a in divisors(K) if a <= rho + 1e-12)

P = primes_upto(5000)
pairs = 0
bases_tested = 0
multi_examples = []

small = [p for p in P if p < 200]
for i,p in enumerate(small):
    for q in small[i:]:
        got = direct_spectrum(p,q)
        want = formula_spectrum(p,q)
        assert got == want, (p,q,got,want)
        pairs += 1
        bases_tested += p*q-q
        if p >= 3 and q >= 3:
            if (p,q) == (3,3):
                assert got == []
            else:
                canonical = (p-1)*(q-1)
                assert canonical in got
                assert all(b % 2 == 0 for b in got)
        if len(got) > 1 and len(multi_examples) < 10:
            multi_examples.append((p,q,got))

for q in P:
    if q < 3:
        continue
    if q >= 5000:
        break
    got3 = formula_spectrum(3,q)
    if q == 3:
        assert got3 == []
    else:
        assert got3 == [2*(q-1)]

    if q >= 5:
        got5 = formula_spectrum(5,q)
        if q >= 11 and q % 3 == 2:
            assert got5 == [(4*q-2)//3, 4*q-4], (q,got5)
        else:
            assert got5 == [4*q-4], (q,got5)

print(
    "VERIFY_OK",
    f"prime_pairs={pairs}",
    f"bases_tested={bases_tested}",
    f"small_prime_q_checked={sum(1 for q in P if q < 5000)}",
    f"multi_examples={multi_examples}"
)
