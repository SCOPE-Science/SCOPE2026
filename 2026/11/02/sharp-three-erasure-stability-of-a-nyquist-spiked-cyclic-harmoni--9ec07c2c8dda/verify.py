#!/usr/bin/env python3
"""Independent finite checks for a three-character cyclic Fourier frame."""
import cmath
import itertools
import math
import numpy as np

def theoretical(m):
    s=1+2*math.cos(2*math.pi/m)
    return (9+math.sqrt(9+8*s*s))/2

def erasure_gram(n, triple):
    z=cmath.exp(2j*math.pi/n)
    vec=np.array([[1,z**k,(-1)**k] for k in triple],dtype=complex)
    return vec@vec.conjugate().T

def sylvester(d,c0_squared):
    a0,a1,a2=d-4,d-3,d-2
    return (a0, a0*a1-c0_squared, a0*(a1*a2-2)-c0_squared*a2)

assert sylvester(6,2)==(2,4,12)
assert sylvester(6,4)==(2,2,4)
assert sylvester(7,8)==(3,4,14)

checks=0
for m in range(3,22):
    n=2*m
    lam=theoretical(m)
    best=-1.0
    winners=[]
    upper_masks=[]
    for triple in itertools.combinations(range(n),3):
        H=erasure_gram(n,triple)
        eig=np.linalg.eigvalsh(H)
        L=float(eig[-1])
        if m<=8 and abs(eig[0])<1e-8:
            upper_masks.append(triple)
        if L>best+1e-9:
            best=L;winners=[triple]
        elif abs(L-best)<1e-9:
            winners.append(triple)
        checks+=1
    expected={tuple(sorted({t%n,(t+2)%n,(t+4)%n})) for t in range(n)}
    assert abs(best-lam)<1e-9,(m,best,lam)
    assert set(winners)==expected,(m,len(winners),len(expected),set(winners)^expected)
    assert len(winners)==(2 if m==3 else n)
    if m<=8:
        expected_upper={t for t in itertools.combinations(range(n),3)
                        if len({k%2 for k in t})==1}
        assert set(upper_masks)==expected_upper,(m,len(upper_masks))
    if m==3: assert abs(best-n)<1e-9
    else: assert best<n
    print('m',m,'N',n,'max',format(lam,'.12f'),'worst_masks',len(winners))

print('VERIFY_OK',checks,'mask_spectra')
