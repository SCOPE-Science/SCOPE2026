#!/usr/bin/env python3
"""Finite checks for an exact four-node Kuramoto locking threshold.

Only the accompanying analytic argument proves the all-parameter theorem.
Uses Python's standard library; no third-party package is required.
"""
import itertools
import math
from fractions import Fraction

checks = 0

def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def maximum_flow(a):
    if a <= 1.0 / 9.0:
        return 1.0-a
    return (1.0+3.0*a)**1.5/(3.0*math.sqrt(3.0*a))

def threshold(a):
    return 1.0/maximum_flow(a)

def flow(a,s):
    return s*(1.0+3.0*a)-4.0*a*s**3

def peak_s(a):
    if a <= 1.0/9.0:
        return 1.0
    return math.sqrt((1.0+3.0*a)/(12.0*a))

def quadratic(a, angles, v):
    d = [v[j+1]-v[j] for j in range(3)]
    return sum(math.cos(angles[j])*d[j]*d[j] for j in range(3)) + a*math.cos(sum(angles))*(v[3]-v[0])**2

# Exact triple-angle identity under rational test inputs.
for k in range(-100,101):
    s = Fraction(k, 100)
    a = Fraction(11,17)
    check(s*(1+3*a)-4*a*s**3 == s+a*(3*s-4*s**3), 'triple-angle polynomial')

# Direct dense one-dimensional checks of derived maximizer/threshold.
for a in (0,.001,.05,1/9,.12,1/6,.2,.3,.4,.41,1,2,6,30):
    smax=peak_s(a)
    fmax=maximum_flow(a)
    check(abs(flow(a,smax)-fmax)<2e-11,'analytic maximum')
    sampled=max(flow(a,-1+2*i/40000) for i in range(40001))
    check(fmax-sampled>-2e-10 and fmax-sampled<2e-7,'dense grid against closed maximum')
    check(threshold(a)>0,'positive threshold')

# Every non-cohesive branch has a direct negative Hessian direction.
for a in (0,.1,1/6,1,10):
    for s in (-.97,-.4,0,.4,.97):
        t=math.asin(s)
        for bits in itertools.product((0,1),repeat=3):
            if bits==(0,0,0):
                continue
            angles=[(math.pi-t) if bit else t for bit in bits]
            negatives=[j for j,x in enumerate(bits) if x]
            if len(negatives)>=2:
                inds=set(negatives[:2])
                if inds=={0,1}: v=(0,1,0,0)
                elif inds=={1,2}: v=(0,0,1,0)
                else: v=(0,1,1,0)
            elif negatives==[1]:
                v=(0,1,-1,0)
            elif negatives==[0]:
                v=(0,1,1,1)
            else:
                v=(0,0,0,1)
            check(quadratic(a,angles,v)<-1e-10,'negative branch witness')

# At 1.02 times the critical coupling, an all-cohesive strictly stable
# phase-locked state can be located on the increasing flow branch.
for a in (0,.001,.05,1/9,.12,1/6,.2,.3,.4,1,2,6,30):
    k=1.02*threshold(a)
    hi=peak_s(a)
    lo=0.0
    for _ in range(100):
        mid=(lo+hi)/2
        if flow(a,mid)<1/k: lo=mid
        else: hi=mid
    s=(lo+hi)/2
    t=math.asin(s)
    c=math.cos(t)
    check(abs(k*(math.sin(t)+a*math.sin(3*t))-1)<3e-12,'lock equation')
    check(c>0 and c+3*a*math.cos(3*t)>1e-6,'quotient Hessian is strictly positive')
    for d in ((1,0,0),(0,1,0),(0,0,1),(1,-2,3),(5,-3,2)):
        q=c*sum(x*x for x in d)+a*math.cos(3*t)*sum(d)**2
        check(q>0,'full Hessian test')

# Critical signs and crossover.
check(abs(threshold(0)-1)<1e-15, 'chain threshold')
check(abs(threshold(1/6)-2/math.sqrt(3))<1e-14, 'peak threshold')
check(abs(threshold(1)-3*math.sqrt(3)/8)<1e-14,'full edge')
lo,hi=1/6,1.0
for _ in range(90):
    mid=(lo+hi)/2
    if (1+3*mid)**3-27*mid<0: lo=mid
    else: hi=mid
root=(lo+hi)/2
check(.40889386<root<.40889387,'unique post-peak crossing')
check(abs(threshold(root)-1)<2e-14,'crossing equation')
for a in (0,.01,.06,.11,.15):
    check(threshold(a+1e-7)>threshold(a),'pre-max increase')
for a in (.17,.19,.3,.4,.6,1.0,9):
    check(threshold(a+1e-7)<threshold(a),'post-max decrease')
print(f'PASS: {checks} finite diagnostics; crossover a={root:.15f}; Kc(1)={threshold(1):.15f}')
print('The analytic proof, not these finite checks, establishes the theorem.')
