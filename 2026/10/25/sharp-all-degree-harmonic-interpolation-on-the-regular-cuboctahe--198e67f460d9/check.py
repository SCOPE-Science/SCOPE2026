"""Exact and independent numerical checks of cuboctahedral harmonic sampling.

Uses Python 3, SymPy and NumPy. It performs all finite comparisons
invoked by the theorem; the infinite tail is handled analytically.
"""
from fractions import Fraction
from itertools import combinations, product
from math import pi, sqrt
import numpy as np
import sympy as sp


def rational_legendre(n, x):
    p, q = Fraction(1), x
    if n == 0:
        return p
    for j in range(1, n):
        p, q = q, ((2*j+1)*x*q-j*p)/(j+1)
    return q


def predicted(n):
    a, b = rational_legendre(n, Fraction(1,2)), rational_legendre(n, Fraction(0))
    if n % 2:
        return [(2*(1+2*a), 3), (2*(1-2*a), 3)]
    return [(2*(1+4*a+b), 1), (2*(1-b), 3), (2*(1-2*a+b), 2)]


def vertices():
    out = []
    for i, j in combinations(range(3), 2):
        for a, b in product((-1,1),repeat=2):
            v=[0,0,0]
            v[i]=a;v[j]=b
            out.append(tuple(v))
    return out


V = vertices()
assert len(V)==12 and len(set(V))==12
mins=[]
for l in range(20):
    ps=predicted(l)
    assert sum(m for _,m in ps)==6
    assert sum(x*m for x,m in ps)==12
    assert all(x>=0 for x,_ in ps)
    positives=[x for x,_ in ps if x>0]
    mins.append(min(positives))
assert min(mins)==Fraction(65,32768)
assert [l for l,mm in enumerate(mins) if mm==min(mins)]==[10]
assert [sum(m for x,m in predicted(l) if x>0) for l in range(20)]==[1,3,5]+[6]*17
assert predicted(10)[0]==(Fraction(65,32768),1)
print('EXACT finite degrees 0..19: all nonzero eigenvalue branches positive')
print('EXACT ranks 0,1,2 and 3..19: 1,3,5 and 6')
print('EXACT minimum among degrees 0..19: 65/32768 at degree 10, multiplicity 1')
print('EXACT lower bound for degrees >=20 follows analytically: 1/30 > 65/32768')

# An independent 12-by-12 Gram construction, not the quotient formula.
max_diff=0.0
for l in range(61):
    G=np.empty((12,12),dtype=float)
    for i,x in enumerate(V):
        for j,y in enumerate(V):
            d=sum(a*b for a,b in zip(x,y)) / 2
            G[i,j]=float(sp.legendre(l, sp.Rational(int(2*d),2)))
    direct=sorted(np.linalg.eigvalsh(G))
    expected=[0.0]*6
    for value,mult in predicted(l):
        expected.extend([float(value)]*mult)
    expected.sort()
    max_diff=max(max_diff,max(abs(a-b) for a,b in zip(direct,expected)))
assert max_diff<1e-11
print(f'INDEPENDENT matrices degrees 0..60: 61 full 12x12 spectra, max error {max_diff:.3e}')

# Check exact signed-edge and perfect-matching reductions.
R=[]
for i,j in combinations(range(3),2):
    for sign in (1,-1):
        v=[0,0,0];v[i]=1;v[j]=sign
        R.append(tuple(v))
H=sp.Matrix([[sp.Rational(sum(a*b for a,b in zip(x,y)),2) for y in R] for x in R])
S=2*(H-sp.eye(6))
assert S.eigenvals()=={sp.Integer(-2):3,sp.Integer(2):3}
assert H.eigenvals()=={sp.Integer(0):3,sp.Integer(2):3}
print('EXACT signed-root operator eigenvalues: +2 and -2, each multiplicity 3')
print('ALL CHECKS PASSED')
