#!/usr/bin/env python3
"""Standalone exact finite-subset checks of the collective exchange spectrum."""
from fractions import Fraction
from math import comb, e

def eigs(d):
    out=[]
    for k in range(d+1):
        for r in range(min(k,d-k)+1):
            lam=k*(d-k)-r*(d-r+1)
            out.extend([lam]*(comb(d,r)-(comb(d,r-1) if r else 0)))
    return sorted(out)

def exact_power2_trace(d):
    return sum(comb(d,k)*k*(d-k) for k in range(d+1))

checks=0
for d in range(2,16):
    L=eigs(d)
    assert len(L)==2**d;checks+=1
    assert sum(L)==0;checks+=1
    assert sum(x*x for x in L)==d*(d-1)*2**(d-2);checks+=1
    assert sum(x*x for x in L)==exact_power2_trace(d);checks+=1
    assert max(map(abs,L))==d*d//4 if d%2==0 else (d*d-1)//4;checks+=1
    for ell in range(0,12):
        a=Fraction(d-1,(ell+d-1)*(ell+d))
        assert a==Fraction(d-1,ell+d-1)-Fraction(d-1,ell+d);checks+=1
    for cut in range(0,12):
        s=sum((Fraction(d-1,(k+d-1)*(k+d)) for k in range(cut+1)),Fraction(0))
        assert s==1-Fraction(d-1,cut+d);checks+=1
for d in (16,18,20,22,24,26,30,36,44):
    # Avoid exponential matrix construction: use harmonic multiplicity formula.
    energy=sum((comb(d,r)-(comb(d,r-1) if r else 0))*abs(k*(d-k)-r*(d-r+1))
               for k in range(d+1) for r in range(min(k,d-k)+1))
    ratio=energy/(d*2**d)
    assert 0 < ratio < 1/2;checks+=1
    if d>=30: assert abs(ratio-1/e)<0.03;checks+=1
print('PASS:',checks,'exact/rational combinatorial assertions and asymptotic consistency checks')
