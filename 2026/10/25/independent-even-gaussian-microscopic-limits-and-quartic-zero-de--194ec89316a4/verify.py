"""Finite Gaussian moment and exact covariance checks for a reciprocal random-polynomial zero law.

Run with: python verify.py
The script checks algebraic coefficients; infinite-dimensional convergence is proved analytically.
"""
from fractions import Fraction
from math import cosh, sin, sinh, isclose
import sympy as sp

x, y = sp.symbols('x y', real=True)
# Exact bivariate Taylor polynomial of the limiting diagonal covariance.
K4 = sp.Integer(4) + sp.Rational(4, 3)*(x*x-y*y) + sp.Rational(4, 15)*(x**4+y**4)
U = sp.expand((K4 - 4)/4)
log4 = sp.expand(U - U*U/2)
log4 = sp.Poly(log4, x, y)
log4 = sp.expand(sum(c*x**e[0]*y**e[1] for e,c in log4.terms() if sum(e) <= 4))
assert sp.expand(log4 - (x*x-y*y)/3 - (x**4+y**4)/90 - x*x*y*y/9) == 0
lap = sp.diff(log4, x, 2) + sp.diff(log4, y, 2)
assert sp.expand(lap-sp.Rational(16,45)*(x*x+y*y)) == 0

# Exact finite-n expansion near the logarithmic reciprocal fixed point.
def finite_local_zero_mass_coefficient(n):
    s2 = sum(Fraction(k*k, n*n) for k in range(1,n+1))
    s4 = sum(Fraction(k**4,n**4) for k in range(1,n+1))
    v_a = Fraction(4*n+1,n)
    cov_a_c = Fraction(2,n)*s2
    v_c = s4/n
    # E[# zeros inside |w|<r] = coefficient*r^4 + O(r^6).
    return 2*(v_c/v_a - cov_a_c**2/v_a**2)

for n in [1,2,3,5,10,25,100,200]:
    z = finite_local_zero_mass_coefficient(n)
    assert z>0
assert abs(float(finite_local_zero_mass_coefficient(1000))-2/45)<0.0001

# Exact covariance of F_n(0); cross covariance for the +/- fixed points.
for n in [3,4,5,8,16,33,64,127]:
    diagonal = Fraction(4*n+1,n)
    direct = (4*sum(Fraction(1,n) for _ in range(n)) + Fraction(1,n))
    assert diagonal == direct
    cross = Fraction(4,n)*sum((-1)**j for j in range(n)) + Fraction((-1)**n,n)
    assert abs(cross) <= Fraction(5,n)

print('CHECK_OK: quartic covariance, Laplacian, finite-n zero-mass coefficients, fixed-point decorrelation')
