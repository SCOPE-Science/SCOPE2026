#!/usr/bin/env python3
"""Finite diagnostics for the piecewise-affine phase Wiener-growth formula.

Standard-library only. These tests do not prove an asymptotic theorem.
"""
import math
import cmath

TAU=2*math.pi

def intervals_for_plateau(t):
    return [(0.0,t,-1.0,0.0),(t,TAU-t,0.0,-t),(TAU-t,TAU,1.0,-TAU)]

def hat_exact(n,k,intervals):
    ans=0j
    for a,b,s,c in intervals:
        q=n*s-k
        integ=(b-a) if q==0 else (cmath.exp(1j*q*b)-cmath.exp(1j*q*a))/(1j*q)
        ans+=cmath.exp(1j*n*c)*integ/TAU
    return ans

def phase_plateau(x,t):
    if x<=t:return -x
    if x<=TAU-t:return -t
    return x-TAU

def hat_midpoint(n,k,t,N=24000):
    # Split at phase breakpoints; midpoint quadrature is independent of (4).
    pts=[0.0,t,TAU-t,TAU]
    total=0j
    for a,b in zip(pts[:-1],pts[1:]):
        dx=(b-a)/N
        for j in range(N):
            x=a+(j+0.5)*dx
            total+=cmath.exp(1j*(n*phase_plateau(x,t)-k*x))*dx/TAU
    return total

def mu_rational(q):
    return 1.0/q*sum(abs(math.sin(math.pi*j/q)) for j in range(1,q))

def predicted(t):
    # Only valid for the indicated rational sample t.
    if abs(t-math.pi/2)<1e-12:return (2+math.sqrt(2))/math.pi
    if abs(t-2*math.pi/3)<1e-12:return 2*math.sqrt(3)/math.pi
    raise ValueError('Rational sample required')

def trunc_norm(n,t,cutoff_multiple=20):
    ints=intervals_for_plateau(t)
    return sum(abs(hat_exact(n,k,ints)) for k in range(-cutoff_multiple*n,cutoff_multiple*n+1))

def main():
    assert abs(mu_rational(2)-0.5)<1e-13
    assert abs(mu_rational(3)-math.sqrt(3)/3)<1e-13
    assert abs(mu_rational(4)-(1+math.sqrt(2))/4)<1e-13
    for t in [math.pi/2,2*math.pi/3,math.pi/math.sqrt(2)]:
        ints=intervals_for_plateau(t)
        for n,k in [(2,0),(3,-4),(4,5)]:
            err=abs(hat_midpoint(n,k,t)-hat_exact(n,k,ints))
            assert err<2e-7,(t,n,k,err)
        print('sample t=',format(t,'.12f'))
        for n in [80,320,1280]:
            v=trunc_norm(n,t)
            print('  n=',n,'truncated Wiener norm=',round(v,8))
        if t!=math.pi/math.sqrt(2):
            print('  predicted asymptotic coefficient=',format(predicted(t),'.12f'))
        else:
            print('  predicted asymptotic coefficient=',format(12/math.pi**2,'.12f'))
    print('finite diagnostics passed')
if __name__=='__main__':main()
