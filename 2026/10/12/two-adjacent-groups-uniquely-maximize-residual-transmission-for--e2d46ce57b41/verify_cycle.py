#!/usr/bin/env python3
"""Exact arithmetic checks for the five-cycle vaccination theorem.

Requires SymPy >=1.12. The analytic compactness and extremal arguments are
proved in RESULT.md, not replaced by this finite symbolic verification.
"""
import sympy as s

n = 5
K = s.zeros(n)
for i in range(n):
    K[i,(i+1)%n] = 1
    K[i,(i-1)%n] = 1
J = s.ones(n)/n
R = (2*s.eye(n)-K+J).inv()-J
assert s.simplify((2*s.eye(n)-K)*R-(s.eye(n)-J)) == s.zeros(n)
assert s.simplify(R*J) == s.zeros(n)
assert s.simplify(J*R) == s.zeros(n)
Qmat = s.Rational(2,n)*R*K
expected=s.zeros(n)
for i in range(n):
    for j in range(n):
        if i==j:
            expected[i,j]=0
        elif (i-j)%n in (1,n-1):
            expected[i,j]=s.Rational(2,25)
        else:
            expected[i,j]=-s.Rational(2,25)
assert Qmat==expected, (Qmat,expected)
u=s.symbols('u0:5', real=True)
U=s.Matrix(u)
q=s.expand((U.T*Qmat*U)[0])
edge=sum(u[i]*u[(i+1)%5] for i in range(5))
nonedge=sum(u[i]*u[(i+2)%5] for i in range(5))
assert s.expand(q-s.Rational(4,25)*(edge-nonedge))==0
v=s.Matrix([s.Rational(1,2),s.Rational(1,2),0,0,0])
assert (v.T*Qmat*v)[0]==s.Rational(1,25)
grad=2*Qmat*v
assert grad == s.Matrix([s.Rational(2,25),s.Rational(2,25),0,-s.Rational(4,25),0])
a=s.symbols('a')
assert s.expand(q.subs(dict(zip(u,[a,1-a,0,0,0])))-s.Rational(4,25)*a*(1-a))==0

e,z=s.symbols('epsilon z')
C0=(z*z+z-1)
P0=z**3-z**2-3*z+2
single=s.diag(1-e,1,1,1,1)
adj=s.diag(1-e/2,1-e/2,1,1,1)
poly_single=s.factor((z*s.eye(n)-K*single).det(method='berkowitz'))
poly_adj=s.factor((z*s.eye(n)-K*adj).det(method='berkowitz'))
assert s.expand(poly_single-C0*(P0+2*e*(z-1)))==0
assert s.expand(poly_adj-s.Rational(1,4)*(2*C0-e*(z-1))*(2*P0+e*(z*z+z-2)))==0
b=s.symbols('b')
for poly,second in [(poly_single,s.Rational(0)),(poly_adj,s.Rational(1,25))]:
    target=z.subs(z,2-s.Rational(2,5)*e+b*e*e)
    expansion=s.series(poly.subs(z,target),e,0,3).removeO().expand()
    assert s.solve(expansion.coeff(e,2),b)==[second]

print('VERIFY_OK: exact resolvent, quadratic expansion, maximizer derivatives, and both characteristic factors')
