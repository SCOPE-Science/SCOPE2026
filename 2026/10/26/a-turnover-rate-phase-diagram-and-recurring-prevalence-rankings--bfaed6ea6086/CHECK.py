#!/usr/bin/env python3
"""Reproduce exact-rational spectral identities and illustrative trajectories.

The infinite-time comparison is proved analytically, not by RK4.
"""
from fractions import Fraction as F
from math import sqrt


def exact_checks():
    cases=0
    for p in range(2,10):
        for q in range(1,8):
            tau=F(p,q)
            if tau<=1: continue
            for i in range(1,8):
                omega=F(i,4)
                A=(tau-1)/(1+omega)
                B=tau*(1+omega)/(tau+omega)
                C=omega*(tau-1)/(tau+omega)
                kap0=A/B
                assert A*B+C==tau-1
                assert C/(A*B)==omega/tau
                assert kap0==(tau-1)*(tau+omega)/(tau*(1+omega)**2)
                ye=(tau-1)/(tau+omega)
                ze=(tau+omega)/(tau*(1+omega))
                assert -ye+tau*ye*(1-ye)*ze==0
                assert 1-ze-omega*ye*ze==0
                assert 0<ye<1 and 0<ze<1
                # Direct Jacobian and equality of determinant identities.
                j11=-1+tau*(1-2*ye)*ze
                j12=tau*ye*(1-ye)
                j21=-kap0*omega*ze
                j22=-kap0*(1+omega*ye)
                assert j11==-A and j22==-kap0*B
                assert j11*j22-j12*j21==kap0*(tau-1)
                q2=F(4)*kap0*(tau-1)/(A+kap0*B)**2-1
                assert q2==omega/tau
                for kap in (kap0/8,kap0/2,kap0,2*kap0,8*kap0):
                    S=A+kap*B
                    T=tau-1
                    D=(A-kap*B)**2-4*kap*C
                    X=B*S-2*T
                    assert X*X-B*B*D==4*T*C
                cases+=1
    # Two exact Jacobians for the same endemic equilibrium.
    assert F(1,3)==(F(2)-1)/(F(2)+1)
    assert F(3,4)==(F(2)+1)/(F(2)*(1+1))
    # Focus: J=[[-1/2,4/9],[-9/32,-1/2]].
    assert F(4,9)*F(-9,32)==F(-1,8)
    # Fast node: trace=-83/6; det=10; characteristic discriminant=5449/36.
    trace=F(-1,2)+F(-40,3)
    det=F(1,2)*F(40,3)-F(4,9)*F(-15,2)
    assert trace==F(-83,6) and det==10
    assert trace*trace-4*det==F(5449,36)
    assert 5449<77**2  # slow real eigenvalue is <-1/2.
    print('Exact rational cases:',cases,'; example spectrum: PASS')


def rhs(v,rate):
    y,z=v
    return (y*(-1+2*(1-y)*z),rate*(1-z-y*z))


def rk4(v,h,rate):
    a=rhs(v,rate)
    b=rhs((v[0]+h*a[0]/2,v[1]+h*a[1]/2),rate)
    c=rhs((v[0]+h*b[0]/2,v[1]+h*b[1]/2),rate)
    d=rhs((v[0]+h*c[0],v[1]+h*c[1]),rate)
    return tuple(v[i]+h*(a[i]+2*b[i]+2*c[i]+d[i])/6 for i in range(2))


def illustrative_trajectory_check():
    # Numerical illustrations only; the theorem is analytic for all small epsilon.
    eps=0.01
    va=(1/3+eps,3/4)
    vb=va
    h=0.001
    values={}
    for k in range(1,25001):
        va=rk4(va,h,3/8)
        vb=rk4(vb,h,10)
        if k in (1000,5000,15000,25000):
            values[k*h]=va[0]-vb[0]
    assert values[1]>0 and values[5]<0 and values[15]>0 and values[25]<0
    print('Illustrative signed prevalence differences:',values)

if __name__=='__main__':
    exact_checks()
    illustrative_trajectory_check()
