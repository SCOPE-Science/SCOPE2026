#!/usr/bin/env python3
"""Direct finite-cell checks for sharp balanced-event conditional-expectation commutator formula.
Run: python3 checker.py; uses only the Python standard library.
The finite tests corroborate, but do not replace, the analytical proof.
"""
import itertools
import math
import random
from fractions import Fraction as F

assertions=0

def ck(cond,msg):
    global assertions
    assert cond,msg
    assertions +=1

states=[(1,1),(-1,-1),(1,-1),(-1,1)]

for s in [F(1,9),F(1,3),F(3,5),F(9,10)]:
    a=(1+s)/2; b=(1-s)/2
    weights=[a/2,a/2,b/2,b/2]
    # Direct conditional means: P_X and P_Y, no use of rank-two formula.
    P=[[weights[j]*2 if states[j][0]==states[i][0] else F(0) for j in range(4)] for i in range(4)]
    Q=[[weights[j]*2 if states[j][1]==states[i][1] else F(0) for j in range(4)] for i in range(4)]
    matmul=lambda X,Y:[[sum((X[i][k]*Y[k][j] for k in range(4)),F(0)) for j in range(4)] for i in range(4)]
    PQ=matmul(P,Q); QP=matmul(Q,P)
    C=[[PQ[i][j]-QP[i][j] for j in range(4)] for i in range(4)]
    for i,j in itertools.product(range(4),repeat=2):
        x,y=states[i],states[j]
        K=s*(x[0]*y[1]-x[1]*y[0])
        ck(C[i][j]==weights[j]*K,'rank-two kernel mismatch')
    infty=max((sum(abs(z) for z in row) for row in C))
    one=max((sum(weights[i]*abs(C[i][j]) for i in range(4))/weights[j] for j in range(4)))
    ck(infty==s*(1+s),'L∞ matrix norm')
    ck(one==s*(1+s),'L1 matrix norm')
    trace=sum((weights[i]/weights[j])*C[i][j]**2 for i,j in itertools.product(range(4),repeat=2))
    ck(trace==2*s*s*(1-s*s),'Hilbert-Schmidt trace')
    def lp(v,p):
        if p==float('inf'): return max(abs(float(z)) for z in v)
        return sum(float(w)*abs(float(z))**p for w,z in zip(weights,v))**(1/p)
    def form(p):
        theta=min(1/p,1-1/p) if math.isfinite(p) else 0
        return 2*float(s)*float(a)**(1-theta)*float(b)**theta
    rng=random.Random(803+int(100*s))
    for p in (1.,1.5,2.,3.,4.,float('inf')):
        optimum=form(p)
        # Sharp two-cell antisymmetric witnesses, in complementary sectors.
        for z in ((1,-1,0,0),(0,0,1,-1)):
            Cz=[sum(float(C[i][j])*z[j] for j in range(4)) for i in range(4)]
            ck(lp(Cz,p)<=optimum*lp(z,p)+1e-10,'witness above formula')
        for _ in range(100):
            z=[rng.uniform(-1,1) for _ in range(4)]
            Cz=[sum(float(C[i][j])*z[j] for j in range(4)) for i in range(4)]
            ck(lp(Cz,p)<=optimum*lp(z,p)+1e-10,'numerical upper check')
        witnessed=max(lp([sum(float(C[i][j])*z[j] for j in range(4)) for i in range(4)],p)/lp(z,p) for z in ((1,-1,0,0),(0,0,1,-1)))
        ck(abs(witnessed-optimum)<1e-12,'sector witnesses attain the formula')

for p in (1.01,1.2,1.5,2,3,4,12,100):
    theta=min(1/p,1-1/p)
    sstar=((1-2*theta)+math.sqrt((1-2*theta)**2+8))/4
    ck(0<sstar<1,'interior optimizer')
    ck(abs(1+sstar*(1-2*theta)-2*sstar*sstar)<1e-12,'stationarity quadratic')
    def f(s): return 2*s*((1+s)/2)**(1-theta)*((1-s)/2)**theta
    for delta in (.001,.01,.1):
        for sb in (max(1e-8,sstar-delta),min(1-1e-8,sstar+delta)):
            ck(f(sstar)>f(sb),'unique-optimizer numerical control')

print(f'PASS: {assertions} exact rational and finite Lp consistency assertions')
