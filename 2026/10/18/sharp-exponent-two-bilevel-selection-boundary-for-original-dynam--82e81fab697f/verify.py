"""Reproducible algebraic and finite-step checks for a quadratic dynamic-FISTA recurrence."""
from fractions import Fraction
import math
import sympy as sp

def check_symbolic():
    x,z,t,a=sp.symbols('x z t a', real=True)
    y=(z+(t-1)*x)/t
    zp=z-a*t*y
    xp=(1-a)*y
    lhs=sp.expand(z*z+a*(t*t-t)*x*x-zp*zp-a*t*t*xp*xp)
    rhs=a*t*(t-1)*(x-y)**2+a*t*y*y+a*a*t*t*(1-a)*y*y
    assert sp.cancel(lhs-rhs)==0
    assert sp.simplify(t*y - z - (t-1)*x)==0

def run_experiment(gamma,a,n=100000):
    tprev=0.;t=1.
    xprev=1.;x=1.;z=1.
    Eprev=z*z
    max_error=0.
    out=[]
    for k in range(n):
        alpha=0.25/(k+a)**gamma
        y=x+(tprev-1)/t*(x-xprev)
        xn=(1-alpha)*y
        zn=t*xn-(t-1)*x
        en=zn*zn+alpha*t*t*xn*xn
        if k<500: assert en<=Eprev+2e-12,(k,en,Eprev)
        if k<500: assert abs(zn-(z-alpha*t*y)) < 1e-11*(1+abs(z))
        if k<500: 
            rhs=alpha*t*(t-1)*(x-y)**2+alpha*t*y*y+alpha*alpha*t*t*(1-alpha)*y*y
            d=z*z+alpha*(t*t-t)*x*x-en
            assert abs(d-rhs)<1e-10
        if k in (0,1,2,10,100,1000,10000,n-1):out.append((k+1,xn,zn))
        xprev,x=x,xn
        z=zn;Eprev=en
        tprev,t=t,(1+math.sqrt(1+4*t*t))/2
    return out

def check_first_coordinate():
    tprev=0.;t=1.;xprev=1.;x=1.
    for k in range(400):
        b=(tprev-1)/t
        if k>0: assert 0<=b<1
        y=x+b*(x-xprev)
        xn=y/4
        xprev,x=x,xn
        tprev,t=t,(1+math.sqrt(1+4*t*t))/2
    assert abs(x)<1e-40

if __name__=='__main__':
    check_symbolic()
    check_first_coordinate()
    for g,a in [(0.5,2),(1.5,2),(2,2),(2.00001,50000),(2.5,8),(3,2)]:
        out=run_experiment(g,a,30000)
        print(f'gamma={g}, a={a}: x_last={out[-1][1]:.12g}, z_last={out[-1][2]:.12g}')
    print('PASS symbolic identities, direct steps, energy dissipation, and sample trajectories')
