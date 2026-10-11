#!/usr/bin/env python3
from fractions import Fraction

cases=0
for n in range(3,201):
    total=n*(n-1)+1
    mu=Fraction(total,n)
    r2=Fraction((n-1)**3,n)
    alpha2=Fraction(n-1,n)

    # Singleton slack and squared distance.
    s1=mu-1
    assert s1==Fraction((n-1)**2,n)
    assert s1*s1/alpha2==r2

    # Sum of singleton constraints reproduces the sharp radius bound.
    assert total-n==(n-1)**2

    for k in range(1,n):
        slack=k*mu-Fraction(k*(k+1),2)
        normal2=Fraction(k*(n-k),n)
        d2=slack*slack/normal2
        if k==1:
            assert d2==r2
        else:
            assert d2>r2
            j=n-k
            Q=n*j*j+(2*n*n-7*n+4)*j+(n-2)**2*(n-1)
            rhs=Fraction((k-1)*Q,4*(n-k))
            assert d2-r2==rhs
        cases+=1

print(f"VERIFY_OK standard-cyclohedron-inradius n=3..200 facet_cardinalities={cases}")
