#!/usr/bin/env python3
"""Exact finite-field checks for a characteristic-three Ciani quartic family.

Run: python3 check.py
Uses only the Python standard library. The proof for all q is in RESULT.md;
finite enumeration is a supplementary consistency check, not a proof for all q.
"""
from collections import Counter
from itertools import product

class Field:
    def __init__(self, modulus):
        # Monic irreducible polynomial over F_3, coefficients low to high.
        self.mod = modulus
        self.d = len(modulus) - 1
        self.q = 3 ** self.d
        self.digits = [self.unpack(i) for i in range(self.q)]
        self.add_table = [[self.pack([(a+b)%3 for a,b in zip(x,y)])
                           for y in self.digits] for x in self.digits]
        self.mult_table = [[self._mul_raw(x,y) for y in self.digits]
                           for x in self.digits]
    def unpack(self,n):
        out=[]
        for _ in range(self.d):
            out.append(n%3);n//=3
        return out
    def pack(self,cs):
        return sum((c%3)*3**i for i,c in enumerate(cs))
    def _mul_raw(self,a,b):
        p=[0]*(2*self.d-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):p[i+j]=(p[i+j]+x*y)%3
        for k in range(len(p)-1,self.d-1,-1):
            h=p[k]
            for i in range(self.d):p[k-self.d+i]=(p[k-self.d+i]-h*self.mod[i])%3
        return self.pack(p[:self.d])
    def add(self,*a):
        out=0
        for x in a:out=self.add_table[out][x]
        return out
    def mul(self,*a):
        out=1
        for x in a:out=self.mult_table[out][x]
        return out
    def neg(self,a):return self.mul(2,a)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def pow(self,x,n):
        out=1
        while n:
            if n&1:out=self.mul(out,x)
            x=self.mul(x,x);n//=2
        return out
    def smooth(self,r,s,t):
        if any(x in (1,2) for x in (r,s,t)):return False
        delta=self.sub(self.add(self.mul(r,r),self.mul(s,s),self.mul(t,t)),
                       self.add(self.mul(r,s,t),1))
        return delta!=0
    def H(self,r,s,t):
        return tuple(self.mul(2,x) for x in (
            self.add(s,self.mul(r,t)),
            self.add(t,self.mul(r,s)),
            self.add(r,self.mul(s,t))))
    def F(self,r,s,t,x,y,z):
        x2=self.mul(x,x);y2=self.mul(y,y);z2=self.mul(z,z)
        return self.add(self.mul(x2,x2),self.mul(y2,y2),self.mul(z2,z2),
                        self.mul(r,x2,y2),self.mul(s,y2,z2),self.mul(t,z2,x2))
    def count_curve(self,r,s,t):
        return sum(self.F(r,s,t,x,y,1)==0 for x,y in product(range(self.q),repeat=2)) + \
               sum(self.F(r,s,t,x,1,0)==0 for x in range(self.q)) + \
               int(self.F(r,s,t,1,0,0)==0)
    def enumerate(self):
        counts=Counter()
        for r,s,t in product(range(self.q),repeat=3):
            if not self.smooth(r,s,t):continue
            H=self.H(r,s,t)
            f=sum(h!=0 for h in H)
            counts[f]+=1
            assert (f==0)==(r==s==t==0)
            if f==1:assert sum(x!=0 for x in (r,s,t))==1
        q=self.q
        expected={0:1,1:3*(q-3),2:3*(q-3)*(q-5),
                  3:(q-3)*(q*q-7*q+18)}
        assert dict(counts)=={k:v for k,v in expected.items() if v}
        assert sum(counts.values())==q**3-7*q**2+18*q-17
        print('PARAMETER_CENSUS_OK',q,dict(sorted(counts.items())))

def verify_coefficient_extraction(K):
    # Full expansion of F^2, extract three Cartier diagonal terms.
    mon=[(4,0,0),(0,4,0),(0,0,4),(2,2,0),(0,2,2),(2,0,2)]
    for r,s,t in product(range(K.q),repeat=3):
        coefficients=[1,1,1,r,s,t]
        pol={}
        for i,mi in enumerate(mon):
            for j,mj in enumerate(mon):
                ex=tuple(mi[k]+mj[k] for k in range(3))
                pol[ex]=K.add(pol.get(ex,0),K.mul(coefficients[i],coefficients[j]))
        assert tuple(pol.get(ex,0) for ex in ((4,2,2),(2,4,2),(2,2,4)))==K.H(r,s,t)
        assert all(pol.get(ex,0)==0 for ex in ((5,1,2),(1,5,2),(2,5,1)))
    print('CARTIER_COEFFICIENTS_OK',K.q)

def check_samples(K):
    u=3 # root of u^2+1 in F9
    r=u;t=K.add(u,1);s=K.neg(K.mul(r,t))
    samples=[(0,0,0),(u,0,0),(r,s,t),(u,u,u)]
    for want,(r,s,t) in enumerate(samples):
        assert K.smooth(r,s,t)
        H=K.H(r,s,t)
        assert sum(h!=0 for h in H)==want
        point_count=K.count_curve(r,s,t)
        trace=K.add(*(K.mul(h,K.pow(h,3)) for h in H))
        predicted=K.sub(1,trace)
        assert point_count%3==predicted%3
        print('WITNESS_OK',want,(r,s,t),'points_over_F9',point_count)

if __name__=='__main__':
    K3=Field([0,1]);K3.enumerate()
    K9=Field([1,0,1]);K9.enumerate();verify_coefficient_extraction(K9);check_samples(K9)
    K27=Field([1,2,0,1]);K27.enumerate()
    print('ALL_CHECKS_OK')
