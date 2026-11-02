#!/usr/bin/env python3
"""Exact finite-field and polynomial checks for five Cartier rank-drop divisors."""
from collections import Counter
from itertools import combinations, product

# Polynomials over F_2 in one indeterminate, encoded as bit masks.
def pmul(a, b):
    z = 0
    while b:
        if b & 1: z ^= a
        a <<= 1; b >>= 1
    return z

def pdiv_possible(a,b):
    while a and a.bit_length()>=b.bit_length():
        a ^= b<<(a.bit_length()-b.bit_length())
    return a==0

def pdiv(a,b):
    q=0
    while a and a.bit_length() >= b.bit_length():
        k=a.bit_length()-b.bit_length()
        q ^= 1 << k; a ^= b << k
    assert a == 0
    return q

x=2
Q=7  # t^2+t+1
fractions=[('infinity',3,1), ('zero',x,3), ('one',1,x), ('lambda',4,1)]
for (name1,n1,d1),(name2,n2,d2) in combinations(fractions,2):
    eliminating=pmul(n1,d2) ^ pmul(n2,d1)
    factor=pdiv(eliminating,Q)
    while factor and factor%2==0: factor >>= 1
    while factor not in (0,1) and pdiv_possible(factor,3):
        factor=pdiv(factor,3)
    assert factor==1, (name1,name2,eliminating)
for name,n,d in fractions:
    eliminating=pmul(n,n)^pmul(x,pmul(d,d))
    factor=pdiv(eliminating,Q)
    while factor and factor%2==0: factor >>= 1
    while factor not in (0,1) and pdiv_possible(factor,3): factor=pdiv(factor,3)
    assert factor==1, ('mu',name)
print('INTERSECTIONS_OK: all ten pairwise intersections have only roots of t^2+t+1 on the smooth parameter locus')

# Arithmetic in F_{2^m}, with standard irreducible modulus.
class Field:
    def __init__(self,m,poly): self.m=m;self.poly=poly;self.q=1<<m
    def mul(self,a,b):
        z=0
        while b:
            if b&1: z^=a
            b>>=1; a<<=1
            if a&self.q: a^=self.poly
        return z
    def pow(self,a,n):
        z=1
        while n:
            if n&1: z=self.mul(z,a)
            a=self.mul(a,a);n>>=1
        return z
    def inv(self,a): assert a;return self.pow(a,self.q-2)
    def root(self,a): return self.pow(a,self.q//2)
    def rank(self,cols):
        vectors=[list(col) for col in cols]; r=0;dim=len(vectors[0]); k=len(vectors)
        for i in range(dim):
            pivot=next((j for j in range(r,k) if vectors[j][i]),None)
            if pivot is None:continue
            vectors[r],vectors[pivot]=vectors[pivot],vectors[r]
            t=self.inv(vectors[r][i]);vectors[r]=[self.mul(t,v) for v in vectors[r]]
            for j in range(k):
                if j!=r and vectors[j][i]:
                    c=vectors[j][i]
                    vectors[j]=[u^self.mul(c,v) for u,v in zip(vectors[j],vectors[r])]
            r+=1
        return r
    def cartier(self,vector,s1,s3):
        a,b,c=map(self.root,vector)
        return (c,self.mul(self.root(s3),a),self.mul(self.root(s1),a))

def check_field(m,modulus):
    F=Field(m,modulus)
    values=[v for v in range(2,F.q)]
    spectra=Counter()
    for l in values:
        for u in values:
            if l==u:continue
            a=[0,1,l,u]
            loci=[1^l^u, F.mul(l,u)^l^u, F.mul(l,u)^1, F.mul(l,l)^u, l^F.mul(u,u)]
            zeros=[i for i,z in enumerate(loci) if z==0]
            if zeros: assert len(zeros) in (1,5)
            roots_by_index=[]
            for i in range(5):
                if i==0: roots=a
                else:
                    v=a[i-1]
                    roots=[0]+[F.inv(v^a[j]) for j in range(4) if j!=i-1]
                s1=0;s3=0
                for r in roots: s1^=r
                for i1,i2,i3 in combinations(range(4),3):
                    s3 ^= F.mul(F.mul(roots[i1],roots[i2]),roots[i3])
                assert (s1==0)==(loci[i]==0)
                assert s1 or s3, (l,u,roots)
                iterated=[(1,0,0),(0,1,0),(0,0,1)]
                assert F.rank([F.cartier(z,s1,s3) for z in iterated])==2
                for _ in range(6): iterated=[F.cartier(z,s1,s3) for z in iterated]
                stable_rank=F.rank(iterated)
                assert stable_rank==(0 if s1==0 else 2)
            f=40-2*len(zeros)
            spectra[f]+=1
    if m==3:assert spectra=={38:30},spectra
    if m==4:assert spectra=={40:120,38:60,30:2},spectra
    print(f'GF(2^{m})_OK: marked smooth family p-rank spectrum {dict(sorted(spectra.items()))}; five quotient Cartier iterates checked')
    if m==4:
        roots=[v for v in values if F.mul(v,v)^v^1==0]
        assert len(roots)==2
        for v in roots:
            mu=v^1
            slopes=[1,F.mul(mu^1,F.inv(v^1)),F.mul(mu,F.inv(v)),0]
            assert len(set(slopes))==4
            assert set(slopes)=={0,1,*roots}
        print('TANGENTS_OK: at both F4 parameters, the five loci have all five distinct P1(F4) tangent directions')

weights=set()
for v in product(range(3),repeat=5):
    if sum(v)%3 or not any(v):continue
    w=tuple((-t)%3 for t in v)
    weights.add(min(v,w))
d=Counter(sum(z!=0 for z in v) for v in weights)
assert d=={2:10,3:10,4:15,5:5},d
assert sum((r-2)*k for r,k in d.items())==55
print('CHARACTERS_OK: support classes 2:10, 3:10, 4:15, 5:5; positive-genus factor dimensions total 55')
check_field(3,0b1011)
check_field(4,0b10011)
print('VERIFY_OK')
