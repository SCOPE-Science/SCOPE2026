#!/usr/bin/env python3
"""Independent p-semilinear matrix checks over F_11, F_(11^5), and F_(11^20)."""
P = 11
class Field:
    def __init__(self, modulus):
        self.mod = tuple(x % P for x in modulus)
        assert self.mod[-1] == 1
        self.n = len(modulus) - 1
        self.q = P ** self.n
        self.zero = self.el(0)
        self.one = self.el(1)
        self.u = self.el([0,1]) if self.n>1 else self.el(0)
    def el(self,x):
        if isinstance(x, E):
            assert x.F is self
            return x
        if isinstance(x,int):
            xs=[x]
        else:
            xs=list(x)
        xs += [0]*max(0,self.n-len(xs))
        return E(self, tuple(t%P for t in xs[:self.n]))

class E:
    def __init__(self,F,x): self.F,self.x=F,x
    def __eq__(self,other):
        other=self.F.el(other)
        return self.x==other.x
    def __add__(self,other):
        b=self.F.el(other)
        return self.F.el([(x+y)%P for x,y in zip(self.x,b.x)])
    __radd__=__add__
    def __neg__(self):return self.F.el([-x for x in self.x])
    def __sub__(self,other):return self+-self.F.el(other)
    def __rsub__(self,other):return self.F.el(other)+-self
    def __mul__(self,other):
        b=self.F.el(other)
        n=self.F.n
        c=[0]*(2*n-1)
        for i,x in enumerate(self.x):
            if x:
                for j,y in enumerate(b.x):
                    c[i+j]=(c[i+j]+x*y)%P
        for i in range(2*n-2,n-1,-1):
            w=c[i]
            if w:
                for j in range(n):c[i-n+j]=(c[i-n+j]-w*self.F.mod[j])%P
        return self.F.el(c[:n])
    __rmul__=__mul__
    def __pow__(self,e):
        assert isinstance(e,int) and e>=0
        r=self.F.one; a=self
        while e:
            if e&1:r=r*a
            a=a*a;e>>=1
        return r
    def inv(self):
        assert self!=self.F.zero
        return self**(self.F.q-2)
    def __repr__(self):return str(self.x)

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),A[0][0].F.zero)
             for j in range(len(B[0]))] for i in range(len(A))]

def rank(M):
    X=[list(row) for row in M]
    h=w=0
    while h<len(X) and w<len(X[0]):
        pivot=next((i for i in range(h,len(X)) if X[i][w]!=0),None)
        if pivot is None:w+=1;continue
        X[h],X[pivot]=X[pivot],X[h]
        inv=X[h][w].inv()
        X[h]=[x*inv for x in X[h]]
        for i in range(len(X)):
            if i!=h:
                t=X[i][w]
                if t!=0:X[i]=[u-t*v for u,v in zip(X[i],X[h])]
        h+=1;w+=1
    return h

def check(F,a,label,expected):
    Z=F.zero
    A0=-a**5-1; A1=-3*a**3; A2=-4*a
    B0=F.el(3);B1=3*a**2
    # Raw coefficient transpose is a p-linear Hasse--Witt matrix.
    H=[[Z,A0,A1,A2],[B0,Z,Z,Z],[B1,Z,Z,Z],[Z,Z,Z,Z]]
    assert rank(H)==2
    M=H
    Frob=H
    ranks=[rank(M)]
    for i in range(1,5):
        Frob=[[x**P for x in row] for row in Frob]
        M=matmul(M,Frob)
        ranks.append(rank(M))
    assert ranks[-1]==expected,(label,ranks)
    scalar=2*a**25-3*a**5-3
    assert (scalar==0)==(expected==0)
    print(label,'stable ranks',ranks,'T_zero',scalar==0)

prime=Field([0,1])
for a in range(11):
    if (a**5+5)%11!=0:
        check(prime,prime.el(a),f'F11:a={a}',2)

m5=[-2]+[0]*4+[1]
F5=Field(m5)
assert F5.u**5==2
check(F5,F5.u,'F_(11^5): a^5=2',0)

m20=[0]*21
for e,c in [(0,-2),(5,-3),(10,4),(15,2),(20,1)]:m20[e]=c
F20=Field(m20)
assert F20.u**20+2*F20.u**15+4*F20.u**10-3*F20.u**5-2==0
check(F20,F20.u,'F_(11^20): quartic-lift root',0)
print('INDEPENDENT_FIELD_CERTIFICATE_OK')
