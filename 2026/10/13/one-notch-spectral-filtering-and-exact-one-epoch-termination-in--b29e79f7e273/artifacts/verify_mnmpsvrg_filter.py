#!/usr/bin/env python3
import math
import random


def P(m, q, theta):
    return ((1.0-theta*q)**m-(1.0-theta))/theta


def direct(m, q, theta, x0):
    x=x0
    snap=x0
    for _ in range(m):
        y=theta*x+(1.0-theta)*snap
        x=x-q*y
    return x

# Closed form versus direct scalar recurrence.
random.seed(34)
for _ in range(1000):
    m=random.randint(1,12)
    q=random.uniform(1e-5,0.499)
    theta=random.uniform(1e-4,0.9999)
    x0=random.uniform(-5,5)
    lhs=direct(m,q,theta,x0)
    rhs=P(m,q,theta)*x0
    assert abs(lhs-rhs) <= 2e-11*max(1.0,abs(lhs),abs(rhs))

# The admissible spectral notch is q_*=(1-u)/(1-u^m)=1/(1+...+u^(m-1)), u=(1-theta)^(1/m).
for m in range(2,12):
    for theta in (0.01,0.1,0.3,0.7,0.99):
        u=(1.0-theta)**(1.0/m)
        qstar=(1.0-u)/theta
        qstar2=1.0/sum(u**j for j in range(m))
        assert abs(qstar-qstar2)<1e-12
        assert qstar>1.0/m and qstar<1.0
        assert abs(P(m,qstar,theta))<2e-12

# Example inside the source algorithm's q<1/2 range: m=3, q=0.4.
def bisect_theta(m,q):
    lo=1e-14; hi=1.0
    flo=P(m,q,lo)
    fhi=P(m,q,hi)
    assert flo<0<fhi
    for _ in range(100):
        mid=(lo+hi)/2
        fm=P(m,q,mid)
        if fm<0: lo=mid
        else: hi=mid
    return (lo+hi)/2

theta=bisect_theta(3,0.4)
assert abs(theta-0.442810861169262)<1e-12
assert abs(direct(3,0.4,theta,2.75))<2e-13

# When m*q <= 1, no positive theta gives a zero; P is nonnegative and approaches 1-mq as theta->0.
for m in range(1,10):
    for q in (0.01, 0.5/m, 1.0/m if 1.0/m < 0.5 else 0.49):
        if q >= 0.5 or m*q>1+1e-14:
            continue
        vals=[P(m,q,j/1000.0) for j in range(1,1000)]
        assert min(vals)>-1e-12
        assert abs(P(m,q,1e-8)-(1.0-m*q))<2e-7

# Diagonal SPD check: each eigenmode follows the same transfer polynomial.
for eigs in ([1.0,2.0,4.0],[0.7,1.3,3.2]):
    eta=0.1/max(eigs)  # all q well inside (0,1/2)
    theta=0.37; m=7
    x0=[1.2,-0.4,2.1]
    x=x0[:]
    snap=x0[:]
    for _ in range(m):
        y=[theta*x[i]+(1-theta)*snap[i] for i in range(3)]
        x=[x[i]-eta*eigs[i]*y[i] for i in range(3)]
    rhs=[P(m,eta*eigs[i],theta)*x0[i] for i in range(3)]
    for a,b in zip(x,rhs):
        assert abs(a-b)<2e-12

print('VERIFY_OK')
