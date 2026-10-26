"""Reproducibility checks for a three-state birth-death Lipschitz theorem.

Analytic proofs, not finite checks, establish the universal claims.
Requires Python 3, NumPy, SciPy.
"""
from math import cosh, sinh, exp, sqrt
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(241026)
checks = {'matrix': 0, 'transport': 0, 'stationary_envelope': 0,
          'monotonic': 0, 'contractivity': 0, 'limit': 0}

def setup(pi, c1, c2):
    u,v,w,z = c1/pi[0],c1/pi[1],c2/pi[1],c2/pi[2]
    Q=np.array([[-u,u,0.],[v,-v-w,w],[0.,z,-z]])
    B=np.array([[-u-v,w],[v,-w-z]])
    return Q,B,(u,v,w,z)

def closed(t,rates):
    u,v,w,z=rates
    ss=(u+v+w+z)/2
    dd=(u+v-w-z)/2
    de=sqrt(dd*dd+v*w)
    if de*t>400:
        return np.nan
    return exp(-ss*t)*(cosh(de*t)+max(w-dd,v+dd)*sinh(de*t)/de)

for _ in range(900):
    pi=rng.dirichlet([rng.uniform(.2,3.) for _ in range(3)])
    c1,c2=10**rng.uniform(-1.7,1.7,2)
    Q,B,rates=setup(pi,c1,c2)
    t=rng.uniform(.0001,2.0)/(max(-B[0,0],-B[1,1]))
    E=expm(t*B)
    F=expm(t*Q)
    N=np.max(E.sum(axis=1))
    C=closed(t,rates)
    assert abs(N-C)<2.e-11*(1+N), (N,C,pi,c1,c2,t)
    checks['matrix']+=1
    # Kantorovich-Rubinstein dual via exact one-dimensional cumulative transport.
    d01=F[0]-F[1]; d12=F[1]-F[2]
    w01=abs(d01[0])+abs(d01[0]+d01[1])
    w12=abs(d12[0])+abs(d12[0]+d12[1])
    assert abs(max(w01,w12)-N)<2.e-11*(1+N)
    checks['transport']+=1
    a=pi[0]/(pi[0]+pi[1]); b=pi[2]/(pi[1]+pi[2])
    assert E.sum(axis=1)[1] < 1+a*(1-exp(-(rates[0]+rates[1])*t))+2.e-12
    assert E.sum(axis=1)[0] < 1+b*(1-exp(-(rates[2]+rates[3])*t))+2.e-12
    assert N < 1+max(a,b)+2.e-12
    checks['stationary_envelope']+=1
    # Holding the invariant measure and opposite conductance fixed, increasing
    # the incident conductance decreases that edge's own norming row.
    Q2,B2,_=setup(pi,c1,c2*1.07)
    Q3,B3,_=setup(pi,c1*1.07,c2)
    assert expm(t*B2)[1].sum() <= E[1].sum()+2.e-12
    assert expm(t*B3)[0].sum() <= E[0].sum()+2.e-12
    checks['monotonic']+=1
    u,v,w,z=rates
    contract=(w<=u+v and v<=w+z)
    if contract:
        assert N<=1+2.e-12
    else:
        assert max(w-u-v,v-w-z)>0
        # The exact infinitesimal row derivative is positive. An
        # extremely short matrix exponential can round back to one.
        assert max(B.sum(axis=1)) > 0
    checks['contractivity']+=1

for pi in [np.array([1/3,1/3,1/3]),
           np.array([.6,.3,.1]), np.array([.01,.04,.95])]:
    for edge in range(2):
        # Weak-edge limit: fast side equilibrates on its edge, isolated leaf
        # retains its initial value over the selected time scale.
        eps=1.e-5
        c1,c2=(1.,eps**2) if edge==0 else (eps**2,1.)
        _,B,_=setup(pi,c1,c2)
        t=1/eps
        N=np.max(expm(t*B).sum(axis=1))
        want=1+(pi[0]/(pi[0]+pi[1]) if edge==0 else pi[2]/(pi[1]+pi[2]))
        assert abs(N-want)<2.e-3,(pi,edge,N,want)
        checks['limit']+=1

print('PASS',checks,'total',sum(checks.values()))
