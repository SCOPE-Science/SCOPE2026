#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt


def mat_entries(tau, sigma):
    one = Fraction(1, 1)
    a = one / (one + tau)
    b = -tau / (one + tau)
    c = sigma * (one - tau) / ((one + sigma) * (one + tau))
    d = (one + tau - 2 * tau * sigma) / ((one + sigma) * (one + tau))
    return a, b, c, d

# Exact rational trace/determinant/discriminant checks.
for tau, sigma in [(Fraction(1,3), Fraction(1,2)), (Fraction(2,5), Fraction(3,7)), (Fraction(3,4), Fraction(2,3))]:
    a,b,c,d = mat_entries(tau,sigma)
    p=tau*sigma
    s=tau+sigma
    den=1+s+p
    tr=a+d
    det=a*d-b*c
    assert tr == (s+2-2*p)/den
    assert det == (1-p)/den
    assert tr*tr-4*det == (s*s-8*p*(1-p))/(den*den)

# Coefficient-level polynomial identity:
# (4t^2+t-1)^2-(3t+1)^2(2t^2-1)=2(1-t)(1+t)^3.
def add(a,b):
    n=max(len(a),len(b)); out=[0]*n
    for i in range(n): out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return out
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out
def scale(a,c): return [c*x for x in a]
A=[-1,1,4]
B=[1,3]
C=[-1,0,2]
left=add(mul(A,A), scale(mul(mul(B,B),C),-1))
right=scale(mul([1,-1], mul([1,1],mul([1,1],[1,1]))),2)
assert left==right, (left,right)

# Deterministic probes of the phase diagram. These do not replace the proof.
def rho(tau,sigma):
    p=tau*sigma; s=tau+sigma; den=1+s+p
    tr=(s+2-2*p)/den
    det=(1-p)/den
    disc=tr*tr-4*det
    if disc <= 1e-14:
        return sqrt(det)
    return 0.5*(tr+sqrt(disc))

for p in [0.05,0.2,0.49]:
    mid=sqrt(2*p*(1-p)); gap=sqrt(p*(1-2*p))
    t1,t2=mid-gap,mid+gap
    pred=sqrt(1-p)/(sqrt(1-p)+sqrt(2*p))
    assert abs(t1*t2-p)<1e-12
    assert abs(rho(t1,t2)-pred)<1e-12
    # Nearby feasible sums on each side have no smaller radius.
    for fac in [0.95,1.05,1.2]:
        tau=t1*fac; sigma=p/tau
        assert rho(tau,sigma) >= pred-1e-12

for p in [0.5,0.6,0.9]:
    t=sqrt(p); pred=rho(t,t)
    for fac in [0.7,0.9,1.1,1.4]:
        tau=t*fac; sigma=p/tau
        assert rho(tau,sigma) >= pred-1e-12

global_tau=1/sqrt(2)
global_rho=rho(global_tau,global_tau)
assert abs(global_rho-(sqrt(2)-1))<1e-12
for p in [0.01,0.1,0.3,0.49,0.51,0.7,0.95]:
    if p<0.5:
        best=sqrt(1-p)/(sqrt(1-p)+sqrt(2*p))
    else:
        best=rho(sqrt(p),sqrt(p))
    assert best > global_rho-1e-12
print('VERIFY_OK')
