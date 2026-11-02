#!/usr/bin/env python3
"""Finite reproducibility tests for a two-channel stochastic switch theorem.

No third-party dependencies. Analytic proofs, not these tests, establish the
all-parameter task classification and the global optimum.
"""
from math import cosh, exp, log, tanh, isclose
from random import Random

count = 0

def check(condition, context):
    global count
    assert condition, context
    count += 1


def root(H, c):
    low, high = 0.0, 1.0
    for _ in range(110):
        mid = (low + high) / 2
        if mid + (1 + H) * mid ** c > H:
            high = mid
        else:
            low = mid
    return (low + high) / 2


def q_from_rates(k, f, theta, x, T, rho):
    forward = k * (exp(theta + f * x / 2) + exp(-theta - f * x / 2))
    reverse = k * (exp(theta - f * x / 2) + exp(-theta + f * x / 2))
    decay = forward + reverse
    return forward / decay + (rho - forward / decay) * exp(-decay * T)


def q_closed(k, f, theta, x, T, rho):
    rate = 4 * k * cosh(theta) * cosh(f / 2)
    return 0.5 + (rho - 0.5) * exp(-rate * T) + 0.5 * x * tanh(theta) * tanh(f / 2) * (1 - exp(-rate * T))


def envelope(k, b, f, T, rho):
    a = 4 * k * T * cosh(f / 2)
    c = cosh(b)
    H = tanh(b) * tanh(f / 2)
    d = abs(rho - 0.5)
    C = d * exp(-a)
    B = H * (1 - exp(-c * a)) / 2 - d * exp(-c * a)
    return C, B


def truth_tasks(k, b, f, T, rho, gamma, resolution=501):
    possible = {'copy': False, 'invert': False, 'plus': False, 'minus': False}
    for j in range(resolution):
        theta = -b + (2 * b * j) / (resolution - 1)
        up = q_from_rates(k, f, theta, +1, T, rho) - 0.5
        down = q_from_rates(k, f, theta, -1, T, rho) - 0.5
        possible['copy'] |= up >= gamma - 1e-12 and down <= -gamma + 1e-12
        possible['invert'] |= up <= -gamma + 1e-12 and down >= gamma - 1e-12
        possible['plus'] |= up >= gamma - 1e-12 and down >= gamma - 1e-12
        possible['minus'] |= up <= -gamma + 1e-12 and down <= -gamma + 1e-12
    return possible

rng = Random(72431)
for _ in range(4500):
    k = rng.uniform(0.05, 3)
    f = rng.uniform(0.02, 4)
    b = rng.uniform(0.03, 2)
    theta = rng.uniform(-b, b)
    T = rng.uniform(0.0001, 4)
    rho = rng.random()
    x = rng.choice((-1, 1))
    p = q_from_rates(k, f, theta, x, T, rho)
    t = q_closed(k, f, theta, x, T, rho)
    check(abs(p - t) < 1e-12, ('population', k, b, f, theta, T, rho, x, p, t))
    check(-1e-12 <= p <= 1+1e-12, ('normalization', p))

for k, b, f in ((1, 1, 1), (0.5, .2, 3), (2, 1.5, .3), (1, 1.5, 2), (.3, .6, .1)):
    c, H = cosh(b), tanh(b) * tanh(f / 2)
    z = root(H, c)
    Tstar = -log(z) / (4*k*cosh(f/2))
    gstar = z / 2
    check(0 < z < 1, ('root range', z))
    check(abs(z + (1+H)*z**c-H) < 1e-13, ('root equation', z))
    C, B = envelope(k, b, f, Tstar, 1)
    check(abs(C - gstar) < 1e-12 and abs(B-gstar) < 1e-12, ('optimal balance', k,b,f,C,B,gstar))
    for scale in (.05,.2,.5,1,1.4,2.0,4.0):
        for rho in [i/100 for i in range(101)]:
            Ct, Bt = envelope(k,b,f,Tstar*scale,rho)
            check(min(Ct,Bt) <= gstar+1e-12, ('global margin',k,b,f,scale,rho))
    for scale in (.2,1,2):
        T = Tstar*scale
        for rho in (0,.2,.5,.8,1):
            C,B = envelope(k,b,f,T,rho)
            for gamma in (.001,.015,.08,.16,.31):
                actual = truth_tasks(k,b,f,T,rho,gamma,301)
                expected = {'copy':B>=gamma,'invert':B>=gamma,
                            'plus':rho>0.5 and C>=gamma,
                            'minus':rho<0.5 and C>=gamma}
                check(actual == expected, ('task count',k,b,f,T,rho,gamma,actual,expected))

# Asymptotic ratios tend to 1 as the signal strength H decreases.
for b, H in ((.6, 1e-12), (1.0, 1e-5), (1.8, 1e-3)):
    c = cosh(b)
    z = root(H,c)
    check(abs((H-z)/H**c-1) < 0.02, ('weak driving',b,H,z))
    check(abs((log(1/z)-log(1/H))/H**(c-1)-1) < 0.02,
          ('weak-drive time',b,H,z))

print('PASS:',count,'finite assertions; theorem relies on analytic proof')
