"""Exact and numerical checks for distance-radial spectra of Hadamard graphs."""
from collections import deque
import numpy as np
import sympy as sp
from scipy.linalg import hadamard

def graph(k):
    H=hadamard(k)
    A=np.zeros((4*k,4*k), dtype=int)
    for i in range(k):
        for j in range(k):
            for sign in range(2):
                a=2*i+sign
                b=2*k+2*j+(sign if H[i,j]==1 else 1-sign)
                A[a,b]=A[b,a]=1
    d=np.zeros_like(A)
    for a in range(4*k):
        row=[-1]*(4*k); row[a]=0
        queue=deque([a]);
        while queue:
            x=queue.popleft()
            for y in np.flatnonzero(A[x]):
                if row[y]<0:row[y]=row[x]+1;queue.append(y)
        assert -1 not in row
        d[a]=row
    return A,d

def calc(k):
    A,d=graph(k)
    assert len(d)==4*k
    assert np.array_equal(np.bincount(d[0],minlength=5),[1,k,2*(k-1),k,1])
    z=sp.symbols('z',real=True)
    t=sp.symbols('t',real=True)
    E={}
    for eigen, p in [(k,[1,k,2*(k-1),k,1]),(sp.sqrt(k),[1,sp.sqrt(k),0,-sp.sqrt(k),-1]),(0,[1,0,-2,0,1]),(-sp.sqrt(k),[1,-sp.sqrt(k),0,sp.sqrt(k),-1]),(-k,[1,-k,2*(k-1),-k,1])]:
        E[str(eigen)]=p
        for z0 in [sp.Rational(1,2),sp.Rational(1,3)]:
            B=sp.Matrix(np.where(d==0,1,np.array([float(z0)**int(r) for r in d.flatten()]).reshape(d.shape))) if False else None
        poly=sp.factor(sum(c*z**i for i,c in enumerate(p)))
        if eigen==-k:
            assert sp.factor(poly-(1-z)**2*(1-(k-2)*z+z*z))==0
        if eigen==0:assert sp.factor(poly-(1-z*z)**2)==0
    for pp in [sp.Rational(1,3),sp.Rational(1,2),sp.Rational(1)]:
        D=np.array([[float(int(e)**float(pp)) if e else 0.0 for e in row] for row in d])
        expected=sorted([float(sum(c*sp.Integer(i)**pp for i,c in enumerate(cs) if i>0)) for cs in E.values()])
        eigen=np.linalg.eigvalsh(D)
        for v in expected:assert min(abs(eigen-v))<1e-6,(k,pp,v)
    print('H',k,'PASS',sorted(E))
for k in [4,8,16]:calc(k)
