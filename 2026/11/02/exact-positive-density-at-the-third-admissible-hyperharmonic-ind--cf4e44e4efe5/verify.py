#!/usr/bin/env python3
"""Exact integer-arithmetic certificate for the 45th hyperharmonic index.

No dependencies outside the Python standard library.  All congruences are exact.
"""
from fractions import Fraction
from math import factorial, prod

PRIMES = (2,3,5,7,11,13,17,19,23,29,31,37,41,43)
PERIODS = (256,243,125,49,121,169,289,361,23,29,31,37,41,43)
ROOT_COUNTS = (32,18,20,25,41,92,193,145,22,16,14,8,4,2)
FIRST_ROOTS = (0,19,31,0,0,0,0,0,0,0,0,0,0,0)
DENSITY = Fraction(15810560, 1807915433082759)
GLOBAL_PERIOD = 1096405020816651129231648000
EXPLICIT_ORDER = 692567016770669472150374656

def rising_derivative(n, x, modulus):
    """Compute d/dx prod_{j=0}^{n-1}(x+j), modulo modulus."""
    value = 1
    deriv = 0
    for j in range(n):
        z = (x+j) % modulus
        deriv = (deriv*z+value) % modulus
        value = (value*z) % modulus
    return deriv

def independent_rising_derivative(n,x,modulus):
    """Independent prefix/suffix implementation of the integer polynomial."""
    vals = [(x+j) % modulus for j in range(n)]
    prefix = [1]
    for z in vals:
        prefix.append(prefix[-1]*z % modulus)
    suffix=1
    total=0
    for j in range(n-1,-1,-1):
        total=(total + prefix[j]*suffix) % modulus
        suffix=suffix*vals[j] % modulus
    return total

def exponent(n,p):
    k=n; e=0
    while k:
        k//=p; e+=k
    return e

def crt(remainders,moduli):
    modulus=prod(moduli)
    solution=0
    for a, m in zip(remainders,moduli):
        cofactor=modulus//m
        solution=(solution+a*cofactor*pow(cofactor,-1,m))%modulus
    return solution

def main():
    n=45
    assert prod(PERIODS)==GLOBAL_PERIOD
    assert len(PRIMES)==len(PERIODS)==len(ROOT_COUNTS)==len(FIRST_ROOTS)
    numerator=1
    moduli=[]
    roots=[]
    checks=0
    for p,t,count,first in zip(PRIMES,PERIODS,ROOT_COUNTS,FIRST_ROOTS):
        e=exponent(n,p)
        q=p**e
        assert t>0 and q%t==0
        # D(X)=P(X+t)-P(X), degree at most n-2=43.
        # Checking at 44 consecutive integers proves divisibility for
        # every integer X by Newton's integer-valued-polynomial expansion.
        for x in range(n-1):
            assert rising_derivative(n,x+t,q)==rising_derivative(n,x,q)
            checks+=1
        residues=[x for x in range(t) if rising_derivative(n,x,q)==0]
        assert len(residues)==count and residues[0]==first
        assert all(rising_derivative(n,x,q)==independent_rising_derivative(n,x,q)
                   for x in range(t))
        numerator*=count
        moduli.append(t); roots.append(first)
        print('p=%2d, exponent=%2d, polynomial period=%3d, local roots=%3d, first=%3d' % (p,e,t,count,first))
    assert Fraction(numerator,GLOBAL_PERIOD)==DENSITY
    assert numerator==9588267818680320000
    chosen=crt(roots,moduli)
    assert chosen==EXPLICIT_ORDER
    assert rising_derivative(n,chosen,factorial(n))==0
    assert independent_rising_derivative(n,chosen,factorial(n))==0
    # The lower index 35 cannot give hyperharmonic integers: 7-adic
    # polynomial residues exhibit an exhaustive root-free period.
    n35=35; q35=7**exponent(n35,7)
    assert exponent(n35,7)==5
    assert all(rising_derivative(n35,x+49,q35)==rising_derivative(n35,x,q35)
               for x in range(n35-1))
    assert all(rising_derivative(n35,x,q35)!=0 for x in range(49))
    # A second direct formula at the positive CRT witness is a genuinely
    # exact check; the integer has more than a thousand decimal digits.
    val=1; df=0
    for j in range(45):
        df=df*(chosen+j)+val
        val*=chosen+j
    assert df%factorial(45)==0
    print('VERIFY_OK: 14 exact prime-power periods, %d shift certificates, %d local residues, 45th-index CRT witness, 35th-index obstruction; density=%s' % (checks, sum(PERIODS),DENSITY))

if __name__=='__main__':
    main()
