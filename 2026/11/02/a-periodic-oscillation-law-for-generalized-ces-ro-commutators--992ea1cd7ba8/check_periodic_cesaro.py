#!/usr/bin/env python3
"""Independent arithmetic diagnostics for a periodic Cesaro commutator theorem.

No finite diagnostic is used as a substitute for the analytic statements.
Run: python3 check_periodic_cesaro.py
"""
from fractions import Fraction as F
from math import log, pi
euler_gamma = 0.577215664901532860606512090082


def gap2(a, b):
    return (a - b) ** 2


def direct_energy(d, q, N):
    p = len(d)
    return sum((sum(q ** k * gap2(d[n % p], d[(n - k) % p])
                    for k in range(n + 1)) / F((n + 1) ** 2))
               for n in range(N))


def grouped_energy(d, q, N):
    """Summation by residue k mod p with an exact finite geometric sum."""
    p = len(d)
    ans = F(0)
    for n in range(N):
        inner = F(0)
        for k in range(p):
            cycles = max(0, (n - k) // p + 1)
            if cycles:
                geom = F(cycles) if q == 1 else (1 - q ** (p * cycles)) / (1 - q ** p)
                inner += gap2(d[n % p], d[(n - k) % p]) * q ** k * geom
        ans += inner / F((n + 1) ** 2)
    return ans


def endpoint_energy(d, N):
    p = len(d)
    ans = F(0)
    for n in range(N):
        r = n % p
        a = sum((gap2(d[r], d[(r - k) % p]) for k in range(p)), F(0))
        b = sum((gap2(d[r], d[(r - k) % p]) for k in range(r + 1)), F(0))
        ans += ((n // p) * a + b) / F((n + 1) ** 2)
    return ans


def approx_energy(d, q, N):
    p = len(d)
    dd = [float(x) for x in d]
    total = 0.0
    q_p = q ** p
    for n in range(N):
        rr = n % p
        inner = 0.0
        for k in range(p):
            h = (n - k) // p + 1
            if h > 0:
                inner += (dd[rr] - dd[(rr - k) % p]) ** 2 * (q ** k) * (1.0 - q_p ** h) / (1.0 - q_p)
        total += inner / (n + 1) ** 2
    return total


def main():
    checks = 0
    profiles = [(1, -1), (0, 1, 3), (4, -2, 0, 3), (1, 1, 1), (2, 5, -1, 0, 3)]
    for d in profiles:
        for q in (F(0), F(1, 4), F(1, 2), F(4, 9), F(1)):
            for N in (1, 2, 3, 4, 6, 9, 12, 16, 23):
                v1 = direct_energy(d, q, N)
                v2 = grouped_energy(d, q, N)
                assert v1 == v2, (d, q, N, v1, v2)
                checks += 1
                if q == 1:
                    assert v1 == endpoint_energy(d, N)
                    checks += 1
    # For d=(1,-1), the formula predicts A=2, C=2-pi^2/4.
    finite_constant = 2 - pi * pi / 4
    for q in (0.99, 0.999, 0.9995):
        E = approx_energy((1, -1), q, 350000)
        residual = E - 2 * log(1 / (1 - q))
        assert abs(residual - finite_constant) < (0.08 if q == 0.99 else 0.025), (q, residual)
        checks += 1
    endpoint_constant = 2 * euler_gamma - pi * pi / 4
    for N in (10000, 100000):
        # Exact endpoint row energy for d=(1,-1) has 4 floor((n+1)/2) nonzero entry sum.
        E = sum(4 * ((n + 1) // 2) / ((n + 1) ** 2) for n in range(N))
        assert abs(E - 2 * log(N) - endpoint_constant) < 0.004
        checks += 1
    print(f'PASS: {checks} exact/independent finite checks and asymptotic diagnostics')

if __name__ == '__main__':
    main()
