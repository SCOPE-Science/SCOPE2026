"""Independent finite-dimensional diagnostics for sharp distributed anchors.
Requires Python 3, numpy, scipy; invocation: python pinning_checker.py
No external data are needed.
"""
import math
import numpy as np
from scipy.optimize import minimize


def predicted(d, budget):
    M=(d+1)//2
    thresholds={1:float('inf')}
    for m in range(2,M+1):
        thresholds[m]=2*(d+2-2*m)/(m*(m-1))
    m=M
    while m>1 and budget>thresholds[m]:
        m-=1
    H=(d+1-m)/(budget+2/m)
    g=np.empty(d)
    for j in range(1,d+1):
        i=min(j,d+1-j)
        g[j-1]=(i*(m-i)/2+i*H/m) if i<m else H
    lap=2*g.copy()
    lap[:-1]-=g[1:]
    lap[1:]-=g[:-1]
    pins=np.where(g>=H-1e-11,(1-lap)/H,0.)
    pins=np.maximum(pins,0)
    f=m*(m*m-1)/6+(d+1-m)**2/(budget+2/m)
    return pins,f,g,m,H


def direct(d,pins):
    a=np.diag(2+pins)
    for j in range(d-1):
        a[j,j+1]=a[j+1,j]=-1
    return np.linalg.solve(a,np.ones(d))

assertions=0
for d in range(1,20):
    thresholds=[2*(d+2-2*m)/(m*(m-1)) for m in range(2,(d+1)//2+1)]
    budgets=[0,1e-9,1e-4,.01,.1,.6,1,3,15,100]+[t*f for t in thresholds for f in (.999999,1,1.000001)]
    for budget in budgets:
        pins,f,g,m,H=predicted(d,budget)
        rec=direct(d,pins)
        assert np.min(pins)>=-1e-10,(d,budget,pins)
        assert abs(pins.sum()-budget) < 1e-8*max(1,budget),(d,budget,pins,pins.sum())
        assert np.allclose(g,rec,atol=1e-8,rtol=1e-9),(d,budget,g,rec)
        assert abs(f-g.sum())<1e-8*max(1,f),(d,budget,f,g.sum())
        assert np.max(g[pins<1e-8],initial=0)<=np.max(g[pins>1e-8],initial=np.max(g))+1e-8
        assertions+=5
    if 2<=d<=9:
        for budget in [0.1,0.75,4.5,30.0]:
            pins,f,_,_,_=predicted(d,budget)
            def fun(p):return direct(d,p).sum()
            res=minimize(fun,np.full(d,budget/d),jac=lambda p:-direct(d,p)**2,bounds=[(0,budget)]*d,
                         constraints={'type':'eq','fun':lambda p:p.sum()-budget,'jac':lambda p:np.ones(d)},
                         method='SLSQP',options={'ftol':1e-11,'maxiter':500})
            assert res.success or abs(fun(res.x)-f)<1e-7,(d,budget,res)
            assert fun(res.x)>=f-2e-8, (d,budget,fun(res.x),f)
            assert np.linalg.norm(res.x-pins)<3e-4,(d,budget,res.x,pins)
            assertions+=3
print('PASS', assertions,'finite diagnostics over dimensions 1..19, transitions, and constrained optimizers')
