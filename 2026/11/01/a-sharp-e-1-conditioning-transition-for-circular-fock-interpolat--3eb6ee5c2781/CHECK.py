#!/usr/bin/env python3
"""Numerical consistency checks for circular Bargmann--Fock conditioning.

Only Python standard-library modules are required. These checks supplement,
but do not replace, the analytical large-deviation proof.
"""
import cmath
import math


def logadd(values):
    m = max(values)
    return m + math.log(sum(math.exp(v - m) for v in values))


def spectrum(n, rho):
    t = rho * n
    cutoff = int(max(t + 40 * math.sqrt(t + 1) + 10 * n, 15 * n + 30))
    logs = [-t + j * math.log(t) - math.lgamma(j + 1) for j in range(cutoff + 1)]
    return [math.log(n) + logadd(logs[k::n]) for k in range(n)]


def rate(rho):
    if rho <= 1 / math.e:
        return rho - 1 - math.log(rho), None
    target = 1 + math.log(rho)

    def equation(u):
        return (u + 1) * math.log(u + 1) - u * math.log(u) - target

    lo, hi = 0.0, max(rho, 1.0)
    assert equation(hi) > 0
    for _ in range(110):
        mid = (lo + hi) / 2
        if equation(mid) < 0:
            lo = mid
        else:
            hi = mid
    u = (lo + hi) / 2
    return rho - u + u * math.log(u / rho), u


def prefactor(n, rho, u):
    if u is None:
        return math.sqrt(rho)
    a = rho / u
    b = rho / (u + 1)
    eta = n * u - math.floor(n * u)
    zstar = math.log(-math.log(b) / math.log(a) * math.sqrt(u / (u + 1))) / math.log(a / b)
    m = math.floor(eta + zstar)

    def f(m):
        d = m - eta
        return a ** d / math.sqrt(u) + b ** d / math.sqrt(u + 1)

    return 1 / (math.sqrt(rho) * min(f(m), f(m + 1)))


def run():
    assertions = 0
    for n, rho in ((4, 0.4), (5, 0.5), (6, 0.8), (8, 1.25)):
        t = n * rho
        eig = spectrum(n, rho)
        for k in range(n):
            lam_from_dft = sum(
                cmath.exp(t * (cmath.exp(2j * math.pi * j / n) - 1))
                * cmath.exp(-2j * math.pi * k * j / n)
                for j in range(n)
            )
            assert abs(lam_from_dft - math.exp(eig[k])) < 1e-9
            assertions += 1
    for rho in (0.15, 0.3, 1 / math.e, 0.4, 0.5, 1.0, 2.0, 5.0):
        h, u = rate(rho)
        assert h > 0
        assertions += 1
        if u is not None:
            assert 0 < u < rho < u + 1
            assert abs((rho - u + u * math.log(u / rho)) -
                       (rho - (u+1) + (u+1)*math.log((u+1)/rho))) < 1e-11
            assertions += 2
        for n in (40, 80, 160, 240):
            eig = spectrum(n, rho)
            low = min(range(n), key=lambda k: eig[k])
            if u is None:
                assert low == n - 1
                assertions += 1
            p = prefactor(n, rho, u)
            predicted = n * h + math.log(p)
            discrepancy = max(eig) - min(eig) - predicted
            # The theorem gives O_rho(1/n), not a universal coefficient.
            assert abs(discrepancy) < 0.18, (rho, n, discrepancy)
            assertions += 1
    print(f'PASS: {assertions} assertions; tested exact Fourier spectrum and fixed-rho asymptotics.')


if __name__ == '__main__':
    run()
