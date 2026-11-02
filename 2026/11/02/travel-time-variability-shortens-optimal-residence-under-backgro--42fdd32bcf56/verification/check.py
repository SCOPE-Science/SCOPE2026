#!/usr/bin/env python3
"""Independent finite checks of a lifetime foraging residence theorem.

Run with Python 3 standard library: python3 verification/check.py
Computations are numerical consistency checks; the all-distribution theorem
is established in RESULT.md analytically.
"""
import math
import random
from fractions import Fraction

CHECKS = 0

def verify(cond, detail=''):
    global CHECKS
    assert cond, detail
    CHECKS += 1


def bisect_decreasing(f, target, hi=1.0):
    lo = 0.0
    while f(hi) > target:
        hi *= 2.0
        assert hi < 1e9
    for _ in range(90):
        mid = (lo+hi)/2
        if f(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def exp_gain(k, death, t):
    return k * (-math.expm1(-(k+death)*t))/(k+death)


def exp_gain_g(k,t):
    return k*math.exp(-k*t)


def H(k,death,t):
    return math.exp(-death*t)*exp_gain_g(k,t) + death*exp_gain(k,death,t)


def root(k,death,A):
    return bisect_decreasing(lambda t:exp_gain_g(k,t)/H(k,death,t),A)


def reward(k,death,A,t):
    return A*exp_gain(k,death,t)/(1-A*math.exp(-death*t))

# Exact Laplace-factor comparison for two mean-matched travel laws.
A_fixed = Fraction(1,2) # T=log 2, death=1
A_spread = Fraction(5,8) # T=0 or log 4 equally likely
verify(A_spread > A_fixed)
t_fixed = math.acosh(2)
t_spread = math.acosh(8/5)
verify(t_spread < t_fixed)
verify(abs(root(1.,1.,float(A_fixed))-t_fixed)<1e-12)
verify(abs(root(1.,1.,float(A_spread))-t_spread)<1e-12)
J_fixed = 2-math.sqrt(3)
J_spread = (8-math.sqrt(39))/5
verify(J_spread>J_fixed)
verify(abs(reward(1.,1.,float(A_fixed),t_fixed)-J_fixed)<1e-12)
verify(abs(reward(1.,1.,float(A_spread),t_spread)-J_spread)<1e-12)

# The critical equation changes sign and the maximum is global.
rng = random.Random(1941)
for _ in range(250):
    k=math.exp(rng.uniform(-2,2))
    death=math.exp(rng.uniform(-3,2))
    m=math.exp(rng.uniform(-2,2))
    spread=rng.random()*m
    A1=math.exp(-death*m)
    A2=.5*(math.exp(-death*(m-spread))+math.exp(-death*(m+spread)))
    verify(A2>=A1-1e-15)
    t1,t2=root(k,death,A1),root(k,death,A2)
    verify(t2<=t1+1e-11)
    verify(reward(k,death,A2,t2)>=reward(k,death,A1,t1)-1e-12)
    for t in (0,t1*.5,t1*.9,t1*1.1,t1*2,t1+3):
        verify(reward(k,death,A1,t1)>=reward(k,death,A1,t)-1e-12)

# The MVT limit and small-mortality coefficient for equal-mean distributions.
m=math.log(2)
def mvteq(t):
    return math.exp(t)-1-t-m
low,high=0.,3.
for _ in range(80):
    mid=(low+high)/2
    if mvteq(mid)>0:high=mid
    else:low=mid
t0=(low+high)/2
variance_difference=m*m
coefficient=-variance_difference/(2*(math.exp(t0)-1))
errors=[]
for death in (.08,.04,.02,.01,.005):
    a1=math.exp(-death*m)
    a2=.5*(1+math.exp(-death*2*m))
    delta=root(1,death,a2)-root(1,death,a1)
    err=abs(delta/death-coefficient)
    errors.append(err)
    verify(delta<0)
    verify(err<death*.12, (death, err))
for i in range(len(errors)-1):
    verify(errors[i+1]<errors[i])

# For non-exponential gain, test a decreasing marginal gain numerically.
# g(t)=(1+t)^-2, so the theorem does not depend on exponential depletion.
def G_nonexp(death,t):
    n=400
    h=t/n
    f=lambda x:math.exp(-death*x)/(1+x)**2
    total=f(0)+f(t)
    total+=4*sum(f(h*j) for j in range(1,n,2))
    total+=2*sum(f(h*j) for j in range(2,n,2))
    return total*h/3

def F_nonexp(death,t):
    g=1/(1+t)**2
    return g/(math.exp(-death*t)*g+death*G_nonexp(death,t))
for death in (.2,.5,1.,2.):
    A1=math.exp(-death)
    A2=.5*(1+math.exp(-2*death))
    t1=bisect_decreasing(lambda t:F_nonexp(death,t),A1)
    t2=bisect_decreasing(lambda t:F_nonexp(death,t),A2)
    verify(t2<t1)
    verify(abs(F_nonexp(death,t1)-A1)<1e-9)
    for t in (.001,.05,.2,.5,1,2,3,5):
        verify(F_nonexp(death,t)>F_nonexp(death,t+.02))

print('PASS:',CHECKS,'checks; exact example and small-hazard asymptotics consistent')
