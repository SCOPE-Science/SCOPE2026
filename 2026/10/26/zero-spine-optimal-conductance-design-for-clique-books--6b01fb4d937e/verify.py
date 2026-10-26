#!/usr/bin/env python3
"""Reproducible direct matrix and exact-arithmetic tests for two-hub clique books."""
import itertools
import math
from fractions import Fraction
import numpy as np
import sympy as S


def edges(m,s,a,b,c):
    n=2+m*s
    E=[(0,1,c)]
    for j in range(m):
        vs=range(2+j*s,2+(j+1)*s)
        for v in vs:
            E.extend(((0,v,a),(1,v,a)))
        E.extend((u,v,b) for u,v in itertools.combinations(vs,2))
    return n,E

def lap(n,E, exact=False):
    if exact:
        L=S.zeros(n)
        for i,j,w in E:
            L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
    else:
        L=np.zeros((n,n))
        for i,j,w in E:
            L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
    return L

def opt(m,s,B=1.0):
    n=2+m*s
    A=n*(m-1)/2+1
    Abar=A+n/(m*s)
    U=math.sqrt(m*(s+1)*Abar)
    V=m*(s-1)*math.sqrt(n/2)
    T=U+V
    a=B*math.sqrt(Abar/(m*(s+1)))/T
    y=B*math.sqrt(2*n)/T
    b=(y-2*a)/s
    return a,b,0.,T*T/B,y


def Kf(n,L):
    w=np.linalg.eigvalsh(L)
    assert abs(w[0])<1e-8
    assert w[1]>1e-10
    return n*np.sum(1/w[1:])

cnt=0
for m in range(2,8):
 for s in range(2,7):
    n=2+m*s
    a,b,c,t,y=opt(m,s)
    assert a>0 and b>0 and c==0 and y>2*a and y<m*s*a
    _,E=edges(m,s,a,b,c)
    L=lap(n,E)
    eig=np.linalg.eigvalsh(L)
    expected=np.array([0]+[n*a]+[m*s*a+2*c]+[2*a]*(m-1)+[2*a+s*b]*(m*(s-1)))
    assert np.allclose(eig,np.sort(expected),atol=1e-8,rtol=1e-10),(m,s)
    assert abs(sum(w for _,_,w in E)-1.)<1e-12
    assert abs(Kf(n,L)-t)<1e-8,(m,s,Kf(n,L),t)
    A=n*(m-1)/2+1; Abar=A+n/(m*s)
    lagrange=Abar/(m*(s+1)*a*a)
    mu=lagrange/2-n/(m*m*s*s*a*a)
    assert mu>0,(m,s,mu)
    cnt+=1
print('numeric families checked',cnt)

cnt=0
for m,s in [(2,2),(2,3),(3,2),(3,3),(4,2)]:
 n=2+m*s
 for a,b,c in [(S.Rational(2,3),S.Rational(1,7),S.Rational(1,5)),
                 (S.Rational(1,3),S.Rational(2,5),S.Integer(0))]:
    L=lap(n,edges(m,s,a,b,c)[1],exact=True)
    char=S.factor(L.charpoly().as_expr())
    t=S.Symbol('lambda')
    assert S.expand(char-t*(t-n*a)*(t-m*s*a-2*c)*(t-2*a)**(m-1)*(t-2*a-s*b)**(m*(s-1)))==0
    # exact Kirchhoff index from inverse is omitted for large cases but checked by rational char poly.
    cnt+=1
print('symbolic characteristic polynomials',cnt)

# independent derivative / convexity via finite difference in edge budgets for all first 6 families
cnt=0
for m,s in [(2,2),(2,3),(3,2),(3,3),(4,2),(4,3)]:
 n=2+m*s
 a,b,c,val,_=opt(m,s)
 _,E=edges(m,s,a,b,c)
 base=Kf(n,lap(n,E))
 for j in range(500):
    # fixed-random seed for genuine asymmetric allocations, budget normalized
    rng=np.random.default_rng(41723+10000*m+100*s+j)
    w=rng.dirichlet(np.ones(len(E)))
    E2=[(u,v,float(wi)) for (u,v,_),wi in zip(E,w)]
    alt=Kf(n,lap(n,E2))
    assert alt>base-1e-7,(m,s,j,alt,base)
    cnt+=1
print('asymmetric allocation comparisons',cnt)

# Check underlying exact arithmetic Kf identity for a small non-boundary and boundary example.
for m,s,a,b,c in [(2,2,S.Rational(1,4),S.Rational(1,5),S.Rational(1,3)),
                  (3,2,S.Rational(1,5),S.Rational(2,7),S.Integer(0))]:
 n=2+m*s
 L=lap(n,edges(m,s,a,b,c)[1],exact=True)
 R=n*(m-1)/(2*a)+1/a+n/(m*s*a+2*c)+n*m*(s-1)/(2*a+s*b)
 M=L+S.ones(n)/n
 exactK=S.factor(n*(S.trace(M.inv())-1))
 assert S.simplify(R-exactK)==0
 print('rational inverse-Kirchhoff identity',m,s,'passed')
print('PASS')
