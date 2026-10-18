"""Finite-field checks for the unit-value range of weight-zero Rota--Baxter maps.
Run: python verify_rb.py
This is a finite test, not a proof of the general theorem.
"""
from itertools import product
from math import ceil

class Field:
    def __init__(self,p,mod=None):
        self.p=p
        self.mod=mod
        self.degree=len(mod)-1 if mod else 1
        self.q=p**self.degree
    def to_poly(self,x):
        return [(x//(self.p**i))%self.p for i in range(self.degree)]
    def from_poly(self,v):
        return sum((c%self.p)*(self.p**i) for i,c in enumerate(v))
    def add(self,a,b):
        return self.from_poly([(x+y)%self.p for x,y in zip(self.to_poly(a),self.to_poly(b))])
    def neg(self,a):
        return self.from_poly([(-x)%self.p for x in self.to_poly(a)])
    def mul(self,a,b):
        va=self.to_poly(a);vb=self.to_poly(b)
        conv=[0]*(2*self.degree-1)
        for i,x in enumerate(va):
            for j,y in enumerate(vb):conv[i+j]=(conv[i+j]+x*y)%self.p
        if self.mod:
            for i in range(len(conv)-1,self.degree-1,-1):
                c=conv[i]
                for j in range(self.degree):
                    conv[i-self.degree+j]=(conv[i-self.degree+j]-c*self.mod[j])%self.p
        return self.from_poly(conv[:self.degree])
    def power(self,a,n):
        o=1
        while n:
            if n&1:o=self.mul(o,a)
            a=self.mul(a,a);n//=2
        return o
    def inv(self,a):
        if not a:raise ZeroDivisionError()
        return self.power(a,self.q-2)

def padd(F,x,y):return tuple(F.add(a,b) for a,b in zip(x,y))
def pneg(F,x):return tuple(F.neg(a) for a in x)
def psub(F,x,y):return padd(F,x,pneg(F,y))
def pscale(F,x,c):return tuple(F.mul(a,c) for a in x)
def pmul(F,x,y):
    N=len(x);r=[0]*N
    for i,a in enumerate(x):
        if a:
            for j,b in enumerate(y[:N-i]):
                if b:r[i+j]=F.add(r[i+j],F.mul(a,b))
    return tuple(r)
def ppow(F,x,n):
    o=(1,)+(0,)*(len(x)-1)
    while n:
        if n&1:o=pmul(F,o,x)
        x=pmul(F,x,x);n//=2
    return o

def build_operator(F,N,a):
    """Triangular k[a]-linear projection onto k[a], then truncated integration."""
    basis=[]; one=(1,)+(0,)*(N-1)
    if not any(a):
        return lambda x:(0,)*N
    r=next(i for i,v in enumerate(a) if v)
    assert r>=1 and r*F.p>=N
    L=(N-1)//r+1
    assert L<=F.p
    powers=[ppow(F,a,j) for j in range(L)]
    for i in range(r):
        for j in range(L):
            d=i+j*r
            if d<N:
                b=(0,)*i+powers[j][:N-i]
                assert b[d] and all(not b[k] for k in range(d))
                basis.append((d,i,j,b))
    basis.sort()
    assert len(basis)==N
    def P(x):
        z=x
        proj=[0]*L
        for d,i,j,b in basis:
            fac=F.mul(z[d],F.inv(b[d]))
            if i==0:proj[j]=fac
            z=psub(F,z,pscale(F,b,fac))
        assert not any(z)
        out=(0,)*N
        for j in range(L-1):
            if proj[j]:
                assert (j+1)%F.p
                out=padd(F,out,pscale(F,powers[j+1],F.mul(proj[j],F.inv((j+1)%F.p))))
        return out
    assert P(one)==a
    return P

def rb_test(F,N,P):
    E=[(0,)*i+(1,)+(0,)*(N-i-1) for i in range(N)]
    X=[P(e) for e in E]
    for i in range(N):
        for j in range(N):
            lhs=pmul(F,X[i],X[j])
            rhs=P(padd(F,pmul(F,E[i],X[j]),pmul(F,X[i],E[j])))
            assert lhs==rhs,(F.p,F.q,N,i,j,lhs,rhs)

def all_value_tests(F,N,limit=None):
    cutoff=ceil(N/F.p)
    v=0
    seq=product(range(F.q),repeat=N-cutoff)
    for tail in seq:
        a=(0,)*cutoff+tail
        assert not any(ppow(F,a,F.p))
        P=build_operator(F,N,a)
        rb_test(F,N,P)
        v+=1
        if limit and v>=limit:break
    return v

def exhaustive_small(F,N):
    """Independent enumeration of every linear operator for very small matrices."""
    E=[(0,)*i+(1,)+(0,)*(N-i-1) for i in range(N)]
    observed=set();num=0
    for coeffs in product(range(F.q),repeat=N*N):
        X=[tuple(coeffs[i*N:(i+1)*N]) for i in range(N)]
        def P(x):
            out=(0,)*N
            for a,y in zip(x,X):
                if a:out=padd(F,out,pscale(F,y,a))
            return out
        good=True
        for i in range(N):
            for j in range(i,N):
                if pmul(F,X[i],X[j]) != P(padd(F,pmul(F,E[i],X[j]),pmul(F,X[i],E[j]))):
                    good=False;break
            if not good:break
        if good:
            num+=1
            observed.add(X[0])
    cutoff=ceil(N/F.p)
    assert observed=={(0,)*cutoff+v for v in product(range(F.q),repeat=N-cutoff)},(F.p,N,observed)
    return num,len(observed)

def main():
    cases=[(Field(2),range(2,8)),(Field(3),range(2,8)),(Field(5),range(2,7)),(Field(2,[1,1,1]),range(2,6)),(Field(3,[1,0,1]),range(2,5))]
    total=0
    for F,ns in cases:
        for N in ns:
            cap=300 if F.q**(N-ceil(N/F.p))>300 else None
            num=all_value_tests(F,N,cap)
            total+=num
            print(f'construction_check q={F.q} p={F.p} N={N} candidates={num}')
    for F,N in [(Field(2),2),(Field(2),3),(Field(2),4),(Field(3),2),(Field(3),3)]:
        num,vals=exhaustive_small(F,N)
        print(f'exhaustive_all_operators q={F.q} N={N} valid_operators={num} distinct_unit_values={vals}')
    print('VERIFICATION_OK',total)

if __name__=='__main__':main()
