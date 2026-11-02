#!/usr/bin/env python3
"""Exact E7-root harmonic sampling spectral certificate (standard library only)."""
from itertools import combinations
from fractions import Fraction as F
from math import comb

def roots():
    vs=[]
    for i in range(8):
        for j in range(8):
            if i!=j:
                x=[0]*8; x[i]=2; x[j]=-2; vs.append(tuple(x))
    for inds in combinations(range(8),4):
        s=set(inds); vs.append(tuple(1 if i in s else -1 for i in range(8)))
    assert len(vs)==126 and len(set(vs))==126
    reps=sorted({min(v,tuple(-a for a in v)) for v in vs})
    assert len(reps)==63
    return reps

def dot(a,b): return sum(x*y for x,y in zip(a,b))

def Gegenbauer(k,t):
    a,b=F(1),F(t)
    if k==0: return a
    for j in range(1,k):
        a,b=b,F(2*j+5,j+5)*t*b-F(j,j+5)*a
    return b

def laplace_ubound(m):
    # E [(1-3/4*(1-Z^2))^m], Z has density proportional (1-Z^2)^(3/2)
    out=F(0)
    poch= lambda a,j: __import__('functools').reduce(lambda r,i:r*(a+i),range(j),F(1))
    for j in range(m+1):
        out+=comb(m,j)*F(-3,4)**j*poch(F(5,2),j)/poch(F(3),j)
    return out

def moment(m):
    z=F(1)
    for j in range(m): z*=F(2*j+1,2*j+6)
    return z

def verify():
    x=roots(); n=len(x)
    assert all(sum(v)==0 and dot(v,v)==8 for v in x)
    B=[[0 if i==j else dot(x[i],x[j])//4 for j in range(n)] for i in range(n)]
    assert all(dot(x[i],x[j]) in (-4,0,4) for i in range(n) for j in range(n) if i!=j)
    assert all(sum(B[i][j]**2 for j in range(n))==32 for i in range(n))
    # Full 8 x 8 tight-frame identity, exact integers.
    assert all(sum(x[i][a]*x[i][b] for i in range(n)) == (63 if a==b else -9) for a in range(8) for b in range(8))
    # Strongly regular unsigned and rank-7 signed spectra, exact 63x63 identities.
    A=[[abs(v) for v in row] for row in B]
    assert all(sum(A[i][h]*A[h][j] for h in range(n)) == 16+(16 if i==j else 0) for i in range(n) for j in range(n))
    assert all(sum(B[i][h]*B[h][j] for h in range(n)) == 14*B[i][j]+(32 if i==j else 0) for i in range(n) for j in range(n))
    assert sum(sum(row) for row in A)==63*32
    assert F(laplace_ubound(4))==F(1437,32768)
    assert F(laplace_ubound(6))==F(304825,16777216)
    assert moment(6)==F(33,4096)
    assert 16*laplace_ubound(4)<1
    assert 32*laplace_ubound(6)+30*moment(6)<1
    assert all(2*laplace_ubound(6)+5*moment(6)<1 for _ in [0])
    # finite low degrees: number of positive eigenvalues on 126 samples
    ranks=[]
    for k in range(13):
        u=Gegenbauer(k,F(1,2)); v=Gegenbauer(k,F(0))
        if k%2:
            eig=[(2*(1+16*u),7),(2*(1-2*u),56)]
        else:
            eig=[(2*(1+32*u+30*v),1),(2*(1+4*u-5*v),27),(2*(1-4*u+3*v),35)]
        assert all(val>=0 for val,mul in eig), (k,eig)
        rank=sum(mul for val,mul in eig if val>0)
        ranks.append(rank)
        print(k,str(u),str(v),[(str(a),b) for a,b in eig],rank)
    assert ranks[:7]==[1,7,27,56,62,63,63],ranks
    assert ranks[7:]==[63]*6
    assert all(ranks[k]+ranks[k+1]<126 for k in range(5))
    assert ranks[5]+ranks[6]==126
    # Direct kernel action on one test vector / row sum for the degree 4 and 6 even sectors.
    for k in (0,2,4,6,8,10,12):
        u=Gegenbauer(k,F(1,2));v=Gegenbauer(k,F(0))
        diag=2*(1+32*u+30*v)
        assert all(2*(1+sum((u if A[i][j] else v) for j in range(n) if j!=i))==diag for i in range(n))
    print('E7_ROOT_HARMONIC_CERTIFICATE_OK')

if __name__=='__main__': verify()
