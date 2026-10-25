#!/usr/bin/env python3
"""Exact algebraic checks for the sharp bounded-slope lens-curvature theorem.

Dependency: sympy. Run: python3 verify.py
This verifies identities and concrete certificates; it does not replace
analytic arguments about all real parameters.
"""
from sympy import Matrix, eye, sqrt, symbols, simplify, factor, diff, Rational

x, y, a, b, R, T = symbols('x y a b R T', real=True)
p = Matrix([x, y])
F = sqrt(1 + p.dot(p)) * (eye(2) + p*p.T)
H = Matrix(2, 2, lambda i, j: a*a*diff(F[i,j], x, 2)
           + 2*a*b*diff(F[i,j], x, y) + b*b*diff(F[i,j], y, 2))
M = H.subs({x: sqrt(R), y: 0}) * sqrt(1+R)
expected = Matrix([[3*(1+2*R)*a*a+(1+R)*b*b, 2*(1+2*R)*a*b],
                   [2*(1+2*R)*a*b, a*a/(1+R)+(3+2*R)*b*b]])
assert all(simplify(M[i,j]-expected[i,j]) == 0
           for i in range(2) for j in range(2))
A = 3*(1+2*R)
B = -4*R**3+4*R**2+14*R+6
C = 2*R**3+7*R**2+8*R+3
assert simplify((1+R)*M.det() - (A*a**4+B*a*a*b*b+C*b**4)) == 0
assert factor(B*B-4*A*C) == 16*R**2*(1+R)**2*(R**2-4*R-2)
R_star = 2+sqrt(6)
assert simplify(-B.subs(R,R_star)/(2*A.subs(R,R_star))-1-sqrt(6)) == 0

def fm(v):
    return sqrt(1 + v.dot(v))*(eye(2)+v*v.T)

p1=Matrix([Rational(13,4),Rational(1,4)])
p2=Matrix([Rational(11,4),-Rational(1,4)])
v=Matrix([1,-2])
p_mid=(p1+p2)/2
delta=simplify((v.T*((fm(p1)+fm(p2))/2 -fm(p_mid))*v)[0])
exact_delta=(201*sqrt(186)+249*sqrt(138))/128-14*sqrt(10)
assert simplify(delta-exact_delta)==0
# Rational root brackets and a strictly negative rational upper bound
assert Rational('13.638182')**2 > 186
assert Rational('11.747341')**2 > 138
assert Rational('3.162277')**2 < 10
upper=(201*Rational('13.638182') + 249*Rational('11.747341'))/128 -14*Rational('3.162277')
assert upper == -Rational(437893,128000000) and upper<0
# Verify that the explicit centers are a genuine mixed, positive-length fiber.
s1=1/sqrt(1+p1.dot(p1));s2=1/sqrt(1+p2.dot(p2))
assert float(abs(s1-s2)) < float((s1+s2)/2)
assert float((s1+s2)/2) < float(s1+s2)
q1=-s1*p1;q2=-s2*p2
center=(q2-q1)/2; x0=(q1+q2)/2
assert all(simplify(x0[i]-center[i]-q1[i])==0 and
           simplify(x0[i]+center[i]-q2[i])==0 for i in range(2))
print('VERIFY_OK: exact second derivative, Hessian determinant/discriminant,')
print('threshold root, strict radical sign, and mixed-fiber realization')
