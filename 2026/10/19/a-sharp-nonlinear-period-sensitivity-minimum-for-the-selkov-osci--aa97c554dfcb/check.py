"""Exact local Hopf calculations for the reduced Selkov kinetic oscillator.

Requirements: Python 3 and SymPy. Optional SciPy numerical checks are not needed
for the theorem. All assertions below use exact symbolic arithmetic.
"""
import sympy as s
k = s.symbols('k', positive=True, real=True)
I = s.I
gamma = 1 + k**2
alpha0 = k**(-2)
omega = k**(-1)
A = s.Matrix([[-1, -gamma], [alpha0, 1]])
q = s.Matrix([1, -(1 + I/k)/gamma])
qbar = s.conjugate(q)
left = s.simplify(s.Matrix.hstack(q, qbar).inv()[0, :])
assert all(s.simplify(v) == 0 for v in A*q - I*omega*q)
assert s.simplify((left*q)[0] - 1) == 0
assert s.simplify((left*qbar)[0]) == 0

def B(u,v):
    z = gamma*(u[0]*v[1]+u[1]*v[0]) + gamma*(gamma-1)*u[1]*v[1]
    return s.Matrix([-z, alpha0*z])

def C(u,v,w):
    z = gamma*(gamma-1)*(u[0]*v[1]*w[1]+u[1]*v[0]*w[1]+u[1]*v[1]*w[0])
    z += gamma*(gamma-1)*(gamma-2)*u[1]*v[1]*w[1]
    return s.Matrix([-z, alpha0*z])

G21 = s.factor((left*(C(q,q,qbar) - 2*B(q,A.inv()*B(q,qbar))
                         + B(qbar, (2*I*omega*s.eye(2)-A).inv()*B(q,q))))[0], extension=I)
expected = -s.Rational(1,2) - I*(2*k**4+k**2+2)/(6*k**3)
assert s.simplify(G21-expected) == 0
coefficient = -s.im(s.expand_complex(G21))/(8*omega)
expected_coefficient = (2*k**4+k**2+2)/(48*k**2)
assert s.simplify(coefficient-expected_coefficient) == 0
assert s.simplify(coefficient - s.Rational(5,48) - (k-1/k)**2/s.Integer(24)) == 0
assert s.simplify(s.re(s.expand_complex(G21)) + s.Rational(1,2)) == 0
print('Exact eigenpair, adjoint projection, quadratic/cubic tensors: PASS')
print('G21 =', G21)
print('C =', s.factor(coefficient))
print('C - 5/48 =', s.factor(coefficient-s.Rational(5,48)))
print('Unique minimum at gamma=2 and supercritical branch: PASS')
