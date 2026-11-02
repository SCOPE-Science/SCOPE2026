#!/usr/bin/env python3
"""Independent finite-field Gauss-fibre enumeration over prime and quadratic fields."""
from collections import defaultdict, Counter

class Field:
    def __init__(self, p, nonsquare=None):
        self.p=p
        self.ext = nonsquare is not None
        self.q=p*p if self.ext else p
        self.c=nonsquare
        self.zero=0
        self.one=1
    def add(self,a,b):
        p=self.p
        if not self.ext:return (a+b)%p
        return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def neg(self,a):return self.sub(0,a)
    def sub(self,a,b):
        p=self.p
        if not self.ext:return (a-b)%p
        return ((a%p-b%p)%p)+p*((a//p-b//p)%p)
    def mul(self,a,b):
        p=self.p
        if not self.ext:return a*b%p
        a0,a1=a%p,a//p; b0,b1=b%p,b//p
        return (a0*b0+self.c*a1*b1)%p + p*((a0*b1+a1*b0)%p)
    def power(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n>>=1
        return z
    def div(self,a,b):
        assert b
        return self.mul(a,self.power(b,self.q-2))
    def smul(self,n,a):return self.mul(n%self.p,a)

def check(p,ns=None):
    F=Field(p,ns);q=F.q
    add,sub,mul=F.add,F.sub,F.mul
    three=3%p
    tangents=defaultdict(list)
    predicted={}
    for x in range(1,q):
        for y in range(1,q):
            z=sub(sub(1,x),y)
            if not z or x==y==z:continue
            e2=add(add(mul(x,y),mul(y,z)),mul(z,x))
            e3=mul(mul(x,y),z)
            A=sub(sub(F.smul(9,e2),F.smul(27,e3)),2%p)
            B=sub(F.smul(27,e3),F.smul(3,e2))
            good=len({x,y,z})==3 and A!=0 and B!=0 and add(A,B)!=0
            grad=tuple(sub(F.div(1,u),three) for u in (x,y,z))
            assert any(grad)
            lead=next(u for u in grad if u)
            key=tuple(F.div(u,lead) for u in grad)
            tangents[key].append((x,y,z))
            predicted[(x,y,z)]=good
    n2=0;n1=0
    for pts in tangents.values():
        assert len(pts) in (1,2),(p,ns,pts)
        for pt in pts: assert predicted[pt] == (len(pts)==2),(p,ns,pt,pts)
        if len(pts)==1:n1+=1
        else:n2+=1
    assert n1+2*n2==(q-1)*(q-2)
    if q%3==2:
        want1=7*q-23
        want2=(q-5)**2//2
        wantT=(q*q+4*q-21)//2
    else:
        want1=9*q-33
        want2=(q-5)*(q-7)//2
        wantT=(q*q+6*q-31)//2
    assert (n1,n2,len(tangents))==(want1,want2,wantT),(p,ns,n1,n2,len(tangents),want1,want2,wantT)
    print('q=%d: smooth=%d singleton=%d double=%d distinct=%d' % (q,(q-1)*(q-2),n1,n2,len(tangents)))

for p in (5,7,11,13,17,19,23,29,31,37,41):check(p)
check(5,2)
check(7,3)
print('FINITE_FIELD_TANGENT_FIBRE_AND_COUNTS_OK')
