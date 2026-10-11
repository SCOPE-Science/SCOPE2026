#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

# Sparse polynomial in variables a,b,c,u,v,w represented by exponent tuples.
NVAR = 6
def add(P,Q):
    R=P.copy()
    for m,c in Q.items():
        R[m]=R.get(m,Fraction(0))+c
        if not R[m]: del R[m]
    return R
def mul(P,Q):
    R={}
    for m,c in P.items():
        for n,d in Q.items():
            k=tuple(m[i]+n[i] for i in range(NVAR))
            R[k]=R.get(k,Fraction(0))+c*d
    return {m:c for m,c in R.items() if c}
def scale(P,c):
    return {m:c*v for m,v in P.items() if c*v}
def power(P,k):
    R={(0,)*NVAR:Fraction(1)}
    for _ in range(k): R=mul(R,P)
    return R
def var(i):
    e=[0]*NVAR; e[i]=1
    return {tuple(e):Fraction(1)}

a=[var(0),var(1),var(2)]
l=[var(3),var(4),var(5)]
F={}
for p in permutations(range(3)):
    s={}
    for i in range(3):
        s=add(s,mul(a[p[i]],l[i]))
    F=add(F,power(s,3))

tr=add(add(l[0],l[1]),l[2])
tr2=add(add(power(l[0],2),power(l[1],2)),power(l[2],2))
tr3=add(add(power(l[0],3),power(l[1],3)),power(l[2],3))

Acoef=scale(mul(mul(a[0],a[1]),a[2]),Fraction(6))
sum_sym={}
for i in range(3):
    for j in range(3):
        if i!=j:
            sum_sym=add(sum_sym,mul(power(a[i],2),a[j]))
Bcoef=scale(add(sum_sym,scale(mul(mul(a[0],a[1]),a[2]),Fraction(-6))),Fraction(3))

def lin(c0,c1,c2):
    return add(add(scale(a[0],Fraction(c0)),scale(a[1],Fraction(c1))),scale(a[2],Fraction(c2)))
Ccoef=mul(mul(lin(1,-2,1),lin(1,1,-2)),lin(2,-1,-1))
rhs=add(add(mul(Acoef,power(tr,3)),mul(Bcoef,mul(tr,tr2))),mul(Ccoef,tr3))
assert F==rhs

# Discriminant identity for t^3 - S t - 2xyz.
# Check exact integer instances, while the closed formula is proved in RESULT.md.
for x in range(-4,5):
    for y in range(-4,5):
        for z in range(-4,5):
            S=x*x+y*y+z*z
            disc=4*S**3-108*x*x*y*y*z*z
            p=-S
            q=-2*x*y*z
            assert disc == -4*p**3-27*q**2

# Repeated-coordinate construction: compare the three distinct values,
# each duplicated, with all six permutation pairings.
tests=[
    (Fraction(3),Fraction(-2),[Fraction(1),Fraction(4),Fraction(-5)]),
    (Fraction(7,3),Fraction(2,5),[Fraction(-2),Fraction(1,2),Fraction(9,4)]),
]
for alpha,beta,lams in tests:
    trv=sum(lams)
    block=sorted([beta*trv+(alpha-beta)*x for x in lams])
    pairings=[]
    weights=[alpha,beta,beta]
    for p in permutations(range(3)):
        pairings.append(sum(weights[p[i]]*lams[i] for i in range(3)))
    assert sorted(block+block)==sorted(pairings)

print("VERIFY_OK d3-spectral-linearization cubic_identity=exact discriminant_cases=729 repeated_cases=2")
