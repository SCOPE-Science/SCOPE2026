#!/usr/bin/env python3
"""Exact-arithmetic finite consistency checks for a sextic Bergman-kernel identity.

The universal assertions follow from the symbolic identities in RESULT.md,
not from this finite test program.  Requires only Python's standard library.
"""
from fractions import Fraction as F


def source_coefficients(m,n):
    out = [0] * (2*(m-n)+1)
    for j in range(m-1):
        L = (1+n*(j+1)+m-1)//m
        kap = m+n-1+n*j-m*L
        pairs = [((j+1)*(kap+1),j-L+1),
                 ((j+1)*(m-kap-1),j-L+2),
                 ((m-j-1)*(kap+1),j-L+m-n+1),
                 ((m-j-1)*(m-kap-1),j-L+m-n+2)]
        for c,exp in pairs:
            assert 0<=exp<len(out)
            out[exp]+=c
    out[m-n]+=m*m
    return out


def closed_coefficients(k,r):
    if r==1:
        a=(k+1)**2*(k+2)//2
        b=(k+1)*(3*k*k+9*k+7)
        c=(k+1)*(6*k*k+18*k+13)
        d=8*k**3+32*k*k+45*k+22
        poly=18*k**5+138*k**4+490*k**3+970*k*k+1015*k+431
        disc=-F((k+1)**3*(3*k+4)**2*poly,4)
        rminus2=k**3+4*k*k+10*k+8
        return a,b,c,d,disc,rminus2
    a=(k+1)*(k+2)**2//2
    b=(k+2)*(3*k*k+9*k+7)
    c=(k+2)*(6*k*k+18*k+13)
    d=8*k**3+40*k*k+69*k+41
    poly=18*k**5+132*k**4+454*k**3+848*k*k+811*k+310
    disc=-F((k+2)**3*(3*k+5)**2*poly,4)
    rminus2=k**3+5*k*k+13*k+13
    return a,b,c,d,disc,rminus2


def disc_cubic(a,b,c,d):
    return b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d


def run():
    checks=0
    for k in range(61):
        for r in (1,2):
            n=3*k+r; m=n+3
            a,b,c,d,expected_discriminant,rm2=closed_coefficients(k,r)
            Q=source_coefficients(m,n)
            assert Q == [a,b,c,d,c,b,a], (k,r,Q)
            assert disc_cubic(a,b,c-3*a,d-2*b)==expected_discriminant
            assert expected_discriminant<0
            def R(u):
                return a*u**3+b*u*u+(c-3*a)*u+d-2*b
            assert R(-2)==rm2 and rm2>0
            assert R(2)==m**3
            assert R(-1)==m
            checks+=5
    print('PASS:', checks, 'exact integer/rational checks over 122 sample pairs')

if __name__=='__main__':
    run()
