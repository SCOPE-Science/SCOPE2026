"""Exact finite-field fiber census for x -> x^q+a*x^2 over F_(q^2).
Python 3 standard library only; self-contained finite-field arithmetic.
"""
from collections import Counter
from math import gcd

class FiniteFieldTower:
    def __init__(self,p,m):
        assert p in (3,5,7,11,13,17,23) and m in (1,2)
        self.p,self.m,self.q=p,m,p**m
        self.delta=next(t for t in range(2,p) if pow(t,(p-1)//2,p)==p-1)
        if m==1:
            self.kmul=lambda a,b:(a*b)%p
            self.kneg=lambda a:(-a)%p
            self.kadd=lambda a,b:(a+b)%p
        else:
            def kmul(a,b):
                s,t=a%p,a//p;u,v=b%p,b//p
                return (s*u+self.delta*t*v)%p+p*((s*v+t*u)%p)
            self.kmul=kmul
            self.kneg=lambda a:(-a%p)+p*((-(a//p))%p)
            self.kadd=lambda a,b:(a%p+b%p)%p+p*((a//p+b//p)%p)
        self.d=next(v for v in range(2,self.q) if self.kpow(v,(self.q-1)//2)!=1)
    def kpow(self,a,n):
        v=1
        while n:
            if n&1:v=self.kmul(v,a)
            a=self.kmul(a,a);n//=2
        return v
    def add(self,x,y):
        q=self.q
        return self.kadd(x%q,y%q)+q*self.kadd(x//q,y//q)
    def mul(self,x,y):
        q=self.q
        s,t=x%q,x//q;u,v=y%q,y//q
        return self.kadd(self.kmul(s,u),self.kmul(self.d,self.kmul(t,v)))+q*self.kadd(self.kmul(s,v),self.kmul(t,u))
    def frob(self,x):
        q=self.q
        return x%q+q*self.kneg(x//q)
    def pow(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n//=2
        return z

def expected(q,cube):
    g=gcd(3,q+1)
    if g==1 or cube:
        return (3*(q*q-1)//8,(2*q*q+q+5-2*g)//6,(q*q-2*q-3+4*g)//4,(q+1-2*g)//2,(q*q-4*q-5+8*g)//24)
    assert g==3
    return (3*(q*q-1)//8,(2*q*q+q+5)//6,(q*q-2*q-3)//4,(q+1)//2,(q*q-4*q-5)//24)

def check(p,m,limit=None):
    f=FiniteFieldTower(p,m);q=f.q;n=q*q
    if limit is None: aa=range(1,n)
    else:
        aa=[1]+[a for a in range(2,n) if f.pow(a,(n-1)//3)!=1][:limit] if gcd(3,q+1)==3 else list(range(1,min(n,limit+1)))
    squares=[f.mul(x,x) for x in range(n)]
    qfrobs=[f.frob(x) for x in range(n)]
    profiles=Counter()
    for a in aa:
        r=Counter(f.add(qfrobs[x],f.mul(a,squares[x])) for x in range(n))
        got=tuple(sum(1 for j in range(n) if r[j]==k) for k in range(5))
        cube=(gcd(3,q+1)==1 or f.pow(a,(n-1)//3)==1)
        want=expected(q,cube)
        assert got==want,(q,a,got,want)
        profiles['cube' if cube else 'noncube']+=1
    return len(aa),profiles

if __name__=='__main__':
    total=0
    for p,m,limit in [(3,1,None),(5,1,None),(7,1,None),(11,1,None),(13,1,None),(17,1,18),(3,2,None),(5,2,14),(7,2,5),(23,1,6)]:
        cases,profiles=check(p,m,limit)
        total+=cases
        print('PASS q=',p**m,'coefficients=',cases,'classes=',dict(profiles))
    print('VERIFY_OK coefficients=',total,'all_target_fibers=PASS')
