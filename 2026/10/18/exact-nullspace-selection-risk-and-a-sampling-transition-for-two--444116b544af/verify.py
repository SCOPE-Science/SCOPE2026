"""Reproduce exact finite-dimensional calculations for a rank-one two-coordinate RBCD law.

Requires Python 3 and SymPy. Analytic convergence and uniqueness arguments
are in RESULT.md; finite experiments here are not substitutes for them.
"""
from fractions import Fraction
from itertools import product
from math import sqrt
import random
import sympy as sp

p, A, B, h = sp.symbols('p A B h', positive=True, real=True)
s = A+B
d = p*A+(1-p)*B
e = p*A**2+(1-p)*B**2
m = (2*p-1)/d
v = h*p*(1-p)*s**2/(d**2*(2*d-h*e))
Q = sp.factor(m**2+v)
coeff2 = (A-B)*(h*s-2)*(3*h*s-8)
coeff1 = -2*(A-3*B)*(h*B-2)*(h*s-2)
coeff0 = -B*(h*B-2)*(h*(A+3*B)-4)
F = coeff2*p**2+coeff1*p+coeff0
assert sp.simplify(sp.diff(Q,p)-s*F/(d**2*(h*e-2*d)**2)) == 0
assert sp.simplify(sp.diff(Q,p).subs(p,1)-s*(h*(3*A+B)-4)/(A**3*(A*h-2))) == 0
assert sp.simplify(Q.subs(h,2/s) - (A-(A-B)*p)/(A*B*(B+(A-B)*p))) == 0

# Independently derive both moments from the affine distributional fixed point.
C = p*(1-h*A)+(1-p)*(1-h*B)
assert sp.simplify(m-h*(2*p-1)/(1-C)) == 0
constant = h**2+2*h*m*(p*(1-h*A)-(1-p)*(1-h*B))
second = sp.factor(constant/(1-(p*(1-h*A)**2+(1-p)*(1-h*B)**2)))
assert sp.simplify(second-Q) == 0

# In the exact 2:1 column example, the unique interior optimizer is algebraic.
q_example = sp.factor(Q.subs({A:4,B:1,h:sp.Rational(1,5)}))
assert sp.simplify(q_example-(20*p**2-23*p+9)/(3*(3*p+1)*(5*p+3))) == 0
p_star = (3+2*sp.sqrt(51))/25
assert 0 < p_star < 1
assert sp.simplify(sp.diff(q_example,p).subs(p,p_star)) == 0
assert sp.simplify(q_example.subs(p,p_star)-(-sp.Rational(89,6)+25*sp.sqrt(51)/12)) == 0
assert q_example.subs(p,sp.Rational(1,2)) == sp.Rational(2,33)
assert q_example.subs(p,0) == 1
assert q_example.subs(p,1) == sp.Rational(1,16)

# Independently enumerate finite prefixes of the exact binary-digit example.
# At depth n, the mean squared error of (x1,x2) from (1/2,1/2) is
# 1/6 + (1/3)*4**(-n), so the infinite-step risk is exactly 1/6.
for n in range(1,11):
    moment = Fraction(0)
    for digits in product((0,1), repeat=n):
        x1 = sum(Fraction(bit,2**(k+1)) for k,bit in enumerate(digits))
        x2 = Fraction(1)-Fraction(1,2**n)-x1
        assert x1>=0 and x2>=0 and x1+x2<=1
        moment += (x1-Fraction(1,2))**2 + (x2-Fraction(1,2))**2
    moment /= 2**n
    asserted = Fraction(1,6)+Fraction(1,3*4**n)
    assert moment == asserted,(n,moment,asserted)

# Direct iteration agrees with the exact residual-product expansion.
rng = random.Random(20241015)
for case in range(160):
    aa=1.0+4*rng.random()
    bb=0.1+0.85*aa*rng.random()
    step=(2.0/(aa*aa+bb*bb))*(0.1+0.85*rng.random())
    yy=-2+4*rng.random()
    x1=x2=0.0
    residual=yy
    expansion=0.0
    product_residual=1.0
    for _ in range(30):
        select1=rng.random()<rng.random()
        sig=1 if select1 else -1
        expansion+=step*sig*product_residual
        if select1:x1+=step*aa*residual
        else:x2+=step*bb*residual
        residual=yy-aa*x1-bb*x2
        product_residual*=1-step*(aa*aa if select1 else bb*bb)
        assert abs(residual-yy*product_residual)<2e-12
        assert abs((bb*x1-aa*x2)-aa*bb*yy*expansion)<2e-11

print('PASS symbolic identities, exact finite-digit enumeration, and 4,800 direct updates')
