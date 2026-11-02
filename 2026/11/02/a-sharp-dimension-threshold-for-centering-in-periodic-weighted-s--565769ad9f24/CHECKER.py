"""Independent symbolic identities and finite-dimensional diagnostics for the theorem.

Requires Python 3, sympy, numpy. The proof is analytic; finite computations
below check identities and the predicted leading perturbative coefficients.
"""
from math import sqrt
import numpy as np
import sympy as s

x = s.symbols('x', real=True)
quadratic = s.Rational(9, 16) * (1 + 14*x - 15*x*x)
assert s.simplify(s.Rational(12, 5) - quadratic - s.Rational(135,16)*(x-s.Rational(7,15))**2) == 0

# The two-supported explicit maximizer (three-periodic case).
i = s.I
z = s.Matrix([3-i*s.sqrt(111),0,3+i*s.sqrt(111)])
P = s.eye(3) - s.ones(3,3)/3
y = s.simplify(P*z)
assert list(y) == [1-i*s.sqrt(111), -2, 1+i*s.sqrt(111)]
assert s.simplify(sum(s.expand_complex(v*s.conjugate(v)) for v in z)-240) == 0
assert s.simplify(sum(s.expand_complex(v*s.conjugate(v)) for v in y)-228) == 0
# For triangle edge moduli (4 sqrt 7,2,4 sqrt 7), eigenvalue 8.
a,b,c = 4*s.sqrt(7), s.Integer(2), 4*s.sqrt(7)
assert 4*8**3-8*(a*a+b*b+c*c)-a*b*c == 0

def radius(weights):
    weights=np.abs(np.asarray(weights, dtype=complex))
    n=len(weights)
    mat=np.zeros((n,n),float)
    for j in range(n):
        k=(j+1)%n
        mat[j,k]+=weights[j]/2
        mat[k,j]+=weights[j]/2
    return np.linalg.eigvalsh(mat)[-1]

assert abs(radius([complex(v.evalf()) for v in z]) - 2*sqrt(15)) < 1e-11
assert abs(radius([complex(v.evalf()) for v in y]) - 8) < 1e-11
assert abs(radius([complex(v.evalf()) for v in y])/radius([complex(v.evalf()) for v in z]) - 4/sqrt(15)) < 1e-11

# The special dimension-2 formula has doubled cycle-edge accounting.
for a0,a1 in [(1+2j,-3+4j),(2.1,-1.8),(0,4j)]:
    inp=(abs(a0)+abs(a1))/2
    out=abs(a0-a1)/2
    assert out<=inp+1e-12

# Isolated two-edge degeneracy: the slope equals 1/n (n=4), 1/(2n) (n>=5)
for n in range(4,14):
    eps=1e-5
    z=np.zeros(n, complex)
    z[0]=1
    z[2]=-np.exp(1j*eps)
    pp=z-z.mean()
    ratio=radius(pp)/radius(z)
    pred=1/n if n==4 else 1/(2*n)
    assert ratio > 1
    assert abs((ratio-1)/eps-pred) < 2e-4,(n,(ratio-1)/eps,pred)

print('PASS: exact quadratic certificate, exact three-cycle witness, two-cycle triangle inequality, and 10 degenerate-edge perturbation checks')
