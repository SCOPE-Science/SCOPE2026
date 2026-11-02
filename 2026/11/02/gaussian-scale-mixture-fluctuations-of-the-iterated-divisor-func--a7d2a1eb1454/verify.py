#!/usr/bin/env python3
"""Reproduce finite arithmetic checks for an iterated-divisor fluctuation theorem.

This program verifies identities exactly and provides illustrative finite
frequencies; it does not establish any infinite limiting distribution.
"""
import argparse
import math
from collections import Counter


def spf_sieve(n):
    s = list(range(n + 1))
    for p in range(2, math.isqrt(n) + 1):
        if s[p] == p:
            for j in range(p * p, n + 1, p):
                if s[j] == j:
                    s[j] = p
    return s


def exponents(n, spf):
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        yield p, e


def count_divisors_direct(n):
    d = 0
    for k in range(1, math.isqrt(n) + 1):
        if n % k == 0:
            d += (1 if k * k == n else 2)
    return d


def factorial_oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


def powerful_density(beta, spf):
    zeta2 = math.pi * math.pi / 6.0
    f = 1.0 / (zeta2 * beta)
    for p, e in exponents(beta, spf):
        assert e >= 2
        f *= p / (p + 1)
    return f


def main(bound):
    spf = spf_sieve(bound)
    mass = Counter()
    weights = Counter()
    examined = 0
    max_tau = 0
    for n in range(1, bound + 1):
        fac = list(exponents(n, spf))
        beta = 1
        sqfree_count = 0
        tau_n = 1
        tau_beta = 1
        for p, e in fac:
            tau_n *= e + 1
            if e == 1:
                sqfree_count += 1
            else:
                beta *= p ** e
                tau_beta *= e + 1
        odd = factorial_oddpart(tau_beta)
        u = (tau_beta // odd).bit_length() - 1
        w = count_divisors_direct(odd)
        tau_tau_n = count_divisors_direct(tau_n)
        assert tau_tau_n == (sqfree_count + u + 1) * w, (n, tau_tau_n)
        assert beta == 1 or all(e >= 2 for p, e in exponents(beta, spf))
        mass[beta] += 1
        weights[w] += 1
        max_tau = max(max_tau, tau_tau_n)
        examined += 1
    # Independently check predicted frequencies in a few fixed powerful fibers.
    checks = []
    for beta in (1, 4, 8, 9, 16, 25, 27, 36):
        observed = mass[beta] / bound
        expected = powerful_density(beta, spf)
        checks.append((beta, round(observed, 6), round(expected, 6)))
        assert abs(observed - expected) < 0.004, (beta, observed, expected)
    # Euler product of squarefree-part-free odd components: W=1.
    product = 1.0
    prime_count = 0
    for p in range(2, bound + 1):
        if spf[p] != p:
            continue
        local = 1.0
        e = 1
        while e < 64:
            local += float(p) ** (-e)
            e = 2 * e + 1
        product *= (1 - 1 / p) * local
        prime_count += 1
    assert 0.68 < product < 0.70
    assert mass[4] > 0 and mass[1] > 0
    print('VERIFY_OK exact_identity_cases=%d powerful_fibers=%d w_classes=%d max_iterated_tau=%d' %
          (examined, len(mass), len(weights), max_tau))
    print('fixed_powerful_fibers: beta, observed, predicted =', checks)
    print('empirical_P_W1=%.6f empirical_P_W2=%.6f prime_truncated_P_W1=%.6f primes=%d' %
          (weights[1]/bound, weights[2]/bound, product, prime_count))
    print('Finite checks do not prove the conditional Erdos-Kac law or the limit distribution.')

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--bound', type=int, default=200000)
    args = ap.parse_args()
    main(args.bound)
