#!/usr/bin/env python3
"""Finite diagnostics for circular Fock sampling; not an infinite-dimensional proof."""
import cmath
import math


def probs(n, rho):
    mu = n * rho
    end = max(160, int(mu + 35 * math.sqrt(mu) + 100))
    p = [0.0] * n
    mass = math.exp(-mu)
    for k in range(end + 1):
        p[k % n] += mass
        mass *= mu / (k + 1)
    return p


def jrate(x, rho):
    return rho if x == 0 else x * math.log(x / rho) - x + rho


def logridentric(x):
    if x == 0:
        return -1.0
    return (x + 1) * math.log(x + 1) - x * math.log(x) - 1


def exponent(rho):
    if rho <= math.exp(-1):
        return jrate(1.0, rho)
    lo, hi = 0.0, max(2.0, rho + 1)
    for _ in range(100):
        mid = (lo + hi) / 2
        if logridentric(mid) < math.log(rho):
            lo = mid
        else:
            hi = mid
    x = (lo + hi) / 2
    return jrate(x, rho)


def run():
    checks = 0
    for n in (5, 9, 17):
        for rho in (0.2, 0.4, 0.75, 1.5):
            p = probs(n, rho)
            assert all(x > 0 for x in p)
            assert abs(math.fsum(p) - 1.0) < 2e-12
            checks += 2
            for mode in range(n):
                eig = 0j
                for t in range(n):
                    theta = 2 * math.pi * t / n
                    w = cmath.exp(1j * theta)
                    eig += cmath.exp(-rho * n + rho * n * w - 1j * mode * theta) / n
                assert abs(eig - p[mode]) < 3e-12, (n, rho, mode, eig, p[mode])
                checks += 1
    for rho in (0.2, 0.4, 0.5, 1.0, 2.0):
        n = 600
        # Log-sum-exp avoiding underflow for the rarest residues.
        logs = [[] for _ in range(n)]
        mu = rho * n
        end = int(mu + 30 * math.sqrt(mu) + 10 * n + 100)
        for k in range(end):
            logs[k % n].append(-mu + k * math.log(mu) - math.lgamma(k + 1))
        vals = []
        for seq in logs:
            mx = max(seq)
            vals.append(mx + math.log(math.fsum(math.exp(z - mx) for z in seq)))
        obs = -min(vals) / n
        expected = exponent(rho) + math.log(n) / (2 * n)
        assert abs(obs - expected) < 0.02, (rho, obs, expected)
        checks += 1
    print(f'PASS: {checks} finite diagnostic assertions; no independent certification')


if __name__ == '__main__':
    run()
