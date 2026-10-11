#!/usr/bin/env python3
"""Finite exact-integer consistency checks for quartic parabola sampling."""
from itertools import product
from math import gcd, isqrt


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def divisor_threshold(d):
    assert d >= 1
    return min(a + d // a for a in range(1, isqrt(d) + 1) if d % a == 0)


def fourth_moment_integer_resonance(k, n, a):
    total = 0j
    for i, j, u, v in product(range(k + 1), repeat=4):
        if i + j == u + v and (i * i + j * j - u * u - v * v) % n == 0:
            total += a[i] * a[j] * a[u].conjugate() * a[v].conjugate()
    assert total.imag == 0
    return int(total.real)


def continuous_moment(a):
    squares = [int(z.real * z.real + z.imag * z.imag) for z in a]
    return 2 * sum(squares) ** 2 - sum(s * s for s in squares)


def signed_defect(k, n, a):
    total = 0
    for h in range(1, k + 1):
        for r in range(1, k - h + 1):
            if (2 * h * r) % n == 0:
                for m in range(k - h - r + 1):
                    z = a[m + h + r] * a[m + r].conjugate() * a[m + h].conjugate() * a[m]
                    assert z.real.is_integer()
                    total += 4 * int(z.real)
    return total


def main():
    cases = 0
    for k in range(0, 12):
        for n in range(1, 38):
            d = n // gcd(n, 2)
            no_alias = k < divisor_threshold(d)
            collision = any(2 * h * r % n == 0 for h in range(1, k + 1)
                            for r in range(1, k - h + 1))
            assert no_alias == (not collision), (k, n, 'threshold')
            for offsets in (0, 1):
                a = [complex(1 + (7 * j + 2 * k + n + offsets) % 5,
                             (3 * j + k + 2 * n + offsets) % 7 - 3)
                     for j in range(k + 1)]
                actual = fourth_moment_integer_resonance(k, n, a)
                formula = continuous_moment(a) + signed_defect(k, n, a)
                assert actual == formula, (k, n, actual, formula)
                cases += 1
            if collision:
                ones = [1 + 0j] * (k + 1)
                assert signed_defect(k, n, ones) > 0
    for k in range(2, 140):
        prime = next(p for p in range(max(k, 3), 300) if p % 2 == 1 and is_prime(p))
        minimum = next(n for n in range(1, prime + 1)
                       if k < divisor_threshold(n // gcd(n, 2)))
        assert minimum == prime, (k, minimum, prime)
    assert fourth_moment_integer_resonance(2, 2, [1 + 0j, 0 + 1j, 1 + 0j]) == 11
    assert continuous_moment([1 + 0j, 0 + 1j, 1 + 0j]) == 15
    print('VERIFY_OK integer_moments=%s cutoff_cases=444 prime_minima_K=2..139 signed_negative=PASS' % cases)


if __name__ == '__main__':
    main()
