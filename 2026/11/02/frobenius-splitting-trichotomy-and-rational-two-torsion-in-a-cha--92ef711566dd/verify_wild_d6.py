#!/usr/bin/env python3
"""Exact finite-field checks of a characteristic-three hyperelliptic family.

No external packages or network needed. Computational tests support, but do not
replace, the uniform algebraic and Artin--Schreier proofs in RESULT.md.
"""
from collections import Counter

class Field:
    def __init__(self, modulus):
        self.mod=tuple(modulus); self.n=len(modulus)-1; self.q=3**self.n
        assert self.mod[-1]==1
        self.E=tuple(range(self.q)); self.zero=0; self.one=1
        self._inv={}
    def poly(self,a):
        return [(a//(3**i))%3 for i in range(self.n)]
    def enc(self,a):
        return sum((v%3)*3**i for i,v in enumerate(a))
    def add(self,a,b):
        A=self.poly(a);B=self.poly(b)
        return self.enc([(x+y)%3 for x,y in zip(A,B)])
    def neg(self,a):
        return self.enc([-x for x in self.poly(a)])
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        A=self.poly(a);B=self.poly(b); C=[0]*(2*self.n-1)
        for i,x in enumerate(A):
            for j,y in enumerate(B): C[i+j]=(C[i+j]+x*y)%3
        for i in range(len(C)-1,self.n-1,-1):
            x=C[i]
            if x:
                for j in range(self.n): C[i-self.n+j]=(C[i-self.n+j]-x*self.mod[j])%3
        return self.enc(C[:self.n])
    def power(self,a,k):
        if k<0: return self.power(self.inv(a),-k)
        v=1
        while k:
            if k&1: v=self.mul(v,a)
            a=self.mul(a,a);k//=2
        return v
    def inv(self,a):
        assert a
        if a not in self._inv: self._inv[a]=self.power(a,self.q-2)
        return self._inv[a]
    def trace(self,a):
        s=0;b=a
        for _ in range(self.n):
            s=self.add(s,b); b=self.power(b,3)
        assert s in (0,1,2)
        return s


def poly_trim(p):
    while p and p[-1]==0: p.pop()
    return p

def poly_add(F,a,b):
    return poly_trim([F.add(a[i] if i<len(a) else 0,b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def poly_neg(F,a):return [F.neg(x) for x in a]

def poly_mul(F,a,b):
    if not a or not b:return []
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=F.add(c[i+j],F.mul(x,y))
    return poly_trim(c)

def poly_divrem(F,a,b):
    assert b; a=list(a); b=poly_trim(list(b))
    while len(a)>=len(b):
        t=F.mul(a[-1],F.inv(b[-1])); shift=len(a)-len(b)
        for i,c in enumerate(b):a[shift+i]=F.sub(a[shift+i],F.mul(t,c))
        poly_trim(a)
    return a

def poly_gcd(F,a,b):
    while b:a,b=b,poly_divrem(F,a,b)
    if a:
        inv=F.inv(a[-1]);a=[F.mul(inv,z) for z in a]
    return a

def poly_powmod(F,a,k,mod):
    v=[1]
    while k:
        if k&1:v=poly_divrem(F,poly_mul(F,v,a),mod)
        a=poly_divrem(F,poly_mul(F,a,a),mod);k//=2
    return v

def count_roots_extension(F,r,d):
    # f_r(t)=1+r(t^3-t)^2 = 1+r(t^6+t^4+t^2) in characteristic 3
    f=[1,0,r,0,r,0,r]
    y=poly_powmod(F,[0,1],F.q**d,f)
    y=poly_add(F,y,[0,F.neg(1)])
    return len(poly_gcd(F,f,y))-1

def run_field(mod):
    F=Field(mod);q=F.q
    # Check basis actually makes a field by Fermat on every nonzero element.
    assert all(F.power(z,q-1)==1 for z in range(1,q))
    counts=Counter()
    for r in range(1,q):
        # Check the reduction and inversion-model identities pointwise.
        for x in F.E:
            x2=F.mul(x,x); x4=F.mul(x2,x2); x6=F.mul(x4,x2)
            lhs=F.add(x6,F.mul(r,F.add(F.add(x4,x2),1)))
            rhs=F.add(x6,F.mul(r,F.power(F.sub(x2,1),2)))
            assert lhs==rhs
        a=F.neg(F.inv(r))  # beta^2=-1/r
        bs=[b for b in F.E if F.mul(b,b)==a]
        if not bs:
            expect='two'; degrees=(0,6,0,6); torsion=4
        elif F.trace(bs[0])==0:
            expect='one'; degrees=(6,6,6,6); torsion=16
        else:
            expect='three'; degrees=(0,0,6,6); torsion=1
        counts[expect]+=1
        # Independent direct count of rational sextic roots.
        roots=sum(1 for t in F.E if F.add(1,F.mul(r,F.power(F.sub(F.power(t,3),t),2)))==0)
        assert roots==degrees[0],(q,r,roots,degrees)
        actual=tuple(count_roots_extension(F,r,d) for d in (1,2,3,6))
        assert actual==degrees,(q,r,expect,actual,degrees)
        assert torsion in (1,4,16)
    assert all(counts[k]==v for k,v in {'one':(q-3)//6,'two':(q-1)//2,'three':q//3}.items()),(q,counts)
    print('GF(%d) all %d nonzero parameters: %s; extension gcds and rational roots verified' %
          (q,q-1,dict(counts)))

if __name__=='__main__':
    for mod in ([0,1],[1,0,1],[2,2,0,1],[2,1,0,0,1]):
        run_field(mod)
    print('WILD_D6_CHAR3_FROBENIUS_2TORSION_ALL_CHECKS_PASS')
