#!/usr/bin/env python3
"""Finite numerical corroboration of cyclic Gaussian CAZAC phase-Hessian theorem.

Run: python3 verify.py. Uses only the Python standard library; does not certify all N.
"""
import cmath
import math
import random

TAU = 2.0 * math.pi


def chirp(n, a):
    eps = n % 2
    return [cmath.exp(1j * math.pi * a * j * (j + eps) / n) for j in range(n)]


def delta(n):
    return sum(1 for k in range(n) if (k * k) % n == 0)


def acf(n, u):
    return [sum(u[(j + s) % n] * u[j].conjugate() for j in range(n)) for s in range(1, n)]


def cost(n, u):
    return sum(abs(z) ** 2 for z in acf(n, u))


def transform(n, h):
    rt = math.sqrt(n)
    return [sum(h[j] * cmath.exp(-1j * TAU * k * j / n)
                for j in range(n)) / rt for k in range(n)]


def predicted_quadratic(n, a, h):
    ft = transform(n, h)
    return 4.0 * n * sum(math.sin(math.pi * a * s * s / n) ** 2
                         * abs(ft[(-a * s) % n]) ** 2 for s in range(1, n))


def run():
    rng = random.Random(314159)
    checked = 0
    max_zero = 0.0
    max_quad_relerr = 0.0
    tested_squareful = 0
    for n in range(2, 27):
        d = delta(n)
        predicted_d = 1
        z = n
        p = 2
        while p * p <= z:
            exponent = 0
            while z % p == 0:
                z //= p
                exponent += 1
            predicted_d *= p ** (exponent // 2)
            p += 1
        assert d == predicted_d, (n, d, predicted_d)
        for a in range(1, n):
            if math.gcd(a, n) != 1:
                continue
            u = chirp(n, a)
            zero = max((abs(z) for z in acf(n, u)), default=0.0)
            max_zero = max(max_zero, zero)
            assert zero < 1e-8, (n, a, zero)
            # Verify the full free d-periodic phase family, not just its tangent.
            phase = [rng.uniform(-1.8, 1.8) for _ in range(d)]
            w = [u[j] * cmath.exp(1j * phase[j % d]) for j in range(n)]
            zero2 = max((abs(z) for z in acf(n, w)), default=0.0)
            max_zero = max(max_zero, zero2)
            assert zero2 < 1e-8, (n, a, d, zero2)
            if d > 1:
                tested_squareful += 1
            h = [rng.uniform(-1, 1) for _ in range(n)]
            # Analytic derivative of autocorrelation as real linear map.
            grad = []
            for s in range(1, n):
                grad.append(1j * sum(u[(j+s) % n] * u[j].conjugate()
                                      * (h[(j+s) % n] - h[j]) for j in range(n)))
            q_direct = sum(abs(t) ** 2 for t in grad)
            q_formula = predicted_quadratic(n, a, h)
            relerr = abs(q_direct - q_formula) / max(1, q_direct, q_formula)
            max_quad_relerr = max(max_quad_relerr, relerr)
            assert relerr < 2e-11, (n, a, q_direct, q_formula)
            # Verify derivative in a genuinely transverse direction.
            t = 2e-5
            p = [u[j] * cmath.exp(1j * t * h[j]) for j in range(n)]
            m = [u[j] * cmath.exp(-1j * t * h[j]) for j in range(n)]
            fd = (cost(n,p)+cost(n,m)) / (2 * t * t)
            assert abs(fd-q_formula)/max(1, q_formula) < 4e-6, (n, a, fd, q_formula)
            # Check the kernel Fourier support criterion directly on real vectors.
            ker = [rng.uniform(-1,1) for _ in range(d)]
            hh = [ker[j % d] for j in range(n)]
            assert abs(predicted_quadratic(n,a,hh)) < 1e-20 + 5e-23*n, (n,a,d)
            checked += 1
    print(f'VERIFY_OK n=2..26 units_checked={checked} squareful_cases={tested_squareful} '
          f'max_abs_autocorrelation={max_zero:.3g} max_quadratic_relerr={max_quad_relerr:.3g}')


if __name__ == '__main__':
    run()
