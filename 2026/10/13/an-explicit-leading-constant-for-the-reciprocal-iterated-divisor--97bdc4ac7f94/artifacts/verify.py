#!/usr/bin/env python3
"""Exact finite checks for the squarefree/powerful decomposition identity.

The asymptotic theorem is proved analytically; this program only tests
its arithmetic identities and sample finite sums. Standard library only.
"""
from math import isqrt, log, pi

LIMIT = 200_000
B_LIMIT = 100_000

smallest = list(range(LIMIT + 1))
for p in range(2, isqrt(LIMIT) + 1):
    if smallest[p] == p:
        for multiple in range(p * p, LIMIT + 1, p):
            if smallest[multiple] == multiple:
                smallest[multiple] = p

def factors(n):
    while n > 1:
        p = smallest[n]
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        yield p, k

# Multiplicative recursion for the divisor-count function.
tau = [0] * (LIMIT + 1)
tau[1] = 1
for n in range(2, LIMIT + 1):
    p = smallest[n]
    reduced = n
    exponent = 0
    while reduced % p == 0:
        reduced //= p
        exponent += 1
    tau[n] = tau[reduced] * (exponent + 1)

# Independent direct divisor counts for the small range.
for n in range(1, 2001):
    by_divisors = sum(1 if k * k == n else 2
                      for k in range(1, isqrt(n) + 1) if n % k == 0)
    assert tau[n] == by_divisors

sum_value = 0.0
strong_checks = 0
for n in range(1, LIMIT + 1):
    unitary_squarefree = 1
    powerful = 1
    number_singletons = 0
    for p, exponent in factors(n):
        if exponent == 1:
            unitary_squarefree *= p
            number_singletons += 1
        else:
            powerful *= p ** exponent
    assert unitary_squarefree * powerful == n
    assert tau[n] == (1 << number_singletons) * tau[powerful]
    assert all(exponent >= 2 for _, exponent in factors(powerful))

    value = tau[powerful]
    two_adic_exponent = 0
    while value % 2 == 0:
        value //= 2
        two_adic_exponent += 1
    assert value % 2 == 1
    assert tau[tau[n]] == (number_singletons + two_adic_exponent + 1) * tau[value]
    strong_checks += 1
    sum_value += 1.0 / tau[tau[n]]

# List powerful integers in two independent ways.
from_factorization = {
    b for b in range(1, B_LIMIT + 1)
    if all(exponent >= 2 for _, exponent in factors(b))
}
from_square_cube = set()
for v in range(1, B_LIMIT + 1):
    if v ** 3 > B_LIMIT:
        break
    if any(exponent >= 2 for _, exponent in factors(v)):
        continue
    for u in range(1, isqrt(B_LIMIT // (v ** 3)) + 1):
        from_square_cube.add(u * u * v ** 3)
assert from_factorization == from_square_cube
assert 1 in from_factorization

# An exact series is proved in the result; the numerical value below
# is a *partial sum*, not a certified interval or a proof of convergence.
constant_partial = 0.0
for b in sorted(from_factorization):
    density_factor = 1.0
    for p, _ in factors(b):
        density_factor *= p / (p + 1)
    u = tau[b]
    while u % 2 == 0:
        u //= 2
    constant_partial += density_factor / (b * tau[u])
constant_partial *= 6 / (pi * pi)
assert 0.82 < constant_partial < 0.84
assert constant_partial > 6 / (pi * pi)

# Check the first two terms of the exact constant series.
assert tau[1] == 1 and tau[4] == 3
assert (2 / 3) / (4 * tau[3]) == 1 / 12

print(
    'VERIFY_OK '
    f'identity_n=1..{LIMIT} '
    'small_divisor_checks=2000 '
    f'powerful_bound={B_LIMIT} '
    f'powerful_count={len(from_factorization)} '
    'square_cube_crosscheck=yes '
    f'finite_sum={sum_value:.9f} '
    f'partial_C={constant_partial:.12f} '
    'analytic_limit_proof=separate'
)
