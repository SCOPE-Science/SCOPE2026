#!/usr/bin/env python3
"""Exact symbolic checks for the cyclic plane-curve inflection-stratum theorem.

Requires sympy. The general theorem is established in RESULT.md; finite
parameter samples in this program are independent checks, not its proof.
"""
import math
from fractions import Fraction
import sympy as s

n,u,v=s.symbols('n u v')
A=(2*n*u+n**2*(n-1))*v-2*(n-2)*u**2+n*(n-2)*(n-3)*u
B=n**2*(u+n-1)*v-(n-2)**2*u**2
assert s.factor(s.resultant(A,B,v)) == n*u*(n-2)*(n+2*u)*(-n**3+4*n**2-3*n+2*u)

x,y,z,t=s.symbols('x y z t')
for N in range(5,11):
    F=y**N-x**N-t*x**(N-2)*z**2-z**N
    Hess=s.det(s.hessian(F, (x,y,z)))
    h=(2*N*t*x**N-2*(N-2)*t**2*x**(N-2)*z**2+
       N**2*(N-1)*x**2*z**(N-2)+N*(N-2)*(N-3)*t*z**N)
    assert s.expand(Hess - N*(N-1)**2*y**(N-2)*x**(N-4)*h)==0
    f0=x**N+x**(N-2)+1
    h0=s.expand(h.subs({t:1,z:1}))
    assert s.degree(s.gcd(f0,h0),x)==0
    assert s.degree(s.gcd(h0,s.diff(h0,x)),x)==0
    g=math.gcd(N,2)
    r=N//g
    power=(N-2)//g
    us=Fraction(N*(N-1)*(N-3),2)
    vs=Fraction((N-2)*(N-3)**2,2)
    ua=Fraction(-N,2)
    va=Fraction(N-2,2)
    K=us**r / vs**power
    S=ua**r / va**power
    assert K!=S
    assert us!=ua
    hxx=s.diff(h.subs(z,1),x,2)
    check=s.cancel(hxx.subs(t, s.Rational(us.numerator,us.denominator)/x**(N-2)))
    check=s.cancel(check-2*N**2*(N-1)*(N-2)**2)
    assert s.rem(s.together(check).as_numer_denom()[0],x**N-s.Rational(vs.numerator,vs.denominator),x)==0
    assert 3*N*(N-2)==N*(N-2)+N*(N-4)+N*N
    assert 3*N*(N-2)==N*(N-2)+N*(N-4)+N*(N-2*g)+2*N*g
    print('DEGREE_OK',N,'r',r,'singular_invariant',S,'jump_invariant',K)

N=5
f=x**5+t*x**3+1
h=10*t*x**5-6*t**2*x**3+100*x**2+30*t
assert s.factor(s.discriminant(f,x))==108*t**5+3125
assert s.factor(s.discriminant(h/2,x)) == -10125*t**3*(27*t**5-400000)*(108*t**5+3125)
assert s.factor(s.resultant(f,h/2,x)) == 32*(108*t**5+3125)**2
print('VERIFY_OK')
