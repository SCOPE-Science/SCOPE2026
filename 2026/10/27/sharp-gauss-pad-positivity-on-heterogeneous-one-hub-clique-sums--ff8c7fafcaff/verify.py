#!/usr/bin/env python3
"""Exact identities and independent matrix checks for Gauss diffusion on one-hub clique sums.

Requires SymPy >= 1.12. Run: python verify.py
"""
from itertools import product
from sympy import (Matrix, eye, diag, symbols, factor, cancel, together, Rational,
                   Poly, S, zeros, simplify, sign)

h, n, k = symbols('h n k', positive=True)

def d(z): return z*z + 6*z + 12

def r(z): return (z*z - 6*z + 12)/d(z)

def P(n, k, h):
    return ((k+1)*(k*n+k-n*n+n+1)*h**4 + 6*(k+1)*(k+2)*h**3
            + 12*(2*k+n*n+n+3)*h**2 + 72*(n+1)*h + 144)

def cross(n, h):
    return 12*h*h*((n+1)*h+6)/(d(h)*d(n*h))

def same(n, k, h):
    return 12*h*P(n,k,h)/(d(h)*d(n*h)*d((k+1)*h))

# Algebraic identities are checked with an expression constructed in a separate way.
assert cancel((1-r(n*h))/n - 12*h/d(n*h)) == 0
assert cancel(((n-1)+r(n*h)-n*r(h))/(n*(n-1)) - cross(n,h)) == 0
assert cancel(((n-1)+r(n*h)-n*r(h))/(n*(n-1))
              +(r(h)-r((k+1)*h))/k - same(n,k,h)) == 0
assert simplify((k*n+k-n*n+n+1).subs(n,k+2+h)
                + 1+h*(k+3)+h*h) == 0


def graph(sizes):
    """Direct graph construction, no use of the projector formulas."""
    N=1+sum(sizes)
    A=zeros(N)
    idx=1
    for sz in sizes:
        vertices=list(range(idx,idx+sz))
        for v in vertices:
            A[0,v]=A[v,0]=1
        for u in vertices:
            for v in vertices:
                if u!=v: A[u,v]=1
        idx+=sz
    L=diag(*[sum(A[i,j] for j in range(N)) for i in range(N)])-A
    return L


def by_orbit(sizes, step):
    N=1+sum(sizes)
    M=zeros(N)
    idx=1
    petals=[]
    for z in sizes:
        petals.append(list(range(idx,idx+z)))
        idx+=z
    for i in range(N):
        for j in range(N):
            if i==j: continue
            if i==0 or j==0:
                M[i,j]=12*step/d(N*step)
                continue
            pi=next(a for a,p in enumerate(petals) if i in p)
            pj=next(a for a,p in enumerate(petals) if j in p)
            M[i,j]=cross(N,step) if pi!=pj else same(N,sizes[pi],step)
    return M


def direct(sizes,step):
    L=graph(sizes)
    I=eye(L.rows)
    numer=12*I - 6*step*L + step**2*(L*L)
    denom=12*I + 6*step*L + step**2*(L*L)
    return denom.inv()*numer

samples=[(1,1),(1,1,1),(2,1),(2,2),(3,1),(3,2),(4,1),
         (2,3),(1,1,2),(2,1,2),(1,3,1),(3,3),(2,2,2),
         (4,2),(2,4),(5,1),(2,1,3),(4,1,1),(3,2,1),
         (1,1,1,1,1),(3,3,1),(2,2,1,2),(4,3)]
steps=[Rational(1,7), Rational(1,2), S.One, S(3), S(12), S(29)]
entry_count=0
for sizes in samples:
    N=1+sum(sizes)
    for step in steps:
        D=direct(sizes,step)
        E=by_orbit(sizes,step)
        assert D == D.T
        assert all(sum(D[i,j] for j in range(N))==1 for i in range(N))
        for i in range(N):
            for j in range(i+1,N):
                assert cancel(D[i,j]-E[i,j])==0,(sizes,step,i,j,D[i,j],E[i,j])
                entry_count+=1
        assert all(D[i,i]>0 for i in range(N))
# Exact witness: one added leaf-leaf edge destroys unconditional positivity.
star=direct((1,1,1),S(29))
paw=direct((2,1),S(29))
assert min(star)>0
assert paw[1,2] < 0
assert direct((2,1),S(28))[1,2] > 0
# A mixed-size example: the middle petal is the first to turn negative.
N=16
assert P(N,4,Rational(2261,1000))>0 and P(N,4,Rational(2262,1000))<0
assert P(N,5,Rational(2221,1000))>0 and P(N,5,Rational(2222,1000))<0
assert P(N,6,Rational(2230,1000))>0 and P(N,6,Rational(2231,1000))<0
print('VERIFY_OK: 3 symbolic orbit identities, 1 symbolic leading-coefficient identity,',
      len(samples),'independent direct Laplacian graphs,',len(steps),'exact timesteps each,',
      entry_count,'off-diagonal equalities, row-stochasticity, positive diagonals,',
      'paw reversal and nonmonotone blade-size thresholds')
