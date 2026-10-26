#!/usr/bin/env python3
"""Reproducible tests for the four-node Fourier-collocation Strang map.

Only the Python standard library is used. These tests supplement the analytic proof;
they do not replace its universal quantifiers.
"""
import math
import random
from fractions import Fraction


def root_q():
    lo, hi = 0.5, 0.6
    for _ in range(120):
        m = (lo + hi) / 2
        if m + m*m + m*m*m > 1:
            hi = m
        else:
            lo = m
    return (lo + hi) / 2


def heat_weights(s):
    q = math.exp(-s)
    return ((1+2*q+q**4)/4, (1-q**4)/4, (1-2*q+q**4)/4)


def heat(s, x):
    a, b, c = heat_weights(s)
    w = (a, b, c, b)
    return [sum(w[(i-j)%4]*x[j] for j in range(4)) for i in range(4)]


def reaction(x, rho):
    r = math.exp(-2*rho)
    return x / math.sqrt(r+(1-r)*x*x)


def strang(s, rho, x):
    return heat(s, [reaction(v, rho) for v in heat(s, x)])


def main():
    checks = 0
    # Polynomial/factorization and stochasticity identities are rational.
    for n in range(1, 500):
        q = Fraction(n, 500)
        assert 1-2*q+q**4 == (1-q)*(1-q-q**2-q**3)
        a=(1+2*q+q**4)/4
        b=(1-q**4)/4
        c=(1-2*q+q**4)/4
        assert a+2*b+c==1
        checks+=2

    qstar=root_q()
    theta=-math.log(qstar)
    assert 0.5<qstar<0.6 and abs(qstar+qstar*qstar+qstar**3-1)<1e-15
    for s in [0.01,0.1,theta/2,0.7*theta,0.9*theta,0.99*theta]:
        a,b,c=heat_weights(s)
        assert c<0 and a>qstar>0.5
        y=strang(s,100,[1.,0.,0.,0.])
        assert y[2]<0
        assert abs(y[2]-(1-2*a))<1e-9
        checks+=4
    for s in [0.001,0.2,theta*0.499,theta*0.5,theta*0.7,theta*0.99]:
        rho=0.75
        if s < theta/2 - 1e-10:
            y=strang(s,rho,[1e-5,0.,0.,0.])
            assert y[2]<0
        if s>=theta/2:
            assert heat_weights(2*s)[2]>-1e-13
        checks+=1
    rng=random.Random(2026)
    for s in [theta+1e-5, 0.7, 0.9, 1.2, 5.0]:
        a,b,c=heat_weights(s)
        assert min(a,b,c)>=-1e-13
        for rho in [0,0.1,1,10,100]:
            for _ in range(100):
                x=[rng.random() for _ in range(4)]
                y=strang(s,rho,x)
                assert min(y)>=-1e-12 and max(y)<=1+1e-12
                checks+=1
    for s in [0.05, theta/3, theta/2+0.01, theta, 3.0]:
        x=[1.,0.,0.,0.]
        y=strang(s,0,x)
        z=heat(2*s,x)
        assert max(abs(i-j) for i,j in zip(y,z))<5e-15
        checks+=1
    print('PASS',checks,'checks')
    print('q_star=',format(qstar,'.16g'))
    print('theta=',format(theta,'.16g'))
    print('2theta=',format(2*theta,'.16g'))
    s=0.75*theta
    print('example diffusion_halfstep=',format(s,'.16g'),'reaction_duration=',100)
    print('example output opposite=',strang(s,100,[1.,0.,0.,0.])[2])
    print('heat-only output opposite=',heat(2*s,[1.,0.,0.,0.])[2])

if __name__=='__main__':main()
