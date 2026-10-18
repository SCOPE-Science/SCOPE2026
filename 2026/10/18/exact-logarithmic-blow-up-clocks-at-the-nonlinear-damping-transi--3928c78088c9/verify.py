"""Standalone finite consistency checks for the exact Lienard crossing laws.

Only the Python standard library is required. These numerical checks do not
replace the analytic arguments for all integer degrees and all parameters.
"""
from math import exp, isclose, log, pi, sin, sqrt


def parameters(n, eta):
    assert n >= 2 and n % 2 == 0
    delta = 4 * (n + 1) - eta * eta
    assert 0 < eta and delta > 0
    q = exp(-pi * eta / sqrt(delta))
    alpha = n / (n + 1)
    period = 2 * pi * alpha * eta / sqrt(delta)
    return delta, q, period


def rhs(n, eta, x, v):
    return v, -(x ** (2*n+1) + eta * x**n * v)


def half_crossing(n, eta, step=0.0002):
    x, v, t = 0.0, 1.0, 0.0
    nsteps = int(120.0 / step)
    for _ in range(nsteps):
        kx1, kv1 = rhs(n, eta, x, v)
        kx2, kv2 = rhs(n, eta, x + step*kx1/2, v + step*kv1/2)
        kx3, kv3 = rhs(n, eta, x + step*kx2/2, v + step*kv2/2)
        kx4, kv4 = rhs(n, eta, x + step*kx3, v + step*kv3)
        x2 = x + step*(kx1+2*kx2+2*kx3+kx4)/6
        v2 = v + step*(kv1+2*kv2+2*kv3+kv4)/6
        if x > 0 and x2 <= 0:
            frac = x / (x - x2)
            return t + step*frac, abs(v + frac*(v2-v))
        x, v, t = x2, v2, t+step
    raise AssertionError('Crossing absent in the finite test window')


def quadrature_time(n, eta, slices=6000):
    delta, _, _ = parameters(n, eta)
    alpha = n / (n+1)
    # Exact endpoint desingularization w=(2*(pi/2-theta)/pi)^(1/(n+1)).
    # Positive and negative angular halves are integrated together.
    h = 1.0 / slices
    total = 0.0
    beta = alpha*eta*pi/sqrt(delta)
    for j in range(slices):
        w = (j+0.5)*h
        u = w**(n+1)
        factor = (pi/2)*(n+1)*w**n/sin((pi/2)*u)**alpha
        total += factor * (exp(beta*u/2)+exp(beta*(1-u/2)))
    constant = (2/sqrt(delta)) * (sqrt(delta)/(2*(n+1)))**alpha
    return constant * h * total


def run():
    samples = [(2,.5),(2,1.0),(2,2.0),(4,.5),(4,1.0)]
    count = 0
    for n, eta in samples:
        delta,q,period=parameters(n,eta)
        t,v = half_crossing(n, eta)
        assert abs(v-q) < 2e-5, (n, eta, v, q)
        count += 1
        # Smooth desingularized midpoint quadrature.
        assert abs(quadrature_time(n,eta)-t) < 2e-4, (n,eta,t)
        count += 1
        assert isclose(period, -2*n*log(q)/(n+1), rel_tol=1e-12)
        count += 1
    _,q,period=parameters(2,1)
    assert abs(period-1.262967766799167) < 5e-12
    count+=1
    assert abs(exp(-period/2)-0.5318020829448200)<5e-12
    count+=1
    assert abs(exp(period)-3.535899656899745)<5e-12
    count+=1
    print('PASS:',count,'finite checks; original analytic proof is separate.')


if __name__ == '__main__':
    run()
