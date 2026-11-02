#!/usr/bin/env python3
"""Exact checks supporting the characteristic-two binary Nash cubic.

Requires Python 3 and SymPy.  Finite-field experiments do not replace
proofs of irreducibility, component exhaustiveness, or the degree formula.
"""
import itertools
from collections import Counter
import sympy as s

av=s.symbols('a0:4'); bv=s.symbols('b0:4'); cv=s.symbols('c0:4')
a=s.Matrix(2,2,av); b=s.Matrix(2,2,bv); c=s.Matrix(2,2,cv)
j=s.Matrix([[0,1],[1,0]])
z=s.symbols('z')
a0,a1=av[0]+av[1]*z,av[2]+av[3]*z
b0,b1=bv[0]+bv[1]*z,bv[2]+bv[3]*z
p=s.expand(cv[0]*a1*b1-cv[1]*a0*b1-cv[2]*b0*a1+cv[3]*a0*b0)
q=s.expand(p).coeff(z,1)
trace=s.expand(s.trace(a*j*b.T*j*c*j))
vars=(*av,*bv,*cv)
assert s.Poly(q-trace,*vars,modulus=2).is_zero
assert s.expand(p).coeff(z,3)==0
assert s.Poly(s.expand((s.expand(p).coeff(z,1)**2-4*s.expand(p).coeff(z,0)*s.expand(p).coeff(z,2))-q**2),*vars,modulus=2).is_zero

h=s.symbols('h1:4')
edge=(h[0]+h[1],h[1]+h[2],h[2]+h[0])
degree=sum(s.prod(edge[i]**e[i] for i in range(3)) for e in itertools.product(range(4),repeat=3) if sum(e)==3)
assert s.expand(degree).coeff(h[0]).coeff(h[1]).coeff(h[2])==14

def matmul(a,b):
    return tuple((a[2*i]*b[j]+a[2*i+1]*b[2+j])%2 for i in range(2) for j in range(2))
def rank(a):
    return 2 if (a[0]*a[3]+a[1]*a[2])%2 else (1 if any(a) else 0)
def to_mats(v):
    aa,bb,cc=v[:4],v[4:8],v[8:]
    return ((aa[1],aa[0],aa[3],aa[2]),
            (bb[2],bb[0],bb[3],bb[1]),
            (cc[1],cc[0],cc[3],cc[2]))

def cubic(mats):
    return (lambda d:(d[0]+d[3])%2)(matmul(matmul(mats[0],mats[1]),mats[2]))

counts=Counter()
for bits in range(1,4096):
    v=tuple((bits>>i)&1 for i in range(12))
    mats=to_mats(v)
    value=cubic(mats)
    # For a multilinear cubic, the finite difference in each F2 coordinate
    # equals the corresponding formal partial derivative.
    derivative=tuple((value+cubic(to_mats(tuple((v[j]^(i==j)) for j in range(12)))))%2 for i in range(12))
    prods=(matmul(mats[0],mats[1]),matmul(mats[1],mats[2]),matmul(mats[2],mats[0]))
    singular=all(x==0 for prod in prods for x in prod)
    assert singular==(not any(derivative))
    if singular:
        assert value==0
        rr=tuple(rank(m) for m in mats)
        assert (max(rr)<=1 or rr in ((2,0,0),(0,2,0),(0,0,2)))
        counts[rr]+=1
assert counts[(1,1,1)]==27
assert counts[(2,0,0)]==counts[(0,2,0)]==counts[(0,0,2)]==6
print('VERIFY_OK: cubic trace identity and specialization over F2; degree 14; exhaustive F2 rank patterns')
