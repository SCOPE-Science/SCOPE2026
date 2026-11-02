#!/usr/bin/env python3
"""Independent finite checks of an affine-monoid centralizer spectrum.

Usage: python verify.py ; requires Python 3.9+ and no packages.
All centralizers are computed from affine composition, not the ideal formula.
"""
from collections import Counter
from itertools import product
from fractions import Fraction

class Ring:
    def __init__(self, p, k, squarezero=False):
        self.p, self.k, self.squarezero = p, k, squarezero
        self.els = list(product(range(p), repeat=k))
        self.zero = (0,) * k
        self.one = (1,) + (0,) * (k - 1)
    def add(self, a, b):
        return tuple((x+y)%self.p for x, y in zip(a,b))
    def mul(self, a, b):
        p,k=self.p,self.k
        out=[0]*k
        if self.squarezero:
            out[0]=a[0]*b[0]%p
            for i in range(1,k):
                out[i]=(a[0]*b[i]+a[i]*b[0])%p
        else:
            for i in range(k):
                for j in range(k-i):
                    out[i+j]+=a[i]*b[j]
            out=[x%p for x in out]
        return tuple(out)
    def sub(self,a,b):
        return tuple((x-y)%self.p for x,y in zip(a,b))

class IntegerModRing:
    def __init__(self,p,k):
        self.p, self.k, self.squarezero = p,k,False
        self.n=p**k
        self.els=list(range(self.n))
        self.zero=0
        self.one=1
    def add(self,a,b): return (a+b)%self.n
    def mul(self,a,b): return (a*b)%self.n
    def sub(self,a,b): return (a-b)%self.n

def verify(p,k,squarezero,integer_mod=False):
    R=IntegerModRing(p,k) if integer_mod else Ring(p,k,squarezero)
    els=R.els
    s=len(els)
    C=Counter()
    for a in els:
        for b in els:
            c=0
            for e in els:
                for f in els:
                    # Affine maps (a,b) and (e,f) commute iff composition constants match.
                    if R.add(R.mul(a,f),b)==R.add(R.mul(e,b),f):
                        c+=1
            C[c]+=1
            u=R.sub(a,R.one)
            ideal={R.add(R.mul(u,x),R.mul(b,y)) for x in els for y in els}
            assert c==s*s//len(ideal), (p,k,squarezero,a,b,c,len(ideal))
    assert sum(C.values())==s*s
    q=p
    if squarezero:
        d=k-1
        expect={s:s*s-q**(2*d),s*s//q**2:(q**d-1)*(q**d-q),s*s//q:(q**d-1)*(q+1),s*s:1}
        # k=2 (d=1) has overlapping centralizer sizes.
        E=Counter()
        for key,value in expect.items(): E[key]+=value
        # Multiplicities in a merged case must be computed from the raw four terms:
        E=Counter()
        for key,value in [(s,s*s-q**(2*d)),(s*s//q**2,(q**d-1)*(q**d-q)),(s*s//q,(q**d-1)*(q+1)),(s*s,1)]:E[key]+=value
        assert C==E, (C,E)
    else:
        E=Counter({q**(k+j):q**(2*(k-j))-q**(2*(k-j-1)) for j in range(k)})
        E[q**(2*k)]+=1
        assert C==E, (C,E)
    prob=Fraction(sum(size*count for size,count in C.items()),s**4)
    if squarezero:
        d=k-1
        exp_prob=Fraction(s*s-q**(2*d),s**3)+Fraction(1,s*s)+Fraction((q**d-1)*(q+1),q*s*s)+Fraction((q**d-1)*(q**d-q),q*q*s*s)
    else:
        exp_prob=Fraction(1,q**k)*(1+Fraction(1,q)-Fraction(1,q**(k+1)))
    assert prob==exp_prob,(prob,exp_prob)
    kind='squarezero' if squarezero else ('integer_mod' if integer_mod else 'chain')
    print('CHECK_OK',kind,'q',p,'k',k,'s',s,'centralizers',sorted(C.items()),'commuting_probability',prob)

if __name__=='__main__':
    for p,k,squarezero in [(2,1,False),(2,2,False),(2,3,False),(2,4,False),(3,2,False),(3,3,False),(2,3,True),(2,4,True),(3,3,True)]:
        verify(p,k,squarezero)
    for p,k in [(2,2),(2,3),(3,2)]: verify(p,k,False,integer_mod=True)
    print('VERIFY_OK')
