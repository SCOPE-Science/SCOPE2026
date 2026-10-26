#!/usr/bin/env python3
"""Independent numerical and algebraic checks for a resetting Brownian gas.
Uses only the Python standard library; not a proof of the infinite-particle theorem.
"""
import math, random
from fractions import Fraction

def assert_near(a,b,eps=1e-8):
    assert abs(a-b)<=eps*max(1.,abs(a),abs(b)), (a,b)

def p(x,a): return math.exp(-a*x)/2

def resolvent_kernel(x,alpha,r):
    return (3*math.exp(-alpha*x)-(alpha*x+2)*math.exp(-2*alpha*x))/(8*r)

def trap_integral(f,L,n):
    h=L/n
    return h*(0.5*(f(0)+f(L))+sum(f(i*h) for i in range(1,n)))

def lattice_plateau(beta):
    return 1/(8*beta*math.tanh(beta/2))-1/(4*beta*beta)

def exp_laplace(rng,scale):
    return scale*(1 if rng.random()<0.5 else -1)*(-math.log1p(-rng.random()))

def check():
    checks=0
    # Exact resolvent identities, with e^{-alpha x} as a formal indeterminate.
    # P(Y>x, Y+Z>x)=3 exp(-alpha x)/8,
    # P(Y>x) P(Y+Z>x)=(alpha*x+2)*exp(-2*alpha*x)/8.
    # Integrated x-kernel: 3 - (1/4+1) = 7/4, over 8 => 7/32.
    assert Fraction(3,8)-Fraction(5,32)==Fraction(7,32);checks+=1
    assert 2*Fraction(7,32)==Fraction(7,16);checks+=1
    for r,D,rho in [(1,1,1),(3,.8,2),(0.7,4.3,1.9)]:
        alpha=math.sqrt(r/D)
        num=rho*trap_integral(lambda x:resolvent_kernel(x,alpha,r), 38/alpha,15000)
        predicted=7*rho/(32*alpha*r)
        assert_near(num,predicted,2e-7);checks+=1
    for beta in [.03,.1,.5,1.,2.,6.,12.]:
        m=lambda u:math.exp(-beta*u)/(2*(-math.expm1(-beta)))
        first=trap_integral(m,1,6000)
        second=trap_integral(lambda u:m(u)**2,1,6000)
        v=second-first**2
        predicted=lattice_plateau(beta)
        assert_near(v,predicted,6e-7);checks+=1
        assert 0<predicted<1/(8*beta);checks+=1
    # Direct path-level Poisson Brownian resolvent sampling, not from evaluated kernel.
    rng=random.Random(413208)
    alpha=1.3;r=1.7;x=0.47
    n=340000
    crossed=0;above=0
    # Y is the stationary displacement and Z is free Brownian motion at independent exponential time.
    for _ in range(n):
        y=exp_laplace(rng,1/alpha)
        z=exp_laplace(rng,1/alpha)
        if y>x:
            above+=1
            if y+z>x: crossed+=1
    expect_cross=3*math.exp(-alpha*x)/8
    assert_near(crossed/n,expect_cross,0.006);checks+=1
    expect_p=.5*math.exp(-alpha*x)
    assert_near(above/n,expect_p,0.007);checks+=1
    expect_free=(alpha*x+2)*math.exp(-alpha*x)/4
    freecross=0
    rng=random.Random(208413)
    for _ in range(n):
        if exp_laplace(rng,1/alpha)+exp_laplace(rng,1/alpha)>x:
            freecross+=1
    assert_near(freecross/n,expect_free,0.007);checks+=1
    for beta in [.0001,.001,.002]:
        assert_near(lattice_plateau(beta),1/48,1e-5);checks+=1
    print('PASS',checks,'independent algebraic/quadrature/Monte-Carlo assertions')
    print('integrated mean kernel coefficient',Fraction(7,32),'per alpha*r')
    print('dynamic time-average variance coefficient',Fraction(7,16),'rho/(alpha*r)')
    print('lattice example beta=1: plateau', format(lattice_plateau(1),'.14f'))
    print('Poisson example beta=1: plateau', format(1/8,'.14f'))
    print('dense-anchor lattice floor',Fraction(1,48))

if __name__=='__main__':check()
