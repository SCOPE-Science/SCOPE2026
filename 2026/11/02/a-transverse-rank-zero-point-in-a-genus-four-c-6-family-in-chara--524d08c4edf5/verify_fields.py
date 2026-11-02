#!/usr/bin/env python3
"""Independent direct Cartier-matrix computation over F_5 and F_25.
Pure Python. The extension F_25=F_5[t]/(t^2-3), represented as u+v*t.
"""
from collections import Counter

class Field:
    def __init__(self, degree): self.q=5**degree;self.degree=degree
    def add(self,x,y):return ((x%5+y%5)%5) +5*((x//5+y//5)%5)
    def neg(self,x):return self.add(0, (5-x%5)%5+5*((5-x//5)%5))
    def sub(self,x,y):return self.add(x,self.neg(y))
    def mul(self,x,y):
        a,b=x%5,x//5;c,d=y%5,y//5
        return (a*c+3*b*d)%5+5*((a*d+b*c)%5)
    def pow(self,x,n):
        r=1
        while n:
            if n&1:r=self.mul(r,x)
            x=self.mul(x,x);n//=2
        return r
    def inv(self,x):
        assert x
        return self.pow(x,self.q-2)
    def rank(self,M):
        a=[row.copy() for row in M]; m=len(a);n=len(a[0]);r=0
        for j in range(n):
            pivot=next((i for i in range(r,m) if a[i][j]),None)
            if pivot is None:continue
            a[r],a[pivot]=a[pivot],a[r]
            factor=self.inv(a[r][j]);a[r]=[self.mul(factor,v) for v in a[r]]
            for i in range(m):
                if i!=r and a[i][j]:
                    z=a[i][j];a[i]=[self.sub(a[i][k],self.mul(z,a[r][k])) for k in range(n)]
            r+=1
            if r==m:break
        return r
    def mm(self,A,B):
        return [[self.sum(self.mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    def sum(self,vals):
        o=0
        for v in vals:o=self.add(o,v)
        return o

def check(degree):
    F=Field(degree);cnt=Counter();z=0
    for a in range(F.q):
        for b in range(F.q):
            pow_=F.pow;add=F.add;mul=F.mul;sub=F.sub
            disc=add(sub(add(pow_(a,3),pow_(a,2)),mul(2,mul(a,b))),sub(b,mul(2,pow_(b,2))))
            if not b or not disc:
                cnt['singular']+=1;continue
            f=[0]*11;f[1]=b;f[4]=a;f[7]=1;f[10]=1
            sq=[0]*21
            for i in range(11):
                for j in range(11):
                    sq[i+j]=add(sq[i+j],mul(f[i],f[j]))
            M=[[sq[5*(i+1)-(j+1)] for j in range(4)] for i in range(4)]
            # Independent p-semilinear ranks: do not use the sparse block decomposition.
            A=[row.copy() for row in M]
            for exponent in range(1,5):
                Mp=[[pow_(v,5**exponent) for v in row] for row in M]
                A=F.mm(Mp,A)
            p_rank=F.rank(A);a_num=4-F.rank(M)
            c=add(pow_(a,2),mul(2,b))
            s=add(mul(pow_(b,2),add(1,mul(2,pow_(a,5)))),mul(4,add(pow_(a,5),pow_(b,5))))
            predicted=(2 if s else 0)+(1 if c else 0)
            assert p_rank==predicted,(degree,a,b,p_rank,predicted)
            assert a_num==(1 if c else 2),(degree,a,b,a_num)
            cnt[(p_rank,a_num)]+=1;z+=1
    assert sum(cnt.values())==F.q**2
    print('GF%d' % F.q,sorted(cnt.items(),key=lambda k:str(k[0])))

for degree in (1,2):check(degree)
print('CHAR5_C6_INDEPENDENT_GF5_GF25_ITERATED_CARTIER_OK')
