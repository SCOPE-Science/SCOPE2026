#!/usr/bin/env python3
"""Independent numerical checks of radial mean exit identities; not a proof.
Requires numpy and scipy. No random seeds or external data.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import dawsn, hyp1f1, exp1
from scipy.optimize import brentq

KAPPA=1.0
R0=0.5
R=1.0
COUNT=0

def check(cond, message):
    global COUNT
    COUNT += 1
    if not bool(cond):
        raise AssertionError(message)

def h(d,z):
    nu=d/2
    if d==1:
        return 2*math.sqrt(z)*dawsn(math.sqrt(z))
    return (z/nu)*hyp1f1(1,nu+1,-z)

def h_direct(d,z):
    nu=d/2
    return z*quad(lambda t: t**(nu-1)*math.exp(-z*(1-t)),0,1,
                  epsabs=2e-13,epsrel=2e-13)[0]

def mean_exit(d,D,r=R0,R=R,kappa=KAPPA):
    return quad(lambda s:h(d,kappa*s*s/(2*D))/(kappa*s),r,R,
                epsabs=3e-12,epsrel=3e-12)[0]

def mean_exit_direct(d,D,r=R0,R=R,kappa=KAPPA):
    def speed(s):
        z=kappa*s*s/(2*D)
        inner=quad(lambda t:t**(d-1)*math.exp(-z*(1-(t/s)**2)),0,s,
                   epsabs=2e-13,epsrel=2e-13)[0]
        return inner/(D*s**(d-1))
    return quad(speed,r,R,epsabs=3e-12,epsrel=3e-12)[0]

for d in range(1,9):
    for z in (0.001,0.03,0.3,1.,2.,6.,20.):
        lhs=h(d,z)
        rhs=h_direct(d,z)
        check(abs(lhs-rhs)<2e-9*(1+abs(rhs)),f'kernel identity d={d} z={z}')

for d in range(1,7):
    for D in (0.04,0.12,0.4,2.0):
        a=mean_exit(d,D)
        b=mean_exit_direct(d,D)
        check(abs(a-b)<1e-8*(1+abs(b)),f'generator-integral identity d={d} D={D}')

for D in (0.025,0.05,0.1,0.5,2.0):
    z0=KAPPA*R0*R0/(2*D)
    z1=KAPPA*R*R/(2*D)
    closed=math.log(R/R0)/KAPPA-(exp1(z0)-exp1(z1))/(2*KAPPA)
    check(abs(closed-mean_exit(2,D))<1e-10,'dimension-two formula')

for d in range(2,9):
    values=[mean_exit(d,D) for D in (0.005,0.01,0.025,0.08,0.15,0.4,1,4,15)]
    for a,b in zip(values,values[1:]):
        check(a>b,f'all-noise monotonic sample d={d}')
    check(all(0<v<math.log(2) for v in values),f'domain bounds d={d}')

peak_z=brentq(lambda z:1-h(1,z)+h(1,z)/(2*z),1,8)
k=(R/R0)**2
a=brentq(lambda x:h(1,k*x)-h(1,x),peak_z/k,peak_z,xtol=1e-14)
opt=KAPPA*R0**2/(2*a)
peak=mean_exit(1,opt)
check(peak>math.log(2),'strict stochastic inertia')
check(1e-12<abs(h(1,k*a)-h(1,a))<1e-10 or abs(h(1,k*a)-h(1,a))<1e-12,'stationarity equation')
for mult in (0.005,0.01,0.1,0.4,0.8,0.99,1.01,1.2,2,10,100):
    check(mean_exit(1,opt*mult)<peak+1e-11,f'optimum side factor={mult}')
for d in range(1,8):
    for D in (0.05,0.3):
        for s in (0.27,0.4,0.6,0.8):
            dx=2e-4
            u=lambda x:mean_exit(d,D,x,R)
            du=(u(s+dx)-u(s-dx))/(2*dx)
            ddu=(u(s+dx)-2*u(s)+u(s-dx))/(dx*dx)
            lhs=D*(ddu+(d-1)*du/s)+KAPPA*s*du
            check(abs(lhs+1)<3e-4,f'backward equation d={d},D={D},s={s}, residual {lhs+1}')
print('all',COUNT,'assertions passed')
print('maximum kernel at z =',peak_z)
print('one-dimensional a*, D*, expected exit =',a,opt,peak)
print('zero-noise expectation =',math.log(2))
