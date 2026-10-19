"""Numerical consistency tests for a renewing Brownian-force harmonic filter.
Run with Python 3 standard library: python verify.py
All infinite-domain statements are proved analytically in RESULT.md.
"""
import math
import random

CHECKS = 0

def close(x, y, atol=1e-9, rtol=1e-9):
    global CHECKS
    assert math.isfinite(x) and math.isfinite(y), (x, y)
    assert abs(x-y) <= atol+rtol*max(abs(x),abs(y)), (x, y)
    CHECKS += 1

def simpson(f, lo, hi, parts=2000):
    assert parts > 0 and parts % 2 == 0
    h=(hi-lo)/parts
    return h/3*(f(lo)+f(hi)+4*sum(f(lo+i*h) for i in range(1,parts,2))
                +2*sum(f(lo+i*h) for i in range(2,parts-1,2)))

def F(t, mu):
    return t*t/mu-2*t/mu**2-2*math.expm1(-mu*t)/mu**3

def two_atoms(m, s, a):
    v=s-m*m
    assert 0<a<m and v>0
    b=m+v/(m-a)
    q=(m-a)/(b-a)
    return [(a,1-q),(b,q)]

def mixture_moment(mix, k):
    return sum(p*t**k for t,p in mix)

def mixture_exp(mix, mu):
    return sum(p*math.exp(-mu*t) for t,p in mix)

def variance_exact(mix, D, mu):
    m=mixture_moment(mix,1)
    return D/(m*mu)*sum(p*F(t,mu) for t,p in mix)

def variance_transform(mix,D,mu):
    m=mixture_moment(mix,1)
    s=mixture_moment(mix,2)
    ell=mixture_exp(mix,mu)
    return D/(m*mu)*(s/mu-2*m/mu**2+2*(1-ell)/mu**3)

def envelope(m,s,D,mu):
    low=D/(m*mu)*(s/mu-2*m/mu**2+2*m*m/(s*mu**3)*(-math.expm1(-mu*s/m)))
    high=D/(m*mu)*(s/mu-2*m/mu**2-2*math.expm1(-mu*m)/mu**3)
    return low,high

def covariance(mix,D,h):
    m=mixture_moment(mix,1)
    return D/m*sum(p*max(t-h,0)**2 for t,p in mix)

# Independent renewal-covariance convolution and moment-transform routes.
rng=random.Random(17495)
for _ in range(45):
    mu=0.45+2*rng.random()
    D=0.45+2*rng.random()
    m=0.75+1.5*rng.random()
    s=m*m*(1.1+2.5*rng.random())
    a=m*(0.03+0.93*rng.random())
    mix=two_atoms(m,s,a)
    close(sum(p for _,p in mix),1)
    close(mixture_moment(mix,1),m)
    close(mixture_moment(mix,2),s)
    direct=variance_exact(mix,D,mu)
    close(direct,variance_transform(mix,D,mu),atol=2e-11)
    low,high=envelope(m,s,D,mu)
    assert low<direct<high, (low,direct,high)
    CHECKS+=1
    tmax=max(t for t,_ in mix)
    independent=simpson(lambda h:math.exp(-mu*h)*covariance(mix,D,h)/mu,
                        0,tmax,parts=2000)
    close(direct,independent,atol=2e-7,rtol=2e-7)

# Endpoints are approached by valid strictly positive two-point laws.
for m,s,D,mu in [(1,2,1,1),(.7,2.1,2.,.9),(3,12,1.2,1.4)]:
    low,high=envelope(m,s,D,mu)
    close(variance_exact(two_atoms(m,s,m*1e-7),D,mu),low,atol=8e-6,rtol=8e-6)
    close(variance_exact(two_atoms(m,s,m*(1-1e-6)),D,mu),high,atol=8e-6,rtol=8e-6)

# Laplace/variance formula specialized to exponential resets.
for r,mu,D in [(1.,1.,1.),(.4,1.7,2.),(3.,.6,.8)]:
    m=1/r;s=2/r**2;ell=r/(r+mu)
    physical=D/(m*mu)*(s/mu-2*m/mu**2+2*(1-ell)/mu**3)
    close(physical,2*D/(r*mu*(r+mu)))
    a,b=envelope(m,s,D,mu)
    assert a<physical<b
    CHECKS+=1

# Strictly stationary periodic protocol: uniform phase versus reset-epoch moments.
for m,mu,D in [(1,1,1),(.7,1.8,2),(.5,.3,.8)]:
    q=math.exp(-mu*m)
    v0=D/mu**3*(2*mu*m-3+4*q-q*q)/(1-q*q)
    def within_phase(age):
        ea=math.exp(-mu*age)
        v_cycle=2*D/mu**2*(age-2*(-math.expm1(-mu*age))/mu+(1-ea*ea)/(2*mu))
        return math.exp(-2*mu*age)*v0+v_cycle
    time_averaged=simpson(within_phase,0,m,parts=4000)/m
    close(time_averaged,D/(m*mu)*F(m,mu),atol=1e-10)

# Fixed-mean deterministic reset minimizes filtered variance (convexity of F).
for _ in range(25):
    m=0.5+rng.random()*2
    mu=0.5+rng.random()*2
    D=0.5+rng.random()*2
    q=.02+.95*rng.random()
    a=q*m
    b=m+(m-a)*rng.uniform(.1,4)
    p=(b-m)/(b-a)
    current=variance_exact([(a,p),(b,1-p)],D,mu)
    minimum=D/(m*mu)*F(m,mu)
    assert current>minimum
    CHECKS+=1

print(f'PASS: {CHECKS} exact-identity, quadrature and inequality checks')
