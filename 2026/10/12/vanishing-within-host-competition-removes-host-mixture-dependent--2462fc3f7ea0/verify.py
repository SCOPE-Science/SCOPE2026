#!/usr/bin/env python3
"""Finite numerical checks for a virulence-selection theorem.

The theorem itself is proved analytically in RESULT.md. All quantities here are
computed with Python's standard library (RK4 and trapezoid integration).
"""
import math
from fractions import Fraction

M=1.0
R=4.0
K=1.0
LAMBDA=1.0
STEPS=6000
H=(1/M)/STEPS


def g(x):
    return x-(10.0+x*x)/20.0


def J(z,t):
    return -math.expm1(z*t)/(-z) if abs(z)>1.e-12 else t


def simulate(x,eps):
    def deriv(y):
        return (x/(1.+LAMBDA*eps*y)-(10.+x*x)/20.)*y
    def fatal(y):
        return x*y/(1.+LAMBDA*eps*y)
    v=1.
    vs=[v]
    pref=[0.]
    pf=[0.]
    for j in range(STEPS):
        a=H*deriv(v)
        b=H*deriv(v+a/2)
        c=H*deriv(v+b/2)
        d=H*deriv(v+c)
        nxt=v+(a+2*b+2*c+d)/6
        assert nxt>0
        pref.append(pref[-1]+H*(v+nxt)/2)
        pf.append(pf[-1]+H*(fatal(v)+fatal(nxt))/2)
        v=nxt
        vs.append(v)
    def interp(a,t):
        j=min(int(t/H),STEPS-1)
        z=t/H-j
        return a[j]*(1-z)+a[j+1]*z
    lo=0.; hi=1/M
    for _ in range(75):
        t=(lo+hi)/2
        if M*t+eps*interp(pf,t)<1:
            lo=t
        else:
            hi=t
    T=(lo+hi)/2
    q=1/T-M
    assert abs(M*T+eps*interp(pf,T)-1)<2e-11
    return interp(pref,1/(M+R)),interp(pref,T),q,T


def potential(x,eps,p):
    a,b,q,t=simulate(x,eps)
    return K*((1-p)*a+p*b),q


def optimize(eps,p):
    lo=8.; hi=12.
    gr=(math.sqrt(5)-1)/2
    a=hi-(hi-lo)*gr
    b=lo+(hi-lo)*gr
    fa=potential(a,eps,p)[0]
    fb=potential(b,eps,p)[0]
    for _ in range(58):
        if fa<fb:
            lo=a; a=b; fa=fb; b=lo+(hi-lo)*gr; fb=potential(b,eps,p)[0]
        else:
            hi=b; b=a; fb=fa; a=hi-(hi-lo)*gr; fa=potential(a,eps,p)[0]
    x=(lo+hi)/2
    return x,*potential(x,eps,p)


def main():
    for x in map(Fraction,['1','2','10','15','20']):
        left=x-Fraction(10+x*x,20)
        right=Fraction(9,2)-(x-10)**2/Fraction(20)
        assert left==right
    for eps in (0.01,0.001,0.0001):
        for x in (0.5,2,6,10,14,20,30):
            a,b,q,t=simulate(x,eps)
            assert 0<t<1/M and q>=0
            assert a<=J(g(x),1/(M+R))+1e-9
            assert b<=J(g(x),1/M)+1e-9
    for eps in (0.0001,0.00001):
        for p in (0,0.5,1):
            x,k,q=optimize(eps,p)
            assert 9.5<x<10.5
            assert k<=K*((1-p)*J(g(10),1/(M+R))+p*J(g(10),1/M))+5e-8
            print(f'eps={eps:g} p={p:g} x_opt={x:.8f} mortality={q:.8g}')
    target=10*M*J(g(10),1/M)
    q1=simulate(10,1e-6)[2]
    assert abs(q1/1e-6/target-1)<0.0025,(q1, target)
    print('asymptotic_mortality_coefficient=',f'{target:.9f}')
    print('VERIFY_OK')

if __name__=='__main__': main()
