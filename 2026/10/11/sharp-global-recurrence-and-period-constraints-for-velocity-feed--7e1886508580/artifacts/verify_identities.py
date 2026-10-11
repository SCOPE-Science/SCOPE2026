"""Symbolic checks for the velocity-feedback jerk recurrence theorem.

Requires Python 3 and sympy; the analytic proof is given separately.
"""
import sympy as s
x, v, a, A, k, l, t, R, c = s.symbols('x v a A k l t R c', real=True)
A = s.symbols('A', positive=True)
f = s.Function('f')
F = s.Function('F')
flow = [v, a, -A*a - x + f(v)]

def lie(phi):
    return s.expand(sum(s.diff(phi, u)*p for u,p in zip([x,v,a],flow)))

q = a*a/s.Integer(2) + x*v - F(v)
qprime = lie(q).subs(s.diff(F(v),v), f(v))
assert s.simplify(qprime - (v*v - A*a*a)) == 0
assert s.simplify(lie(v*a) - (a*a - A*v*a - x*v + v*f(v))) == 0
assert lie(v*v/s.Integer(2)) == v*a
assert lie(x*x/s.Integer(2)) == x*v
J = s.Matrix([[0, 1, 0], [0, 0, 1], [-1, k, -A]])
charpoly = s.expand((l*s.eye(3) - J).det())
assert charpoly == l**3 + A*l**2 - k*l + 1
assert s.simplify(charpoly.subs(k, -1/A) - (l+A)*(l*l+1/A)) == 0
# Sharpness at the critical affine feedback on the periodic velocity interval:
xh = c + R*s.sqrt(A)*s.sin(t/s.sqrt(A))
vh = s.diff(xh,t)
ah = s.diff(vh,t)
assert s.simplify(s.diff(ah,t)+A*ah+xh-(c-vh/A)) == 0
# Original Sprott quadratic case has weighted velocity law v^3+v^2/A=0.
assert s.expand(v*f(v)+v*v/A).subs(f(v),v*v) == v**3+v**2/A
print('VERIFY_OK')
