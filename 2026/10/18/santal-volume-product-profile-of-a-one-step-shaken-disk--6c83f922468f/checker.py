"""Independent numerical spot checks for the two-semiellipse Santaló profile.

Requires mpmath>=1.3. Numerical testing supplements the analytic proof; it
cannot certify assertions for every interpolation parameter.
"""
import mpmath as mp

mp.mp.dps = 42


def J_closed(a, c):
    a, c = mp.mpf(a), mp.mpf(c)
    if a == 0:
        assert c < 0
        return -2/c
    assert c < a
    if abs(a+c) < mp.mpf('1e-32'):
        return 4/(3*a)
    if c > -a:
        G = 2*mp.acos(-c/a)/mp.sqrt(a*a-c*c)
    else:
        G = 4*mp.atanh(mp.sqrt((-a-c)/(a-c)))/mp.sqrt(c*c-a*a)
    return (a*a*G+2*c)/(a*a-c*c)


def J_integral(a, c):
    a, c = mp.mpf(a), mp.mpf(c)
    return 2*mp.quad(lambda x: (mp.sqrt(x*x+a*a)-c)**(-2), [0, 1, mp.inf])


def polar_area(delta, center, method=J_closed):
    return (method(1+delta, center) + method(1-delta, -center))/2


def optimum(delta, guess):
    delta = mp.mpf(delta)
    deriv = lambda c: mp.diff(lambda z: polar_area(delta, z), c)
    center = mp.findroot(deriv, (mp.mpf(guess)*mp.mpf('0.98'), mp.mpf(guess)*mp.mpf('1.02')))
    assert 0 < center < 1+delta
    assert abs(deriv(center)) < mp.mpf('1e-27')
    return center, mp.pi*polar_area(delta, center)


if __name__ == '__main__':
    cases = [('0.001', '0.00085'), ('0.05', '0.0424'), ('0.25', '0.2117'),
             ('0.5', '0.420'), ('0.75', '0.619'), ('1', '0.7833')]
    last = mp.pi**2
    for d, initial in cases:
        d = mp.mpf(d)
        center, value = optimum(d, initial)
        for a, c in [(1+d, center), (1-d, -center)]:
            j1, j2 = J_closed(a, c), J_integral(a, c)
            assert abs(j1-j2) < mp.mpf('1e-29'), (d, a, c, j1, j2)
        assert value < last
        last = value
        print('delta=', mp.nstr(d, 8), 'Santalo_y=', mp.nstr(center, 16),
              'Mahler=', mp.nstr(value, 16))
    assert abs(last-mp.mpf('8.716345507152885')) < mp.mpf('1e-11')
    d = mp.mpf('0.001')
    center, value = optimum(d, '0.00085')
    assert abs(center/d - 8/(3*mp.pi)) < mp.mpf('1e-5')
    cubic = 32*(88-9*mp.pi**2)/(27*mp.pi**3)
    assert cubic < 0
    assert abs((center-8*d/(3*mp.pi))/d**3-cubic) < mp.mpf('1e-5')
    assert abs((mp.pi**2-value)/d**2 - (mp.mpf(32)/3-mp.pi**2)) < mp.mpf('3e-6')
    assert abs(J_closed(1, -1)-mp.mpf(4)/3) < mp.mpf('1e-39')
    print('All independent quadrature and local-coefficient spot checks passed.')
