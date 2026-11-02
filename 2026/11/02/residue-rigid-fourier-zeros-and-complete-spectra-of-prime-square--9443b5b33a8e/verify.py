#!/usr/bin/env python3
"""Exact cyclotomic verification of the spectral universality of residue-lift graphs."""
from itertools import product, combinations
from collections import Counter
from math import comb

def graph_values(p,h):
    q=p*p
    return [(pow(x%p,p,q)+p*h[x%p])%q for x in range(q)]

def is_cyclotomic_zero(p,u,v,F):
    q=p*p
    coeff=[0]*q
    for x,y in enumerate(F):
        coeff[(u*x+v*y)%q]+=1
    return all(coeff[j]==coeff[j+p*t] for j in range(p) for t in range(1,p))

def theoretical_zero(p,u,v):
    if u%p: return True
    if v%p: return False
    return (u+v)%(p*p)!=0

def check(p,h):
    q=p*p; f=graph_values(p,h)
    assert all(f[x]==f[x+p] for x in range(q-p))
    assert all(f[x]%p==x%p for x in range(q))
    nz=0
    for u in range(q):
        for v in range(q):
            z=is_cyclotomic_zero(p,u,v,f)
            assert z==theoretical_zero(p,u,v), (p,h,u,v,z)
            nz+=not z
    assert nz==p**3-p*p+p
    # Construct spectra with a distinct choice of sum of second digits in each first-digit residue class.
    for seed in range(3):
        Lambda=[]
        for a in range(p):
            b=(a*a+seed)%p
            for c in range(p):
                s=(2*c+a+seed)%p
                t=(c-s)%p
                Lambda.append((a+p*s,b+p*t))
        assert len(set(Lambda))==q
        for i,j in combinations(Lambda,2):
            assert theoretical_zero(p,(i[0]-j[0])%q,(i[1]-j[1])%q)
            assert is_cyclotomic_zero(p,(i[0]-j[0])%q,(i[1]-j[1])%q,f)
    print(f'EXACT_FOURIER_AND_SPECTRAL_WITNESSES_OK p={p} Fourier_pairs={q*q} rank={nz}')

for p in (3,):
    for h in product(range(p),repeat=p): check(p,h)
for p in (5,7):
    for seed in (0,1,3):
        h=[(a*a+seed*a+2*seed)%p for a in range(p)]
        check(p,h)
# independent exhaustive enumeration of size-p^2 spectra when p=2 on the 16-point dual group.
p=2; q=4; f=graph_values(p,[0,1]); count=0
for S in combinations(product(range(q),repeat=2),q):
    if all(is_cyclotomic_zero(p,(a[0]-b[0])%q,(a[1]-b[1])%q,f) for a,b in combinations(S,2)):
        count+=1
assert count==2**(2*2+2)==64
print('EXHAUSTIVE_TWO_ADIC_CROSSCHECK_OK spectra=64')
print('ALL_EXACT_CERTIFICATES_OK')
# Independently count all affine graphs for small primes using exact cyclotomic character sums.
for p in (3,5):
    q=p*p; f=graph_values(p,[a*a%p for a in range(p)])
    good=0
    for alpha in range(q):
        for beta in range(q):
            L=[(u,(alpha*u+beta)%q) for u in range(q)]
            # translation-invariant differences make beta irrelevant to zero status,
            # but verify all consecutive and all a-residue equal pairs.
            ok=all(is_cyclotomic_zero(p,(x[0]-y[0])%q,(x[1]-y[1])%q,f)
                   for x,y in combinations(L,2))
            good+=ok
    assert good==p**3*(p-1)
    print('AFFINE_SPECTRA_ENUMERATION_OK',p,good)
