#!/usr/bin/env python3
"""Reproducible finite checks for angular multiplication and harmonic projection leakage.
Run: python3 verify_angular_leakage.py  (Python standard library only).
Finite tests supplement, but do not prove, the stated infinite-dimensional theorem.
"""
import math
from fractions import Fraction

def moment(s,p):
    return math.exp(math.lgamma(p+1)+math.lgamma(s+1)-math.lgamma(s+p+1))

def defect(n,k,p):
    a,b=abs(n),abs(n+k)
    lw=2*(math.lgamma(p+1)+math.lgamma((a+b)/2+1)-math.lgamma((a+b)/2+p+1))
    lw-=(math.lgamma(p+1)+math.lgamma(a+1)-math.lgamma(a+p+1))
    lw-=(math.lgamma(p+1)+math.lgamma(b+1)-math.lgamma(b+p+1))
    if lw>1e-9: raise AssertionError(('unexpected weight',n,k,p,lw))
    return max(0., -math.expm1(lw))

def finite_unweighted_exact(n,k):
    a,b=abs(n),abs(n+k)
    avg=Fraction(a+b,2)
    m=lambda z: Fraction(1,1)/(z+1)
    return 1-m(avg)**2/(m(a)*m(b))

def trace_coefficient(p):
    return math.exp(math.log(p)+math.lgamma(p+1)+math.lgamma(.5)-math.lgamma(p+1.5))

def count_coefficient(p,tau):
    u=(1-tau)**(1/p)
    return u / math.sqrt(1-u)

def limit_profile(x,p):
    if -1<x<0: return 1-(4*(-x)*(1+x))**p
    if x>=0: return 1-(1-1/(2*x+1)**2)**p
    return 1-(1-1/(2*abs(x+1)+1)**2)**p

checks=0
for p in (.25,.5,1.,1.3,2.,3.,6.):
    for k in range(1,13):
        for n in range(-k-65,66):
            d=defect(n,k,p)
            assert -1e-11<=d<1
            dd=defect(-k-n,k,p)
            assert abs(d-dd)<2e-11
            checks+=2
        assert abs(1-max(defect(n,k,p) for n in range(-k-30,31))-moment(k/2,p)**2/moment(k,p))<3e-10
        checks+=1
for k in range(1,80):
    for n in range(-2*k,2*k+1):
        x=finite_unweighted_exact(n,k)
        assert x>=0 and x<1
        assert abs(defect(n,k,1)-float(x))<1e-12
        checks+=1
    jsum=sum(finite_unweighted_exact(-j,k) for j in range(1,k))
    assert jsum==Fraction(k*(k-1)*(k-2),3*(k+2)**2)
    checks+=1
for p in (.5,1,2,3):
    for k in (128,384,768):
        # 15-to-1 truncated domain; the O(1/15) tail is not discarded in any proof.
        N=15*k
        vals=[defect(n,k,p) for n in range(-N-k,N+1)]
        observed=sum(v>=.36 for v in vals)/k
        expected=count_coefficient(p,.36)
        assert abs(observed-expected)<.045, (p,k,observed,expected)
        checks+=1
    for k in (128,512):
        measured=defect(k,k,p)
        predicted=1-(1-1/9)**p
        assert abs(measured-predicted)<.03, (p,k,measured,predicted)
        checks+=1
print('PASS:',checks,'finite exact-rational, symmetry, moment, and scaling checks')
print('Asymptotic trace constants:',', '.join('p=%s: %.12g'%(p,trace_coefficient(p)) for p in (.5,1,2,3)))
print('Finite tests do not establish infinite-dimensional results.')
