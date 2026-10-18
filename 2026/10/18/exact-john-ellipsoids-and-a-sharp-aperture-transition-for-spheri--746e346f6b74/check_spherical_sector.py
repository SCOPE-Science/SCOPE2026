#!/usr/bin/env python3
"""Reproduce algebraic and numerical checks for John's spherical-sector ellipsoid.
Use python3 with scipy and numpy (numerical comparisons are not proofs).
"""
from fractions import Fraction as F
from math import sin, asin, sqrt, log
import numpy as np
from scipy.optimize import minimize


def analytic(d, s2):
    theta = asin(sqrt(s2)); st = sqrt(s2); ct = sqrt(1-s2)
    if s2 <= 1/d:
        a=1/(d+1); c=d/(d+1)
        b=sqrt((d-1)/(d+1))*st/ct
        mode='tip'
    else:
        a=sqrt(d)/(d+1)*st
        b=sqrt(d/(d+1))*st
        c=sqrt(d)/(d+1)*sqrt(1+d*ct*ct)
        mode='ring'
    return a,b,c,mode


def radius2(a,b,c):
    A=a*a; B=b*b
    # maximize c^2+B+2ca u+(A-B)u^2, -1 <=u<=1
    u=1.0 if B-A <= c*a else c*a/(B-A)
    return c*c+B+2*c*a*u+(A-B)*u*u, u


def check(d,s2):
    a,b,c,mode=analytic(d,s2)
    k2=(1-s2)/s2
    assert abs(c*c-a*a-k2*b*b)<1e-13
    rad,u=radius2(a,b,c)
    assert abs(rad-1)<1e-12
    if mode=='tip':
        assert abs(u-1)<1e-12
        t=1/d
        W=d*d/(d+1); D=d/(d+1)
    else:
        gamma=sqrt(1+(d+1)*k2)
        t=1/gamma; v=gamma/d
        W=d*v/(t+v); D=d*t/(t+v)
        assert abs(t*v-1/d)<1e-12
        assert abs(u-v)<1e-12
    v=1 if mode=='tip' else gamma/d
    assert abs(W+D-d)<1e-10
    assert abs(-W*t+D*v)<1e-10
    assert abs(W*t*t+D*v*v-1)<1e-10
    assert abs((W*(1-t*t)+D*(1-v*v))/(d-1)-1)<1e-10

    def f(x):
        aa,bb,cc=x
        return -(np.log(aa)+(d-1)*np.log(bb))
    def g1(x):
        aa,bb,cc=x; return cc*cc-aa*aa-k2*bb*bb
    def g2(x):
        aa,bb,cc=x; return 1-radius2(aa,bb,cc)[0]
    best=float('inf')
    for q in (.83, .94, 1.0, 1.06):
        x0=np.array([a*q,b*q,c*q]);
        opt=minimize(f,x0,method='SLSQP',bounds=[(1e-7,1)]*3,
                     constraints=[{'type':'ineq','fun':g1},{'type':'ineq','fun':g2}],
                     options={'ftol':1e-13,'maxiter':250})
        if opt.success and g1(opt.x)>-1e-8 and g2(opt.x)>-1e-8:
            best=min(best,opt.fun)
    assert abs(best-f([a,b,c]))<2e-6, (d,s2,best,f([a,b,c]))
    print(f'd={d:2d} sin^2(theta)={s2:.4f} mode={mode:4s} '
          f'(a,b,c)=({a:.12f}, {b:.12f}, {c:.12f}), '
          f'vol/vol(ball)={a*b**(d-1):.12g}; OK')


# Exact rational identities at rational sine-squared parameter values.
def rational_checks(d, s):
    k2=(1-s)/s
    if s<=F(1,d):
        A=F(1,(d+1)**2); C=F(d*d,(d+1)**2)
        B=F(d-1,d+1)*s/(1-s)
        tw=F(1,d)
        W=F(d*d,d+1); D=F(d,d+1); v=F(1)
        assert B-A <= F(d,(d+1)**2)
        assert C+2*F(d,(d+1)**2)+A==1
    else:
        A=d*s/(d+1)**2; B=d*s/(d+1)
        C=d*(1+d*(1-s))/(d+1)**2
        gamma2=((d+1)-d*s)/s
        tw2=A/C; v2=gamma2/(d*d)
        assert tw2*v2==F(1,d*d)
        # Algebraic squared weights; moment follows tv=1/d.
        assert (B-A)==d*A
        assert (F(d+1,d)*(C+d*A))==1
        tw=None
    assert C==A+k2*B
    print('exact rational containment identities: d=',d,'sin²=',s,'OK')

if __name__=='__main__':
    for d,s in [(2,F(1,4)),(2,F(1,2)),(2,F(3,4)),(3,F(1,9)),
                (3,F(1,3)),(3,F(1,2)),(5,F(1,10)),(5,F(1,5)),
                (5,F(1,2)),(9,F(1,3))]:
        rational_checks(d,s)
        check(d,float(s))
    print('All checks passed. John contact moment proof is analytical, not computational.')
