#!/usr/bin/env python3
"""Exact finite-field checks for characteristic-two Picard quartic strata.

All arithmetic is in binary polynomial representations of finite fields.
The general mathematical statement is proved symbolically in RESULT.md;
finite enumeration below checks small instances only.
"""
from itertools import product

IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}

class GF2m:
    def __init__(self, m):
        self.m=m; self.q=1<<m; self.pol=IRREDUCIBLE[m]; self.mask=self.q-1
    def mul(self,x,y):
        z=0
        for _ in range(self.m):
            if y&1: z ^= x
            y >>= 1
            x <<= 1
            if x&self.q: x ^= self.pol
        return z & self.mask
    def pow(self,x,n):
        result=1
        while n:
            if n&1:result=self.mul(result,x)
            x=self.mul(x,x); n>>=1
        return result
    def sq(self,x): return self.mul(x,x)
    def sqrt(self,x):return self.pow(x,self.q//2)
    def f(self,x,d,a,b,c):
        x2=self.sq(x); x3=self.mul(x2,x); x4=self.sq(x2)
        return x4 ^ self.mul(d,x3) ^ self.mul(a,x2) ^ self.mul(b,x) ^ c
    def smooth(self,d,a,b,c):
        if d==0:return b!=0
        s=self.sqrt(self.mul(b,self.pow(d,self.q-2)))
        return self.f(s,d,a,b,c)!=0
    def cartier(self,d,b,v):
        u0,u1,u2=map(self.sqrt,v)
        return (u2,self.mul(self.sqrt(b),u0),self.mul(self.sqrt(d),u0))
    def rank(self,vectors):
        if not vectors:return 0
        a=[list(row) for row in zip(*vectors)]; r=0
        for j in range(len(a[0])):
            pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
            if pivot is None: continue
            a[pivot],a[r]=a[r],a[pivot]
            inv=self.pow(a[r][j],self.q-2)
            a[r]=[self.mul(v,inv) for v in a[r]]
            for i in range(len(a)):
                if i!=r and a[i][j]:
                    t=a[i][j]
                    a[i]=[u^self.mul(t,v) for u,v in zip(a[i],a[r])]
            r+=1
        return r
    def cartier_ranks(self,d,b):
        basis=[(1,0,0),(0,1,0),(0,0,1)]
        ans=[]
        for n in range(1,5):
            basis=[self.cartier(d,b,v) for v in basis]
            ans.append(self.rank(basis))
        return ans
    def num_points(self,d,a,b,c):
        counts=[0]*self.q
        for y in range(self.q):counts[self.pow(y,3)] += 1
        return 1+sum(counts[self.f(x,d,a,b,c)] for x in range(self.q))

for m in (1,2,3,4):
    F=GF2m(m); total=ss=rank2=0
    samples={}
    for d,a,b,c in product(range(F.q), repeat=4):
        if not F.smooth(d,a,b,c):continue
        total+=1
        expected_rank=0 if d==0 else 2
        if d==0:ss+=1
        else:rank2+=1
        if (d,b) not in samples:
            observed=F.cartier_ranks(d,b)
            assert observed[0]==2 and observed[3]==expected_rank,(m,d,b,observed)
            samples[d,b]=observed
    q=F.q
    assert (total,ss,rank2)==(q**3*(q-1),q*q*(q-1),q*q*(q-1)**2)
    print(f'GF({q}): total={total} supersingular_marked={ss} rank2_marked={rank2} Cartier_pairs={len(samples)}')

# Illustrative point counts over GF(2), GF(4); in F_2 every x has one y.
f2=GF2m(1); f4=GF2m(2)
for d,a,b,c in ((0,0,1,0),(1,0,0,1)):
    assert f2.smooth(d,a,b,c)
    n1=f2.num_points(d,a,b,c);n2=f4.num_points(d,a,b,c)
    coeff2=(n2-(4+1))//2
    assert n1==3 and (n2-5)%2==0
    assert coeff2%2==d
    print(f'F2 coefficients d,a,b,c={(d,a,b,c)}: N1={n1},N2={n2},L=1+({coeff2})T^2+({2*coeff2})T^4+8T^6')
print('VERIFY_OK')
