#!/usr/bin/env python3
"""Exact checks for the spin-2 equatorial Fourier-sampling classification.

Only standard-library arithmetic is used.  The Wigner-small-d sum is
independent of the associated-Legendre/eth expression checked against it.
Finite tests corroborate, but do not establish, the all-degree theorem.
"""
from fractions import Fraction
from math import factorial


def odd_double_factorial(n):
    """General double factorial, with (-1)!! = 0!! = 1."""
    assert n >= -1
    ans = 1
    for j in range(n, 0, -2):
        ans *= j
    return ans


def wigner_d_squared(ell, m, n=-2):
    """Exact |d^ell_{m,n}(pi/2)|^2 from the finite Wigner factorial sum."""
    root_sq = (factorial(ell+m) * factorial(ell-m) *
               factorial(ell+n) * factorial(ell-n))
    summation = Fraction(0)
    for s in range(2*ell+1):
        args = (ell+n-s, s, m-n+s, ell-m-s)
        if min(args) < 0:
            continue
        denom = 1
        for j in args:
            denom *= factorial(j)
        summation += Fraction((-1)**(m-n+s), denom)
    return root_sq * summation * summation / 4**ell


def eth_prediction(ell, m):
    """Exact |d^ell_{m,-2}(pi/2)|^2 via two eth differentiations."""
    q = abs(m)
    factor = Fraction(factorial(ell-2) * factorial(ell-q),
                      factorial(ell+2) * factorial(ell+q))
    if (ell + q) % 2 == 0:
        legendre_zero = Fraction(odd_double_factorial(ell+q-1),
                                 odd_double_factorial(ell-q))
        return factor * (2*m*m-ell*(ell+1))**2 * legendre_zero**2
    legendre_derivative = Fraction(odd_double_factorial(ell+q),
                                   odd_double_factorial(ell-q-1))
    return factor * 4*m*m * legendre_derivative**2


def blind_orders(ell):
    return [m for m in range(-ell, ell+1)
            if (m == 0 and ell % 2 == 1) or (2*m*m == ell*(ell+1))]


def run():
    count = 0
    for ell in range(2, 61):
        acc = Fraction(0)
        zero_direct = []
        for m in range(-ell, ell+1):
            from_sum = wigner_d_squared(ell, m)
            from_eth = eth_prediction(ell, m)
            assert from_sum == from_eth, (ell, m, from_sum, from_eth)
            if from_sum == 0:
                zero_direct.append(m)
            acc += from_sum
            count += 1
        assert acc == 1, (ell, acc)  # Orthogonality of Wigner d column.
        assert zero_direct == blind_orders(ell), (ell, zero_direct)
        for m in zero_direct:
            if m:
                assert (ell + abs(m)) % 2 == 0
    pell = []
    x, y = 3, 2
    for k in range(1, 9):
        ell = (x-1)//2
        m = y//2
        assert 2*m*m == ell*(ell+1)
        assert (ell+m) % 2 == 0
        pell.append((ell,m))
        x, y = 3*x+4*y, 2*x+3*y
    print('PASS exact Wigner versus eth comparison:',count,'individual modes, degrees 2..60')
    print('PASS Wigner unitarity:',59,'individual degrees')
    print('PASS nullity, Pell parity, sample progression:',pell)
    print('FINITE VERIFICATION ONLY; unrestricted assertion is proved symbolically.')


if __name__ == '__main__':
    run()
