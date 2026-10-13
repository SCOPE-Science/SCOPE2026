#!/usr/bin/env python3
# Standard-library exact polynomial replay for the q=3, k=3 Potts calculation.
from fractions import Fraction

# Polynomials in (v,t) are dictionaries {(degree_v, degree_t): integer}.
def clean(a):
    return {k:c for k,c in a.items() if c}
def add(a,b):
    r=dict(a)
    for k,c in b.items(): r[k]=r.get(k,0)+c
    return clean(r)
def neg(a): return {k:-c for k,c in a.items()}
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    r={}
    for (i,j),c in a.items():
        for (k,l),d in b.items():
            key=(i+k,j+l); r[key]=r.get(key,0)+c*d
    return clean(r)
def scale(a,c): return clean({k:c*v for k,v in a.items()})
def powp(a,n):
    r={(0,0):1}
    for _ in range(n): r=mul(r,a)
    return r
def dv(a):
    return clean({(i-1,j):i*c for (i,j),c in a.items() if i})

ONE={(0,0):1}; V={(1,0):1}; T={(0,1):1}
p=add(V,powp(V,2))
L=sub(mul(sub(T,ONE),p),add(powp(V,3),ONE))
Lfac=mul(add(V,ONE),sub(mul(T,V),add(powp(V,2),ONE)))
assert L==Lfac

# Source derivative numerator for k=3:
# (p+1)(p-2L)L' - 3 L(1-L)p'
N=sub(mul(mul(add(p,ONE),sub(p,scale(L,2))),dv(L)), scale(mul(mul(L,sub(ONE,L)),dv(p)),3))
Q={
 (4,0):-2, (3,1):2, (3,0):-6,
 (2,1):5, (2,0):-5,
 (1,1):2, (1,0):-6, (0,0):-2
}
rhs=mul(mul(mul(add(T,scale(ONE,2)),sub(V,ONE)),add(V,ONE)),Q)
assert N==rhs

# Exact endpoint identities for R_t(x).
def R(theta,x):
    return -2*x*x + (2*theta-6)*x + 5*theta - 1
for th in [Fraction(9,4), Fraction(7,3), Fraction(5,2), Fraction(8,1), Fraction(20,1)]:
    assert R(th,Fraction(2,1)) == 3*(3*th-7)
    assert R(th,th) == -(th+1)

# Supplementary finite shape checks only; the proof in RESULT.md is analytic.
for th in [Fraction(9,4), Fraction(5,2), Fraction(5,1), Fraction(8,1), Fraction(20,1)]:
    if th <= Fraction(7,3):
        assert R(th,Fraction(2,1)) <= 0
    else:
        assert R(th,Fraction(2,1)) > 0 and R(th,th) < 0

print('VERIFY_OK')
