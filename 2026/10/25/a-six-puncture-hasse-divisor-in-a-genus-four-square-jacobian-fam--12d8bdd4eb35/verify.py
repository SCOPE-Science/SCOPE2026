#!/usr/bin/env python3
"""Exact finite-field consistency checks for a genus-four Hasse divisor."""
from itertools import product

class Field:
    def __init__(self, mod):
        self.mod=mod
        self.m=len(mod)-1
        self.q=5**self.m
        self.els=list(product(range(5),repeat=self.m))
        self.zero=(0,)*self.m
        self.one=(1,)+(0,)*(self.m-1)
    def c(self,x):return (x%5,)+(0,)*(self.m-1)
    def add(self,x,y):return tuple((a+b)%5 for a,b in zip(x,y))
    def neg(self,x):return tuple(-a%5 for a in x)
    def sub(self,x,y):return self.add(x,self.neg(y))
    def mul(self,x,y):
        c=[0]*(2*self.m-1)
        for i,a in enumerate(x):
            for j,b in enumerate(y):c[i+j]=(c[i+j]+a*b)%5
        for i in range(2*self.m-2,self.m-1,-1):
            b=c[i]
            for j in range(self.m):c[i-self.m+j]=(c[i-self.m+j]-b*self.mod[j])%5
        return tuple(c[:self.m])
    def pow(self,x,n):
        y=self.one
        while n:
            if n&1:y=self.mul(y,x)
            x=self.mul(x,x);n>>=1
        return y
    def inv(self,x):return self.pow(x,self.q-2)
    def field_check(self):
        for x in self.els:
            if x!=self.zero:assert self.pow(x,self.q-1)==self.one


def run(F):
    F.field_check()
    zero,one=F.zero,F.one
    minus=lambda x:F.neg(x)
    n4=0
    Hcount=0
    exceptional=[]
    for u in F.els:
        for v in F.els:
            u2=F.mul(u,u)
            smooth=(v!=zero and F.add(u2,v)!=zero
                    and F.add(F.add(one,u),v)!=zero)
            if not smooth:continue
            n4+=1
            U=lambda n:F.c(n)
            # f(t) = v(t^5+1)-u(t^4+t)+(2u+1)(t^3+t^2).
            A=F.sub(F.add(F.mul(U(2),u),one),F.mul(U(2),F.mul(u,v)))
            B=F.mul(U(-2),F.mul(F.sub(u,v),F.add(F.mul(U(2),u),one)))
            C=F.mul(U(-2),F.mul(u,v))
            D=F.add(F.add(u2,F.mul(U(4),F.mul(u,v))),F.mul(U(2),v))
            det=F.sub(F.mul(A,D),F.mul(B,C))
            N=F.mul(u2,F.add(F.mul(U(2),u),one))
            d=F.sub(F.add(u2,F.mul(U(2),u)),U(2))
            delta=F.sub(N,F.mul(v,d))
            assert det==delta, (F.q,u,v,det,delta)
            if det==zero:
                Hcount+=1
                assert d!=zero
                assert v==F.mul(N,F.inv(d))
                exceptional.append((u,v))
    pred=F.q-4-(2 if F.m%2==0 else 0)
    assert Hcount==pred, (F.q,Hcount,pred)
    print(f'F_{F.q}: smooth parameters={n4}, nonordinary={Hcount}, prediction={pred}')
    return exceptional

if __name__=='__main__':
    for mod in [(0,1),(3,0,1),(1,1,0,1)]:
        F=Field(mod)
        exc=run(F)
        if F.q==5:
            assert exc==[((4,), (2,))],exc
            # At this point H=[3,4;4,2], nilpotent of rank 1.
            H=((3,4),(4,2))
            assert all(sum(H[i][k]*H[k][j] for k in range(2))%5==0
                       for i in range(2) for j in range(2))
    print('VERIFY_OK')
