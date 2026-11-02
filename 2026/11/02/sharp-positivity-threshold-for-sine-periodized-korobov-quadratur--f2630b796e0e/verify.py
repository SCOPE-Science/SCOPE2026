#!/usr/bin/env python3
"""Direct numerical cross-checks of one-dimensional Korobov-sine quadrature."""
import math
import numpy as np
from scipy.integrate import quad

PI=math.pi

def density(t):
    return (PI/2.0)*abs(math.sin(2*PI*t))

def bernoulli2(t):
    u=t%1.0
    return u*u-u+1/6

def kernel(t, gamma):
    return 1+2*gamma*PI**2*bernoulli2(t)

def h_formula(n):
    if n%2==0:
        t=PI/n
        return 1/(2*PI**2)-1/(2*PI*n*math.tan(t))
    t=PI/(2*n)
    return 1/(8*n*n)+1/(2*PI**2)-1/(4*PI*n*math.tan(t))

def p0_formula(n):
    return .5-n*math.sin(2*PI/n)/(4*PI)

def critical(n):
    h=h_formula(n)
    p=p0_formula(n)
    return 3*n*n*p/(PI**2*(6*n*h-p))

def integral(f, breaks):
    return sum(quad(f, a,b,epsabs=7e-12,epsrel=7e-12,limit=300)[0] for a,b in zip(breaks[:-1],breaks[1:]))

num_h=0;num_k=0;num_s=0;num_sign=0
for n in range(2,15):
    mesh=[j/n for j in range(n+1)]
    bp=sorted(set(mesh+[0.5]));
    # evaluate separately from closed-form, using local physical coordinates
    H=sum(integral(lambda t,j=j:density(t)*(t-j/n)*((j+1)/n-t),
                   sorted(set([j/n,(j+1)/n]+([.5] if j/n<.5<(j+1)/n else [])))) for j in range(n))
    assert abs(H-h_formula(n))<2e-12,(n,H,h_formula(n))
    num_h+=1
    gamma_c=critical(n)
    assert gamma_c>0
    for scale in (.25,.75,1,1.25,3):
        gamma=gamma_c*scale
        x=np.arange(n)/n
        K=np.array([[kernel(float(a-b),gamma) for b in x] for a in x])
        kap=np.array([integral(lambda y,x0=x0:kernel(float(x0-y),gamma)*density(y),
                               sorted(set(bp+[float(x0)]))) for x0 in x])
        weights=np.linalg.solve(K,kap)
        delta=2*gamma*PI**2*H/(n*(1+gamma*PI**2/(3*n*n)))
        pred0=p0_formula(n)-delta
        assert max(abs(weights[0]-pred0),abs(weights.min()-pred0))<3e-10,(n,scale,weights,pred0)
        assert abs(weights.sum()-(1-n*delta))<3e-10
        num_k+=1
        if scale<1:
            assert weights.min()>-2e-10
        elif scale>1:
            assert weights.min()<-1e-8
        else:
            assert abs(weights.min())<3e-10
        num_sign+=1
    if n<=8:
        gamma=1.2*gamma_c
        x=np.arange(n)/n
        K=np.array([[kernel(float(a-b),gamma) for b in x] for a in x])
        vals=np.array([math.sin(j+0.31)+.05*j for j in range(n)])
        coefs=np.linalg.solve(K,vals)
        M=vals.mean()/(1+gamma*PI**2/(3*n*n))
        for j in range(n):
            for fract in (.13,.33,.66,.91):
                y=(j+fract)/n
                actual=sum(float(a)*kernel(float(y-z),gamma) for a,z in zip(coefs,x))
                predicted=vals[j]*(1-fract)+vals[(j+1)%n]*fract -2*PI**2*gamma*M*fract*(1-fract)/(n*n)
                assert abs(actual-predicted)<6e-12,(n,j,fract,actual,predicted)
                num_s+=1

from mpmath import mp
mp.dps=70
asym=[]
for n in (100,101,500,501,2000,2001):
    N=mp.mpf(n)
    p=mp.mpf('.5')-N*mp.sin(2*mp.pi/N)/(4*mp.pi)
    H=1/(2*mp.pi**2)-mp.cot(mp.pi/N)/(2*mp.pi*N) if n%2==0 else 1/(8*N*N)+1/(2*mp.pi**2)-mp.cot(mp.pi/(2*N))/(4*mp.pi*N)
    g=3*N*N*p/(mp.pi**2*(6*N*H-p))
    asym.append((n,float(g-N)))
print('PASS: H cell-integral comparisons',num_h)
print('PASS: direct kernel-system weight comparisons',num_k)
print('PASS: off-grid kernel interpolant comparisons',num_s)
print('PASS: positive/zero/negative sign classifications',num_sign)
print('gamma_c - N asymptotic',asym,'limit',float(mp.pi**2/3))
