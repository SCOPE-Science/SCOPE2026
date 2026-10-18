#!/usr/bin/env python3
"""Independent finite-algebra test of Frobenius-rectangle automorphism formulas.

Run: python3 verify.py. Uses only Python 3 standard library.
"""
from itertools import product
from math import prod

def parameters(p, exps):
    bounds = tuple(p**a for a in exps)
    basis = list(product(*(range(v) for v in bounds)))
    N = len(basis)
    U = tuple(prod(p**(b-a) for b in exps if b>a) for a in exps)
    m = {a: exps.count(a) for a in set(exps)}
    M = sum(N-u for u in U)-sum(t*t for t in m.values())
    def gl(t,q):
        return prod(q**t-q**j for j in range(t))
    count = p**M*prod(gl(t,p) for t in m.values())
    thickness = p**sum(a*u for a,u in zip(exps,U))
    return basis, bounds, U, M, count, thickness

def mul(a,b,basis,index,bounds,p):
    out=[0]*len(basis)
    for i,x in enumerate(a):
        if not x: continue
        ii=basis[i]
        for j,y in enumerate(b):
            if not y: continue
            jj=basis[j]; z=tuple(u+v for u,v in zip(ii,jj))
            if all(w<t for w,t in zip(z,bounds)):
                out[index[z]]=(out[index[z]]+x*y)%p
    return out

def is_aut(images, basis, bounds,p):
    d=len(bounds); N=len(basis); index={x:i for i,x in enumerate(basis)}
    def mult(a,b):return mul(a,b,basis,index,bounds,p)
    unit=[0]*N;unit[index[(0,)*d]]=1
    # Independently check the actual defining ideal, without using U.
    for f,b in zip(images,bounds):
        power=unit
        for _ in range(b): power=mult(power,f)
        if any(power):return False
    cols=[]
    for e in basis:
        v=unit[:]
        for i,ei in enumerate(e):
            for _ in range(ei):v=mult(v,images[i])
        cols.append(v)
    rows=[[cols[j][i] for j in range(N)] for i in range(N)]
    rank=0
    for j in range(N):
        pivot=next((i for i in range(rank,N) if rows[i][j]%p),None)
        if pivot is None:continue
        rows[pivot],rows[rank]=rows[rank],rows[pivot]
        inv=pow(rows[rank][j],-1,p)
        rows[rank]=[(x*inv)%p for x in rows[rank]]
        for i in range(rank+1,N):
            c=rows[i][j]%p
            if c:rows[i]=[(x-c*y)%p for x,y in zip(rows[i],rows[rank])]
        rank+=1
    return rank==N

def exhaustive(p,exps):
    basis,bounds,U,M,formula,thick=parameters(p,exps)
    N=len(basis);d=len(exps); zero=(0,)*d
    vecs=[]
    for coords in product(range(p),repeat=N-1):vecs.append((0,)+coords)
    # Basis lexicographic begins with unit.
    num=0
    for images in product(vecs,repeat=d):
        if is_aut(images,basis,bounds,p):num+=1
    assert num==formula,(p,exps,num,formula)
    print('PASS exhaustive:',f'p={p} exps={exps}',f'actual={num}',f'expected={formula}',f'U={U}',f'thickness={thick}')

def small_rank_check():
    # Check Frobenius survival counts directly in three-dimensional example.
    p,exps=2,(1,1,2)
    B,bounds,U,M,formula,thick=parameters(p,exps)
    for a,u in zip(exps,U):
        survives=[m for m in B if all(mj*p**a<bd for mj,bd in zip(m,bounds))]
        assert len(survives)==u,(a,len(survives),u)
    assert U==(2,2,1) and M==3*(len(B))-sum(U)-(2**2+1**2)
    print('PASS structural:',f'p={p} exps={exps}',f'N={len(B)} U={U}',f'dim_reduced={sum(len(B)-u for u in U)}',f'dim_Lie={len(exps)*len(B)}',f'thickness={thick}')

if __name__=='__main__':
    exhaustive(2,(1,))
    exhaustive(2,(2,))
    exhaustive(3,(1,))
    exhaustive(2,(1,1))
    exhaustive(2,(1,2))
    small_rank_check()
    print('VERIFY_OK')
