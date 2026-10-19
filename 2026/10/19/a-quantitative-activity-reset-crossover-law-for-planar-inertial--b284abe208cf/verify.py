#!/usr/bin/env python3
"""Independent finite-parameter and limiting-moment checks for an inertial-reset law.

Python 3 standard library only. The theorems require the separate analytic proof.
"""
from fractions import Fraction as F
from math import exp, factorial, isclose, sqrt
import random

N = 0

def check(test, label):
    global N
    N += 1
    if not test:
        raise AssertionError(label)

def exact_passive_msd(M, r):
    return 4 * (F(1, 1) / r - 2*M*(1 - r/(r+1/M)) + M/F(2)*(1-r/(r+2/M)))

def paper_msd(M,r,p):
    return (2/(r*(1+M*r)*(2+M*r))) * (4+p*p*(2+2*M+3*M*r)/((r+1)*(1+M+M*r)))

def finite_mean(M,r,p):
    return p/((1+M*r)*(1+r))

# The passive second moment is derived by integrating the Gaussian propagator
# over the exact exponential age law; this must agree with the full model's
# independent moment recursion at zero activity.
for M in (F(1,3),F(1),F(3,2),F(4),F(9,5)):
    for r in (F(1,5),F(1),F(2),F(7),F(29)):
        check(exact_passive_msd(M,r)==paper_msd(M,r,F(0)), 'exact passive MSD')

# Exact factorial moments of E~Exp(1).  Independent expansions for the
# limit mean, covariance and longitudinal/mixed third central moments.
for alpha in (F(0),F(1,4),F(1),F(5,3),F(7)):
    mean = alpha*F(factorial(2),2)
    active_var = alpha**2/F(4)*(F(factorial(4))-F(factorial(2))**2)
    noise_var = F(2,3)*factorial(3)
    check(mean == alpha, 'mean')
    check(active_var+noise_var == 4+5*alpha**2, 'longitudinal variance')
    check(noise_var==4, 'transverse variance')
    ex2=alpha**2/F(4)*factorial(4)+2*noise_var
    check(ex2==8+6*alpha**2,'mean square displacement')
    k3_active=alpha**3/F(8)*(factorial(6)-3*factorial(2)*factorial(4)+2*factorial(2)**3)
    k3_cross=alpha*(factorial(5)-factorial(2)*factorial(3))
    check(k3_active+k3_cross==74*alpha**3+108*alpha,'longitudinal third cumulant')
    check(k3_cross/F(3)==36*alpha,'mixed third cumulant')

# Source finite-r exact moment formulas agree with the proposed crossover
# coefficients and with a strictly different large-activity scaling.
for M in (F(1,2), F(2), F(7,3)):
    for alpha in (0.,0.4,1.,2.):
        for r in (100,1000,10000,100000):
            a=float(M); p=alpha*sqrt(r)
            finite_scaled_mean=(a*r**1.5)*finite_mean(a,r,p)
            finite_scaled_msd=a*a*r**3*paper_msd(a,r,p)
            target=8+6*alpha**2
            check(abs(finite_scaled_mean-alpha)< 6*(1+alpha)/r,'scaled mean asymptotics')
            check(abs(finite_scaled_msd-target)< 60*(1+alpha**2)/r,'scaled MSD asymptotics')
for M in (0.7,1.7,4.0):
    for r in (10000.,100000.):
        p=r
        active_scaled_mean=M*r*r/p*finite_mean(M,r,p)
        active_scaled_msd=(M*r*r/p)**2*paper_msd(M,r,p)
        check(abs(active_scaled_mean-1)<10/r,'supercritical mean')
        check(abs(active_scaled_msd-6)<100/r,'supercritical second moment')

# A second route: approximate the original angular diffusion over a whole
# reset cycle, retaining exact Gaussian thermal increments conditional on age.
# Samples are only consistency checks, never a proof of the weak limit.
rng=random.Random(20261017)
M=1.6; r=170.; alpha=1.1; p=alpha*sqrt(r)
sumx=sumsq=0.
nsample=14000
nsteps=32
for i in range(nsample):
    s=rng.expovariate(1.)
    t=s/r
    dt=t/nsteps
    theta=0.; ax=ay=0.
    for j in range(nsteps):
        # Brownian angular midpoint update with the correct covariance.
        theta_mid=theta+rng.gauss(0,sqrt(dt))
        theta=theta_mid+rng.gauss(0,sqrt(dt))
        q=(j+0.5)*dt
        factor=-__import__('math').expm1(-(t-q)/M)
        ax+=factor*__import__('math').cos(theta_mid)*dt
        ay+=factor*__import__('math').sin(theta_mid)*dt
    thermal_var=2*(t-2*M*(-__import__('math').expm1(-t/M))+(M/2)*(-__import__('math').expm1(-2*t/M)))
    sig=sqrt(max(thermal_var,0.))
    x=(p*ax+sig*rng.gauss(0,1))*M*r**1.5
    y=(p*ay+sig*rng.gauss(0,1))*M*r**1.5
    sumx+=x; sumsq+=x*x+y*y
check(abs(sumx/nsample -M*r**1.5*finite_mean(M,r,p))<0.22, 'finite stochastic mean')
check(abs(sumsq/nsample -M*M*r**3*paper_msd(M,r,p))<1.9,'finite stochastic MSD')

# Bounds derived from |u(theta)-u(0)|<=|theta| and
# 0<=w-Mr(1-exp(-w/(Mr)))<=w^2/(2Mr): checked on a dense grid.
for M in (0.25,1.,4.):
    for r in (1.,3.,25.,100.):
        for j in range(1,251):
            w=j/17.
            h=M*r*(-__import__('math').expm1(-w/(M*r)))
            check(-1e-12<=w-h<=w*w/(2*M*r)+1e-12,'deterministic propagator bound')
print('PASS',N,'checks')
