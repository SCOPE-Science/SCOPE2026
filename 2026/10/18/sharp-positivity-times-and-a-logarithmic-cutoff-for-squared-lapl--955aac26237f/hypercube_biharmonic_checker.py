"""Independent finite checks for the squared-hypercube-Laplacian kernel.

Run with Python >=3.11: python hypercube_biharmonic_checker.py
Finite tests support, but do not replace, the proof of the all-dimension theorem.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import product
from math import comb


def coefficient(d, k, j):
    return sum((-1)**a * comb(k, a) * comb(d-k, j-a)
               for a in range(max(0, j-(d-k)), min(k, j)+1))


def kernel_poly(d, k, z):
    return sum(Decimal(coefficient(d,k,j)) * (z ** (j*j))
               for j in range(d+1)) / (2**d)


def corner_poly(d,z):
    return sum(Decimal((-1)**j * comb(d,j)) * (z ** (j*j))
               for j in range(d+1))


def threshold(d):
    # Root with 1/d < z_d < 1/d+1/d^2, rather than the root z=1 at t=0.
    low=Decimal(1)/d
    high=low+Decimal(1)/(d*d)
    assert corner_poly(d, low)>0
    assert corner_poly(d, high)<0
    for _ in range(300):
        mid=(low+high)/2
        if corner_poly(d,mid)>0: low=mid
        else: high=mid
    z=(low+high)/2
    return -z.ln()/4,z


def spectral_rational(d,k,base):
    return sum(Fraction(coefficient(d,k,j),base**(j*j)) for j in range(d+1))/2**d


def direct_rational(d,k,base):
    # Trace every Fourier character on the hypercube, without Krawtchouk grouping.
    y=(1<<k)-1
    acc=Fraction(0)
    for s in range(1<<d):
        j=s.bit_count()
        acc+=(-1 if ((s&y).bit_count()%2) else 1)*Fraction(1,base**(j*j))
    return acc/(1<<d)


def main():
    tests=0
    for d in range(2,8):
        for base in range(max(d,2),max(d,2)+3):
            for k in range(d+1):
                assert spectral_rational(d,k,base)==direct_rational(d,k,base)
                tests+=1
    with localcontext() as ctx:
        ctx.prec=75
        previous=Decimal(0)
        for d in range(2,41):
            t,z=threshold(d)
            assert t>previous
            assert t<Decimal(d).ln()/4
            assert abs(corner_poly(d,z))<Decimal('1e-60')
            for k in range(d):
                assert kernel_poly(d,k,z)>kernel_poly(d,k+1,z)
                assert kernel_poly(d,k,z)>0
                tests+=2
            lower_z=z+Decimal(1)/(d*d*d*d)
            upper_z=z-Decimal(1)/(d*d*d*d)
            if upper_z>0:
                assert corner_poly(d,lower_z)<0
                assert corner_poly(d,upper_z)>0
                tests+=2
            previous=t
            tests+=3
        for d in (40,60,100,160):
            t,z=threshold(d)
            approx=Decimal(d).ln()/4-Decimal(1)/(8*d*d)+Decimal(1)/(8*d*d*d)
            err=abs(t-approx)
            assert err*d**4 < Decimal('0.5'),(d,err*d**4)
            tests+=1
    print(f'PASS: {tests} independent finite checks; no claim of exhaustive infinite verification.')
    for d in (2,3,4,8,16,40,100):
        with localcontext() as ctx:
            ctx.prec=55
            t,z=threshold(d)
            print(f'd={d:3d} threshold={t:.16f}, 4t-log(d)={4*t-Decimal(d).ln():.12f}')

if __name__=='__main__':
    main()
