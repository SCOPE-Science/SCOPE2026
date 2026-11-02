#!/usr/bin/env python3
"""Exact cyclotomic Fourier-support checks for quartic graphs modulo prime squares."""
from itertools import product

def nz_fourier(p, a,b):
    q=p*p
    cnt=[0]*q
    for x in range(q):
        cnt[(a*x+b*pow(x,4,q))%q]+=1
    # Phi_{p^2}(X)=sum_{j=0}^{p-1}X^{jp}; coefficient vector
    # at each exponent mod p is constant across all p lifts iff zero.
    return any(cnt[r]!=cnt[r+j*p] for r in range(p) for j in range(1,p))

def predicted(p,a,b):
    ar=a%p; br=b%p
    if ar==br==0:
        A=(a//p)%p; B=(b//p)%p
        return not ((B==0 and A!=0) or (p==7 and B!=0 and A in {3*B%p,4*B%p}))
    if br==0:return False
    return any((ar+4*br*pow(x,3,p))%p==0 for x in range(p))

for p in (5,7,11):
    q=p*p; count=0
    for a,b in product(range(q),repeat=2):
        expected=predicted(p,a,b)
        actual=nz_fourier(p,a,b)
        assert actual==expected,(p,a,b,actual,expected)
        count+=actual
    d=3 if p%3==1 else 1
    rank=q*(p-1)*(1+(p-1)//d)+q-(p-1)*(1+2*(p==7))
    assert count==rank,(p,count,rank)
    print('QUARTIC_EXACT_OK',p,'rank',rank,'dimension',q*q)
for p in (13,17,19):
    g=[c for c in range(1,p) if len({(x**4+c*x)%p for x in range(p)})==p]
    assert not g,(p,g)
print('QUARTIC_PRIME_SQUARE_CYCLOTOMIC_OK')
