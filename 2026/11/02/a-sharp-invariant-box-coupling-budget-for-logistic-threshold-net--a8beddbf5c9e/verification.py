#!/usr/bin/env python3
"""Reproduce arithmetic and numerical boundary diagnostics for a logistic network theorem.
This checks finite instances and identities; it does not replace the analytical proof.
"""
import math
from fractions import Fraction

def logistic(z):
    if z >= 0:
        return 1/(1+math.exp(-z))
    e=math.exp(z)
    return e/(1+e)

def parameters(beta):
    t=math.sqrt(1-4/beta)
    b=(1-t)/2
    E=(t-(1-t*t)*math.atanh(t))/(1+t)
    return t,b,E

def rate(beta,eps):
    _,b,_=parameters(beta)
    z=beta*(b+(1-b)*eps-0.5)
    p=logistic(z)
    return 1-beta*p*(1-p)

def check():
    W=[[.80,.05,.10,.05], [.05,.81,.01,.13], [.06,.04,.75,.15], [.11,.02,.12,.75]]
    assert all(abs(sum(r)-1)<1e-13 for r in W)
    exits=[sum(W[i][j] for j in (2,3)) if i<2 else sum(W[i][j] for j in (0,1)) for i in range(4)]
    assert all(abs(x-y)<1e-13 for x,y in zip(exits,[.15,.14,.10,.13]))
    for beta in [4.01,4.1,5,6,8,10,25,100,1000]:
        t,b,E=parameters(beta)
        assert 0 < b < .5 and 0 < E < 1
        assert abs(beta*b*(1-b)-1)<2e-11
        for frac in [.001,.1,.5,.99,.999999]:
            eps=E*frac
            z=beta*(b+(1-b)*eps-.5)
            assert z < math.log(b/(1-b))
            assert rate(beta,eps)>0
            assert logistic(z)<b
            assert logistic(-z)>1-b
        for eps in [E+(1-E)*.1,E+(1-E)*.9]:
            assert logistic(beta*(b+(1-b)*eps-.5))>b
    beta=8
    t,b,E=parameters(beta)
    assert .15<E<.16
    assert rate(8,.15)>0
    # Compute fixed points by contraction iteration for each pattern.
    roots=[]
    for signs in [(0,0),(0,1),(1,0),(1,1)]:
        x=[(b/2 if signs[i//2]==0 else 1-b/2) for i in range(4)]
        for k in range(50000):
            nx=[logistic(8*(sum(W[i][j]*x[j] for j in range(4))-.5)) for i in range(4)]
            delta=max(abs(nx[i]-x[i]) for i in range(4))
            x=nx
            if delta < 1e-14: break
        assert k<50000
        for i in range(4):
            assert 0<x[i]<b if signs[i//2]==0 else 1-b<x[i]<1
        roots.append(tuple(x))
    assert len(set(roots))==4
    # Universal sharpness for rectangle invariance at any crossing above E.
    for eps in [E+(1-E)*.01, E+(1-E)*.5, 1.0]:
        assert logistic(8*(b+(1-b)*eps-.5))>b
    # At the cusp, (beta-4)^3/2/12 is the leading asymptotic.
    for d in [1e-2,1e-3,1e-4]:
        ratio=parameters(4+d)[2] / (d**1.5/12)
        assert abs(ratio-1)<.20
    print('PASS: row sums, 4 non-equitable cross weights, 9 beta ranges, contraction, four numerical fixed points, sharpness and cusp checks')
    print('beta=8 b=%.14g E*=%.14g rate at eps=.15=%.14g'%(b,E,rate(8,.15)))
    for p,r in zip([(0,0),(0,1),(1,0),(1,1)],roots): print(p,tuple(round(v,10) for v in r))

if __name__=='__main__':check()
