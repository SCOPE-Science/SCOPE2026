#!/usr/bin/env python3
"""Supplementary exact and numerical checks for critical Cauchy-mixture Gabor bounds.

The universal theorem is proved analytically in RESULT.md; finite checks are not a proof.
"""
from fractions import Fraction as F
from math import exp, pi, log, sqrt, cos, sin
import random

checks = 0

def verify(statement, label):
    global checks
    if not statement:
        raise AssertionError(label)
    checks += 1

def D(q, x):
    return 1-2*q*x+q*q

def R(q, x):
    return (1-q*x)/D(q,x)

def cross(q, r, x):
    return (1-(q+r)*x+q*r)/(D(q,x)*D(r,x))

def energy(qs, bs, x):
    return sum((bi*bj*cross(qi,qj,x) for qi,bi in zip(qs,bs)
                for qj,bj in zip(qs,bs)),F(0))

rng = random.Random(1729)
for m in range(1,7):
    for trial in range(15):
        qs = [F(rng.randint(1,10),rng.randint(12,27)) for _ in range(m)]
        bs = [F(rng.randint(1,8),rng.randint(1,8)) for _ in range(m)]
        xs = [F(k,12) for k in range(-12,13)]
        values = [energy(qs,bs,x) for x in xs]
        for i,x in enumerate(xs):
            for q in qs:
                for r in qs:
                    verify(cross(q,r,x) == (R(q,x)+R(r,x)-1)/(1-q*r),
                           'two-pole partial fraction identity')
                    verify(cross(q,r,x)>0,'positive cross term')
            if i:
                verify(values[i]>values[i-1],'strict spatial monotonicity')
        verify(values[0]==sum((b/(1+q) for b,q in zip(bs,qs)),F(0))**2,
               'left extreme')
        verify(values[-1]==sum((b/(1-q) for b,q in zip(bs,qs)),F(0))**2,
               'right extreme')
        lower_weights = [b*q for b,q in zip(bs,qs)]
        upper_weights = list(bs)
        for x in xs:
            verify(energy(qs,lower_weights,x)<energy(qs,upper_weights,x),
                   'frequency endpoint strict monotonicity')
        verify(energy(qs,lower_weights,F(-1)) ==
               sum((b*q/(1+q) for b,q in zip(bs,qs)),F(0))**2,
               'two-dimensional minimum')
        verify(energy(qs,upper_weights,F(1)) ==
               sum((b/(1-q) for b,q in zip(bs,qs)),F(0))**2,
               'two-dimensional maximum')

# Critical condition-number barrier and equality at the unique one-pole width.
rstar = 1+sqrt(2)
kstar = 17+12*sqrt(2)
verify(abs((rstar*(rstar+1)/(rstar-1))**2-kstar)<1e-12,'sharp constant')
for _ in range(3000):
    Rvals=[exp(rng.uniform(.03,4)) for _ in range(rng.randrange(1,9))]
    weights=[exp(rng.uniform(-4,4)) for _ in Rvals]
    L=sum(a/(r+1) for a,r in zip(weights,Rvals))
    U=sum(a*r/(r-1) for a,r in zip(weights,Rvals))
    verify((U/L)**2 >= kstar - 2e-12,'mixture barrier')

# Direct Zak multiplier comparison at interior points for a two-pole mixture.
for alpha in [0.75,1.0,1.6]:
    ws=[0.15,0.42]; mass=[0.7,1.1]
    qq=[exp(-2*pi*w/alpha) for w in ws]
    A=(4*pi*pi/alpha)*sum(a*q/(1+q) for a,q in zip(mass,qq))**2
    B=(4*pi*pi/alpha)*sum(a/(1-q) for a,q in zip(mass,qq))**2
    verify(0<A<B,'strict frame bounds')
    for _ in range(1000):
        u=rng.random(); theta=2*pi*rng.random()
        total=sum(a*exp(-2*pi*w*(1-u)/alpha)/(1-q*complex(cos(theta),sin(theta)))
                  for a,w,q in zip(mass,ws,qq))
        lam=4*pi*pi/alpha*abs(total)**2
        verify(A-1e-12 <= lam <= B+1e-12,'direct Zak bound')

print(f'PASS: {checks} supplementary assertions; exact rational identities and sampled fibers.')
print(f'Sharp barrier B/A = {kstar:.14f}; optimal w/alpha = {log(rstar)/(2*pi):.14f}.')
