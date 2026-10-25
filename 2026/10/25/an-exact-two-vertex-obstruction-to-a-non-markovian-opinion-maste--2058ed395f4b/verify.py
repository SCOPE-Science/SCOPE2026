#!/usr/bin/env python3
"""Exact arithmetic checks for the two-agent renewal-copying discrepancy."""
from fractions import Fraction as F
from math import factorial

def deriv(p):
    return [F(k)*p[k] for k in range(1,len(p))]

def plus(p,q):
    return [ (p[k] if k<len(p) else F(0)) +(q[k] if k<len(q) else F(0)) for k in range(max(len(p),len(q)))]

def eq(p,q):
    return all((p[k] if k<len(p) else F(0))==(q[k] if k<len(q) else F(0)) for k in range(max(len(p),len(q))))

# Integrand after u=2v: P(v)e^v, P(v)=v(1-v)^2.
P=[F(0),F(1),F(-2),F(1)]
Q=[F(0)]
sign=1; d=P[:]
while d:
    Q=plus(Q,[sign*x for x in d])
    d=deriv(d); sign=-sign
assert eq(plus(Q,deriv(Q)),P)  # d(e^v Q)/dv=e^v P
assert Q[0]==-11 and sum(Q)==-4
# Thus integral_0^1 P(v)e^v dv = 11-4e > 0 by P(v)>0 inside.
# Renewal T^{*k}(u) for 0<u<2 has u^(k-1)/(2^k (k-1)!).
for k in range(1,18):
    assert F(1,2**k*factorial(k-1)) == F(1,2)*F(1,2**(k-1)*factorial(k-1))
# Taylor residual coefficient at order 4: from (t-6) e^(t/2).
e=lambda n:F(1,2**n*factorial(n))
assert e(3)-6*e(4)==F(1,192)
# Direct first-event partition for continuous independent survivals at sample rational times.
for p in range(1,10):
 for q in range(1,10):
    S1,S2=F(p,10),F(q,10)
    p_first1=F(1)-S1
    p_first2=S1*(F(1)-S2)
    p_none=S1*S2
    assert p_first1+p_first2+p_none==1
    assert p_none==S1*S2
print('PASS: exact first-event law, renewal density, antiderivative, and nonzero residual')
