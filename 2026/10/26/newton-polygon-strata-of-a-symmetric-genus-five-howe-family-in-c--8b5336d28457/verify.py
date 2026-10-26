#!/usr/bin/env python3
"""Independent exact finite-field verification of a genus-five Howe rank census.
Only elementary polynomial arithmetic over GF(3^m), m <= 4, is used.
The script does not serve as a proof for unbounded m.
"""
from collections import Counter

IRRED = {1: (0, 1), 2: (1, 0, 1), 3: (1, 2, 0, 1), 4: (2, 1, 0, 0, 1)}

class FiniteField:
    def __init__(self, m):
        self.m = m
        self.q = 3**m
        self.pol = IRRED[m]
        self.digits = [[(n // 3**j) % 3 for j in range(m)] for n in range(self.q)]
        self.addtable = [[sum(((a[j] + b[j]) % 3) * (3**j) for j in range(m)) for b in self.digits] for a in self.digits]
        self.negtable = [sum(((-a[j]) % 3) * 3**j for j in range(m)) for a in self.digits]
        self.multable = [[self._mul(a,b) for b in self.digits] for a in self.digits]
    def _mul(self, a, b):
        m = self.m
        f = [0]*(2*m-1)
        for i in range(m):
            for j in range(m):
                f[i+j] = (f[i+j]+a[i]*b[j])%3
        for i in range(2*m-2,m-1,-1):
            z=f[i]
            if z:
                for j in range(m):
                    f[i-m+j]=(f[i-m+j]-z*self.pol[j])%3
        return sum(f[i]*3**i for i in range(m))
    def add(self,a,b): return self.addtable[a][b]
    def neg(self,a): return self.negtable[a]
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b): return self.multable[a][b]
    def pow(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a)
            n//=2
        return z
    def inv(self,a):
        assert a
        return self.pow(a,self.q-2)


def trim(p):
    while p and p[-1] == 0:p.pop()
    return p

def poly_mult(F,p,q):
    if not p or not q:return []
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            r[i+j]=F.add(r[i+j],F.mul(a,b))
    return trim(r)

def poly_rem(F,a,b):
    a=trim(a[:]); b=trim(b[:])
    assert b
    inv=F.inv(b[-1])
    while len(a)>=len(b):
        k=len(a)-len(b)
        s=F.mul(a[-1],inv)
        for j in range(len(b)):
            a[k+j]=F.sub(a[k+j],F.mul(s,b[j]))
        trim(a)
    return a

def poly_gcd(F,a,b):
    while b:a,b=b,poly_rem(F,a,b)
    return a

def derivative(F,p):
    return trim([F.mul(i%3,p[i]) for i in range(1,len(p))])

def matrix_rank(F,A):
    A=[row[:] for row in A]
    if not A:return 0
    R=len(A); C=len(A[0]); rank=0
    for j in range(C):
        pivot=next((i for i in range(rank,R) if A[i][j]),None)
        if pivot is None:continue
        A[rank],A[pivot]=A[pivot],A[rank]
        inv=F.inv(A[rank][j]); A[rank]=[F.mul(x,inv) for x in A[rank]]
        for i in range(R):
            if i==rank or not A[i][j]:continue
            factor=A[i][j]
            A[i]=[F.sub(u,F.mul(factor,v)) for u,v in zip(A[i],A[rank])]
        rank+=1
        if rank==R:break
    return rank

def mmul(F,A,B):
    return [[sum_field(F,[F.mul(a,c) for a,c in zip(row,col)]) for col in zip(*B)] for row in A]

def sum_field(F,terms):
    r=0
    for v in terms:r=F.add(r,v)
    return r

def hasse_matrix(f,g):
    return [[f[3*(i+1)-(j+1)] if 0<=3*(i+1)-(j+1)<len(f) else 0
             for j in range(g)] for i in range(g)]

def stable_rank(F,H):
    g=len(H)
    A=[[1 if i==j else 0 for j in range(g)] for i in range(g)]
    for k in range(g):
        twist=[[F.pow(v,3**k) for v in row] for row in H]
        A=mmul(F,A,twist)
    return matrix_rank(F,A)

def predicted(m,q):
    epsilon=2 if m%2==0 else 0
    if m%2:
        n4=(q-1)*(q-3)
    else:
        n4=q*q-6*q+11
    n3=2*q-epsilon-4
    return {2:1,3:n3,4:n4}

def main():
    for m in (1,2,3,4):
        F=FiniteField(m); q=F.q
        for a in range(1,q): assert F.mul(a,F.inv(a)) == 1
        # This exhaustive check of separability and disjointness does not rely on
        # the closed formulas used in the mathematical statement.
        Q1=[1,0,0,0,1]
        assert len(poly_gcd(F,Q1,derivative(F,Q1)))==1
        seen=Counter()
        for b in range(q):
            for c in range(q):
                Q2=[c,0,b,0,1]
                if len(poly_gcd(F,Q2,derivative(F,Q2)))>1:continue
                if len(poly_gcd(F,Q1,Q2))>1:continue
                Q3=poly_mult(F,Q1,Q2)
                H0=hasse_matrix(Q1,1)
                H2=hasse_matrix(Q2,1)
                H3=hasse_matrix(Q3,3)
                a_number=5-sum(map(lambda hg:matrix_rank(F,hg),(H0,H2,H3)))
                p_rank=sum(stable_rank(F,hg) for hg in (H0,H2,H3))
                assert p_rank in (2,3,4)
                assert a_number == 5-p_rank
                predicted_p=2+(b!=0)+(c!=F.neg(1))
                assert p_rank==predicted_p, (m,b,c,p_rank,predicted_p)
                seen[p_rank]+=1
        assert {r:seen[r] for r in (2,3,4)}==predicted(m,q), (m,seen,predicted(m,q))
        print(f'F_{q}: ranks 2={seen[2]}, 3={seen[3]}, 4={seen[4]}, smooth={sum(seen.values())}')
    print('VERIFY_OK')

if __name__=='__main__':main()
