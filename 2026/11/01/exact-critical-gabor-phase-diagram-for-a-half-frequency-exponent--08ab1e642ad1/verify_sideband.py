"""Supplementary numerical verification for the half-frequency sideband exponential Gabor theorem.

No finite test replaces the proof of the universal extremal statements.
"""
import numpy as np


def sharp_bounds(r,c):
    assert 0<r<1 and c>0
    cm=(1-r)/(1+r); cp=1/cm
    upper=max(1/(1-r)+c/(1+r),1/(1+r)+c/(1-r))**2
    if c<cm:
        lower=r*r*(1/(1+r)-c/(1-r))**2
    elif c>cp:
        lower=r*r*(c/(1+r)-1/(1-r))**2
    else: lower=0.
    return lower, upper


def zval(r,c,x,w):
    z=np.exp(-2j*np.pi*w)
    return r**x*(1/(1-r*z)+c*np.exp(1j*np.pi*x)/(1+r*z))


def direct_sum(r,c,x,w,terms=2500):
    z=np.exp(-2j*np.pi*w)
    j=np.arange(terms)
    return r**x*np.sum((r*z)**j*(1+c*np.exp(1j*np.pi*x)*(-1)**j))


def exact_interior_zero(r,c):
    u=(c*c-1)*(1+r*r)/(2*r*(1+c*c))
    assert -1<u<1
    w=np.arccos(u)/(2*np.pi)
    x=1-np.arctan2(2*r*np.sqrt(1-u*u),1-r*r)/np.pi
    return x,w


def main():
    total=0
    for r in (0.08,0.2,0.4142135623730951,0.55,0.8,0.96):
        cm=(1-r)/(1+r); cp=1/cm
        cs=[cm/8,cm/2,cm*.99,cm, cm*1.01, np.sqrt(cm), 1., np.sqrt(cp),cp*.99,cp,cp*1.01,cp*2,cp*10]
        xs=np.linspace(0,1,201,endpoint=False)
        ws=np.linspace(0,1,641,endpoint=False)
        zz=np.exp(-2j*np.pi*ws)[None,:]
        tt=np.exp(1j*np.pi*xs)[:,None]
        for c in cs:
            a,b=sharp_bounds(r,c)
            total+=1
            f=r**xs[:,None]*(1/(1-r*zz)+c*tt/(1+r*zz))
            vals=np.abs(f)**2
            tol=1e-10*(1+b)
            assert np.min(vals)>=a-tol,(r,c,a,vals.min())
            assert np.max(vals)<=b+tol,(r,c,b,vals.max())
            total+=2
            # The upper bound is always attained at x=0, frequency 0 or 1/2.
            assert abs(max(abs(zval(r,c,0,0))**2,abs(zval(r,c,0,.5))**2)-b)<tol
            total+=1
            # The lower bound in the frame regimes is a one-sided x->1 limit.
            if c<cm:
                assert abs(abs(zval(r,c,1,0.5))**2-a)<tol
                total+=1
            if c>cp:
                assert abs(abs(zval(r,c,1,0))**2-a)<tol
                total+=1
            if cm<c<cp:
                x,w=exact_interior_zero(r,c)
                assert 0<x<1 and 0<w<.5
                assert abs(zval(r,c,x,w))<1e-10*(1+c)
                total+=3
            for x,w in ((.05,.3),(.4,.6),(.85,.93)):
                # Geometric-series Zak identity, independently computed from shifts.
                assert abs(zval(r,c,x,w)-direct_sum(r,c,x,w))<1e-9*(1+c)
                total+=1
    print('PASS:',total,'numerical checks; all analytical claims require the written proof')

if __name__=='__main__':main()
