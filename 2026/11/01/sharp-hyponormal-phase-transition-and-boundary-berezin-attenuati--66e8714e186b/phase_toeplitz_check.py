"""Finite numerical tests for phase-twisted Bergman Toeplitz shifts.
Reproducible supplementary checks; proofs of limiting statements are analytic.
"""
import math
import cmath
from scipy.special import loggamma

NASSERT=0

def check(cond,why):
    global NASSERT
    if not cond:
        raise AssertionError(why)
    NASSERT+=1

def w2(n,k,t):
    prod=1.0
    for j in range(1,n+k+2):
        prod*=j*j/(j*j+t*t)
    return (n+1)/(n+k+1)*prod

def w2_fast(n,k,t):
    x=n+k+2
    return (n+1)/(n+k+1)*abs(cmath.exp(loggamma(1+1j*t)+loggamma(x)-loggamma(x+1j*t)))**2

def ber_series(r,k,t):
    # Coefficients from the beta integral and the reproducing-kernel basis.
    q=r*r
    s=0j
    for n in range(12000):
        z=n+k+1
        beta=cmath.exp(loggamma(z)+loggamma(1+1j*t)-loggamma(z+1+1j*t))
        term=(n+1)*(n+k+1)*beta*(q**n)
        s+=term
        if n>200 and abs(term)<1e-15*max(1,abs(s)):
            break
    return (1-q)**2*(r**k)*s

for k in (1,2,3,5,9):
    for tau in (0.,0.25,0.8,1.,1.4,2.,3.1):
        for n in (0,1,2,5,10,100):
            lhs=w2(n,k,tau)
            rhs=w2_fast(n,k,tau)
            check(abs(lhs-rhs)<3e-12*max(1,lhs),'beta/gamma disagreement')
            numer=k*(n+k+2)-(n+1)*tau*tau
            delta=w2(n+1,k,tau)-lhs
            check((numer>=-1e-12 and delta>=-1e-12) or (numer<=1e-12 and delta<=1e-12),'adjacent-weight sign')
        if tau*tau<=k:
            vals=[w2(n,k,tau) for n in range(180)]
            check(all(y>=x-1e-13 for x,y in zip(vals,vals[1:])),'hyponormal branch')
        elif tau*tau>k:
            x=max(150,math.ceil(k*(k+1)/(tau*tau-k))+15)
            check(w2(x+1,k,tau)<w2(x,k,tau),'nonhyponormal tail')

for tau in (0.0,0.5,1.0,2.0):
    L=abs(cmath.exp(loggamma(1+1j*tau)))
    B=abs(cmath.exp(loggamma(1+1j*tau)+loggamma(2-1j*tau)))
    check(abs(B-math.sqrt(1+tau*tau)*L*L)<2e-13,'Gauss constant')
    if tau:
        check(B<L,'strict Berezin gap')
    for k in (1,3):
        vals=[]
        for r in (.90,.95,.97):
            z=ber_series(r,k,tau)/(r**k*(1-r*r)**(1j*tau))
            I=cmath.exp(loggamma(1+1j*tau)+loggamma(2-1j*tau))
            vals.append(abs(z-I))
        check(vals[-1]<vals[0]+0.01,'boundary-kernel asymptotic trend')
        if tau==0:
            check(abs(vals[-1])<0.1,'untwisted boundary formula')
print('PASS finite tests:',NASSERT)
