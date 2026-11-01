#!/usr/bin/env python3
"""Independent reproducibility checks for the rectangular Fock cubic cumulant.

Run: python3 CHECK.py (requires the SymPy package).
This is a finite algebraic check supporting, not replacing, the proof.
"""
from math import pi, sqrt, log, isclose
from sympy import Matrix, Rational, I, simplify, eye

h = Rational(1, 2)
M = Matrix([[1, -h, 0, I*h], [-h, 1, -I*h, 0],
            [0, -I*h, 1, -h], [I*h, 0, -h, 1]])
assert M.det() == 1
C = M.inv()/2
assert (M*C - eye(4)/2) == Matrix.zeros(4,4)
X = Matrix([[1,0,0,0],[0,1,0,0],[1,-1,0,0]])
Y = Matrix([[0,0,1,0],[0,0,0,1],[0,0,1,-1]])
assert X*C*X.T == Matrix([[h, Rational(1,4), Rational(1,4)],
                          [Rational(1,4),h,-Rational(1,4)],
                          [Rational(1,4),-Rational(1,4),h]])
assert Y*C*Y.T == X*C*X.T
rho = 2*X*C*Y.T
assert sum(x == 0 for x in rho) == 3
assert sum(x in (I*h,-I*h) for x in rho) == 6
phi = (1+sqrt(5))/2
E_mixed = (3/(4*pi))*(1+sqrt(5)-log(phi))
tr3_const = E_mixed/pi
tr2_const = 1/pi**2
cumulant = -3*tr2_const + 2*tr3_const
formula = 3/(2*pi**2)*(sqrt(5)-1-log(phi))
assert isclose(cumulant, formula, rel_tol=1e-13, abs_tol=1e-13)
assert cumulant > 0
assert isclose(formula, 0.11472437826741094, rel_tol=1e-13)
print('PASS: covariance matrix, 9 correlations, cancellation, positive exact constant')
print('C3 limiting value:',format(formula,'.17g'))
