#!/usr/bin/env python3
"""Exact symbolic checks for weighted phase-volume identities of a damped oscillator."""
import sympy as s

x, y, z, a, b, lam = s.symbols('x y z a b lam', real=True)
state = s.Matrix([x, y, z])
F = s.Matrix([y - b*x, y*z - x, a - y**2])
Psi = (-x**2 + y**2 + z**2)/(2*a) - z/(a*b)
D = s.factor(s.trace(F.jacobian(state)))
dPsi = s.factor(s.Matrix([s.diff(Psi, v) for v in state]).dot(F))
q = (y-b*x)**2/(a*b)
rate = 1/b-b
assert s.simplify(D - (z-b)) == 0
assert s.simplify(dPsi - (z-1/b+q)) == 0
assert s.simplify(D - dPsi - (rate-q)) == 0
for sign in [1, -1]:
    pt = {x:sign*s.sqrt(a)/b, y:sign*s.sqrt(a), z:1/b}
    assert all(s.simplify(f.subs(pt)) == 0 for f in F)
    assert s.simplify(q.subs(pt)) == 0
    assert s.simplify(D.subs(pt)-rate) == 0
    J = F.jacobian(state).subs(pt)
    char = s.factor((lam*s.eye(3) - J).det())
    expect = lam**3 + (b-1/b)*lam**2 + 2*a*lam + 2*a*b
    assert s.simplify(char-expect) == 0
# Algebraic exhaustion of stationary points: y=bx and a=y**2 => y != 0;
# yz=x then forces z=1/b and x=y/b. This is a hand-checked proof step.
print('PASS: exact coboundary, weighted divergence, equilibria, and characteristic polynomial')
