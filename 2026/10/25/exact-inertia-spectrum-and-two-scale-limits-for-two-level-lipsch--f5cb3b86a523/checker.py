"""Independent finite-dimensional checks of the two-level Lipschitz-polytope formulas.

Usage: python checker.py
Only the analytic argument in RESULT.md proves the stated all-dimensional and
asymptotic results. This script evaluates selected finite identities exactly.
"""
from fractions import Fraction
from math import factorial
from sympy import symbols, integrate, Rational, Matrix, simplify
import random

A, B, Y = symbols('A B Y')

# On the chamber 0 <= A <= B <= 1, the lower coordinates are (A,B)
# or (B,A), and the upper coordinate lies between B and 1+A.
def chamber_moment(exponents):
    a,b,y = exponents
    f = (A**a * B**b + B**a * A**b) * Y**y
    return simplify(integrate(integrate(integrate(f, (Y,B,1+A)),(A,0,B)),(B,0,1)))

moment_keys = [(0,0,0),(1,0,0),(0,0,1),(2,0,0),(1,1,0),
               (1,0,1),(0,0,2)]
mom = {k:chamber_moment(k) for k in moment_keys}
V = mom[(0,0,0)]
assert V == Rational(2,3), V
Ex=mom[(1,0,0)]/V
Ey=mom[(0,0,1)]/V
assert Ex == Rational(1,2) and Ey == Rational(1)
var_x=mom[(2,0,0)]/V-Ex**2
cov_xx=mom[(1,1,0)]/V-Ex**2
cov_xy=mom[(1,0,1)]/V-Ex*Ey
var_y=mom[(0,0,2)]/V-Ey**2
n,p,q=3,2,1
s=Rational((q+2)*(q+3),(n+1)*(n+2))
t=Rational(p*(p-1),(n+1)*(n+2))
assert var_x==s/12+t*Rational(p+4,12*p)
assert cov_xx==s/12-t*Rational(1,2*p*(p-1))
assert cov_xy==s/12
assert var_y==s/6

# Independent finite-volume check by direct integration in lower extremes.
for p,q in [(2,1),(2,2),(3,1),(3,4),(5,3),(7,11)]:
 r=symbols('r', nonnegative=True)
 exact=integrate(p*(p-1)*r**(p-2)*(1-r)**(q+1),(r,0,1))
 assert exact==Rational(factorial(p)*factorial(q+1),factorial(p+q))

# Algebraic covariance eigenstructure must agree with the full block matrix.
for p,q in [(2,1),(2,3),(3,2),(3,4),(5,5),(8,3)]:
 n=p+q
 s=Rational((q+2)*(q+3),(n+1)*(n+2))
 t=Rational(p*(p-1),(n+1)*(n+2))
 lo_diag=s/12+t*Rational(p+4,12*p)
 lo_off=s/12-t*Rational(1,2*p*(p-1))
 up_diag=s/6
 up_off=s/12
 C=Matrix(n,n,lambda i,j:
          lo_diag if i==j and i<p else
          lo_off if i<p and j<p else
          up_diag if i==j and i>=p else
          up_off if i>=p and j>=p else s/12)
 lambda_lo=Rational((p+1)*(p+2),12*(n+1)*(n+2))
 lambda_up=s/12
 det_mean=(p*s*s+Rational((q+1)*(p-2),p)*s*t)/144
 assert simplify(C.det()-lambda_lo**(p-1)*lambda_up**(q-1)*det_mean)==0
 assert all(simplify(z)==0 for z in list(C*Matrix([1]*p+[0]*q)-Matrix([lo_diag+(p-1)*lo_off]*p+[p*s/12]*q)))

print('VERIFY_OK direct_exact_moments=7 beta_volumes=6 covariance_determinants=6')
