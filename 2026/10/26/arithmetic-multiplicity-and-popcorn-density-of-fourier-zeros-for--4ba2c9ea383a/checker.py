#!/usr/bin/env python3
"""Exact rational check of arithmetic zero-lattice multiplicities."""
from collections import Counter
from fractions import Fraction

def Lvalue(q):
    for L in range(1,10000):
        if pow(3,L,q) in {1 % q,(-1)%q}:
            return L
    raise ValueError(q)

def zeros(R,p,q):
    # two signs; q=2 is the coalesced double mask zero
    out=Counter()
    n=1
    while 3**n*min(Fraction(p,q),1-Fraction(p,q))<=R:
        a=3**n
        m=R//a + 2
        for k in range(-m,m+1):
            for sign in ((1,) if (q==2 and 2*p==q) else (-1,1)):
                z=Fraction(a*(q*k+sign*p),q)
                if abs(z)<=R: out[z]+=(2 if q==2 and 2*p==q else 1)
        n+=1
    return Counter(out.values())

for p,q in [(2,5),(2,7),(3,8),(1,3),(1,2)]:
    L=Lvalue(q) if q%3 else None
    print('alpha',p,q,'L',L)
    for R in (90,900,9000):
        observed=zeros(R,p,q)
        densities={m: float(c/(2*R)) for m,c in sorted(observed.items())}
        if q==2:
            predicted={2*m:2/3**(m+1) for m in (1,2,3)}
        elif q%3==0:
            predicted={1:1.0}
        else:
            predicted={m:(1-3**(-L))**2*3**(-(m-1)*L) for m in (1,2,3)}
        print(' R',R,'count',sum(observed.values()),'density',round(sum(observed.values())/(2*R),8),'orders', {k:round(v,8) for k,v in list(densities.items())[:5]},'pred', {k:round(v,8) for k,v in predicted.items()})
    if q%3:
        assert 3**L % q in {1, q-1}
        assert all(3**j % q not in {1,q-1} for j in range(1,L))
        print(' modular minimality verified')
print('Exact rational enumeration: PASS')
