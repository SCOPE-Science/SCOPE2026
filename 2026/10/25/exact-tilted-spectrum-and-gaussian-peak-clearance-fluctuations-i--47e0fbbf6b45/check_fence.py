#!/usr/bin/env python3
"""Independent numerical diagnostics for peak-clearance statistics of zigzag order polytopes.
All tests are finite-dimensional and do not substitute for the analytic spectral proof.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq


def spectral_lambda(t):
    if abs(t-2.0) < 1e-12:
        return 1.0
    if t < 2.0:
        k=brentq(lambda z:2*z/math.tan(z)-t,1e-12,math.pi-1e-12,xtol=1e-14)
        return 1/(k*k+t*t/4)
    q=brentq(lambda z:2*z/math.tanh(z)-t,1e-12,max(t,3),xtol=1e-13)
    return 1/(t*t/4-q*q)


def matrix(t,N=240):
    nodes, w=leggauss(N)
    x=(nodes+1)/2;w=w/2
    mx=np.maximum(x[:,None],x[None,:])
    if abs(t)<1e-12:
        integral=1-mx
    else:
        integral=(np.exp(t)-np.exp(t*mx))/t
    K=integral*np.exp(-t*(x[:,None]+x[None,:])/2)
    return np.sqrt(w[:,None]*w[None,:])*K, np.sqrt(w)


def finite_mgf(m,t,N=200):
    K, w=matrix(t,N)
    z=w.copy()
    for j in range(m): z=K@z
    return w@z


def checks():
    count=0
    for t in [-2.0,-0.8,-0.1,0,0.15,0.9,1.7,2.0,2.7,4.0]:
        K,_=matrix(t,260)
        num=np.linalg.eigvalsh(K)[-1]
        exact=spectral_lambda(t)
        err=abs(num-exact)
        assert err<0.000015,(t,num,exact,err)
        count+=1
    # Direct three-variable integral: x,z in [0,y], 0<y<1.
    assert abs(finite_mgf(1,0,180)-1/3)<6e-6
    count+=1
    h=0.005
    def L(t):return math.log(finite_mgf(1,t,220))
    mean=(L(h)-L(-h))/(2*h)
    var=(L(h)+L(-h)-2*L(0))/h**2
    assert abs(mean-3/8)<0.00001,(mean,3/8)
    assert abs(var-11/320)<0.00001,(var,11/320)
    count+=2
    def l(t):return math.log(spectral_lambda(t))
    deriv=(l(h)-l(-h))/(2*h)
    variance=(l(h)+l(-h)-2*l(0))/h**2
    mu=4/math.pi**2
    sigma2=24/math.pi**4-2/math.pi**2
    assert abs(deriv-mu)<0.000003,(deriv,mu)
    assert abs(variance-sigma2)<0.000003,(variance,sigma2)
    assert sigma2>0
    count+=3
    for t in [0.1,0.4,1.0]:
        for m in [10,40]:
            logratio=(math.log(finite_mgf(m,t,96))-math.log(finite_mgf(m,0,96)))/m
            target=math.log(spectral_lambda(t)/spectral_lambda(0))
            assert abs(logratio-target)<0.12/m,(t,m,logratio,target)
            count+=1
    print('VERIFY_OK eigenvalue_cases=10 moments=3 cumulants=3 finite_transfer_cases=6', 'total=',count)
    print('asymptotic_mean',mu,'asymptotic_variance',sigma2)

if __name__=='__main__':checks()
