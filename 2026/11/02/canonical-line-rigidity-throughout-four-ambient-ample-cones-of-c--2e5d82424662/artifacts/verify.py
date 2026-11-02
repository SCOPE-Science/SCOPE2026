#!/usr/bin/env python3
"""Exact verification of four polarized Hilbert-polynomial identities.

Requires sympy. No network, external input or numerical approximations.
"""
import sympy as s
A,B,T,U,j=s.symbols('A B T U j')

def choose_poly(z,m):
    return s.prod(z-i for i in range(m))/s.factorial(m)

def count_direct(k,n,r):
    c=5-k
    assert n>=r>=0
    return s.binomial(n+5,5)-sum(s.binomial(v+c-1,c-1)*s.binomial(n-v+k,k) for v in range(r))

expected_A=[
    (3*A**4-2*B**4)/12,
    (A**4-2*A*B**3+B**4)/4,
    (A*A-B*B)**2/4,
    (A-B)**3*(3*A+7*B)/12,
]
expected_B=[
    (45*A**2-10*B**2)/12,
    (15*A*A-2*A*B-5*B*B)/4,
    (15*A*A-6*A*B-5*B*B)/4,
    5*(A-B)*(9*A+B)/12,
]
expected_disc=[
    (1129*B**4+5148*B**3*U+9522*B**2*U**2+6948*B*U**3+1737*U**4)/144,
    (64*B**4+384*B**3*U+832*B**2*U**2+712*B*U**3+193*U**4)/16,
    (16*B**4+192*B**3*U+568*B**2*U**2+592*B*U**3+193*U**4)/16,
    U**2*(2500*B**2+3540*B*U+1737*U**2)/144,
]
for k in range(4):
    c=5-k
    summand=s.expand(choose_poly(j+c-1,c-1)*choose_poly(A-j+k,k))
    C=s.expand(choose_poly(A+5,5)-s.summation(summand,(j,0,B-1)))
    poly=s.expand(C.subs({A:T*A,B:T*B},simultaneous=True)
                  -C.subs({A:T*A-6,B:T*B-(c-1)},simultaneous=True))
    P=s.Poly(poly,T)
    assert s.expand(poly-(expected_A[k]*T**4+expected_B[k]*T**2+2))==0
    assert s.expand((expected_B[k]**2-8*expected_A[k]).subs(A,B+U)-expected_disc[k])==0
    for coeff in (s.Poly(s.expand(expected_A[k].subs(A,B+U)),B,U),
                  s.Poly(s.expand(expected_B[k].subs(A,B+U)),B,U),
                  s.Poly(s.expand(expected_disc[k]),B,U)):
        assert coeff.terms() and all(v>0 for _,v in coeff.terms())
    for n,r in ((8,2),(10,3),(12,4)):
        assert C.subs({A:n,B:r}) == count_direct(k,n,r)
    # Independent exact evaluation of hypersurface Euler difference at large twist.
    for t,a,b in ((7,2,1),(9,3,1)):
        s1,r1=t*a,t*b
        s2,r2=s1-6,r1-(c-1)
        assert s1>=r1>=0 and s2>=r2>=0
        brute=count_direct(k,s1,r1)-count_direct(k,s2,r2)
        assert s.expand(poly.subs({A:a,B:b,T:t})-brute)==0
print('VERIFY_OK: 4 symbolic families; positive-coefficient certificates; monomial counts')
