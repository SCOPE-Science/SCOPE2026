"""Finite computational checks of price-dependent Kirchhoff minimization on clique windmills.
Run with python verify.py. Requires numpy, scipy, sympy.
"""
from fractions import Fraction
from math import sqrt
import numpy as np
from scipy.optimize import minimize
import sympy as sp


def edges(s,r):
    spoke=[(0,1+i*r+j) for i in range(s) for j in range(r)]
    blade=[(1+i*r+j,1+i*r+k) for i in range(s) for j in range(r) for k in range(j+1,r)]
    return spoke,blade

def optimizer(s,r,p,q,budget=1.):
    M=s*r
    threshold=2*(M+1)/M
    if q/p>=threshold:
        return budget/(M*p),0.,threshold
    C=s-1+1/(M+1)
    z=sqrt(s*(2*r*p/q-(r-1))/C)
    a=budget/(M*p+s*r*(r-1)*q/2*((z-1)/r))
    b=(z-1)*a/r
    return a,b,threshold

def lap_trace(s,r,a,b):
    E,F=edges(s,r); n=1+s*r
    L=np.zeros((n,n))
    for (i,j),v in [(e,a) for e in E]+[(e,b) for e in F]:
        L[i,i]+=v;L[j,j]+=v;L[i,j]-=v;L[j,i]-=v
    lam=np.linalg.eigvalsh(L)
    return sum(1/t for t in lam[1:]),lam

def explicit_trace(s,r,a,b):
    n=1+s*r
    return s*(r-1)/(a+r*b)+(s-1+1/n)/a

def cost(s,r,a,b,p,q):
    return s*r*p*a+s*r*(r-1)/2*q*b

matrices=0; eigens=0
for s in (2,3,4):
  for r in (2,3,4):
    for a in (sp.Rational(1,3),sp.Rational(2,3),sp.Rational(2)):
      for b in (sp.Rational(0),sp.Rational(1,5),sp.Rational(3,2)):
        E,F=edges(s,r);n=1+s*r
        L=sp.zeros(n)
        for links,value in ((E,a),(F,b)):
          for i,j in links:
            L[i,i]+=value;L[j,j]+=value;L[i,j]-=value;L[j,i]-=value
        tr=(L+sp.ones(n)/n).inv().trace()-1
        expect=sp.Rational(s*(r-1),1)/(a+r*b)+(s-1+sp.Rational(1,n))/a
        assert sp.simplify(tr-expect)==0,(s,r,a,b,tr,expect)
        matrices+=1
        es=L.eigenvals()
        assert es.get(a+r*b,0)>=s*(r-1) # degeneracies add, valid even equal
        eigens+=1

numerical_cases=0; random_feasible=0; full_dim=0
rng=np.random.default_rng(360047)
for s,r in ((2,2),(2,3),(3,2),(3,3),(2,4)):
 for p,q in ((1.,1.),(1.,2.),(1.,2.4),(2.,5.),(1.,4.),(.4,.6)):
    B=10.
    a,b,th=optimizer(s,r,p,q,B)
    assert a>0 and b>=0 and np.isclose(cost(s,r,a,b,p,q),B)
    mine=explicit_trace(s,r,a,b)
    tr,_=lap_trace(s,r,a,b)
    assert np.isclose(mine,tr,rtol=1e-10)
    for j in range(100):
        # random edge conductances, individually adjustable, total budget B
        es,fs=edges(s,r)
        v=rng.dirichlet(np.ones(len(es)+len(fs))) *B/np.array([p]*len(es)+[q]*len(fs))
        L=np.zeros((1+s*r,1+s*r))
        for (u,w),c in zip(es+fs,v):
            L[u,u]+=c;L[w,w]+=c;L[u,w]-=c;L[w,u]-=c
        lam=np.linalg.eigvalsh(L)
        assert np.sum(1/lam[1:])>=mine-1e-8
        random_feasible+=1
    # Optimize all edges independently with finite-dimensional SLSQP to corroborate global value
    es,fs=edges(s,r); E=es+fs
    weights=np.array([p]*len(es)+[q]*len(fs))
    n=1+s*r
    def obj(v):
      L=np.zeros((n,n))
      for (u,w),c in zip(E,v):
        L[u,u]+=c;L[w,w]+=c;L[u,w]-=c;L[w,u]-=c
      eig=np.linalg.eigvalsh(L)
      if eig[1]<1e-8:return 1e12
      return np.sum(1/eig[1:])
    start=np.array([a]*len(es)+[max(b,1e-5)]*len(fs));start*=B/np.dot(weights,start)
    res=minimize(obj,start,method='SLSQP',bounds=[(0,None)]*len(E),constraints=[{'type':'eq','fun':lambda x:B-np.dot(weights,x)}],options={'maxiter':300,'ftol':1e-10})
    if not res.success and abs(res.fun-mine)>1e-4:
       raise AssertionError((s,r,p,q,res.message,res.fun,mine))
    assert abs(res.fun-mine)<2e-5,(s,r,p,q,res.fun,mine)
    full_dim+=1
    numerical_cases+=1

# Sample exactly on/above/below the analytic support transition.
thresholds=0
for s in (2,3,4,7):
 for r in (2,3,5):
    th=2*(s*r+1)/(s*r)
    for factor in (.999,1.,1.001,2.):
       a,b,tc=optimizer(s,r,1.,th*factor,5.)
       assert abs(tc-th)<1e-14
       assert (b>0)==(factor<1)
       assert np.isclose(explicit_trace(s,r,a,b),lap_trace(s,r,a,b)[0])
       thresholds+=1
print('PASS exact_grounded_spectral_comparisons=',matrices)
print('PASS independent_eigenspace_multiplicity_checks=',eigens)
print('PASS full_dimensional_SLSQP_runs=',full_dim)
print('PASS sampled_asymmetric_budgeted_feasible_allocations=',random_feasible)
print('PASS threshold_boundary_tests=',thresholds)
print('One case: s=3,r=2,p=1,q=1,B=10 ->', optimizer(3,2,1,1,10.))
print('One case: s=3,r=2,p=1,q=5/2,B=10 ->', optimizer(3,2,1,2.5,10.))
