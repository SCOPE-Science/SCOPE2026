"""Reproduce finite angular-chain identities for radial Toeplitz operators on regular trees.

Run: python checker.py
Only finite matrices are tested; infinite statements require the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import numpy as np


def vertices(b,L):
    return [w for k in range(L+1) for w in product(range(b),repeat=k)]


def matrix(b,L,r):
    verts=vertices(b,L); a=[]
    for u in verts:
        row=[]
        for v in verts:
            if u==v: row.append(r**len(u))
            elif len(v)>len(u) and v[:len(u)]==u:
                row.append((r-1)*r**(len(v)-1))
            else: row.append(F(0))
        a.append(row)
    return verts,a


def wavelets(b):
    if b==4:
        return [[F(x,2) for x in arr] for arr in ((1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))]
    if b==2:
        return [[1/sqrt(2),-1/sqrt(2)]]
    raise ValueError


def angular_basis(b,L):
    verts=vertices(b,L)
    basis=[]
    wave=wavelets(b)
    for k in range(L+1):
        starts=[]
        if k==0: starts=[{():F(1)}]
        else:
            for p in product(range(b),repeat=k-1):
                for row in wave:
                    starts.append({p+(c,):val for c,val in enumerate(row)})
        for wi,start in enumerate(starts):
            for m in range(k,L+1):
                scale=F(1,2**(m-k)) if b==4 else 1/(sqrt(b)**(m-k))
                vec=[0]*len(verts)
                for vno,v in enumerate(verts):
                    if len(v)==m and v[:k] in start:
                        vec[vno]=start[v[:k]]*scale
                basis.append(((k,wi,m-k),vec))
    assert len(basis)==len(verts)
    return basis


def target(b,r,ind1,ind2):
    k,w,i=ind1; l,z,j=ind2
    if (k,w)!=(l,z) or i>j: return 0
    if i==j: return r**(k+i)
    return r**k * (r-1)*r**(j-1)*(sqrt(b)**(j-i) if b==2 else 2**(j-i))


def exact_test(b,L,r):
    verts,M=matrix(b,L,r)
    basis=angular_basis(b,L)
    U=[v for _,v in basis]
    n=len(verts)
    assert all(sum(U[i][t]*U[j][t] for t in range(n))==int(i==j)
               for i in range(n) for j in range(n))
    tU=[[sum(M[i][j]*U[c][j] for j in range(n)) for i in range(n)] for c in range(n)]
    checks=0
    for i,(label1,u) in enumerate(basis):
        for j,(label2,v) in enumerate(basis):
            value=sum(u[a]*tU[j][a] for a in range(n))
            assert value==target(b,r,label1,label2),(i,j,label1,label2,value,target(b,r,label1,label2))
            checks+=1
    # Independently recompute every matrix-square entry's finite HS sum using row levels.
    H2=sum(x*x for row in M for x in row)
    formula=sum(b**n*r**(2*n)*(1+b*(1-r)**2*sum((b*r*r)**k for k in range(L-n)))
                for n in range(L+1))
    assert H2==formula,(H2,formula)
    return n,checks,H2


def numeric_test(b,L,r):
    verts,M=matrix(b,L,F(r))
    basis=angular_basis(b,L)
    u=np.array([v for _,v in basis],dtype=float).T
    t=np.array(M,dtype=float)
    p=u.T @ t @ u
    target_matrix=np.array([[target(b,float(r),i[0],j[0]) for j in basis]
                            for i in basis],dtype=float)
    assert np.max(np.abs(u.T@u-np.eye(len(verts))))<2e-13
    assert np.max(np.abs(p-target_matrix))<2e-13
    ss=np.linalg.svd(t,compute_uv=False)
    bb=np.linalg.svd(target_matrix,compute_uv=False)
    assert np.max(abs(ss-bb))<2e-13
    for depth in range(L+1):
        assert ss[b**depth-1] >= float(r)**depth-1e-12
    return len(verts),max(abs(ss-bb))


if __name__=='__main__':
    exact_configs=((4,2,F(1,4)),(4,2,F(1,5)),(4,1,F(1,3)))
    total=0
    for b,L,r in exact_configs:
        n,checks,h2=exact_test(b,L,r)
        print('EXACT PASS',b,L,str(r),'dimension',n,'block-inner-products',checks,'HS-square',h2)
        total+=checks
    for b,L,r in ((2,5,F(1,4)),(2,5,F(1,2)),(4,3,F(1,5))):
        n,err=numeric_test(b,L,r)
        print('NUMERIC PASS',b,L,str(r),'dimension',n,'max-spectrum-error',err)
    print('TOTAL_EXACT_BLOCK_ENTRIES',total)
    print('PASS')
