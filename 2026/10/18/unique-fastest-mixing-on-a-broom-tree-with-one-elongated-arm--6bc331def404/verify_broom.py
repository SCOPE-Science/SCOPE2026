"""Reproduce algebraic identities and finite spectral checks for broom-chain optimum.
Requires Python 3, sympy, numpy; no external data or network calls.
"""
from fractions import Fraction
import sympy as sp
import numpy as np

n, z = sp.symbols('n z', positive=True, integer=True)
# Independent unassumed polynomial variable avoids accidental symbol mismatch.
t = sp.Symbol('t')
D = n*n+n-1
a = n*(n-1)/D
b = (2*n-1)/D
c = (n-1)/D
mu = n*n/D
Q = sp.Matrix([
    [1-a,a,0,0],
    [a,1-a-b,b,0],
    [0,b,1-b-n*c,n*c],
    [0,0,c,1-c],
])
q = t*t + (n*(n-1)/D)*t + (n**3-5*n*n+4*n-1)/D**2
assert sp.simplify(Q.charpoly(t).as_expr()-(t-1)*(t-mu)*q)==0
assert sp.simplify(q.subs(t,-mu)-(n-1)**2*(2*n-1)/D**2)==0
assert sp.simplify(q.subs(t,mu)-(n-1)*(2*n**3+2*n*n-3*n+1)/D**2)==0
N = n**4+n*n*(n-1)**2+n*(2*n-1)**2
E = n*n*a+n*n*(n-1)**2*b+n*(2*n-1)**2*c
assert sp.simplify(E-mu*0-N*c)==0
assert sp.simplify((1-a-b))==0
assert sp.simplify((1-b-n*c))==0
# The common Fiedler eigenvector in four orbit coordinates.
x = sp.Matrix([n*n,n*(n-1),0,-(2*n-1)])
assert all(sp.simplify(y)==0 for y in (Q-mu*sp.eye(4))*x)
assert sp.simplify(x[0]+x[1]+x[2]+n*x[3])==0
# Prove n^3(n-2)>(2n-1)^2 for every integer n>=3 by
# a base case and a polynomial forward difference with positive coefficients.
k = sp.Symbol('k', integer=True, nonnegative=True)
f = n**3*(n-2)-(2*n-1)**2
poly = sp.Poly(sp.expand(f.subs(n,k+3)),k)
assert all(v>0 for v in poly.all_coeffs()),poly

checks = 0
for nn in range(3,101):
    dd=nn*nn+nn-1
    aa=nn*(nn-1)/dd; bb=(2*nn-1)/dd; cc=(nn-1)/dd
    size=nn+3
    P=np.eye(size)
    for i,j,w in [(0,1,aa),(1,2,bb),*[(2,3+k,cc) for k in range(nn)]]:
        P[i,j]=w;P[j,i]=w;P[i,i]-=w;P[j,j]-=w
    vals=np.linalg.eigvalsh(P)
    assert abs(vals[-1]-1)<1e-11
    assert abs(vals[-2]-nn*nn/dd)<2e-11
    assert max(abs(vals[:-1]))<=nn*nn/dd+2e-11
    assert np.max(np.abs(P.sum(axis=1)-1))<1e-12
    assert P.min()>-1e-12
    assert np.allclose(P,P.T)
    checks+=1
# For the excluded n=2, give an exact PSD witness that the proposed
# n>=3 rational family is NOT optimal: weights 1/2,1/2,1/4 beat 4/5.
Pn=sp.eye(5)
for i,j,w in [(0,1,sp.Rational(1,2)),(1,2,sp.Rational(1,2)),(2,3,sp.Rational(1,4)),(2,4,sp.Rational(1,4))]:
    Pn[i,j]=Pn[j,i]=w
    Pn[i,i]-=w;Pn[j,j]-=w
centered=Pn-sp.ones(5)/5
for M in (sp.Rational(4,5)*sp.eye(5)-centered,sp.Rational(4,5)*sp.eye(5)+centered):
    assert all(M[:j,:j].det()>0 for j in range(1,6))
print('VERIFIED symbolic characteristic polynomial, Rayleigh identities, positivity inequality,')
print('         98 full-matrix spectral tests (n=3,...,100), and exact n=2 boundary witness.')
