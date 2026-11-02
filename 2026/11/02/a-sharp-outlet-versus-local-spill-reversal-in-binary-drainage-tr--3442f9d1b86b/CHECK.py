#!/usr/bin/env python3
"""Exact independent enumeration for a seven-input binary spill tree."""
from itertools import product
from math import comb
from fractions import Fraction

# Polynomials in p and q with integer coefficients indexed by (p-power,q-power).
def poly_add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return {k:v for k,v in out.items() if v}

def poly_neg(a):
    return {k:-v for k,v in a.items()}

def poly_sub(a,b):
    return poly_add(a,poly_neg(b))

def poly_mul(a,b):
    out = {}
    for (i,j),x in a.items():
        for (u,v),y in b.items():
            z=(i+u,j+v)
            out[z]=out.get(z,0)+x*y
    return {k:v for k,v in out.items() if v}

def polypow(a,n):
    out={(0,0):1}
    for _ in range(n):out=poly_mul(out,a)
    return out

ONE={(0,0):1}
P={(1,0):1}
Q={(0,1):1}
TWO={(0,0):2}
ZERO={}

def bit_probability(leaf_bits, storm_bits):
    a=sum(leaf_bits);b=sum(storm_bits)
    return poly_mul(poly_mul(polypow(Q,a),polypow(poly_sub(ONE,Q),4-a)),
                    poly_mul(polypow(P,b),polypow(poly_sub(ONE,P),3-b)))

def majority(x,y,z):
    return int(x+y+z>=2)

def configurations(leaf,storm):
    a,b,c,d=leaf
    i,j,k=storm
    lo=majority(a,b,i)
    mid_b=majority(c,d,j)
    root_b=majority(lo,mid_b,k)
    mid_c=majority(lo,c,j)
    root_c=majority(mid_c,d,k)
    return (root_b,root_c,lo+mid_b+root_b,lo+mid_c+root_c)

out=[ZERO,ZERO,ZERO,ZERO]
counts=0
for leaf in product((0,1),repeat=4):
    for storm in product((0,1),repeat=3):
        w=bit_probability(leaf,storm)
        states=configurations(leaf,storm)
        out=[poly_add(z,{k:v*s for k,v in w.items()}) for z,s in zip(out,states)]
        counts+=1

# Directly compute two algebraic identities, not via the tree recursion.
root_gap=poly_sub(out[0],out[1])
internal_gap=poly_sub(out[2],out[3])
root_rhs=polypow(P,1)
for t in (Q,poly_sub(ONE,P),poly_sub(ONE,Q),poly_sub(poly_mul(TWO,P),ONE)):
    root_rhs=poly_mul(root_rhs,t)
internal_rhs=poly_neg(poly_mul(poly_mul(Q,poly_sub(ONE,Q)),
                     poly_mul(poly_sub(poly_mul(TWO,P),ONE),
                              poly_add(polypow(P,2),poly_mul(poly_sub(ONE,poly_mul(TWO,P)),Q)))))
assert root_gap==root_rhs,(root_gap,root_rhs)
assert internal_gap==internal_rhs,(internal_gap,internal_rhs)
assert len(root_gap)>0 and len(internal_gap)>0

# Check the probability normalization and direct sums at 17 rational pairs.
assert counts==128
for pn,qn in [(1,1),(1,2),(1,3),(2,3),(1,4),(3,4),(1,5),(4,5),(1,7),
              (2,7),(3,7),(4,7),(5,7),(6,7),(2,5),(3,5),(1,9)]:
    p=Fraction(pn,11);q=Fraction(qn,12)
    def evaluate(poly):
        return sum(Fraction(v)*p**i*q**j for (i,j),v in poly.items())
    for z in out[:2]:assert Fraction(0)<=evaluate(z)<=Fraction(1)
    assert evaluate(root_gap)==p*q*(1-p)*(1-q)*(2*p-1)
    assert evaluate(internal_gap)==-q*(1-q)*(2*p-1)*(p*p+(1-2*p)*q)
print('PASS: 128/128 configurations, two exact bivariate polynomial identities, 68 rational checks')
