#!/usr/bin/env python3
"""Exact proof checks and independent finite-state calculations for a four-spin heat current."""
from itertools import product
from sympy import Matrix, Rational, cancel, factor, symbols


a, b = symbols('a b', real=True)
STATES = list(product((-1, 1), repeat=4))
INDEX = {x: k for k, x in enumerate(STATES)}


def stats(x):
    u = sum(x[i] * x[(i + 1) % 4] for i in range(4))
    v = x[0] * x[2]
    w = x[1] * x[3]
    p = x[0] * x[1] * x[2] * x[3]
    return u, v, w, p


def transitions(x, aa=a, bb=b):
    for i in range(4):
        gamma = aa if i % 2 == 0 else bb
        q = Rational(x[i] * (x[(i - 1) % 4] + x[(i + 1) % 4]), 2) if i % 2 == 0 else Rational(0)
        neighbor = Rational(x[i] * (x[(i - 1) % 4] + x[(i + 1) % 4]), 2)
        rate = 1 - gamma * neighbor
        y = list(x)
        y[i] *= -1
        yield tuple(y), rate, q


def gen(phi, x):
    return sum(rate * (phi(y) - phi(x)) for y, rate, _ in transitions(x))


def iszero(expr):
    assert cancel(expr) == 0, factor(expr)


def algebraic_checks():
    mu = (b - a) / 2
    h0 = lambda x: (stats(x)[0] + b * stats(x)[1] - a * stats(x)[2]) / 8
    for x in STATES:
        u, v, w, p = stats(x)
        f = sum(rate * q for _, rate, q in transitions(x))
        shot = sum(rate * q ** 2 for _, rate, q in transitions(x))
        l1h = sum(rate * q * h0(y) for y, rate, q in transitions(x))
        iszero(gen(lambda y: stats(y)[0], x) - (-4*u + 4*a*(1+w) + 4*b*(1+v)))
        iszero(gen(lambda y: stats(y)[1], x) - (a*u-4*v))
        iszero(gen(lambda y: stats(y)[2], x) - (b*u-4*w))
        iszero(gen(lambda y: stats(y)[3], x) - (-8*p+(a+b)*u))
        iszero(f - (u/2-a*(1+w)))
        iszero(shot - (1+w-a*u/2))
        iszero(gen(h0, x) - (mu-f))
        expression = (a*a+2)/4 - (5*a+b)*u/8 + (a*b+2)*v/4 + (a*a+2)*w/4 + (a*b+2)*p/4
        iszero(shot+2*l1h-expression)
    eu=2*(a+b)/(2-a*b)
    ev=a*eu/4
    ew=b*eu/4
    ep=(a+b)*eu/8
    e_h=eu/8
    e_g=(a*a+2)/4 - (5*a+b)*eu/8 + (a*b+2)*ev/4 + (a*a+2)*ew/4 + (a*b+2)*ep/4
    iszero(eu/2-a*(1+ew)-mu)
    iszero(e_g - 2*mu*e_h - (8-a*a-6*a*b-b*b)/16)
    avg=(a+b)/2
    iszero((8-a*a-6*a*b-b*b)/16-((1-avg**2)/2+mu**2/4))
    print('Exact symbolic generator, Poisson, moment, and noise identities: PASS (16 states).')


def numerical_matrix_check(aa, bb):
    dim=16
    q0=Matrix.zeros(dim,dim)
    q1=Matrix.zeros(dim,dim)
    q2=Matrix.zeros(dim,dim)
    for x in STATES:
        col=INDEX[x]
        for y,rate,increment in transitions(x,aa,bb):
            row=INDEX[y]
            q0[row,col]+=rate
            q0[col,col]-=rate
            q1[row,col]+=rate*increment
            q2[row,col]+=rate*increment**2
    row=dim-1
    mat=q0.copy()
    for j in range(dim):
        mat[row,j]=1
    rhs=Matrix([0]*(dim-1)+[1])
    pi=mat.inv()*rhs
    assert all(x>0 for x in pi)
    one=Matrix([[1]*dim])
    current=cancel((one*q1*pi)[0])
    iszero(current-(bb-aa)/2)
    r= current*pi - q1*pi
    r[row]=0
    derivative=mat.inv()*r
    noise=cancel((one*(q2*pi+2*q1*derivative))[0])
    iszero(noise-(8-aa*aa-6*aa*bb-bb*bb)/16)
    return current,noise


if __name__ == '__main__':
    algebraic_checks()
    cases=[(0,0),(0,Rational(1,3)),(0,Rational(9,10)),
           (Rational(1,5),Rational(4,5)),
           (Rational(4,5),Rational(1,5)),
           (Rational(1,3),Rational(1,3)),
           (Rational(3,4),Rational(7,8)),
           (Rational(2,3),Rational(1,7))]
    for aa,bb in cases:
        numerical_matrix_check(aa,bb)
    print('Independent exact 16-state stationary and tilted-generator computations: PASS (%d parameter pairs).' % len(cases))
    print('All tests passed.')
