#!/usr/bin/env python3
"""Exact-arithmetic checks for resistance curvature on iterated polygon pyramids.

Python 3, sympy. Run `python verify.py`. This supplements, but does not
replace, the analytical all-parameter proof in RESULT.md.
"""
import sympy as sp

x=sp.symbols('x')

def cyclic_eigenvalue_product(n):
    # det(x I + L(C_n))/x; polynomial with integer coefficients.
    p=sp.Poly(sp.cancel(2*(sp.chebyshevt(n, (x+2)/2)-1)/x), x)
    assert p.degree()==n-1
    return p

def hub_curvature_via_product(n,r):
    p=cyclic_eigenvalue_product(n)
    H=sp.Rational(p.diff().eval(r),p.eval(r))
    return (sp.Rational(n+1,n+r)-H)/2

def reduced_inverse_resistance_curvatures(n,r):
    N=n+r
    L=sp.zeros(N)
    def edge(i,j):
        L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    for i in range(r):
        for j in range(i+1,r):edge(i,j)
    for i in range(r):
        for j in range(r,N):edge(i,j)
    for j in range(n):edge(r+j,r+(j+1)%n)
    G=L[0:N-1,0:N-1].inv()
    def res(i,j):
        if i==N-1:return G[j,j]
        if j==N-1:return G[i,i]
        return G[i,i]+G[j,j]-2*G[i,j]
    vals=[]
    for i in range(N):
        vals.append(1-sp.Rational(1,2)*sum(res(i,j) for j in range(N) if L[i,j]==-1))
    return vals

checked=0
for n in range(3,12):
    for r in range(1,12):
        c=hub_curvature_via_product(n,r)
        direct=reduced_inverse_resistance_curvatures(n,r)
        assert all(v==c for v in direct[:r]),(n,r,'hub')
        assert all(v==(1-r*c)/n for v in direct[r:]),(n,r,'rim')
        cutoff=sp.Rational(n*(n-3)-2,2)
        assert (c>0)==(r>=cutoff),(n,r,c,cutoff)
        assert all(v>0 for v in direct[r:]),(n,r,'rim not positive')
        checked+=1

threshold_checks=0
for n in range(3,45):
    cutoff=max(1, (n*(n-3)-2)//2)
    for r in sorted({1,2,3,4,5,max(1,cutoff-2),max(1,cutoff-1),cutoff,cutoff+1,cutoff+2,3*cutoff+1}):
        c=hub_curvature_via_product(n,r)
        assert (c>0)==(r>=cutoff),(n,r,c,cutoff)
        assert c!=0
        threshold_checks+=1

print(f'EXACT_OK independent_laplacian_cases={checked} spectral_threshold_cases={threshold_checks}')
