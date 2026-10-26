#!/usr/bin/env python3
"""Exact integer-exponent and finite-field checks for cyclic Klein reductions.

Not a substitute for the symbolic scheme-isomorphism proof in RESULT.md.
"""
from math import gcd

def vp(n,p):
    v=0
    while n%p==0:
        n//=p;v+=1
    return v

def check(p,d,m):
    assert m>=3 and d>=3 and d%p==0 and m%p==0
    exps=[0,1]
    for i in range(1,m):
        exps.append((d-1)*exps[i-1]-(d-2)*exps[i])
    a=exps[m]
    assert a == (1-(1-d)**m)//d
    assert 1-(d-1)*exps[m-1]==a
    assert (d-2)*exps[m-1]-(d-1)*exps[m-2] == -a
    assert all((d-1)*exps[i-1]-(d-2)*exps[i]==exps[i+1] for i in range(1,m))
    N=abs(a)
    predicted=(vp(m,p) if p!=2 or d%4==0 else vp(d-2,2)+vp(m,2)-1)
    assert vp(N,p)==predicted
    multiplicity=p**predicted
    assert N % multiplicity == 0
    distinct=N//multiplicity
    # The monomials x_i^(d-1)*x_(i+1) are equal modulo t^a=1.
    e=[(d-1)*exps[i]+exps[(i+1)%m] for i in range(m)]
    assert len({z % N for z in e})==1
    # Every gradient relation x_i^(d-2)*x_(i+1)=x_(i-1)^(d-1)
    # holds in the quotient by t^a-1.
    rel=[(d-2)*exps[i]+exps[(i+1)%m]-(d-1)*exps[(i-1)%m] for i in range(m)]
    assert all(z%N==0 for z in rel)
    return N,distinct,multiplicity,gcd(distinct,p-1)

for p,d,m in [(2,4,4),(2,6,4),(2,4,6),(3,3,3),(3,3,6),(3,3,9),(3,6,6),(3,6,9),(5,5,5),(5,10,10),(7,7,7)]:
    out=check(p,d,m)
    print('p,d,m=',p,d,m,'(length,geom_support,local_length,Fp_support)=',out)
print('VERIFY_OK')
