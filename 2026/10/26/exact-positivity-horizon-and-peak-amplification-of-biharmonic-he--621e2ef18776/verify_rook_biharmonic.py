#!/usr/bin/env python3
"""Independent finite-matrix and asymptotic checks for the rook-graph biharmonic heat formula.

Dependencies: Python >=3.9, NumPy and SciPy. Run: python verify_rook_biharmonic.py
The universal mathematical statements require the accompanying analytical proof.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

checks = 0

def test(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def near(u, v, tol=2e-10):
    test(abs(u-v) <= tol * max(1.0, abs(u), abs(v)), (u, v))

def four(a, b, t):
    x, y, z = (math.exp(-a*a*t), math.exp(-b*b*t), math.exp(-(a+b)**2*t))
    return ((1+(a-1)*x+(b-1)*y+(a-1)*(b-1)*z)/(a*b),
            (1-x+(b-1)*(y-z))/(a*b),
            (1-y+(a-1)*(x-z))/(a*b),
            (1-x-y+z)/(a*b))

def gap(a, b, t):
    return math.expm1(-a*a*t)*(-1) - math.exp(-b*b*t)*(-math.expm1(-(a*a+2*a*b)*t))

def root(a, b):
    # Start strictly positive: F(t)=-2ab*t+O(t^2).
    lo = 1e-7/(a+b)**2
    hi = 40.0/min(a,b)**2
    test(gap(a, b, lo)<0, (a,b,lo,gap(a,b,lo)))
    test(gap(a, b, hi)>0, (a,b,hi,gap(a,b,hi)))
    return brentq(lambda t: gap(a,b,t), lo, hi, xtol=1e-14)

for a in range(2,8):
    for b in range(2,8):
        u = np.ones((a,a))/a
        v = np.ones((b,b))/b
        I_a, I_b = np.eye(a),np.eye(b)
        Qa, Qb = I_a-u,I_b-v
        E0=np.kron(u,v); Ea=np.kron(Qa,v); Eb=np.kron(u,Qb); Eab=np.kron(Qa,Qb)
        L=a*np.kron(Qa,I_b)+b*np.kron(I_a,Qb)
        near(np.max(np.abs(E0+Ea+Eb+Eab-np.eye(a*b))),0)
        near(np.max(np.abs(L-(a*Ea+b*Eb+(a+b)*Eab))),0)
        tau=root(a,b)
        peak=brentq(lambda t: a*a*math.exp(-a*a*t)+b*b*math.exp(-b*b*t)-(a+b)**2*math.exp(-(a+b)**2*t),
                    0,12/min(a,b)**2,xtol=1e-14)
        test(0<peak<tau, (a,b,peak,tau))
        for t in [0, .2*peak,peak,(peak+tau)/2,tau,1.5*tau,2*tau]:
            K=expm(-t*(L@L))
            Ki=E0+math.exp(-a*a*t)*Ea+math.exp(-b*b*t)*Eb+math.exp(-(a+b)**2*t)*Eab
            near(np.max(np.abs(K-Ki)),0)
            k00,k10,k01,k11=four(a,b,t)
            for j in range(a*b):
                i0,j0=divmod(j,b)
                vexpected= (k00 if (i0==0 and j0==0) else
                            k10 if (i0!=0 and j0==0) else
                            k01 if (i0==0 and j0!=0) else k11)
                near(K[0,j],vexpected)
            expected=1+2*(a-1)*(b-1)/(a*b)*max(0,-a*b*k11)
            near(float(np.max(np.sum(np.abs(K),axis=1))),expected)
            near(float(np.max(np.abs(np.sum(K,axis=1)-1))),0)
            if t>0 and abs(t-tau)>1e-12:
                test((k11<0)==(t<tau), (a,b,t,k11,tau))
                test(k00>0 and k10>0 and k01>0,(a,b,t))
        if a==b:
            z0=brentq(lambda z:z**3+z*z+z-1,0,1)
            near(tau*a*a,-math.log(z0))
            near(peak*a*a,math.log(2)/3)
            near(1+2*((a-1)/a)**2*(3*2**(-4/3)-1),
                 1+2*(a-1)*(b-1)/(a*b)*(-a*b*four(a,b,peak)[3]))

for a in (2,3,5):
    for b in (100,1000,10000,100000):
        # Stable logarithmic crossing via log ratio.
        def logratio(y):
            p=(a*a/(b*b))*y
            q=(a*a/(b*b)+2*a/b)*y
            return y+math.log(-math.expm1(-p))-math.log(-math.expm1(-q))
        yl=brentq(logratio,1e-8,40,xtol=1e-13)
        near(math.exp(logratio(yl)),1)
        test(abs(yl-math.log(2*b/a))<=8*(math.log(b)/b+1e-12),
             (a,b,yl,math.log(2*b/a)))
        # Leading peak-amplification asymptotic from the exact scalar formula.
        ymax=brentq(lambda y:a*a*math.exp(-(a*a/(b*b))*y) +
                     b*b*math.exp(-y)-(a+b)**2*math.exp(-((a+b)**2/(b*b))*y),
                     .05,2.5,xtol=1e-12)
        test(abs(ymax-1)<12/b,(a,b,ymax))
        f=gap(a,b,ymax/(b*b))
        norm=1+2*(a-1)*(b-1)/(a*b)*max(0,-f)
        test(abs(b*(norm-1)-4*(a-1)/math.e)<150*a*a/b,(a,b,norm))

print('PASS: %d finite-matrix identities and asymptotic consistency assertions' % checks)
