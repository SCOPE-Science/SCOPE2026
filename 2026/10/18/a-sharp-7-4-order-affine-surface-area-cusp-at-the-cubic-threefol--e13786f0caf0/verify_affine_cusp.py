#!/usr/bin/env python3
"""Exact local algebra and an independent curvature check for a cubic support body.

Run with Python 3 and SymPy; NumPy is used only for supplementary sampling.
All the limiting claims in the accompanying proof are analytic, not simulated.
"""
import itertools
import math
import sympy as sp
import numpy as np

s, t, eps = sp.symbols('s t eps', real=True)
e_star = 3 * sp.sqrt(6) / 8
u0 = sp.Matrix([2, 1, 1]) / sp.sqrt(6)
v1 = sp.Matrix([0, 1, -1]) / sp.sqrt(2)
v2 = sp.Matrix([-1, 1, 1]) / sp.sqrt(3)
assert sp.simplify(u0.dot(v1)) == 0
assert sp.simplify(u0.dot(v2)) == 0
assert sp.simplify(v1.dot(v2)) == 0
assert sp.simplify(v1.dot(v1)) == 1
assert sp.simplify(v2.dot(v2)) == 1


def det_formula(u, e):
    x, y, z = u
    q = x*y*z
    r = x*x*y*y + x*x*z*z + y*y*z*z
    return 1 - 10*e*q + e**2*(4*r + 16*q*q - 1)


u = sp.sqrt(1-s*s-t*t)*u0 + s*v1 + t*v2
f = det_formula(u, e_star)
origin = {s: sp.Integer(0), t: sp.Integer(0)}
checks = {
    'D_at_contact': sp.simplify(f.subs(origin)),
    'D_s_at_contact': sp.simplify(sp.diff(f, s).subs(origin)),
    'D_t_at_contact': sp.simplify(sp.diff(f, t).subs(origin)),
    'D_ss_at_contact': sp.simplify(sp.diff(f, s, 2).subs(origin)),
    'D_st_at_contact': sp.simplify(sp.diff(f, s, t).subs(origin)),
    'D_tt_at_contact': sp.simplify(sp.diff(f, t, 2).subs(origin)),
    'minus_D_e_at_contact': sp.simplify((-sp.diff(det_formula(u, eps), eps)).subs({**origin, eps:e_star})),
}
expected = [0,0,0,sp.Rational(27,4),0,sp.Rational(9,8),sp.sqrt(6)/3]
for v, want in zip(checks.values(),expected):
    assert sp.simplify(v-want)==0, (v,want)

# Derive the tangent determinant directly from the ambient Hessian, independently
# of the closed formula, using a rational orthonormal tangent frame.
p = sp.Matrix([sp.Rational(3,5),sp.Rational(4,5),0])
a = sp.Matrix([sp.Rational(-4,5),sp.Rational(3,5),0])
b = sp.Matrix([0,0,1])
x,y,z=p
H=sp.Matrix([[0,z,y],[z,0,x],[y,x,0]])
q=x*y*z
M = sp.Matrix([[a.dot(H*a)-2*q, a.dot(H*b)],
               [b.dot(H*a), b.dot(H*b)-2*q]])
assert sp.simplify((sp.eye(2)+eps*M).det()-det_formula(p,eps))==0

# Check all twelve support-radius contacts at the sharp parameter.
contacts = set()
for perm in set(itertools.permutations((2,1,1))):
    for signs in itertools.product((-1,1),repeat=3):
        if math.prod(signs) != 1: continue
        point=tuple(sp.Integer(signs[i]*perm[i])/sp.sqrt(6) for i in range(3))
        contacts.add(point)
assert len(contacts)==12
for point in contacts:
    assert sp.simplify(det_formula(point,e_star))==0
    assert sp.simplify(2-10*e_star*sp.prod(point)-sp.Rational(3,4))==0

# The singular coefficient is the integral of the local quadratic model:
# -12*pi*a**(p+1)/((p+1)*sqrt(b*c)), with p=3/4.
power=sp.Rational(3,4)
a_const=sp.sqrt(6)/3
b_const=sp.Rational(27,8)
c_const=sp.Rational(9,16)
C=sp.simplify(12*sp.pi*a_const**(power+1)/((power+1)*sp.sqrt(b_const*c_const)))
C_expected=256*sp.pi/(21*sp.sqrt(6))*(sp.sqrt(6)/3)**sp.Rational(7,4)
assert sp.simplify(C-C_expected)==0
# Independent 2nd-variation coefficient: -12*p*pi*a**(p+1)/sqrt(b*c).
K=sp.simplify(-12*power*sp.pi*a_const**(power+1)/sp.sqrt(b_const*c_const))
assert sp.simplify(K+power*(power+1)*C)==0

# Supplementary, NOT a proof of global nonnegativity. The geometric Fourier
# inequality in the accompanying text proves nonnegativity for all normals.
rng=np.random.default_rng(20261015)
vectors=rng.normal(size=(10000,3))
vectors/=np.linalg.norm(vectors,axis=1)[:,None]
vals=np.array([float(det_formula(v, float(e_star))) for v in vectors])
assert np.min(vals)>=-1e-12

print('PASS: exact tangent determinant, twelve contact normals, local Hessian,')
print('      first parameter variation, and singular-integral coefficient.')
print('Coefficient C =',sp.sstr(C))
print('C decimal =',float(C.evalf(17)))
print('Supplementary sample D_min =',float(np.min(vals)))
for k,v in checks.items():print(k,'=',v)
