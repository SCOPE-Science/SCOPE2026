#!/usr/bin/env python3
import sympy as s
wd, ws, alpha, beta = s.symbols('wd ws alpha beta', real=True)
q, k = s.symbols('q k', real=True)
l1 = (wd + ws)/2
l2 = (ws - wd)/2
phi0 = s.pi/4 + l1*q + l2*k
phi1 = s.pi/4 + l2*q + l1*k
t = alpha*(q+k)
mu = s.Rational(1,2)*(1 + s.cos(2*beta)**2*s.cos(phi0)
    - s.sin(2*beta)**2*(s.cos(phi0)*s.sin(phi1)*s.cos(t) + s.cos(phi1)*s.sin(t)))
params = (wd, ws, alpha, beta)
point = {wd:s.pi/2, ws:s.pi/3, alpha:s.pi/4, beta:s.pi/8}
inputs = [(-2,2),(-1,-2),(1,2),(2,2)]
J = s.Matrix([[s.trigsimp(s.diff(mu,p).subs({q:qv,k:kv,**point})) for p in params] for qv,kv in inputs])
r2=s.sqrt(2); r3=s.sqrt(3); r6=s.sqrt(6)
expected = s.Matrix([
    [-s.Rational(1,2)-r2/4, 0, 0, -s.Rational(1,2)+r2/2],
    [-r2/16, -3*r2/16, -3*r2/8, -1-r2/2],
    [s.Rational(1,8), -s.Rational(3,8), -3*r2/8, r2/2],
    [0, (-r6+r2+2*r3)/8, (-r6-r2)/4, -s.Rational(1,4)+(r2+r6)/4],
])
assert all(s.simplify(J[i,j]-expected[i,j]) == 0 for i in range(4) for j in range(4))
det = s.simplify(expected.det())
expected_det = s.Rational(111,512) + 87*r2/512 + 45*r3/256 + 129*r6/1024
assert s.simplify(det-expected_det) == 0
assert expected_det > 0
print('VERIFY_OK')
print('det =', expected_det)
