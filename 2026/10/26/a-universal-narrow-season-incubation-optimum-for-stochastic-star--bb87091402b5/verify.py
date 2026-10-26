#!/usr/bin/env python3
"""Independent finite-star epidemic checks, standard-library only.

This checks the one-dimensional conditioning formula against a numerical
integration of the continuous-time Markov forward equations, and samples
optimality signs. Neither finite checks nor numerical quadrature constitute
a proof of the all-parameter theorem.
"""
import math
from math import comb, exp


def simpson(f, x, y, n=800):
    if x == y:
        return 0.0
    assert n % 2 == 0
    h = (y - x) / n
    ans = f(x) + f(y)
    for j in range(1, n):
        ans += (4 if j % 2 else 2) * f(x + j * h)
    return ans * h / 3


def qp(z, k, m, beta, gamma):
    return (m * comb(m - 1, k - 1) * beta
            * exp(-(gamma + beta * (m - k + 1)) * z)
            * (-math.expm1(-beta * z)) ** (k - 1))


def q(z, k, m, beta, gamma):
    return simpson(lambda t: qp(t, k, m, beta, gamma), 0.0, z, 400)


def pulse_tail(sigma, k, m, a, b, beta, gamma):
    w = b - a
    c = q(w, k, m, beta, gamma)
    return sigma * (
        simpson(lambda l: exp(-sigma * l - gamma * (a - l)) * c, 0., a)
        + simpson(lambda l: exp(-sigma * l) * q(b - l, k, m, beta, gamma), a, b, 100))


def rate_balance(sigma, k, m, a, b, beta, gamma):
    c = q(b - a, k, m, beta, gamma)
    A = gamma * c * simpson(
        lambda l: l * exp(-gamma * (a - l) - sigma * l), 0., a)
    B = simpson(lambda l: l * exp(-sigma * l)
                * qp(b - l, k, m, beta, gamma), a, b)
    return B - A


def optimum(k, m, a, b, beta, gamma):
    lo, hi = 0., 100.
    assert rate_balance(lo, k, m, a, b, beta, gamma) > 0
    assert rate_balance(hi, k, m, a, b, beta, gamma) < 0
    for _ in range(55):
        mid = (lo + hi) / 2
        if rate_balance(mid, k, m, a, b, beta, gamma) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def ode_tail(sigma, k, m, a, b, beta, gamma):
    # States: E, I, R, each at cumulative leaf-infection count 0,...,m.
    n = m + 1
    p = [0.] * (3 * n)
    p[0] = 1.

    def deriv(p, contact):
        d = [0.] * len(p)
        for j in range(n):
            E, I, R = j, n + j, 2 * n + j
            d[E] -= sigma * p[E]
            d[I] += sigma * p[E]
            d[I] -= gamma * p[I]
            d[R] += gamma * p[I]
            if j < m:
                flow = contact * (m - j) * p[I]
                d[I] -= flow
                d[I + 1] += flow
        return d

    def advance(start, duration, contact):
        steps = max(2, int(math.ceil(duration / 0.001)))
        dt = duration / steps
        x = start[:]
        for _ in range(steps):
            k1 = deriv(x, contact)
            k2 = deriv([u + dt * v / 2 for u, v in zip(x, k1)], contact)
            k3 = deriv([u + dt * v / 2 for u, v in zip(x, k2)], contact)
            k4 = deriv([u + dt * v for u, v in zip(x, k3)], contact)
            x = [u + dt*(v1 + 2*v2 + 2*v3 + v4)/6
                 for u, v1, v2, v3, v4 in zip(x, k1, k2, k3, k4)]
        return x

    p = advance(p, a, 0.)
    p = advance(p, b - a, beta)
    return sum(p[h*n+j] for h in range(3) for j in range(k, n))


def short_window_limit(a, gamma):
    def fun(sigma):
        return gamma * simpson(lambda u: (a-u)*exp((sigma-gamma)*u), 0., a)-a
    lo, hi = 0., 100.
    assert fun(lo) < 0 < fun(hi)
    for _ in range(55):
        mid = (lo + hi)/2
        if fun(mid) < 0: lo = mid
        else: hi = mid
    return (lo + hi)/2


def check():
    m, a, b, beta, gamma = 4, 1., 1.4, 2., 1.
    ref = [1.994736066197, 2.171050460690, 2.319640945216, 2.427796102801]
    for k in range(1, m + 1):
        s = optimum(k, m, a, b, beta, gamma)
        assert abs(s - ref[k-1]) < 3e-7, (k, s)
        assert rate_balance(.5*s, k, m, a, b, beta, gamma) > 0
        assert rate_balance(1.5*s, k, m, a, b, beta, gamma) < 0
        assert pulse_tail(s, k, m, a, b, beta, gamma) > (
            exp(-gamma*a)*q(b-a, k, m, beta, gamma))
        for test_s in (0.3, 1.0, 2.0, 4.0):
            conditioned = pulse_tail(test_s, k, m, a, b, beta, gamma)
            markov = ode_tail(test_s, k, m, a, b, beta, gamma)
            assert abs(conditioned - markov) < 3e-8, (k, test_s, conditioned, markov)
        print('k=', k, 'unique stationary root=', f'{s:.12f}',
              'tail at root=', f'{pulse_tail(s,k,m,a,b,beta,gamma):.12f}')
    lim = short_window_limit(a,gamma)
    assert abs(lim - 2.79328213290076) < 1e-8
    for width in (0.01, 0.001):
        opts = [optimum(k, m, a, a+width, beta, gamma) for k in range(1, m+1)]
        assert max(abs(x-lim) for x in opts) < 2.2 * width, (width, opts)
    print('common narrow-pulse limit=',f'{lim:.12f}')
    print('CHECK_OK')


if __name__ == '__main__':
    check()
