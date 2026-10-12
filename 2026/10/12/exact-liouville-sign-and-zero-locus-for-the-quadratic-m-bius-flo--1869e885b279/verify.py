#!/usr/bin/env python3
"""Independent finite checks for the quadratic floor-transform theorem.

The infinite theorem requires the separate algebraic proof; these tests do
not turn a finite range into an infinite verification.
"""
from math import isqrt


def mu_omega_phi(limit):
    mu = [1] * (limit + 1)
    omega = [0] * (limit + 1)
    phi = list(range(limit + 1))
    mu[0] = 0
    for p in range(2, limit + 1):
        if phi[p] != p:
            continue
        for n in range(p, limit + 1, p):
            phi[n] -= phi[n] // p
            mu[n] *= -1
            v = n
            while v % p == 0:
                v //= p
                omega[n] += 1
        pp = p * p
        for n in range(pp, limit + 1, pp):
            mu[n] = 0
    return mu, omega, phi


def divisorial_star(limit):
    s = [0] + [1] + [-1] * (limit - 1)
    for d in range(2, limit + 1):
        for q in range(2, limit // d + 1):
            s[d * q] -= s[d] * (2 * q - 1)
    return s


def direct_star(limit):
    s = [0] * (limit + 1)
    s[1] = 1
    for n in range(2, limit + 1):
        s[n] = 1 - n - sum(s[d] * (n // d) ** 2 for d in range(2, n))
    return s


def inverse_h(limit, phi):
    divisors = [[] for _ in range(limit + 1)]
    for d in range(2, limit + 1):
        for n in range(d, limit + 1, d):
            divisors[n].append(d)
    h = [0] * (limit + 1)
    h[1] = 1
    for n in range(2, limit + 1):
        h[n] = -sum(2 * phi[d] * h[n // d] for d in divisors[n])
    return h, divisors


def main():
    bound = 100000
    mu, omega, phi = mu_omega_phi(bound)
    star = divisorial_star(bound)
    direct = direct_star(700)
    assert star[1:701] == direct[1:701]

    nonzero = 0
    zero = 0
    for n in range(2, bound + 1):
        a = (n & -n).bit_length() - 1
        odd_omega = omega[n] - a
        predicted_zero = a >= odd_omega + 3
        assert (star[n] == 0) == predicted_zero, (n, star[n])
        if predicted_zero:
            zero += 1
        else:
            nonzero += 1
            assert ((-1) ** omega[n]) * star[n] > 0, (n, star[n])
        assert (star[n] - mu[n]) % 2 == 0
        assert (star[n] == -1) == (omega[n] == 1 and phi[n] == n - 1), (n, star[n])

    mid = 12000
    inv, divisors = inverse_h(mid, phi)
    for n in range(1, mid + 1):
        a = (n & -n).bit_length() - 1
        expected_positive = (a <= omega[n] - a + 1)
        positive = ((-1) ** omega[n]) * inv[n]
        assert positive >= 0, (n, inv[n])
        assert (positive > 0) == expected_positive, (n, positive)
        assert n == 1 or inv[n] % 2 == 0
        if n >= 2:
            via_inv = sum(mu[d] * inv[n // d] for d in divisors[n] if mu[d])
            assert via_inv == star[n], (n, via_inv, star[n])

    print('PASS direct recurrence vs divisor recurrence: 700 integers')
    print('PASS exact Liouville sign, zero-support and prime-fiber tests: 2..100000')
    print('PASS independent totient-convolution inverse and coefficient support: 1..12000')
    print('PASS parity congruence against the Moebius function: 2..100000')
    print('Nonzero cases: %d; zero cases: %d' % (nonzero, zero))
    print('Initial values: ' + ', '.join('%d:%d' % (n, star[n]) for n in range(2, 31)))
    print('Finite checks support, but do not replace, the infinite proof.')


if __name__ == '__main__':
    main()
