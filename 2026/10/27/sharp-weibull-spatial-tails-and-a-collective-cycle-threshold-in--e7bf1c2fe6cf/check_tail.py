#!/usr/bin/env python3
"""Reproducible finite checks for Weibull-switched harmonic diffusion tails.

Requires Python, NumPy and SciPy. Finite checks do not establish asymptotic theorems.
"""
import math
import numpy as np
from scipy.special import erf, gammaln, logsumexp
from scipy.optimize import minimize_scalar

checks=0

def verify(condition, label):
    global checks
    assert bool(condition), label
    checks += 1


def a_weight(p, c, theta):
    if p<=1:
        return theta**(-p)
    q=p/(p-1)
    return theta**(-p) * (1-c**q)**(p-1)


def tail_k(p,c,theta,D):
    return (p+1) * a_weight(p,c,theta)**(1/(p+1)) / (4*D*p)**(p/(p+1))


def mean_off_age(p,theta):
    # Equilibrium renewal age, E[A] = E[T^2]/(2 E[T]).
    return theta*math.gamma(1+2/p)/(2*math.gamma(1+1/p))


def log_mA_rayleigh(s,theta):
    z=theta*s/2
    return z*z+math.log1p(erf(z))


def log_mT_rayleigh(s,theta):
    mu=theta*math.sqrt(math.pi)/2
    return float(np.logaddexp(0, math.log(s*mu)+log_mA_rayleigh(s,theta))) if s>0 else 0.0


def log_mW_off_rayleigh(s,theta,c):
    out=log_mA_rayleigh(s,theta)
    z=s*c
    while z>1e-12:
        out+=log_mT_rayleigh(z,theta)
        z*=c
    return out


def simulate(p,theta,kappa,tau,D,rep=160000,seed=20261020):
    rng=np.random.default_rng(seed)
    c=math.exp(-2*kappa*tau)
    mu=theta*math.gamma(1+1/p)
    off_prob=mu/(mu+tau)
    is_off=rng.random(rep)<off_prob
    # T_j are independently Weibull; the stationary birth variance is a geometric sum.
    sums=np.zeros(rep)
    coeff=c
    for j in range(65):
        t=theta*rng.weibull(p,rep)
        sums+=coeff*t
        coeff*=c
    # Stationary age density is S(a)/mu. For p=2, A is a positive half-normal.
    if p==2:
        ages=np.abs(rng.normal(0,theta/math.sqrt(2),rep))
    elif p==1:
        ages=rng.exponential(theta,rep)
    else:
        # Numerical inversion is unnecessary here: simulation comparison uses p=2.
        raise ValueError('age simulation only for p=1 or p=2')
    T0=theta*rng.weibull(p,rep)
    U=rng.uniform(0,tau,rep)
    W=np.where(is_off, ages+sums, np.exp(-2*kappa*U)*(T0+sums))
    V=D/kappa+2*D*W
    X=rng.standard_normal(rep)*np.sqrt(V)
    return is_off,W,X


def main():
    # Variational identity: the p-Weibull large-deviation cost for a geometric weighted sum.
    for p in [1.01,1.1,1.6,2,3,5]:
        for c in [0.13,0.47,0.83]:
            q=p/(p-1)
            n=120
            w=c**np.arange(n)
            s=np.sum(w**q)
            optimizer=w**(1/(p-1))/s
            verify(abs(float(np.dot(w,optimizer))-1)<1e-12,'Hölder constraint')
            finite_cost=float(np.sum(optimizer**p))
            expected_cost=(1-c**q)**(p-1)
            verify(abs(finite_cost/expected_cost-1)<2e-10,'Hölder rate')
    # Gaussian-mixture saddle point reproduces the closed-form tail rate.
    for p in [0.5,0.75,1.,1.4,2.,3.5]:
        for c in [0.12,0.4,0.82]:
            D=1.7; theta=0.8
            a=a_weight(p,c,theta)
            zstar=(1/(4*D*p*a))**(1/(p+1))
            obj=lambda z:a*z**p+1/(4*D*z)
            num=minimize_scalar(obj,bounds=(zstar*0.4,zstar*2.5),method='bounded',options={'xatol':1e-12})
            verify(abs(num.fun/tail_k(p,c,theta,D)-1)<1e-9,'tail rate saddle')
            verify(abs(obj(zstar)/tail_k(p,c,theta,D)-1)<2e-13,'tail rate formula')
    # Rayleigh p=2 closed-form mgf of a stationary off-phase variance.
    theta=1.3;c=math.exp(-1.2)
    limit=theta**2/(4*(1-c*c))
    ratios=[log_mW_off_rayleigh(s,theta,c)/(s*s) for s in [10.,20.,40.,80.]]
    verify(abs(ratios[-1]-limit)/limit<0.025,'off-phase quadratic log-mgf limit')
    verify(all(ratios[i]>ratios[i+1] for i in range(3)),'off-phase convergence trend')
    # Rayleigh and exponential stationary age moments and exact phase weighting.
    for p in [1.,2.]:
        theta=1.3
        ea=mean_off_age(p,theta)
        if p==1:
            verify(abs(ea-theta)<1e-12,'memoryless age')
        else:
            verify(abs(ea-theta/math.sqrt(math.pi))<1e-12,'Rayleigh age')
    # Monte Carlo checks of the stationary variance law, not the remote tails.
    p=2.;theta=1.3;kappa=1.25;tau=0.48;D=0.9
    c=math.exp(-2*kappa*tau)
    mu=theta*math.gamma(1+1/p)
    off_prob=mu/(mu+tau)
    expectation_off=mean_off_age(p,theta)+mu*c/(1-c)
    expectation_on=mu/(2*kappa*tau)
    exact_W=off_prob*expectation_off+(1-off_prob)*expectation_on
    exact_X2=D/kappa+2*D*exact_W
    is_off,W,X=simulate(p,theta,kappa,tau,D)
    verify(abs(float(np.mean(is_off))-off_prob)<0.008,'renewal phase fraction')
    verify(abs(float(np.mean(W))-exact_W)<0.015*exact_W,'stationary variance excess')
    verify(abs(float(np.mean(X**2))-exact_X2)<0.03*exact_X2,'Gaussian-mixture second moment')
    verify(abs(float(np.mean(X)))<0.025*math.sqrt(exact_X2),'spatial symmetry')
    # p=2 critical factor: no residual memory as tau->infinity, nontrivial at finite tau.
    for tau in [0.1,0.4,1.7]:
        c=math.exp(-2*kappa*tau)
        ratio=tail_k(2,c,theta,D)/tail_k(2,0.,theta,D)
        verify(abs(ratio-(1-c*c)**(1/3))<1e-13,'multicycle correction')
    for p in [0.6,0.9,1.0]:
        verify(abs(tail_k(p,0.8,theta,D)/tail_k(p,0.1,theta,D)-1)<1e-13,'single-cycle regime')
    print('PASS',checks,'assertions')
    print('Rayleigh log-mgf ratio sequence:',[round(r,8) for r in ratios])
    print('Rayleigh limit:',round(limit,8))
    print('Example p=2 tail exponent = 4/3; coefficient:',round(tail_k(2,math.exp(-2*kappa*0.48),theta,D),9))
    print('Simulation E[X^2] and exact:',round(float(np.mean(X**2)),6),round(exact_X2,6))

if __name__=='__main__':
    main()
