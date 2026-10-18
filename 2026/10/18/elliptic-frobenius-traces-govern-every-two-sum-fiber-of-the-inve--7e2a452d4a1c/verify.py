#!/usr/bin/env python3
"""Exact-arithmetic verification of reciprocal-square curve convolution identities."""
from collections import Counter


def prime_fields():
    return [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


def test_prime(p):
    chi = lambda v: 0 if v % p == 0 else (1 if pow(v % p, (p - 1)//2, p) == 1 else -1)
    r=Counter()
    for a in range(1,p):
        for b in range(1,p):
            r[((a+b)%p,(pow(a,-2,p)+pow(b,-2,p))%p)]+=1
    S=sum(chi((1-4*z)*(1-4*z*z)) for z in range(p))
    predicted=(p-1)*(3*p-10-2*chi(-1)-2*chi(-3)+S)
    E=sum(z*z for z in r.values())
    assert E==predicted,(p,E,predicted)
    N3=(p-1) if chi(3)==1 else 0
    N1=(p-1)-N3
    N4=(E-2*(p-1)**2+N1-3*N3)//8
    N2=((p-1)**2-N1-3*N3-4*N4)//2
    N0=p*p-N1-N2-N3-N4
    obs=Counter(r.values()); obs[0]=p*p-len(r)
    assert {j:obs[j] for j in range(5)}==dict(enumerate((N0,N1,N2,N3,N4))), (p,obs)
    print(f'q={p}: E={E}, a_q={-S}, multiplicities={[obs[i] for i in range(5)]}')


class Fp2:
    def __init__(self,p):
        self.p=p
        self.d=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
        self.zero=(0,0)
        self.one=(1,0)
        self.elems=[(a,b) for a in range(p) for b in range(p)]
        self.nonzero=[v for v in self.elems if v!=self.zero]
    def add(self,x,y):return ((x[0]+y[0])%self.p,(x[1]+y[1])%self.p)
    def neg(self,x):return ((-x[0])%self.p,(-x[1])%self.p)
    def sub(self,x,y):return self.add(x,self.neg(y))
    def mul(self,x,y):return ((x[0]*y[0]+self.d*x[1]*y[1])%self.p,(x[0]*y[1]+x[1]*y[0])%self.p)
    def pow(self,x,n):
        if n<0:return self.pow(self.inv(x),-n)
        res=self.one
        while n:
            if n&1:res=self.mul(res,x)
            x=self.mul(x,x);n//=2
        return res
    def inv(self,x):
        assert x!=self.zero
        D=pow((x[0]*x[0]-self.d*x[1]*x[1])%self.p,-1,self.p)
        return ((x[0]*D)%self.p,(-x[1]*D)%self.p)
    def smul(self,n,x):return ((n*x[0])%self.p,(n*x[1])%self.p)
    def chi(self,x):
        if x==self.zero:return 0
        return 1 if self.pow(x,(self.p*self.p-1)//2)==self.one else -1
    def calc(self):
        p=self.p;q=p*p
        chi=self.chi
        S=sum(chi(self.mul(self.sub(self.one,self.smul(4,z)),self.sub(self.one,self.smul(4,self.mul(z,z))))) for z in self.elems)
        C=[(u,self.inv(self.mul(u,u))) for u in self.nonzero]
        r=Counter()
        for a,a2 in C:
            for b,b2 in C:
                r[(self.add(a,b),self.add(a2,b2))]+=1
        E=sum(v*v for v in r.values())
        predicted=(q-1)*(3*q-10-2*chi(self.smul(-1,self.one))-2*chi(self.smul(-3,self.one))+S)
        assert E==predicted,(q,E,predicted)
        N3=(q-1) if chi(self.smul(3,self.one))==1 else 0
        N1=(q-1)-N3
        N4=(E-2*(q-1)**2+N1-3*N3)//8
        N2=((q-1)**2-N1-3*N3-4*N4)//2
        N0=q*q-N1-N2-N3-N4
        obs=Counter(r.values());obs[0]=q*q-len(r)
        assert {j:obs[j] for j in range(5)}==dict(enumerate((N0,N1,N2,N3,N4))), (q,obs)
        print(f'q={q}: E={E}, a_q={-S}, multiplicities={[obs[i] for i in range(5)]}')
        return -S


if __name__=='__main__':
    for p in prime_fields():test_prime(p)
    for p in [5,7,11,13]:
        Fp2(p).calc()
    print('VERIFICATION_OK')
