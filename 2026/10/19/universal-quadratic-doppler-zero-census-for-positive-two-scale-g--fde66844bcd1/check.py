"""Numerical checks for two-scale Gaussian ambiguity zeros.

Requires scipy and mpmath. Finite tests supplement the mathematical argument.
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar, brentq
import mpmath as mp


def pieces(a,b,c,t,v):
    assert 0<a<b and c>0
    aa=(2*a)**(-0.5)*np.exp(-np.pi*(a*t*t/2+v*v/(2*a)))
    bb=c*c*(2*b)**(-0.5)*np.exp(-np.pi*(b*t*t/2+v*v/(2*b)))
    cross=2*c*(a+b)**(-0.5)*np.exp(-np.pi*(a*b*t*t+v*v)/(a+b))
    return aa,bb,cross


def ratio(a,b,c,t,v):
    beta=np.pi*(b-a)/(2*(a+b))
    aa=(a+b)**0.5/(2*c*(2*a)**0.5)*np.exp(beta*(a*t*t-v*v/a))
    bb=c*(a+b)**0.5/(2*(2*b)**0.5)*np.exp(beta*(v*v/b-b*t*t))
    return aa+bb


def count_positive_roots(a,b,c,t):
    k=np.pi*(b-a)*t/(a+b)
    period=2*np.pi/k
    j_lo=max(0,int(np.floor((a*t-3)*k/(2*np.pi)-0.75)))
    j_hi=int(np.ceil((b*t+3)*k/(2*np.pi)+0.75))
    cnt=0
    for j in range(j_lo,j_hi+1):
        lo=(0.5+2*j)*np.pi/k
        hi=(1.5+2*j)*np.pi/k
        # negative cosine lobe: center at (2j+1)*pi/k
        center=(2*j+1)*np.pi/k
        if lo<0:lo=0
        if lo>=hi:continue
        def h(v):return np.cos(k*v)+ratio(a,b,c,t,v)
        val=h(center)
        if val >=0:
            if center<a*t-0.25 or center>b*t+0.25:continue
            opt=minimize_scalar(h,bounds=(lo,hi),method='bounded',options={'xatol':1e-12})
            val=opt.fun
        if val < -1e-9:cnt+=2
        elif abs(val)<1e-9:cnt+=2 # counted with multiplicity
    return cnt


def check_integral(a,b,c,t,v):
    mp.mp.dps=55
    a,b,c,t,v=map(mp.mpf,map(str,[a,b,c,t,v]))
    f=lambda z:mp.exp(-mp.pi*a*z*z)+c*mp.exp(-mp.pi*b*z*z)
    integrand=lambda z:f(z+t/2)*f(z-t/2)*mp.cos(2*mp.pi*v*z)
    q=2*mp.quad(integrand,[0,mp.inf])
    pa=mp.exp(-mp.pi*(a*t*t/2+v*v/(2*a)))/mp.sqrt(2*a)
    pb=c*c*mp.exp(-mp.pi*(b*t*t/2+v*v/(2*b)))/mp.sqrt(2*b)
    pc=2*c/mp.sqrt(a+b)*mp.exp(-mp.pi*(a*b*t*t+v*v)/(a+b))*mp.cos(mp.pi*(b-a)*t*v/(a+b))
    exact=pa+pb+pc
    return float(abs(q-exact)/(abs(q)+abs(exact)+mp.mpf('1e-40')))

if __name__=='__main__':
    for a,b,c,t,v in [(1,3,1,0.7,0.4),(1,3,0.1,1.5,1.1),(1,3,10,2.5,2.0),(0.7,2.4,0.2,1.1,0.8),(0.5,5,3,1.4,1.6)]:
        diff=check_integral(a,b,c,t,v)
        print('integral',a,b,c,t,v,'relative_error',diff)
        assert diff < 1e-18
    for a,b,c in [(1,3,0.1),(1,3,1),(1,3,10),(0.7,2.4,0.2),(0.5,5,3)]:
        C=(b-a)**2/(a+b)
        for t in [6.,12.,24.]:
            n=count_positive_roots(a,b,c,t)
            err=n-C*t*t
            print('count',a,b,c,t,n,'leading',C*t*t,'error',err)
            assert abs(err)<30
    print('ALL CHECKS PASSED')
