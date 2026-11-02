#!/usr/bin/env python3
"""Deterministic numerical cross-checks of the support-max formulas for tapered homothetic hulls.

The infinite assertions are proved in RESULT.md; finite quadratures are regression tests.
"""
import math


def support(vertices, x, y):
    return max(a*x+b*y for a,b in vertices)


def width_direct(vertices, height, taper, angle, t):
    x=math.sqrt(1-t*t)*math.cos(angle)
    y=math.sqrt(1-t*t)*math.sin(angle)
    p=support(vertices,x,y)
    q=support(vertices,-x,-y)
    plus=max((1+taper)*p+height*t/2,(1-taper)*p-height*t/2)
    minus=max((1+taper)*q-height*t/2,(1-taper)*q+height*t/2)
    return plus+minus


def width_reduced(vertices, height, taper, angle, t):
    a=math.sqrt(1-t*t)
    v=(math.cos(angle),math.sin(angle))
    p=support(vertices,*v)
    q=support(vertices,-v[0],-v[1])
    return a*((1+taper)*p+(1-taper)*q)+height*t+max(2*taper*a*q-height*t,0.0)


def numerical_means(vertices,height,taper,nphi=240,nt=640):
    total=0.0
    base=0.0
    hmean=0.0
    moment2=0.0
    for j in range(nphi):
        angle=2*math.pi*(j+0.5)/nphi
        p=support(vertices,math.cos(angle),math.sin(angle))
        q=support(vertices,-math.cos(angle),-math.sin(angle))
        hmean+=p*math.atan(2*taper*p/height)*taper
        moment2+=p*p
        for k in range(nt):
            t=(k+0.5)/nt
            w=width_direct(vertices,height,taper,angle,t)
            r=width_reduced(vertices,height,taper,angle,t)
            assert abs(w-r)<2e-12
            total+=w
            base+=math.sqrt(1-t*t)*(p+q)+height*t
    return ((total-base)/(nphi*nt),hmean/nphi,moment2/nphi)


def check():
    triangle=[(-0.9,-0.5),(1.4,-0.2),(0.15,1.3)]
    square=[(-1.,-1.),(-1.,1.),(1.,1.),(1.,-1.)]
    for base in (triangle,square):
        for s in (0.12,0.45,0.85):
            empirical,analytic,m2=numerical_means(base,1.6,s)
            assert abs(empirical-analytic)<1e-5,(empirical,analytic)
            assert analytic>0
        tiny=0.004
        _,analytic,m2=numerical_means(base,1.6,tiny,120,220)
        assert abs(analytic/tiny**2-2*m2/1.6)<0.0001
    # For centrally symmetric bases, every fixed direction is ordered.
    for j in range(480):
        angle=2*math.pi*(j+.5)/480
        for k in range(100):
            t=(k+.5)/100
            v0=width_direct(square,1.6,0.0,angle,t)
            v1=width_direct(square,1.6,0.3,angle,t)
            v2=width_direct(square,1.6,0.9,angle,t)
            assert v0<=v1+1e-12 and v1<=v2+1e-12
    # For a radius-one disk, the analytical response simplifies exactly.
    for s in (0.1,0.4,0.9):
        expected=s*math.atan(2*s/1.6)
        integral=sum(max(2*s*math.sqrt(1-t*t)-1.6*t,0)
                     for t in [(j+.5)/300000 for j in range(300000)])/300000
        assert abs(integral-expected)<1e-8
    print('DIRECT_SUPPORT_VERSUS_HINGE_FORMULA_PASSED')
    print('ASYMMETRIC_AND_SYMMETRIC_MEAN_RESPONSE_PASSED')
    print('QUADRATIC_TAPER_COEFFICIENT_PASSED')
    print('SYMMETRIC_BASE_POINTWISE_STOCHASTIC_ORDER_PASSED')
    print('DISK_CLOSED_FORM_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    check()
