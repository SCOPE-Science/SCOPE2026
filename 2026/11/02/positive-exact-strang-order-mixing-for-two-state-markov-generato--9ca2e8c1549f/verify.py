#!/usr/bin/env python3
"""Reproduce the binary exact Strang mixture and the three-state trace identity.
Requires only Python 3 standard library.  Scientific computations use fixed inputs.
"""
from fractions import Fraction as F
from math import exp, sinh
from random import Random


def mul(x,y):
    n=len(x); m=len(y[0]); k=len(y)
    return [[sum(x[i][t]*y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def add(x,y):
    return [[x[i][j]+y[i][j] for j in range(len(x[0]))] for i in range(len(x))]


def scale(x,c):
    return [[c*z for z in row] for row in x]


def eye(n,one=1):
    return [[one if i==j else 0*one for j in range(n)] for i in range(n)]


def trace(x):
    return sum(x[i][i] for i in range(len(x)))


def gen(a,b):
    return [[-a,b],[a,-b]]


def exp2(a,b,h):
    s=a+b
    return add(eye(2),scale(gen(a,b),-__import__('math').expm1(-s*h)/s))


def theta(s,t,h):
    x=(s+t)*h/2
    ua=sinh(t*h/2)/sinh(x)
    ub=sinh(s*h/2)/sinh(x)
    return (s/(s+t)-ub)/(1-ua-ub)


def evaluate(a,b,c,d,h):
    EA=exp2(a,b,h/2)
    EB=exp2(c,d,h)
    P=mul(mul(EA,EB),EA)
    FB=exp2(c,d,h/2)
    FA=exp2(a,b,h)
    Q=mul(mul(FB,FA),FB)
    exact=exp2(a+c,b+d,h)
    w=theta(a+b,c+d,h)
    mix=add(scale(P,w),scale(Q,1-w))
    assert 0<w<1, (a,b,c,d,h,w)
    return max(abs(mix[i][j]-exact[i][j]) for i in range(2) for j in range(2)),w


A=[[F(-1),F(1),F(0)],[F(1),F(-1),F(0)],[F(0),F(0),F(0)]]
B=[[F(0),F(0),F(0)],[F(0),F(-1),F(1)],[F(0),F(1),F(-1)]]


def exp_edge(M,z,half):
    # z=e^{-h}, exp(h M/2) if half; exp(h M) otherwise
    u=(1-z if half else 1-z*z)/2
    return add(eye(3,F(1)),scale(M,u))


def test_trace(z):
    P=mul(mul(exp_edge(A,z,True),exp_edge(B,z,False)),exp_edge(A,z,True))
    Q=mul(mul(exp_edge(B,z,True),exp_edge(A,z,False)),exp_edge(B,z,True))
    target=1+z+z**3
    defect=(1-z)**4/4
    assert trace(P)-target==defect
    assert trace(Q)-target==defect
    assert trace(P)==trace(Q)


def run():
    tests=0
    # Interpolation proves the exact polynomial trace identity for every z:
    # both sides have degree <=4 and agree at five distinct rational nodes.
    for z in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
        test_trace(z); tests+=1
    for den in range(2,25):
        for num in range(1,den):
            test_trace(F(num,den)); tests+=1
    rng=Random(341026)
    for i in range(300):
        a,b,c,d=[rng.uniform(0.08,7) for _ in range(4)]
        h=[0.03,0.1,0.5,1.3,3.0][i%5]
        err,w=evaluate(a,b,c,d,h)
        assert err<3e-12,(i,err,w)
        tests+=1
    # Equal relaxation rates but different equilibrium measures:
    for a,b,c,d in [(1,4,2,3),(3,1,1,3),(.3,2.7,2.4,.6)]:
        for h in [.02,.2,.8,2.,4.]:
            err,w=evaluate(a,b,c,d,h)
            assert err<3e-12 and abs(w-.5)<2e-10
            tests+=1
    # The three-state witness has strictly positive trace defect for h>0.
    for h in [.01,.1,1.,2.]:
        z=exp(-h)
        assert (1-z)**4/4>0
        tests+=1
    print('VERIFY_OK',tests,'exact rational trace tests + binary mixture tests')

if __name__=='__main__':
    run()
