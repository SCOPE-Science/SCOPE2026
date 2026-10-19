"""Reproduce determinant-fiber and diagonalizable/square-zero counts for M2 over small finite fields."""
from itertools import product

IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}

class Field:
    def __init__(self, q):
        self.q = q
        self.m = 0
        t=q
        while t%2 == 0:
            self.m += 1; t//=2
        if t==1:
            self.kind='two'; self.pol=IRREDUCIBLE[self.m]
        else:
            assert self.m==0
            self.kind='prime'; self.p=q
        self.mul_table=[[self.mul_direct(a,b) for b in range(q)] for a in range(q)]
    def add(self,a,b):
        return a^b if self.kind=='two' else (a+b)%self.p
    def neg(self,a):
        return a if self.kind=='two' else (-a)%self.p
    def mul_direct(self,a,b):
        if self.kind=='prime':return (a*b)%self.p
        v=0
        for k in range(self.m):
            if (b>>k)&1:v^=a
            a<<=1
            if a>>self.m:a^=self.pol
        return v
    def mul(self,a,b):return self.mul_table[a][b]
    def sub(self,a,b):return self.add(a,self.neg(b))
    def det(self,A):
        a,b,c,d=A
        return self.sub(self.mul(a,d),self.mul(b,c))
    def tr(self,A):return self.add(A[0],A[3])
    def sqzero(self,N):
        return self.tr(N)==0 and self.det(N)==0
    def eiglines(self,A):
        a,b,c,d=A
        # (1,t), t in Fq, plus (0,1)
        e=0
        for t in range(self.q):
            at=self.add(a,self.mul(b,t))
            ct=self.add(c,self.mul(d,t))
            if ct==self.mul(t,at): e+=1
        if b==0:e+=1
        return e
    def diagonalizable(self,A):
        if self.tr(A)==0 and self.kind=='two':
            return A[1]==A[2]==0 and A[0]==A[3]
        # Explicit eigenbasis classification by two distinct rational eigenvalues, or scalar.
        if A[1]==A[2]==0 and A[0]==A[3]:return True
        s=self.tr(A);d=self.det(A)
        roots=[t for t in range(self.q) if self.add(self.sub(self.mul(t,t),self.mul(s,t)),d)==0]
        return len(roots)==2

def test(q):
    f=Field(q)
    Q=range(q)
    nz=[N for N in product(Q,repeat=4) if f.sqzero(N)]
    assert len(nz)==q*q,(q,len(nz))
    checked=0
    for A in product(Q,repeat=4):
        e=f.eiglines(A)
        fibers=[0]*q
        good=0
        for N in nz:
            B=tuple(f.add(a,n) for a,n in zip(A,N))
            fibers[f.det(B)]+=1
            good+=f.diagonalizable(B)
        da=f.det(A)
        predicted=[1+e*(q-1) if v==da else q+1-e for v in Q]
        assert fibers==predicted, (q,A,e,fibers,predicted)
        if f.kind=='two':
            exp=1 if f.tr(A)==0 else q*(q+1)//2
        else:
            scalar=A[1]==A[2]==0 and A[0]==A[3]
            exp=(1 if scalar else ((q*q-1)//2 if e==0 else (q*(q-1)//2+1 if e==1 else (q*q+1)//2)))
        assert good==exp,(q,A,e,good,exp)
        checked+=1
    return q,checked,len(nz)

if __name__=='__main__':
    for q in [2,3,4,5,7,8]:
        print('PASS q=%d | A=%d | N=%d' % test(q))
