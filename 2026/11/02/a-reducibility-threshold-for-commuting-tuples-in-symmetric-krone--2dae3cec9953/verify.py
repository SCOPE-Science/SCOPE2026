#!/usr/bin/env python3
"""Direct finite-field checks for commuting tuples in symmetric Kronecker trivial extensions."""
from itertools import product

class Field:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
        self.p=2 if q==4 else q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.p
    def neg(self,a):
        return a if self.p==2 else (-a)%self.p
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4: return (a*b)%self.p
        v=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:
                    d=i+j
                    v ^= (1<<d) if d<2 else 3 # alpha^2 = alpha+1
        return v

def multiplication(a,b,r,F):
    # e1, e2, forward arrows, reverse arrows, p1, p2
    n=4+2*r
    assert len(a)==len(b)==n
    c=[0]*n
    c[0]=F.mul(a[0],b[0]); c[1]=F.mul(a[1],b[1])
    for i in range(r):
        j=2+i;k=2+r+i
        c[j]=F.add(F.mul(a[0],b[j]), F.mul(a[j],b[1]))
        c[k]=F.add(F.mul(a[1],b[k]), F.mul(a[k],b[0]))
    p=2+2*r; q=3+2*r
    c[p]=F.add(F.mul(a[0],b[p]), F.mul(a[p],b[0]))
    c[q]=F.add(F.mul(a[1],b[q]), F.mul(a[q],b[1]))
    for i in range(r):
        c[p]=F.add(c[p],F.mul(a[2+i],b[2+r+i]))
        c[q]=F.add(c[q],F.mul(a[2+r+i],b[2+i]))
    return tuple(c)

def commute(a,b,r,F):
    ab=multiplication(a,b,r,F)
    ba=multiplication(b,a,r,F)
    return all(x==y for x,y in zip(ab,ba))

def base_vectors(r,F):
    # quotient by the 3-dimensional center: e1-e2 difference and forward/reverse arrows
    for co in product(range(F.q),repeat=1+2*r):
        v=[0]*(4+2*r)
        v[0]=co[0]
        for i in range(2*r):v[2+i]=co[i+1]
        yield tuple(v)

def isotropic_grassmannian_count(r,s,q):
    top=bottom=1
    for i in range(s):
        top*=q**(2*r-i)-q**i
        bottom*=q**s-q**i
    assert top%bottom==0
    return top//bottom

def predicted_base(q,r,m):
    isotropic=0
    for s in range(min(m,r)+1):
        maps=1
        for i in range(s):maps*=q**m-q**i
        isotropic+=isotropic_grassmannian_count(r,s,q)*maps
    return (q**m-1)*q**(2*r)+isotropic

def check_basis_associative(r,F):
    n=4+2*r
    basis=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    for a,b,c in product(basis,repeat=3):
        assert multiplication(multiplication(a,b,r,F),c,r,F)==multiplication(a,multiplication(b,c,r,F),r,F)
    unit=tuple(int(i<2) for i in range(n))
    for a in basis:
        assert multiplication(unit,a,r,F)==a and multiplication(a,unit,r,F)==a

def count_direct(q,r,m):
    F=Field(q)
    elements=list(base_vectors(r,F))
    n=len(elements)
    neighbours=[]
    for a in elements:
        neighbours.append([j for j,b in enumerate(elements) if commute(a,b,r,F)])
    if m==2:
        total=sum(map(len,neighbours))
    elif m==3:
        neighbour_set=[set(indices) for indices in neighbours]
        total=sum(len(neighbour_set[i].intersection(neighbour_set[j])) for i in range(n) for j in neighbours[i])
    else:raise ValueError
    expected=predicted_base(q,r,m)
    assert total==expected,(q,r,m,total,expected)
    return (q,r,m,total,total*q**(3*m))

if __name__=='__main__':
    for q in (2,3,4):
        for r in (1,2,3):check_basis_associative(r,Field(q))
    print('ASSOCIATIVE_UNITAL_BASIS_CHECKS 9')
    cases=[(2,1,2),(3,1,2),(4,1,2),(2,2,2),(3,2,2),(4,2,2),(2,3,2),(2,1,3),(3,1,3),(2,2,3),(2,3,3)]
    for q,r,m in cases:
        # 128^3 for r=3 over F2; direct pair table keeps computation bounded
        print('EXHAUSTIVE',count_direct(q,r,m))
    print('KRONECKER_TRIVIAL_EXTENSION_COMMUTING_TUPLES_OK',len(cases),'EXHAUSTIVE_CASES')
