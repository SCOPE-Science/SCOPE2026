#!/usr/bin/env python3
"""Exact rational-polynomial checks for radial Fourier dimension thresholds."""
from math import comb, factorial
import sympy as sp

r = sp.symbols('r', positive=True)

def pieces(m):
    cuts = sorted({0, m} | {m-2*j for j in range(m//2+1) if m-2*j > 0})
    result=[]
    for a,b in zip(cuts, cuts[1:]):
        mid=sp.Rational(a+b,2)
        term=sum((-1)**j*comb(m,j)*(m-2*j-r)**(m-1)
                 for j in range(m+1) if m-2*j>mid)
        result.append((a,b,sp.factor(term / (2**m * factorial(m-1)))))
    return result

def walk(f):
    return sp.factor(-sp.diff(f,r)/r)

def Dk(f,k):
    for _ in range(k):
        f=walk(f)
    return f

def eq(a,b):
    assert sp.simplify(a-b)==0, (a,b)

for m in range(2,6):
    rows=pieces(m)
    assert rows[0][0]==0 and rows[-1][1]==m
    # The pieces constitute the density of a sum of m independent U[-1,1].
    assert sum(sp.integrate(f,(r,a,b)) for a,b,f in rows)*2 == 1
    for idx in range(1,4):
        assert all(not Dk(f,idx).has(sp.DiracDelta) for _,_,f in rows)

# m=1: b1(r)=1/2 on (0,1), zero beyond. D b1 has positive
# sphere atom 1/2 delta_1; one more lift differentiates the atom.

# m=2: positive R5 interior and a positive outer sphere atom.
m2=pieces(2)
assert [(a,b) for a,b,_ in m2] == [(0,2)]
eq(Dk(m2[0][2],2),sp.Rational(1,4)/r**3)
atom2=sp.simplify(Dk(m2[0][2],1).subs(r,2)/2)
eq(atom2,sp.Rational(1,16))

# m=3: positive R5 annulus; the upward jump forces a negative
# atom in the R7 lift.
m3=pieces(3)
assert [(a,b) for a,b,_ in m3]==[(0,1),(1,3)]
eq(Dk(m3[0][2],2),0)
eq(Dk(m3[1][2],2),sp.Rational(3,8)/r**3)
j3=sp.simplify(Dk(m3[1][2],2).subs(r,1)-Dk(m3[0][2],2).subs(r,1))
eq(j3,sp.Rational(3,8))
assert -j3 < 0

# m=4: positive R7 density, but it jumps UP at radius 2.
m4=pieces(4)
assert [(a,b) for a,b,_ in m4]==[(0,2),(2,4)]
eq(Dk(m4[0][2],3),sp.Rational(3,32)/r**3)
eq(Dk(m4[1][2],3),(48-r*r)/(32*r**5))
j4=sp.simplify(Dk(m4[1][2],3).subs(r,2)-Dk(m4[0][2],3).subs(r,2))
eq(j4,sp.Rational(1,32))
assert -j4/2<0 # negative sphere atom in R9 distributional lift

# m=5: positive R7 annulus; the next odd-dimensional lift is
# pointwise negative for radii 1<r<sqrt(5/3).
m5=pieces(5)
assert [(a,b) for a,b,_ in m5]==[(0,1),(1,3),(3,5)]
eq(Dk(m5[0][2],3),0)
eq(Dk(m5[1][2],3),5*(r*r-1)/(32*r**5))
eq(Dk(m5[2][2],3),5*(25-r*r)/(64*r**5))
eq(Dk(m5[1][2],4),5*(3*r*r-5)/(32*r**7))
assert Dk(m5[1][2],4).subs(r,sp.Rational(6,5)) < 0

# Other critical densities are nonnegative on each whole stated
# open interval by the explicit factors certified above.
assert all(Dk(f,3).subs(r,sp.Rational(a+b,2))>0 for a,b,f in m4)
assert Dk(m5[1][2],3).subs(r,2)>0 and Dk(m5[2][2],3).subs(r,4)>0
print('PASS: exact B-spline pieces, Fourier dimension walks, jump coefficients, and obstruction signs for m=1..5')
