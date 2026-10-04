#!/usr/bin/env python3
from fractions import Fraction

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

assert mul(mul([1,1],[1,1]),[1,1,1]) == [1,3,4,3,1]
assert mul(mul([-1,1],[-1,1]),[1,-1,1]) == [1,-3,4,-3,1]

d=4
chi=Fraction(72-62*d+35*d*d-10*d**3+d**4,12)
assert chi == 0

def padd(A,B):
    C=A.copy()
    for m,c in B.items():
        C[m]=C.get(m,0)+c
        if C[m]==0: del C[m]
    return C

def pmul(A,B):
    C={}
    for m,c in A.items():
        for n,e in B.items():
            k=tuple(m[i]+n[i] for i in range(4))
            C[k]=C.get(k,0)+c*e
    return {m:c for m,c in C.items() if c}

def pscale(A,s): return {m:s*c for m,c in A.items() if s*c}
one={(0,0,0,0):1}
a={(1,0,0,0):1}; dd={(0,1,0,0):1}; x={(0,0,1,0):1}; y={(0,0,0,1):1}
p12=one; p14=dd; p23=pscale(a,-1); p13=pmul(dd,y); p24=pscale(pmul(a,x),-1)
p34=padd(pmul(a,dd), pscale(pmul(pmul(pmul(a,dd),x),y),-1))
rel=padd(padd(pmul(p12,p34),pscale(pmul(p13,p24),-1)),pmul(p14,p23))
assert rel == {}
rhs=padd(pmul(a,dd),pscale(pmul(pmul(pmul(a,dd),x),y),-1))
assert p34 == rhs
print('VERIFY_OK')
