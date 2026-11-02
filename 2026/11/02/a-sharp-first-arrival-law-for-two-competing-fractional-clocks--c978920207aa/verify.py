#!/usr/bin/env python3
"""Reproducibility checks for an exact fair-clock first-arrival theorem.
Numerical checks supplement the stated analytic proof; they do not establish limits.
"""
import math
from collections import defaultdict
import numpy as np
from scipy.integrate import quad
from scipy.special import expit, erfcx, roots_legendre

checks=0

def test(ok,desc):
    global checks
    assert ok,desc
    checks+=1


def lograte_density(y,a):
    if a==1:raise ValueError('a=1 has point mass at zero')
    v=abs(a*y)
    if v>40: return (math.sin(math.pi*a)/math.pi)*math.exp(-v)
    return math.sin(math.pi*a)/(2*math.pi*(math.cosh(a*y)+math.cos(math.pi*a)))

# The nontrivial spectral density is a probability density and even in log rate.
for a in [0.2,0.35,0.5,0.75,0.91]:
    mass=quad(lambda y:lograte_density(y,a),-400,400,epsabs=1e-11,limit=500)[0]
    test(abs(mass-1)<1e-10,f'log rate mass alpha={a}, {mass}')
    for y in [0.1,0.7,2,6,11]:
        test(abs(lograte_density(y,a)-lograte_density(-y,a))<1e-14,'rate inversion symmetry')
    for u in [0.23,0.8,2.2]:
        val=quad(lambda y:lograte_density(y,a)/(u+math.exp(y)),-400,400,epsabs=1e-11,limit=500)[0]
        true=u**(a-1)/(1+u**a)
        test(abs(val-true)<3e-9,f'Stieltjes check {a},{u},{val},{true}')

# A separate finite-dimensional Gaussian quadrature for the race probability.
# Its joint distribution is a product of nonidentical symmetric log-rate densities.
node,w=roots_legendre(900)
y=np.tan(np.pi*node/2); weights=(np.pi/2)*w*(1+y*y)
for a,b in [(0.2,0.8),(0.35,0.71),(0.55,0.9),(0.42,0.42)]:
    x=np.array([lograte_density(float(z),a) for z in y])*weights
    v=np.array([lograte_density(float(z),b) for z in y])*weights
    p=np.sum(x[:,None]*v[None,:]*expit(y[:,None]-y[None,:]))
    test(abs(p-0.5)<2e-9,f'fair clocks alpha={a},beta={b},p={p}')
    high=np.sum(x[:,None]*v[None,:]*expit(math.log(2)+y[:,None]-y[None,:]))
    low=np.sum(x[:,None]*v[None,:]*expit(-math.log(2)+y[:,None]-y[None,:]))
    test(high>0.5 and low<0.5 and abs(high+low-1)<3e-9,f'unequal clock scale order {a},{b}')

# An independent embedded random-walk dynamic program for the event count N.
# At each event: reset to zero 1/2, step right 1/4, left 1/4; +1 is absorbing.
states={0:1.0}
survivals=[1.0]
masses=[]
for step in range(850):
    new=defaultdict(float);hit=0.
    for x,prob in states.items():
        new[0]+=0.5*prob
        if x==0:hit+=0.25*prob
        else:new[x+1]+=0.25*prob
        new[x-1]+=0.25*prob
    states=new
    masses.append(hit)
    survivals.append(sum(states.values()))
    test(abs(survivals[-2]-hit-survivals[-1])<1e-11,'mass conservation in absorption chain')
    if step>20 and step%30==0:
        test(survivals[-1] <= (7/8)**(step//2)+1e-10,'two-event survival tail bound')

r=2-math.sqrt(3)
en=2*(1+math.sqrt(3))
test(abs((1-r)/(0.5*r)-en)<1e-13,'embedded expected event count identity')
test(abs(sum(survivals[:-1])-en)<1e-10,'dynamic event-count expectation')
test(abs(sum(masses)-1)<1e-10,'sure first arrival')

# Continuous-time check in exactly exponential-clock boundary alpha=beta=1:
# conditional event holding times are iid exponential with rate 2.
for u in [0.05,0.23,0.7,1.8]:
    z=2/(2+u)
    empirical=sum(p*z**(i+1) for i,p in enumerate(masses))
    a=1/(2+u);b=a
    ru=(1-math.sqrt(1-a*a))/a
    closed=ru*(1-a)/(1-a-b*(1-ru))
    test(abs(empirical-closed)<1e-10,f'Laplace transform u={u}')
test(abs(en/2-(1+math.sqrt(3)))<1e-13,'exponential-clock mean')

# The analytic alpha=beta=1/2 survival is erfcx(sqrt(t)). The min-clock
# tail has exponent one and exact coefficient 1/pi.
for t in [100,1000,10000,100000]:
    surv=erfcx(math.sqrt(t))
    normalized=t*surv*surv
    test(abs(normalized-1/math.pi)<0.5/t,'critical min-clock tail constant')

print(f'{checks} checks passed: spectral inversion, clock fairness, event-count dynamics, transform, tail diagnostics')
