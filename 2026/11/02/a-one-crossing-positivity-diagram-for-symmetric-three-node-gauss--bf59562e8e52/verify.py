"""Standalone numerical verification for symmetric three-node Gaussian kernel quadrature.

The symbolic/inequality proof in RESULT.md establishes the theorem for all
parameters; these finite high-precision checks independently test formulas,
limits, signs, and sample values, not infinitely many cases.
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 75


def moments(a, t):
    e = mp.sqrt(t)
    c = mp.sqrt(mp.pi) * mp.erf(e) / e
    b = mp.sqrt(mp.pi) * (mp.erf(e*(1+a)) + mp.erf(e*(1-a))) / (2*e)
    return b, c


def weights_formula(a, t):
    q = mp.exp(-t*a*a)
    b, c = moments(a, t)
    u = (b-q*c)/(1-q*q)**2
    v = (c*(1+q**4)-2*q*b)/(1-q*q)**2
    return u, v, u


def weights_direct(a, t):
    nodes = [-a, mp.mpf(0), a]
    K = mp.matrix([[mp.exp(-t*(xi-xj)**2) for xj in nodes] for xi in nodes])
    b, c = moments(a, t)
    return tuple(mp.lu_solve(K, mp.matrix([b, c, b])))


def central_integral(a, t):
    f = lambda x: mp.exp(-t*x*x)*(mp.cosh(2*t*a*a)-mp.cosh(2*t*a*x))
    q = mp.exp(-t*a*a)
    return 4*q*q/(1-q*q)**2*mp.quad(f, [0, a, 1])


def crossing_for_half():
    a = mp.mpf('0.5')
    return mp.findroot(lambda e: weights_formula(a, e*e)[1], (mp.mpf('1.05'), mp.mpf('1.12')))


def run():
    checks = 0
    for a_txt in ['0.20', '0.25', '0.50', '0.56', '0.5773502691896257645', '0.58', '0.80', '1.0']:
        a = mp.mpf(a_txt)
        for t_txt in ['0.0001', '0.01', '0.2', '1', '3', '10', '40', '100']:
            t = mp.mpf(t_txt)
            exact = weights_direct(a, t)
            formula = weights_formula(a, t)
            for v, w in zip(exact, formula):
                assert mp.almosteq(v, w, rel_eps=mp.mpf('1e-45'), abs_eps=mp.mpf('1e-40'))
                checks += 1
            assert formula[0] > 0
            checks += 1
            if t >= mp.mpf('0.01'):
                integ = central_integral(a, t)
                assert mp.almosteq(integ, formula[1], rel_eps=mp.mpf('1e-35'), abs_eps=mp.mpf('1e-35'))
                checks += 1
            if a >= mp.mpf('0.58'):
                assert formula[1] > 0
                checks += 1

    crit = 1/mp.sqrt(3)
    for t_txt in ['0.00001','0.0001','0.01','0.1','1','10','100']:
        assert weights_formula(crit, mp.mpf(t_txt))[1] > 0
        checks += 1

    for a_txt in ['0.25','0.40','0.50','0.55','0.575']:
        a = mp.mpf(a_txt)
        assert weights_formula(a, mp.mpf('0.00001'))[1] < 0
        assert weights_formula(a, mp.mpf('1000'))[1] > 0
        checks += 2

    for a_txt in ['0.25','0.50','0.75']:
        a = mp.mpf(a_txt)
        t = mp.mpf('0.0000001')
        u, v, _ = weights_formula(a, t)
        assert abs(u-1/(3*a*a)) < mp.mpf('1e-5')
        assert abs(v-(2-2/(3*a*a))) < mp.mpf('1e-5')
        checks += 2

    for a_txt in ['0.25','0.5','0.75']:
        a = mp.mpf(a_txt)
        for xfactor in ['0.15','0.60','0.95']:
            x = a*mp.mpf(xfactor)
            for yfactor in ['0.05','0.5','0.95']:
                y = a+(1-a)*mp.mpf(yfactor)
                def ratio(t):
                    p = mp.exp(-t*x*x)*(mp.cosh(2*t*a*a)-mp.cosh(2*t*a*x))
                    n = mp.exp(-t*y*y)*(mp.cosh(2*t*a*y)-mp.cosh(2*t*a*a))
                    return p/n
                assert ratio(mp.mpf('0.1')) < ratio(mp.mpf('0.3')) < ratio(mp.mpf('1')) < ratio(mp.mpf('4'))
                checks += 1

    eps = crossing_for_half()
    assert abs(eps-mp.mpf('1.0786096032571438128686939826218155')) < mp.mpf('1e-34')
    assert weights_formula(mp.mpf('.5'), (eps-mp.mpf('.001'))**2)[1] < 0
    assert weights_formula(mp.mpf('.5'), (eps+mp.mpf('.001'))**2)[1] > 0
    checks += 3
    print('PASS', checks, 'checks; a=1/2 epsilon_* =', mp.nstr(eps, 48))


if __name__ == '__main__':
    run()
