"""Supplementary checks for critical quartic Bessel gaps.

Run with Python 3, NumPy, SciPy and SymPy: python CHECK.py
Analytic Hankel asymptotics and the uniform Dirichlet argument are proved in RESULT.md;
finite checks here do not substitute for these infinite arguments.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import jv
import sympy as sp

checks = 0
r, j, A, B = sp.symbols('r j A B', real=True)
W = A*A + B*B
Ap = (j - 1)*A/r - B
Bp = A - j*B/r
flux_derivative = r*W*W + r*r*W*(2*A*Ap+2*B*Bp)
assert sp.simplify(flux_derivative-(2*j-1)*r*(A**4-B**4)) == 0
checks += 1

# Exact harmonic-number telescoping and the semigroup integral algebra.
for k in range(1, 61):
    odd = sum((Fraction(1,2*l-1) for l in range(1,k+1)), Fraction(0,1))
    harm2 = sum((Fraction(1,l) for l in range(1,2*k+1)), Fraction(0,1))
    harmk = sum((Fraction(1,l) for l in range(1,k+1)), Fraction(0,1))
    assert odd == harm2 - harmk/Fraction(2,1)
    assert odd > 0
    if k>1:
        last = sum((Fraction(1,2*l-1) for l in range(1,k)), Fraction(0,1))
        assert odd - last == Fraction(1,2*k-1)
        checks += 1
    checks += 2

# Exact finite-R flux verifies the integration normalization, without taking a numerical limit.
for k in range(1,9):
    for R in (2.5, 8.0, 25.0, 65.0, 125.0):
        a,b = float(jv(k-1,R)),float(jv(k,R))
        boundary = R*R*(a*a+b*b)**2 / (2*(2*k-1))
        value=quad(lambda x: x*(jv(k-1,x)**4-jv(k,x)**4),0,R,
                   epsabs=1e-10, epsrel=1e-10,limit=600)[0]
        assert abs(value-boundary) < 3.e-7, (k,R,value,boundary)
        checks+=1

# The semigroup representation is the same finite weighted harmonic sum.
for k in (1,2,3,5,13,30):
    semigroup = 0.5*quad(lambda t: math.exp(-t/2)*(-math.expm1(-k*t))/(-math.expm1(-t)),
                           0,65,epsabs=1e-11)[0]
    target = sum(1/(2*j-1) for j in range(1,k+1))
    assert abs(semigroup-target) < 1.e-9
    checks+=1

# Quadratic-form Poincare equality classes, on finitely supported test vectors.
for count in (2,5,17,44):
    for trial in range(5):
        coeff=np.array([complex(math.sin((i+1)*(trial+1)),math.cos((i+2)*(trial+1)))
                        for i in range(-count,count+1)])
        energies = np.array([sum(1/(2*j-1) for j in range(1,abs(i)+1))
                             for i in range(-count,count+1)])
        Q=(2/math.pi**2)*np.dot(energies, abs(coeff)**2)
        gap=(2/math.pi**2)*(np.dot(abs(coeff)**2, [int(i!=0) for i in range(-count,count+1)]))
        assert Q>=gap-1.e-12
        checks+=1

print(f'PASS: {checks} supplementary checks; analytic proof is in RESULT.md')
