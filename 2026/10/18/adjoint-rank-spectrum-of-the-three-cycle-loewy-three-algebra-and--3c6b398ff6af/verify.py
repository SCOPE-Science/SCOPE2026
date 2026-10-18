#!/usr/bin/env python3
"""Finite-field checks for the rank enumerator of the length-three cyclic path algebra.
All tables are constructed from path concatenation, independently of the proof's block ranks.
"""
from collections import Counter
from itertools import product

class Field:
    def __init__(self,q):
        self.q=q
        if q==4:
            self.add=lambda a,b:a^b
            # GF(4)=F2[t]/(t^2+t+1), encoded as bit-polynomials.
            def mult(a,b):
                z=0
                for i in range(2):
                    if (b>>i)&1:z^=a<<i
                if z&8:z^=0b1100
                if z&4:z^=0b111
                return z
            self.mul=mult
        else:
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
        self.neg=[next(y for y in range(q) if self.add(x,y)==0) for x in range(q)]
        self.inv=[None]+[next(y for y in range(1,q) if self.mul(x,y)==1) for x in range(1,q)]
        self.sub=lambda a,b:self.add(a,self.neg[b])

PATHS=[(i,length) for length in range(3) for i in range(3)]
PINDEX={p:k for k,p in enumerate(PATHS)}
PRODUCT=[[None]*9 for _ in range(9)]
for r,(i,a) in enumerate(PATHS):
    for s,(j,b) in enumerate(PATHS):
        if (i+a)%3==j and a+b<3:
            PRODUCT[r][s]=PINDEX[(i,a+b)]

def adjoint_matrix(element,F):
    out=[[0]*9 for _ in range(9)]
    for h in range(9):
        for j,value in enumerate(element):
            if not value:continue
            u=PRODUCT[j][h]
            v=PRODUCT[h][j]
            if u is not None:out[u][h]=F.add(out[u][h],value)
            if v is not None:out[v][h]=F.sub(out[v][h],value)
    return out

def matrix_rank(a,F):
    mat=[row[:] for row in a]
    r=0
    for j in range(9):
        pivot=next((i for i in range(r,9) if mat[i][j]),None)
        if pivot is None:continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        u=F.inv[mat[r][j]]
        for col in range(j,9):mat[r][col]=F.mul(mat[r][col],u)
        for i in range(r+1,9):
            if mat[i][j]:
                mul=mat[i][j]
                for col in range(j,9):mat[i][col]=F.sub(mat[i][col],F.mul(mul,mat[r][col]))
        r+=1
    return r

def expected_for_diagonal(q,kind):
    if kind=='equal':return {0:1,1:3*(q-1),2:q**3-3*q+2,3:3*(q-1)*q**3,4:(q-1)**2*(q+2)*q**3}
    if kind=='double':return {4:q**4,5:q**6-q**4}
    return {6:q**6}

def run(q):
    F=Field(q)
    reps=[('equal',(0,0,0)),('double',(0,0,1))]
    if q>=3:
        reps.append(('distinct',(0,1,2)))
    counters={}
    for kind,diag in reps:
        found=Counter()
        for rad in product(range(q),repeat=6):
            r=matrix_rank(adjoint_matrix(diag+rad,F),F)
            found[r]+=1
        expected={r:n for r,n in expected_for_diagonal(q,kind).items() if n}
        assert dict(sorted(found.items()))==expected,(q,kind,found,expected)
        counters[kind]=dict(sorted(found.items()))
    print('q=',q,'conditional_rank_counts=',counters)

if __name__=='__main__':
    for q in (2,3,4,5):run(q)
    print('VERIFY_OK')
