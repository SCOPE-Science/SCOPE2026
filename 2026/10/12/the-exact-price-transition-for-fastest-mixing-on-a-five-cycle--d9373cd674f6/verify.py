#!/usr/bin/env python3
"""Exact symbolic checks for the five-cycle priced-edge mixing theorem.

Requires Python 3 and SymPy. The manuscript supplies the infinite-parameter proof;
this program checks its algebraic certificates and exact sign encodings.
"""
from math import comb
import sympy as s

u, z, x = s.symbols('u z x', real=True)
f = 5*u**2 - 6*u + 2
T = (5*u-4)*(5*u-2)*f**2/((u-1)*(2*u-1)*(5*u-3)**2)
B = (2*u-1)/(5*u-3)
Q = (2*u-1)**2/f
R = u*(5*u-3)/f
E = 1-1/u
S = 2/u-4
e = s.Matrix([1,E,S,E,1])
o = s.Matrix([1,R,0,-R,-1])
Co = T/4
Ce = s.factor(u**2*(1-Co*(1-R)**2))
assert s.factor(Ce + u**2*(5*u**2-2)*f/(4*(u-1)*(2*u-1)*(5*u-3)**2)) == 0
assert s.expand(sum(e)) == 0
assert s.factor(sum(o)) == 0
L = s.zeros(5)
edges = [(0,1,u,1),(1,2,B,1),(2,3,B,1),(3,4,u,1),(0,4,Q,T)]
for i,j,w,price in edges:
    L[i,i] += w; L[j,j] += w
    L[i,j] -= w; L[j,i] -= w
    assert s.factor(Ce*(e[i]-e[j])**2+Co*(o[i]-o[j])**2-price) == 0
assert all(s.factor(v) == 0 for v in L*e-e)
assert all(s.factor(v) == 0 for v in L*o-o)
assert s.factor(2*u+B+2*Q-1-(2*u-1)*(25*u**3-20*u**2+2)/((5*u-3)*f)) == 0
assert s.factor(5*u*B - 1 - (10*u**2-10*u+3)/(5*u-3)) == 0

P6 = 2500*u**6-10125*u**5+16575*u**4-14100*u**3+6600*u**2-1620*u+164
assert s.factor(s.diff(T,u)-f*P6/((u-1)**2*(2*u-1)**2*(5*u-3)**3)) == 0

def bernstein_coefficients(polynomial, degree):
    """Bernstein coefficients after u=(3+z)/5 on z in [0,1]."""
    p = s.Poly(s.expand(polynomial.subs(u,(3+z)/5)), z)
    a = [p.nth(j) for j in range(degree+1)]
    return [s.factor(sum(a[j]*s.Rational(comb(k,j),comb(degree,j))
                         for j in range(k+1))) for k in range(degree+1)]

assert bernstein_coefficients(P6,6) == [
    -s.Rational(4,25),-s.Rational(11,50),-s.Rational(31,125),
    -s.Rational(29,125),-s.Rational(24,125),
    -s.Rational(6,25),-s.Rational(12,25)]
odd_poly = 50*u**4-90*u**3+65*u**2-24*u+4
assert bernstein_coefficients(odd_poly,4) == [
    s.Rational(1,25),s.Rational(1,25),s.Rational(17,150),
    s.Rational(8,25),s.Rational(4,5)]
assert s.factor((2*u+B+2*Q-2)-(odd_poly/((5*u-3)*f))) == 0
assert s.simplify(T.subs(u,s.sqrt(s.Rational(2,5)))-16) == 0
assert s.limit(T,u,s.Rational(4,5),dir='-') == 0

# Endpoint family: chord q, other edges a=1/5-4q, b=3/10-4q.
ap=s.Rational(1,5)-4*x
bp=s.Rational(3,10)-4*x
assert s.factor(2*ap+2*bp+16*x-1)==0
boundary=s.factor(5*ap*bp-s.Rational(1,10)*(2*ap+3*bp)+s.Rational(1,100))
assert s.factor(boundary - (4000*x**2-400*x+9)/50)==0
r0 = s.Rational(1,20)-s.sqrt(10)/200
assert s.simplify(boundary.subs(x,r0)) == 0
v=s.Matrix([-2,-1,0,1,2])
Lp=s.zeros(5)
for i,j,w in [(0,1,ap),(1,2,bp),(2,3,bp),(3,4,ap),(0,4,x)]:
    Lp[i,i]+=w; Lp[j,j]+=w; Lp[i,j]-=w; Lp[j,i]-=w
assert all(s.factor(t)==0 for t in Lp*v-v/10)

# Exact equal-cost cycle: u=(5+sqrt(5))/10, all five conductances 1/5.
u1=(5+s.sqrt(5))/10
assert s.simplify(T.subs(u,u1)-1)==0
D=2*u+2*B+T*Q
assert s.simplify((1/D).subs(u,u1)-(5-s.sqrt(5))/10)==0
for weight in (u,B,Q):
    assert s.simplify((weight/D).subs(u,u1)-s.Rational(1,5))==0
print('VERIFY_OK exact five-cycle algebra, Bernstein signs and endpoint identities')
