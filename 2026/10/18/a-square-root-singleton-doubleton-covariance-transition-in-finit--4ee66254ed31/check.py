"""Reproducibility checks for symmetric Dirichlet-multinomial singleton/doubleton covariance.

Exact probability checks use rational arithmetic; asymptotic checks use arbitrary precision.
"""
from fractions import Fraction
from math import factorial
from itertools import product
from functools import lru_cache
import mpmath as mp


def rising(x, n):
    p = 1
    for j in range(n):
        p *= x+j
    return p


def covariance_formula(m, n, alpha):
    z = rising(m*alpha,n)
    p1 = n*alpha*rising((m-1)*alpha,n-1)/z
    p2 = Fraction(n*(n-1),2)*alpha*(alpha+1)*rising((m-1)*alpha,n-2)/z
    p12 = Fraction(n*(n-1)*(n-2),2)*alpha*alpha*(alpha+1)*rising((m-2)*alpha,n-3)/z
    return m*(m-1)*p12-m*m*p1*p2


def compositions(n,m):
    if m==1:
        yield (n,)
    else:
        for k in range(n+1):
            for rest in compositions(n-k,m-1):
                yield (k,)+rest


def covariance_exhaustive(m,n,alpha):
    z=rising(m*alpha,n)
    e1=e2=e12=Fraction(0)
    for v in compositions(n,m):
        w=Fraction(factorial(n),1)
        for j in v:
            w *= Fraction(rising(alpha,j),factorial(j))
        w /= z
        a=v.count(1); b=v.count(2)
        e1+=w*a; e2+=w*b; e12+=w*a*b
    return e12-e1*e2

checks=0
for m in (3,4,5):
    for n in range(3,9):
        for a in (Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(2)):
            exact=covariance_exhaustive(m,n,a)
            formula=covariance_formula(m,n,a)
            assert exact==formula, (m,n,a,exact,formula)
            checks+=1
print('exact rational comparisons:',checks)

mp.mp.dps=70

def logq(m,n,gamma):
    m=mp.mpf(m);n=mp.mpf(n);g=mp.mpf(gamma);a=g/m
    return (mp.log((m-1)*(n-2)/(m*n))+
            mp.loggamma(g+n)-mp.loggamma(g)+
            mp.loggamma(g-2*a+n-3)-mp.loggamma(g-2*a)-
            mp.loggamma(g-a+n-1)+mp.loggamma(g-a)-
            mp.loggamma(g-a+n-2)+mp.loggamma(g-a))

root_checks=0
for gs in ('0.1','0.5','0.9'):
    g=mp.mpf(gs)
    target=(3+2*g)/2
    for m in (100,1000,10000):
        c=mp.sqrt(2*(1-g)*m)
        root=mp.findroot(lambda x:logq(m,x,g),(c+mp.mpf('0.7'),c+mp.mpf('3.2')))
        assert abs((root-c)-target)<mp.mpf('1.5')/mp.sqrt(m)+mp.mpf('0.3')
        assert logq(m,c+target-1,g)>0
        assert logq(m,c+target+1,g)<0
        root_checks+=1
        print('gamma',gs,'m',m,'root-offset',mp.nstr(root-c,12),'predicted',mp.nstr(target,6))
print('high precision threshold checks:',root_checks)
