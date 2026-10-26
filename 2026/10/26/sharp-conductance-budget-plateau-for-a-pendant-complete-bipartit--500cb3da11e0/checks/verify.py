#!/usr/bin/env python3
"""Check finite exact identities and samples for the pendant biclique eigenvalue theorem.
Science-only reproducibility. Requires SymPy and NumPy. Infinite assertions rely on the written proof.
"""
import sympy as sp
import numpy as np


def matrices(p, q, budget=sp.Integer(1)):
    """Return the proposed Laplacian and the dual Gram matrix, with exact entries."""
    assert p >= 4 and q >= 2
    m = p - 1
    n = p + q + 1
    scale = budget / (p + 4)
    L = sp.zeros(n)
    def add(i, j, conductance):
        L[i, i] += conductance
        L[j, j] += conductance
        L[i, j] -= conductance
        L[j, i] -= conductance
    leaf = n - 1
    add(leaf, 0, 2 * scale)
    for j in range(p, p + q):
        add(0, j, 3 * scale / q)
        for i in range(1, p):
            add(i, j, scale / q)
    v = sp.Matrix([1] + [-sp.Rational(3, m)] * m + [0] * q + [2])
    X = v * v.T
    s2 = sp.Rational(m*m - 9, m*(m-1))
    for i in range(1, p):
        for j in range(1, p):
            X[i, j] += s2 * ((1 if i == j else 0) - sp.Rational(1,m))
    return L, X


def independent_direct_L(p, q, budget=1):
    n=p+q+1
    scale=float(budget)/(p+4)
    L=np.zeros((n,n), dtype=float)
    weights=[]
    weights.append((0,n-1,2*scale))
    for b in range(p,p+q):
        weights.append((0,b,3*scale/q))
        for a in range(1,p):
            weights.append((a,b,scale/q))
    for i,j,w in weights:
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    return L


def main():
    m,q=sp.symbols('m q', integer=True, positive=True)
    t=sp.Symbol('t')
    Q=sp.Matrix([[2,-2,0,0],[-2,5,0,-3],[0,0,1,-1],
                 [0,-3/q,-m/q,(m+3)/q]])
    expected=t*(t-1)*(q*t*t-(7*q+m+3)*t+6*q+6*m+12)/q
    assert sp.simplify(Q.charpoly(t).as_expr()-expected)==0
    assert sp.expand((q*t*t-(7*q+m+3)*t+6*q+6*m+12).subs(t,1)) == 5*m+9
    # A symbolic nonnegative PSD coefficient makes the Gram construction valid for m>=3.
    s2=(m*m-9)/(m*(m-1))
    assert sp.simplify(sp.Rational(9,1)/m**2 + s2*(1-1/m)-1)==0
    assert sp.simplify(5+sp.Rational(9,1)/m+s2*(m-1)-(m+5))==0
    exact_checks=0
    for p in range(4,10):
        for q in range(2,min(p+6,12)):
            L,X=matrices(p,q)
            N=L.rows
            assert all(v==0 for v in (L*sp.ones(N,1)))
            assert all(v==0 for v in (X*sp.ones(N,1)))
            assert sp.trace(X)==p+4
            edge_pairs=[(0,N-1)] + [(a,b) for a in range(p) for b in range(p,p+q)]
            assert all(X[i,i]+X[j,j]-2*X[i,j]==1 for i,j in edge_pairs)
            assert sp.trace(L*X)==1
            assert all(sp.simplify(v)==0 for v in (L-sp.eye(N)/(p+4))*sp.Matrix([1]+[-sp.Rational(3,p-1)]*(p-1)+[0]*q+[2]))
            exact_checks+=1
    num_checks=0
    minmargin=1e9
    for p in range(4,31):
        for q in (2,3,4,p,p+2,p+3,p+5):
            if q<2: continue
            A=independent_direct_L(p,q)
            ev=np.linalg.eigvalsh(A)
            predicted=min(1,(p+2)/q)/(p+4)
            err=abs(ev[1]-predicted)
            assert err<2e-10,(p,q,ev[1],predicted)
            minmargin=min(minmargin,err)
            num_checks+=1
    # Sharpness of p>=4: p=3,q=2 with a rational graph having gap 6/41 >1/7.
    p,q=3,2
    x,y,z=sp.Rational(8,41),sp.Rational(7,82),sp.Rational(11,41)
    T=sp.zeros(6)
    def edge(i,j,w):
        T[i,i]+=w;T[j,j]+=w;T[i,j]-=w;T[j,i]-=w
    edge(0,5,z)
    for j in (3,4):
        edge(0,j,x)
        for i in (1,2):edge(i,j,y)
    spectrum=T.eigenvals()
    assert sum(spectrum.values())==6
    assert sp.Rational(6,41) in spectrum
    assert all((lambda x: float(x)>0)(vv) for vv in spectrum if vv!=0)
    assert sorted((float(vv) for vv in spectrum))[1]==float(sp.Rational(6,41))
    assert sp.Rational(6,41)>sp.Rational(1,7)
    print('PASS charpoly identity; dual Gram symbolic identities')
    print('PASS exact matrix Gram/eigenvector identities:',exact_checks,'instances')
    print('PASS independent numerical Laplacian spectra:',num_checks,'instances')
    print('PASS p=3,q=2 sharpness rational counterexample')

if __name__=='__main__':main()
