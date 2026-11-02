#!/usr/bin/env python3
"""Independent finite-field Cartier enumeration; uses no symbolic package."""
from collections import Counter

P = 7

class Field:
    def __init__(self, modulus):
        self.mod = [c % P for c in modulus]
        self.m = len(modulus)-1
        self.q = P**self.m
        self.vectors = [self._decode(z) for z in range(self.q)]
        self.plus = [[self._encode([(u+v)%P for u,v in zip(self.vectors[i],self.vectors[j])])
                      for j in range(self.q)] for i in range(self.q)]
        self.times = [[self._mul(i,j) for j in range(self.q)] for i in range(self.q)]
        self.neg = [self._encode([(-u)%P for u in self.vectors[i]]) for i in range(self.q)]
        self.inv = [0]+[self.pow(i,self.q-2) for i in range(1,self.q)]
        self.root = [self.pow(i,self.q//P) for i in range(self.q)]
        assert all(self.times[i][self.inv[i]]==1 for i in range(1,self.q))

    def _decode(self, a):
        result=[]
        for _ in range(self.m):
            result.append(a%P);a//=P
        return result

    def _encode(self, a):
        return sum(v*P**i for i,v in enumerate(a))

    def _mul(self, i,j):
        if not i or not j: return 0
        u=self.vectors[i];v=self.vectors[j]
        t=[0]*(2*self.m-1)
        for r in range(self.m):
            for s in range(self.m):t[r+s]=(t[r+s]+u[r]*v[s])%P
        for h in range(len(t)-1,self.m-1,-1):
            c=t[h]
            for s in range(self.m):t[h-self.m+s]=(t[h-self.m+s]-c*self.mod[s])%P
        return self._encode(t[:self.m])

    def add(self,a,b):return self.plus[a][b]
    def mul(self,a,b):return self.times[a][b]
    def sub(self,a,b):return self.plus[a][self.neg[b]]
    def pow(self,a,n):
        z=1
        while n:
            if n&1:z=self.times[z][a]
            a=self.times[a][a];n//=2
        return z


def polynomial_power3(a,b,F):
    f=[0]*11
    for i,v in [(1,b),(4,a),(7,1),(10,1)]:f[i]=v
    def mulpoly(g,h):
        z=[0]*(len(g)+len(h)-1)
        for i,u in enumerate(g):
            if not u:continue
            for j,v in enumerate(h):
                if v:z[i+j]=F.add(z[i+j],F.mul(u,v))
        return z
    c=mulpoly(mulpoly(f,f),f)
    return [[c[7*i-j] for j in range(1,5)] for i in range(1,5)]


def matmul(A,B,F):
    n=len(A)
    return [[sum_field((F.mul(A[i][k],B[k][j]) for k in range(n)),F)
             for j in range(n)] for i in range(n)]

def sum_field(vals,F):
    u=0
    for v in vals:u=F.add(u,v)
    return u

def rank(M,F):
    A=[row[:] for row in M];h=len(A);w=len(A[0]);r=0
    for j in range(w):
        pivot=next((i for i in range(r,h) if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        z=F.inv[A[r][j]]
        for t in range(j,w):A[r][t]=F.mul(A[r][t],z)
        for i in range(r+1,h):
            fac=A[i][j]
            if not fac:continue
            for t in range(j,w):A[i][t]=F.sub(A[i][t],F.mul(fac,A[r][t]))
        r+=1
        if r==h:break
    return r


def independently_computed_ranks(a,b,F):
    H=polynomial_power3(a,b,F)
    # On omega_j=x^{j-1} dx/y, Cartier is inverse-Frobenius-semilinear
    # with entries (coefficient of x^{7i-j} in f^3)^{1/7}.
    D=[[F.root[v] for v in row] for row in H]
    T=[row[:] for row in D]
    for _ in range(3):
        T=matmul(D,[[F.root[v] for v in row] for row in T],F)
    return 4-rank(H,F),rank(T,F)


def theoretical_ranks(a,b,F):
    plus,mul,sub=F.add,F.mul,F.sub
    a2=mul(a,a);a3=mul(a2,a);b2=mul(b,b)
    L=sub(plus(a3,mul(3,b2)),mul(a,b))
    R=sub(plus(mul(3,a2),mul(3,a)),b)
    S=plus(mul(a,b2),F.pow(plus(a,1),7))
    if R==0:return (2,1 if S==0 else 2)
    if L==0:return (1,3)
    return (0,4)


def smooth(a,b,F):
    plus,mul,sub=F.add,F.mul,F.sub
    a2=mul(a,a);a3=mul(a2,a);b2=mul(b,b)
    disc=sum_field([mul(3,a3),a2,F.neg[mul(3,mul(a,b))],b2,mul(3,b)],F)
    return b!=0 and disc!=0


def census(F):
    found=Counter()
    for a in range(F.q):
        for b in range(F.q):
            if not smooth(a,b,F):continue
            got=independently_computed_ranks(a,b,F)
            want=theoretical_ranks(a,b,F)
            assert got==want,(F.q,a,b,got,want)
            found[got]+=1
    return dict(sorted(found.items()))

if __name__=='__main__':
    F7=Field([0,1]);got7=census(F7)
    assert got7=={(0,4):29,(1,3):4,(2,1):2,(2,2):2},got7
    print('F7_EXHAUSTIVE_CARTIER_OK',got7)
    F49=Field([1,0,1]);got49=census(F49)
    print('F49_EXHAUSTIVE_CARTIER_OK',got49)
    F343=Field([-1,0,3,1]);alpha=7
    assert F343.pow(alpha,3)==F343.sub(1,F343.mul(3,F343.pow(alpha,2)))
    special=[]
    for aa in [alpha,F343.pow(alpha,7),F343.pow(alpha,49),2,3]:
        bb=F343.mul(3,F343.mul(aa,F343.add(aa,1)))
        assert smooth(aa,bb,F343)
        assert theoretical_ranks(aa,bb,F343)==(2,1)
        assert independently_computed_ranks(aa,bb,F343)==(2,1)
        special.append((aa,bb))
    assert len(set(special))==5
    print('GF343_FIVE_DEEP_POINTS_OK',special)
