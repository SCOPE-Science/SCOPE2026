#!/usr/bin/env python3
"""Deterministic numerical and exact-arithmetic checks for a binary Markov transport limit.

Requires Python >=3.10, numpy, scipy. Does not prove the infinite-size assertion.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.special import ndtri

checks = 0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def distribution(n, p, rho):
    a, b = p*(1-rho), (1-p)*(1-rho)
    q0, q1 = np.array([1-p, 0.]), np.array([0., p])
    for length in range(2, n+1):
        z0, z1 = np.zeros(length+1), np.zeros(length+1)
        z0[:length] = (1-a)*q0 + b*q1
        z1[1:] = a*q0 + (1-b)*q1
        q0, q1 = z0, z1
    result=q0+q1
    result /= result.sum()
    return result


def asymptotic_constant(p, rho):
    q=1-p
    sigma2=p*q*(1+rho)/(1-rho)
    third=p*q*(q-p)*(1+4*rho+rho*rho)/(1-rho)**2
    return 1/(12*sigma2)+third*third/(18*sigma2**3)


def transport(n,p,rho):
    mass=distribution(n,p,rho)
    index=np.arange(n+1, dtype=float)
    h=np.arange(1,n)
    v=p*(1-p)*(n+2*np.sum((n-h)*rho**h))
    x=(index-n*p)/math.sqrt(v)
    left=np.r_[0.,np.clip(np.cumsum(mass)[:-1],0,1)]
    z=ndtri(left)
    phi=np.exp(-z*z/2)/math.sqrt(2*math.pi)
    # Each mass maps an adjacent interval of the normal distribution to its atom.
    corr=float(np.sum(x*(phi-np.r_[phi[1:],0.])))
    variance_check=float(np.dot(mass,x*x))
    return 1+variance_check-2*corr,variance_check


def exact_moments_check():
    p,rho=Fraction(3,10),Fraction(-1,4)
    a=p*(1-rho);b=(1-p)*(1-rho)
    # Exact distributions indexed by (running sum, final state).
    states={(0,0):1-p,(1,1):p}
    for n in range(1,11):
        mean=sum(Fraction(s)*v for (s,t),v in states.items())
        var=sum((s-mean)**2*v for (s,t),v in states.items())
        third=sum((s-mean)**3*v for (s,t),v in states.items())
        predicted=p*(1-p)*(n+2*sum((n-h)*rho**h for h in range(1,n)))
        predthird=p*(1-p)*(1-2*p)*(n + 6*sum((n-h)*rho**h for h in range(1,n))
             +6*sum((n-h)*(h-1)*rho**h for h in range(2,n)))
        check(mean==n*p, 'exact mean')
        check(var==predicted, 'exact variance')
        check(third==predthird, 'exact third centered moment')
        new={}
        for (s,t),w in states.items():
            for nt,prob in ([(0,1-a),(1,a)] if t==0 else [(0,b),(1,1-b)]):
                key=(s+nt,nt)
                new[key]=new.get(key, Fraction(0))+w*prob
        states=new


def main():
    exact_moments_check()
    scenarios=[(.30,0.0),(.30,-2+math.sqrt(3)),(.30,.40),(.40,-.40),(.50,.55)]
    ns=[50,150,500,1500,3500]
    print('Exact finite-n binary Markov occupation transport checks:')
    for p,rho in scenarios:
        a,b=p*(1-rho),(1-p)*(1-rho)
        check(0<a<1 and 0<b<1,'valid strictly positive kernel')
        target=asymptotic_constant(p,rho)
        errors=[]
        results=[]
        for n in ns:
            w,v=transport(n,p,rho)
            result=n*w
            results.append(result)
            errors.append(abs(result-target))
            check(abs(v-1)<1e-9,f'exact variance normalization n={n}')
            check(w>0 and math.isfinite(w),f'quadratic transport n={n}')
        check(all(errors[j+1]<errors[j] for j in range(len(errors)-1)),f'numerical convergence p={p},rho={rho}')
        check(errors[-1]<0.001,f'leading coefficient n=3500 p={p},rho={rho}')
        print('p=%.3f rho=% .8f constant=%.9f n=50:%.9f n=3500:%.9f'
             %(p,rho,target,results[0],results[-1]))
    r0=-2+math.sqrt(3)
    check(abs(1+4*r0+r0*r0)<1e-12, 'anti-persistent cancellation root')
    check(abs(asymptotic_constant(.3,0)-(.3*.7)**-1*(3+2*.4**2)/36)<1e-12,
          'independent-binomial consistency')
    print('PASS %d deterministic checks'%checks)

if __name__=='__main__':
    main()
