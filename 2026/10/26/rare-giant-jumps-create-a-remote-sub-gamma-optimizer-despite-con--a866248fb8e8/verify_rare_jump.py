"""Exact moments and numerical witnesses for rare two-point compound-Poisson jumps.

Numerical tests do not replace the uniform asymptotic and phase-transition proofs.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from math import factorial
getcontext().prec = 65
D = Decimal

def psi(b, q, t):
    b = D(b); q = D(q); t = D(t)
    a = 1 - q + q*b*b
    # Finite t inputs are chosen so cancellation is smaller than 65 digit precision.
    m = 2*((1-q)*(t.exp()-1-t) + q*((b*t).exp()-1-b*t))/(a*t*t)
    return (1-1/m)/t

def at_zero(b, q):
    b=Fraction(b); q=Fraction(q)
    a=1-q+q*b*b
    mom3=1-q+q*b**3
    mom4=1-q+q*b**4
    return (mom3/(3*a), (3*a*mom4-4*mom3**2)/(36*a*a))

# Beta(1,2) has nth moment 2/((n+1)(n+2)); this reconstructs its MGF.
for n in range(101):
    assert Fraction(2, (n+1)*(n+2)*factorial(n)) == Fraction(2, factorial(n+2))
    if n>=2:
        assert Fraction(2, factorial(n+2)) < Fraction(1, 3**n)

# Genuine global witnesses and negative slope for kappa=5.
for b in [100, 1000, 10000, 100000]:
    q=Fraction(1,b**5)
    v,slope=at_zero(b,q)
    assert slope<0
    t=D('3.5')*D(b).ln()/D(b)
    y=psi(b, D(1)/D(b)**5,t)
    assert y > D(v.numerator)/D(v.denominator), (b,y,v)
    print('b=',b,'origin=',float(v),'slope=',float(slope),'remote_witness=',float(y),'normalized=',float(y*D(b).ln()/D(b)))

# Arbitrary finite-order convergence: all m < kappa.
for k in [5,8,12]:
    for m in range(2,k):
        b=10**4
        q=Fraction(1,b**k)
        cumulant_per_intensity=1-q+q*b**m
        assert abs(cumulant_per_intensity-1) <= Fraction(1,b**(k-m))
print('PASS: 101 Beta coefficients, four remote witnesses, negative slopes, cumulant identities')
