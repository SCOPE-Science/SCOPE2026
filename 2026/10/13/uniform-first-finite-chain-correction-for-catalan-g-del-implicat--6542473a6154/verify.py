#!/usr/bin/env python3
"""Numerical checks of uniformly corrected Gödel-chain survival probabilities."""
import math

def predicted(m,k):
    t=k/m; y=1+2*t
    E=0.5+(math.log(y)-2)/(4*y)
    return y**(-0.5)*(1+E/m)

def exact_products(m):
    h=1/m; u=0.5; p=1.0
    yield 0,p
    for k in range(1,m):
        root=math.sqrt(u*u+h)
        p *= (1+u/root)/2
        u=(u+root)/2
        yield k,p

for m in [2,3,4,5,10,20,50,100,200,500,1000,2000]:
    samples=list(exact_products(m))
    errors=[abs(p-predicted(m,k)) for k,p in samples]
    k,p=samples[-1]
    y=3
    top_asym=(1/math.sqrt(3))*(1+(8+math.log(3))/(12*m))
    print('m',m,'maxerr*m²',f'{m*m*max(errors):.8f}','top',f'{p:.12f}','top_asym',f'{top_asym:.12f}','scaled coefficient',f'{m*(p*math.sqrt(3)-1):.9f}')
    assert m*m*max(errors) < 2.0
# Independent finite-size Catalan/valuation recurrence, not relying on the product formula.
from math import comb
for m in range(2,7):
    counts = {1:[1]*m}
    for n in range(2,9):
        out=[0]*m
        for left_size in range(1,n):
            left=counts[left_size]
            right=counts[n-left_size]
            for a in range(m):
                for b in range(m):
                    result=(m-1) if a<=b else b
                    out[result]+=left[a]*right[b]
        counts[n]=out
        total=m**n*comb(2*(n-1), n-1)//n
        assert sum(out)==total, (m,n,total,sum(out))
        if n==2:
            assert out[-1]==m*(m+1)//2
    print('Catalan_DPI_OK',m,counts[8][-1])
print('VERIFY_OK')
