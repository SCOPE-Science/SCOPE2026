"""Finite diagnostics for prime-gap constrained renewal entropy.

This verifies finite-sum Gibbs identities, not the asymptotic prime number theorem.
"""
import math


def primes_up_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for j in range(2, math.isqrt(n) + 1):
        if sieve[j]:
            sieve[j * j:n + 1:j] = b'\x00' * ((n - j * j) // j + 1)
    return [j for j in range(n + 1) if sieve[j]]


def run():
    primes = primes_up_to(200000)
    assert len(primes) > 17000
    for s in (0.02, 0.01, 0.005, 0.002):
        weights = [math.exp(-s * (p + 1)) for p in primes]
        z = sum(weights)
        m = sum((p + 1) * w for p, w in zip(primes, weights)) / z
        t = 1 / m
        h_direct = -sum((w / z) * math.log(w / z)
                        for w in weights if w / z > 0) * t
        h_legendre = t * math.log(z) + s
        assert abs(h_direct - h_legendre) < 1e-10
        assert 0 < t < 1 / 3
    print('FINITE_RENEWAL_IDENTITY_OK: 4 numerical finite-prime Gibbs checks')
    print('LIMITATION: finite prime cutoffs do not verify the infinite prime asymptotic')


if __name__ == '__main__':
    run()
