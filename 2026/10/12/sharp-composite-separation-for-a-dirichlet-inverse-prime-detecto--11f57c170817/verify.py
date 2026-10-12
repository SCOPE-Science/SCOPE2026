#!/usr/bin/env python3
"""Exact finite checks for the Dirichlet-inverse/Jordan-totient composite gap.

Uses the convolution recurrence and independent prime-power formulas. Finite
checks do not establish the universal theorem, whose proof is in RESULT.md.
"""
from math import prod

N = 4000

def sieve(n):
    spf = list(range(n + 1))
    for p in range(2, int(n ** .5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def factors(n, spf):
    out = []
    while n > 1:
        p, e = spf[n], 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out


def run():
    spf = sieve(N)
    fac = [factors(n, spf) for n in range(N + 1)]
    mu = [0] * (N + 1)
    mu[1] = 1
    for n in range(2, N + 1):
        mu[n] = 0 if any(e > 1 for _, e in fac[n]) else (-1) ** len(fac[n])
    div = [[] for _ in range(N + 1)]
    for d in range(1, N + 1):
        for n in range(d, N + 1, d):
            div[n].append(d)

    count = 0
    for k in range(2, 8):
        power = [n ** k for n in range(N + 1)]
        sigma = [0] * (N + 1)
        jordan = [0] * (N + 1)
        inverse = [0] * (N + 1)
        inverse[1] = 1
        for n in range(1, N + 1):
            sigma[n] = sum(power[d] for d in div[n])
            jordan[n] = sum(mu[d] * power[n // d] for d in div[n])
            if n > 1:
                inverse[n] = -sum(sigma[n // d] * inverse[d] for d in div[n][:-1])

        minima = []
        for n in range(1, N + 1):
            f = fac[n]
            jk = prod(p ** ((e - 1) * k) * (p ** k - 1) for p, e in f)
            ik = prod({1: -(1 + p ** k), 2: p ** k}.get(e, 0) for p, e in f)
            assert jordan[n] == jk, (n, k, jordan[n], jk)
            assert inverse[n] == ik, (n, k, inverse[n], ik)
            F = inverse[n] + mu[n] + jordan[n] + 3
            if n == 1:
                assert F == 6
            elif len(f) == 1 and f[0][1] == 1:
                assert F == 0
            else:
                assert abs(F) >= 4 ** k + 3, (n, k, F)
                assert (abs(F) == 4 ** k + 3) == (n == 4), (n, k, F)
                minima.append((abs(F), n))
            count += 1
        print('k=%d n<=%d smallest composite residual=%s second=%s' % (
            k, N, sorted(minima)[0], sorted(minima)[1]))
    print('VERIFY_OK: %d exact values; independent convolution and prime-power checks; finite only' % count)

if __name__ == '__main__':
    run()
