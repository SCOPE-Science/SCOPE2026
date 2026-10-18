#!/usr/bin/env python3
"""Independent numerical checks for the constant-opacity map's re-entrant two-cycle theorem.

Finite floating-point tests are diagnostics, not substitutes for the analytic proof.
Requires Python 3 standard library only.
"""
import math


def bisect(fun, left, right, steps=100):
    fl, fr = fun(left), fun(right)
    assert fl * fr < 0, (left, right, fl, fr)
    for _ in range(steps):
        mid = (left + right) / 2
        fm = fun(mid)
        if fm == 0:
            return mid
        if fl * fm > 0:
            left, fl = mid, fm
        else:
            right, fr = mid, fm
    return (left + right) / 2


def data(gamma, p2):
    assert gamma > 1 and p2 > 0
    a, b = 1 + 1/gamma, 1 - 1/gamma
    c = 2 ** (-0.25)

    def h(x):
        return (a + b*math.exp(-gamma*x)) ** (-0.25)

    def hprime(x):
        u = math.exp(-gamma*x)
        return b*gamma*u/(4*(a + b*u)**1.25)

    def f(x, p1):
        return p1 * math.exp(p2 * (c - h(x)))

    def fp(x, p1):
        return -p2 * f(x, p1) * hprime(x)

    def slope_at_fixed(x):
        return p2*x*hprime(x)

    def phi(t):
        u = math.exp(-t)
        return b*t*u/(4*(a+b*u)**1.25)

    def philogprime(t):
        u = math.exp(-t)
        return 1/t - 1 + 1.25*b*u/(a+b*u)

    tpeak = bisect(philogprime, 1, 8/3)
    critical = 1/phi(tpeak)

    def p1_from_fixed(x):
        return x*math.exp(p2*(h(x)-c))

    def root_for_p1(p1):
        right = max(1.0, p1)
        return bisect(lambda x: f(x,p1)-x, 0, right)

    return locals()


def test():
    count = 0
    for gamma in (1.02, 1.4, 2, 3, 5, 10, 100):
        for p2 in (4, 15, 30, 80):
            d = data(gamma, p2)
            F, FP, tpeak = d['f'], d['fp'], d['tpeak']
            assert 1 < tpeak < 8/3
            for x in (0, 0.001, 0.03, .1, .35, 1, 3, 10):
                # Direct numerical derivative and derivative from exact chain-rule formula.
                if gamma*x>650:
                    continue  # Avoid floating-point underflow at extreme optical depth.
                p1 = 1.3
                hh = 1e-5 / (1 + gamma + p2)
                approx = (F(x + hh, p1) - F(x - hh,p1))/(2*hh)
                assert abs(approx - FP(x,p1)) < 1e-7 * (1 + abs(FP(x,p1)))
                assert FP(x,p1) < 0
                count += 1
            p1 = 1.3
            fixed = d['root_for_p1'](p1)
            assert abs(F(fixed,p1)-fixed) < 1e-12
            assert abs(-FP(fixed,p1)-d['slope_at_fixed'](fixed))<1e-12
            count += 2
    d = data(3, 30)
    assert abs(d['critical'] - 28.34317352186779) < 1e-11
    h, F, FP = d['h'], d['f'], d['fp']
    func = lambda t: 30*d['phi'](t) - 1
    t1 = bisect(func, 1e-8, d['tpeak'])
    t2 = bisect(func, d['tpeak'], 10)
    pminus = d['p1_from_fixed'](t1/3)
    pplus = d['p1_from_fixed'](t2/3)
    assert abs(pminus-1.149552) < 1e-5
    assert abs(pplus-4.045508) < 1e-5
    assert 0 < pminus < pplus
    for p1, expected in ((0.7,False), (1.5,True),(2,True),(3,True),(5,False),(10,False)):
        fixed = d['root_for_p1'](p1)
        cycle = pminus < p1 < pplus
        assert cycle == expected
        assert (abs(FP(fixed,p1))>1) == cycle
        z = 0.01
        for _ in range(700):
            z=F(z,p1)
        if cycle:
            assert abs(z-fixed)>.03
            assert abs(F(F(z,p1),p1)-z)<1e-10
            assert 0 < FP(z,p1)*FP(F(z,p1),p1) < 1
        else:
            assert abs(z-fixed)<1e-9
        count += 5
    print(f'PASS {count} diagnostics; gamma=3,p2=30: critical p2={d["critical"]:.12f}, p1-window=({pminus:.12f},{pplus:.12f})')

if __name__ == '__main__':
    test()
