"""Exact spectrum and feasible-design checks for star-Cartesian-product mixing."""
from fractions import Fraction
from itertools import product
from math import sqrt
import numpy as np
import sympy as sp


def graph_matrix(m, a, b, c):
    """Build symmetric stochastic matrix on K_(1,m) Cartesian K_2.

    Vertices: hubs 0, 1; leaves 2+i (attached to hub 0) and 2+m+i
    (attached to hub 1).  All adjacency is specified directly.
    """
    n = 2*m+2
    P = sp.zeros(n)
    for i in range(m):
        x, y = 2+i, 2+m+i
        for u,v,w in ((0,x,b),(1,y,b),(x,y,c)):
            P[u,v] = P[v,u] = w
    P[0,1] = P[1,0] = a
    for i in range(n):
        P[i,i] = 1-sum(P[i,j] for j in range(n) if j!=i)
    return P


def predicted_eigs(m,a,b,c):
    # Eigenvalues from normalized layer/reflection and page-permutation modes.
    hub = 1-2*a-m*b
    leaf = 1-b-2*c
    disc = sp.sqrt((hub-leaf)**2+4*m*b*b)
    return [sp.Integer(1),1-(m+1)*b] + [1-b]*(m-1) + [leaf]*(m-1) + [(hub+leaf+disc)/2,(hub+leaf-disc)/2]


def same_spectrum(P, theory):
    t1 = P.charpoly().as_expr()
    z=next(iter(P.charpoly().gens))
    t2=sp.prod(z-v for v in theory)
    return sp.simplify(t1-t2)==0


def check():
    tests=0
    for m in range(2,10):
        vals=[(sp.Rational(0),sp.Rational(1,3*m),sp.Rational(1,5)),
              (sp.Rational(1,7),sp.Rational(1,4*m),sp.Rational(1,5)),
              (sp.Rational(0),sp.Rational(1,m),sp.Rational(m-1,2*m))]
        if m==2:
            b=sp.sqrt(2)-1
            vals.append(((1-2*b)/2,b,(1-b)/2))
        for a,b,c in vals:
            assert a>=0 and b>=0 and c>=0 and (a+m*b)<=1 and b+c<=1
            P=graph_matrix(m,a,b,c)
            assert P==P.T and P*sp.ones(P.rows,1)==sp.ones(P.rows,1)
            assert same_spectrum(P,predicted_eigs(m,a,b,c))
            tests+=1
    for m in range(3,13):
        t=sp.Rational(m-1,m)
        P=graph_matrix(m,0,sp.Rational(1,m),sp.Rational(m-1,2*m))
        spc=predicted_eigs(m,0,sp.Rational(1,m),sp.Rational(m-1,2*m))
        assert all(abs(float(s)) <= float(t)+1e-12 for s in spc[1:]); tests+=1
        lo=sp.Rational(1,2*(m-1))
        hi=t-lo
        for cc in (lo,hi):
            eigs=predicted_eigs(m,0,sp.Rational(1,m),cc)
            assert all(abs(float(s)) <= float(t)+1e-12 for s in eigs[1:])
            tests+=1
        eps=sp.Rational(1,1000*m)
        for cc in (lo-eps,hi+eps):
            assert 0 <= cc <= t
            eigs=predicted_eigs(m,0,sp.Rational(1,m),cc)
            assert max(abs(float(s)) for s in eigs[1:]) > float(t)+1e-8
            tests+=1
    b=sp.sqrt(2)-1
    a=(1-2*b)/2
    c=(1-b)/2
    P=graph_matrix(2,a,b,c)
    assert same_spectrum(P,predicted_eigs(2,a,b,c))
    assert abs(float(max(abs(v.evalf()) for v in predicted_eigs(2,a,b,c)[1:]))) - (2-sqrt(2))<1e-13
    tests+=1
    # Numerical checks over a rational feasible grid (invariant weights).
    for m in range(2,13):
        bound=2-sqrt(2) if m==2 else 1-1/m
        for bi,ai,ci in product(range(7),repeat=3):
            bb=bi/(6*m)
            aa=ai*(1-m*bb)/6
            cc=ci*(1-bb)/6
            P=np.array(graph_matrix(m,aa,bb,cc),dtype=float)
            eigen=np.linalg.eigvalsh(P)
            mu=np.max(np.abs(eigen[:-1]))
            assert mu>=bound-1e-10,(m,bb,aa,cc,mu,bound)
            tests+=1
    print('PASS',tests,'exact and numerical checks')
if __name__=='__main__':
    check()
