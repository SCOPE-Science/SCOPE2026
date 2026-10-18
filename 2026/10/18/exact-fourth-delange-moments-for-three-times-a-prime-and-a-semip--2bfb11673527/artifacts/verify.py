#!/usr/bin/env python3
"""Independent exact checks for finite-modulus totative-discrepancy identities.
All arithmetic is integer or rational. This finite program is supplementary to
and does not replace the polynomial-degree argument in the proof.
"""
from fractions import Fraction
from math import gcd

def numerator_for_two_exclusions(p):
    """Grid fourth-moment numerator for excluding multiples of 3 and p.
    Works for arbitrary p>=1, including interpolation nodes that are not prime.
    """
    n=3*p
    delta=2*(p-1)
    c=0
    accum=0
    for j in range(n):
        E=n*c-delta*j
        accum+=E**5-(E-delta)**5
        if (j+1)%3 and (j+1)%p:
            c+=1
    assert c==delta
    return accum

def poly_pred(p):
    if p%3==1:
        f=(p-1)*(13*p*p-8*p-14)
    elif p%3==2:
        f=13*p**3-31*p*p+14*p+14
    else:
        raise ValueError('p multiple 3')
    return 24*(p-1)*p*p*f

def h4_from_grid(n):
    phi=sum(gcd(i,n)==1 for i in range(1,n+1))
    c=0
    N=0
    for j in range(n):
        E=n*c-phi*j
        N+=E**5-(E-phi)**5
        if gcd(j+1,n)==1:c+=1
    return Fraction(N,5*phi*n**5)

def exact_formula(p):
    q=3
    if p%3==1:
        f=(p-1)*(13*p*p-8*p-14)
    else:
        f=13*p**3-31*p*p+14*p+14
    return Fraction(4*f,405*p**3)

def isprime(n):
    return n>=2 and all(n%d for d in range(2,int(n**0.5)+1))

# Polynomial interpolation certificate: for each residue, grid numerator
# has degree <= 6 in m, so seven exact points uniquely identify it.
for residue in (1,2):
    for m in range(7):
        p=3*m+residue
        assert numerator_for_two_exclusions(p)==poly_pred(p), (p,m)
print('POLYNOMIAL_CERTIFICATE_OK nodes=14 degree_bound=6')

# Direct totative counts using gcd, independent of two-exclusion formula.
checks=0
for p in range(5,700):
    if isprime(p):
        assert h4_from_grid(3*p)==exact_formula(p),p
        checks+=1
print('DIRECT_PRIME_CHECKS_OK primes=',checks)

# Exact characteristic moments of H_q(U), U continuous uniform, J discrete.
# These identities are proven in the accompanying text by elementary moments.
for q in (2,3,5,7,11):
    mean=Fraction(0)
    moments={}
    for d in (1,2,3,4):
        moments[d]=sum(Fraction((q-1-u)**(d+1)-(-u)**(d+1),q**(d+1)*(q-1)*(d+1)) for u in range(q))
    assert moments[1]==0 and moments[3]==0
    assert moments[2]==Fraction(q-1,6*q)
    assert moments[4]==Fraction((q-1)*(2*q*q-2*q-1),30*q**3)
print('CONTINUOUS_MOMENT_FORMULAS_OK')
print('VERIFY_OK')
