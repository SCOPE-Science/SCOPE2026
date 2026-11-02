#!/usr/bin/env python3
"""Independent finite checks of the Gaussian renewal-reset reward envelope.
Requires Python 3.9+ standard library. Numerical checks do not replace proof.
"""
import math
import random

RANDOM = random.Random(20261025)
COUNT = 0

def check(ok, msg):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(msg)

def u(c, x):
    return c + (1-c)*(-math.expm1(-x))

def f(c, x):
    v = u(c,x)
    return (v-c)**2 / v

def j(c, x):
    return f(c, x)/(2*c)

def h(c, x):
    v = u(c,x)
    return x*(1-v)*(v+c)-v*(v-c)

def tangent(c):
    lo = max(1e-15, c*1e-10)
    hi = 4.0
    check(h(c,lo)>0 and h(c,hi)<0, 'root bracket')
    for k in range(90):
        mid = .5*(lo+hi)
        if h(c,mid)>0: lo=mid
        else: hi=mid
    return .5*(lo+hi)

def env_f(c, m, star=None):
    z = tangent(c) if star is None else star
    return f(c,z)*m/z if m <= z else f(c,m)

# Direct Gaussian KL integral of two density functions for arbitrary variance ratio.
def direct_jeffreys(c,v):
    def norm_pdf(t,variance):
        return math.exp(-t*t/(2*variance))/math.sqrt(2*math.pi*variance)
    l = 12*max(math.sqrt(c),math.sqrt(v))
    n = 8000
    dx=2*l/n
    tot=0.
    for k in range(n+1):
        x=-l+k*dx
        p=norm_pdf(x,c)
        q=norm_pdf(x,v)
        val=(p-q)*math.log(p/q) if p>0 and q>0 else 0.
        tot+=(1 if k==0 or k==n else 4 if k%2 else 2)*val
    return tot*dx/3

for c in [0.1, 0.25, 0.5, 0.8]:
    for x in [.01, .15, .5, 1.3]:
        check(abs(direct_jeffreys(c,u(c,x))-j(c,x))<2e-9,'Gaussian KL')

for c in [1e-6,1e-4,.003,.02,.1,.2,.5,.8,.96,.999]:
    z=tangent(c)
    v=u(c,z)
    check(abs(z*(1-v)*(v+c)-v*(v-c)) < 5e-10, 'tangent equality')
    check(z>0, 'positive tangent')
    # Envelope must dominate everywhere and be tangent at z.
    for k in range(1,301):
        x=.001 + 9*k/301
        check(f(c,x) <= f(c,z)*x/z + 2e-10, 'supporting line')
        val=env_f(c,x,z)
        check(val+2e-10>=f(c,x), 'concave envelope majorant')
    # Numerical samples of random waiting laws; compare expected reward to envelope.
    for k in range(100):
        knots=[math.exp(RANDOM.uniform(-7,2.4)) for _ in range(5)]
        weights=[RANDOM.expovariate(1) for _ in knots]
        total=sum(weights)
        weights=[q/total for q in weights]
        m=sum(q*x for q,x in zip(weights,knots))
        reward=sum(q*f(c,x) for q,x in zip(weights,knots))
        check(reward <= env_f(c,m,z) + 4e-11, 'renewal rate bound')
    # For below threshold, a two-point positive law approaches the bound.
    m=.55*z
    for eps in [1e-2*z,1e-3*z,1e-4*z]:
        p=(z-m)/(z-eps)
        reward=p*f(c,eps)+(1-p)*f(c,z)
        check(reward <= env_f(c,m,z)+1e-10, 'two-point bound')
    eps=1e-5*z
    p=(z-m)/(z-eps)
    reward=p*f(c,eps)+(1-p)*f(c,z)
    check(abs(reward-env_f(c,m,z)) < 3e-4*env_f(c,m,z),'two-point sharpness')
    # Above threshold the deterministic law is exact.
    m=1.7*z
    check(abs(env_f(c,m,z)-f(c,m))<1e-12,'deterministic optimizer')

# Check unique inflection via strict decrease of the cubic in variance u.
for c in [.01,.2,.5,.9]:
    vals=[2*c*c-c*c*v-v**3 for v in [c+(1-c)*q/100 for q in range(101)]]
    check(vals[0]>0 and vals[-1]<0,'inflection crossing')
    check(all(vals[k]>vals[k+1] for k in range(100)),'unique inflection')

# Small-reset-width asymptotics. x_* = sqrt(2c) - c/3 + O(c^(3/2)).
for c in [1e-4,1e-6,1e-8]:
    z=tangent(c)
    check(abs(z/math.sqrt(2*c)-1)<2*math.sqrt(c),'cold leading scale')
    check(abs((z-math.sqrt(2*c))/c+1/3)<2*math.sqrt(c),'cold correction')
    peak=f(c,z)/(c*z)
    leading=1/c-math.sqrt(2/c)-1/6
    check(abs(peak-leading)<2*math.sqrt(c),'cold peak expansion')

# Warm reset-width endpoint: e^z = 2z+1.
a,b=1.,2.
for k in range(90):
    mid=(a+b)/2
    if math.exp(mid)>2*mid+1: b=mid
    else:a=mid
warm=(a+b)/2
check(abs(math.exp(warm)-2*warm-1)<1e-12,'warm root')
for c in [.99,.999,.9999]:
    check(abs(tangent(c)-warm)<3*(1-c),'warm limit')
print('PASS:',COUNT,'finite assertions; tangent, envelope, KL, asymptotic and renewal checks.')
