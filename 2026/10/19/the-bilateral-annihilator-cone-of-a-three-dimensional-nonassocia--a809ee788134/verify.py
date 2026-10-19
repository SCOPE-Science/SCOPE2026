#!/usr/bin/env python3
"""Exact finite-field checks for the common left/right singular locus of A_t.

Run: python3 verify.py
No external packages are required.
"""
from itertools import product

class Field:
    def __init__(self,p,poly):
        self.p=p
        self.mod=poly  # monic, low-degree coefficients first
        self.m=len(poly)-1
        self.q=p**self.m
        self.digits=[tuple((a//(p**k))%p for k in range(self.m)) for a in range(self.q)]
        self.add=[[self.encode([(u+v)%p for u,v in zip(self.digits[a],self.digits[b])]) for b in range(self.q)] for a in range(self.q)]
        self.mul=[[self.multiply(a,b) for b in range(self.q)] for a in range(self.q)]
        self.one=1
    def encode(self,co):
        return sum((c%self.p)*(self.p**i) for i,c in enumerate(co))
    def multiply(self,a,b):
        p=self.p;m=self.m
        x=[0]*(2*m-1)
        for i,u in enumerate(self.digits[a]):
            for j,v in enumerate(self.digits[b]):
                x[i+j]=(x[i+j]+u*v)%p
        for deg in range(2*m-2,m-1,-1):
            c=x[deg]
            if c:
                for k in range(m): x[deg-m+k]=(x[deg-m+k]-c*self.mod[k])%p
        return self.encode(x[:m])
    def a(self,x,y):return self.add[x][y]
    def mlt(self,x,y):return self.mul[x][y]
    def neg(self,x):return self.encode([(-v)%self.p for v in self.digits[x]])
    def sub(self,x,y):return self.a(x,self.neg(y))


def product_a(F,t,x,y):
    a,b,c=x;d,e,f=y
    A=F.a(F.sub(F.mlt(a,d),F.mlt(b,e)),F.neg(F.mlt(c,f)))
    B=F.a(F.a(F.mlt(a,e),F.mlt(b,d)),F.mlt(t,F.mlt(c,e)))
    C=F.a(F.a(F.mlt(a,f),F.mlt(c,d)),F.mlt(t,F.mlt(c,e)))
    return A,B,C


def determinant(F,M):
    v=F.a;z=F.sub;u=F.mlt
    a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
    return v(z(u(a,z(u(e,i),u(f,h))),u(b,z(u(d,i),u(f,g)))),u(c,z(u(d,h),u(e,g))))


def mat_left(F,t,x):
    b0=(1,0,0); e1=(0,1,0);e2=(0,0,1)
    cols=[product_a(F,t,x,y) for y in (b0,e1,e2)]
    return [[cols[j][i] for j in range(3)] for i in range(3)]


def mat_right(F,t,x):
    b0=(1,0,0); e1=(0,1,0);e2=(0,0,1)
    cols=[product_a(F,t,y,x) for y in (b0,e1,e2)]
    return [[cols[j][i] for j in range(3)] for i in range(3)]


def roots(F,t):
    v=F.a; u=F.mlt
    r_i=sum(v(u(x,x),1)==0 for x in range(F.q))
    r_k=sum(v(v(u(x,x),u(t,x)),v(1,1))==0 for x in range(F.q))
    r_anti=sum(v(u(x,x),v(1,1))==0 for x in range(F.q))
    return (r_i,r_k,r_anti)


def expected_common_zero(F,t,x):
    a,b,c=x;v=F.a;u=F.mlt
    norm_i=lambda v0: v(u(a,a),u(v0,v0))
    norm_k=v(v(u(a,a),u(t,u(a,b))),u(v(1,1),u(b,b)))
    sphere=v(v(u(a,a),u(b,b)),u(c,c))
    return ((b==c and (a==0 or norm_k==0))
            or (c==0 and norm_i(b)==0)
            or (b==0 and norm_i(c)==0)
            or (v(b,c)==0 and sphere==0))


def check(F,t,brute):
    q=F.q;zero=(0,0,0)
    ri,rk,ra=roots(F,t)
    s=4 if F.p==2 else 1+2*ri+rk+ra
    predicted=1+(q-1)*s
    got=0
    points=list(product(range(q),repeat=3))
    for x in points:
        left=determinant(F,mat_left(F,t,x))
        right=determinant(F,mat_right(F,t,x))
        common=(left==0 and right==0)
        assert common==expected_common_zero(F,t,x),('structure',q,t,x,left,right)
        got+=int(common)
        if brute:
            lker=any(y!=zero and product_a(F,t,x,y)==zero for y in points)
            rker=any(y!=zero and product_a(F,t,y,x)==zero for y in points)
            assert lker==(left==0) and rker==(right==0),('kernel',q,t,x)
    assert got==predicted,('count',q,t,got,predicted,ri,rk,ra)
    return got,s,(ri,rk,ra)


def main():
    specs=[(2,[0,1]),(3,[0,1]),(4,[1,1,1]),(5,[0,1]),(7,[0,1]),(8,[1,1,0,1]),(9,[1,0,1]),(11,[0,1]),(16,[1,1,0,0,1])]
    tested=0
    for q,poly in specs:
        p=next(k for k in (2,3,5,7,11) if q%k==0)
        F=Field(p,poly)
        assert F.q==q
        for v0 in range(1,q):
            assert any(F.mlt(v0,w)==1 for w in range(1,q)),('field',q,v0)
        for t in range(1,q):
            count,s,rs=check(F,t,brute=q<=5)
            tested+=1
        print('q=%d: checked %d nonzero parameters; common singular lines last=%d'%(q,q-1,s))
    print('PASS: %d parameter configurations; exact double-singular loci and annihilator checks'%tested)

if __name__=='__main__': main()
