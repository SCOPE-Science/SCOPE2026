#!/usr/bin/env python3

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p)//p)+1)
    return [i for i in range(2, n+1) if sieve[i]]

def isprime64(n):
    if n < 2:
        return False
    small = [2,3,5,7,11,13,17,19,23,29,31,37]
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n-1):
            continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1:
                break
        else:
            return False
    return True

ells = [l for l in primes_upto(31) if l % 2]
ps = [p for p in primes_upto(97) if p > 2]
checks = 0
for ell in ells:
    for p in ps:
        D = p + p**ell - 1
        U = p**(ell*ell) + 1
        R = 1 - (p-1)**ell
        assert U % D == R % D
        assert 0 < abs(R) < D
        assert U % D != 0
        checks += 1

ray = []
for ell in ells:
    D = 2**ell + 1
    U = 2**(ell*ell) + 1
    assert U % D == 0
    q = U // D
    ray.append((ell, q))

assert ray[0] == (3, 57)
assert 57 == 3 * 19
assert ray[1] == (5, 1016801)
assert 1016801 == 251 * 4051
q7 = dict(ray)[7]
assert q7 == 4363953127297
assert isprime64(q7)

ell = 7
p = 2
q = q7
sig_star = (1 + p**(ell*ell)) * (1 + q)
sig_e = (p + p**ell + p**(ell*ell)) * q
assert sig_star == sig_e

print(
    "VERIFY_OK",
    f"odd_base_checks={checks}",
    f"prime_square_rays={len(ray)}",
    f"ell7_q={q7}",
    f"ell7_prime={isprime64(q7)}",
)
