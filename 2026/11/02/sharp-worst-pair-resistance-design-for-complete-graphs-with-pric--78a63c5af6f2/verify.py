"""Reproducible checks for the worst-pair resistance matching-price theorem.
Run: python verify.py. Requires numpy, scipy and sympy.
"""
from fractions import Fraction
from math import sqrt
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar

checks=0

def chk(condition, label):
    global checks
    assert condition, label
    checks += 1

def edges(m):
    N=2*m
    return [(i,j, (i//2 == j//2)) for i in range(N) for j in range(i+1,N)]

def conductance(m,P,Q,B,t):
    y=B/(m*(P*t+(2*m-2)*Q))
    return t*y,y

def predicted_t(m,P,Q):
    r=P/Q
    lo=2*(m-1)/(2*m-1)
    if r<lo:
        return (sqrt((2*m-2)*(2*m)*(2/r-1))-(2*m-2))/2
    if r<=2: return 1.0
    return 0.0

def closed_worst(m,P,Q,B,t):
    x,y=conductance(m,P,Q,B,t)
    la=2*x+(2*m-2)*y
    lb=2*m*y
    return max(2/la,1/la+1/lb)

def full_worst(m, ws):
    E=edges(m); N=2*m
    L=np.zeros((N,N))
    for (i,j,_),w in zip(E,ws):
        L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
    inv=np.linalg.inv(L+np.ones((N,N))/N)-np.ones((N,N))/N
    return max(inv[i,i]+inv[j,j]-2*inv[i,j] for i in range(N) for j in range(i+1,N))

# Finite exact rational inverse identities; for every tested vertex pair, not just a sample.
for m in range(2,7):
    N=2*m
    for x,y in [(sp.Rational(0),sp.Rational(1)),(sp.Rational(1),sp.Rational(1)),(sp.Rational(3,2),sp.Rational(2,3))]:
        L=sp.zeros(N)
        for i,j,matched in edges(m):
            w=x if matched else y
            L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
        J=sp.ones(N)/N
        G=(L+J).inv()-J
        la=2*x+(N-2)*y; lb=N*y
        chk(la>0 and lb>0, 'connected graph in exact case')
        for i in range(N):
            for j in range(i+1,N):
                observed=sp.cancel(G[i,i]+G[j,j]-2*G[i,j])
                expected=2/la if i//2==j//2 else 1/la+1/lb
                chk(sp.simplify(observed-expected)==0,(m,i,j,x,y,observed,expected))

# Derivative identities for the two active-pair regimes (up to positive factors).
t,mm,P,Q,B=sp.symbols('t mm P Q B',positive=True)
A=2*mm-2;N=2*mm
y=B/(mm*(P*t+A*Q));la=(2*t+A)*y;lb=N*y
F1=2/la; F2=1/la+1/lb
D1=sp.factor(sp.diff(F1,t))
D2=sp.factor(sp.diff(F2,t))
chk(sp.simplify(D1-2*mm*A*(P-2*Q)/(B*(2*t+A)**2))==0,'matched derivative')
chk(sp.simplify(D2-mm/B*(A*(P-2*Q)/(2*t+A)**2+P/N))==0,'unmatched derivative')
chk(sp.simplify(F1.subs(t,1)-F2.subs(t,1))==0,'switch equality')
chk(sp.simplify(sp.solve(sp.factor(D2.subs(t,1)),P)[0]/Q-2*(mm-1)/(2*mm-1))==0,'low threshold')

rng=np.random.default_rng(17485)
for m in range(2,11):
    lo=2*(m-1)/(2*m-1)
    for r in [0.15,0.4,lo*0.9,lo, (lo+2)/2,1,1.6,2,2.01,3,8]:
        Q=1.0; P=r;B=2.3
        tstar=predicted_t(m,P,Q)
        W=closed_worst(m,P,Q,B,tstar)
        result=minimize_scalar(lambda z:closed_worst(m,P,Q,B,z),bounds=(0,10000),method='bounded',options={'xatol':1e-11})
        chk(W<=result.fun+max(1e-7,1e-7*W),(m,r,W,result.fun))
        for tt in [0,0.05,0.2,0.5,1,1.01,2,3,10,100,300]:
            chk(W <= closed_worst(m,P,Q,B,tt)+1e-8,(m,r,tt,W))
        if abs(r-2)<1e-10:
            for tt in [0,0.2,0.5,0.9,1.0]:
                chk(abs(closed_worst(m,P,Q,B,tt)-W)<1e-10,'r=2 flat interval')

# Independent full-matrix random allocations; not a proof, just a consistency check.
for m in [2,3,4,5]:
    E=edges(m)
    for r in [0.25,0.75,1,1.5,2,3.0]:
        P=r;Q=1;B=1.7
        tt=predicted_t(m,P,Q)
        x,y=conductance(m,P,Q,B,tt)
        ws=np.array([x if s else y for _,_,s in E],float)
        chk(abs(full_worst(m,ws)-closed_worst(m,P,Q,B,tt))<1e-8,'optimal matrix matches formula')
        cost=np.array([P if s else Q for _,_,s in E])
        for _ in range(30):
            u=rng.dirichlet(np.ones(len(E)))
            alternative=B*u/cost
            chk(full_worst(m,alternative)>=closed_worst(m,P,Q,B,tt)-1e-8,'random feasible')

# Critical window / fixed surcharge calculations.
for m in [1000,5000,10000]:
    for delta in [-1.0,0,0.25,0.75,1,1.25,2]:
        r=1+delta/m
        chk(abs(predicted_t(m,r,1)-max(1,0.5-delta))<0.005,'window limit')

print('PASS',checks,'exact algebraic / numerical assertions')
