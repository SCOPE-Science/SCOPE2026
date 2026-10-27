"""Standalone finite checks of a weighted spanning-tree budget theorem on parallel-path networks."""
import itertools
from fractions import Fraction
from math import prod
import numpy as np
from scipy.optimize import minimize, brentq
import sympy as sp

def weights(lengths,B=1.0):
    m=len(lengths); d=[l-1 for l in lengths]; rho=1+sum(d); S=sum(1/(l+1) for l in lengths)
    if S<=1:
        return B*(1-S)/rho, [B*l/(rho*(l+1)) for l in lengths], None
    def fun(x):return sum((l-1)/(x*l*l-1) for l in lengths)-1
    root=brentq(fun, max(1.,max(1/(l*l) for l in lengths))+1e-10, max(2.0,len(lengths)),xtol=1e-14)
    return 0., [B*(l-1)*root*l/(rho*(root*l*l-1)) for l in lengths], root

def graph(lengths):
    edges=[(0,1)]
    n=2
    paths=[]
    for l in lengths:
        curr=0; branch=[]
        for j in range(l-1):
            edges.append((curr,n));branch.append(len(edges)-1);curr=n;n+=1
        edges.append((curr,1)); branch.append(len(edges)-1)
        paths.append(branch)
    return n,edges,paths

def tau_det(n,edges,ew):
    L=sp.zeros(n)
    for (u,v),w in zip(edges,ew):
        L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
    return L[1:,1:].det()

def product_tau(lengths,w0,wi):
    return prod(sp.Integer(l)*w**(l-1) for l,w in zip(lengths,wi))*(w0+sum(w/sp.Integer(l) for l,w in zip(lengths,wi)))

def fastlogdet(n,edges,ww):
    L=np.zeros((n,n))
    for (u,v),w in zip(edges,ww):
        L[u,u]+=w; L[v,v]+=w; L[u,v]-=w; L[v,u]-=w
    sign, ld=np.linalg.slogdet(L[1:,1:]); return ld if sign>0 else -1e90

records=[]
for lengths in [(2,),(2,3),(2,2,2),(2,2,2,2),(3,3,3,3),(2,2,4,7),(5,5,5,5,5,5),(2,2,2,3),(2,3,4,5)]:
    n,edges,paths=graph(lengths)
    B=sp.Rational(1,1)
    w0,wi,root=weights(lengths)
    ww=[w0]+[0]*(len(edges)-1)
    for j,branch in enumerate(paths):
        for k in branch: ww[k]=wi[j]
    assert abs(sum(ww)-1.0)<2e-12
    opt=fastlogdet(n,edges,ww)
    formula=float(product_tau(lengths,w0,wi))
    assert abs(np.exp(opt)-formula)/formula<1e-9
    # Full unsymmetrized numerical optimization; all edge costs independently varied.
    res=minimize(lambda z:-fastlogdet(n,edges,z), np.array([1/len(edges)]*len(edges)),
       bounds=[(0,1)]*len(edges), constraints={'type':'eq','fun':lambda z:np.sum(z)-1},
       method='SLSQP', options={'maxiter':500,'ftol':1e-12})
    assert res.success, (lengths,res.message)
    assert -res.fun <= opt+1e-7, (lengths,-res.fun,opt)
    assert np.max(np.abs(res.x-np.array(ww)))<3e-4, (lengths,res.x,ww)
    records.append((lengths,'positive' if w0>1e-12 else 'deleted',round(w0,9),round(opt,9)))

# Rational matrix-tree checks and permutation invariance in every path.
rat_cases=[((2,2,2),[sp.Rational(1,10),sp.Rational(1,7),sp.Rational(2,5)]),
           ((2,3),[sp.Rational(1,11),sp.Rational(2,9)]),
           ((2,3,4),[sp.Rational(1,9),sp.Rational(3,10),sp.Rational(2,11)])]
for lengths,_ in rat_cases:
    n,edges,paths=graph(lengths)
    ew=[sp.Rational(2,7)]+[sp.Rational(j+1,7+j) for j in range(1,len(edges))]
    products=[prod(ew[e] for e in branch) for branch in paths]
    broken=[sum(prod(ew[e] for e in branch if e!=cut) for cut in branch) for branch in paths]
    # Correct direct-edge-present formula: trees with direct edge + each long path broken once,
    # or one intact long path, with direct edge deleted.
    enumerator=ew[0]*prod(broken)+sum(products[i]*prod(broken[j] for j in range(len(paths)) if j!=i) for i in range(len(paths)))
    assert tau_det(n,edges,ew)==enumerator
    for j,path in enumerate(paths):
        perm=list(ew); perm[path[0]],perm[path[-1]]=perm[path[-1]],perm[path[0]]
        assert tau_det(n,edges,perm)==enumerator

print('finite configurations:',len(records),'rational determinant/permutation cases:',len(rat_cases),'PASS')
for rec in records:print(*rec)
