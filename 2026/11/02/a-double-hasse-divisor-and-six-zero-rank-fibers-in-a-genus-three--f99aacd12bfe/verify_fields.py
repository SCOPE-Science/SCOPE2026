#!/usr/bin/env python3
"""Independent finite-field tests (no CAS): direct Cartier convolutions and point counts."""
from collections import Counter
from itertools import product
P=5
MODULI={1:(0,1),2:(2,0,1),3:(1,1,0,1)}

class GF:
    def __init__(self,n):
        self.n=n; self.mod=MODULI[n]; self.q=P**n
        self.elements=[tuple((j//P**i)%P for i in range(n)) for j in range(self.q)]
        self.zero=(0,)*n;self.one=(1,)+(0,)*(n-1)
    def c(self,v): return (v%P,)+(0,)*(self.n-1)
    def add(self,a,b):return tuple((u+v)%P for u,v in zip(a,b))
    def neg(self,a):return tuple((-u)%P for u in a)
    def mul(self,a,b):
        n=self.n;buf=[0]*(2*n-1)
        for i,ai in enumerate(a):
            for j,bj in enumerate(b):buf[i+j]+=ai*bj
        for k in range(2*n-2,n-1,-1):
            x=buf[k]%P
            if x:
                for j in range(n):buf[k-n+j]-=x*self.mod[j]
        return tuple(x%P for x in buf[:n])
    def pw(self,a,r):
        out=self.one
        while r:
            if r&1:out=self.mul(out,a)
            a=self.mul(a,a);r>>=1
        return out
    def inv(self,a): return self.pw(a,self.q-2)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def det3(self,M):
        A=M
        t=self.zero
        for j in range(3):
            s=self.mul(A[0][j],self.sub(self.mul(A[1][(j+1)%3],A[2][(j+2)%3]),self.mul(A[1][(j+2)%3],A[2][(j+1)%3])))
            t=self.add(t,s)
        return t
    def mm(self,A,B):
        return [[self.add(self.add(self.mul(A[i][0],B[0][j]),self.mul(A[i][1],B[1][j])),self.mul(A[i][2],B[2][j])) for j in range(3)] for i in range(3)]
    def rank(self,M):
        B=[list(row) for row in M];r=0
        for j in range(3):
            pivot=next((i for i in range(r,3) if B[i][j]!=self.zero),None)
            if pivot is None: continue
            B[r],B[pivot]=B[pivot],B[r]
            inv=self.inv(B[r][j]);B[r]=[self.mul(inv,x) for x in B[r]]
            for i in range(r+1,3):
                c=B[i][j]
                if c!=self.zero:B[i]=[self.sub(B[i][k],self.mul(c,B[r][k])) for k in range(3)]
            r+=1
            if r==3:break
        return r
    def polynomial(self,a,b):
        # x^7 + a*x^5 + b*x^3 + x
        d=[self.zero for _ in range(8)];d[1]=self.one;d[3]=b;d[5]=a;d[7]=self.one
        sq=[self.zero for _ in range(15)]
        for i in range(8):
            for j in range(8):sq[i+j]=self.add(sq[i+j],self.mul(d[i],d[j]))
        return d,sq
    def hw(self,a,b):
        coeff=self.polynomial(a,b)[1]
        return [[coeff[5*(i+1)-(j+1)] for j in range(3)] for i in range(3)]
    def disc(self,a,b):
        # resultant of z^3+a z^2+b z+1 and derivative, using formula
        a2=self.mul(a,a);b2=self.mul(b,b);ab=self.mul(a,b)
        v=self.sub(self.mul(a2,b2),self.mul(self.c(4),self.mul(a2,a)))
        v=self.add(v,self.mul(self.c(18),ab));v=self.sub(v,self.mul(self.c(4),self.mul(b2,b)))
        return self.sub(v,self.c(27))
    def pr(self,H):
        T=H
        for r in range(1,3):
            V=[[self.pw(H[i][j],P**r) for j in range(3)] for i in range(3)]
            T=self.mm(T,V)
        return self.rank(T)

for n in (1,2):
    K=GF(n); c=Counter();exceptions=[]
    for a,b in product(K.elements,repeat=2):
        if K.disc(a,b)==K.zero:continue
        H=K.hw(a,b)
        arn=3-K.rank(H);fr=K.pr(H)
        ab=K.mul(a,b)
        exceptional=K.add(ab,K.one)==K.zero
        expecta=2 if exceptional else 0
        expectf=(0 if K.pw(b,6)==K.one else 1) if exceptional else 3
        assert (arn,fr)==(expecta,expectf),(n,a,b,arn,fr,expecta,expectf)
        c[(arn,fr)]+=1
        if fr==0:exceptions.append((a,b))
    print(f'GF({K.q}) smooth {sum(c.values())}: {dict(c)}, p-rank-zero parameters {exceptions}')
    if n==1: assert c[(2,0)]==2
    if n==2: assert c[(2,0)]==6

# Unrelated arithmetic check: Hasse-zero Frobenius coefficients from actual point counts
# for the rational representative (a,b)=(4,1).
N=[]
for n in (1,2,3):
    K=GF(n);a=K.c(4);b=K.one;cnt=1
    for x in K.elements:
        x3=K.pw(x,3);x5=K.pw(x,5);x7=K.pw(x,7)
        f=K.add(K.add(K.add(x7,K.mul(a,x5)),K.mul(b,x3)),x)
        if f==K.zero:cnt+=1
        else:cnt+=2 if K.pw(f,(K.q-1)//2)==K.one else 0
    N.append(cnt)
s=[5**(r+1)+1-N[r] for r in range(3)]
c1=-s[0]
c2=(s[0]**2-s[1])//2
c3=(-s[0]**3+3*s[0]*s[1]-2*s[2])//6
assert c1%5==c2%5==c3%5==0
print(f'POINT_COUNT_F5_F25_F125_OK counts={N}, L1-3={c1,c2,c3}')
print('GF5_GF25_FULL_CARTIER_STRATA_OK')
