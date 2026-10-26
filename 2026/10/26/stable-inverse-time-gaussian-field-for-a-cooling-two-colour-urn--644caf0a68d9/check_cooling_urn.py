#!/usr/bin/env python3
"""Exact finite-time consistency checks for a time-inhomogeneous symmetric two-colour urn."""
from fractions import Fraction as F
from collections import defaultdict
from math import log, exp

SCHEDULES = [
    [F(1,2),F(1,3),F(1,5),F(3,4),F(2,3),F(1,7),F(1,4),F(0),F(1,2),F(3,10)],
    [F(1),F(0),F(1),F(0),F(1,2),F(1,3),F(2,5),F(1,4),F(0),F(1,7)],
]
checks=0
for (w0,b0) in [(1,1),(1,2),(3,4),(2,3)]:
 for ps in SCHEDULES:
    m=w0+b0; dist={w0:F(1)}; a=F(1); h=F(w0-b0,m)**2
    for n,p in enumerate(ps,1):
        tot=m+n; nxt=defaultdict(F)
        for w,pr in dist.items():
            q=p+(1-2*p)*F(w,tot-1)
            assert 0<=q<=1
            nxt[w+1]+=pr*q
            nxt[w]+=pr*(1-q)
        dist=nxt
        a*=1-2*p/F(tot)
        prev_q2=h
        h=F((tot-1)*(tot+1-4*p),tot**2)*h +F(1,tot**2)
        mu=sum(pr*F(2*w-tot,tot) for w,pr in dist.items())
        sec=sum(pr*F(2*w-tot,tot)**2 for w,pr in dist.items())
        assert mu==a*F(w0-b0,m), (n,mu,a)
        assert sec==h,(n,sec,h)
        assert sum(dist.values())==1
        # Formula for the one-step unconditional martingale increment variance.

        vardelta=(1-(1-2*p)**2*prev_q2)/((tot*a)**2)
        assert vardelta>=0
        checks+=4
print('EXACT: %d rational consistency checks passed, 4 initial configurations, 2 inhomogeneous schedules, 10 steps.'%checks)
for beta in [0.5,1.0,1.5]:
    theta=0.4;m=3
    a=1.
    samples={20000,100000,200000}
    values=[]
    for n in range(1,200001):
        p=min(1,theta/log(n+2.718281828459045))
        if beta!=1:
            p=min(1,theta/(log(n+2.718281828459045)**beta))
        a*=1-2*p/(m+n)
        if n in samples:
            if beta<1: reference=2*theta/(1-beta)*(log(n)**(1-beta))
            elif beta==1: reference=2*theta*log(log(n))
            else:reference=0.
            values.append((n,round(log(a)+reference,9)))
    assert 0<a<=1
    print('ASYMPTOTIC diagnostic beta=%.1f, log(a_n)+leading_scale: %s'%(beta,values))
print('Numerical diagnostics are illustrative; infinite-time convergence is established analytically.')
