#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json, math
ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/'artifacts'/'certificate.json').read_text())
# irreducible binary moduli, top bit included
MOD={4:0b10011,6:0b1000011,8:0b100011101}

def mul(a,b,m):
    mod=MOD[m]; r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a&(1<<m):a^=mod
    return r&((1<<m)-1)

def sqpow(a,e,m):
    for _ in range(e):a=mul(a,a,m)
    return a

def trace(a,m):
    s=0;x=a
    for _ in range(m):s^=x;x=mul(x,x,m)
    return s&1

def rank_bits(vecs,m):
    B=[0]*m;r=0
    for v in vecs:
        x=v
        while x:
            i=x.bit_length()-1
            if B[i]:x^=B[i]
            else:
                B[i]=x;r+=1;break
    return r

def phi(x,lam,mu,m,k):
    return mul(lam,x,m)^mul(mu,sqpow(x,k,m),m)

def adj(x,lam,mu,m,k):
    s=m-k
    return mul(lam,x,m)^mul(sqpow(mu,s,m),sqpow(x,s,m),m)

def hull_dim(m,k,lam,mu):
    # image basis
    ims=[phi(1<<i,lam,mu,m,k) for i in range(m)]
    imrank=rank_bits(ims,m)
    # Build hull directly as vectors in image killed by adjoint.
    # Enumerate image set (m<=8 in tests).
    image={phi(x,lam,mu,m,k) for x in range(1<<m)}
    hull=[y for y in image if adj(y,lam,mu,m,k)==0]
    # cardinality is power of two
    assert hull and len(hull)&(len(hull)-1)==0
    return len(hull).bit_length()-1

def projective_params(m):
    # P^1(F): (lam:mu) represented by (rho,1), plus (1,0)
    for rho in range(1<<m):yield rho,1
    yield 1,0

cases=[(4,2),(6,2),(6,3),(8,2),(8,4)]
for m,k in cases:
    d=math.gcd(m,k); obs=Counter()
    for lam,mu in projective_params(m):
        h=hull_dim(m,k,lam,mu)
        assert h in (0,d)
        obs[h]+=1
    key=f'q=2,m={m},k={k},d={d}'
    exp={int(a):b for a,b in cert['finite_stress_tests'][key]['hull_dimension_counts'].items()}
    assert dict(obs)==exp,(key,obs,exp)
    assert sum(obs.values())==(1<<m)+1
print('VERIFY_OK')
