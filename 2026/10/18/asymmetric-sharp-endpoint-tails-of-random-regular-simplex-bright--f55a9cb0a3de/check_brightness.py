#!/usr/bin/env python3
"""Finite, reproducible numerical tests of simplex brightness endpoint formulas."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

def constants(m):
    k=m-2;p=m//2;q=m-p
    L=2*math.sqrt(p*q/m)
    D=2*math.sqrt(((m-1)//2)*((m-1+1)//2)/(m-1))
    E=2*math.sqrt((p-1)*(q+1)/m)
    delta=L-max(D,E)
    assert delta>0
    area=2*math.pi**((k+1)/2)/gamma((k+1)/2)
    N=(math.comb(m,p) if m%2==0 else 2*math.comb(m,p))
    lower=m*(m-1)*2**k*math.sqrt(m/2)/(math.factorial(k)*area)
    upper=N*math.pi**(k/2)/gamma(1+k/2)/area*(2/L)**(k/2)
    return k,L,delta,area,N,lower,upper

def cap_probability(m,t):
    k,L,delta,area,N,lower,upper=constants(m)
    assert 0<=t<=delta+1e-14
    theta=math.acos(1-t/L)
    den=quad(lambda z:math.sin(z)**(k-1),0,math.pi,epsabs=1e-12)[0]
    num=quad(lambda z:math.sin(z)**(k-1),0,theta,epsabs=1e-12)[0]
    return N*num/den

rng=np.random.default_rng(4417)
for m in [3,4,5,6,8]:
    k,L,delta,area,N,cl,cu=constants(m)
    n=300000
    x=rng.normal(size=(n,m))
    x-=x.mean(axis=1,keepdims=True)
    x/=np.linalg.norm(x,axis=1,keepdims=True)
    z=np.abs(x).sum(axis=1)
    assert np.min(z)>=math.sqrt(2)-1e-12
    assert np.max(z)<=L+1e-12
    t=min(delta*0.5,0.06)
    observed=np.mean(z>=L-t)
    expected=cap_probability(m,t)
    sd=math.sqrt(expected*(1-expected)/n)
    assert abs(observed-expected)<8*sd+0.002,(m,observed,expected)
    for h in [0.002,0.001,0.0005]:
        assert abs(cap_probability(m,h)/(cu*h**(k/2))-1)<0.012,(m,h)
    print('CHECK_TOP',m,'delta',round(delta,8),'exact',round(expected,8),'sample',round(observed,8))
assert abs(cap_probability(3,constants(3)[2])-1)<1e-12
# The complete m=3 cap formula also determines its lower endpoint expansion.
for h in [1e-3, 1e-4, 1e-5]:
    c3=constants(3)
    lower_cdf=1-cap_probability(3,c3[2]-h)
    assert abs(lower_cdf/(c3[5]*h)-1)<0.004,(h,lower_cdf)
assert abs(constants(4)[5]-2.700948948471318)<1e-10
assert abs(constants(4)[6]-1.5)<1e-12
print('REGULAR_SIMPLEX_BRIGHTNESS_TAILS_OK')
