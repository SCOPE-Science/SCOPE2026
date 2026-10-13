#!/usr/bin/env python3
from math import isqrt

def sigma_sieve(n):
    s = [0] * (n + 1)
    for d in range(1, n + 1):
        for m in range(d, n + 1, d):
            s[m] += d
    return s

def omega_sieve(n):
    w = [0] * (n + 1)
    for p in range(2, n + 1):
        if w[p] == 0:
            for m in range(p, n + 1, p):
                w[m] += 1
    return w

def is_prime_power(n):
    if n < 2:
        return False
    # Determine whether n has exactly one distinct prime divisor.
    x = n
    distinct = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            distinct += 1
            while x % p == 0:
                x //= p
            if distinct > 1:
                return False
        p += 1 if p == 2 else 2
    if x > 1:
        distinct += 1
    return distinct == 1

N = 3000
sigma = sigma_sieve(N)
omega = omega_sieve(N)

# Source-table examples for WPM(1).
source_examples = [(4, 6), (10, 16), (34, 68), (60, 81), (91, 273)]
for a, b in source_examples:
    assert a * sigma[a] + b * sigma[b] == (a + b) ** 2

pairs = []
for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        if a * sigma[a] + b * sigma[b] == (a + b) ** 2:
            pairs.append((a, b))
            assert a > 1 and b > 1
            assert omega[a] >= 1 and omega[b] >= 1
            # The theorem's two support conclusions.
            assert not (omega[a] == 1 and omega[b] == 1)
            # Neither coordinate is prime.
            assert not (omega[a] == 1 and sigma[a] == a + 1)
            assert not (omega[b] == 1 and sigma[b] == b + 1)

# Direct prime-power grid check, independent of the pair scan's classification assertions.
prime_powers = [n for n in range(2, N + 1) if is_prime_power(n)]
pp_checks = 0
for i, a in enumerate(prime_powers):
    for b in prime_powers[i:]:
        pp_checks += 1
        assert a * sigma[a] + b * sigma[b] != (a + b) ** 2

print(
    "VERIFY_OK "
    f"bound={N} "
    f"pairs={len(pairs)} "
    f"source_examples={len(source_examples)} "
    f"prime_power_pair_checks={pp_checks}"
)
