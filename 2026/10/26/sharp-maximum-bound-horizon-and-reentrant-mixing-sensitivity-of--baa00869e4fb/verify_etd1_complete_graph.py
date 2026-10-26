#!/usr/bin/env python3
"""Standalone finite checks for a complete-graph Allen--Cahn ETD1 step.

Run: python3 verify_etd1_complete_graph.py
Analytical inequalities and uniqueness proofs are supplied in RESULT.md.
"""
import math
import random

CHECKS = 0

def check(cond, detail=''):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(detail or ('check ' + str(CHECKS)))

def coeffs(n, rate, step):
    assert n >= 2 and rate > 0 and step > 0
    z = rate * step
    one_minus_exp = -math.expm1(-z)
    e = math.exp(-z)
    pd = (1 + (n - 1) * e) / n
    po = one_minus_exp / n
    kd = (step + (n - 1) * one_minus_exp / rate) / n
    ko = (step - one_minus_exp / rate) / n
    return pd, po, kd, ko

def threshold(n, rate):
    left, right = 0., 0.5
    for _ in range(120):
        h = (left + right) * 0.5
        pd, po, kd, ko = coeffs(n, rate, h)
        if 2 * kd >= pd:
            right = h
        else:
            left = h
    return (left + right) * 0.5

def scalar_max(p, k):
    if 2 * k <= p:
        return p, 1.
    u = math.sqrt((p+k)/(3*k))
    return (p + k) * u - k * u**3, u

def exact_bound(n, rate, h):
    pd, po, kd, ko = coeffs(n, rate, h)
    md, ud = scalar_max(pd, kd)
    mo, uo = scalar_max(po, ko)
    return md+(n-1)*mo, ud, uo

def step_coordinate(n, rate, h, x, target=0):
    pd,po,kd,ko=coeffs(n, rate, h)
    val = 0.
    for j in range(n):
        p,k = (pd,kd) if j == target else (po,ko)
        val += p*x[j] + k*(x[j]-x[j]**3)
    return val

def minimizer(n):
    a=n-1
    def H(y):
        return math.exp(y)-(1+y+y*y)+a*(1-y-math.exp(-y))
    lo,hi=1e-3,12.
    check(H(lo)<0 and H(hi)>0)
    for _ in range(100):
        mid=(lo+hi)/2
        if H(mid)<0:
            lo=mid
        else:
            hi=mid
    y=(lo+hi)/2
    e=math.exp(-y)
    rate=2*(y+a*(1-e))/(1+a*e)
    return y,rate,y/rate

rng=random.Random(517892)
for n in range(2,9):
    for rate in (0.02,0.1,0.7,1.0,5.0,20.0,100.0):
        hc=threshold(n,rate)
        check(0 < hc < .5)
        pd,po,kd,ko=coeffs(n,rate,hc)
        check(abs(2*kd-pd)<1e-12)
        check(2*ko<po)
        for h in (.4*hc, .95*hc, .5*(hc+.5), .5, .7, 1.2, 2.0):
            if h <=0: continue
            pd,po,kd,ko=coeffs(n,rate,h)
            check(abs(pd+(n-1)*po-1.)<1e-12)
            check(abs(kd+(n-1)*ko-h)<1e-12)
            bound,ud,uo=exact_bound(n,rate,h)
            witness=[ud]+[uo]*(n-1)
            check(abs(step_coordinate(n,rate,h,witness)-bound)<1e-11)
            check(bound >= 1-1e-12)
            check((bound<=1+1e-11) if h < hc else (bound>1+1e-12))
            for _ in range(18):
                x=[rng.uniform(-1,1) for _ in range(n)]
                for i in range(n):
                    check(abs(step_coordinate(n,rate,h,x,i))<=bound+1e-11)
        # A nonpositive vertex drift is a property of the exact evolution.
        x=[rng.uniform(-1,1) for _ in range(n)]
        mx=max(x)
        for i in range(n):
            if x[i]==mx:
                q=rate*(sum(x)/n-x[i])
                check(q <= 1e-12)
for n in (2,3,5,10,30):
    y,rate,hmin=minimizer(n)
    check(0<hmin<.5)
    check(abs(threshold(n,rate)-hmin)<2e-12)
    check(threshold(n,rate*.8)>hmin)
    check(threshold(n,rate*1.2)>hmin)
    if n==2:
        check(abs(rate-5.827985443462673)<1e-10)
        check(abs(hmin-0.395437327369877)<1e-10)
# Weak/strong mixing and high dimension checks are diagnostics, not proofs.
for n in (2,3,6):
    a=n-1
    t=0.0001
    check(abs((.5-threshold(n,t))/t-a/(8*n))<.0002)
    t=1000.
    check(abs((.5-threshold(n,t))*t-a)<.001)
for rate in (.5,2.,10.):
    limit=math.log1p(rate/2)/rate
    check(abs(threshold(50000,rate)-limit)<1e-4)
print('VERIFICATION_OK',CHECKS)
