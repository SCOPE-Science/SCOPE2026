#!/usr/bin/env python3
"""Numerical checks for the normalized capped Milstein construction (stdlib only)."""
import math

def f(x): return x/(1+x)
def a(x): return x*x/(1+x)**3
def g(x): return x*x/(1+x)
def gp(x): return 1-(1+x)**-2

def integrand(u,x,h,p):
    z=math.sqrt(h)*u
    e=f(x)*z+0.5*a(x)*(min(z*z,1.0)-h)-0.5*f(x)**2*h
    return math.exp(p*e-0.5*u*u)/math.sqrt(2*math.pi)

def quad_moment(x,h,p,steps=16000):
    lo,hi=-15.0,15.0
    step=(hi-lo)/steps
    s=integrand(lo,x,h,p)+integrand(hi,x,h,p)
    for i in range(1,steps):
        s+=(4 if i%2 else 2)*integrand(lo+i*step,x,h,p)
    return s*step/3

def main():
    print('Rational-coefficient identity and Gaussian integral checks')
    for x in [0.05,0.2,2.0,10.0,200.0]:
        assert 0<=a(x)<=4/27+1e-14
        assert abs(x*(f(x)**2+a(x))-g(x)*gp(x))<2e-12*max(1,x)
    print('coefficient identity: PASS')
    for h in [0.05,0.5,4.,8.]:
        x=2.
        m=quad_moment(x,h,1)
        p2=quad_moment(x,h,2)/(m*m)
        assert math.isfinite(m) and m>0 and math.isfinite(p2)
        print('h=%.2f normalizer=%.9g normalized_first_moment=1 normalized_second_moment=%.9g'%(h,m,p2))
    print('uncapped threshold at x=2 for q=2: h>=27/8=3.375 => divergent Gaussian integral')
    for h in [0.08,0.04,0.02]:
        x=2.
        m=quad_moment(x,h,1)
        bound=abs(m-1.)/(h*h)
        print('h=%.3f |M-1|/h^2=%.7g'%(h,bound))
    print('NUMERICAL_CHECKS_OK')

if __name__=='__main__':main()
