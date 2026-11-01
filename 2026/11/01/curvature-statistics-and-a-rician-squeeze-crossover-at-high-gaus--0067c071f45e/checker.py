#!/usr/bin/env python3
"""Supplementary numerical and algebraic tests for Gaussian spectrogram peak-shape crossover.

The mathematical result rests on the proof; finite checks do not certify infinite limits.
"""
import math
import random

RNG = random.Random(173281)
checks = 0

def approx(x, y, tol=1.e-8):
    global checks
    checks += 1
    assert abs(x-y) < tol, (x,y,tol)

def simpson(f,a,b,n=12000):
    assert n%2 == 0
    h=(b-a)/n
    return h/3 * (f(a)+f(b)+4*sum(f(a+(2*j-1)*h) for j in range(1,n//2+1)) +2*sum(f(a+2*j*h) for j in range(1,n//2)))

def pdf_u(u):
    return 3*(1-u)/(1+u/2)**3

approx(simpson(pdf_u,0,1),1.,1.e-10)
for u in [0.,.05,.2,.4,.7,.9,.97]:
    cdf_tail=(1-u)**2/(1+u/2)**2
    approx(simpson(pdf_u,u,1),cdf_tail,2.e-9)
for e in [1., 1.2, 1.7, 2., 3., 10., 100.]:
    u=((e-1)/(e+1))**2
    tail=64*e**2/(3*e**2+2*e+3)**2
    approx((1-u)**2/(1+u/2)**2,tail,1.e-12)
for alpha in [0.,.125,.5,1.,3.]:
    lhs=simpson(lambda w:(w**2/2)*math.exp(-(1+alpha)*w),0,100.,20000)
    approx(lhs,(1+alpha)**-3,1.e-7)

# Check Hessian shape from the exact real quadratic expansion for randomly chosen jets.
def condition_ratio(q,phi,a):
    x=q*math.cos(phi)
    y=q*math.sin(phi)
    m11=math.exp(2*a)*(1-x)
    m22=math.exp(-2*a)*(1+x)
    m12=y
    disc=math.hypot(m11-m22,2*m12)
    return (m11+m22+disc)/(m11+m22-disc)

for _ in range(40):
    q=.9*RNG.random()
    phi=2*math.pi*RNG.random()
    approx(condition_ratio(q,phi,0),(1+q)/(1-q),2.e-13)

# At a height s, the Palm density of t=|a_2|^2 is proportional to
# (1-2t/s)exp(-t), restricted to 0<t<s/2.
def sample_t_conditional(s):
    while True:
        t=RNG.expovariate(1)
        if t<s/2 and RNG.random()<=1-2*t/s:
            return t

# Uniform-in-sample error between exact scaled eigenratio and Rice limit.
for eta in [-2.,-.7,0.,.5,1.4]:
    for h in [1.e4, 1.e6]:
        worst=0.
        for _ in range(1600):
            t=sample_t_conditional(h)
            phi=2*math.pi*RNG.random()
            q=math.sqrt(2*t/h)
            x=math.sqrt(h)*q*math.cos(phi)
            y=math.sqrt(h)*q*math.sin(phi)
            limit=2*math.hypot(2*eta-x,y)
            actual=math.sqrt(h)*(condition_ratio(q,phi,eta/math.sqrt(h))-1)
            worst=max(worst,abs(actual-limit)/(1+limit)**2)
        checks+=1
        assert worst < (.015 if h==1.e4 else .0015), (eta,h,worst)

# Exact covariance normalization: conditioned on one zero and a local maximum,
# Kac-Rice mass is E[(s-2t)_+] = 1/3.
val=simpson(lambda t:math.exp(-3*t),0.,30.)
approx(val,1./3.,1.e-8)

# Independently recover the Palm eccentricity tails using the unweighted
# Gaussian coefficient law with Kac-Rice Jacobian importance weights.
tails=[.1,.4,.8]
num=[0.]*len(tails)
den=0.
for _ in range(250000):
    s=RNG.expovariate(1)
    t=RNG.expovariate(1)
    wt=max(s-2*t,0.)
    den+=wt
    if wt:
        u=2*t/s
        for j,cut in enumerate(tails):
            if u>cut:num[j]+=wt
for j,cut in enumerate(tails):
    approx(num[j]/den,(1-cut)**2/(1+cut/2)**2,.015)

# Isotropic high-threshold Hessian condition number has Rayleigh tails.
s=8000.
N=20000
sample=[]
for _ in range(N):
    t=sample_t_conditional(s)
    q=math.sqrt(2*t/s)
    e=(1+q)/(1-q)
    sample.append(math.sqrt(s)*(e-1))
for x in [1.,2.,3.,4.,5.]:
    tail=sum(y>x for y in sample)/N
    approx(tail,math.exp(-x*x/8),.020)
print(f'PASS: {checks} supplementary assertions including independent weighted samples')
