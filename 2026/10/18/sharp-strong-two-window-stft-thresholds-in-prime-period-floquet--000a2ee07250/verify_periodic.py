#!/usr/bin/env python3
"""Finite numerical and combinatorial checks for prime-period cyclic STFT thresholds.

The universal assertion uses a prime-order uncertainty theorem; finite checks here
corroborate the explicit polynomial witnesses and support-gap bookkeeping.
"""
import cmath
import math


def threshold(p, q):
    a, b = divmod(p - 1, q + 2)
    return q * a + min(b, q - 1)


def zero_run_lengths(support):
    """Cyclic zero intervals between consecutive nonzero coordinates."""
    n = len(support)
    indices = [i for i in range(n) if support[i]]
    if not indices:
        return []
    return [((indices[(i + 1) % len(indices)] - indices[i]) % n - 1)
            if i + 1 < len(indices) else
            (indices[0] + n - indices[-1] - 1)
            for i in range(len(indices))]


def disconnected(support, m):
    # At least two distinct gaps each containing m or more zeros.
    return sum(gap >= m for gap in zero_run_lengths(support)) >= 2


def dft(values):
    n = len(values)
    return [sum(values[t] * cmath.exp(-2j * math.pi * k * t / n)
                for t in range(n)) for k in range(n)]


def witness(p, q, m):
    n = p * q
    h = m // q
    roots = list(range(1, h + 1)) + list(range(h + 2, 2 * h + 2))
    coeffs = [1 + 0j]
    for ell in roots:
        r = cmath.exp(-2j * math.pi * ell / p)
        nxt = [0j] * (len(coeffs) + 1)
        for j, a in enumerate(coeffs):
            nxt[j] -= r * a
            nxt[j + 1] += a
        coeffs = nxt
    f = [coeffs[t % p] if t % p < len(coeffs) else 0j for t in range(n)]
    F = dft(f)
    maxf, maxF = max(abs(x) for x in f), max(abs(x) for x in F)
    sf = [abs(x) > 1e-8 * maxf for x in f]
    sF = [abs(x) > 1e-8 * maxF for x in F]
    assert disconnected(sf, m), (p, q, m, 'time', zero_run_lengths(sf))
    assert disconnected(sF, m), (p, q, m, 'freq', zero_run_lengths(sF))
    assert all(not sF[k] for k in range(n) if k % q), (p, q, m)
    for ell in range(p):
        if ell in roots:
            assert not sF[q * ell], (p, q, m, ell)
        else:
            assert sF[q * ell], (p, q, m, ell)
    return len(roots)


def check_support_bound(p, q):
    # Exhaust support-pattern compatibility with the prime-order uncertainty
    # inequality. It is a finite combinatorial implication, not an exhaustive
    # enumeration of all signal amplitudes.
    nonempty = [[i in S for i in range(p)]
                for bits in range(1, 1 << p)
                for S in [[i for i in range(p) if bits >> i & 1]]]
    for m in range(threshold(p, q) + 1, p):
        h = m // q
        for st in nonempty:
            if not any(v >= m for v in zero_run_lengths(st)):
                continue
            s = sum(st)
            for sf in nonempty:
                t = sum(sf)
                if s + t < p + 1:
                    continue
                expanded = [False] * (p * q)
                for ell, v in enumerate(sf):
                    expanded[q * ell] = v
                assert not disconnected(expanded, m), (p, q, m, st, sf)


def main():
    primes = [3, 5, 7, 11, 13, 17]
    multipliers = [2, 3, 4, 7]
    ntests = 0
    total_roots = 0
    for p in primes:
        for q in multipliers:
            M = threshold(p, q)
            assert all(m + 2 * (m // q) <= p - 1 for m in range(1, M + 1))
            assert all(m + 2 * (m // q) > p - 1 for m in range(M + 1, p))
            for m in range(1, M + 1):
                total_roots += witness(p, q, m)
                ntests += 1
    for p in [3, 5, 7]:
        for q in multipliers:
            check_support_bound(p, q)
    print('VERIFY_OK constructed_witnesses=%d polynomial_roots=%d '
          'prime_support_bounds_p=3,5,7' % (ntests, total_roots))

if __name__ == '__main__':
    main()
