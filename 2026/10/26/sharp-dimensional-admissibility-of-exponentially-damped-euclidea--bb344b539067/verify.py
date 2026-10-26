"""Reproducible checks for the exponentially damped Euclidean wave kernel.

The algebraic and numerical checks supplement the analytic sign proof.
Run with Python 3 and SymPy installed: python verify.py
"""
from math import atan, pi
import sympy as sp

x, a, w = sp.symbols('x a w', positive=True, real=True)
Q = (x + a*a + w*w)**2 - 4*x*w*w
F3 = 8*sp.pi*a/Q

# Independently differentiate the rational three-dimensional density.
F5 = sp.factor(-4*sp.pi*sp.diff(F3, x))
assert sp.simplify(F5 - 64*sp.pi**2*a*(x+a*a-w*w)/Q**2) == 0
F7 = sp.factor((-4*sp.pi)**2*sp.diff(F3, x, 2))
F7_at_zero = sp.factor(F7.subs(x, 0))
assert sp.simplify(F7_at_zero - 256*sp.pi**3*a*(3*a*a-w*w)*(a*a-3*w*w)/(a*a+w*w)**6) == 0

# Compare the dimension-walk transform with the complex-power formula
# for several dimensions and numerical parameter sets.
for m in range(5):
    derivative = sp.lambdify((x,a,w), sp.factor((-4*sp.pi)**m*sp.diff(F3,x,m)), 'mpmath')
    # Direct numeric complex-power implementation, with Im taken correctly.
    for aa, ww, s2 in [(1.,0.25,0.),(1.,1.,0.5),(1.25,2.,3.)]:
        z = complex(s2+aa*aa-ww*ww,-2*aa*ww)
        expected = float((4*sp.pi)**(m+1)*sp.factorial(m)/ww) * (z**(-m-1)).imag
        actual = float(derivative(s2,aa,ww))
        assert abs(actual-expected) <= 2e-8*max(1.,abs(actual),abs(expected)), (m,aa,ww,s2,actual,expected)

# The sign criterion follows from the exact phase representation.
for d in (3,5,7,9,11):
    p=(d-1)//2
    for ratio in (0.1,0.25,0.5,1.,2.,4.):
        predicted=2*p*atan(ratio)<=pi
        samples=[]
        deriv=sp.lambdify((x,a,w), sp.factor((-4*sp.pi)**(p-1)*sp.diff(F3,x,p-1)), 'math')
        for s2 in (0.,0.001,0.1,1.,5.,20.,100.):
            samples.append(float(deriv(s2,1.,ratio)))
        if predicted:
            assert min(samples)>-1e-7
print('PASS: exact low-dimensional identities, complex representation, sampled signs')
