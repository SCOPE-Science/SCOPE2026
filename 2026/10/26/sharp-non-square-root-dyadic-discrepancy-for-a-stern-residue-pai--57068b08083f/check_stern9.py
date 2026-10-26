#!/usr/bin/env python3
"""Exact certificate for dyadic Stern-pair discrepancy modulo nine.
Requires Python 3 and SymPy. All characteristic polynomials, coefficient
identities and complex-root disks are certified with exact arithmetic.
"""
from fractions import Fraction as F
from math import gcd, comb
import sympy as sp

x = sp.symbols('x')
modulus=9
states=[(a,b) for a in range(modulus) for b in range(modulus) if gcd(gcd(a,b),modulus)==1]
assert len(states)==72
idx={q:i for i,q in enumerate(states)}
M=sp.zeros(72)
for i,(a,b) in enumerate(states):
    M[i,idx[(a,(a+b)%9)]]+=1
    M[i,idx[((a+b)%9,b)]]+=1
# Permutation property, critical to the uniform Perron eigenvector.
assert all(sum(int(M[i,j]) for j in range(72))==2 for i in range(72))
assert all(sum(int(M[i,j]) for i in range(72))==2 for j in range(72))
P=sp.Poly(M.charpoly(x).as_expr(),x)
q=x**6+2*x**5+3*x**4+2*x**3+x**2+3
h=x**6-x**5+x**4-x**3+2*x**2-4*x+8
expected=x**14*(x-2)*(x-1)**17*(x+1)**6*(x*x-2*x+2)**2*(x*x+x+2)**3*q**2*h**2
assert P==sp.Poly(expected,x)
assert sp.Poly(q,x,modulus=17).is_irreducible

# Evaluate R(E)b at index 0 for the pair (1,2).
# R=P/q^2; E shifts the dyadic length k by one.
R=P.exquo(sp.Poly(q,x)**2)
coeff=[int(z) for z in R.all_coeffs()[::-1]]
row=[0]*72
row[idx[(0,1)]]=1
value=0
for coeff_i in coeff:
    value+=coeff_i*row[idx[(1,2)]]
    nex=[0]*72
    for i,(a,b) in enumerate(states):
        if row[i]:
            nex[idx[(a,(a+b)%9)]]+=row[i]
            nex[idx[((a+b)%9,b)]]+=row[i]
    row=nex
assert value==116619264, value

# Integer-rational Rouché disks around all roots of q and h.
# Each disk radius 0.001 contains exactly one zero; comparisons exact.
# Gaussian rational arithmetic as (real, imaginary) Fractions.
def mul(z,w):
    return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def add(z,w):return (z[0]+w[0],z[1]+w[1])
def ev(poly,center):
    t=(F(0),F(0))
    for a in reversed(poly):t=add(mul(t,center),(F(a),F(0)))
    return t
def normsq(z):return z[0]*z[0]+z[1]*z[1]
def certify(poly,centers):
    r=F(1,1000)
    # bound Taylor terms of order >=2 at |center|<3/2
    tail=sum(F(abs(a))*comb(k,j)*F(3,2)**(k-j)*r**j
             for k,a in enumerate(poly) for j in range(2,k+1))
    assert tail<F(1,1000)
    dp=[k*a for k,a in enumerate(poly)][1:]
    for A,B in centers:
        c=(F(A,100000),F(B,100000))
        assert normsq(c)<F(3,2)**2
        assert normsq(ev(poly,c))<F(1,1000)**2
        assert normsq(ev(dp,c))>F(10)**2
        # |poly(c)|+Taylor_tail < 0.002 < 0.010 < r |poly'(c)|
    for i,c in enumerate(centers):
        for d in centers[i+1:]:
            assert (F(c[0]-d[0],100000)**2+F(c[1]-d[1],100000)**2) > (2*r)**2
    # Rouché relative to the linear Taylor term proves one root per disk.

centers_q=[(-118967,-75338),(-118967,75338),(-38416,-138684),(-38416,138684),(57383,-63346),(57383,63346)]
centers_h=[(-104307,-95499),(-104307,95499),(28600,-138499),(28600,138499),(125707,-64790),(125707,64790)]
# Centers are integers / 100000; list e.g -118967/100000=-1.18967.
q_coeff=[int(sp.Poly(q,x).nth(k)) for k in range(7)]
h_coeff=[int(sp.Poly(h,x).nth(k)) for k in range(7)]
certify(q_coeff,centers_q)
certify(h_coeff,centers_h)

def sqmag(center):return F(center[0],100000)**2+F(center[1],100000)**2
for i,c in enumerate(centers_q):
    if i in (2,3):
        assert sqmag(c)>F(1439,1000)**2  # root modulus > 1.438
        assert sqmag(c)<F(1440,1000)**2  # root modulus < 1.441
    else:
        assert sqmag(c)<F(1415,1000)**2
for c in centers_h:
    assert sqmag(c)<F(1415,1000)**2 # root modulus < 1.416
# Other characteristic roots have moduli <=sqrt(2), 1, or 0.

# Independent direct evaluation of the first 12 dyadic pair frequencies.
def stern(n):
    if n==0:return 0
    if n==1:return 1
    if n%2==0:return stern(n//2)
    return stern(n//2)+stern(n//2+1)
row=[0]*72;row[idx[(0,1)]]=1
for k in range(12):
    counted=sum(1 for n in range(1<<k) if (stern(n)%9,stern(n+1)%9)==(1,2))
    assert counted==row[idx[(1,2)]],(k,counted,row[idx[(1,2)]])
    nxt=[0]*72
    for i,(a,b) in enumerate(states):
        if row[i]:
            nxt[idx[(a,(a+b)%9)]]+=row[i]
            nxt[idx[((a+b)%9,b)]]+=row[i]
    row=nxt
print('PASS: 72-state characteristic polynomial; q irreducible mod 17;')
print('      nonzero projected discrepancy 116619264;')
print('      exact 12-root Rouché disks and dyadic counts k=0..11.')
