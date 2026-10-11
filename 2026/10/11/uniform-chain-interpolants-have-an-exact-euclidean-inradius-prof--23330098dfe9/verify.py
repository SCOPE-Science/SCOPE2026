#!/usr/bin/env python3
import math
import numpy as np
from scipy.optimize import linprog

def profile(m,t):
    N=[1.0]
    for j in range(1,m):
        N.append(math.sqrt(
            1.0+(1.0-t)**2*sum(t**(2*r) for r in range(j))
        ))
    N.append(math.sqrt(sum(t**(2*r) for r in range(m))))
    radius=1.0/sum(N)

    X=[0.0]
    for i in range(1,m+1):
        X.append(radius*sum(N[:i]))
    y=np.array([X[i]-t*X[i-1] for i in range(1,m+1)])
    return np.array(N),radius,y

for m in range(2,13):
    for t in (0.0,0.07,0.25,0.5,0.73,0.93,1.0):
        N,r,y=profile(m,t)

        # Variables are y_1,...,y_m,rho.
        # Each row encodes -slack_j + rho*N_j <= 0,
        # except the top facet, whose constant is one.
        A=[]
        b=[]

        row=np.zeros(m+1)
        row[0]=-1.0
        row[-1]=N[0]
        A.append(row)
        b.append(0.0)

        for j in range(1,m):
            row=np.zeros(m+1)
            row[j]=-1.0
            for i in range(j):
                row[i]+=(1.0-t)*t**(j-1-i)
            row[-1]=N[j]
            A.append(row)
            b.append(0.0)

        row=np.zeros(m+1)
        for i in range(m):
            row[i]=t**(m-1-i)
        row[-1]=N[m]
        A.append(row)
        b.append(1.0)

        c=np.zeros(m+1)
        c[-1]=-1.0
        lp=linprog(
            c,
            A_ub=np.array(A),
            b_ub=np.array(b),
            bounds=[(None,None)]*m+[(0.0,None)],
            method="highs"
        )
        assert lp.success,(m,t,lp.message)
        assert abs(lp.x[-1]-r)<3e-10,(m,t,lp.x[-1],r)
        assert np.max(np.abs(lp.x[:-1]-y))<3e-9,(m,t)

    # Endpoint values and derivatives.
    N0,r0,_=profile(m,0.0)
    N1,r1,_=profile(m,1.0)
    assert abs(r0-1.0/(2.0+(m-1)*math.sqrt(2.0)))<1e-14
    assert abs(r1-1.0/(m+math.sqrt(m)))<1e-14

    h=1e-7
    D0=sum(profile(m,0.0)[0])
    Dh=sum(profile(m,h)[0])
    deriv0=(Dh-D0)/h
    target0=-(m-1)/math.sqrt(2.0)
    assert abs(deriv0-target0)<2e-5

    D1=sum(profile(m,1.0)[0])
    Dm=sum(profile(m,1.0-h)[0])
    deriv1=(D1-Dm)/h
    target1=(m-1)*math.sqrt(m)/2.0
    assert abs(deriv1-target1)<2e-4

# Exact two-dimensional optimum.
m=2
t=0.5
_,r,_=profile(m,t)
assert abs(r-1.0/(1.0+math.sqrt(5.0)))<1e-14
for q in np.linspace(0.0,1.0,1001):
    _,rq,_=profile(m,float(q))
    assert rq <= r+1e-13

print("VERIFY_OK uniform-chain-interpolant-inradius m=2..12 full_chebyshev_lp=yes endpoint_slopes=yes midpoint_2d=yes")
