#!/usr/bin/env python3
"""Standalone finite exact check for a characteristic-five genus-three plane quartic.
No external libraries are required. The proof of the universal assertion is in RESULT.md.
"""
from itertools import product
from math import factorial

P=5
# Each monomial is (exponents of x,y,z,a,b) with a coefficient in F5.
TERMS = [((0,3,1,0,0), 1), ((4,0,0,0,0),-1),
         ((2,0,2,1,0),-1),((0,0,4,0,1),-1)]
coeff={}
for selection in product(TERMS, repeat=4):
    exponent=tuple(sum(t[0][j] for t in selection) for j in range(5))
    scalar=1
    for term in selection:scalar=scalar*term[1]%P
    coeff[exponent]=(coeff.get(exponent,0)+scalar)%P

def polynomial_coefficient(spatial):
    return {ab: value for exponent,value in coeff.items()
            if exponent[:3] == spatial and value and (ab := exponent[3:])}

BASIS=[(2,1,1),(1,2,1),(1,1,2)]
M=[[polynomial_coefficient(tuple(5*s[k]-t[k] for k in range(3)))
    for s in BASIS] for t in BASIS]
expect=[[{}, {}, {}], [{}, {}, {(2,1):3,(0,2):3}], [{}, {(0,0):1}, {}]]
assert M==expect, (M,expect)
print('CARTIER_COEFFICIENTS_OK',M)

# A finite-field test over F5 and F25; F25=F5[u]/(u^2-2).
def mul(x,y):return ((x[0]*y[0]+2*x[1]*y[1])%5,
                      (x[0]*y[1]+x[1]*y[0])%5)
def add(x,y):return ((x[0]+y[0])%5,(x[1]+y[1])%5)
def exp(x,n):
    z=(1,0)
    for _ in range(n):z=mul(z,x)
    return z
fields=[[(i,0) for i in range(5)],list(product(range(5),repeat=2))]
for elems in fields:
    q=len(elems);one=(1,0)
    for av,bv in ((0,1),(1,1),(3,2)):
        a=(av,0);b=(bv,0)
        smooth=mul(b,add(exp(a,2),b))!=(0,0)
        if not smooth:continue
        count=1 # unique rational smooth point at infinity
        for x in elems:
            f=add(add(exp(x,4),mul(a,exp(x,2))),b)
            for y in elems:
                if exp(y,3)==f:count+=1
        if q==5:assert count%5==1,(av,bv,count)
        print('FIELD_COUNT',q,'a',av,'b',bv,'n',count)
print('CHECK_OK')
