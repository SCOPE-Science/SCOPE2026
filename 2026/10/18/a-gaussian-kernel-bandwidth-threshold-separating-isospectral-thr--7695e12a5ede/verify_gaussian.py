#!/usr/bin/env python3
"""Checks for the Gaussian-MMD threshold of two three-state Markov chains.
Standard library only. Exact fractions check finite algebra; the accompanying
proof establishes every-bandwidth and limiting claims.
"""
from fractions import Fraction as F
from math import exp, log, sqrt

J=F(1,3)
P_adj=((F(7,12),F(1,12),J),
       (F(1,12),F(7,12),J),
       (J,J,J))
P_end=((F(7,12),J,F(1,12)),
       (J,J,J),
       (F(1,12),J,F(7,12)))
for P in (P_adj,P_end):
    assert all(sum(row)==1 and min(row)>0 for row in P)
    assert all(P[i][j]==P[j][i] for i in range(3) for j in range(3))
    assert max(sum(abs(P[i][k]-P[j][k]) for k in range(3))/2
               for i in range(3) for j in range(3))==F(1,2)

def action(P,v):
    return tuple(sum(P[i][j]*v[j] for j in range(3)) for i in range(3))
assert action(P_adj,(1,-1,0))==(F(1,2),F(-1,2),F(0))
assert action(P_adj,(1,1,-2))==(0,0,0)
assert action(P_end,(1,0,-1))==(F(1,2),F(0),F(-1,2))
assert action(P_end,(1,-2,1))==(0,0,0)

def R(t):
    return t*t*(1+t+t*t)**2/(3+2*t+2*t*t+2*t**3)

def gram_det(t):
    # a = u^T K u, b = v^T K v, and c^2=(u^T K v)^2.
    a=1-t
    b=1-t/F(3)-F(2,3)*t**4
    c2=(t-t**4)**2/F(3)
    return a,b,c2,a*b-c2

checks=0
for k in range(1,1000):
    t=F(k,1000)
    a,b,c2,det=gram_det(t)
    assert a>0 and b>0 and det>0
    assert c2/(a*b)==R(t)
    # The general rank-one generalized-Rayleigh-quotient result.
    assert a*b/(4*det)==F(1,4)/(1-R(t))
    checks+=1

# The exact phase-transition polynomial and a rigorous bracketing.
def q(t):
    return 4*t**6+8*t**5+12*t**4+2*t**3-2*t**2-6*t-9
assert q(F(8977,10000))<0 and q(F(8978,10000))>0
assert R(F(8977,10000))<F(3,4)<R(F(8978,10000))
assert R(F(1,10))<R(F(1,2))<R(F(9,10))<R(F(99,100))
# Analytic derivative factor (all coefficients and factors are positive on (0,1)).
for k in range(1,100):
    t=F(k,100)
    num=2*t*(t*t+t+1)*(3*t*t+2*t+1)*(t**3+t*t+t+3)
    den=(2*t**3+2*t*t+2*t+3)**2
    # Numerical finite difference is only a cross-check of exact derivative formula.
    dt=1e-6
    assert abs(float(num/den)- (float(R(t+F(1,1000000)))-float(R(t-F(1,1000000))))/(2*dt))<1e-7
    checks+=1

# Numerically check the full Gaussian-MMD ratio against the finite matrix law.
def mmd_sq(vec, kernel):
    return sum(vec[i]*kernel[i][j]*vec[j] for i in range(3) for j in range(3))
for h in (0.0001,0.01,0.05,0.10790643085271807,0.2,1.,4.):
    t=exp(-h)
    kernel=[[1.,t,t**4],[t,1.,t],[t**4,t,1.]]
    # Obtain the maximizing signed vector in u,v coordinates using inverse Gram.
    a,b,c2,det=gram_det(t)
    c=(t-t**4)/sqrt(3)
    z1=float(b); z2=-c
    u=(1/sqrt(2),-1/sqrt(2),0.)
    v=(1/sqrt(6),1/sqrt(6),-2/sqrt(6))
    signed=[z1*u[i]+z2*v[i] for i in range(3)]
    transformed=[sum(float(P_adj[j][i])*signed[j] for j in range(3)) for i in range(3)]
    gain2=mmd_sq(transformed,kernel)/mmd_sq(signed,kernel)
    assert abs(gain2-1/(4*(1-float(R(t)))))<1e-5*max(1,gain2)
    # Reflection-compatible operator is tested by exact eigenvectors above.
    checks+=1
print('PASS:',checks,'exact and finite-state numerical checks; two positive reversible chains;')
print('PASS: exact rational threshold bracket, polynomial identity and sharp MMD gain.')
