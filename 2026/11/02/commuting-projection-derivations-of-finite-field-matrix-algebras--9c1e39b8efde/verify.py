#!/usr/bin/env python3
"""Reproducible finite-field census from original associative matrix multiplication.
No computer-algebra dependencies; ranks and pairs are counted by direct linear maps.
"""
import itertools
import math
from collections import Counter

class Field:
    def __init__(self,q):
        self.q=q
        assert q in (2,3,4,5)
        self.p=2 if q in (2,4) else q
    def add(self,a,b):return a^b if self.p==2 else (a+b)%self.p
    def sub(self,a,b):return a^b if self.p==2 else (a-b)%self.p
    def mul(self,a,b):
        if self.q==4:
            c=0
            for i in range(2):
                if (b>>i)&1:c^=a<<i
            if c&8:c^=0b1110
            if c&4:c^=0b111
            return c
        return (a*b)%self.p
    def dot(self,a,b):
        v=0
        for x,y in zip(a,b):v=self.add(v,self.mul(x,y))
        return v

def matmul(f,n,A,B):
    return tuple(f.dot((A[i*n+k] for k in range(n)),(B[k*n+j] for k in range(n)))
                 for i in range(n) for j in range(n))
def ad(f,n,A,X):
    return tuple(f.sub(a,b) for a,b in zip(matmul(f,n,A,X),matmul(f,n,X,A)))
def central(f,n,A):
    return all(A[i*n+j]==0 for i in range(n) for j in range(n) if i!=j) and len({A[i*n+i] for i in range(n)})==1

def glorder(q,n):return math.prod(q**n-q**i for i in range(n))
def gauss(q,n,r):
    return math.prod(q**(n-j)-1 for j in range(r))//math.prod(q**(r-j)-1 for j in range(r))
def idem(q,n):
    return sum(gauss(q,n,r)*q**(r*(n-r)) for r in range(n+1))
def irred(q,n):
    return glorder(q,n)//glorder(q*q,n//2) if n%2==0 else 0

def expected(q,n):
    if q%2:return (1,Counter({1:1}),Counter({0:1}))
    split={r:gauss(q,n,r)*q**(r*(n-r))//(2 if r*2==n else 1)
           for r in range(1,n//2+1)}
    nonsplit=glorder(q,n)//(2*glorder(q*q,n//2)) if n%2==0 else 0
    total=1+sum(split.values())+nonsplit
    degree=Counter({total:1})
    rank=Counter({0:1})
    for r,cnt in split.items():
        s=n-r
        degree[(idem(q,r)*idem(q,s)+irred(q,r)*irred(q,s))//2]+=cnt
        rank[2*r*s]+=cnt
    if nonsplit:
        degree[idem(q*q,n//2)]+=nonsplit
        rank[n*n//2]+=nonsplit
    return total,degree,rank

def run(q,n,full_operator_pair_check=True):
    f=Field(q); d=n*n
    units=[tuple(int(j==i) for j in range(d)) for i in range(d)]
    solutions=[]
    ranks=Counter()
    for tail in itertools.product(range(q),repeat=d-1):
        A=(0,)+tail
        cols=[ad(f,n,A,E) for E in units]
        if any(ad(f,n,A,col)!=col for col in cols):continue
        solutions.append((A,cols))
        # Rank of the image of D by row reduction of the d x d column matrix.
        rows=[[cols[j][i] for j in range(d)] for i in range(d)];r=0
        for k in range(d):
            pivot=next((i for i in range(r,d) if rows[i][k]!=0),None)
            if pivot is None:continue
            rows[r],rows[pivot]=rows[pivot],rows[r]
            inv=next(a for a in range(1,q) if f.mul(a,rows[r][k])==1)
            for j in range(k,d):rows[r][j]=f.mul(inv,rows[r][j])
            for i in range(r+1,d):
                c=rows[i][k]
                if c:
                    for j in range(k,d):rows[i][j]=f.sub(rows[i][j],f.mul(c,rows[r][j]))
            r+=1
        ranks[r]+=1
    deg=Counter(); total_pairs=0
    for A,acols in solutions:
        degree=0
        for B,bcols in solutions:
            # First compute commutator directly in M_n. When it is central,
            # its inner derivation vanishes on every matrix unit.
            AB=matmul(f,n,A,B);BA=matmul(f,n,B,A)
            comm=tuple(f.sub(u,v) for u,v in zip(AB,BA))
            same=central(f,n,comm)
            if full_operator_pair_check:
                direct=all(
                    tuple(f.sub(x,y) for x,y in zip(ad(f,n,A,bcols[j]),ad(f,n,B,acols[j])))==(0,)*d
                    for j in range(d)
                )
                assert direct==same,(q,n,A,B)
            if same:degree+=1
        deg[degree]+=1;total_pairs+=degree
    predicted_total,predicted_degree,predicted_rank=expected(q,n)
    assert len(solutions)==predicted_total,(q,n,len(solutions),predicted_total)
    assert deg==predicted_degree,(q,n,deg,predicted_degree)
    assert ranks==predicted_rank,(q,n,ranks,predicted_rank)
    assert total_pairs==sum(k*v for k,v in predicted_degree.items())
    print('PASS',f'q={q}',f'n={n}',f'maps={len(solutions)}',f'ordered_commuting_pairs={total_pairs}',
          f'degree_distribution={sorted(deg.items())}',f'rank_distribution={sorted(ranks.items())}',
          f'direct_operator_compositions={full_operator_pair_check}')

if __name__=='__main__':
    for q,n,direct in [(2,1,True),(3,2,True),(5,2,True),(2,2,True),(4,2,True),(2,3,True),(2,4,False)]:
        run(q,n,direct)
    print('COMMUTING_PROJECTION_DERIVATIONS_OK 7_EXHAUSTIVE_CONFIGURATIONS')
