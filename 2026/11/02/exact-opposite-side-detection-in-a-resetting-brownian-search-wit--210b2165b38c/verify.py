#!/usr/bin/env python3
"""Reproduce analytic boundary-value and event-driven first-absorption checks.

Only standard-library Python is required. Monte Carlo checks are numerical diagnostics,
not a substitute for the proof of universal statements.
"""
import math
import random


def probability(r, gamma, a, D):
    if not (r > 0 and gamma > 0 and a > 0 and D > 0):
        raise ValueError('strictly positive parameters required')
    k = math.sqrt(r / D)
    h = math.sqrt((r + 2 * gamma) / D)
    t = k / h
    return 0.25 * (1.0 - t + t * t / (1.0 + t) * math.exp(-a * h))


def components(r, gamma, a, D, x):
    k = math.sqrt(r / D)
    h = math.sqrt((r + 2 * gamma) / D)
    c = r / (r + 2 * gamma)
    um = -h * math.exp(-h * a) / (4 * (h + k))
    up = 0.25 * (1 - k / h + k*k / (h*(h+k)) * math.exp(-h*a))
    if x >= 0:
        q = up
        q1, q2 = 0.0, 0.0
        m = c * um - (h-k)/(4*h) * math.exp(-h*x)
        m1 = (h-k)/4 * math.exp(-h*x)
        m2 = -(h-k)*h/4 * math.exp(-h*x)
    else:
        q = up + 0.5 * math.exp(k*x)
        q1 = 0.5*k*math.exp(k*x)
        q2 = 0.5*k*k*math.exp(k*x)
        m = c * um + (h+k)/(4*h) * math.exp(h*x)
        m1 = (h+k)/4 * math.exp(h*x)
        m2 = (h+k)*h/4 * math.exp(h*x)
    return (q+m, q-m), (q1+m1, q1-m1), (q2+m2, q2-m2)


def event_simulation(N, r, gamma, a, D, seed):
    rng = random.Random(seed)
    count = 0
    for _ in range(N):
        x = a
        gate_active = rng.random() < 0.5
        for _step in range(1000000):
            t = -math.log1p(-rng.random())/(r+gamma)
            y = x + math.sqrt(2*D*t)*rng.gauss(0,1)
            if gate_active:
                if x*y <= 0 or rng.random() < math.exp(-x*y/(D*t)):
                    count += (x < 0)
                    break
            if rng.random() < r/(r+gamma):
                x = a
            else:
                x = y
                gate_active = not gate_active
        else:
            raise AssertionError('unreasonably long path')
    return count/N


def main():
    checks = 0
    rng = random.Random(20261031)
    for _ in range(300):
        r = math.exp(rng.uniform(-3,3))
        gamma = math.exp(rng.uniform(-3,3))
        a = math.exp(rng.uniform(-1.5,1))
        D = math.exp(rng.uniform(-1,1))
        k = math.sqrt(r/D)
        h = math.sqrt((r+2*gamma)/D)
        at_reset, _, _ = components(r,gamma,a,D,a)
        assert abs(0.5*(at_reset[0]+at_reset[1])-probability(r,gamma,a,D)) < 2e-13
        checks += 1
        for x in (-a, -0.12*a, 0.13*a, a, 2*a):
            values, derivs, seconds = components(r,gamma,a,D,x)
            for j in range(2):
                laplace = D*seconds[j] + gamma*(values[1-j]-values[j]) + r*(at_reset[j]-values[j])
                assert abs(laplace) < 8e-11*(1+abs(values[j]))
                checks += 1
        eps = 1e-12
        (a0, i0), _, _ = components(r,gamma,a,D,eps)
        (a1, i1), _, _ = components(r,gamma,a,D,-eps)
        assert abs(a0) < 2e-9
        assert abs(a1-1) < 2e-9
        assert abs(i0-i1) < 2e-9
        _, dp, _ = components(r,gamma,a,D,eps)
        _, dm, _ = components(r,gamma,a,D,-eps)
        assert abs(dp[1]-dm[1]) < 2e-9
        checks += 4
        assert 0 < probability(r,gamma,a,D) < .25
        checks += 1
        assert probability(1.001*r,gamma,a,D)<probability(r,gamma,a,D)
        assert probability(r,1.001*gamma,a,D)>probability(r,gamma,a,D)
        checks += 2
    # Exact-bridge event simulation conditions on switching/resetting times.
    # Unlike Euler time stepping, it samples zero-crossing events of a Brownian bridge.
    for n,(r,gamma,a,D,seed) in enumerate([(1,0.1,1,1,13),(1,1,1,1,17),(1,10,1,1,23),(2,0.7,0.5,1.3,29)]):
        N = 18000
        obs = event_simulation(N,r,gamma,a,D,seed)
        pred = probability(r,gamma,a,D)
        se = math.sqrt(pred*(1-pred)/N)
        assert abs(obs-pred) < 6*se+0.003,(n,obs,pred,se)
        print('bridge_Monte_Carlo',n,'observed',round(obs,7),'analytic',round(pred,7),'standard_error',round(se,7))
        checks += 1
    assert probability(1,1e8,1,1) > .2499
    assert probability(1e8,1,1,1) < 1e-7
    checks += 2
    print('PASS',checks,'analytic-boundary/residual/ordering and fixed-seed Monte Carlo diagnostics')


if __name__ == '__main__':
    main()
