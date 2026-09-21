#!/usr/bin/env python3
"""Exact finite checks for the prime-power-complement psi-divisibility theorem."""

from math import gcd


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def v_q(n, q):
    e = 0
    while n % q == 0:
        e += 1
        n //= q
    return e


def psi_prime_power(p, a):
    if a == 0:
        return 1
    return (p ** (2 * a + 1) + 1) // (p + 1)


checked = 0
for p in range(2, 200):
    if not is_prime(p):
        continue
    for q in range(2, p):
        if not is_prime(q) or (p - 1) % q:
            continue
        max_gamma = v_q(p - 1, q)
        for alpha in range(1, 5):
            A = psi_prime_power(p, alpha)
            for beta in range(1, 9):
                for gamma in range(1, min(beta, max_gamma) + 1):
                    psi_H = psi_prime_power(q, beta)
                    psi_C = psi_prime_power(q, beta - gamma)
                    psi_G = (
                        p ** alpha * psi_H
                        + (A - p ** alpha) * psi_C
                    )
                    E = (q ** (2 * gamma) - 1) // (q + 1)

                    assert gcd(A, psi_G) == gcd(A, E)
                    assert E < q ** (2 * gamma)
                    assert q ** (2 * gamma) < A
                    assert psi_G % A != 0
                    checked += 1

assert checked == 4544
print(f"{checked} compatible parameter tuples checked; 0 failures")
