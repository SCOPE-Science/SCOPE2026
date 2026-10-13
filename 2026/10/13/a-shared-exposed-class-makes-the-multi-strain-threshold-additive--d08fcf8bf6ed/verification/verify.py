#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt

alpha=Fraction(4,5)
beta=Fraction(3,2)
mu=Fraction(1,10)
phi1=phi2=Fraction(9,20)
phi=phi1+phi2
mu1=mu2=Fraction(1,5)
gamma1=gamma2=Fraction(7,10)
delta1=Fraction(1,5)
gamma=Fraction(7,10)

a=mu+phi
d1=mu1+gamma1+mu
d2=mu2+gamma2+mu
dC=mu+delta1+gamma
assert a == d1 == d2 == dC == 1

C0=beta*(1-alpha)*phi/(a*dC)
A1=beta*alpha*phi1/(a*d1)
A2=beta*alpha*phi2/(a*d2)
assert C0 == Fraction(27,100)
assert A1 == A2 == Fraction(54,100)
source_sq=C0+A1
correct=C0+A1+A2
assert source_sq == Fraction(81,100)
assert correct == Fraction(27,20)
assert Fraction(9,10)**2 == source_sq
assert Fraction(9,10) < 1 < correct

# Matrix entries of the infected linearization.
M = [
    [Fraction(-1), Fraction(3,2), Fraction(3,2), Fraction(3,2)],
    [Fraction(9,25), Fraction(-1), Fraction(0), Fraction(0)],
    [Fraction(9,25), Fraction(0), Fraction(-1), Fraction(0)],
    [Fraction(9,50), Fraction(0), Fraction(0), Fraction(-1)],
]

# Evaluate det(lambda I-M) exactly by permutation expansion.
from itertools import permutations

def parity(p):
    inv=0
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            inv += p[i] > p[j]
    return -1 if inv % 2 else 1

def det_at(lam):
    A=[[ (lam if i==j else Fraction(0)) - M[i][j] for j in range(4)] for i in range(4)]
    total=Fraction(0)
    for p in permutations(range(4)):
        prod=Fraction(1)
        for i,j in enumerate(p):
            prod *= A[i][j]
        total += parity(p)*prod
    return total

def claimed(lam):
    return (lam+1)**2 * (lam*lam+2*lam-Fraction(7,20))

# Equality at five points certifies equality of the degree-four polynomials.
for lam in map(Fraction, [-3,-2,-1,0,2]):
    assert det_at(lam) == claimed(lam)

largest=-1+3*sqrt(15)/10
assert largest > 0
assert abs(largest-0.161895003862225) < 1e-12

print('VERIFY_OK')
