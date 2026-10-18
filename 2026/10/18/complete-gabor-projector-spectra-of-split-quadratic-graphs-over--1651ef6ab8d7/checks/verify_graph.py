#!/usr/bin/env python3
"""Independent small-field enumeration of Gabor ambiguity spectra for split quadratic graphs."""
from itertools import product
from collections import Counter
import numpy as np

def finite_field(q):
    if q==4:
        add=lambda x,y:x^y
        def mul(x,y):
            p=0
            for k in range(2):
                if (y>>k)&1:p ^= x<<k
            if p&8:p ^= 0b1110  # not needed for products of degree<=2
            if p&4:p ^= 0b111  # reduce t^2=t+1
            return p
        def phase(x):
            xx=mul(x,x)
            assert add(x,xx) in (0,1)
            return add(x,xx)
        prime=2
    else:
        assert q in (2,3,5)
        add=lambda x,y:(x+y)%q
        mul=lambda x,y:(x*y)%q
        phase=lambda x:x
        prime=q
    return add,mul,phase,prime

def enumerate_one(q,r):
    add,mul,phase,p=finite_field(q)
    coords=list(product(range(q),repeat=2*r+1))
    D=len(coords)
    dot=lambda x,y:sum(0 for _ in []) if False else _dot(x,y)
    def _dot(x,y):
        s=0
        for a,b in zip(x,y):s=add(s,mul(a,b))
        return s
    C=[]
    for t in coords:
        x,y,z=t[:r],t[r:2*r],t[-1]
        if z==dot(x,y):C.append(t)
    assert len(C)==q**(2*r)
    zeta=np.exp(2j*np.pi/p)
    phase_matrix=np.empty((D,len(C)),dtype=np.complex128)
    for i,eta in enumerate(coords):
        for j,t in enumerate(C):phase_matrix[i,j]=zeta**phase(dot(eta,t))
    pair_to_c_index={t:j for j,t in enumerate(C)}
    values=[]
    spec=Counter()
    for h in coords:
        # A(h,eta)=|C|^{-1} sum_{t in C, t+h in C} psi(eta dot t)
        indices=[]
        for j,t in enumerate(C):
            u=tuple(add(a,b) for a,b in zip(t,h))
            if u in pair_to_c_index:indices.append(j)
        A=phase_matrix[:,indices].sum(axis=1)/len(C) if indices else np.zeros(D,dtype=complex)
        for av in abs(A):
            possible=[0.0,1.0,1/q,q**(-r),q**(-r-0.5)]
            v=min(possible,key=lambda z:abs(z-av))
            if abs(v-av)>1e-8:raise AssertionError((q,r,h,av,possible))
            spec[v]+=1
    c0=q**(2*r-1)+(q-1)*q**(r-1)
    expected=Counter()
    expected[1.0]+=1
    expected[1/q]+=q*q*(q**(2*r)-1)
    if p==2:
        expected[q**(-r)]+=(q-1)*q**(4*r)
    else:
        expected[q**(-r)]+=(q-1)*q**(2*r)*c0
        expected[q**(-r-0.5)]+=(q-1)*q**(2*r+1)*(q**(2*r)-c0)
    for k,cnt in expected.items():
        assert spec[k]==cnt,(q,r,'expected nonzero count mismatch',k,spec,expected)
    assert sum(spec.values())==D**2,(q,r,'total wrong')
    assert sum(expected.values())<=D**2
    expected[0.0]=D**2-sum(expected.values())
    assert spec==expected,(q,r,'full spectrum mismatch',spec,expected)
    print(f'field={q} r={r} D={D} |C|={len(C)} Gram-rank={D*D-spec[0.0]} spectrum(ambiguity absolute values)={sorted(spec.items())}',flush=True)

if __name__=='__main__':
    for q,r in [(2,1),(3,1),(4,1),(5,1),(2,2),(3,2)]:enumerate_one(q,r)
    print('ALL_DIRECT_ENUMERATIONS_PASS')
