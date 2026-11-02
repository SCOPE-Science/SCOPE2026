#!/usr/bin/env python3
"""Independent finite-field verification of two-dimensional Jordan-plane representations.

Run: python3 verify_jordan_plane.py
Requires Python 3 standard library only.
"""
from itertools import product


class Field:
    def __init__(self, p, modulus=(0, 1)):
        self.p = p
        self.modulus = tuple(modulus)
        self.d = len(self.modulus) - 1
        assert self.modulus[-1] == 1
        self.q = p ** self.d
        self.digits = [self.to_digits(i) for i in range(self.q)]
        self.add_table = [[self.from_digits([(a+b)%p for a,b in zip(self.digits[i],self.digits[j])]) for j in range(self.q)] for i in range(self.q)]
        self.mul_table = [[self.poly_mul(i,j) for j in range(self.q)] for i in range(self.q)]
        self.inv_table = [None] + [next(b for b in range(1,self.q) if self.mul_table[a][b]==1) for a in range(1,self.q)]

    def to_digits(self, a):
        z=[]
        for _ in range(self.d):z.append(a%self.p);a//=self.p
        return z
    def from_digits(self, z):
        return sum(c*self.p**i for i,c in enumerate(z))
    def poly_mul(self,i,j):
        p=self.p; d=self.d
        t=[0]*(2*d-1)
        for a,x in enumerate(self.digits[i]):
            for b,y in enumerate(self.digits[j]): t[a+b]=(t[a+b]+x*y)%p
        for e in range(2*d-2,d-1,-1):
            c=t[e]
            if c:
                for a in range(d):t[e-d+a]=(t[e-d+a]-c*self.modulus[a])%p
        return self.from_digits(t[:d])
    def add(self,a,b):return self.add_table[a][b]
    def neg(self,a):return self.from_digits([(-v)%self.p for v in self.digits[a]])
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):return self.mul_table[a][b]
    def inv(self,a):return self.inv_table[a]


def mm(A,B,F):
    a,b,c,d=A;e,f,g,h=B
    return (F.add(F.mul(a,e),F.mul(b,g)),F.add(F.mul(a,f),F.mul(b,h)),
            F.add(F.mul(c,e),F.mul(d,g)),F.add(F.mul(c,f),F.mul(d,h)))


def residual(X,Y,F):
    xy=mm(X,Y,F); yx=mm(Y,X,F); yy=mm(Y,Y,F)
    return tuple(F.sub(F.sub(a,b),c) for a,b,c in zip(xy,yx,yy))


def linear_rank(rows,F):
    A=[list(r) for r in rows]
    ncols=len(A[0]); nrows=len(A); piv=0
    for col in range(ncols):
        i=next((i for i in range(piv,nrows) if A[i][col]),None)
        if i is None:continue
        A[piv],A[i]=A[i],A[piv]
        inv=F.inv(A[piv][col]);A[piv]=[F.mul(inv,z) for z in A[piv]]
        for j in range(nrows):
            if j!=piv and A[j][col]:
                t=A[j][col]
                A[j]=[F.sub(x,F.mul(t,y)) for x,y in zip(A[j],A[piv])]
        piv+=1
        if piv==nrows:break
    return piv


def count_by_linear_fibers(F):
    q=F.q
    basis=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    counts={}
    for Y in product(range(q),repeat=4):
        rhs=mm(Y,Y,F)
        cols=[]
        for E in basis:
            EY=mm(E,Y,F);YE=mm(Y,E,F)
            cols.append(tuple(F.sub(x,y) for x,y in zip(EY,YE)))
        rows=[[cols[col][row] for col in range(4)] for row in range(4)]
        r=linear_rank(rows,F)
        s=linear_rank([row+[rhs[i]] for i,row in enumerate(rows)],F)
        n=q**(4-r) if r==s else 0
        counts[r,s]=counts.get((r,s),0)+1
        total=counts.get('weighted',0)+n
        counts['weighted']=total
    return counts


def brute_count(F):
    q=F.q;mat=list(product(range(q),repeat=4))
    return sum(residual(X,Y,F)==(0,0,0,0) for X in mat for Y in mat)


def run():
    configurations=[(2,(0,1)),(3,(0,1)),(5,(0,1)),(7,(0,1)),
                    (2,(1,1,1)),(2,(1,1,0,1)),(3,(1,0,1))]
    for p,poly in configurations:
        F=Field(p,poly);q=F.q
        stats=count_by_linear_fibers(F);obtained=stats.pop('weighted')
        expected=(q**5+q**4-q**3) if p==2 else (2*q**4-q**2)
        assert obtained==expected,(q,obtained,expected)
        if q<=3:
            brute=brute_count(F)
            assert brute==obtained,(q,brute,obtained)
        print(f'F_{q}: independent linear-equation count={obtained}; formula={expected}; fiber-rank summary={sorted(stats.items())}; brute={"passed" if q<=3 else "not requested"}')
    print('JORDAN_PLANE_MODULAR_M2_OK 7 FIELD_CONFIGURATIONS 2 EXHAUSTIVE_PAIR_CHECKS')

if __name__=='__main__':run()
