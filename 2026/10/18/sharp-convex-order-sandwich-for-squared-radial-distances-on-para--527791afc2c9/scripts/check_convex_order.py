"""Reproducibility checks for the parallelogram radial convex-order theorem.

Tests complement the analytical single-crossing/Jensen proof. Requires numpy.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

X,W=leggauss(160)


def expectation(a,b,c,phi):
    z1=b*b+a*a*X*X
    z2=a*a+b*b*X*X
    m1=(phi(z1+2*a*b*c*X)+phi(z1-2*a*b*c*X))*0.5
    m2=(phi(z2+2*a*b*c*X)+phi(z2-2*a*b*c*X))*0.5
    return (a*float(W@m1)+b*float(W@m2))/(2*(a+b))


def law_cdf_rectangle(a,b,z):
    L=a+b
    if z>=a*a+b*b: return 1.0
    return (math.sqrt(max(0.0,z-a*a))+math.sqrt(max(0.0,z-b*b)))/L


def stoploss(a,b,c,t):
    return expectation(a,b,c,lambda z:np.maximum(t-z,0))


def run():
    checks=0
    for q in np.linspace(0.03,0.5,28):
        a=float(q);b=1-a
        for c in [-0.95,-0.6,0.,0.4,0.97]:
            for name,phi in [
                ('s2',lambda z:z*z),
                ('s3',lambda z:z*z*z),
                ('exp',lambda z:np.exp(2*z)),
                ('inverse',lambda z:1/(0.05+z)),
                ('sqrt-concave',lambda z:-np.sqrt(z))]:
                lo=expectation(.5,.5,0,phi)
                mid=expectation(a,b,c,phi)
                hi=expectation(1.,0.,0.,phi)
                assert lo <= mid+1e-12,(q,c,name,'lower',lo,mid)
                assert mid <= hi+1e-12,(q,c,name,'upper',mid,hi)
                checks+=1
            m2=expectation(a,b,c,lambda z:z)
            m4=expectation(a,b,c,lambda z:z*z)
            exact=.2-(4/3)*(a*b)**2*(1-c*c)
            assert abs(m2-1/3)<3e-13 and abs(m4-exact)<3e-13,(q,c,m2,m4,exact)
            checks+=2
    for q in np.linspace(0.003,0.497,58):
        a=float(q);b=1-a
        aa,bb=max(a,b),min(a,b)
        sstar=(1-bb*bb)/3
        assert .25<sstar<.5 and sstar<=aa**2
        for t in np.linspace(0.001,0.998,130):
            fs=law_cdf_rectangle(.5,.5,float(t))
            fr=law_cdf_rectangle(a,b,float(t))
            if t<sstar-1e-12:assert fr+1e-12>=fs,(q,t,fr,fs,sstar)
            if t>sstar+1e-12:assert fr<=fs+1e-12,(q,t,fr,fs,sstar)
            checks+=1
    for q in [0.1,0.2,0.37,0.49]:
        a=q;b=1-q
        for c in [0,.5,.95]:
            for t in np.linspace(0.05,.95,30):
                lo=stoploss(.5,.5,0,float(t))
                mid=stoploss(a,b,c,float(t))
                hi=stoploss(1,0,0,float(t))
                assert lo<=mid+8e-7 and mid<=hi+8e-7,(q,c,t,lo,mid,hi)
                checks+=1
    print('RADIAL_CONVEX_ORDER_CHECK_OK comparisons='+str(checks)+' exact_radial_moments='+str(28*5*2))

if __name__=='__main__':run()
