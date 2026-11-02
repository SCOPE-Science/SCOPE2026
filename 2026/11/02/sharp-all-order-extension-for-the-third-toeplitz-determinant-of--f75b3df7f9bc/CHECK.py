"""Supplementary coefficient algebra and finite Schur-parameter checks.

The universal inequality is established analytically in RESULT.md.
These tests check identities and selected admissible coefficient triples only.
"""
import cmath
import random
from fractions import Fraction
import sympy as sp

D, x, y, w = sp.symbols('D x y w')
a2 = 2*D*x
a3 = D*y + 2*D**2*x**2
a4 = sp.Rational(2,3)*D*w + 2*D**2*x*y + sp.Rational(4,3)*D**3*x**3
M = sp.Matrix([[a2,a3,a4],[a3,a2,a3],[a4,a3,a2]])
assert sp.expand(M.det() - (a2-a4)*(a2*a2+a2*a4-2*a3*a3)) == 0
S=6*x*x+2*x*w-3*y*y
assert sp.expand((a2*a2+a2*a4-2*a3*a3) - sp.Rational(2,3)*D**2*(S-6*D*x*x*y-8*D**2*x**4)) == 0
for d in [sp.Rational(1,1),sp.Rational(1,3),sp.Rational(1,5),sp.Rational(1,17),sp.Rational(1,99)]:
    for xx in [sp.I, -sp.I]:
        val=sp.simplify(M.det().subs({D:d,x:xx,y:xx**2,w:xx**3}))
        sharp=sp.Rational(4,9)*d**3*(4+3*d+2*d*d)*(7+6*d+8*d*d)
        assert sp.simplify(val*sp.conjugate(val)-sharp**2)==0

rng = random.Random(76174)
checks=0
for i in range(12000):
    r=rng.random()**0.5
    phi=rng.uniform(-3.141592653589793,3.141592653589793)
    xx=r*cmath.exp(1j*phi)
    s=rng.random()**0.5
    u=s*cmath.exp(1j*rng.uniform(-3.141592653589793,3.141592653589793))
    v=rng.random()**0.5*cmath.exp(1j*rng.uniform(-3.141592653589793,3.141592653589793))
    h=1-abs(xx)**2
    yy=xx**2+h*u
    ww=xx**3+h*(2*xx*u-xx.conjugate()*u**2+(1-abs(u)**2)*v)
    S0=6*xx**2+2*xx*ww-3*yy**2
    assert abs(S0) <= 7+1e-10
    d=rng.random()
    aa2=2*d*xx
    aa3=d*yy+2*d*d*xx**2
    aa4=2*d*ww/3+2*d*d*xx*yy+4*d**3*xx**3/3
    determinant=(aa2-aa4)*(aa2**2+aa2*aa4-2*aa3**2)
    bound=4*d**3*(4+3*d+2*d*d)*(7+6*d+8*d*d)/9
    assert abs(determinant) <= bound+1e-10
    checks+=2
print(f'PASS: symbolic determinant/factorization/sharpness and {checks} finite Schur checks')
