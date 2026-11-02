#!/usr/bin/env python3
"""Separate exhaustive field check over F3 and F9; stdlib only."""
from itertools import product

class Field:
    def __init__(self, p2):
        self.elements = tuple(range(9 if p2 else 3))
    @staticmethod
    def add(x,y): return ((x%3+y%3)%3) + 3*((x//3+y//3)%3)
    @staticmethod
    def neg(x): return (-x%3)+3*((-(x//3))%3)
    @staticmethod
    def mul(x,y):
        a,b=x%3,x//3; c,d=y%3,y//3
        return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
    def pow(self,a,n):
        z=1
        while n:
            if n&1: z=self.mul(z,a)
            a=self.mul(a,a);n>>=1
        return z
    def inv(self,x):
        if x==0:raise ZeroDivisionError
        return self.pow(x,7)
    def sub(self,x,y):return self.add(x,self.neg(y))

F=Field(True)
def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def remainder(p,q):
    p=trim(p[:]);q=trim(q[:]);dq=len(q)-1
    inv=F.inv(q[-1])
    while len(p)>=len(q) and p!=[0]:
        s=F.mul(p[-1],inv); off=len(p)-len(q)
        for j in range(len(q)):
            p[off+j]=F.sub(p[off+j],F.mul(s,q[j]))
        trim(p)
    return p

def squarefree(a,b,c):
    # h(t)=t^5+a t^3+b t^2+c t+1
    # h'(t)=2t^4+2bt+c, characteristic 3.
    f=[1,c,b,a,0,1]; df=[c,F.mul(2,b),0,0,2]
    while df!=[0]:
        f,df=df,remainder(f,df)
    return len(f)==1

def H(a,b,c):
    return [[0,1,0,0,0],[b,0,c,0,1],[0,a,0,b,0],[1,0,0,0,a],[0,0,0,1,0]]

def mmul(A,B):
    return [[sum_field(F.mul(x,y) for x,y in zip(row,col)) for col in zip(*B)] for row in A]

def sum_field(vals):
    out=0
    for v in vals:out=F.add(out,v)
    return out

def rank(A):
    B=[row[:] for row in A];rows=len(B);cols=len(B[0]);i=0
    for j in range(cols):
        pivot=next((k for k in range(i,rows) if B[k][j]!=0),None)
        if pivot is None:continue
        B[i],B[pivot]=B[pivot],B[i]
        inv=F.inv(B[i][j]);B[i]=[F.mul(inv,x) for x in B[i]]
        for k in range(i+1,rows):
            u=B[k][j]
            if u:
                B[k]=[F.sub(x,F.mul(u,y)) for x,y in zip(B[k],B[i])]
        i+=1
        if i==rows:break
    return i

def predicted(a,b,c):
    u=F.add(F.pow(b,3),F.mul(a,F.pow(c,3)))
    T=F.sub(F.add(F.mul(F.pow(a,3),F.pow(b,3)),F.mul(F.pow(c,3),F.sub(F.pow(a,4),b))),1)
    E=F.add(u,F.pow(a,27))
    return 4 if T!=0 else (2 if E!=0 else 0)

def measured(a,b,c):
    m=[list(row) for row in zip(*H(a,b,c))];prod=[[int(i==j) for j in range(5)] for i in range(5)]
    for n in range(5):
        twist=[[F.pow(x,3**n) for x in row] for row in m]
        prod=mmul(prod,twist)
    return 5-rank(m),rank(prod)

for coeffs in (tuple(range(3)),tuple(range(9))):
    tally={0:0,2:0,4:0};bad=0
    for a,b,c in product(coeffs,repeat=3):
        if not squarefree(a,b,c):
            bad+=1;continue
        anum,pr=measured(a,b,c)
        assert anum==1,(a,b,c,anum)
        assert predicted(a,b,c)==pr,(a,b,c,predicted(a,b,c),pr)
        tally[pr]+=1
    q=len(coeffs)
    assert sum(tally.values())+bad==q**3
    print('GF%d_EXHAUSTIVE_CARTIER_OK'%q, 'smooth',sum(tally.values()),'singular',bad,'ranks',tally)
    assert tally[0]>0 and tally[2]>0 and tally[4]>0
print('INDEPENDENT_GENUS5_CHAR3_FIELD_CERTIFICATE_OK')
