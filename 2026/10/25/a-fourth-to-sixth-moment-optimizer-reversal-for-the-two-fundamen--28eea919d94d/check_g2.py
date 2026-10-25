#!/usr/bin/env python3
"""Exact Laurent-coefficient verification for two fundamental G2 character moments."""
from collections import defaultdict
from math import comb
from fractions import Fraction
from itertools import product
import cmath
import sympy as sp

SHORT = [(1, 0), (0, 1), (-1, 1)]
LONG = [(1, 1), (2, -1), (1, -2)]

def add(A, B):
    C = defaultdict(int, A)
    for k, v in B.items():
        C[k] += v
    return {k: v for k, v in C.items() if v}

def multiply(A, B):
    C = defaultdict(int)
    for (a, b), v in A.items():
        for (c, d), w in B.items():
            C[(a+c, b+d)] += v*w
    return {k: v for k, v in C.items() if v}

def powers(A, n):
    out = [{(0,0):1}]
    for _ in range(n):
        out.append(multiply(out[-1], A))
    return out

def character(constant, pairs):
    D = {(0,0):constant}
    for a,b in pairs:
        D = add(D, {(a,b):1,(-a,-b):1})
    return D

def weyl_density():
    D = {(0,0):1}
    for a,b in SHORT+LONG:
        D = multiply(D, {(0,0):2,(a,b):-1,(-a,-b):-1})
    return D

U = character(1, SHORT)
V = character(2, SHORT+LONG)
W = weyl_density()
assert W[(0,0)] == 12

def moment(M):
    numerator = sum(v*W.get((-a,-b), 0) for (a,b),v in M.items())
    assert numerator % 12 == 0
    return numerator // 12

T = sp.Symbol('t')
TABLES = {
    2: [1,0,1],
    4: [4,2,3,1,5],
    6: [35,30,33,32,45,40,80],
}
POLYS = {
    4: 4 + 8*T + 18*T**2 + 4*T**3 + 5*T**4,
    6: 35+180*T+495*T**2+640*T**3+675*T**4+240*T**5+80*T**6,
}
QS = {
    4: T**4+4*T**3+3*T**2-5*T-2,
    6: 8*T**6+29*T**5+24*T**4-24*T**3-34*T**2-26*T-6,
}
DERIVATIVE_MULTIPLIERS = {4:-4, 6:-30}

for n in (2,4,6):
    up, vp = powers(U,n), powers(V,n)
    calculated = [moment(multiply(up[n-j],vp[j])) for j in range(n+1)]
    assert calculated == TABLES[n], (n, calculated)
    print(f'moments[{n}]={calculated}')
    if n>2:
        polynomial = sum(comb(n,j)*calculated[j]*T**j for j in range(n+1))
        assert sp.expand(polynomial - POLYS[n]) == 0
        D = sp.expand(sp.diff(polynomial,T)*(1+T*T) - n*T*polynomial)
        assert sp.expand(D - DERIVATIVE_MULTIPLIERS[n]*QS[n]) == 0

# A single change from negative to positive in coefficients ordered low-to-high
# establishes a unique positive root by Descartes' rule and the endpoint signs.
for n in (4,6):
    q = sp.Poly(QS[n],T)
    coeffs = [int(q.nth(j)) for j in range(q.degree()+1)]
    signs = [1 if c>0 else -1 for c in coeffs]
    assert signs.count(1)>0 and signs.count(-1)>0
    assert sum(signs[i]!=signs[i-1] for i in range(1,len(signs))) == 1
    assert q.eval(0) < 0 and q.LC()>0
    assert (q.eval(1)>0 if n==4 else q.eval(1)<0)

bounds={4:(Fraction('0.93628195'), Fraction('0.93628197')),
        6:(Fraction('1.14507475'), Fraction('1.14507478'))}
for n,(lo,hi) in bounds.items():
    assert QS[n].subs(T,sp.Rational(lo.numerator,lo.denominator))<0
    assert QS[n].subs(T,sp.Rational(hi.numerator,hi.denominator))>0
    # No second positive root exists by the coefficient sign count above.
    rr=sp.nroots(QS[n],maxsteps=200)
    roots=[float(sp.re(z)) for z in rr if abs(float(sp.im(z)))<1.e-10 and float(sp.re(z))>0]
    assert len(roots)==1
    r=roots[0]
    k=float(POLYS[n].subs(T,r)/(1+r*r)**(n//2))
    print(f'K[{n}]={k:.14f}; ratio b/a={r:.14f}; weight on 7={1/(1+r*r):.14f}')

# Separate finite torus quadrature check: the weighted integrands are Laurent
# polynomials with coordinate exponents in [-18,18]; any uniform grid of order
# at least 37 integrates them exactly before floating rounding.
import numpy as np
N=48
ang=2*np.pi*np.arange(N)/N
z=np.exp(1j*ang)[:,None]; w=np.exp(1j*ang)[None,:]
def zpower(pair):
    a,b=pair
    return z**a*w**b
u=np.ones((N,N),dtype=complex)
v=2*np.ones((N,N),dtype=complex)
for a,b in SHORT:
    contribution=zpower((a,b))+zpower((-a,-b))
    u+=contribution;v+=contribution
for a,b in LONG:v+=zpower((a,b))+zpower((-a,-b))
weight=np.ones((N,N),dtype=complex)
for a,b in SHORT+LONG:
    root=zpower((a,b))
    weight*=2-root-1/root
for n in (2,4,6):
    for j in range(n+1):
        answer=np.mean((u**(n-j))*(v**j)*weight)/12
        assert abs(answer-TABLES[n][j])<1.e-7,(n,j,answer)
print('PASS: exact Weyl coefficient moments, derivative polynomials, root isolation, finite exact-grid quadrature')
