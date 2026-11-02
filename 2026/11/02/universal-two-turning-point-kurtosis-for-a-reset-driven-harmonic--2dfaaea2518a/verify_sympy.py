#!/usr/bin/env python3
"""Exact rational-symbolic check of the resetting-oscillator kurtosis theorem.
Requires sympy. Run: python verify_sympy.py
"""
import sympy as s

a,r=s.symbols('a r',positive=True)
x,v,z=s.symbols('x v z')
N=(9*a**4*r+27*a**4+91*a**3*r**3+87*a**3*r**2+108*a**3*r+54*a**3
   +199*a**2*r**5+535*a**2*r**4+510*a**2*r**3+204*a**2*r**2+18*a**2*r
   +21*a*r**7+47*a*r**6+37*a*r**5+11*a*r**4-18*a*r**3-18*a*r**2
   +21*r**7+93*r**6+141*r**5+87*r**4+18*r**3)
Q=r*(r+1)*(4*a+r*r+2*r)*(9*a+r*r+3*r)*(a+r*r+3*r+2)
K=3*N/((4*a+3)*Q)
# Direct finite-dimensional moment solves at independent rational parameter points.
# The proof gives the general moment recurrences, not an inference from tests.
for aa,rr in [(s.Rational(1,3),s.Rational(2,5)),(2,1),(s.Rational(7,2),3)]:
    mu={(0,0,0):s.Integer(1)}
    for n in (2,4):
        indices=[(i,j,n-i-j) for i in range(n+1) for j in range(n+1-i)]
        matrix=s.zeros(len(indices)); rhs=s.zeros(len(indices),1)
        for row,(i,j,k) in enumerate(indices):
            p=x**i*v**j*z**k
            generator=s.Poly(s.expand(v*s.diff(p,x)+(-aa*x-v+z)*s.diff(p,v)
                             +s.diff(p,z,2)+rr*(p.subs(z,0)-p)),x,v,z)
            for ex,coef in generator.terms():
                if sum(ex)==n: matrix[row,indices.index(ex)]=coef
                else:
                    assert ex in mu
                    rhs[row]-=coef*mu[ex]
        sol=matrix.LUsolve(rhs)
        for index,value in zip(indices,sol): mu[index]=value
    assert s.cancel(mu[(0,2,0)]-2/(aa+rr*rr+rr))==0
    assert s.cancel(mu[(0,4,0)]/mu[(0,2,0)]**2-3-2*K.subs({a:aa,r:rr}))==0
# Two independent equal walls double variance and double fourth cumulant,
# therefore halve their common single-wall standardized fourth cumulant.
P=s.expand(N*s.diff(Q,r)-s.diff(N,r)*Q)
assert s.simplify(s.diff(K,r)+3*P/((4*a+3)*Q**2))==0
p=s.Poly(P,r)
assert p.degree()==14
assert s.simplify(p.nth(14)-21*(a+1))==0
assert s.simplify(p.nth(0)-972*a**5*(a+2)**2)==0
# The named exceptional coefficient polynomials and their signs are
# proved analytically in RESULT.md; check their exact algebraic values.
assert s.simplify(p.nth(11)-2*(1013*a*a-2564*a+372))==0
assert s.simplify(p.nth(10)-(154*a**3+4111*a*a-22121*a-453))==0
assert all(s.factor(p.nth(j))!=0 for j in range(15))
t=s.symbols('t',positive=True)
H=(27200*t**10+112720*t**9+196248*t**8+179452*t**7
   +99362*t**6+84520*t**5+125063*t**4+117810*t**3
   +60009*t**2+15588*t+1620)
assert s.expand(P.subs({a:t*t,r:t})+t**6*H)==0
# Exact sign witnesses for the canonical equal-spring choice a=2.
assert p.eval(0).subs(a,2)>0
assert p.eval(1).subs(a,2)<0
assert p.eval(10).subs(a,2)>0
print('VERIFY_OK: exact degree-2/4 hierarchy, closed formula, derivative, Descartes witnesses')
