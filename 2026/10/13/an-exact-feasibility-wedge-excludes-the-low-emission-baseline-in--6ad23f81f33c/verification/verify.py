#!/usr/bin/env python3
from fractions import Fraction

m=Fraction(2,5)
alpha=Fraction(1,5)
delta=Fraction(17,20)
ks=(Fraction(11,10),Fraction(13,10))
thetas=(Fraction(7,10),Fraction(29,20))
phis=(Fraction(3,4),Fraction(9,10))

def bounds(theta,phi):
    A=m+(1-alpha)*delta
    L=A*(delta*theta+phi)/(2*theta*phi)
    D=4*m*theta-2*(1-alpha)*phi
    U=A*A/D
    return L,U,D

for theta in thetas:
    for phi in phis:
        L,U,D=bounds(theta,phi)
        wedge=((1-alpha)*phi/Fraction(2) < m*theta < (1-alpha)*phi)
        nonempty=(D>0 and L<U)
        assert wedge == nonempty

L,U,D=bounds(Fraction(7,10),Fraction(3,4))
assert L == Fraction(2421,1750)
assert U == -Fraction(729,50)
assert D < 0
assert not any(L < k < U for k in ks)

L,U,D=bounds(Fraction(7,10),Fraction(9,10))
assert L == Fraction(897,700)
assert U == -Fraction(729,200)
assert D < 0
assert not any(L < k < U for k in ks)

L,U,D=bounds(Fraction(29,20),Fraction(3,4))
assert L == Fraction(7137,7250)
assert U == Fraction(729,700)
assert D > 0
assert not any(L < k < U for k in ks)

L,U,D=bounds(Fraction(29,20),Fraction(9,10))
assert L == Fraction(2559,2900)
assert U == Fraction(729,550)
assert D > 0
assert all(L < k < U for k in ks)

for theta in thetas:
    for phi in phis:
        lhs=((1-alpha)*phi/Fraction(2) < m*theta < (1-alpha)*phi)
        rhs=(phi < theta < 2*phi)
        assert lhs == rhs

print("VERIFY_OK")
