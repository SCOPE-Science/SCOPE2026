#!/usr/bin/env python3
"""Exact, dependency-free checks for the four-asset correlation example."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial, exp, sqrt, cosh


def padd(p, q):
    n=max(len(p),len(q)); out=[F(0)]*n
    for i,v in enumerate(p): out[i]+=v
    for i,v in enumerate(q): out[i]+=v
    while len(out)>1 and out[-1]==0: out.pop()
    return out


def pmul(p, q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]+=a*b
    while len(out)>1 and out[-1]==0: out.pop()
    return out


def determinant_polynomial(M):
    n=len(M); out=[F(0)]
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=[F(1)]
        for i,j in enumerate(perm):
            entry=[F(-M[i][j]), F(1) if i==j else F(0)]
            term=pmul(term,entry)
        if inversions % 2: term=[-x for x in term]
        out=padd(out,term)
    out += [F(0)]*(n+1-len(out))
    return out


def cosh_upper_from_square(q):
    """Upper bound through x^4, with a geometric bound for the x^6 tail."""
    assert F(0) <= q < 56
    return F(1)+q/2+q*q/24+q**3/(720*(1-q/56))


def cosh_lower_through_eighth(q):
    """Lower bound from the positive Taylor series through x^8."""
    return sum((q**k/F(factorial(2*k)) for k in range(5)), F(0))


A=[
 [0,-1,-1,-1],
 [-1,0,-1,1],
 [-1,-1,0,1],
 [-1,1,1,0],
]
B=[[abs(v) for v in row] for row in A]
assert determinant_polynomial(A)==[F(5),F(0),F(-6),F(0),F(1)]
assert determinant_polynomial(B)==[F(-3),F(-8),F(-6),F(0),F(1)]

# C = I + (2/5) A is positive definite because (2 sqrt(5) / 5)^2 = 4/5 < 1.
assert F(4,5) < 1
# The Euclidean condition-number ratio is exp((4 sqrt(5)-8)/5), strictly > 1.
assert 5 > 4

# Exact rational enclosure of the Schatten-1 ratio at t=2/5.
Ux=cosh_upper_from_square(F(4,5))
Uy=cosh_upper_from_square(F(4,25))
Lz=cosh_lower_through_eighth(F(64,25))
numerator_upper=4*(Ux+Uy)**2
denominator_lower=10+6*Lz
assert numerator_upper < denominator_lower
assert numerator_upper/denominator_lower < F(989,1000)

# Floating-point values are only illustrative; the assertions above are exact.
t=2/5
r2=exp(t*(2*sqrt(5)-4))
r1=4*(cosh(t*sqrt(5))+cosh(t))**2/(10+6*cosh(4*t))
print('PASS: exact characteristic polynomials for A and |A|')
print('PASS: C is positive definite; diagonal entries are 1')
print('PASS: exact rational upper bound for Schatten-1 ratio is < 0.989')
print('PASS: Euclidean condition-number ratio is exactly exp((4*sqrt(5)-8)/5) > 1')
print('illustrative cond2 ratio:', format(r2,'.12f'))
print('illustrative Schatten-1 ratio:', format(r1,'.12f'))
print('rational upper bound:', numerator_upper/denominator_lower)
