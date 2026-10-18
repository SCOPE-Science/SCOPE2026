"""Exact and numerical checks for a priced pendant-clique spectral-gap theorem.
Requires sympy and numpy.  Run: python verify_pendant_clique_20261014.py
"""
from itertools import combinations
import numpy as np
import sympy as sp

checks=0

def assert_equal(a,b):
    global checks
    d=sp.simplify(a-b)
    if isinstance(d,sp.MatrixBase):
        assert d.is_zero_matrix, (a,b)
    else:
        assert d==0,(a,b)
    checks+=1

def lap(m,x,y,z):
    N=m+2
    L=sp.zeros(N)
    for i in range(1,m+1):
        L[i,i]+=x; L[0,0]+=x; L[i,0]-=x; L[0,i]-=x
    for i,j in combinations(range(1,m+1),2):
        L[i,i]+=y; L[j,j]+=y;L[i,j]-=y;L[j,i]-=y
    L[0,0]+=z;L[m+1,m+1]+=z;L[0,m+1]-=z;L[m+1,0]-=z
    return L

def dual(m,q,alpha):
    P=sp.zeros(m+2)
    for i in range(1,m+1):
        for j in range(1,m+1):
            P[i,j]=int(i==j)-sp.Rational(1,m)
    u=sp.Matrix([1-m*q]+[1+2*q]*m+[-(m+1+m*q)])
    return alpha*P +u*u.T/(m+2)**2

for m in range(2,12):
    tc=sp.Rational(2*(m+1),m)
    for q in [sp.Rational(m+1,2*m),sp.Rational(2*m+1,3*m)]:
        if not (sp.Rational(1,m)<q<1): continue
        t=sp.Rational(2*m,m-1)*(1-q*q)
        assert t<tc
        x=(2+1/q)/(m+2)
        y=(m-1/q)/(m*(m+2))
        z=(m+1+m*q)/(m+2)
        L=lap(m,x,y,z)
        E=dual(m,q,t/2)
        assert_equal(L[0,0],m*x+z)
        assert_equal(L[m+1,m+1],z)
        assert_equal(sum(L[i,j] for i in range(m+2) for j in range(m+2)),0)
        assert_equal(m*y+x,1)
        assert_equal((m+1)*x+2*z-1,(m+2)*x*z)
        assert_equal(E.trace(),m*x+sp.Rational(m*(m-1),2)*t*y+z)
        assert_equal(E.trace(),m+1-(m*q-1)**2/(m+2))
        assert_equal(E*L,E)
        for i,j,p in [(0,1,sp.S(1)),(0,m+1,sp.S(1)),(1,2,t)]:
            v=sp.eye(m+2)[:,i]-sp.eye(m+2)[:,j]
            assert_equal((v.T*E*v)[0],p)
        eig=L.eigenvals()
        assert sp.S(1) in eig and eig[sp.S(1)]==m
        checks+=1
        assert sorted([float(v) for v in eig.keys()])[0]==0
        checks+=1
    # boundary and high prices, including equality and one large margin
    x=sp.S(1); y=sp.S(0); z=sp.S(1)
    E=dual(m,sp.Rational(1,m),sp.Rational(m+1,m))
    L=lap(m,x,y,z)
    assert_equal(E.trace(),m+1)
    assert_equal(E*L,E)
    for i,j,p in [(0,1,sp.S(1)),(0,m+1,sp.S(1)),(1,2,tc)]:
        v=sp.eye(m+2)[:,i]-sp.eye(m+2)[:,j]
        assert_equal((v.T*E*v)[0],p)
    assert L.eigenvals()=={0:1,1:m,m+2:1}
    checks+=1

rng=np.random.default_rng(20261014)
for m in range(2,10):
    edges=[(0,i,1.0) for i in range(1,m+1)] + [(i,j,None) for i,j in combinations(range(1,m+1),2)] + [(0,m+1,1.0)]
    for t in [0.1,0.9,1.9,2.5,5.0]:
        cost=np.array([c if c is not None else t for _,_,c in edges])
        q=np.sqrt(max(0.0,1-t*(m-1)/(2*m))) if t<2*(m+1)/m else 1/m
        if t<2*(m+1)/m:
            x=(2+1/q)/(m+2);y=(m-1/q)/(m*(m+2));z=(m+1+m*q)/(m+2)
            C=m*x+t*m*(m-1)*y/2+z
        else:
            x=1.0;y=0.0;z=1.0; C=m+1
        expected=1/C
        for _ in range(40):
            weights=rng.dirichlet(np.ones(len(edges))) /cost
            A=np.zeros((m+2,m+2))
            for (i,j,_),w in zip(edges,weights):
                A[i,i]+=w;A[j,j]+=w;A[i,j]-=w;A[j,i]-=w
            eig=np.linalg.eigvalsh(A)
            assert eig[1] <= expected + 1e-9,(m,t,eig[1],expected)
            checks+=1
        A=np.array(lap(m,sp.Rational(str(x)).limit_denominator(10**10),sp.Rational(str(y)).limit_denominator(10**10),sp.Rational(str(z)).limit_denominator(10**10))).astype(np.float64)
        ev=np.linalg.eigvalsh(A)
        assert abs(ev[1]-1)<1e-6,(m,t,ev[1])
        checks+=1
print('PASS',checks,'independent assertions across exact duals, spectra, budgets and random asymmetric edge allocations')
