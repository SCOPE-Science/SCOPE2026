"""Numerical cross-checks for an exact hazard-shape classification.

Requires only the Python standard library (decimal, 3.11+).
The infinite-parameter statement is proved analytically in RESULT.md;
finite tests here check identities, boundaries and illustrative constants.
"""
from decimal import Decimal as D, getcontext

getcontext().prec = 72
ONE = D(1)
TWO = D(2)


def dec(s):
    return D(str(s))


def log_transform(x, alpha, theta, scale):
    v = (-theta * (ONE + x / scale).ln()).exp()
    return -(ONE - v / TWO).ln()


def kappa(alpha, t):
    a = alpha
    return (t.exp() - ONE) * (
        a / (ONE - (-a * t).exp())
        - ONE / (ONE - (-t).exp())
    )


def kappa_edge(alpha):
    return alpha / (ONE - TWO ** (-alpha)) - TWO


def hazard(x, alpha, theta, scale):
    t = log_transform(x, alpha, theta, scale)
    return theta / (scale + x) * alpha * (t.exp() - ONE) / (
        (alpha * t).exp() - ONE
    )


def log_derivative(x, alpha, theta, scale):
    t = log_transform(x, alpha, theta, scale)
    return (theta * kappa(alpha, t) - ONE) / (scale + x)


def central_difference(f, x, step):
    return (f(x + step) - f(x - step)) / (TWO * step)


def test_identity():
    tested = 0
    for a0 in ('0.1', '0.5', '1', '1.00001', '1.5', '2', '3', '10'):
        for t0 in ('0.4', '2', '30'):
            for lam0 in ('1', '1.9', '5'):
                a, theta, scale = dec(a0), dec(t0), dec(lam0)
                for x0 in ('0.0001', '0.01', '0.1', '1', '10'):
                    x = dec(x0)
                    eps = dec('1e-18')
                    exact = log_derivative(x, a, theta, scale)
                    fd = central_difference(
                        lambda y: hazard(y, a, theta, scale).ln(), x, eps
                    )
                    assert abs(exact - fd) < dec('1e-12'), (a, theta, scale, x, exact, fd)
                    tested += 1
    return tested


def test_boundary_and_peak():
    edge = kappa_edge(dec('2'))
    assert abs(edge - TWO / dec('3')) < dec('1e-65')
    assert dec('1.5') * edge == ONE
    a, theta, scale = dec('2'), dec('2'), ONE
    z = (dec('3') + dec('17').sqrt()) / dec('4')
    tstar = z.ln()
    vstar = TWO * (ONE - (-tstar).exp())
    xstar = scale * ((-vstar.ln() / theta).exp() - ONE)
    assert abs(theta * kappa(a, tstar) - ONE) < dec('1e-65')
    assert abs(log_transform(xstar, a, theta, scale) - tstar) < dec('1e-65')
    assert log_derivative(ONE / dec('100'), a, theta, scale) > 0
    assert log_derivative(dec('1'), a, theta, scale) < 0
    assert hazard(xstar, a, theta, scale) > hazard(dec('0'), a, theta, scale)
    assert hazard(xstar, a, theta, scale) > hazard(dec('1'), a, theta, scale)
    for alpha, th in [(dec('0.5'), dec('100')),
                         (dec('1'), dec('100')),
                         (dec('2'), dec('1.5')),
                         (dec('2'), dec('1')),
                         (dec('3'), dec('0.7'))]:
        for x0 in (('0.000001', '0.01', '0.1') if th == dec('100') else ('0.000001', '0.01', '0.1', '1', '10')):
            assert log_derivative(dec(x0), alpha, th, ONE) < 0
    return xstar, hazard(xstar, a, theta, scale)


if __name__ == '__main__':
    count = test_identity()
    xstar, hstar = test_boundary_and_peak()
    print('finite derivative identity tests:', count)
    print('alpha=2, theta=2: x*/lambda=', xstar)
    print('alpha=2, theta=2: hazard maximum (lambda=1)=', hstar)
    print('test status: PASS')
