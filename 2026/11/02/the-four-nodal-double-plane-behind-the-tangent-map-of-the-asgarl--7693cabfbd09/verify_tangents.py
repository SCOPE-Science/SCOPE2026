#!/usr/bin/env python3
"""Exact finite-field checks of tangent-line multiplicities and quartic branch counts."""
from collections import Counter

class Field:
    def __init__(self, p, n=1):
        self.p, self.n, self.q = p, n, p**n
        if n == 2:
            self.d = next(i for i in range(2,p) if pow(i,(p-1)//2,p)==p-1)
        elif n != 1:
            raise ValueError("only degrees 1 and 2")
    def pair(self, x): return (x%self.p, x//self.p) if self.n==2 else (x%self.p, 0)
    def enc(self, x, y=0): return (x%self.p)+self.p*(y%self.p) if self.n==2 else x%self.p
    def add(self, x, y):
        a,b=self.pair(x); c,d=self.pair(y); return self.enc(a+c,b+d)
    def neg(self,x): a,b=self.pair(x); return self.enc(-a,-b)
    def sub(self,x,y): return self.add(x,self.neg(y))
    def mul(self,x,y):
        a,b=self.pair(x); c,d=self.pair(y)
        return self.enc(a*c+(self.d if self.n==2 else 0)*b*d,a*d+b*c)
    def pow(self,x,n):
        z=1
        while n:
            if n&1:z=self.mul(z,x)
            x=self.mul(x,x);n>>=1
        return z
    def inv(self,x):
        if x==0: raise ZeroDivisionError
        return self.pow(x,self.q-2)
    def sum(self,*args):
        z=0
        for x in args:z=self.add(z,x)
        return z
    def prod(self,*args):
        z=1
        for x in args:z=self.mul(z,x)
        return z
    def normal(self, xyz):
        x,y,z=xyz
        for v in xyz:
            if v:
                t=self.inv(v)
                return tuple(self.mul(w,t) for w in xyz)
        raise ValueError

def run(p,n):
    f=Field(p,n); q=f.q
    projective=[(1,y,z) for y in range(q) for z in range(q)] + [(0,1,z) for z in range(q)] + [(0,0,1)]
    A={}
    S0=f.enc(3)
    for x,y,z in projective:
        s=f.sum(x,y,z)
        if not f.prod(x,y,z,s):continue
        if x==y==z:continue
        # Tangent gradient of x^(q-1)+y^(q-1)+z^(q-1)-3s^(q-1).
        invs=f.inv(s)
        g=f.normal(tuple(f.sub(f.mul(S0,invs),f.inv(w)) for w in (x,y,z)))
        A[g]=A.get(g,0)+1
    dist=Counter(A.values()); assert not any(k>2 for k in dist)
    one=(9*q-33) if q%3==1 else (7*q-23)
    two=((q-5)*(q-7)//2) if q%3==1 else ((q-5)**2//2)
    assert dist[1]==one and dist[2]==two,(q,dist,one,two)
    assert one+2*two==(q-1)*(q-2)
    def branch(g):
        a,b,c=g
        e2=f.sum(f.mul(a,b),f.mul(a,c),f.mul(b,c))
        s=f.sum(a,b,c)
        return f.sub(f.mul(e2,e2),f.mul(f.enc(3),f.prod(s,a,b,c)))
    branch_n=sum(branch(g)==0 for g in projective)
    assert branch_n==(2*q-2 if q%3==1 else 4),(q,branch_n)
    print('q=%-3d points=%-4d singleton=%-4d double=%-4d distinct_lines=%-4d branch_points=%-4d' %
          (q,one+2*two,one,two,one+two,branch_n))

if __name__=='__main__':
    for p,n in [(5,1),(7,1),(11,1),(13,1),(17,1),(19,1),(23,1),(31,1),(5,2),(7,2)]:
        run(p,n)
    print('TANGENT_FILLING_DOUBLE_PLANE_CHECKS_PASS')
