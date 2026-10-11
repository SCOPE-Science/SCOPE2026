#!/usr/bin/env python3
import sympy as s

th, eps = s.symbols("th eps", real=True)
sq = s.sqrt

def third_amplitude_sq(n):
    n = s.Matrix(n)
    seed = s.Matrix([0, 0, 1]) if abs(float(n[2])) < 0.9 else s.Matrix([1, 0, 0])
    v = seed - seed.dot(n) * n
    e1 = s.simplify(v / s.sqrt(v.dot(v)))
    e2 = s.simplify(n.cross(e1))
    u = e1*s.cos(th) + e2*s.sin(th)
    H = s.expand(u[0]*u[1]*u[2])
    C = s.simplify(s.integrate(H*s.cos(3*th), (th, 0, 2*s.pi))/s.pi)
    D = s.simplify(s.integrate(H*s.sin(3*th), (th, 0, 2*s.pi))/s.pi)
    return s.simplify(C*C + D*D), C, D

frames = [
    s.Matrix([1,0,0]),
    s.Matrix([0,0,1]),
    s.Matrix([1,1,1])/sq(3),
    s.Matrix([1,2,2])/3,
]
for n in frames:
    r2, C, D = third_amplitude_sq(n)
    target = s.simplify(s.prod(1-n[i]**2 for i in range(3))/16)
    assert s.simplify(r2-target) == 0

n = s.Matrix([1,1,1])/sq(3)
r2, C, D = third_amplitude_sq(n)
assert s.simplify(r2-s.Rational(1,54)) == 0
p = 1 + eps*(C*s.cos(3*th)+D*s.sin(3*th))
area = s.simplify(s.integrate(p*p-s.diff(p,th)**2, (th,0,2*s.pi))/2)
assert s.simplify(area-s.pi*(1-s.Rational(2,27)*eps**2)) == 0
print("VERIFY_OK")
