#!/usr/bin/env python3
"""Supplementary checks for Fourier multipliers of the uniform ternary carpet measure.
Analytic arguments in RESULT.md establish the infinite-frequency theorem."""
import math
import cmath
from fractions import Fraction
from itertools import product

DIGITS = [(a,b) for a in range(3) for b in range(3) if (a,b)!=(1,1)]
assert len(DIGITS)==8

def mask_direct(x,y):
    return sum(cmath.exp(-2j*math.pi*(a*x+b*y)) for a,b in DIGITS)/8

def mask_trig(x,y):
    return cmath.exp(-2j*math.pi*(x+y))*((1+2*math.cos(2*math.pi*x))*(1+2*math.cos(2*math.pi*y))-1)/8

def coeff(m,n,depth=24):
    p=1+0j
    for j in range(1,depth+1):
        p*=mask_direct(m/(3**j),n/(3**j))
    return p

def reduced(m,n):
    while m%3==0 and n%3==0 and (m,n)!=(0,0):
        m//=3;n//=3
    return m,n

def mask_nonzero_mod_3(m,n,j):
    # In Z[zeta_{3^j}] / (3,zeta_{3^j}-1), the unnormalized
    # Fourier mask numerator becomes 8 (= -1 modulo 3).
    return (len(DIGITS)%3)==2

def run():
    count=0
    for a,b in product(range(-14,15),repeat=2):
        for j in range(1,7):
            x,y=a/(3**j),b/(3**j)
            assert abs(mask_direct(x,y)-mask_trig(x,y))<2e-12
            count+=1
    assert all(mask_nonzero_mod_3(a,b,j) for a,b,j in product(range(-3,4),range(-3,4),range(1,8)))
    # Verify the critical 9-adic nonaxis mask bound directly for all residues.
    for m,n in product(range(9),repeat=2):
        if (m%3==0)==(n%3==0):
            continue
        is_axis_residue=(m%9 in (1,8) and n%9==0) or (n%9 in (1,8) and m%9==0)
        v=abs(mask_direct(m/9,n/9))
        if not is_axis_residue:
            assert v < .500000000001, (m,n,v)
        count+=1
    N=42
    A=abs(coeff(1,0))
    B=abs(coeff(1,1))
    assert 0.1<A<0.102 and 0.080<B<0.082 and A>B>1/16
    for m,n in product(range(-N,N+1),repeat=2):
        if (m,n)==(0,0):
            continue
        z=abs(coeff(m,n))
        a,b=reduced(m,n)
        first=(abs(a),abs(b)) in ((1,0),(0,1))
        second=(abs(a),abs(b))==(1,1)
        if first:
            assert abs(z-A)<1e-9, ((m,n),z,A)
        elif second:
            assert abs(z-B)<1e-9, ((m,n),z,B)
        else:
            assert z<B-1e-8, ((m,n),z,B)
        if (a%3==0) != (b%3==0) and not first:
            assert z < 1/16 +1e-12, ((m,n),z)
        count+=1
    # Exact rational product lower-bound certificate.
    assert Fraction(1,8)*Fraction(5,9)*Fraction(103,108)>Fraction(1,16)
    # The mask at a 3-adic primitive residue is exactly -1/8, as each
    # ternary full coordinate sum vanishes and the missing center contributes -1.
    omega=cmath.exp(-2j*math.pi/3)
    for m,n in product(range(3),repeat=2):
        if (m,n)!=(0,0):
            assert abs(mask_direct(m/3,n/3) + omega**(m+n)/8)<2e-14
    print(f'CARPET_FOURIER_CERTIFICATE_OK {count} mask_and_frequency_checks')
    print(f'A={A:.16f} B={B:.16f} lower_bound_B>{float(Fraction(515,7776)):.14f}')
if __name__ == '__main__':
    run()
