"""Reproduce spectral-curvature and unique threshold calculations.
This is a supplementary finite/numerical check, not a substitute for the proof.
"""
import math
from fractions import Fraction
import sympy as sp
import mpmath as mp


def s(u):
    if u == 0:
        return mp.mpf(1)
    return 1-u*(-mp.expm1(-1/u))

def ds(u):
    return -1+(1+1/u)*mp.exp(-1/u)

def dds(u):
    return mp.exp(-1/u)/u**3

def Q(u):
    return s(u)*dds(u)/(2*ds(u)**2)

def rho(alpha,u,b):
    s1,s2=s(u*(1+b/2)),s(u*(1-b/2))
    a=1-alpha/2
    return (a*(s1+s2)+mp.sqrt(a*a*(s1-s2)**2+alpha*alpha*s1*s2))/2

def rho2(alpha,u):
    return u*u/4*(dds(u)-2*(alpha-1)/alpha*ds(u)**2/s(u))

def check_symbolic():
    t,u,a=sp.symbols('t u a',positive=True)
    ee=sp.exp(-1/u)
    ss=1-u*(1-ee)
    assert sp.simplify(sp.diff(ss,u)-(-1+(1+1/u)*ee))==0
    assert sp.simplify(sp.diff(ss,u,2)-ee/u**3)==0
    tt=sp.symbols('t',positive=True)
    H=tt*tt*sp.exp(-tt)*(tt-1+sp.exp(-tt))/(2*(1-(1+tt)*sp.exp(-tt))**2)
    N=(tt**2-4*tt+2)*sp.exp(2*tt)+(tt**3+tt**2+4*tt-4)*sp.exp(tt)+2
    assert sp.simplify(sp.diff(H,tt)+tt*N/(2*(sp.exp(tt)-1-tt)**3))==0
    for n in range(0,33):
        coef=sp.simplify(sp.diff(N,tt,n).subs(tt,0))
        if n>=3:
            known=(n-1)*(2**(n-2)*(n-8)+n*n-n+4)
            assert coef==known,(n,coef,known)
        else:
            assert coef==0
    print('PASS exact derivatives and positive-series formula (orders 0..32)')


def check_numerical():
    mp.mp.dps=80
    vals=[]
    for alpha in [mp.mpf(1)/2,mp.mpf(1),mp.mpf(5)/4,mp.mpf(3)/2,mp.mpf(2)]:
        for u in [mp.mpf('0.05'),mp.mpf('0.1'),mp.mpf('0.2'),mp.mpf('0.238'),mp.mpf('0.3'),mp.mpf('0.5'),mp.mpf(1),mp.mpf(3)]:
            h=mp.mpf('0.00001')
            numeric=(rho(alpha,u,h)-2*rho(alpha,u,0)+rho(alpha,u,-h))/h**2
            theo=rho2(alpha,u)
            assert abs(numeric-theo) < mp.mpf('0.00000001') * max(1,abs(theo)),(alpha,u,numeric,theo)
            vals.append((alpha,u))
    root=mp.findroot(lambda x: Q(x)-mp.mpf('0.5'),(mp.mpf('0.20'),mp.mpf('0.3')))
    assert abs(root-mp.mpf('0.238036776718270'))<mp.mpf('1e-14')
    assert Q(mp.mpf('0.1'))<mp.mpf('0.5')<Q(mp.mpf('0.3'))
    for u in [mp.mpf('0.1'),mp.mpf(1)]:
        print('bipartite u:',mp.nstr(u,6),'fair rho:',mp.nstr(rho(2,u,0),20),'endpoint rho:',mp.nstr(rho(2,u,2),20),'rho2:',mp.nstr(rho2(2,u),20))
    print('PASS',len(vals),'symmetric finite-difference curvature comparisons')
    print('threshold alpha=2 u* =',mp.nstr(root,32))

if __name__=='__main__':
    check_symbolic()
    check_numerical()
