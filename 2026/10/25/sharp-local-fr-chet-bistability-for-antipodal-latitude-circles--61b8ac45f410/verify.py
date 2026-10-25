"""Reproduce numerical diagnostics for antipodal two-latitude-circle Fréchet energies.

Only Python's standard library is needed. Numerical checks complement the analytic proof.
"""
import math

PI = math.pi


def dilog_series(z, terms=3000):
    if not 0 <= z < 1:
        raise ValueError('requires 0 <= z < 1')
    return sum(z ** n / (n * n) for n in range(1, terms + 1))


def energy_integral(h, t, count=16384):
    """Fréchet energy for a direction with axial coordinate t in [-1, 1]."""
    r = math.sqrt(1.0 - h * h)
    s = math.sqrt(max(0., 1. - t * t))
    total = 0.
    for j in range(count):
        phi = (j + .5) * 2. * PI / count
        q = h * t + r * s * math.cos(phi)
        total += math.asin(max(-1., min(1., q))) ** 2
    return PI ** 2 / 4. + total / count


def equator_formula(h):
    return PI ** 2 / 4. + dilog_series(1. - h * h) / 2.


def pole_formula(h):
    return PI ** 2 / 4. + math.asin(h) ** 2


def equator_coefficient(h):
    return 1. + math.log(h)


def pole_coefficient(h):
    return .5 * (1. - h * math.asin(h) / math.sqrt(1. - h * h))


def bisect(fun, a, b):
    fa = fun(a)
    assert fa * fun(b) < 0.
    for _ in range(90):
        m = (a + b) / 2.
        if fun(m) * fa > 0.:
            a = m
        else:
            b = m
    return (a + b) / 2.


def run_checks():
    total = 0
    for h in (.2, .3, .4, .45, .5, .55, .6, .65, .7, .8, .9):
        eq = energy_integral(h, 0.)
        po = energy_integral(h, 1.)
        assert abs(eq - equator_formula(h)) < 2e-10, (h, eq, equator_formula(h))
        assert abs(po - pole_formula(h)) < 2e-11
        total += 2
        # Cartesian latitude t is a local normal coordinate at the equator.
        step = .01
        eq_num = (energy_integral(h, step) - eq) / step ** 2
        assert abs(eq_num - equator_coefficient(h)) < .003, (h, eq_num, equator_coefficient(h))
        total += 1
        # Geodesic angle theta is a normal coordinate at the pole.
        pole_num = (energy_integral(h, math.cos(step)) - po) / step ** 2
        assert abs(pole_num - pole_coefficient(h)) < .003, (h, pole_num, pole_coefficient(h))
        total += 1
    he = math.exp(-1.)
    hp = bisect(lambda x: x * math.asin(x) / math.sqrt(1. - x*x) - 1., .7, .8)
    hc = bisect(lambda x: equator_formula(x) - pole_formula(x), .55, .65)
    assert .3678 < he < .368 and .758 < hp < .7581 and .5924 < hc < .5926
    assert he < hc < hp
    assert equator_coefficient(.5) > 0 and pole_coefficient(.5) > 0
    assert equator_coefficient(.2) < 0 and pole_coefficient(.9) < 0
    total += 4
    print('PASS', total, 'numerical comparisons and transition checks')
    print('equatorial threshold', format(he, '.15f'))
    print('axial threshold', format(hp, '.15f'))
    print('equal-energy crossing', format(hc, '.15f'))


if __name__ == '__main__':
    run_checks()
