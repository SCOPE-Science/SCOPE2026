"""Reproducible numerical diagnostics for the unequal-radius two-ball ellipsoid theorem.

Run: python verify.py (requires numpy and scipy). Numeric tests do not prove universality.
"""
import numpy as np
from scipy.optimize import brentq


def ellipse(d, q, L):
    assert d >= 2 and 0 < q < 1 and L > 0
    Lc = d * (1-q*q) / ((d-1)*q)
    if L <= 1-q:
        return 1., 1., 0., 'nested'
    if L <= Lc:
        H=L+q
        B=(d-1)*H
        r=2/(B+np.sqrt(B*B+4*d))
        a=d*(H+r)/(d+1)
        c=(H-d*r)/(d+1)
        b=np.sqrt(d*a*r)
        return a,b,c,'single'
    bc=np.sqrt((d*d-q*q)/(d*d-1))
    def betas(b):
        return np.sqrt(1-b**-2),np.sqrt(1-q*q/b**2)
    def et(b):
        x,y=betas(b)
        return x*y
    bmax=brentq(lambda z:d*et(z)-1,bc,100)
    def lof(b):
        x,y=betas(b)
        e=x*y
        return b*np.sqrt(d*e/(1-d*e))*(x+y)
    b=brentq(lambda z:lof(z)-L,bc,bmax*(1-1e-13),xtol=1e-13)
    e=et(b)
    T=b*np.sqrt(d*e/(1-d*e))
    a=np.hypot(b,T)
    c=T*betas(b)[0]
    x,y=betas(b)
    y1,y2=-a*x/T,a*y/T
    assert abs(y1*y2+1/d)<1e-7
    return a,b,c,'double'


def run():
    cases=0
    min_margin=1
    for d in (2,3,4,7,11):
        for q in (.08,.25,.5,.85,.98):
            Lc=d*(1-q*q)/((d-1)*q)
            for L in (max(.001, (1-q)*.6), 1-q, (1-q+Lc)/2, Lc, Lc*1.01, Lc*1.2, Lc*2, Lc*10):
                a,b,c,phase=ellipse(d,q,L)
                ts=np.linspace(-1.,1.,1001)
                h=c*ts+np.sqrt(b*b+(a*a-b*b)*ts*ts)
                err1=np.min(h-1.)
                err2=np.min(h-L*ts-q)
                scale=max(1.,L)
                assert err1>-2e-7*scale,(d,q,L,phase,err1)
                assert err2>-2e-7*scale,(d,q,L,phase,err2)
                min_margin=min(min_margin,err1,err2)
                cases+=1
            eps=1e-7*Lc
            e1=ellipse(d,q,Lc)
            e2=ellipse(d,q,Lc+eps)
            assert max(abs(e1[i]-e2[i]) for i in range(3))<2e-4*max(1,Lc)
    print(f'PASS: {cases} geometric cases, each with 1001 support normals; min sampled margin={min_margin:.2g}')


if __name__=='__main__':
    run()
