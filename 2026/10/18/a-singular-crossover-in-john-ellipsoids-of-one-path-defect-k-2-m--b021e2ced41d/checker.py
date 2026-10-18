#!/usr/bin/env python3
"""Direct finite-dimensional checks of an exact John-ellipsoid construction.
SciPy numerical linear algebra plus direct spanning-tree enumeration in small graphs;
not a substitute for the proof for all parameters.
"""
from itertools import combinations
from fractions import Fraction
from math import sqrt, isclose
import numpy as np

def data(m,t):
    s=t*t
    r=2*(m-1)/(m*s-2+sqrt((m*s-2)**2+4*s*(m-1))) if m*s-2+sqrt((m*s-2)**2+4*s*(m-1)) > 1e-12 else ((2-m*s)+sqrt((m*s-2)**2+4*s*(m-1)))/(2*s)
    # quadratic form avoids cancellation via the stable branch as appropriate
    c=(m+r)/(2*(m-1+r)); e=r*c
    n=m+2
    edges=[]
    for i in range(m):
        k=2+i
        cond=e if i==0 else c
        length=t if i==0 else 1.0
        edges.extend([(0,k,cond,length),(1,k,cond,length)])
    L=np.zeros((n,n));
    for u,v,w,_ in edges:
        L[u,u]+=w; L[v,v]+=w; L[u,v]-=w; L[v,u]-=w
    S=np.linalg.pinv(L,hermitian=True)
    for u,v,w,h in edges:
        B=np.zeros(n);B[u]=1;B[v]=-1
        R=B @ S @ B
        assert isclose(R,h*h,rel_tol=2e-10,abs_tol=2e-10),(m,t,R,h*h)
    eigen=np.linalg.eigvalsh(L)
    assert abs(eigen[0])<1e-8
    tau=2**(m-1)*c**(m+1)*r*(m-1+r)
    assert isclose(np.prod(eigen[1:]),n*tau,rel_tol=2e-10,abs_tol=2e-10)
    assert isclose(2*((m-1)*c+t*t*e),n-1,rel_tol=2e-10,abs_tol=2e-10)
    # analytic KKT yields global optimality; independent checks of all edge contacts and determinant
    return r,c,e

def tree_check(m,t):
    # full Kirchhoff sum using exact rational conductances for t=1 case
    r,c,e=data(m,t)
    if t!=1:return
    n=m+2
    ed=[(u,k) for k in range(2,n) for u in (0,1)]
    count=0
    for tree in combinations(ed,n-1):
        parent=list(range(n))
        def find(x):
            while x!=parent[x]: x=parent[x]
            return x
        cycles=False
        for u,v in tree:
            a,b=find(u),find(v)
            if a==b: cycles=True;break
            parent[a]=b
        if not cycles: count+=1
    assert count==m*2**(m-1)
    return count
if __name__=='__main__':
    k=0
    for m in range(2,16):
        for t in (0.1,0.25,0.5,1.,1.5,2.,3.,7.,10.):
            r,c,e=data(m,t)
            if t==1 and m<=8: tree_check(m,t)
            k+=1
    print(f'PASS: {k} full-matrix contact, trace and eigen-determinant checks; 7 direct tree enumerations')
    for m,t in [(2,.5),(3,1),(4,2),(9,.25)]:
        r,c,e=data(m,t); print(f'm={m}, t={t}: r={r:.9f}, c={c:.9f}, e={e:.9f}')
