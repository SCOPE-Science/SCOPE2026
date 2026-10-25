#!/usr/bin/env python3
"""Reproducible Gaussian normal-cone and sharp-crossover diagnostics.

Monte Carlo checks supplement, but do not prove, the asymptotic theorem.
"""
import math
import numpy as np
from scipy import integrate, special
C=math.sqrt(3)*math.gamma(4/3)/(2*math.pi**(1/3))
print('constant',format(C,'.12f'))
rng=np.random.default_rng(271828)
for n,trials in [(3,900000),(4,900000),(20,3000000),(80,3000000),(300,2000000)]:
    end=0; circwin=0; doub=0; used=0
    batch=10000
    for off in range(0,trials,batch):
        b=min(batch,trials-off)
        g=rng.standard_normal((b,n))
        h=np.abs(np.diff(g,axis=1))
        i=np.argmax(h,axis=1)
        end+=np.count_nonzero(i==0)
        hn=np.abs(g[:,-1]-g[:,0])
        hc=np.concatenate([h,hn[:,None]],axis=1)
        circwin+=np.count_nonzero(np.argmax(hc,axis=1)==0)
        doub+=np.count_nonzero((hn>h[:,0]) & (h[:,0]>h[:,1:].max(axis=1))) if n>2 else 0
        used+=b
    p=end/used
    pp=1/n+C*n**(-4/3)*math.log(n)**(-1/3)
    predicted=(p-1/n)*n**(4/3)*math.log(n)**(1/3)
    se=math.sqrt(p*(1-p)/used)
    print(f'n={n}, trials={used}, endpoint_probability={p:.8f}, cyclic_probability={circwin/used:.8f}, event_probability={doub/used:.8f}, 1/n={1/n:.8f}, theoretical_asymptotic={pp:.8f}, scaled_excess={predicted:.6f}, stderr={se:.8f}')
    assert abs(p-circwin/used-doub/used)<1e-12
    assert abs(circwin/used-1/n)<5*math.sqrt((1/n)*(1-1/n)/used)
    if n==3: assert abs(p-.5)<5*se
# Poissonized one-dimensional tail integral, a diagnostic not a finite-n identity.
scaled=[]
for n in (10**3,10**6,10**12):
    def integrand(u):
        if u <= 0: return 0.0
        t=-special.ndtri(u/(2*n))
        a=special.ndtr(-t/math.sqrt(3))+special.ndtr(-math.sqrt(3)*t)
        return a*math.exp(-u)
    val,_=integrate.quad(integrand,0,40,epsabs=1e-14,epsrel=1e-10)
    x=val*n**(1/3)*math.log(n)**(1/3)
    scaled.append(x)
    print(f'Poissonized tail integral n={n}: scaled={x:.9f}')
assert scaled[0] < scaled[1] < scaled[2] < C
assert abs(scaled[-1]-C) < .02
print('ALL_DIAGNOSTICS_PASS')
