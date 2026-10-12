"""Exact algebraic and characteristic-zero combinatorial checks for the sextic quotient."""
from math import comb
import sympy as sp

x=sp.symbols('x0 x1 x2')
y=sp.symbols('y0 y1 y2')
f=lambda a: a[0]**6 + 2*a[0]**5*a[1]+3*a[1]**6+5*a[2]**6+7*a[0]**3*a[1]**3
F=f(x)-f(y)
I=sp.I
assert sp.expand(F.subs({**dict(zip(x,[I*t for t in y])),**dict(zip(y,[-I*t for t in x]))}, simultaneous=True)-F)==0
assert sp.expand(F.subs(dict(zip(y,[I*t for t in x])),simultaneous=True)-2*f(x))==0
assert sp.expand(F.subs(dict(zip(y,[-I*t for t in x])),simultaneous=True)-2*f(x))==0
# A smooth test curve suffices for symbolic sanity, but the theorem invokes smoothness as a hypothesis.
Fermat=sum(z**6 for z in x)-sum(z**6 for z in y)
assert sp.expand(Fermat.subs(dict(zip(y,[I*t for t in x])),simultaneous=True)-2*sum(z**6 for z in x))==0
# The invariant monomials are even total degree; the 2-Veronese Hilbert series.
t=sp.symbols('t')
H=(1+3*t)/(1-t)**3
for m in range(10):
    assert sp.series(H,t,0,m+1).coeff(t,m)==comb(2*m+2,2)
assert sp.limit((1-t)**3*H,t,1)==4
# Chern class and Lefschetz-Euler quotient calculation.
d=6
chiX=d*sum(comb(6,j)*(-d)**(4-j) for j in range(5))
assert chiX==2610
b4X=chiX-4
assert b4X==2606
gC=(d-1)*(d-2)//2
assert gC==10
chiFix=2*(2-2*gC)
assert chiFix==-36
tr4=chiFix-4
assert tr4==-40
b4Y=(b4X+tr4)//2
assert b4Y==1283
assert (chiX+chiFix)//2==4+b4Y==1287
# A quasi-reflection-free cyclic quotient of type 1/2(1,1,1).
assert 3*sp.Rational(1,2)>1
assert (-1)**3==-1
print('SEXTIC_QUOTIENT_EXACT_OK')
