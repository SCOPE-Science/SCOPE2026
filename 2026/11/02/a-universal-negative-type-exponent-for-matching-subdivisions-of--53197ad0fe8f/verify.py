"""Standalone distance-matrix checks for matching-edge subdivisions of cliques.

Requires Python 3 and NumPy. Finite tests corroborate (but do not prove)
the all-order theorem.
"""
import math
from collections import deque
import numpy as np


def graph_distances(r, t):
    m = 2*r+t
    n = m+r
    adj = [[] for _ in range(n)]
    for u in range(m):
        for v in range(u+1, m):
            if u < 2*r and u % 2 == 0 and v == u+1:
                continue
            adj[u].append(v)
            adj[v].append(u)
    for i in range(r):
        w = m+i
        for u in (2*i, 2*i+1):
            adj[u].append(w)
            adj[w].append(u)
    d = []
    for root in range(n):
        row = [-1]*n
        row[root] = 0
        todo=deque([root])
        while todo:
            u=todo.popleft()
            for v in adj[u]:
                if row[v]<0:
                    row[v]=row[u]+1
                    todo.append(v)
        assert min(row)>=0
        d.append(row)
    for u in range(n):
        for v in range(n):
            if u==v: expected=0
            elif u<m and v<m:
                expected=2 if (u<2*r and v==u^1) else 1
            elif u>=m and v>=m:
                expected=3
            else:
                w = u if u>=m else v
                core = v if u>=m else u
                expected=1 if core in (2*(w-m),2*(w-m)+1) else 2
            assert d[u][v]==expected, (r,t,u,v,d[u][v],expected)
    return np.array(d,dtype=float)


def critical():
    lo, hi=0.0,1.0
    def f(p):
        a=2**p; b=3**p
        return b*(2-a)-2*(a-1)**2
    for _ in range(72):
        mi=(lo+hi)/2
        if f(mi)>0: lo=mi
        else: hi=mi
    return (lo+hi)/2


def zero_sum_helmert(n):
    H=np.zeros((n,n-1))
    for j in range(1,n):
        H[:j,j-1]=1/math.sqrt(j*(j+1))
        H[j,j-1]=-j/math.sqrt(j*(j+1))
    assert np.max(np.abs(H.T@H-np.eye(n-1)))<1e-12
    assert np.max(np.abs(H.sum(axis=0)))<1e-12
    return H


def standard_matrix(p):
    a,b=2**p,3**p
    return np.array([[2*a-4,-2*(a-1)],[-2*(a-1),-b]])


def expected_global(p,r,t):
    a,b=2**p,3**p
    c=a-1; d=b-1; k=2*c-d
    if t:
        h=r/t
        return -r*np.array([[2*(1-c+2*h),2*(c+h)],
                             [2*(c+h),r*k+1+d+h]])
    return -2*r*(3-c+2*(r-1)*k)


def quadratic_global_numeric(D,p,r,t,x,z):
    m=2*r+t
    v=np.array([x]*(2*r) + [(-r*(2*x+z)/t) if t else 0]*t + [z]*r,float)
    assert abs(v.sum())<1e-9
    return float(v@np.where(D>0,D**p,0)@v)


def verify():
    p=critical()
    assert 0<p<1
    a,b=2**p,3**p
    assert abs(b*(2-a)-2*(a-1)**2)<2e-14
    assert 2*a-b-1>0
    cases=0
    for r in range(2,6):
        for t in (0,1,2,4):
            D=graph_distances(r,t)
            n=len(D)
            H=zero_sum_helmert(n)
            for exponent in (0.0,p-0.08,p,p+0.08,1.0):
                C=H.T@np.where(D>0,D**exponent,0)@H
                eig=np.linalg.eigvalsh(C)
                if exponent<p-1e-5:
                    assert eig[-1]<-1e-7,(r,t,exponent,eig[-1])
                elif exponent>p+1e-5:
                    assert eig[-1]>1e-7,(r,t,exponent,eig[-1])
                else:
                    assert np.sum(np.abs(eig)<2e-8)==r-1,(r,t,eig)
                    assert eig[-r]<-1e-5,(r,t,eig)
                cases+=1
            for x,z in ((1.,-2.), (0.2,-0.7),(-0.4,0.1)):
                if t==0 and abs(z+2*x)>1e-8:continue
                actual=quadratic_global_numeric(D,p,r,t,x,z)
                if t:
                    expected=float(np.array([x,z])@expected_global(p,r,t)@np.array([x,z]))
                else:
                    expected=expected_global(p,r,t)*x*x
                assert abs(actual-expected)<1e-8,(r,t,actual,expected)
                cases+=1
            A=standard_matrix(p)
            assert abs(np.linalg.det(A))<1e-12
            cases+=1
    print(f"PASS: critical exponent p={p:.15f}; {cases} independent structural and spectral checks across 16 graphs")

if __name__=='__main__': verify()
