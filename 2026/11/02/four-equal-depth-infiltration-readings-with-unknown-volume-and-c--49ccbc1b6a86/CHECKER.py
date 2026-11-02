#!/usr/bin/env python3
"""Numerical replay of the four-level Green--Ampt inverse theorem.

Requires only Python 3 standard library. All tests check the newly asserted
model/inverse; finite tests corroborate but do not replace the proof.
"""
import math
import random


def D(x):
    assert x > 0
    return math.log1p(1.0 / (x * (x + 2.0)))


def R(x):
    return D(x) / D(x + 1.0)


def g(F, a):
    return F - a * math.log1p(F / a)


def forward(K, a, c, epoch, z0, h):
    assert K > 0 and a > 0 and h > 0 and z0 > c
    return [epoch + g(z0 + i * h - c, a) / K for i in range(4)]


def invert(t, z0, h):
    assert len(t) == 4 and h > 0
    tau = [t[i + 1] - t[i] for i in range(3)]
    u, v = tau[1] - tau[0], tau[2] - tau[1]
    if not (u > v > 0):
        raise ValueError('temporal curvature condition fails')
    target = u / v
    # Monotonicity and limits R(x): (0,+infty)->(+infty,1).
    lo, hi = 1e-12, 1e12
    for _ in range(160):
        mid = (lo + hi) / 2.0
        if R(mid) > target:
            lo = mid
        else:
            hi = mid
    x = (lo + hi) / 2.0
    S = u / D(x)
    L = math.log1p(1.0 / x)
    if not tau[0] > S * (1.0 / x - L):
        raise ValueError('positive observed infiltration baseline fails')
    lam = (tau[0] + S * L) / h
    K, a = 1.0 / lam, S / lam
    c = z0 + a - h * x
    if not (K > 0 and a > 0 and z0 - c > 0):
        raise AssertionError('inversion positivity')
    epoch = t[0] - g(z0 - c, a) / K
    return K, a, c, epoch, x


def close(x, y, rel=8e-7, abs_=2e-8):
    if not math.isclose(x, y, rel_tol=rel, abs_tol=abs_):
        raise AssertionError(f'{x} != {y}')


def run():
    # Symbolic logarithmic example: x=1 exactly, K=1, a=1/2,
    # depth offset c=3/2 and observational zero z0=2.
    sample = forward(1.0, 0.5, 1.5, 3.0, 2.0, 1.0)
    dt = [sample[i + 1] - sample[i] for i in range(3)]
    close(dt[0], 1.0 - 0.5 * math.log(2.0))
    close(dt[1], 1.0 - 0.5 * math.log(1.5))
    close(dt[2], 1.0 - 0.5 * math.log(4.0 / 3.0))
    close((dt[1]-dt[0])/(dt[2]-dt[1]), math.log(4.0/3.0)/math.log(9.0/8.0))
    recovered = invert(sample, 2.0, 1.0)
    for got, expected in zip(recovered, (1.0,0.5,1.5,3.0,1.0)):
        close(got, expected)

    rng = random.Random(451045)
    for k in range(800):
        K = rng.uniform(0.3, 3.5)
        a = rng.uniform(0.2, 2.5)
        F0 = rng.uniform(0.3, 3.5)
        h = rng.uniform(0.5, 2.0)
        c = rng.uniform(-1.5, 2.0)
        z0 = c + F0
        epoch = rng.uniform(-4.0, 4.0)
        samples = forward(K, a, c, epoch, z0, h)
        observed = invert(samples, z0, h)
        for got, expected in zip(observed, (K, a, c, epoch, (F0+a)/h)):
            close(got, expected)
        # Verify the candidate's four actual observations, not just parameters.
        for got, expected in zip(forward(*observed[:4], z0, h), samples):
            close(got, expected)

    # Three-level nonidentification: perturb x in an admissible model,
    # reconstruct K,a,c,epoch with identical first three time readings.
    tau = [sample[i + 1]-sample[i] for i in range(2)]
    for x in (0.95, 1.05):
        S = (tau[1]-tau[0])/D(x)
        lam = (tau[0]+S*math.log1p(1/x))
        a = S/lam
        c = 2+a-x
        K = 1/lam
        epoch = sample[0]-g(2-c,a)/K
        assert 2-c > 0
        for got, expected in zip(forward(K,a,c,epoch,2,1)[:3],sample[:3]):
            close(got,expected)
        assert abs(a-0.5)>1e-3

    # Sharp forbidden-shape example: its positive time increments have
    # increasingly large consecutive increments, impossible under the model.
    for impossible in ((1., 2., 4., 7.), (1., 2., 4., 6.), (1., 2., 3., 4.)):
        try:
            invert(impossible, 2.0, 1.0)
        except ValueError:
            pass
        else:
            raise AssertionError('accepted forbidden shape')
    print('PASS: 800 seeded model recoveries, exact-log example,')
    print('      two distinct 3-level witnesses, 3 excluded data shapes')


if __name__ == '__main__':
    run()
