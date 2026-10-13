#!/usr/bin/env python3
"""Exact arithmetic checks of the three-point log-determinant identities.

These tests accompany, but do not replace, the analytic parameter-uniform proof.
Requires only Python 3 standard library.
"""
from fractions import Fraction as F
from itertools import product


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def coeff(a, gamma):
    b = gamma*(1-a)-1
    k = gamma*a
    return b, k, b*(b+2*k), b*b*(b+3*k)


def polynomial(a, gamma, x):
    b,k,B,H = coeff(a, gamma)
    e2 = x[0]*x[1]+x[0]*x[2]+x[1]*x[2]
    e3 = x[0]*x[1]*x[2]
    return 1+(b+k)*sum(x)+B*e2+H*e3


def matrix(a, gamma, x):
    b,k,_,_ = coeff(a, gamma)
    return [[int(i==j)*(1+b*x[i])+k*x[j]
             for j in range(3)] for i in range(3)]


def dmax(a, gamma):
    return ((1+2*gamma*(1-a))**2
            *(1+2*gamma*(1+2*a))/27)


n = 0
as_ = [F(1,20), F(1,5), F(1,3), F(2,3), F(9,10)]
for a in as_:
    glo, gmid, ghi = 1/(1+2*a), 1/(1+a), 1/(1-a)
    gammas = [glo/2, glo, (glo+gmid)/2, gmid,
              (gmid+ghi)/2, ghi, ghi+F(1,2)]
    for gamma in gammas:
        b,k,B,H = coeff(a,gamma)
        for u in [F(0),F(1,4),F(1,2),F(2,3),F(3,4),F(1)]:
            for v in [F(0),F(1,4),F(1,2),F(2,3),F(3,4),F(1)]:
                w=2-u-v
                if 0<=w<=1:
                    x=(u,v,w)
                    assert det3(matrix(a,gamma,x))==polynomial(a,gamma,x)
                    assert polynomial(a,gamma,x)>0
                    n+=1
        assert polynomial(a,gamma,(F(2,3),)*3)==dmax(a,gamma)
        if glo<=gamma<=gmid:
            assert B>=0 and H>=0
            assert dmax(a,gamma)>0
        if gmid<gamma<ghi:
            assert B<0
            # Explicit relative-interior point with positive curvature.
            delta=min(F(1,4), -B/(2*H)) if H>0 else F(1,4)
            assert 0<delta<F(1)
            x=(delta,1-delta/2,1-delta/2)
            assert B+H*delta<0
            assert polynomial(a,gamma,x)>0
            # Along v with u fixed, D_v=0 and D_vv=-2(B+H*u).
            assert -2*(B+H*delta)>0
        if gamma==ghi:
            assert b==0 and B==0 and H==0
            assert polynomial(a,gamma,(F(2,3),)*3)==polynomial(a,gamma,(0,1,1))

    # The log of the exact symmetric optimum is decreasing on the low interval.
    # Its derivative is -2 P / [g*(1+2g*(1-a))*(1+2g*(1+2a))].
    def P(g):
        return 1+(1+2*a)*g-2*(1-a)*(1+2*a)*g*g
    assert P(0)==1
    assert P(gmid)==a*(7*a+3)/(a+1)**2>0
    for g in (glo, (glo+gmid)/2, gmid):
        assert P(g)>0

    # On x_1+x_2+x_3=2, the negative e3 Hessian is 2[[v,r],[r,u]].
    for u in (F(1,4),F(1,2),F(3,4)):
        for v in (F(1,4),F(1,2),F(3,4)):
            w=2-u-v
            if 0<=w<=1:
                r=u+v-1
                p=1-u
                q=1-v
                assert u>=0 and v>=0 and r>=0
                assert u*v-r*r==p*q+r*(p+q)>=0

print('VERIFY_OK: {} positive exact determinant identities, phase witnesses, monotonicity endpoints, and slice curvature checks'.format(n))
