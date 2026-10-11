"""Finite numerical diagnostics for the dyadic return-pressure identities.

This program tests numerical consequences only; the infinite theorem is proved analytically.
Requires Python 3.10+ standard library.
"""
import math


def lacunary_sum(epsilon):
    assert epsilon > 0
    total = 0.0
    for j in range(1000):
        x = math.ldexp(epsilon, j)
        if x > 45:
            break
        total += math.exp(-x)
    return total


def scaled_limit(u):
    assert u > 0
    # F(u) = sum_{j>=0} exp(-2^j u) + sum_{j>=1}(exp(-u / 2^j) - 1)
    val = 0.0
    for j in range(80):
        x = math.ldexp(u, j)
        if x > 45:
            break
        val += math.exp(-x)
    for j in range(1, 80):
        x = math.ldexp(u, -j)
        val += math.expm1(-x)
    return val


def bisect_decreasing(f, target, lo, hi, steps=90):
    assert f(lo) > target > f(hi), (f(lo), target, f(hi))
    for _ in range(steps):
        mid = (lo + hi) / 2
        if f(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def u_star(c):
    return bisect_decreasing(scaled_limit, c, 1e-7, 1e5)


def eps_scaled(q, n, c):
    t = -math.log((n+c)/q)
    def func(u):
        eps = math.ldexp(u, -n)
        return lacunary_sum(eps) - math.exp(eps) * q * math.exp(-t)
    return bisect_decreasing(func, 0., 1e-7, 1e4)


def run_checks():
    for u in [0.03,0.1,0.4,1.,1.7,4.,20.]:
        assert abs(scaled_limit(2*u) - (scaled_limit(u)-1)) < 3e-12
    for c in [-1,0,0.5,1,2]:
        u = u_star(c)
        assert abs(scaled_limit(u)-c) < 3e-12
        assert abs(u_star(c+1)-u/2)<3e-11*max(1,u)
        for n in [9,13,17,21]:
            est = eps_scaled(2,n,c)
            assert abs(est-u)<(15/n)*max(1,u), (c,n,est,u)
            print(f'c={c:4.1f} n={n:2d} target={u:.9f} scaled_gap={est:.9f}')
    # Discrete periodic correction: the dependence on q enters only via s=q*exp(-t).
    theta_0 = u_star(0.)
    theta_half = math.sqrt(2.) * u_star(.5)
    assert theta_0 > theta_half + 1.0e-6, (theta_0, theta_half)
    assert abs(theta_0 - 2*u_star(1.)) < 2e-12
    print(f'periodic factor at phases 0,1/2: {theta_0:.12f}, {theta_half:.12f}')
    for q in [2,3,7]:
        for n in [11,16,20]:
            phase = .37
            # Since q exp(-t)=n+phase, this test is q-independent.
            t = -math.log((n+phase)/q)
            assert abs(q*math.exp(-t) - (n+phase)) < 3e-13
            un = eps_scaled(q,n,phase)
            assert abs(un-u_star(phase)) < .002
    # The finite sums converge to F uniformly on each sampled compact range.
    for u in [0.3,1.,1.9,4.]:
        for n in [8,12,18]:
            assert abs((lacunary_sum(math.ldexp(u,-n)) - n)-scaled_limit(u)) < 5*u*math.ldexp(1.,-n)
    print('PASS: discrete-scale identity, unique-root convergence diagnostics, and dyadic-sum limits.')


if __name__ == '__main__':
    run_checks()
