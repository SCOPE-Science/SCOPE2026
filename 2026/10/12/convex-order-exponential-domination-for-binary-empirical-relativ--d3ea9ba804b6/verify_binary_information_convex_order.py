#!/usr/bin/env python3
import math

def normalize_p(p):
    return min(p, 1.0-p)

def x_atoms(p):
    p = normalize_p(p)
    q = 1.0-p
    if p == 0.5:
        return p,q,0.0,0.0
    d = math.log(q/p)
    return p,q,-p*d,q*d

def stop_x(p,a):
    p,q,xm,xp = x_atoms(p)
    return q*max(xm-a,0.0)+p*max(xp-a,0.0)

def stop_y(a):
    return -a if a <= -1.0 else math.exp(-(1.0+a))

def log_mgf_x(p,t):
    p,q,xm,xp = x_atoms(p)
    m = max(t*xm,t*xp)
    return m + math.log(q*math.exp(t*xm-m)+p*math.exp(t*xp-m))

probs=[1e-10,1e-8,1e-6,1e-4,1e-3,0.01,0.03,0.07,0.1,0.2,0.3,0.4,0.49,0.5,
       0.51,0.6,0.8,0.9,0.99,1-1e-6]
ts=[0.0,0.01,0.1,0.25,0.5,0.75,0.9,0.99]
stoploss_cases=0
mgf_cases=0
min_gap=float("inf")
for p0 in probs:
    p,q,xm,xp=x_atoms(p0)
    lo=-1.25
    hi=max(1.0,xp+0.5)
    for j in range(801):
        a=lo+(hi-lo)*j/800.0
        gap=stop_y(a)-stop_x(p0,a)
        min_gap=min(min_gap,gap)
        assert gap > -2e-12, (p0,a,gap)
        stoploss_cases+=1
    for t in ts:
        lhs=log_mgf_x(p0,t)
        rhs=0.0 if t==0.0 else -t-math.log1p(-t)
        assert lhs <= rhs+2e-12, (p0,t,lhs,rhs)
        mgf_cases+=1

print("VERIFY_OK stoploss_cases=%d mgf_cases=%d min_gap=%.3e" %
      (stoploss_cases,mgf_cases,min_gap))
