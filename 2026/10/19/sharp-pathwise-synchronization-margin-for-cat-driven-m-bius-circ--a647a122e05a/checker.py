"""Reproducibility diagnostics for a robust Möbius-fiber contraction theorem.
All assertions are finite consistency checks; the infinite-time statements use the written proof.
"""
import math
import random

pi=math.pi
rng=random.Random(29046)
checks=0

def phi(x,eps):
    return math.atan2(eps*math.sin(2*pi*x),1+eps*math.cos(2*pi*x))/pi

def fiber(x,d,eps):
    return x+d-phi(x,eps)

def derivative(x,eps):
    return (1-eps**2)/(1+2*eps*math.cos(2*pi*x)+eps**2)

def params(eps,q):
    v=math.asin(math.sin(pi*q)/eps)
    p=(pi*q+v)/(2*pi)
    r=(pi*q+pi-v)/(2*pi)
    K=math.exp(-2*math.acosh(math.cos(pi*q)/math.sqrt(1-eps**2)))
    return p,r,K

for eps in [.05,.2,.4,.8,.975]:
    delta=math.asin(eps)/pi
    for frac in [.005,.05,.3,.75,.985,.999]:
        q=frac*delta
        p,r,K=params(eps,q)
        assert 0<p<r<.5 and p>q
        for x in [p,r,-p,-r]:
            assert abs(abs(phi(x,eps))-q)<1e-12
            checks+=1
        assert abs(derivative(p,eps)-K)<5e-11
        assert abs(derivative(r,eps)*K-1)<5e-11
        checks+=2
        for _ in range(250):
            d=rng.uniform(-q,q)
            x=rng.uniform(-p,p)
            assert -p-1e-11<=fiber(x,d,eps)<=p+1e-11
            assert derivative(x,eps)<=K+1e-11
            y=rng.uniform(r,1-r)
            assert derivative(y,eps)>=1/K-1e-10
            assert fiber(r,d,eps)<=r+1e-11
            assert fiber(1-r,d,eps)>=1-r-1e-11
            checks+=5

for eps in [.2,.4,.8]:
    delta=math.asin(eps)/pi
    constant=2*math.sqrt(2*pi*eps/math.sqrt(1-eps**2))
    for eta in [1e-3,1e-4,1e-5,1e-6]:
        if eta>=delta: continue
        K=params(eps,delta-eta)[2]
        ratio=-math.log(K)/math.sqrt(eta)
        assert abs(ratio-constant)<25*eta
        checks+=1

for eps in [.2,.4,.8]:
    delta=math.asin(eps)/pi
    q=delta*.5
    p,r,K=params(eps,q)
    # Two starting positions inside common absorbing strip contract for all driving sequences.
    x,y=-p,p
    for n in range(150):
        d=rng.uniform(-q,q)
        x,y=fiber(x,d,eps),fiber(y,d,eps)
        assert -p-1e-12<=x<=p+1e-12
        assert -p-1e-12<=y<=p+1e-12
        assert abs(y-x)<=(2*p)*(K**(n+1))+5e-15
        checks+=3

print('PASS',checks,'finite consistency checks')
