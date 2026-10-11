#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial

def C(p,q):
    d=p+q
    return (Fraction(comb(d,p)**2,1)
            * Fraction((p+1)*(p+2),(d+1)*(d+2))**p
            * Fraction((q+1)*(q+2),(d+1)*(d+2))**q)

def cube_S(d):
    return Fraction(1,12)**d

def cross_S(d):
    return Fraction(factorial(d)**2,
                    (2**d)*(((d+1)*(d+2))**d))

# Direct-sum coefficient certificate.
assert C(1,1)==1
for d in range(3,41):
    for p in range(1,d):
        q=d-p
        assert 0<C(p,q)<1, (p,q,C(p,q))

# Cross-polytope recursion and endpoint comparison.
for d in range(2,41):
    for p in range(1,d):
        q=d-p
        assert cross_S(d)==C(p,q)*cross_S(p)*cross_S(q)
    assert cross_S(d)<=cube_S(d)
    if d>=3:
        assert cross_S(d)<cube_S(d)

# Recursively enumerate exact isotropic values of all Hanner construction
# expressions, identifying equal values even when expressions differ.
values={1:{Fraction(1,12)}}
for d in range(2,10):
    vals=set()
    for p in range(1,d):
        q=d-p
        for a in values[p]:
            for b in values[q]:
                vals.add(a*b)          # Cartesian product
                vals.add(C(p,q)*a*b)   # l1 direct sum
    values[d]=vals
    assert min(vals)==cross_S(d), (d,min(vals),cross_S(d))
    assert max(vals)==cube_S(d), (d,max(vals),cube_S(d))

# Independent moment formulas.
# Cube [-1,1]^d: covariance scalar 1/3 and volume 2^d.
for d in range(1,20):
    cube_from_moments = Fraction(1,3)**d / Fraction(4**d,1)
    assert cube_from_moments==cube_S(d)

    # Cross-polytope: covariance scalar 2/((d+1)(d+2)),
    # volume 2^d/d!.
    covdet=Fraction(2,(d+1)*(d+2))**d
    vol2=Fraction(4**d,factorial(d)**2)
    assert covdet/vol2==cross_S(d)

print("VERIFY_OK")
print("direct_sum_loss_up_to_dimension = 40")
print("all_hanner_values_enumerated_through_dimension = 9")
print("cube_and_crosspolytope_moments = exact")
