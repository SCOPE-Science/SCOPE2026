#!/usr/bin/env python3
"""Independent finite checks of Fourier/PBH rank law for uniformly decorated cycles."""
import math, random, numpy as np
from fractions import Fraction
from sympy import Matrix

def lap(n,weights,a):
    ell=len(weights); d=n*(ell+1); L=np.zeros((d,d),float)
    def edge(i,j,c): L[i,i]+=c;L[j,j]+=c;L[i,j]-=c;L[j,i]-=c
    for x in range(n):
        edge(x*(ell+1),(x+1)%n*(ell+1),a)
        for t,w in enumerate(weights): edge(x*(ell+1)+t,x*(ell+1)+t+1,w)
    return L

def jac(weights,a,mu):
    ell=len(weights); J=np.zeros((ell+1,ell+1),float)
    J[0,0]+=a*mu
    for t,w in enumerate(weights):
        J[t,t]+=w;J[t+1,t+1]+=w;J[t,t+1]-=w;J[t+1,t]-=w
    return J

def formula(n,ell,S):
    g=n
    for s in S[1:]: g=math.gcd(g,2*(s-S[0]))
    return (ell+1)*(n-(g-1)//2)

def numerical_pbhrank(L,n,ell,S):
    vals,vec=np.linalg.eigh(L)
    B=vec[[s*(ell+1)+ell for s in S],:]
    d=len(vals); rank=0; groups=[]; st=0
    for z in range(1,d+1):
        if z==d or vals[z]-vals[st]>1e-7:
            A=B[:,st:z]; rr=np.linalg.matrix_rank(A,tol=1e-7)
            rank+=rr;groups.append((z-st,rr))
            st=z
    return rank,groups

def one(n,ell,a,weights,S):
    L=lap(n,weights,a)
    # Check block spectrum matches full network and ordered fiber bands don't overlap.
    allv=[];bands=[[] for i in range(ell+1)]
    for k in range(n):
        mu=2-2*math.cos(2*math.pi*k/n)
        ev=np.linalg.eigvalsh(jac(weights,a,mu))
        allv.extend(ev)
        for j,v in enumerate(ev):bands[j].append(v)
    assert np.allclose(sorted(allv),np.linalg.eigvalsh(L),atol=2e-9)
    for j in range(ell):assert max(bands[j]) < min(bands[j+1])-1e-8
    rank, groups=numerical_pbhrank(L,n,ell,S)
    expected=formula(n,ell,S)
    assert rank==expected,(n,ell,S,weights,rank,expected,groups)
    return 1

def checks():
    rng=random.Random(4102026)
    runs=0
    for n in range(3,12):
        for ell in range(1,5):
            for weights,a in [([1.0]*ell,1.0),([1.0+i/2 for i in range(ell)],2.0),([rng.choice([0.8,1.3,2.7,4.0]) for _ in range(ell)],1.7)]:
                for d in range(1,n):
                    runs+=one(n,ell,a,weights,[0,d])
                for S in [[0],[0,1,2],[0,2,4],[0,1,n-1]]:
                    S=sorted(set(x%n for x in S))
                    runs+=one(n,ell,a,weights,S)
    # Exact characteristic polynomial for small cases: full Laplacian and fibers.
    from sympy import symbols, prod, eye, cos, pi, simplify
    x=symbols('x')
    # Numeric exact root-of-unity decomposition for n=3,4,6 with integer coefficients.
    for n in [3,4,6]:
      for ww in [[1],[2,3]]:
        ell=len(ww);a=2; N=n*(ell+1)
        MM=Matrix(np.rint(lap(n,ww,a)).astype(int).tolist())
        full=MM.charpoly(x).as_expr().expand()
        blks=[]
        for k in range(n):
          mu=2-2*cos(2*pi*k/n)
          J=Matrix(jac(ww,a,float(mu)).round().astype(int).tolist())
          # exact parameters here mu integral for n=3,4,6
          blks.append(J.charpoly(x).as_expr())
        assert simplify(full-prod(blks).expand())==0,(n,ww)
        runs+=1
    # Exact rational Kalman ranks from explicit integer matrices; no eigenvalue grouping.
    exact=0
    from sympy import zeros
    for n in range(3,8):
      for ell in (1,2):
        A=Matrix(np.rint(lap(n,list(range(1,ell+1)),2)).astype(int).tolist())
        dim=A.rows
        for S in [[0],[0,1],[0,2],[0,n-1]]:
          S=sorted(set(x%n for x in S))
          B=zeros(dim,len(S))
          for j,p in enumerate(S):B[p*(ell+1)+ell,j]=1
          cols=[];T=B
          for _ in range(dim):
            cols.append(T);T=A*T
          C=Matrix.hstack(*cols)
          assert C.rank()==formula(n,ell,S),(n,ell,S,C.rank())
          exact+=1
    print('PASS',runs+exact,'spectral, PBH and exact rational Kalman checks; ',
          '6 exact characteristic identities and',exact,'exact Kalman ranks')
if __name__=='__main__':checks()
