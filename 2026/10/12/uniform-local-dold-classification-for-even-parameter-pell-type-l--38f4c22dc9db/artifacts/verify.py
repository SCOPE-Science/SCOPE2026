"""Direct exact-integer checks of Lucas p-part and Mobius-transform identities.

Finite checks are corroboration, not a proof of the infinite statements.
"""
from math import gcd, isqrt


def primes_up_to(limit):
    return [n for n in range(2, limit+1) if all(n % d for d in range(2, isqrt(n)+1))]


def vp(n, p):
    assert n > 0
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def lucas(P, count):
    U = [0, 1]
    for n in range(2, count+1):
        U.append(P * U[-1] + U[-2])
    return U[:count+1]


def mobius(n):
    if n == 1:
        return 1
    sign = 1
    for p in primes_up_to(isqrt(n)):
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            sign = -sign
            while n % p == 0:
                n //= p
    if n > 1:
        sign = -sign
    return sign


def divisors(n):
    return (d for d in range(1, n+1) if n % d == 0)


def predicted(P, p, n, z, e):
    if n == 1:
        return 1
    if p == 2:
        s = vp(P, 2)
        if n == 2:
            return 2**s - 1
        if n & (n-1) == 0:
            j = n.bit_length()-1
            return 2**(s+j-2) if j >= 2 else 0
        return 0
    if n == z:
        return p**e - 1
    if n % z:
        return 0
    q = n // z
    if q <= 1:
        return 0
    j = vp(q, p)
    return p**(e+j-1)*(p-1) if q == p**j else 0


count = 0
odd_cases = 0
for P in range(2, 19, 2):
    U = lucas(P, 120)
    for p in primes_up_to(53):
        A = [0] + [p**vp(U[n],p) for n in range(1,121)]
        if p == 2:
            z, e = 2, vp(P,2)
        else:
            z = next(n for n in range(2, p+2) if U[n] % p == 0)
            e = vp(U[z],p)
            odd_cases += 1
            for n in range(1,121):
                assert vp(U[n],p) == (e + vp(n//z,p) if n % z == 0 else 0), (P,p,n)
        for n in range(1,121):
            d = sum(mobius(n//j)*A[j] for j in divisors(n))
            want = predicted(P,p,n,z,e)
            assert d == want, (P,p,n,d,want)
            assert d >= 0
            count += 1
        if p != 2:
            for n in range(1,121):
                d = predicted(P,p,n,z,e)
                if d and n > 1:
                    assert (z//gcd(z,p-1)*d) % n == 0, (P,p,n)
        else:
            for n in range(2,121):
                assert (2*predicted(P,p,n,z,e)) % n == 0, (P,n)

print(f'VERIFY_OK parameters={len(range(2,19,2))} primes={len(primes_up_to(53))} mobius_checks={count} odd_prime_valuation_cases={odd_cases} all_support_nonnegative=PASS repair_divisibility=PASS')
