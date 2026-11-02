#!/usr/bin/env python3
"""Finite exact-arithmetic cross-checks for a two-experiment chi-square theorem."""
from fractions import Fraction as F
from itertools import product
from math import sqrt

def chi2(P,Q):
    return sum((p-q)**2/q for p,q in zip(P,Q))

def tensor(A,B):
    return [a*b for a in A for b in B]

def model(a,b,m):
    a,b=F(a),F(b)
    m=F(m)
    Q=[m*m/(1+m*m),1/(1+m*m)]
    h=[-1/m,m]
    P1=[Q[i]*(1+a*h[i]) for i in range(2)]
    P2=[Q[i]*(1+b*h[i]) for i in range(2)]
    assert sum(P1)==sum(P2)==sum(Q)==1
    assert all(x>0 for x in P1+P2)
    return P1,P2,Q

def curve(s,t):
    return ((s+2*t)/2+(s+2*t)**2/16)/(s+t*t)

checks=0
A=[F(0),F(1,4),F(1,2),F(3,4),F(1),F(3,2),F(2),F(3)]
for a,b in product(A,A):
    if not a and not b: continue
    P1,P2,Q=model(a,b,7)
    M=[(x+y)/2 for x,y in zip(P1,P2)]
    original=chi2(tensor(P1,P2),tensor(Q,Q))
    homogeneous=chi2(tensor(M,M),tensor(Q,Q))
    s=a*a+b*b;t=a*b
    predicted=s+t*t
    numerator=(1+(s+2*t)/4)**2-1
    assert original==predicted and homogeneous==numerator
    assert homogeneous-original==(s-2*t)*(s+6*t-8)/16
    assert homogeneous/original==curve(s,t)
    if s<=2: assert homogeneous<=original
    checks+=5+(1 if s<=2 else 0)

# Angle deficit: independent and opposite score configurations on four atoms.
Q=[F(1,4)]*4
h1=[F(1),F(-1),F(1),F(-1)]
h2=[F(1),F(1),F(-1),F(-1)]
for z in [-1,0,1]:
    h=[(-x if z==-1 else h2[i] if z==0 else x) for i,x in enumerate(h1)]
    for a,b in product([F(1,4),F(1,2),F(3,4)],repeat=2):
        p1=[Q[i]*(1+a*h1[i]) for i in range(4)]
        p2=[Q[i]*(1+b*h[i]) for i in range(4)]
        M=[(x+y)/2 for x,y in zip(p1,p2)]
        s=a*a+b*b;t=a*b;c=F(z)
        lhs=chi2(tensor(M,M),tensor(Q,Q))-chi2(tensor(p1,p2),tensor(Q,Q))
        rhs=(s-2*t)*(s+6*t-8)/16-t*(1-c)*(4+s+t*(1+c))/4
        assert lhs==rhs
        checks+=1

# Direct numerical maximization verifies the interior root and critical window.
for T in [0.1,0.5,1,1.9,2,2.001,2.1,3,5,8,20,100]:
    root=(sqrt(T*(T+16))-T)/4
    opt=min(root,T/2)
    val=curve(T,opt)
    assert abs(val-max(curve(T,T*i/20000) for i in range(10001)))<2e-7
    assert (val>1+1e-10)==(T>2.001) or (2<T<=2.001 and val>=1)
    checks+=2
for delta in [0.01,0.003,0.001]:
    T=2+delta
    t=(sqrt(T*(T+16))-T)/4
    err=curve(T,t)-1
    assert abs(err/(delta*delta)-1/36)<0.0002
    checks+=1
print(f'PASS {checks} exact and numerical cross-checks')
