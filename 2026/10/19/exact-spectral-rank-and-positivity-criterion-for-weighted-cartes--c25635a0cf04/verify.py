#!/usr/bin/env python3
"""Exact rational spectral- and Fourier-side checks for star-box Cesaro mixing."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict


def projector(r, sector):
    n=r+1
    if sector=='0':
        return [[F(1,n) for _ in range(n)] for _ in range(n)]
    if sector=='R':
        v=(r,)+(-1,)*r
        return [[F(v[a]*v[b],r*(r+1)) for b in range(n)] for a in range(n)]
    if sector=='L':
        p0=projector(r,'0'); pr=projector(r,'R')
        return [[F(a==b)-p0[a][b]-pr[a][b] for b in range(n)] for a in range(n)]
    raise ValueError(sector)


def coeffs(r,sector):
    if sector=='0': return {0:F(1)}
    if sector=='L':
        return {0:F(r-2,r),-1:F(1,r),1:F(1,r)}
    if sector=='R':
        return {0:F(r-1,2*r),-2:F(r+1,4*r),2:F(r+1,4*r)}
    raise ValueError(sector)


def fourier_eigenvalue(rs,ws,sectors):
    freq={0:F(1)}
    for r,w,s in zip(rs,ws,sectors):
        nxt=defaultdict(F)
        for base,amount in freq.items():
            for k,c in coeffs(r,s).items():
                nxt[base+k*w]+=amount*c
        freq=dict(nxt)
    return freq.get(0,F(0))


def product_entry(matrices, rows,cols):
    v=F(1)
    for i,m in enumerate(matrices): v*=m[rows[i]][cols[i]]
    return v


def predicted_matrix(rs,ws):
    n=1
    for r in rs: n*=r+1
    vertices=list(product(*(range(r+1) for r in rs)))
    pcs={(j,s):projector(rs[j],s) for j in range(len(rs)) for s in '0LR'}
    eig={s:fourier_eigenvalue(rs,ws,s) for s in product('0LR',repeat=len(rs))}
    result=[[F(0) for _ in range(n)] for _ in range(n)]
    for a,va in enumerate(vertices):
        for b,vb in enumerate(vertices):
            result[a][b]=sum(lam*product_entry([pcs[j,s] for j,s in enumerate(sect)],va,vb) for sect,lam in eig.items())
    rank=sum((1 if s!='L' else rs[j]-1) for j,s in enumerate('')) if False else sum(
        (int(lam>0))*__import__('math').prod((rs[j]-1 if s=='L' else 1) for j,s in enumerate(sect)) for sect,lam in eig.items())
    return result,rank,eig


def spectral_local_coefficient(r,kind,a,b):
    # The factor 1/sqrt(r) for hub-leaf coordinates is handled globally.
    if kind==0:
        return (F(a==b)-F(1,r)) if (a>0 and b>0) else F(0)
    if a==0 and b==0:return F(1,2)
    if a==0 or b==0:return F(kind,2)
    return F(1,2*r)


def spectral_matrix(rs,ws):
    n=1
    for r in rs: n*=r+1
    vertices=list(product(*(range(r+1) for r in rs)))
    eigengroups=defaultdict(list)
    for signs in product((-1,0,1),repeat=len(rs)):
        eigengroups[sum(w*s for w,s in zip(ws,signs))].append(signs)
    out=[[F(0) for _ in range(n)] for _ in range(n)]
    for a,va in enumerate(vertices):
        for b,vb in enumerate(vertices):
            denom=__import__('math').prod(r for r,u,v in zip(rs,va,vb) if (u==0)!=(v==0))
            value=F(0)
            for group in eigengroups.values():
                component=F(0)
                for signs in group:
                    term=F(1)
                    for r,s,u,v in zip(rs,signs,va,vb):
                        term*=spectral_local_coefficient(r,s,u,v)
                    component+=term
                value+=component*component/denom
            out[a][b]=value
    return out


def rank_fraction(a):
    a=[row[:] for row in a]; n=len(a); pivots=0
    for j in range(n):
        k=next((k for k in range(pivots,n) if a[k][j]),None)
        if k is None:continue
        a[pivots],a[k]=a[k],a[pivots]
        x=a[pivots][j]
        for c in range(j,n): a[pivots][c]/=x
        for i in range(pivots+1,n):
            v=a[i][j]
            if v:
                for c in range(j,n):a[i][c]-=v*a[pivots][c]
        pivots+=1
        if pivots==n:break
    return pivots


def main():
    configs=[((2,),(1,)),((3,),(1,)),((4,),(1,)),
             ((2,2),(1,1)),((2,2),(1,2)),((2,2),(1,3)),
             ((2,3),(1,1)),((2,3),(2,1)),((2,3),(1,2)),
             ((3,3),(1,1)),((3,4),(1,2)),
             ((2,2,2),(1,1,1)),((2,2,2),(1,1,2)),
             ((2,2,2),(1,2,4)),((2,2,3),(1,1,1)),
             ((2,3,3),(1,1,2)),((2,2,4),(2,3,4))]
    matrix_entries=0
    for rs,ws in configs:
        predicted,rank,eigs=predicted_matrix(rs,ws)
        spectral=spectral_matrix(rs,ws)
        assert predicted==spectral, (rs,ws,'matrix disagreement')
        numerical_rank=rank_fraction(spectral)
        assert rank==numerical_rank,(rs,ws,rank,numerical_rank)
        all_ge3=all(r>=3 for r in rs)
        assert (rank==len(spectral))==all_ge3, (rs,ws,'positive-definite threshold')
        if all(r==2 for r in rs) and len(set(ws))==1:
            assert rank==(3**len(rs)+1)//2
        matrix_entries+=len(spectral)**2
        print('PROFILE',rs,ws,'rank',rank,'dim',len(spectral))
    print('VERIFY_OK exact_profiles=',len(configs),'matrix_entries=',matrix_entries,'methods=spectral_projectors,fourier_tensor,exact_rational_rank')

if __name__=='__main__': main()
