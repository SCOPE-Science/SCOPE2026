#!/usr/bin/env python3
"""Independent finite-path checks of a uniform-history relocation walk's centroid law.
Uses only Python's standard library; exact rational arithmetic where feasible.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import log

checks=0

def equal(a,b,msg):
    global checks
    assert a==b,(msg,a,b)
    checks+=1

def moment_recurrence(n,p,variance=F(1)):
    """Independent unconditional first/second moment recurrences.
    Returns E X_n^2 and E A_n^2 where A_n is the average of X_0,...,X_n.
    """
    v=F(0); q=F(0); t=F(0); s=F(0)
    values=[(v,s)]
    for k in range(1,n+1):
        y2=p*(v+variance)+(1-p)*q/k
        ty=p*t+(1-p)*s/k+y2
        sy=s+2*(ty-y2)+y2
        v=y2; q+=v; t=ty; s=sy
        values.append((v,s/F((k+1)**2)))
    return values

def enumerate_history(n,p,steps):
    """Exact trajectory-law recursion, independent of moment recurrence."""
    states={(0,):F(1)}
    for k in range(n):
        new=defaultdict(F)
        for path,mass in states.items():
            for step,prob in steps:
                new[path+(path[-1]+step,)]+=mass*p*prob
            for i in range(k+1):
                new[path+(path[i],)]+=mass*(1-p)/F(k+1)
        states=dict(new)
        equal(sum(states.values()),F(1),('normalization',n,k))
    vx=sum(weight*path[-1]**2 for path,weight in states.items())
    va=sum(weight*(F(sum(path),len(path)))**2 for path,weight in states.items())
    return vx,va,len(states)

for p in [F(1,3),F(1,2),F(2,3)]:
    vals=moment_recurrence(7,p)
    for n in range(1,8):
        v,s=vals[n]
        harmonic=sum((F(1,k) for k in range(1,n+1)),F(0))
        geometric=sum((p**k/F(k) for k in range(1,n+1)),F(0))
        equal(v,p/(1-p)*(harmonic-geometric),('exact endpoint MSD',p,n))
    for n in range(1,7):
        a,b,count=enumerate_history(n,p,[(-1,F(1,2)),(1,F(1,2))])
        equal(a,vals[n][0],('endpoint law',p,n,count))
        equal(b,vals[n][1],('centroid law',p,n,count))
    # Alternative symmetric steps with equal variance 1: ±2 with prob 1/8, zero with 3/4.
    for n in range(1,5):
        a,b,count=enumerate_history(n,p,[(-2,F(1,8)),(0,F(3,4)),(2,F(1,8))])
        equal(a,vals[n][0],('distribution universality endpoint',p,n,count))
        equal(b,vals[n][1],('distribution universality centroid',p,n,count))

# Large-N deterministic recurrence checks the exact limiting constant and log/n rate.
def long_check(p,n=500000):
    v=q=t=s=0.0
    u_mid=None
    for k in range(1,n+1):
        y2=p*(v+1.0)+(1-p)*q/k
        ty=p*t+(1-p)*s/k+y2
        sy=s+2*(ty-y2)+y2
        v=y2; q+=v; t=ty; s=sy
        if k==n//2: u_mid=s/(k+1)**2
    u=s/(n+1)**2
    L=p*(2+p)/(2*(1-p))
    B=p*(1+p)/(1-p)**2
    # Once the log/n correction is removed, the residual is of order 1/n.
    error1=(L-u_mid)-B*log(n//2)/(n//2)
    error2=(L-u)-B*log(n)/n
    assert abs(n*error2-(n//2)*error1)<0.2,(p,n*error2,(n//2)*error1)
    return n*error2
for p in [.2,.5,.75]:
    long_check(p)
    checks+=1
print(f'PASS: {checks} exact/computed assertions; independent history-law enumeration, endpoint moments, increment universality and logarithmic correction checks.')
