#!/usr/bin/env python3
"""Arithmetic tests for a two-atom Acc-Sinkhorn local-rate formula.

Standard-library only; finite tests complement, not replace, the analytic proof.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from math import exp, log, sqrt


def exact_matrix(a, lam):
    b = 1 + a
    u = a*a - 2 + 2*lam
    return ((lam / b, 1 / b), (u*lam/(b*b), (b+u)/(b*b)))


def root_parameter(r):
    with localcontext() as ctx:
        ctx.prec = 70
        x = Decimal(str(r))
        h = 1-x
        a = ((h**4 + 4*h*(1+3*x)).sqrt()-h*h)/2
        q = x/(1+a)
        return a, q


def sinkhorn_scalar(x, s):
    p = (1+s)/4
    z = (1-s)/4
    e1,e2 = exp(x),exp(-x)
    u1 = .5/(p*e1+z*e2)
    u2 = .5/(z*e1+p*e2)
    c1 = e1*(p*u1+z*u2)
    c2 = e2*(z*u1+p*u2)
    return .5*((x+log(.5/c1))-(-x+log(.5/c2)))


def acc_step(x, w, a, s):
    xx = (w+sinkhorn_scalar(x,s))/(1+a)
    ww = (w+(a*a-2)*xx+2*sinkhorn_scalar(xx,s))/(1+a)
    return xx,ww


def check_exact():
    n=0
    for s in (Q(1,13), Q(1,4), Q(1,2), Q(3,4), Q(9,10)):
        lam=s*s
        for a in (Q(1,25), Q(1,6), Q(1,3), Q(2,3), Q(1,1), Q(7,5)):
            m=exact_matrix(a,lam)
            trace=m[0][0]+m[1][1]
            det=m[0][0]*m[1][1]-m[0][1]*m[1][0]
            assert trace == (a*a+a-1+(a+3)*lam)/(1+a)**2
            assert det == lam/(1+a)**2
            assert (1-trace+det)*(1+a)**2 == (a+2)*(1-lam)
            assert (1+trace+det)*(1+a)**2 == 2*a*a+3*a+(a+4)*lam
            assert det<1 and 1-trace+det>0 and 1+trace+det>0
            n+=1
        x=1/s-1
        g=x*x+(1-s)**2*x-(1-s)*(1+3*s)
        factor=(s-1)*(s+1)**2*(2*s-1)/(s*s)
        assert g == factor
        assert 1+(1-s)**2-(1-s)*(1+3*s)==(2*s-1)**2
        n+=2
    return n


def check_high_precision():
    n=0
    with localcontext() as ctx:
        ctx.prec=70
        for k in range(1, 99):
            r=Decimal(k)/Decimal(100)
            a,q=root_parameter(r)
            l=r*r
            g=a*a+(1-r)**2*a-(1-r)*(1+3*r)
            T=(a*a+a-1+(a+3)*l)/(1+a)**2
            d=l/(1+a)**2
            assert abs(g) < Decimal('1e-65')
            assert abs(T-2*q) < Decimal('1e-65')
            assert abs(d-q*q) < Decimal('1e-65')
            assert 0<a<=1
            if r<Decimal('0.5'):
                assert q>l
            elif r>Decimal('0.5'):
                assert q<l
            else:
                assert abs(q-l)<Decimal('1e-65')
            for ratio in (Decimal('.1'),Decimal('.4'),Decimal('.8')):
                aa=a*ratio
                det=l/(1+aa)**2
                assert det.sqrt()>q
            for shift in (Decimal('.0001'),Decimal('.01'),Decimal('.1'),Decimal('.4')):
                aa=a+shift
                f=(1+aa)**2*q*q-(aa*aa+aa-1+(aa+3)*l)*q+l
                assert f<0
            n+=1
    return n


def check_finite_differences():
    n=0
    h=1e-5
    for r in (.03,.1,.3,.5,.7,.9,.99):
        err=(sinkhorn_scalar(h,r)-sinkhorn_scalar(-h,r))/(2*h)
        assert abs(err-r*r)<2e-9, (r,err)
        for a in (.07,.35,.75,1.0,1.3):
            m=exact_matrix(a,r*r)
            c1=acc_step(h,0.,a,r)
            c2=acc_step(-h,0.,a,r)
            d1=((c1[0]-c2[0])/(2*h),(c1[1]-c2[1])/(2*h))
            c1=acc_step(0.,h,a,r)
            c2=acc_step(0.,-h,a,r)
            d2=((c1[0]-c2[0])/(2*h),(c1[1]-c2[1])/(2*h))
            assert abs(d1[0]-float(m[0][0]))<2e-9
            assert abs(d1[1]-float(m[1][0]))<2e-9
            assert abs(d2[0]-float(m[0][1]))<2e-9
            assert abs(d2[1]-float(m[1][1]))<2e-9
            n+=1
    return n


if __name__=='__main__':
    count=check_exact()+check_high_precision()+check_finite_differences()
    print('VERIFY_OK',count,'arithmetic and nonlinear finite-difference test cases')
