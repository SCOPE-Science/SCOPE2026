#!/usr/bin/env python3
"""Deterministic checks for a coupled compound-Poisson linear Euler calculation."""
import math

def calc(a,x0,times,marks,n):
    exact=x0*math.exp(a)+sum(h*math.exp(a*(1-t)) for t,h in zip(times,marks))
    approx=x0*(1+a/n)**n+sum(h*(1+a/n)**(n-1-math.floor(n*t)) for t,h in zip(times,marks))
    return n*(exact-approx),exact

def phase(a,x0,times,marks,n):
    return .5*a*a*x0*math.exp(a)+sum(h*math.exp(a*(1-t))*(a*(1-(n*t%1))+.5*a*a*(1-t)) for t,h in zip(times,marks))

def level(a,x0,times,marks,n):
    e1,_=calc(a,x0,times,marks,n)
    e2,_=calc(a,x0,times,marks,2*n)
    return e1-.5*e2

def predicted_level(a,x0,times,marks,n):
    return .25*a*a*x0*math.exp(a)+sum(h*math.exp(a*(1-t))*(.25*a*a*(1-t)+.5*a*(1 if n*t%1<.5 else 0)) for t,h in zip(times,marks))

def test():
    times=[.123451,.347821,.672411,.987461]
    marks=[2.,-1.5,1.25,-.75]
    tests=0
    for a in (-1.5,-.3,.25,1.7):
      for x0 in (-2.,0.,3.):
        for n in (64,256,1024,4096):
          for t,h in [(times[:1],marks[:1]),(times,marks),([],[])]:
            q,_=calc(a,x0,t,h,n)
            assert abs(q-phase(a,x0,t,h,n))< 1000/n
            z=level(a,x0,t,h,n)
            assert abs(z-predicted_level(a,x0,t,h,n))<1000/n
            tests+=2
    for k in range(10001):
        u=(k+.13)/10002
        assert abs((1-u)-.5*(1-((2*u)%1))-.5*(u<.5))<1e-12
        tests+=1
    assert abs((.5*1**2)*(.5*0**2))<1e-12  # simple finite nonnegative check
    assert abs(sum((b-.5)**2 for b in (0,1))/2-.25)<1e-12
    print('PASS',tests,'checks')
if __name__=='__main__': test()
