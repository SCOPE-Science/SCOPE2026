#!/usr/bin/env python3

SIEVE_MAX = 410000
CHECK_R = 300
CHECK_P = 1000

def sieve(n):
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
    return is_prime

IP = sieve(SIEVE_MAX)
PRIMES = [i for i in range(2, SIEVE_MAX + 1) if IP[i]]

violations = []
for a, b in zip(PRIMES, PRIMES[1:]):
    if a >= 396738:
        break
    if 5 * b > 7 * a:
        violations.append((a, b))
assert violations == [(2, 3), (3, 5), (7, 11)], violations

def next_prime_strict(x_num, x_den=1):
    k = x_num // x_den + 1
    while k <= SIEVE_MAX and not IP[k]:
        k += 1
    assert k <= SIEVE_MAX
    return k

def least_prime_gt(r):
    return next_prime_strict(r)

def witness(r, p):
    target = p * (p - r)
    if r == 1:
        if p == 2:
            return 6, 2
        return 2 * p * p, target

    a = least_prime_gt(r)
    delta = a - r

    if delta == 1:
        if p != a:
            return a * p * p, target
        b = next_prime_strict(a)
        return a * b, (a - r) * (b - r)

    q = next_prime_strict(p * p, a)
    if q == 11 and 7 * a <= p * p < 11 * a:
        if r == 3 and p == 7:
            return 55, (5 - 3) * (11 - 3)
        if r == 5 and p == 7:
            return 77, (7 - 5) * (11 - 5)

    return a * q, (a - r) * (q - r)

tested = 0
identity_checks = 0
for r in range(1, CHECK_R + 1):
    for p in PRIMES:
        if p > CHECK_P:
            break
        if p <= r:
            continue

        m, sm = witness(r, p)
        target = p * (p - r)
        assert m > p * p, (r, p, m)
        assert sm > 0, (r, p, m, sm)
        assert sm <= target, (r, p, m, sm, target)
        tested += 1

        if r >= 2:
            a = least_prime_gt(r)
            d = a - r
            if d >= 2:
                x = p - a
                cleared = (
                    d * a * (3 * r - 2 * d)
                    + a * (5 * r - 4 * d) * x
                    + (5 * r - 2 * d) * x * x
                )
                assert cleared > 0
                identity_checks += 1

print(
    "VERIFY_OK",
    f"ratio_violations={violations}",
    f"witnesses={tested}",
    f"identity_checks={identity_checks}",
    f"r=1..{CHECK_R}",
    f"p<={CHECK_P}",
)
