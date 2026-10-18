"""Independent quadrature check of the degree-one Hardy extremizer.

Uses only Python's standard library. The values are numerical diagnostics,
not substitutes for the asymptotic proof.
"""
from math import cos, log, pi, sqrt

N = 20000
samples = [1.0 - cos(pi * (j + 0.5) / N) for j in range(N)]


def derivative_balance(a, p):
    return sum(s * (1 - 2 * a * s) * abs(1 - 2 * a * s) ** (p - 2)
               for s in samples) / N


def extremizer(p):
    lo, hi = 0.25, 0.5
    for _ in range(58):
        mid = (lo + hi) / 2
        if derivative_balance(mid, p) > 0:
            lo = mid
        else:
            hi = mid
    a = (lo + hi) / 2
    objective = sum(abs(1 - 2 * a * s) ** p for s in samples) / N
    return a, objective


print('p    a_p            root             4*p*(0.5-a_p)-log(4*p)   F_p*sqrt(2*pi*p)')
for p in (2, 4, 6, 10, 20, 50, 100, 200, 400):
    a, f = extremizer(p)
    print(f'{p:<4} {a:.10f}  {1-1/a: .10f}  '
          f'{4*p*(0.5-a)-log(4*p): .10f}  {f*sqrt(2*pi*p): .10f}')
