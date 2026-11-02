#!/usr/bin/env python3
"""Reproducible exact rational and stochastic checks of the stated isotropic row-refresh theorem.
Only Python 3 and NumPy are needed. All stochastic checks have fixed seeds.
"""
from fractions import Fraction as F
import math
import numpy as np

count=0
for d in range(2,129):
    z2=F(1,d)
    z4=F(3,d*(d+2))
    a4=1-2*z2+z4
    assert a4==F(d*d-1,d*(d+2))
    assert 0<a4<1
    assert 1-z2==F(d-1,d)
    for m4 in (F(1),F(2),F(3),F(5),F(9)):
        radial4=(2*(d-1)+m4)/(1-a4)
        projection4=3*radial4/(d*(d+2))
        predicted=3+F(3,2*d+1)*(m4-3)
        assert projection4==predicted
        assert radial4==F(d*(d+2),2*d+1)*(2*(d-1)+m4)
        count+=1
    r=F(d-1,d)
    assert (1+r)/(1-r)==2*d-1
    count+=1

# Independently check integrated covariance and finite-N average variance.
for d in range(2,51):
    r=F(d-1,d)
    for N in (1,2,3,5,10,40):
        time_cov=F(N)+2*sum(F(N-l)*r**l for l in range(1,N))
        direct=sum(r**abs(i-j) for i in range(N) for j in range(N))
        assert time_cov==direct
        count+=1

# Empirical tests are illustrative only, not proofs of infinite-dimensional or long-time claims.
for d,kind,seed in [(2,'sign',1927),(5,'sign',1977),(2,'sparse',2117),(5,'sparse',2167)]:
    gen=np.random.default_rng(seed)
    x=np.zeros(d)
    samples=[]
    T=260_000
    for j in range(T+10_000):
        u=gen.normal(size=d)
        u/=np.linalg.norm(u)
        if kind=='sign':
            y=1.0 if gen.integers(2)==0 else -1.0
            mu4=1.0
        else:
            r=float(gen.random())
            y=(-math.sqrt(5) if r<0.1 else (math.sqrt(5) if r>0.9 else 0.0))
            mu4=5.0
        x=x+(y-float(u@x))*u
        if j>=10_000:
            samples.append(float(x[0]))
    s=np.asarray(samples)
    var=float(np.mean(s*s))
    fourth=float(np.mean(s**4))
    lag1=float(np.mean(s[:-1]*s[1:]))
    target_fourth=3+3*(mu4-3)/(2*d+1)
    target_lag1=(d-1)/d
    assert abs(var-1)<0.085,(d,kind,var)
    assert abs(fourth-target_fourth)<0.45,(d,kind,fourth,target_fourth)
    assert abs(lag1-target_lag1)<0.085,(d,kind,lag1)
    count+=3
    print(f'd={d} noise={kind} stationary coordinate variance {var:.5f} (target 1), fourth {fourth:.5f} (target {target_fourth:.5f}), lag-one covariance {lag1:.5f} (target {target_lag1:.5f})')
print(f'PASS {count} check groups; exact rational checks plus seeded simulations')
