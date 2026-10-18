#!/usr/bin/env python3
"""Independent finite binomial checks for power-phase mean-transform weights.

Finite checks are numerical corroboration, not proof of operator-topology limits.
Run: python3 check.py
"""
import cmath
import math


def binomial_phase(n: int, beta: float, theta: float = 1., start: int = 0):
    mu = n / 2
    r = min(n, int(13 * math.sqrt(n) / 2) + 10)
    lo, hi = max(0, n // 2 - r), min(n, (n + 1) // 2 + r)
    logprob = (math.lgamma(n + 1) - math.lgamma(lo + 1)
               - math.lgamma(n - lo + 1) - n * math.log(2))
    p = math.exp(logprob)
    z = 0j
    mass = 0.
    for k in range(lo, hi + 1):
        z += p * cmath.exp(1j * theta * (start + k + 1) ** beta)
        mass += p
        if k < hi:
            p *= (n - k) / (k + 1)
    h = mu + start + 1
    t = theta * beta * h ** (beta - 1)
    linearized = cmath.exp(1j * theta * h ** beta) * math.cos(t / 2) ** n
    return z, linearized, mass


def check():
    count = 0
    for beta in (0.3, 0.5, 0.7, 0.9):
        previous_err = None
        for n in (500, 2000, 10000):
            z, lin, mass = binomial_phase(n, beta)
            assert abs(mass - 1) < 1e-8, (beta, n, mass)
            err = abs(z - lin)
            assert err < (0.025 if beta < .8 else .002), (beta, n, err)
            if previous_err is not None:
                assert err < previous_err + 0.00003, (beta, n, err, previous_err)
            previous_err = err
            count += 3 if n > 500 else 2
        z, _, _ = binomial_phase(10000, beta)
        if beta == 0.3:
            assert abs(z) > .998
        if beta == 0.5:
            assert abs(abs(z) - math.exp(-1 / 16)) < 1e-4
        if beta == 0.7:
            assert abs(z) < .03
        if beta == 0.9:
            assert abs(z) < 1e-9
        count += 1
    # Independent direct finite convolution for low n, all starting sites.
    for n in range(0, 13):
        for j in range(0, 9):
            for beta in (.3, .5, .7):
                direct = sum(math.comb(n, k) / 2 ** n
                             * cmath.exp(1j * (j + k + 1) ** beta)
                             for k in range(n + 1))
                recurrence, _, _ = binomial_phase(n, beta, start=j)
                assert abs(direct - recurrence) < 1e-11, (n, j, beta)
                count += 1
    print(f"PASS: {count} independent finite numerical assertions")

if __name__ == '__main__':
    check()
