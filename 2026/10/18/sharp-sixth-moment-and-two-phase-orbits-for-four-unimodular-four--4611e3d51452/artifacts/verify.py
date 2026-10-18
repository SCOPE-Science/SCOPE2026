#!/usr/bin/env python3
"""Exact coefficient and finite-quadrature checks for four-mode sixth moments."""
import cmath
import itertools
import json
import math
from collections import Counter
from fractions import Fraction


def multiply(a, b):
    out=Counter()
    for k,x in a.items():
        for j,y in b.items():
            out[tuple(k[i]+j[i] for i in range(3))]+=x*y
    return dict(out)


def conj_laurent(a):
    return {tuple(-i for i in k): v for k,v in a.items()}

# Independently build |P^3|^2 as a Laurent polynomial in three free phases.
# Coordinates: U=c1, V=c2, W=c3, c0=1. Circle average fixes frequency.
zero=(0,0,0)
poly={0:{zero:1},1:{(1,0,0):1},2:{(0,1,0):1},3:{(0,0,1):1}}
triples={}
for a,b,c in itertools.product(range(4), repeat=3):
    term=multiply(multiply(poly[a],poly[b]),poly[c]); j=a+b+c
    triples.setdefault(j,Counter()).update(term)
coeff=Counter()
for group in triples.values():
    cg=conj_laurent(group)
    for k,x in group.items():
        for l,y in cg.items():
            coeff[tuple(k[i]+l[i] for i in range(3))]+=x*y
coeff={k:v for k,v in coeff.items() if v}
# I=256 +84 cos alpha+84 cos(beta-2alpha)+144 cos(beta-alpha)
#              +6 cos beta+6 cos(2beta-3alpha),
# where U=c1,V=c2,W=c3 and alpha=arg(V/U^2),beta=arg(W/U^3).
expected={zero:256}
terms=[(42,( -2, 1,0)),(42,(1,-2,1)),(72,(-1,-1,1)),(3,(-3,0,1)),(3,(0,-3,2))]
for amp,key in terms:
    expected[key]=amp
    expected[tuple(-i for i in key)]=amp
assert coeff==expected,(coeff,expected)

# Symbolic exact evaluation of minimizer using rational polynomial arithmetic.
# s*=2-sqrt(111)/6, H=112-132s+288s^2-48s^3.
# Represent algebraic numbers a+b sqrt(111) as rational pairs.
D=111
add=lambda x,y:(x[0]+y[0],x[1]+y[1])
mul=lambda x,y:(x[0]*y[0]+D*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
S=(Fraction(2),-Fraction(1,6));S2=mul(S,S);S3=mul(S2,S)
value=(Fraction(112),Fraction(0))
for c,p in [(-132,S),(288,S2),(-48,S3)]:value=add(value,mul((Fraction(c),Fraction(0)),p))
assert value == (Fraction(616),-Fraction(148,3)),value

# Sharpness of N>=10 from deg(P^3)=9. N=9 counter-witness.
t=Fraction(-1,4)
T3=4*t**3-3*t
T9=4*T3**3-3*T3
assert T9==Fraction(-781,1024)
N9=Fraction(385,4)+2*T9
assert N9==Fraction(48499,512)
assert float(N9)<float(value[0]+value[1]*math.sqrt(D))

# Numerical quadrature tests, including both optimizer branches.
u=complex((math.sqrt(111)-12)/6,math.sqrt(1-((math.sqrt(111)-12)/6)**2))
convolution=[sum(a*b*c for i,a in enumerate([1,1,u,u**3]) for j,b in enumerate([1,1,u,u**3]) for k,c in enumerate([1,1,u,u**3]) if i+j+k==m) for m in range(10)]
norm=sum(abs(x)**2 for x in convolution)
assert abs(norm-float(value[0]+value[1]*math.sqrt(D)))<1e-9
for N in [10,11,12,16,19,32,101]:
    total=0.0
    for j in range(N):
        z=cmath.exp(2j*math.pi*j/N)
        P=1+z+u*z*z+u**3*z**3
        total+=abs(P)**6
    assert abs(total/N-norm)<1e-8,(N,total/N,norm)

print(json.dumps({
    'status':'PASS',
    'exact_laurent_terms':len(coeff),
    'exact_coefficient_identity':True,
    'radical_minimum':'616 - (148/3)*sqrt(111)',
    'numerical_minimum':float(value[0]+value[1]*math.sqrt(D)),
    'optimizer_cosine':(math.sqrt(D)-12)/6,
    'finite_grids_verified':[10,11,12,16,19,32,101],
    'N9_counterexample_value':'48499/512',
    'N9_counterexample_decimal':float(N9)
},sort_keys=True,indent=2))
