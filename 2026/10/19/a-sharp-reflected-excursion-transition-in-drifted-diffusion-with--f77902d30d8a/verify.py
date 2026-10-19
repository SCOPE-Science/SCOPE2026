"""Exact checks for stationary drift-diffusion with sign-reversing proportional resets."""
from fractions import Fraction as Q
from math import comb, factorial
import sympy as S

passed = 0
z = S.Symbol('z')
rate_plus, rate_minus = S.Integer(1), S.Integer(3)
h = lambda x: S.Rational(3,1) / ((1-x)*(3+x))
for b0 in (Q(1, 4), Q(1, 3), Q(1, 2), Q(4, 5)):
    b = S.Rational(b0.numerator, b0.denominator)
    # Cumulants from the absolutely convergent independent innovation expansion.
    cumulants = {k: Q(factorial(k-1),1) * (1+Q((-1)**k, 3**k)) / (1-(-b0)**k)
                 for k in range(1, 13)}
    moments = {0:Q(1)}
    for n in range(1, 13):
        moments[n] = sum(Q(comb(n-1,k-1))*cumulants[k]*moments[n-k]
                         for k in range(1,n+1))
        # Stationarity identity for mu=2, D=1, r=3, a=-b.
        assert 3*(1-(-b0)**n)*moments[n] == 2*n*moments[n-1] + n*(n-1)*moments.get(n-2,0)
        passed += 1
    for N in (2,3,4,5):
        f = S.cancel(S.prod(h((-b)**j*z) for j in range(N+1)))
        right_coefficient = S.limit((1-z)*f,z,1)
        expect_right = S.prod(h((-b)**j) for j in range(1,N+1))*S.Rational(3,4)
        assert S.simplify(right_coefficient-expect_right)==0
        passed += 1
        if b<S.Rational(1,3):
            k,m = S.Integer(3),1
            independent_coeff = S.Rational(3,4)*S.prod(h(-3*(-b)**j) for j in range(1,N+1))
        elif b>S.Rational(1,3):
            k,m = S.Rational(1,1)/b,1
            independent_coeff = k*S.Rational(3,4)*S.prod(h(-k*(-b)**j) for j in range(0,N+1) if j!=1)
        else:
            k,m = S.Integer(3),2
            independent_coeff = S.Integer(9)*S.Rational(1,4)*S.Rational(3,4)*S.prod(h(-3*(-b)**j) for j in range(2,N+1))
        pole_coeff=S.limit((z+k)**m*f,z,-k)
        assert S.simplify(pole_coeff-independent_coeff)==0
        assert pole_coeff>0
        passed+=2
print('Exact rational stationary-moment and tail-pole assertions passed:',passed)
