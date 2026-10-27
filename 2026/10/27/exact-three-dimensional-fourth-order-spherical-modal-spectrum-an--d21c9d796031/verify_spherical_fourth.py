"""Supplemental tests for 3D spherical Fourier fourth-modal moments.

Run with Python 3, sympy, scipy, numpy. All theorems require the analytic
proof supplied separately; finite numerical checks are not universal proofs.
"""
from fractions import Fraction
import math
import sympy as sp
import numpy as np
from scipy.special import eval_legendre, roots_legendre, jv
from scipy.integrate import quad

x=sp.symbols('x')
expected={0:sp.Rational(1),1:sp.Rational(7,15),2:sp.Rational(11,35),
          3:sp.Rational(3607,15015),4:sp.Rational(30001,153153)}
values=[]
for k in range(10):
    P=sp.legendre(k,1-2*x*x)
    Q=sp.integrate(sp.expand(P*P),(x,0,1))
    assert Q.is_Rational and Q>0
    if k in expected:assert Q==expected[k]
    values.append(Q)
# Transform test: numerical fourth Bessel moment should converge to Q/pi.
# Truncation is controlled by the J_{k+1/2}(r)=O(r^-1/2) tail.
for k in range(3):
    integral=quad(lambda r:jv(k+0.5,r)**4,0,2000,epsabs=2e-8,limit=1000)[0]
    assert abs(integral-float(values[k])/math.pi)<0.0002,(k,integral)
# Two-term angular-mode tail, using polynomial-exact degree >=2k quadrature.
C=0.5772156649015328606+math.log(32)
errors=[]
for k in (20,40,80,160,320,640):
    nodes,weights=roots_legendre(2*k+20)
    nodes=(nodes+1)/2;weights=weights/2
    Q=float(np.dot(weights,eval_legendre(k,1-2*nodes*nodes)**2))
    K=k+0.5
    discrepancy=abs((2*math.pi*K*Q-math.log(K))-C)
    errors.append(discrepancy)
assert errors[-1]<1.1e-6 and all(a>b for a,b in zip(errors,errors[1:])),errors
Gamma=8*math.pi**2.5*(1-math.sqrt(7/15))
assert Gamma>0
print('VERIFY_OK 10 exact modal rationals; 3 Bessel integrals; '
      '6 two-term asymptotic quadratures; sharp stability coefficient', Gamma)
