#!/usr/bin/env python3
"""Finite diagnostic for a translated Boole iteration and its logarithmic identity."""
import cmath
import math


def run(beta, threshold=600.0):
    h = beta * beta
    w = complex(0.0, beta)
    potential = w + cmath.log(w-1)
    errors = 0j
    n = 0
    checks = 0
    while w.real < threshold and n < 1000000:
        t = h / abs(w)**2
        assert 0 < t <= 1 + 1e-12
        nxt = w + h - h / w
        assert nxt.imag >= w.imag and nxt.real >= -1e-12
        err = cmath.log(1 + h / w) - h / w
        errors += err
        if n < 500:
            left = (nxt + cmath.log(nxt-1)) - potential
            assert abs(left - (h + err)) < 1e-10
            checks += 1
        w = nxt
        potential = w + cmath.log(w-1)
        n += 1
    assert w.real >= threshold, (beta, n)
    # For x>=2, x gains at least h*(1-1/x) each step.
    # Sum of future log-height increments is bounded by
    # h/x**2 + 1/[(1-1/x)*x].
    tail = h / w.real**2 + 1 / ((1 - 1 / w.real) * w.real)
    low, high = w.imag, w.imag * math.exp(tail)
    bound = beta**3 / 3 + 2 * beta**2 * math.log(4 * math.pi / beta)
    assert low >= math.pi-bound and high <= math.pi + bound
    assert high - low < 0.10
    return beta, n, low, high, checks


def main():
    total = 0
    for b in (0.25, 0.125, 0.0625, 0.03125):
        beta, n, low, high, checks = run(b)
        total += checks + 5
        print(f'beta={beta:.5g}, iterations={n}, B_infinity in [{low:.8f}, {high:.8f}]')
    print(f'PASS: {total} finite checks; all infinite conclusions use the analytic proof.')


if __name__ == '__main__':
    main()
