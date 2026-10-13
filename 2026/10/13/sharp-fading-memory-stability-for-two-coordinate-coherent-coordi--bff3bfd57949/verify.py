"""Reproduce the algebra for the two-coordinate fading-buffer CoCD stability theorem.

Dependencies: Python 3.10+, sympy, numpy. All tests deterministic.
The exhaustive claims are proved in RESULT.md; numerical checks here are diagnostic.
"""
import itertools
import math
from fractions import Fraction
import sympy as sp
import numpy as np

A, G, R, Z = sp.symbols('A G R Z', real=True)
S1 = sp.Matrix([[1-A, -A*R, 0, 0],
                [0, 1, 0, -A*G],
                [1, R, 0, 0],
                [0, 0, 0, G]])
S2 = sp.Matrix([[1, 0, -A*G, 0],
                [-A*R, 1-A, 0, 0],
                [0, 0, G, 0],
                [R, 1, 0, 0]])
T = (S2 * S1).extract([0, 1, 3], [0, 1, 3])
T_expected = sp.Matrix([
    [1-A*(1+G), -A*R*(1+G), 0],
    [-A*R*(1-A), 1-A+A**2*R**2, -A*G*(1-A)],
    [R*(1-A), 1-A*R**2, -A*G],
])
assert all(sp.expand(z)==0 for z in T-T_expected)
b = -2+2*A*(1+G)-A**2*R**2
c = (1-A*(1+G))**2-2*A**2*G*R**2
d = -A**2*G**2*R**2
p = Z**3 + b*Z**2 + c*Z + d
assert sp.expand((Z*sp.eye(3)-T).det() - p) == 0
assert sp.expand(p.subs(Z,1)-A**2*(1+G)**2*(1-R**2)) == 0
assert sp.expand(-p.subs(Z,-1)-((2-A*(1+G))**2 + A**2*R**2*(1-G)**2)) == 0
F = sp.factor(1-c+b*d-d*d)
assert sp.expand(F-A*(1+G)*(1+A*G*R**2)*(2-A*(1+G)+A**2*G*(1-G)*R**2)) == 0
assert sp.expand(p.subs({A:1,G:1})-(Z-R**2)*(Z+1)**2) == 0
assert sp.expand(p.subs(R,0)-Z*(Z-1+A*(1+G))**2) == 0

count=0
for g,r in itertools.product(
    [0, 0.01, 0.1, 0.25, 1/3, 0.5, 0.75, 0.99, 1.0],
    [0, 0.01, 0.3, 0.6, 0.9, 0.99, -0.6, -0.99]):
    delta = (1+g)**2-8*g*(1-g)*r*r
    assert delta >= -1e-12
    crit = 4 / ((1+g)+math.sqrt(max(0,delta)))
    for scale in [0.01, 0.2, 0.8, 0.999, 1.001, 1.2, 2, 5]:
        a = crit*scale
        mat = np.array(T.subs({A:a,G:g,R:r})).astype(float)
        sr = max(abs(np.linalg.eigvals(mat)))
        if scale < 1:
            assert sr < 1 - 1e-10, (g,r,a,crit,sr)
        else:
            assert sr > 1 + 1e-10, (g,r,a,crit,sr)
        count += 1

# At the unit-circle boundary check spectral modulus and the remaining root.
for g,r in [(0,0.8),(0.1,0.2),(.25,.99),(.5,.7),(.99,.2),(1,.9)]:
    a=4/(1+g+math.sqrt((1+g)**2-8*g*(1-g)*r*r))
    roots=np.linalg.eigvals(np.array(T.subs({A:a,G:g,R:r})).astype(float))
    assert abs(max(abs(roots))-1)<1e-8, (g,r,a,roots)

# Quadratic central differences equal the exact coordinate gradient for any h != 0.
x,y,h,rr = sp.symbols('x y h rr',real=True, nonzero=True)
f = lambda u,v: (u*u+v*v)/2+rr*u*v
assert sp.simplify((f(x+h,y)-f(x-h,y))/(2*h)-(x+rr*y))==0
assert sp.simplify((f(x,y+h)-f(x,y-h))/(2*h)-(y+rr*x))==0

print(f'VERIFY_OK symbolic identities; {count} matrix-root checks; 6 boundary checks; central differences')
