#!/usr/bin/env python3
"""Reproduce finite-difference spectral covariances and numerical asymptotic checks.

Requirements: Python 3 and mpmath. This checker is corroborative, not a proof
of a limit or a substitute for the analytical arguments in RESULT.md.
"""
import math
from math import comb
import mpmath as mp
mp.mp.dps = 45

def coeffs(m):
    return [(-1)**j * comb(2*m,m+j) for j in range(m+1)]

def wt(m,t,th):
    r = mp.sqrt(1-t)
    aa = coeffs(m)
    W = mp.mpf(aa[0]) + sum(2*aa[j]*r**j*mp.cos(j*th)
                                for j in range(1,m+1))
    W_t = sum(-j*aa[j]*r**(j-2)*mp.cos(j*th)
              for j in range(1,m+1))
    return W, W_t

def theta_deriv_integrand(m,k,t,th):
    r=mp.sqrt(1-t)
    W,W_t=wt(m,t,th)
    d=2-t-2*r*mp.cos(th)
    d_t=-1+mp.cos(th)/r
    H=W+k*t/d
    return (W_t+k/d-k*t*d_t/(d*d))/H

def scaled_count(m,k,t):
    alpha=mp.mpf(1)/(2*m+2)
    s=t**alpha
    splits=sorted(set([mp.mpf(0),t,mp.sqrt(t),s/10,s,5*s,
                       mp.mpf(1),mp.pi]))
    return (1-t)*t**(1-alpha)*mp.quad(
        lambda th: theta_deriv_integrand(m,k,t,th),splits)/mp.pi

def intensity(m,k,t,x):
    r=mp.sqrt(1-t); alpha=mp.mpf(1)/(2*m+2)
    th=t**alpha*x
    def log_cov(rad,ang):
        ss=1-rad**2
        W=mp.mpf(coeffs(m)[0])+sum(
            2*coeffs(m)[j]*rad**j*mp.cos(j*ang)
            for j in range(1,m+1))
        d=1+rad**2-2*rad*mp.cos(ang)
        return mp.log(W/ss+k/d)
    delta=mp.diff(lambda y: log_cov(y,th),r,2)+mp.diff(
        lambda y: log_cov(y,th),r)/r+mp.diff(
        lambda y: log_cov(r,y),th,2)/(r*r)
    return t*t*delta/4

def check():
    n=0
    for m in range(1,9):
        a=coeffs(m)
        for lag in range(-m,m+1):
            # Independent finite-filter convolution.
            got=sum((-1)**j*comb(m,j)*(-1)**(j+lag)*comb(m,j+lag)
                    for j in range(m+1) if 0<=j+lag<=m)
            assert got==a[abs(lag)]
            n+=1
        for theta in (mp.mpf('0.17'),mp.mpf('1.1'),mp.pi):
            W,_=wt(m,mp.mpf('1e-12'),theta)
            w=(2-2*mp.cos(theta))**m
            assert abs(W-w)<mp.mpf('1e-7')
            n+=1
    for m in (1,2,3):
        alp=mp.mpf(1)/(2*m+2)
        for k in (mp.mpf('0.5'),mp.mpf(2)):
            expected=alp*k**alp/mp.sin(mp.pi*alp)
            v1=scaled_count(m,k,mp.mpf('1e-5'))
            v2=scaled_count(m,k,mp.mpf('1e-7'))
            assert abs(v2-expected)<abs(v1-expected)
            assert abs(v2-expected)<mp.mpf('0.04')
            n+=2
    for m in (1,2):
        for x in (mp.mpf(0),mp.mpf('0.5'),mp.mpf(1),mp.mpf(2)):
            target=1-(1/(1+x**(2*m+2)))**2
            v1=intensity(m,mp.mpf(1),mp.mpf('1e-4'),x)
            v2=intensity(m,mp.mpf(1),mp.mpf('1e-8'),x)
            assert abs(v2-target)<abs(v1-target)+mp.mpf('1e-14')
            assert abs(v2-target)<mp.mpf('0.003')
            n+=2
    print('PASS:',n,'independent finite calculations and asymptotic corroborations')

if __name__=='__main__':
    check()
