"""Exact characteristic-zero polynomial checks for a quintic polar-map branch calculation.

Requires Python 3 and SymPy; no numerical approximation is used.
"""
import sympy as S

s, p, t, X, Y, x, y, z, u = S.symbols('s p t X Y x y z u')
f = x * ((x*z)**2 + s*x*z*y**2 + p*y**4)
P = t**2 + s*t + p
A = 3*t**2 + 2*s*t + p
B = s*t + 2*p
C = 2*t + s
Phi = 3*s*t**3 + 18*p*t**2 + (13*s*p - s**3)*t + s*s*p + 2*p*p
F = ((s*s-3*p)*X**3 + (-56*s**3+180*s*p)*X**2*Y
     + (16*s**4+720*s*s*p-3888*p*p)*X*Y**2
     - 192*s**3*p*Y**3)
Q = 3*s*(x*z)**3 + 18*p*(x*z)**2*y**2 + (13*s*p-s**3)*(x*z)*y**4 + (s*s*p+2*p*p)*y**6

assert S.expand(S.hessian(f, (x,y,z)).det() + 16*x**3*Q) == 0
partials = [S.diff(f, var) for var in (x,y,z)]
assert S.expand(partials[0].subs({x:u,y:1,z:t/u})-A) == 0
assert S.expand(partials[1].subs({x:u,y:1,z:t/u})-2*u*B) == 0
assert S.expand(partials[2].subs({x:u,y:1,z:t/u})-u**2*C) == 0
v, w = 2*u*B/A, u**2*C/A
jac = S.det(S.Matrix([[S.diff(v,u),S.diff(v,t)],
                      [S.diff(w,u),S.diff(w,t)]]))
assert S.factor(jac - 4*u**2*Phi/A**3) == 0
assert S.factor(S.discriminant(Phi,t) - 3*(s*s-4*p)**3*(4*s**4-108*s*s*p+243*p*p)) == 0
assert S.factor(S.resultant(Phi,A,t) - 9*p*(3*p-s*s)*(4*p-s*s)**2) == 0
assert S.factor(S.resultant(Phi,B,t) + 3*p*s*(4*p-s*s)**2) == 0
assert S.factor(S.resultant(Phi,C,t) + (4*p-s*s)**2) == 0
assert S.factor(S.resultant(Phi,A*C*X-4*B**2*Y,t) - 9*p*(s*s-4*p)**4*F) == 0
assert S.factor(S.discriminant(F.subs(Y,1),X) - 12288*(s*s-4*p)*(4*s**4-108*s*s*p+243*p*p)**3) == 0

specialized = S.factor(F.subs({s:1,p:1}))
assert S.expand(specialized + 2*(X**3-62*X**2*Y+1576*X*Y**2+96*Y**3)) == 0
assert S.expand(Phi.subs({s:1,p:1})-3*(t**3+6*t**2+4*t+1)) == 0
print('PASS: symbolic Hessian, polar coordinates, Jacobian, nonvanishing resultants, discriminants, critical-image resultant, and example')
