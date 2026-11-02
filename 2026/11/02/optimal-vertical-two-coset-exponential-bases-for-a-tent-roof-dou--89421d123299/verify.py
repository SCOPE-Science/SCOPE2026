"""Finite consistency checks for the analytic two-coset double-tile result.

Run: python3 verify.py. Standard library only. These checks do not prove the continuum theorem.
"""
import math


def rho(t):
    return max(abs(math.cos(math.pi * a * t / 4)) for a in (1, 2, 3))


def bounds(t):
    r = rho(t)
    return ((1-r)/2, (1+r)/2)


def displacement(x, s):
    low = .25 + min(x, 1-x)
    for a in (1, 2, 3):
        y = s + a/4
        if low < y < low + .25:
            return a
    raise AssertionError('boundary sample or incorrect double tile')


def test():
    for x, s, a in ((.125, .2, 1), (.125, .05, 2), (.375, .05, 3)):
        assert displacement(x, s) == a
    for t in (1.0, 1.125, 1.3333333, 1.5, 2.17, 2.6666667, 3.0):
        for a in (1, 2, 3):
            phi = math.pi * a * t / 2
            gram_trace = 4.0
            # The Gram determinant is 4-|1+exp(i phi)|^2.
            modulus_sq = (1+math.cos(phi))**2 + math.sin(phi)**2
            low, high = 2-math.sqrt(modulus_sq), 2+math.sqrt(modulus_sq)
            assert abs(low+high-gram_trace) < 1e-12
            assert abs(low-(2-2*abs(math.cos(phi/2)))) < 1e-12
    optimum = 1 / math.sqrt(2)
    for k in range(4001):
        t = 4*k/4000
        assert rho(t) >= optimum - 1e-12
    for t in (1., 3.):
        assert abs(rho(t)-optimum) < 1e-12
        A, B = bounds(t)
        assert abs(B/A-(3+2*math.sqrt(2))) < 1e-10
    for t0, a in ((0.,1), (4/3,3), (2.,2), (8/3,3)):
        assert bounds(t0)[0] < 1e-12
        h = 1.e-4
        asymptotic = (math.pi**2)*(a**2)/64
        for sign in (-1,1):
            quotient = bounds(t0+sign*h)[0] / (h*h)
            assert abs(quotient-asymptotic) < 1e-6
    print('CHECK_OK: double-tile fibers, matrix Gram eigenvalues, minimax offsets, four resonances, three quadratic rates')

if __name__ == '__main__':
    test()
