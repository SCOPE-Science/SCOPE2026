"""Numerical consistency checks for a two-species Poisson placement curve.

Run using Python 3.9+; only the standard library is required.
These finite calculations are not substitutes for the analytic proof.
"""
from math import exp, expm1, log
from random import Random


def richness(eps, x):
    return -expm1(-x) - expm1(-eps*x)


def slope(eps, x):
    p, q = exp(-x), exp(-eps*x)
    return x*(p + eps*q)/richness(eps, x)


def numerator(eps, x):
    p, q = exp(-x), exp(-eps*x)
    S = richness(eps, x)
    P = p + eps*q
    Q = p + eps*eps*q
    return S*P - x*(S*Q + P*P)


def alternate_numerator(eps, x):
    p, q = exp(-x), exp(-eps*x)
    y = eps*x
    return (eps*q*(2*(1-y)-q)
            + p*((2-q)*(1-x)-eps*q*(1+(2-eps)*x)) - p*p)


def bisect(f, a, b):
    fa, fb = f(a), f(b)
    assert fa * fb < 0, (a, b, fa, fb)
    for _ in range(160):
        m = (a+b)/2
        if m == a or m == b:
            break
        fm = f(m)
        if fm == 0:
            return m
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b, fb = m, fm
    return (a+b)/2


def main():
    rng = Random(710279)
    for i in range(2000):
        e = exp(rng.uniform(-13, -0.1))
        x = exp(rng.uniform(-5, min(12, -log(e)+4)))
        direct, alt = numerator(e, x), alternate_numerator(e, x)
        assert abs(direct-alt) <= 3e-12*(1+abs(direct)+abs(alt))
        assert 0 < slope(e, x) < 1 + 1e-12

    f = lambda y: 2*(1-y)-exp(-y)
    y0 = bisect(f, 0.0, 1.0)
    eta0 = 1-y0
    assert abs(eta0-0.23196095298653444) < 1e-14
    assert abs(y0-0.7680390470134656) < 1e-14
    print('universal rare-scale coordinate', format(y0, '.15f'))
    print('universal secondary slope', format(eta0, '.15f'))
    for e in (1e-2, 1e-3, 1e-4, 1e-6, 1e-8):
        L = log(1/e)
        cent = L + log(L)
        h = lambda x: numerator(e, x)
        left = bisect(h, cent-1.0, cent+1.0)
        right = bisect(h, (y0-0.1)/e, (y0+0.1)/e)
        assert 0 < left < right
        assert h(left-0.001) < 0 < h(left+0.001)
        assert h(right-0.001/e) > 0 > h(right+0.001/e)
        assert abs(e*right-y0) < 1e-9
        assert abs(slope(e, right)-eta0) < 1e-9
        print('eps={:.0e} x_min={:.12f} z_min={:.12g} x_max={:.12f} z_max={:.12f}'.format(
            e, left, slope(e, left), right, slope(e, right)))
        if e == 1e-3:
            assert abs(left-9.0189658383563) < 1e-10
            assert abs(right-768.0390470134656) < 1e-9
            assert abs(slope(e, left)-0.0099420480482055) < 1e-12
        assert abs(left-cent) < 0.5
        assert abs(slope(e, left)/(e*(cent+1))-1) < 0.08
    print('2000 algebraic checks and five two-extremum scenarios passed')


if __name__ == '__main__':
    main()
