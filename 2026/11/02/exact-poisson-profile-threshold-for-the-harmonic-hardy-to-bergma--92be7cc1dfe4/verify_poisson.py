#!/usr/bin/env python3
"""Exact symbolic consistency checks for the normalized harmonic Poisson-profile fourth norm."""
import sympy as S
x,k=S.symbols('x k', positive=True)
Q=(1+9*x+9*x*x+x**3)/(1-x)**3
F=S.factor(Q/(1-x)**4)
D=lambda f:S.expand(x*S.diff(f,x))
# a_k = binomial(k+3,3)^2, and (k+1)^2 a_(k+1)=(k+4)^2 a_k
assert S.simplify((1-x)*D(D(F))-8*x*D(F)-16*x*F)==0
assert S.limit(F,x,0)==1
assert S.simplify(F-(1+9*x+9*x*x+x**3)/(1-x)**7)==0
I=-x-12*S.log(1-x)+20-30/(1-x)+10/(1-x)**2
assert S.simplify(S.diff(I,x)-Q)==0
assert S.limit(I,x,0)==0
R=(1-x)**2*I/(x*(1+x)**2)
N=3*(x-1)*(x*x-4*x-1)*S.log(1-x)-9*x**3+11*x**2+3*x
assert S.simplify(S.diff(R,x)-4*N/(x*x*(1+x)**3))==0
assert S.limit(R,x,0,dir='+')==1
assert S.limit(R,x,1,dir='-')==S.Rational(5,2)
for j in range(2,24):
 c=S.expand(S.series(N,x,0,j+1).removeO()).coeff(x,j)
 target=S.Rational(1,2) if j in (2,3) else S.Rational(6)*(2*j*j-8*j+3)/(j*(j-1)*(j-2)*(j-3))
 assert S.simplify(c-target)==0,(j,c,target)
assert S.simplify(-3/k-9/(k-1)+15/(k-2)-3/(k-3)-6*(2*k*k-8*k+3)/(k*(k-1)*(k-2)*(k-3)))==0
assert all((2*j*j-8*j+3)>0 for j in range(4,100))
print('SYMBOLIC_POISSON_PROFILE_OK: moment, integral, monotonicity coefficients and endpoint')
