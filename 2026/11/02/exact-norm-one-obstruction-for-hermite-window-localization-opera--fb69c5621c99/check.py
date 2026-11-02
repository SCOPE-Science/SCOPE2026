#!/usr/bin/env python3
"""Finite exact-arithmetic supplementary checks for the Laguerre Gaussian identity.

The universal theorem is established by the proof, not by these finite tests.
No network or third-party packages are required.
"""
from fractions import Fraction as Q
from math import comb, factorial


def laguerre(n, x):
    return sum((Q((-1) ** j * comb(n, j), factorial(j)) * x ** j
                for j in range(n + 1)), Q(0))


def product(p, q):
    out = {}
    for (i, j), c in p.items():
        for (u, v), d in q.items():
            key = (i + u, j + v)
            out[key] = out.get(key, Q(0)) + c * d
    return {key: value for key, value in out.items() if value}


def power(p, n):
    out = {(0, 0): Q(1)}
    for _ in range(n):
        out = product(out, p)
    return out


def polynomial_laguerre(n, xpoly):
    out = {}
    for j in range(n + 1):
        factor = Q((-1) ** j * comb(n, j), factorial(j))
        for key, value in power(xpoly, j).items():
            out[key] = out.get(key, Q(0)) + factor * value
    return {key: value for key, value in out.items() if value}


def gaussian_moment_with_holomorphic_tilt(p, a):
    """Exact Gaussian integral of exp(a*w) times a polynomial in w and wbar.

    The measure is pi^{-1} exp(-|w|^2) dA; monomial moments are q! if p=q.
    """
    ans = Q(0)
    for (i, j), c in p.items():
        if j >= i:
            ans += c * Q(factorial(j), factorial(j-i)) * a ** (j-i)
    return ans


def integral_laguerre_pair(n, m, a):
    absw2 = {(1, 1): Q(1)}
    shifted = {(1, 1): Q(1), (1, 0): -a, (0, 1): -a, (0, 0): a*a}
    p = product(polynomial_laguerre(n, absw2), polynomial_laguerre(m, shifted))
    return gaussian_moment_with_holomorphic_tilt(p, a)


def test():
    assert laguerre(1, Q(1)) == 0
    count = 0
    for a in [Q(0), Q(1, 2), Q(1), Q(3, 2)]:
        for n in range(8):
            for m in range(8):
                answer = laguerre(n, a*a) if n == m else Q(0)
                observed = integral_laguerre_pair(n, m, a)
                assert observed == answer, (n, m, a, observed, answer)
                count += 1
    print('PASS: %s exact polynomial Gaussian identities' % count)
    print('PASS: L_1(1)=0, so the first nonanalytic level has a forbidden unit-frequency circle')
    print('FINITE CHECKS ONLY: existence and norm separation are proved analytically.')

if __name__ == '__main__':
    test()
