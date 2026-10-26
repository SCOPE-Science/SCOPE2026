"""Standalone rational and numerical checks for one-price D-optimal clique design."""
from fractions import Fraction
from itertools import combinations
import random
import sympy as sp
import numpy as np
from scipy.optimize import minimize

def optimum(n, r, B):
    r, B = sp.Rational(r), sp.Rational(B)
    if r < sp.Rational(n-1,n-2):
        h = sp.Rational(n-1) - sp.Rational(n-2,2)*r
        t = B/sp.Rational(n-1)
        a=t*(1/r-sp.Rational(n-2,2)/h)
        b=t/h
        c=t*2*(h-1)/(h*(n-2))
    else:
        a=sp.S.Zero
        b=2*B/(n-1)**2
        c=2*B*(n-3)/((n-1)**2*(n-2))
    return a,b,c

def edges(n):
    return list(combinations(range(n),2))

def graph_weights(n,a,b,c):
    ee=edges(n)
    return [a if (i,j)==(0,1) else b if i<2 or j<2 else c for i,j in ee]

def reduced_laplacian(n,vals):
    L=sp.zeros(n)
    for (i,j),val in zip(edges(n), vals):
        L[i,i]+=val;L[j,j]+=val;L[i,j]-=val;L[j,i]-=val
    return L[:n-1,:n-1]

checks=0
for n in range(4,10):
    critical=sp.Rational(n-1,n-2)
    for r in [sp.Rational(1,4),sp.Rational(1,2),sp.S.One,
              1+(critical-1)/2,critical,critical+sp.Rational(1,4),sp.Rational(3)]:
        B=sp.Rational(7,3)
        a,b,c=optimum(n,r,B)
        assert a>=0 and b>0 and c>0
        assert sp.simplify(r*a+2*(n-2)*b+sp.Rational((n-2)*(n-3),2)*c-B)==0
        tree=sp.factor(reduced_laplacian(n,graph_weights(n,a,b,c)).det(method='domain-ge'))
        factor=sp.factor(b*(2*a+(n-2)*b)*(2*b+(n-2)*c)**(n-3))
        assert sp.simplify(tree-factor)==0,(n,r,tree,factor)
        # Full gradient costs for each edge, verifying all KKT inequalities.
        L=reduced_laplacian(n,graph_weights(n,a,b,c))
        Linv=L.inv()
        price=[]; grad=[]
        for i,j in edges(n):
            v=sp.zeros(n-1,1)
            if i<n-1:v[i]=1
            if j<n-1:v[j]-=1
            val=sp.factor((v.T*Linv*v)[0])
            cp = r if (i,j)==(0,1) else 1
            price.append(cp);grad.append(val)
        dual=(n-1)/B
        for k,(val,cp,w) in enumerate(zip(grad,price,graph_weights(n,a,b,c))):
            assert sp.simplify(val-dual*cp)==0 if w>0 else sp.simplify(val-dual*cp)<=0
        checks+=1

# Evaluate derivative and direct optimization without assuming symmetry.
rng=np.random.default_rng(9217)
for n in [4,5,6,7]:
    ee=edges(n)
    D=np.zeros((n-1,len(ee)))
    for k,(i,j) in enumerate(ee):
        if i<n-1:D[i,k]+=1
        if j<n-1:D[j,k]-=1
    for r in [0.65,1.0,1+1/(3*(n-2)),(n-1)/(n-2),2.0]:
        prices=np.array([r if e==(0,1) else 1.0 for e in ee])
        a,b,c=map(float,optimum(n,sp.Rational(str(r)),sp.S.One))
        w0=np.array([float(x) for x in graph_weights(n,a,b,c)])
        def f(w):
            _, logdet=np.linalg.slogdet((D*w)@D.T)
            return -logdet if np.isfinite(logdet) else 1e50
        constraint={'type':'eq','fun':lambda w:prices@w-1.0,'jac':lambda w:prices}
        for _ in range(12):
            zz=rng.dirichlet(np.ones(len(ee)))*1/prices
            assert f(w0)<f(zz)+1e-9,(n,r,f(w0),f(zz))
        # numerical minimization from asymmetric point
        for _ in range(2):
            ww=rng.dirichlet(np.ones(len(ee)))/prices
            sol=minimize(f,ww,method='SLSQP',bounds=[(0,None)]*len(ee),constraints=[constraint],
                options={'ftol':1e-11,'maxiter':700})
            assert sol.success,(n,r,sol.message)
            assert abs(sol.fun-f(w0))<2e-7,(n,r,sol.fun,f(w0))
print(f'PASS: {checks} exact matrix-tree identities, budget, and all edge KKT derivatives; numerical unrestricted multi-start and asymmetric comparisons.')
