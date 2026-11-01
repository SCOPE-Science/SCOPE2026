"""Reproducible finite checks for fractal Bergman localization constants.
The proof is analytical; these checks are not an infinite-dimensional certificate.
Run: python check.py
"""
from fractions import Fraction
from math import sqrt, isfinite

def D(m):
    a=[0]
    for j in range(m):
        a += [v+2*3**j for v in a[:]]
    return sorted(a)

def cantor_left(n):
    a=[0]
    for j in range(1,n+1):
        a += [v+2*3**(n-j) for v in a[:]]
    return sorted(a) # integers with interval denominator 3**n

def exact_b1_eigen(n,k):
    # Use t=3**(n/2)*[q/3**n,(q+1)/3**n].
    # For even n, rational intervals permit exact verification.
    assert n%2==0
    m=n//2
    R=Fraction(3**m)
    den=3**n
    total=Fraction(0)
    for q in cantor_left(n):
        lo=R*q/den; hi=R*(q+1)/den
        total += (hi/(1+hi))**(k+1)-(lo/(1+lo))**(k+1)
    return total

def decomposed_even(n,k):
    assert n%2==0
    m=n//2
    den=3**m
    total=Fraction(0)
    for a in D(m):
        for q in cantor_left(m):
            lo=Fraction(a)+Fraction(q,den)
            hi=lo+Fraction(1,den)
            total += (hi/(1+hi))**(k+1)-(lo/(1+lo))**(k+1)
    return total

def direct_float(n,k):
    R=3**(n/2)
    den=3**n
    s=0.
    for q in cantor_left(n):
        lo=R*q/den;hi=R*(q+1)/den
        s+=(hi/(1+hi))**(k+1)-(lo/(1+lo))**(k+1)
    return s

def numeric_decomposed_odd(m,k):
    # Actual identity: 3**((2m+1)/2) C_{2m+1} = sqrt(3)(D_m+C_{m+1}).
    s=0.
    h=3**(-m-1)
    for a in D(m):
        for q in cantor_left(m+1):
            lo=sqrt(3)*(a+q*h)
            hi=lo+sqrt(3)*h
            s+=(hi/(1+hi))**(k+1)-(lo/(1+lo))**(k+1)
    return s

checks=0
for m in range(0,5):
    for k in range(0,6):
        assert exact_b1_eigen(2*m,k)==decomposed_even(2*m,k)
        checks+=1
for m in range(0,5):
    for k in range(0,6):
        x=direct_float(2*m+1,k)
        y=numeric_decomposed_odd(m,k)
        assert abs(x-y)<5e-11
        checks+=1
for k in range(0,7):
    # n=0 is the hyperbolic disk t in [0,1].
    assert exact_b1_eigen(0,k)==Fraction(1,2**(k+1))
    checks+=1
for k in (0,1,2,3,5,10):
    ev=[(3/2)**m*direct_float(2*m,k) for m in range(4,9)]
    od=[(3/2)**(m+.5)*direct_float(2*m+1,k) for m in range(4,8)]
    assert all(isfinite(x) and x>0 for x in ev+od)
    assert abs(ev[-1]-ev[-2])<.004
    assert abs(od[-1]-od[-2])<.004
    checks+=4
print('PASS',checks,'finite identities and numerical convergence checks')
print('flat Bergman example: n=16 renormalized k=0 eigenvalue',format((3/2)**8*direct_float(16,0),'.9f'))
