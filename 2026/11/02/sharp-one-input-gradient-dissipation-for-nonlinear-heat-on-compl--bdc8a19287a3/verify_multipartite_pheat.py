#!/usr/bin/env python3
"""Standalone finite exact checks for multipartite nonlinear heat-flow edge-gradient formulas.

All mathematical statements quantified over arbitrary graph orders are established by
analytical inequalities in RESULT.md; finite checks here only test implementations.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt
import random

def edges_of(parts):
    labels = [i for i, a in enumerate(parts) for _ in range(a)]
    return [(i, j) for i in range(len(labels)) for j in range(i+1, len(labels)) if labels[i] != labels[j]], labels

def flux(z, p):
    if z == 0:
        return z
    return (1 if z > 0 else -1) * abs(z)**(p-1)

def flow(u, edges, p):
    out = [Q(0) for _ in u]
    for i,j in edges:
        q=flux(u[j]-u[i],p)
        out[i]+=q
        out[j]-=q
    return out

def tight_derivative(u,edges,p):
    L=max(abs(u[i]-u[j]) for i,j in edges)
    if not L:
        return Q(0), Q(0)
    F=flow(u,edges,p)
    deriv=max((F[i]-F[j] if u[i]>u[j] else F[j]-F[i]) for i,j in edges if abs(u[i]-u[j])==L)
    return L,deriv

def exact_gamma(a,b,k,p):
    d=abs(a-b)
    if p<=2 or d>=k:
        return Q(d-k-2)
    if p==3:
        return -Q(2)-Q(k*(k-d),2*k-d)
    raise ValueError('gamma needs numeric method for this exponent')

def witness(parts,i,j,p):
    a,b=parts[i],parts[j]
    d=abs(a-b); k=sum(parts)-a-b
    if a>b: i,j=j,i; a,b=b,a
    if p>2 and d<k:
        s = Q(k,2*k-d) if p==3 else k**(1/(p-2))/(k**(1/(p-2))+(k-d)**(1/(p-2)))
    else:
        s=Q(1)
    z=s if p>2 and d<k else Q(1)
    labels=[r for r,n in enumerate(parts) for _ in range(n)]
    u=[]; hit_i=hit_j=False
    for r in labels:
        if r==i:
            if not hit_i:
                u.append(Q(1));hit_i=True
            else:
                u.append(s)
        elif r==j:
            if not hit_j:
                u.append(Q(0));hit_j=True
            else:
                u.append(Q(1)+s)
        else:
            u.append(z)
    return u,labels

rng=random.Random(20261030)
checks=0
for parts in [(1,1), (1,3), (1,4), (2,2), (2,5), (3,3,1), (5,1,1,1),
              (6,1,1), (4,3,2), (2,2,2), (1,1,1,1), (3,4,5)]:
    E,labels=edges_of(parts)
    for p in (2,3,4):
        for _ in range(80):
            u=[Q(rng.randrange(-6,7),2) for i in labels]
            L,dL=tight_derivative(u,E,p)
            if not L: continue
            gamma=max(exact_gamma(parts[i],parts[j],sum(parts)-parts[i]-parts[j],p)
                      if p in (2,3) else
                      (max(abs(parts[i]-parts[j])-(sum(parts)-parts[i]-parts[j]),-1)-2)
                      for i in range(len(parts)) for j in range(i+1,len(parts)))
            if p in (2,3):
                assert dL <= gamma*L**(p-1), (parts,p,u,L,dL,gamma)
            elif 2*max(parts)<=sum(parts)+2:
                assert dL <= 0, (parts,p,u,L,dL)
            checks+=1
print('EXACT_RANDOM_EDGE_DERIVATIVE_INEQUALITIES_OK',checks)

wcheck=0
for parts in [(1,1), (1,4), (2,5), (3,3,1), (5,1,1,1), (6,1,1),
              (4,3,2), (2,2,2), (3,4,5), (1,1,1,1)]:
    E,lab=edges_of(parts)
    for i in range(len(parts)):
        for j in range(i+1,len(parts)):
            for p in (2,3):
                u,lab=witness(parts,i,j,p)
                L=max(abs(u[x]-u[y]) for x,y in E)
                assert L==1,(parts,i,j,p,u,L)
                F=flow(u,E,p)
                i0=lab.index(i);j0=lab.index(j)
                if parts[i]>parts[j]:i0,j0=j0,i0
                got=F[i0]-F[j0]
                exp=exact_gamma(parts[i],parts[j],sum(parts)-parts[i]-parts[j],p)
                assert got==exp,(parts,i,j,p,got,exp,u)
                wcheck+=1
print('EXACT_SHARP_WITNESS_IDENTITIES_OK',wcheck)

from scipy.integrate import solve_ivp
import numpy as np
for parts,p in [((6,1,1),3.),((7,1,1,1),1.5),((5,1,1,1),3.),((2,2,2),4.)]:
    E,lab=edges_of(parts)
    imax=parts.index(max(parts)); jnext=next(i for i in range(len(parts)) if i != imax)
    u,_=witness(parts,imax,jnext,3)
    y0=np.array([float(x) for x in u])
    edgearr=np.array(E)
    def f(t,y):
        d=y[edgearr[:,1]]-y[edgearr[:,0]]
        q=np.sign(d)*np.abs(d)**(p-1)
        out=np.zeros(len(y))
        np.add.at(out,edgearr[:,0],q)
        np.add.at(out,edgearr[:,1],-q)
        return out
    init=np.max(abs(y0[edgearr[:,0]]-y0[edgearr[:,1]]))
    res=solve_ivp(f,(0,1e-5),y0,rtol=1e-11,atol=1e-13)
    assert res.success
    final=np.max(abs(res.y[edgearr[:,0],-1]-res.y[edgearr[:,1],-1]))
    mustgrow=2*max(parts)>sum(parts)+2
    assert ((final>init) if mustgrow else (final<=init+1e-10)),(parts,p,init,final)
    print('FLOW_SHORT_TIME_CHECK_OK',parts,p,'growth',format(final/init-1,'.10g'))

def global_gamma(parts,p):
    N=sum(parts)
    sizes=sorted(parts,reverse=True)
    s,t=sizes[:2]
    if p<=2 or 2*s>=N:
        return float(2*s-N-2)
    v=p-2
    q=N-2*s
    r=N-s-t
    return -2-(q**(-1/v)+r**(-1/v))**(-v)

cases=0
for _ in range(70):
    count=rng.randint(2,6)
    parts=tuple(rng.randint(1,6) for i in range(count))
    E,lab=edges_of(parts)
    imax=max(range(count),key=lambda i:parts[i]);
    second=sorted((i for i in range(count) if i!=imax),key=lambda i:parts[i],reverse=True)[0]
    for p in (1.5,2,3,4,5):
        u,_=witness(parts,imax,second,p)
        assert abs(float(max(abs(u[i]-u[j]) for i,j in E))-1)<1e-10
        F=flow(u,E,p)
        x=lab.index(imax);y=lab.index(second)
        if parts[imax]>parts[second]:x,y=y,x
        rate=float(F[x]-F[y])
        goal=global_gamma(parts,p)
        assert abs(rate-goal)<2e-8,(parts,p,rate,goal)
        rate2=float(tight_derivative(u,E,p)[1])
        assert rate2 <= goal+2e-8,(parts,p,rate2,goal)
        for sample in range(10):
            ur=[Q(rng.randint(-10,10),4) for z in lab]
            L,dL=tight_derivative(ur,E,p)
            if L:
                assert float(dL) <= goal*float(L)**(p-1)+2e-8,(parts,p,L,dL,goal)
        cases+=1
print('GLOBAL_SHARP_RATE_FORMULA_OK',cases)
print('ALL_MULTIPARTITE_PHEAT_TESTS_OK')
