#!/usr/bin/env python3
"""Exact algebraic check of the prime-three rational-map identities.

Dependency: SymPy. All assertions use integers and rational polynomials;
no floating point or experimental orbit sampling is needed.
"""
import sympy as s

m, x = s.symbols('m x')
K = lambda t: s.cancel(m * t * (1-t) / (1+t))
U = K(x)
V = K(U)
W = K(V)
ratio = s.cancel((W - x) / (U - x))
P, Q = s.fraction(ratio)
P, Q = s.expand(P), s.expand(Q)

coefficients = [
 m**2+m+1,
 -(m**2-3)*(m**2+m+1),
 (m**2+m+1)*(2*m**3-2*m**2-2*m+3),
 -m**6-3*m**5+3*m**4+2*m**3-3*m**2-3*m+1,
 m*(m**2-m+1)*(3*m**3+2*m**2-2*m-2),
 -m**2*(3*m**2-1)*(m**2-m+1),
 m**4*(m**2-m+1)
]
expected = sum(coefficients[j]*x**j for j in range(7))
assert s.expand(P-expected) == 0

N1=m*x*(1-x)
D1=1+x
N2=m*N1*(D1-N1)
D2=D1*(D1+N1)
assert s.expand(Q-(D1+N1)*(D2+N2)) == 0

A=m**4-4*m**3-10*m**2+4*m+1
B=m**4-6*m**3+10*m**2+6*m+1
expected_disc=256*m**16*(m**2-m+1)**2*(m**2+m+1)**2*B**2*A**3
assert s.factor(s.discriminant(P, x)-expected_disc)==0
assert s.factor(P.subs(x,0)-(m*m+m+1))==0
assert s.factor(P.subs(x,1)-8)==0
assert s.factor(P.subs(x,(m-1)/(m+1)) - 16*m**4*B/(m+1)**6)==0
assert s.factor(B-((m*m-3*m-1)**2+3*m*m)) == 0
assert A.subs(m,s.Rational(1,2))>0
assert A.subs(m,1)<0
assert A.subs(m,s.Rational(5641,1000))<0
assert A.subs(m,s.Rational(5642,1000))>0
assert A.subs(m,s.Rational(23,4))>0

T=s.Poly(P.subs(m,s.Rational(23,4)),x)
brackets=[(725,726),(1062,1063),(3606,3607),(4935,4936),(9623,9624),(9744,9745)]
for j,(a,b) in enumerate(brackets):
 assert 0<a<b<10000
 left=T.eval(s.Rational(a,10000))
 right=T.eval(s.Rational(b,10000))
 assert left*right<0, (a,b)
 assert s.sign(left)==(1 if j%2==0 else -1)
 assert s.sign(right)==(-1 if j%2==0 else 1)
print('PASS: 7 polynomial coefficients, exact denominator, discriminant, fixed-point exclusions,')
print('      threshold bracketing, and 6 exact rational sign-changing root intervals.')
