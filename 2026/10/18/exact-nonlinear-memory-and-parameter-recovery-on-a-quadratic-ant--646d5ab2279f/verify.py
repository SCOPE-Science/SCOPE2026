"""Auxiliary arithmetic/finite-sample sanity checks for the published equations.

The analytic proof, not the sampled trajectories, establishes the theorem.
No external packages required. Run: python3 verify.py
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def theory(d, r):
    a = d / (1 + d)
    b = r / (1 + d)
    return {
        'm2': 1,
        'm4': 1 + r*r / (1 + 2*d),
        'b1': b,
        'b2': a*b,
        'v': r*r / (1 + 2*d),
        'square_cov1': a * r*r / (1 + 2*d),
    }


def check_exact():
    passes = 0
    for d in (F(1, 5), F(1, 2), F(1), F(2), F(5)):
        for r in (F(-3, 4), F(-1, 3), F(0), F(1, 3), F(3, 4)):
            if r*r >= 4*d:
                continue
            a, b = d/(1+d), r/(1+d)
            t = theory(d, r)
            assert t['v'] == b*b/(1-a*a)
            assert t['m4']-t['m2']**2 == t['v']
            assert t['square_cov1'] == a*t['v']
            assert t['b2'] == a*t['b1']
            assert 1-a == 1/(1+d)
            assert 4*d-r*r > 0
            if r:
                assert a == t['b2']/t['b1']
                assert d == a/(1-a)
                assert r == t['b1']/(1-a)
            passes += 9 if r else 6
    return passes


def trajectory(d, r, n, seed):
    rng = Random(seed)
    x = 0.0
    result = []
    for i in range(n+3000):
        rad = (1+d*x*x+r*x)/(1+d)
        assert rad > 0
        x = (1 if rng.getrandbits(1) else -1)*sqrt(rad)
        if i >= 3000:
            result.append(x)
    return result


def check_samples():
    checks = 0
    for k, (d, r) in enumerate(((0.5, 0.3), (1.0, 0.7), (2.0,-0.6), (4.0,0.0))):
        x = trajectory(d, r, 240000, 89731+k)
        N = len(x)
        m2 = sum(z*z for z in x)/N
        m4 = sum(z**4 for z in x)/N
        b1 = sum(x[i]**2*x[i-1] for i in range(1,N))/(N-1)
        b2 = sum(x[i]**2*x[i-2] for i in range(2,N))/(N-2)
        c1 = sum((x[i]**2-1)*(x[i-1]**2-1) for i in range(1,N))/(N-1)
        t = theory(d, r)
        for actual, expected, tol in ((m2,t['m2'],0.022),
                                      (m4,t['m4'],0.035),
                                      (b1,t['b1'],0.027),
                                      (b2,t['b2'],0.027),
                                      (c1,t['square_cov1'],0.028)):
            if abs(actual-expected) >= tol:
                raise AssertionError((d,r,actual,expected,tol))
            checks += 1
    return checks

if __name__ == '__main__':
    exact = check_exact()
    sampled = check_samples()
    print(f'PASS: {exact} exact rational identities and {sampled} finite-sample diagnostics')
    print('Finite-sample checks do not establish the infinite-time theorem.')
