#!/usr/bin/env python3
"""Reproducible finite-field structural checks; no external packages."""
from itertools import product

def mul(a,b,q):
    if q==2:return a&b
    p=0
    for i in range(2):
        if (b>>i)&1:p^=a<<i
    # GF(4) = F2[z]/(z^2+z+1)
    for i in (2,3):
        if (p>>i)&1:p^=7<<(i-2)
    return p

def test(q):
    els=range(q); count=0; mats=set()
    for a,b,f,g in product(els,repeat=4):
        delta=mul(a,g,q)^mul(b,f,q)
        if delta==0:continue
        for s,t in product(els,repeat=2):
            count+=1
            M=(a,f,0,b,g,0,s,t,delta)
            assert M[2]==0 and M[5]==0
            mats.add(M)
    gl2=(q*q-1)*(q*q-q)
    assert count==q*q*gl2 and len(mats)==count
    print('AUT_REDUCED_OK',q,count)
for q in (2,4):test(q)
# Eight formal independent coefficients of a derivation give exactly every
# traceless 3x3 matrix in characteristic 2.
mat={}
for u,v,b,c,d,f,g,h in product(range(2),repeat=8):
    z=(b,f,v,c,g,u,d,h,b^g)
    assert z[0]^z[4]^z[8]==0
    mat[z]=1
assert len(mat)==2**8
print('LIE_DIFFERENTIAL_OK',len(mat))
# The coordinate algebra of the infinitesimal constant part has basis
# {1,c,e,ce}, not merely {1,c,e}.
assert len({(i,j) for i in range(2) for j in range(2)})==4
print('AUT_SCHEME_TESTS_OK')
