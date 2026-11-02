#!/usr/bin/env python3
"""Standalone arithmetic checks for geometric Galton--Watson immigrant clans.

Requires Python 3 standard library only. These checks test finite identities and
numerical approximations; the infinite limiting theorem follows from the proof.
"""
import math
from fractions import Fraction

checks=0

def verify(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks+=1


def family_pgf(t,z):
    return (t-(t-1)*z)/(t+1-t*z)


def family_tail(t,h):
    if t==0:
        return Fraction(int(h<=1),1)
    return Fraction(1,t+1)*Fraction(t,t+1)**(h-1)

# Iterate the *actual* geometric offspring pgf, not just the proposed formula.
for z in [Fraction(i,13) for i in range(0,13)]:
    cur=z
    for t in range(45):
        verify(cur==family_pgf(t,z),f'generating function t={t} z={z}')
        cur=1/(2-cur)

# Verify the normalization and tail identity using the rational infinite sum.
for t in range(1,42):
    survive=Fraction(1,t+1)
    r=Fraction(t,t+1)
    verify(survive+Fraction(t,t+1)==1,'survival')
    verify(Fraction(t,t+1)+(survive/(t+1))/(1-r)==1,'mass normalized')
    for h in range(1,24):
        verify(family_tail(t,h)-family_tail(t,h+1)==survive/(t+1)*r**(h-1), 'mass from tails')
        verify(family_tail(t,h)==survive*r**(h-1), 'survival geometric')

# Moments from exact iteration (mean 1 and variance 2t).
# f_t'(1)=1, f_t''(1)=2t; E Z^2 = 1+2t.
for t in range(1,300):
    a,b,c=t,1-t,t+1
    # f_t(z) = (a+bz)/(c-tz): derivatives at one
    first=(b*(c-t)+t*(a+b))/(c-t)**2
    second=2*t*first/(c-t)
    verify(first==1, 'mean')
    verify(second==2*t, 'second factorial moment')


def root_lambda(n,alpha,c):
    # Root of lambda+(alpha+1)*log(lambda)=alpha*log(n)+log(c Gamma(alpha+1)).
    goal=alpha*math.log(n)+math.log(c*math.gamma(alpha+1))
    lo=1e-12
    hi=max(2.,2.*alpha*math.log(n)+abs(goal)+5)
    while hi+(alpha+1)*math.log(hi) < goal: hi*=2
    for _ in range(90):
        md=(hi+lo)/2
        if md+(alpha+1)*math.log(md)<goal:lo=md
        else: hi=md
    return (hi+lo)/2


def exceedance(n,alpha,c,x=0.0):
    lam=root_lambda(n,alpha,c)
    h=math.ceil(n*(lam+x))
    total=0.; err=0.; logs=0.; maxq=0.
    # b_k immigrants at time k, with t=n-k future branching generations.
    for k in range(1,n):
        t=n-k
        b=math.floor(c*k**alpha)
        q=math.exp(-math.log(t+1)+(h-1)*math.log1p(-1/(t+1)))
        total+=b*q
        logs-=b*math.log1p(-q)
        err+=b*q*q
        maxq=max(maxq,q)
    return lam,h,total,logs,err,maxq

for alpha,c in [(0.5,2),(1.,1.),(2.,1.)]:
    vals=[]
    for n in [512,2048,8192,32768]:
        lam,h,total,logs,err,maxq=exceedance(n,alpha,c)
        verify(lam>0 and h>1,'positive critical centering')
        verify(abs(lam+(alpha+1)*math.log(lam)-alpha*math.log(n)-math.log(c*math.gamma(alpha+1)))<1e-10,'root equation')
        verify(logs>=total-1e-8,'log-product lower')
        verify(logs-total<=err/(2*(1-maxq))+1e-8,'log-product upper')
        verify(maxq<1,'rare individual')
        vals.append(total)
    verify(vals[-1]>vals[0],'eventual intensity approximation in tested sequence')

print(f'PASS: {checks} exact-arithmetic and numerical assertions')
for alpha,c in [(0.5,2),(1.,1.),(2.,1.)]:
    lam,h,total,logs,err,maxq=exceedance(32768,alpha,c)
    print(f'alpha={alpha}, c={c}, n=32768: lambda={lam:.6f}, expected exceedances={total:.6f}, P(max<h)={math.exp(-logs):.6f}')
print('These finite checks do not certify any asymptotic limit or mathematical priority.')
