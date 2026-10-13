#!/usr/bin/env python3
"""Direct enumeration of centralizer dimensions in three-vertex path algebras."""
from collections import Counter
from itertools import product

def gf_mul(x,y,q):
    if q==4:
        z=0
        for i in range(2):
            for j in range(2):
                if (x>>i)&1 and (y>>j)&1: z^=1<<(i+j)
        # x^2+x+1 = 0
        if z&8: z^=0b1110
        if z&4: z^=0b111
        return z
    return x*y%q

def gf_add(x,y,q):return x^y if q==4 else (x+y)%q

def gf_neg(x,q):return x if q==4 else (-x)%q

def gf_inv(x,q):
    for t in range(1,q):
        if gf_mul(x,t,q)==1:return t
    raise ValueError(x)

def centralizer_dim(a,r,s,q):
    d=3+r+s+r*s
    ed=[(0,0),(1,1),(2,2)]
    ed += [(0,1)]*r+[(1,2)]*s+[(0,2)]*(r*s)
    # pair coordinates are a multigraph, with distinct arrow basis identified by index
    mult={}
    for i in range(3,3+r):
        for j in range(3+r,3+r+s):
            mult[(i,j)]=3+r+s+(i-3)*s+(j-3-r)
    # multiplication on basis
    def basis_mul(i,j):
        u,v=ed[i];w,z=ed[j]
        if v!=w:return -1
        if i<3:return j
        if j<3:return i
        return mult.get((i,j),-1)
    # columns of ad_a for each basis vector j
    mat=[[0]*d for _ in range(d)]
    for i,ai in enumerate(a):
        if not ai:continue
        for j in range(d):
            k=basis_mul(i,j)
            if k>=0:mat[k][j]=gf_add(mat[k][j],ai,q)
            k=basis_mul(j,i)
            if k>=0:mat[k][j]=gf_add(mat[k][j],gf_neg(ai,q),q)
    rank=0
    for col in range(d):
        pivot=next((i for i in range(rank,d) if mat[i][col]),None)
        if pivot is None:continue
        mat[rank],mat[pivot]=mat[pivot],mat[rank]
        inv=gf_inv(mat[rank][col],q)
        for j in range(col,d):mat[rank][j]=gf_mul(mat[rank][j],inv,q)
        for row in range(rank+1,d):
            if mat[row][col]:
                v=mat[row][col]
                for j in range(col,d):
                    mat[row][j]=gf_add(mat[row][j],gf_neg(gf_mul(v,mat[rank][j],q),q),q)
        rank+=1
        if rank==d:break
    return d-rank

def predicted(q,r,s):
    d=3+r+s+r*s; z=Counter()
    def add(n,dim):
        if n:z[dim]+=n
    # distinct eigenvalues and two equal eigenvalues
    add(q*(q-1)*(q-2)*q**(r+s+r*s),3)
    add(q*(q-1)*q**(s+r*s),r+3)
    add(q*(q-1)*q**(s+r*s)*(q**r-1),r+2)
    add(q*(q-1)*q**(r+r*s),s+3)
    add(q*(q-1)*q**(r+r*s)*(q**s-1),s+2)
    add(q*(q-1)*q**(r+s),r*s+3)
    add(q*(q-1)*q**(r+s)*(q**(r*s)-1),r*s+2)
    # scalar diagonal and radical
    add(q,d)
    add(q*(q**(r*s)-1),d-1)
    add(q*(q**r-1)*q**s,r*s+r+2)
    add(q*(q**r-1)*(q**(r*s)-q**s),r*s+r+1)
    add(q*(q**s-1)*q**r,r*s+s+2)
    add(q*(q**s-1)*(q**(r*s)-q**r),r*s+s+1)
    add(q*(q**r-1)*(q**s-1)*q**(r*s),r*s+2)
    assert sum(z.values())==q**d,(q,r,s,sum(z.values()),q**d)
    return z

def check(q,r,s):
    d=3+r+s+r*s; expected=predicted(q,r,s);got=Counter()
    for coords in product(range(q),repeat=d):got[centralizer_dim(coords,r,s,q)]+=1
    assert got==expected,(q,r,s,got,expected)
    total=sum(m*q**c for c,m in expected.items());print('CHECK_OK',q,r,s,'dimension',d,'spectrum',sorted(got.items()),'commuting_pairs',total,'prob_numerator',total,'prob_denominator',q**(2*d))

if __name__=='__main__':
    for p in [(2,1,1),(3,1,1),(4,1,1),(2,2,1),(2,1,2),(2,2,2),(3,2,1),(5,1,1),(4,2,1)]:check(*p)
    print('VERIFY_OK')
