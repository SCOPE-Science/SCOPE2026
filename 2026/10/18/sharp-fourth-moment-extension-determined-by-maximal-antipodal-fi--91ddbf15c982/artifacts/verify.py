#!/usr/bin/env python3
"""Exact finite tests of sharp fourth moments for cubic/even finite-field curves.

Uses exact Gaussian-integer coefficients and exact field arithmetic.  Tests are
finite reproducibility checks, not a substitute for the proof over all fields.
"""
from collections import defaultdict
from fractions import Fraction
import random

class Field:
    def __init__(self, p, nonsquare=None):
        self.p=p
        self.nonsquare=nonsquare
        self.q=p if nonsquare is None else p*p
        self.zero=0
        self.one=1
    def parts(self,x):
        return x%self.p, x//self.p
    def add(self,x,y):
        if self.nonsquare is None: return (x+y)%self.p
        a,b=self.parts(x);c,d=self.parts(y)
        return (a+c)%self.p + self.p*((b+d)%self.p)
    def neg(self,x):
        return self.add(0, self.p-x) if self.nonsquare is None else ((-x%self.p)+self.p*((-(x//self.p))%self.p))
    def mul(self,x,y):
        if self.nonsquare is None: return x*y%self.p
        a,b=self.parts(x);c,d=self.parts(y)
        return (a*c+self.nonsquare*b*d)%self.p + self.p*((a*d+b*c)%self.p)
    def power(self,x,n):
        a=self.one
        while n:
            if n&1: a=self.mul(a,x)
            x=self.mul(x,x);n//=2
        return a
    def pair_sum(self, h, a,b):
        return (self.add(a,b), self.add(self.power(a,3),self.power(b,3)), self.add(h[a],h[b]))

def fibers(F,h):
    d=defaultdict(list)
    for a in range(F.q):
        for b in range(F.q):
            d[F.pair_sum(h,a,b)].append((a,b))
    return d

def antipodal_blocks(F,h):
    seen={0}; blocks=defaultdict(list)
    for t in range(1,F.q):
        if t in seen:continue
        u=F.neg(t); assert t!=u
        seen.update([t,u])
        assert h[t]==h[u]
        blocks[h[t]].append((t,u))
    return list(blocks.values())

def norm2(z):
    return int(z.real)**2+int(z.imag)**2

def validate(F,h,seed):
    assert h[0] not in h[1:]
    for x in range(F.q):assert h[x]==h[F.neg(x)]
    blocks=antipodal_blocks(F,h)
    M=max(map(len,blocks))
    fs=fibers(F,h)
    assert sum(map(len,fs.values()))==F.q*F.q
    for key,pairs in fs.items():
        s=key[0]
        if s!=0:
            unord={tuple(sorted(ab)) for ab in pairs}
            assert len(unord)==1,(F.q,key,pairs)
        elif key[2]==F.add(h[0],h[0]):
            assert pairs==[(0,0)]
        else:
            assert len(pairs)==2*next(len(b) for b in blocks if F.add(h[b[0][0]],h[b[0][0]])==key[2])
    rng=random.Random(seed)
    tests=8
    for _ in range(tests):
        f=[complex(rng.randrange(-2,3),rng.randrange(-2,3)) for _ in range(F.q)]
        if not any(f):continue
        q4=sum(norm2(sum(f[a]*f[b] for a,b in pairs)) for pairs in fs.values())
        S=sum(norm2(z) for z in f)
        q0=2*S*S-sum(norm2(z)**2 for z in f)
        corr=0
        for block in blocks:
            z=[f[a]*f[b] for a,b in block]
            corr += 4*(norm2(sum(z))-sum(norm2(v) for v in z))
        assert q4==q0+corr,(F.q,M,q4,q0+corr)
        C=Fraction(2*F.q-1,F.q) if M==1 else Fraction(6*M-3,2*M)
        assert Fraction(q4,S*S)<=C,(F.q,M,q4,S,C)
    # Attain all sharp constants explicitly.
    if M==1: f=[1]*F.q
    else:
        f=[0]*F.q
        target=next(block for block in blocks if len(block)==M)
        for a,b in target:f[a]=f[b]=1
    S=sum(norm2(z) for z in f)
    direct=sum(norm2(sum(f[a]*f[b] for a,b in pairs)) for pairs in fs.values())
    C=Fraction(2*F.q-1,F.q) if M==1 else Fraction(6*M-3,2*M)
    assert Fraction(direct,int(S*S))==C,(F.q,M,direct,S,C)
    if M>=2:
        f[next(x for x in range(F.q) if f[x]!=0)]=-1
        perturbed=sum(norm2(sum(f[a]*f[b] for a,b in pairs)) for pairs in fs.values())
        assert Fraction(perturbed,int(S*S))<C
    return (F.q,M,len(blocks),len(fs),C)

def monomial(F,m):
    return [F.power(x,2*m) for x in range(F.q)]

def partition_h(F, sizes):
    antipodal=[];seen={0}
    for x in range(1,F.q):
        if x in seen:continue
        y=F.neg(x);seen.update((x,y));antipodal.append((x,y))
    assert sum(sizes)==len(antipodal)
    h=[0]*F.q;i=0
    for label,n in enumerate(sizes,1):
        assert label < F.p  # distinct field elements are ordinary integers here
        for x,y in antipodal[i:i+n]:h[x]=h[y]=label
        i+=n
    return h

def main():
    cases=[]
    for p in (5,7,11,13,17,19,23,31):
        F=Field(p)
        for m in (2,3,4,5,6,7,8,9):
            h=monomial(F,m)
            assert max(map(len,antipodal_blocks(F,h)))==__import__('math').gcd(m,(p-1)//2)
            cases.append(validate(F,h,p*100+m))
    # Extension fields, exact arithmetic modulo irreducible X^2 - d.
    for p,d in ((5,2),(7,3)):
        F=Field(p,d)
        for m in (2,3,4,5,6,7):
            h=monomial(F,m)
            assert max(map(len,antipodal_blocks(F,h)))==__import__('math').gcd(m,(F.q-1)//2)
            cases.append(validate(F,h,p*100+m+4000))
    for p,sizes in ((13,[3,2,1]),(17,[4,2,1,1]),(11,[5]),(5,[1,1]),(19,[3,3,2,1])):
        F=Field(p)
        cases.append(validate(F,partition_h(F,sizes),p*1000))
    levels=sorted({str(c[-1]) for c in cases})
    print('VERIFY_OK')
    print('cases:',len(cases),'random_complex_tests:',8*len(cases))
    print('finite_orders:',sorted(set(c[0] for c in cases)))
    print('highest_antipodal_fiber:',max(c[1] for c in cases))
    print('norm4_levels:',levels)
    print('all direct character-orthogonality fiber moments and sharp examples agree')
if __name__=='__main__':main()
