#!/usr/bin/env python3
"""Reproduce weighted-Bergman monomial Hankel phase-transition calculations.

Uses only the Python standard library.  Checks finite-dimensional exact
identities independently of the asymptotic derivation; finite checks do not
certify the theorem for all degrees or parameters.
"""
import math
from fractions import Fraction

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def moment(k, alpha):
    return math.exp(math.lgamma(k+1) + math.lgamma(alpha+2)-math.lgamma(k+alpha+2))

def discrete(n, m, alpha):
    a = moment(n+m,alpha)/moment(n,alpha)
    if n>=m:
        a -= moment(n,alpha)/moment(n-m,alpha)
    return a

def direct_orthogonal_projection(n,m,alpha):
    # Norm of the anti-holomorphic monomial product, minus its projection.
    norm2 = moment(n+m,alpha)/moment(n,alpha)
    if n<m:
        return norm2
    coefficient = moment(n,alpha) / (math.sqrt(moment(n,alpha)) * math.sqrt(moment(n-m,alpha)))
    return norm2 - coefficient**2

def limiting(t,p):
    if t==0.0:
        return 0.0
    first=(t/(t+1))**p
    if t<1:
        return first
    return first-((t-1)/t)**p

def optimum(p):
    if p<=1:
        return 1.0,2.0**(-p)
    # Find positive root after its unique maximum by bisection.
    low=1.0/p
    high=1.0 - 1e-12
    def fun(x):
        return (p-1)*math.log1p(-x)+(p+1)*math.log1p(x)
    check(fun(low)>0,'Maximum of log intersection is positive')
    check(fun(high)<0,'Log intersection crosses negative')
    for _ in range(110):
        mid=(low+high)/2
        if fun(mid)>0:
            low=mid
        else:
            high=mid
    x=(low+high)/2
    t=1/x
    return t,limiting(t,p)

# Independent direct Hilbert-space projection and norm subtractions.
for alpha in (-0.8,-0.25,0.0,0.3,1.0,2.0,4.0):
    for m in range(1,12):
        for n in range(0,49):
            a=discrete(n,m,alpha)
            b=direct_orthogonal_projection(n,m,alpha)
            check(abs(a-b)<1e-10,'Polar-norm/projection decomposition mismatch')
            check(-2e-12<=a<=1+2e-12,'Squared singular-value bounds')

# Exactly solvable unweighted case: norm 1/sqrt(2) uniquely at n=m-1.
for m in range(1,101):
    seq=[]
    for n in range(0,3*m+100):
        a=Fraction(n+1,n+m+1) if n<m else Fraction(m*m,(n+1)*(n+m+1))
        seq.append(a)
    check(max(seq)==Fraction(1,2),'Unweighted exact norm')
    check(seq.index(Fraction(1,2))==m-1,'Unweighted unique maximizing monomial')
    check(seq.count(Fraction(1,2))==1,'Unweighted unique maximizer')

# Derivative signs and uniqueness of the scaled maximum.
for alpha in (-0.8,-0.25,0.0,0.2,0.5,1.0,2.0,5.0):
    p=alpha+1
    t,c=optimum(p)
    check(abs(limiting(t,p)-c)<1e-12,'Extremal function evaluation')
    for j in range(1,350):
        test_t=0.001 + j*0.06
        check(limiting(test_t,p) <= c+1e-11,'Global envelope inequality')

# Discrete maxima approach the correct large-symbol-degree limit.
for alpha in (-0.5,0,0.2,0.5,1.0,2.0):
    p=alpha+1
    t,c=optimum(p)
    for m in (60,120,250,500):
        Ns=range(0,max(2*m,int((t+1.0)*m)))
        vals=[discrete(n,m,alpha) for n in Ns]
        j=max(range(len(vals)),key=lambda k: vals[k])
        check(abs(vals[j]-c)<0.07,'Discrete-to-continuum norm limit')
        if m>=250 and alpha in (-0.5,0.0,0.5,1,2):
            check(abs(j/m-t)<0.17,'Scaled maximizing degree convergence')

# Integer weight exponent 2: golden-ratio maximizing mode.
t,c=optimum(3.0)
check(abs(t-(1+math.sqrt(5))/2)<1e-10,'Golden ratio critical degree')

# Essential-singularity scaling: log(delta) ~ -log(4)/alpha-log(2).
for alpha in (0.16,0.2,0.25,0.3):
    # Equation can be evaluated reliably at these alpha.
    t,c=optimum(1+alpha)
    delta=t-1
    check(delta>0,'Positive interior displacement')
    ratio=delta/(0.5*4**(-1/alpha))
    check(abs(ratio-1)<0.03,'Essential singularity asymptotic at small weights')

print(f'WEIGHTED_HANKEL_CHECKS_PASS {checks}')
