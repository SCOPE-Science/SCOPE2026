#!/usr/bin/env python3
"""Reproducible numerical diagnostics for a finite Legendre-tail identity.

Requires mpmath. The proof is mathematical and does not rely on this test.
"""
import mpmath as mp

mp.mp.dps = 65


def partial_kernel(n, r, t):
    if n == 0:
        return mp.mpf(1)
    p0, p1 = mp.mpf(1), t
    power = r
    ans = p0 + 3 * power * p1
    for k in range(2, n + 1):
        p2 = ((2*k - 1)*t*p1 - (k - 1)*p0)/k
        power *= r
        ans += (2*k + 1)*power*p2
        p0, p1 = p1, p2
    return ans


def infinite_kernel(r, t):
    return (1-r*r)/(1-2*r*t+r*r)**mp.mpf('1.5')


def tail_integral(n, r, z):
    theta = z/n
    def integrand(phi):
        q = mp.cos(theta)+1j*mp.sin(theta)*mp.cos(phi)
        return q**(n+1)*((2*n+3)/(1+r*q)-2*r*q/(1+r*q)**2)
    return (-r)**(n+1)*mp.quad(integrand, [0, mp.pi])/mp.pi


def verify():
    # The finite tail identity is checked with two computationally
    # different forms, not inferred from the asymptotic limit.
    for n in (4, 7, 10):
        r = mp.mpf('0.61')
        z = mp.mpf('1.75')
        t = -mp.cos(z/n)
        direct = infinite_kernel(r,t)-partial_kernel(n,r,t)
        tail = tail_integral(n,r,z)
        assert abs(mp.im(tail)) < mp.mpf('1e-52')
        assert abs(direct-mp.re(tail)) < mp.mpf('1e-51')

    # Symbolically certified in RESULT.md via the alternating series.
    assert mp.besselj(0, 4) < -mp.mpf(1)/3
    gamma = mp.log(-2*mp.besselj(0,4))
    assert mp.mpf('-.24') < gamma < mp.mpf('-.22')
    predicted = mp.mpf('0.5')+mp.e*mp.besselj(0,4)
    assert predicted < 0
    for n in (100, 400, 1000, 4000):
        nmp=mp.mpf(n)
        c=mp.mpf(-1)
        radius=1-(2*mp.log(nmp)-mp.log(mp.log(nmp))+c)/nmp
        t=-mp.cos(4/nmp)
        v=partial_kernel(n,radius,t)
        assert v < 0, (n, v)
        observed=nmp*v/mp.log(nmp)
        assert abs(observed-predicted) < mp.mpf('0.2'), (n, observed, predicted)
    print('PASS: finite tail identity, J0 sign, and even-degree boundary-layer diagnostics')


if __name__ == '__main__':
    verify()
