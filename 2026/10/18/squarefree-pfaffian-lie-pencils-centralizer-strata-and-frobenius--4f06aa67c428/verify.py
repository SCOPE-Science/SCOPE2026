#!/usr/bin/env python3
"""Finite-field tests for rank strata of alternating-pencil Lie algebras.

Self-contained arithmetic in small prime and extension fields. These finite
computations corroborate the proof but do not replace its all-field argument.
"""
from itertools import product

class FiniteField:
    def __init__(self, p, modulus):
        self.p = p
        self.mod = tuple(modulus)  # ascending, monic, irreducible
        self.d = len(modulus) - 1
        self.q = p ** self.d
        self.coords = [self.unpack(i) for i in range(self.q)]
        self.add_table = [[self.pack([(x+y) % p for x,y in zip(self.coords[a], self.coords[b])])
                           for b in range(self.q)] for a in range(self.q)]
        self.mul_table = [[self.mul_unchecked(a,b) for b in range(self.q)] for a in range(self.q)]
        self.neg_table = [self.pack([(-x) % p for x in self.coords[a]]) for a in range(self.q)]
    def unpack(self,a):
        v = []
        for _ in range(self.d):
            v.append(a % self.p); a //= self.p
        return v
    def pack(self,v):
        return sum(x * (self.p ** i) for i,x in enumerate(v))
    def mul_unchecked(self,a,b):
        u,v=self.coords[a],self.coords[b]
        out=[0]*(2*self.d-1)
        for i,x in enumerate(u):
            for j,y in enumerate(v): out[i+j]=(out[i+j]+x*y)%self.p
        for k in range(2*self.d-2,self.d-1,-1):
            t=out[k]
            for j in range(self.d):out[k-self.d+j]=(out[k-self.d+j]-t*self.mod[j])%self.p
        return self.pack(out[:self.d])
    def add(self,a,b):return self.add_table[a][b]
    def mul(self,a,b):return self.mul_table[a][b]
    def neg(self,a):return self.neg_table[a]
    def sub(self,a,b):return self.add(a,self.neg(b))
    def polyeval(self,poly,at):
        z=0
        for coeff in reversed(poly):
            z=self.add(self.mul(z,at),coeff)
        return z

def companion(f,p):
    m=len(f)-1
    C=[[0]*m for _ in range(m)]
    for j in range(m-1):C[j+1][j]=1
    for i in range(m):C[i][m-1]=(-f[i])%p
    return C

def linear(C,x,F,transpose=False):
    m=len(x); out=[]
    for i in range(m):
        z=0
        for j in range(m):
            val=C[j][i] if transpose else C[i][j]
            if val:z=F.add(z,F.mul(val,x[j]))
        out.append(z)
    return out

def adrank(v,C,F):
    m=len(C)
    x,y=v[:m],v[m:]
    Tx=linear(C,x,F)
    Ty=linear(C,y,F,True)
    a=[F.neg(z) for z in y]+list(x)
    b=[F.neg(z) for z in Ty]+Tx
    if all(z==0 for z in a):return 0
    pivot=next(i for i,z in enumerate(a) if z!=0)
    for j in range(2*m):
        if F.mul(a[pivot],b[j])!=F.mul(a[j],b[pivot]):return 2
    return 1

def check(p,modulus,f,expected_s=None):
    F=FiniteField(p,modulus)
    m=len(f)-1
    C=companion(f,p)
    roots=[u for u in range(F.q) if F.polyeval(f,u)==0]
    s=len(roots)
    if expected_s is not None:assert s==expected_s,(F.q,f,s)
    counts=[0,0,0]
    for v in product(range(F.q),repeat=2*m):
        counts[adrank(v,C,F)]+=1
    expected=[1,s*(F.q**2-1),F.q**(2*m)-1-s*(F.q**2-1)]
    assert counts==expected,(p,modulus,f,counts,expected)
    # Rank-one elements of the full Lie algebra include two central coordinates.
    lie_counts=[z*F.q**2 for z in counts]
    assert sum(lie_counts)==F.q**(2*m+2)
    # Double-count the commuting pairs from centralizer dimensions.
    commuting=sum(lie_counts[j]*F.q**(2*m+2-j) for j in (0,1,2))
    prob_num=sum(counts[j]*F.q**(2-j) for j in (0,1,2))
    assert commuting==prob_num*F.q**(2*m+2)
    print('PASS',f'p={p}',f'field_order={F.q}',f'f={f}',f'roots={s}',f'vector_ranks={counts}',f'Lie_ranks={lie_counts}',f'commuting_pairs={commuting}')

if __name__=='__main__':
    # Base fields, split and irreducible binary quadratic examples.
    check(2,[0,1],[1,1,1],0)   # t^2+t+1, irreducible over F_2.
    check(2,[1,1,1],[1,1,1],2) # splits over F_4.
    check(3,[0,1],[0,2,1],2)   # t(t-1), split over F_3.
    check(3,[0,1],[1,0,1],0)   # t^2+1, irreducible over F_3.
    check(3,[1,0,1],[1,0,1],2) # splits over F_9.
    check(5,[0,1],[0,4,1],2)   # t(t-1), split over F_5.
    # First cubic splitting cycle: no F_2 points, three F_8 roots.
    check(2,[0,1],[1,1,0,1],0)
    check(2,[1,1,0,1],[1,1,0,1],3)
    print('VERIFY_OK')
