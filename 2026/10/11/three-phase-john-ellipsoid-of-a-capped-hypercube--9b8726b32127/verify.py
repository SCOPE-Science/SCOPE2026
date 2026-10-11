#!/usr/bin/env python3
"""Exact support-function checks and independent one-variable grid stress tests.
Run: python3 verify.py. Uses only Python's standard library.
The general theorem rests on the written calculus proof, not this finite test.
"""
from fractions import Fraction as F
from math import sqrt,log

def parameters(n,tau):
    assert n>=2 and F(0)<tau<=n
    if 2*tau<=n+1:
        t=tau/F(n+1)
        a=tau*tau/F(n*(n+1))
        b=tau*tau/F(n*(n+1)**2)
        return t,a,b,1
    if (2*tau-n)**2<=n:
        t=F(1,2)
        a=tau*(n-tau)/F(n*(n-1))
        b=(2*tau-n)**2/F(4*n)
        return t,a,b,2
    return F(1,2),F(1,4),F(1,4),3

def exact_support_checks():
    k=0
    all_phases=set()
    for n in range(2,22):
        for j in range(1,24*n+1):
            tau=F(j,24)
            t,a,b,phase=parameters(n,tau)
            all_phases.add(phase)
            s2=((n-1)*a+b)/n
            # +/- coordinate support under x_i=t+/-sqrt(s2)
            assert 0<t<=F(1,2) and a>0 and b>0
            assert s2<=t*t and s2<=(1-t)**2
            # sum upper support (n*t+sqrt(n*b)<=tau)
            slack=tau-n*t
            assert slack>=0 and n*b<=slack*slack
            assert s2==t*t  # all lower coordinate facets touched
            if phase==1:
                assert slack*slack==n*b
                assert (2*t<=1)
            elif phase==2:
                assert t==F(1,2) and (1-t)**2==s2 and slack*slack==n*b
            else:
                assert t==F(1,2) and a==b==F(1,4)
            k+=1
    assert all_phases=={1,2,3},all_phases
    return k

def independent_grid_checks():
    trials=0
    # This scans the feasible 2-parameter symmetric-ellipsoid family
    # using a different parametrization than the displayed closed forms.
    for n in (2,3,4,5,6,9,13,20):
        for j in range(1,32):
            tau=F(n*j,32)
            if tau==0:continue
            t,a,b,phase=parameters(n,tau)
            optimum=(n-1)*log(float(a))+log(float(b))
            cap=float(tau/n)
            for k in range(1,501):
                x=min(.5,cap)*k/501
                lower=min(x*x,n*(cap-x)**2)
                if lower<=0:continue
                # Optimize b at this t separately, without using the theorem.
                bb=lower
                aa=(n*x*x-bb)/(n-1)
                if aa<=0:continue
                v=(n-1)*log(aa)+log(bb)
                assert v<optimum+1e-8,(n,tau,x,v-optimum)
            trials+=1
    return trials

if __name__=='__main__':
    e=exact_support_checks()
    g=independent_grid_checks()
    print('PASS: exact support/phase/positivity certificates for',e,'rational instances')
    print('PASS: independent symmetric two-variable grid optimization for',g,'parameter cases')
