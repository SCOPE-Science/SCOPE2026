"""Reproducible numerical checks for Radon mean-projection bodies of boxes.
Requires numpy and scipy. Finite checks supplement, but do not replace, the proof.
"""
import math
import numpy as np
from scipy.optimize import minimize


def coefficient(d):
    return math.gamma((d-1)/2)/(math.sqrt(math.pi)*math.gamma(d/2))


def radii(a):
    """Exact formulas, with the unique squared maximizing normal."""
    a=np.asarray(a,dtype=float)
    d=len(a)
    low=float(min(a))
    high=float(max(a)*math.sqrt(d/(d-1))*2)
    for _ in range(120):
        mid=(low+high)/2
        phi=sum(max(0.0,1-(v/mid)**2) for v in a)
        if phi>1: high=mid
        else: low=mid
    lam=(low+high)/2
    t=np.array([max(0.,1-(v/lam)**2) for v in a])
    c=coefficient(d)
    r=c*(sum(a)-max(a))
    R=c*sum(a*np.sqrt(np.maximum(0.,1-t)))
    return r,R,t,lam


def support(a,u):
    return coefficient(len(a))*float(np.dot(a,np.sqrt(np.maximum(0,1-u*u))))

rng=np.random.default_rng(20261029)
checks=0
for d in (3,4,5,8):
    for _ in range(125):
        a=np.exp(rng.uniform(-1.5,1.5,d))
        r,R,t,lam=radii(a)
        assert abs(sum(t)-1)<1e-12
        assert np.all(t>=-1e-12)
        assert np.all(t<=1+1e-12)
        assert abs(support(a,np.sqrt(t))-R)<1e-10
        assert R/r+1e-12>=math.sqrt(d/(d-1))
        # An independently parameterized constrained maximization.
        def f(q):return coefficient(d)*np.dot(a,np.sqrt(np.maximum(0,1-np.asarray(q))))
        res=minimize(lambda q:-f(q),np.ones(d)/d,bounds=[(0,1)]*d,
                     constraints=[{'type':'eq','fun':lambda q:np.sum(q)-1}],
                     method='SLSQP',options={'ftol':1e-12,'maxiter':600})
        assert abs(-res.fun-R)<2e-6,(d,a,R,-res.fun)
        for _ in range(3):
            u=rng.normal(size=d);u/=np.linalg.norm(u)
            val=support(a,u)
            assert r-1e-9<=val<=R+1e-9
            # Independent Haar integration of projection-volumes, in u-perp.
            X=rng.normal(size=(6000,d));X-=np.outer(X@u,u)
            X/=np.linalg.norm(X,axis=1)[:,None]
            est=np.abs(X)@a
            assert abs(est.mean()-val)<0.15*(1+val)
            checks+=1
    ac=np.ones(d)
    r,R,t,lam=radii(ac)
    assert abs(R/r-math.sqrt(d/(d-1)))<1e-10
    assert np.max(abs(t-1/d))<1e-10
# Explicit three-dimensional transition.
for a in ([math.sqrt(2),1,1],[1.2,1,1],[2,1,1]):
    r,R,t,lam=radii(a)
    A,B,C=sorted(a,reverse=True)
    if A*A<=B*B+C*C:
        expected=math.sqrt(2*(A*A+B*B+C*C))
    else:
        expected=A+math.hypot(B,C)
    assert abs(R/coefficient(3)-expected)<1e-10
print(f'PASS: 500 independent constrained optimizations, {checks} random-direction/quadrature comparisons, equality and phase-boundary tests')
