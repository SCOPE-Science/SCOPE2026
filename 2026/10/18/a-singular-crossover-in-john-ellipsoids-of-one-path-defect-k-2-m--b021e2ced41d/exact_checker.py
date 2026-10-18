#!/usr/bin/env python3
"""Exact symbolic Laplacian checks; requires SymPy."""
import sympy as sp

def check(m,t):
    t=sp.Rational(t)
    s=t*t
    delta=(m*s-2)**2+4*s*(m-1)
    r=sp.simplify((2-m*s+sp.sqrt(delta))/(2*s))
    a=sp.simplify((m+r)/(2*(m-1+r)))
    b=sp.simplify(r*a)
    n=m+2
    L=sp.zeros(n)
    for i in range(m):
        for u in [0,1]:
            v=i+2; g=b if i==0 else a
            L[u,u]+=g;L[v,v]+=g;L[u,v]-=g;L[v,u]-=g
    # Grounds the last vertex, evaluates voltage differences exactly.
    inv=L[:n-1,:n-1].inv()
    for i in range(m):
        for u in (0,1):
            v=i+2
            vec=sp.zeros(n-1,1)
            if u<n-1:vec[u]=1
            if v<n-1:vec[v]=-1
            R=sp.simplify((vec.T*inv*vec)[0])
            desired=t*t if i==0 else sp.Integer(1)
            assert sp.simplify(R-desired)==0,(m,t,i,u,R)
    tau=sp.simplify(2**(m-1)*a**(m+1)*r*(m-1+r))
    assert sp.simplify(L[:n-1,:n-1].det()-tau)==0
    assert sp.simplify(2*((m-1)*a+s*b)-(m+1))==0
    return (m,str(t))

if __name__=='__main__':
    cases=[(2,'1/2'),(2,'2'),(3,'3/2'),(4,'1/3'),(5,'1')]
    for m,t in cases:
        print('PASS',check(m,t))
