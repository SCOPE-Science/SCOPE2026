#!/usr/bin/env python3
"""Finite-state checks of exact fixation on uniform-petal hypergraph sunflowers.

All transition matrices below are independently assembled from the parent
reproduction rule. No candidate equation is used in constructing them.
"""
from itertools import product
from math import comb
import numpy as np

def formula(s,m,r):
    q=(r+s*m)/(r*(1+s*m*r))
    a=1/(1+(s*m/r)*sum(q**j for j in range(m)))
    b=a*m*(r+s*m)/(m*(r+s-1)+1)
    rho=(a+s*m*b)/(s*m+1)
    alternate=a*(m*r+s*m*m-m+1)/(m*r+m*(s-1)+1)
    assert abs(rho-alternate)<2e-14
    return np.array([a,b,rho])

def full_chain(s,m,r):
    n=1+s*m
    all0=(0,)*n; all1=(1,)*n
    states=[tuple(x) for x in product((0,1),repeat=n) if tuple(x) not in (all0,all1)]
    ix={x:i for i,x in enumerate(states)}
    a=np.eye(len(states)); b=np.zeros(len(states))
    for row,x in enumerate(states):
        total=n+(r-1)*sum(x)
        for parent in range(n):
            edges=range(m) if parent==0 else [(parent-1)//s]
            for petal in edges:
                y=list(x)
                for v in (0,*range(1+s*petal,1+s*(petal+1))):
                    y[v]=x[parent]
                y=tuple(y)
                w=(r if x[parent] else 1)/total/len(edges)
                if y==all1:b[row]+=w
                elif y!=all0:a[row,ix[y]]-=w
    v=np.linalg.solve(a,b)
    hub=(1,)+(0,)*(n-1)
    leaf=(0,1)+(0,)*(n-2)
    return np.array([v[ix[hub]],v[ix[leaf]],(v[ix[hub]]+s*m*v[ix[leaf]])/n])

def comps(s,m):
    if s==0:
        yield (m,)
    else:
        for k in range(m+1):
            for t in comps(s-1,m-k): yield (k,)+t

def symmetric_chain(s,m,r):
    n=1+s*m
    states=[(h,*co) for h in (0,1) for co in comps(s,m)]
    all0=(0,m,*([0]*s));all1=(1,*([0]*s),m)
    transient=[x for x in states if x not in (all0,all1)]
    ix={x:i for i,x in enumerate(transient)}
    a=np.eye(len(transient)); b=np.zeros(len(transient))
    for row,x in enumerate(transient):
        h,*co=x
        total=n+(r-1)*(h+sum(j*co[j] for j in range(s+1)))
        for j,count in enumerate(co):
            if not count: continue
            for t,w in ((h,count*(r if h else 1)/m),
                        (0,count*(s-j)),(1,count*j*r)):
                if w==0:continue
                new=co.copy();new[j]-=1;new[s*t]+=1
                y=(t,*new)
                if y==all1:b[row]+=w/total
                elif y!=all0:a[row,ix[y]]-=w/total
    v=np.linalg.solve(a,b)
    hub=(1,m,*([0]*s))
    leaf=(0,m-1,1,*([0]*(s-1)))
    return np.array([v[ix[hub]],v[ix[leaf]],(v[ix[hub]]+s*m*v[ix[leaf]])/n])

def main():
    ct=0
    for s in range(1,5):
      for m in range(1,5):
        for r in (0.5,1.,1.7,3.):
          theoretical=formula(s,m,r)
          reduced=symmetric_chain(s,m,r)
          assert np.max(np.abs(theoretical-reduced)) < 1e-10, (s,m,r,theoretical,reduced)
          ct+=3
          if 1+s*m<=8:
            direct=full_chain(s,m,r)
            assert np.max(np.abs(theoretical-direct)) < 1e-10,(s,m,r,theoretical,direct)
            ct+=3
    for s in range(1,10):
        for m in range(1,100):
            for r in (0.55,1.,1.01,1.5,3.):
                a,b,rho=formula(s,m,r)
                assert 0<a<=1 and 0<b<=1 and 0<rho<=1
                if m>1: assert b>a
                if r==1:
                    assert abs(a-1/(1+s*m*m))<1e-13
                    assert abs(b-m/(1+s*m*m))<1e-13
                    assert abs(rho-1/(1+s*m))<1e-13
                ct+=3
    print(f'PASS: {ct} independent Markov comparisons and formula consistency checks')

if __name__=='__main__':main()
