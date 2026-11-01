#!/usr/bin/env python3
"""Finite exact/independent Fourier checks for finite-range convolution first defects.

This program checks finite identities and sampled multiplier maxima only.
It is not a proof of the stated limits or of ideal membership.
"""
from fractions import Fraction
from functools import reduce
from math import cos, sin, pi, gcd, sqrt, exp, isclose


def invariants(weights):
    assert len(weights) >= 2 and all(p > 0 for p in weights.values())
    assert sum(weights.values()) == 1
    keys = sorted(weights)
    span = reduce(gcd, (abs(k - keys[0]) for k in keys[1:]))
    q = span // gcd(span, keys[0])
    mean = sum((k * p for k, p in weights.items()), Fraction())
    variance = sum((p * (k - mean)**2 for k, p in weights.items()), Fraction())
    assert variance > 0
    return span, q, mean, variance


def predicted(weights):
    _, q, mean, variance = invariants(weights)
    if q > 1:
        return 'linear', (2.0 if q % 2 == 0 else 2.0 * cos(pi / (2*q)))
    if mean:
        return 'sqrt', abs(float(mean)) / sqrt(exp(1.0)*float(variance))
    return 'bounded', exp(-1.0)


def phi(weights, t):
    return sum(float(p) * complex(cos(k*t), sin(k*t)) for k, p in weights.items())


def sampled_norm(weights, n, samples=15000):
    maxval = 0.0
    # Whole circle, not a certificate of the continuum maximum.
    for j in range(samples):
        z = phi(weights, 2*pi*j/samples)
        x = n * abs(z)**(n-1) * abs(1-z)
        if x > maxval:
            maxval = x
    return maxval


def run():
    exact = 0
    for support, q_expected, m_expected, v_expected in [
        ({-1: Fraction(1,2),1:Fraction(1,2)}, 2, Fraction(0),Fraction(1)),
        ({0:Fraction(1,2),1:Fraction(1,2)},1,Fraction(1,2),Fraction(1,4)),
        ({-1:Fraction(1,4),0:Fraction(1,2),1:Fraction(1,4)},1,Fraction(0),Fraction(1,2)),
        ({1:Fraction(1,2),4:Fraction(1,2)},3,Fraction(5,2),Fraction(9,4)),
        ({-2:Fraction(2,5),0:Fraction(2,5),4:Fraction(1,5)},1,Fraction(0),Fraction(24,5)),
        ({2:Fraction(1,2),8:Fraction(1,2)},3,Fraction(5),Fraction(9)),
        ({-5:Fraction(1,2),1:Fraction(1,2)},6,Fraction(-2),Fraction(9)),
        ({0:Fraction(1,3),3:Fraction(1,3),6:Fraction(1,3)},1,Fraction(3),Fraction(6)),
        ({-2:Fraction(1,4),1:Fraction(1,2),4:Fraction(1,4)},3,Fraction(1),Fraction(9,2)),
    ]:
        g,q,m,v = invariants(support)
        assert q == q_expected, (support, q, q_expected)
        assert m == m_expected and v == v_expected, (support,m,v,m_expected,v_expected)
        exact += 3
        # Exact Fourier-product identities on basic discrete-support moments.
        assert sum(support.values()) == 1
        exact += 1
        for j in range(g):
            t = 2*pi*j/g
            assert isclose(abs(phi(support,t)), 1.0,abs_tol=1e-12)
            exact += 1
        mode, target=predicted(support)
        n=6400
        value=sampled_norm(support,n)
        normalized=value / (n if mode=='linear' else sqrt(n) if mode=='sqrt' else 1)
        assert abs(normalized-target) < 0.025, (support,mode,normalized,target)
        exact += 1
        print('case',support,'g=',g,'q=',q,'mode=',mode,'n=',n,'sampled_normalized=',round(normalized,8),'target=',round(target,8))
    # Arithmetic parity constants for primitive q, both exact and numerical.
    for q in range(2,32):
        lattice_max=max(abs(1-complex(cos(2*pi*j/q), sin(2*pi*j/q))) for j in range(q))
        closed=2.0 if q%2==0 else 2*cos(pi/(2*q))
        assert isclose(lattice_max,closed,abs_tol=3e-14)
        exact += 1
    print('CHECK_OK:',exact,'exact-arithmetic, root, and sampled-frequency assertions passed')

if __name__ == '__main__':
    run()
