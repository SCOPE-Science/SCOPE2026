#!/usr/bin/env python3
"""Reproducibility diagnostics for finite-horizon angular resonance crossover.
Numerical tests supplement, and do not replace, the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad

def g(kappa, th):
    a=(kappa-1/kappa)/2
    return math.pi/2-math.atan(a*abs(math.sin(2*th)))

def alpha_exact(kappa,n,t,th):
    ph=math.pi/2+t/n
    a=(kappa-1/kappa)/2
    angles=th+np.arange(n)*ph
    # determinant and dot of B e(theta), B e(theta+phi)
    # angle = atan2(abs(cross),abs(dot))
    det=np.sin(ph)*np.ones(n)
    dot=np.cos(ph)*(kappa*np.cos(angles)**2+np.sin(angles)**2/kappa)+(1/kappa-kappa)*np.sin(ph)*np.sin(angles)*np.cos(angles)
    return np.arctan2(np.abs(det),np.abs(dot)).mean()

def F(kappa,t,th):
    if t==0: return g(kappa,th)
    P=math.pi/2
    lo,hi=sorted((th,th+t))
    loidx=math.floor(lo/P)-1
    hiidx=math.ceil(hi/P)+1
    pts=sorted((j*P-th)/t for j in range(loidx,hiidx+1) if 0 < (j*P-th)/t < 1)
    return quad(lambda u:g(kappa,th+t*u),0,1,epsabs=5e-11,points=pts,limit=100)[0]

def width_formula(kappa,t):
    a=(kappa-1/kappa)/2
    P=math.pi/2
    if t==0: return math.atan(a)
    r=abs(t)%P
    return 2/abs(t)*quad(lambda u:math.atan(a*math.cos(2*u))-math.atan(a*math.sin(2*u)),0,r/2,epsabs=1e-12)[0]

def numerical_width(kappa,t):
    th=np.linspace(0,math.pi/2,2001)
    vals=np.array([F(kappa,t,x) for x in th])
    return vals.max()-vals.min()

def main():
    for k in [1.2,2.0,3.7]:
        P=math.pi/2
        for t in [0.0,0.1,0.6,1.0,P/2,P,2*P,2*P+0.3,5.3]:
            w=width_formula(k,t); num=numerical_width(k,t)
            assert abs(w-num)<3e-6,(k,t,w,num)
        print('WIDTH_QUADRATURE_PASS',k)
    for t in [-1.4,-0.4,0,0.13,1.1,math.pi/2,math.pi,3.7]:
        k=2.2; n=2001; th=0.123
        err=abs(alpha_exact(k,n,t,th)-F(k,t,th))
        a=(k-1/k)/2
        assert err <= (k+a)*abs(t)/n+1e-12,(t,err)
        print('FINITE_HORIZON_PASS',t,'error',format(err,'.9g'))
    for k in [1.5,2.0,5.0]:
      a=(k-1/k)/2
      t0=math.pi/2
      for eps in [1e-2,2e-3,5e-4]:
        ratio=width_formula(k,t0+eps)*t0/(eps*math.atan(a))
        assert abs(ratio-1)<10*eps
      print('RESONANT_CUSP_PASS',k)
    print('CHECKS_PASS')
if __name__=='__main__':main()
