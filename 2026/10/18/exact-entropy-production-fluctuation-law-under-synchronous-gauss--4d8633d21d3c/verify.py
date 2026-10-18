#!/usr/bin/env python3
"""Independent quadrature, symbolic, and regenerative checks of joint Gaussian-reset entropy fluctuations."""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad
from numpy.random import default_rng

TEST_COUNT=0

def check_close(actual,expected,rtol=3e-9,atol=3e-10):
    global TEST_COUNT
    assert math.isclose(float(actual),float(expected),rel_tol=rtol,abs_tol=atol), (actual,expected)
    TEST_COUNT+=1

def theory(q,s,d,kappa=1.0):
    m1=kappa*q*(s-1)**2/(s*(q+2))
    a=kappa*2*q*(s-1)**2*(q*s+2*s*s+2)/(s*s*(q+2)*(q+4))
    cross=kappa*8*q*(s-1)**4/(s*s*(q+2)**3*(q+4))
    v=d*a+d*d*cross
    fano=2+4*(s-1)**2/(s*(q+4))*(1+2*d/(q+2)**2)
    return d*m1,v,cross,fano

def independent_quadrature(q,s,d):
    # OU has kappa=D=1, reset variance s, reset rate q.
    c=(1-s)/(2*s)
    def integrand(u):
        t=math.exp(-2*u)
        yvar=1+(s-1)*t
        covsq=s*s*t
        conditional_mean=c*(yvar-s)
        conditional_var=2*c*c*(yvar*yvar+s*s-2*covsq)
        return conditional_mean,conditional_var
    Emean=quad(lambda u:q*math.exp(-q*u)*integrand(u)[0],0,1000,epsabs=1e-11)[0]
    m=q*Emean
    Econdvar=quad(lambda u:q*math.exp(-q*u)*integrand(u)[1],0,1000,epsabs=1e-11)[0]
    center=quad(lambda u:q*math.exp(-q*u)*(integrand(u)[0]-m*u)**2,0,1000,epsabs=1e-11)[0]
    return d*m, q*(d*Econdvar+d*d*center),q*center

# Tests are independent quadrature of conditional Gaussian moments; no prior integral identities assumed.
for q in [0.19,0.7,1.0,2.9,13.0]:
    for s in [.17,.55,1.0,1.82,4.9]:
        for d in [1,2,4,9]:
            m,v,c,f=theory(q,s,d)
            mi,vi,ci=independent_quadrature(q,s,d)
            check_close(m,mi)
            check_close(v,vi)
            check_close(c,ci)
            if s!=1.0:
                check_close(v/m,f)
                assert f>2
                TEST_COUNT+=1
                if d>1:
                    check_close((v-d*theory(q,s,1)[1])/(d*(d-1)),c)

# Physical-time regenerative simulation of completed cycles. The omitted partial-cycle term is bounded in L2.
def simulate(q,s,d,nrep=6000,T=400,seed=2):
    rng=default_rng(seed)
    # Simulate each entire trajectory independently; exact OU conditional transitions.
    vals=np.zeros((nrep,d),dtype=float)
    for run in range(nrep):
        time=0.
        while True:
            tau=rng.exponential(1/q)
            if time+tau>T:break
            x=rng.normal(0,math.sqrt(s),size=d)
            t=math.exp(-2*tau)
            y=math.sqrt(t)*x+math.sqrt(1-t)*rng.normal(size=d)
            vals[run,:]+=(1-s)/(2*s)*(y*y-x*x)
            time+=tau
    return vals

for q,s,d,T,seed in [(.8,.6,3,350,103),(2.1,2.7,4,250,111)]:
    samples=simulate(q,s,d,T=T,seed=seed)
    m,v,c,f=theory(q,s,d)
    # Fixed-time fluctuations have O(1) end effects; simulation has finite-sample error.
    mean_obs=float(samples.sum(axis=1).mean()/T)
    var_obs=float(samples.sum(axis=1).var(ddof=1)/T)
    cross_obs=float(np.cov(samples.T)[0,1]/T)
    assert abs(mean_obs/m-1)<.045,(mean_obs,m)
    assert abs(var_obs/v-1)<.09,(var_obs,v)
    assert abs(cross_obs/c-1)<.35,(cross_obs,c)
    TEST_COUNT+=3

# Free-Brownian limiting case kappa->0, D=r=sigma^2=1: Mori et al. mean rate=1, variance rate=6.
for kap in [0.001,.0002]:
    q=1/kap;s=kap
    m,v,c,f=theory(q,s,1,kap)
    assert abs(m-1)<.008 and abs(v-6)<.05,(kap,m,v)
    TEST_COUNT+=2

print('PASSED', TEST_COUNT, 'independent analytical-quadrature/renewal/sample checks')
