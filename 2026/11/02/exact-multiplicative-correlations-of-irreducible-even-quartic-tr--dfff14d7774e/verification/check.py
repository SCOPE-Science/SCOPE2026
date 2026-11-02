#!/usr/bin/env python3
"""Independent finite-field and polynomial-arithmetic checks for simultaneous quartic irreducibility."""
from itertools import product

class Field:
    def __init__(self, p, ext=1):
        self.p, self.ext = p, ext
        self.q = p ** ext
        if ext == 2:
            self.delta = next(z for z in range(2, p) if pow(z,(p-1)//2,p)==p-1)
        elif ext != 1:
            raise ValueError('only prime and quadratic extension fields')
    def a(self,x,y):return ((x+y)%self.p if self.ext==1 else (((x%self.p+y%self.p)%self.p) + self.p*((x//self.p+y//self.p)%self.p)))
    def n(self,x):return (-x)%self.p if self.ext==1 else (-x%self.p)+self.p*((-(x//self.p))%self.p)
    def s(self,x,y):return self.a(x,self.n(y))
    def m(self,x,y):
        p=self.p
        if self.ext==1:return x*y%p
        a,b=x%p,x//p; c,d=y%p,y//p
        return ((a*c+self.delta*b*d)%p)+p*((a*d+b*c)%p)
    def pw(self,x,n):
        y=1
        while n:
            if n&1:y=self.m(y,x)
            x=self.m(x,x);n//=2
        return y
    def inv(self,x):
        if not x:raise ZeroDivisionError
        return self.pw(x,self.q-2)
    def chi(self,x):
        if not x:return 0
        return 1 if self.pw(x,(self.q-1)//2)==1 else -1
    def polynomial_trim(self,v):
        v=list(v)
        while v and not v[-1]:v.pop()
        return v
    def prem(self,v,w):
        v=self.polynomial_trim(v);w=self.polynomial_trim(w)
        if not w:raise ZeroDivisionError
        leadinv=self.inv(w[-1]);d=len(w)-1
        while len(v)>d:
            co=self.m(v[-1],leadinv);start=len(v)-d-1
            for j,t in enumerate(w):v[start+j]=self.s(v[start+j],self.m(co,t))
            v=self.polynomial_trim(v)
        return v
    def pmul(self,v,w):
        out=[0]*(len(v)+len(w)-1)
        for i,a in enumerate(v):
            for j,b in enumerate(w):out[i+j]=self.a(out[i+j],self.m(a,b))
        return self.polynomial_trim(out)
    def ppowmod(self,v,n,f):
        o=[1]
        while n:
            if n&1:o=self.prem(self.pmul(o,v),f)
            v=self.prem(self.pmul(v,v),f);n//=2
        return o
    def gcd(self,v,w):
        while w:v,w=w,self.prem(v,w)
        return v
    def irreducible_even_quartic(self,a,b):
        f=[b,0,a,0,1]
        pol=self.ppowmod([0,1],self.q*self.q,f)
        pol=self.polynomial_trim([self.s(pol[i] if i<len(pol) else 0, 1 if i==1 else 0) for i in range(max(len(pol),2))])
        return len(self.gcd(f,pol))==1

def verify(p,ext):
    F=Field(p,ext);q=F.q
    squares=[u for u in range(1,q) if F.chi(u)==1]
    nonsquares=[b for b in range(1,q) if F.chi(b)==-1]
    checks=0;independent=0
    for u in range(1,q):
        elliptic_trace=-sum(F.chi(F.m(F.m(x,F.s(1,x)),F.s(1,F.m(u,x)))) for x in range(q)) if u!=1 else None
        expected=(q+1+elliptic_trace)//4 if u!=1 and F.chi(u)==1 else ((q+1)//2 if u==1 else 0)
        if u!=1 and F.chi(u)==1:assert (q+1+elliptic_trace)%4==0
        for b in range(1,q):
            exp=expected if F.chi(b)==-1 else 0
            count=0
            for a in range(q):
                f=F.irreducible_even_quartic(a,b)
                g=F.irreducible_even_quartic(a,F.m(u,b))
                cp=(F.chi(b)==-1 and F.chi(F.s(F.m(a,a),F.m(4%p,b)))==-1)
                cq=(F.chi(F.m(u,b))==-1 and F.chi(F.s(F.m(a,a),F.m(4%p,F.m(u,b))))==-1)
                assert f==cp and g==cq,('Capelli',p,ext,u,b,a)
                count+=f and g;independent+=2
            assert count==exp,('count',p,ext,u,b,count,exp)
            checks+=1
    return (q,checks,independent)

if __name__=='__main__':
    rs=[verify(p,1) for p in (3,5,7,11,13,17,19,23,29)]
    rs.extend([verify(3,2),verify(5,2)])
    print('VERIFY_OK fields',rs,'total_pairs',sum(r[1] for r in rs),'irreducibility_checks',sum(r[2] for r in rs))
