#!/usr/bin/env python3
"""Finite checks supporting the double-star equivariant first-top-degree theorem."""
import itertools, math
from fractions import Fraction


def mons(n,k):
    if k==0: return [(0,)*n]
    if n==1: return [(k,)]
    return [(i,)+z for i in range(k+1) for z in mons(n-1,k-i)]

def rank_mod(rows,p):
    if not rows: return 0
    a=[[v%p for v in row] for row in rows]
    m=len(a); n=len(a[0]); r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if a[i][j]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        d=pow(a[r][j],-1,p)
        a[r]=[v*d%p for v in a[r]]
        for i in range(r+1,m):
            if a[i][j]:
                t=a[i][j]; a[i]=[(x-t*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==m: break
    return r

def differential(a,b,weight):
    # variables y,u_0..u_(a-1),v_0..v_(b-1)
    N=1+a+b; k=weight-2
    pols=mons(N,k); dest=mons(N,k+1)
    src=[(i,j,e) for i in range(a) for j in range(b) for e in pols]
    dst=[('A',i,e) for i in range(a) for e in dest]+[('B',j,e) for j in range(b) for e in dest]
    row={x:h for h,x in enumerate(dst)}
    mat=[[0]*len(src) for _ in dst]
    for col,(i,j,e) in enumerate(src):
        u=list(e);u[1+i]+=1
        v=list(e);v[1+a+j]+=1
        mat[row[('B',j,tuple(u))]][col]+=1
        mat[row[('A',i,tuple(v))]][col]-=1
    return mat,len(src),len(dst)

def rel_perm(i,j,a):
    # image of exterior generator e_i wedge e_j under adjacent swap a<->a+1
    f=lambda x:a+1 if x==a else a if x==a+1 else x
    x,y=f(i),f(j)
    return (min(x,y),max(x,y)),(1 if x<y else -1)

def exterior_actions(m):
    pairs=list(itertools.combinations(range(m),2)); index={p:i for i,p in enumerate(pairs)}
    out=[]
    for s in range(m-1):
        T=[[0]*len(pairs) for _ in pairs]
        for j,(i,k) in enumerate(pairs):
            p,sign=rel_perm(i,k,s)
            T[index[p]][j]=sign
        out.append(T)
    return out

def tensor_actions(a,b):
    A=exterior_actions(a); B=exterior_actions(b)
    da=math.comb(a,2);db=math.comb(b,2);d=da*db
    out=[]
    for T in A:
        Z=[[0]*d for _ in range(d)]
        for x in range(da):
            for y in range(da):
                if T[x][y]:
                    for j in range(db): Z[x*db+j][y*db+j]=T[x][y]
        out.append(Z)
    for T in B:
        Z=[[0]*d for _ in range(d)]
        for x in range(da):
            for i in range(db):
                for j in range(db):
                    if T[i][j]: Z[x*db+i][x*db+j]=T[i][j]
        out.append(Z)
    if a==b:
        Z=[[0]*d for _ in range(d)]
        for i in range(da):
            for j in range(db): Z[j*db+i][i*db+j]=-1
        out.append(Z)
    return out

def invariant_dimension(matrices,p):
    d=len(matrices[0]); rows=[]
    for T in matrices:
        for i in range(d):
            rows.append([T[i][j]-(i==j) for j in range(d)])
    return d-rank_mod(rows,p)

if __name__=='__main__':
    for a,b in [(2,2),(2,3),(3,3),(3,4)]:
        for n in (2,3,4):
            D,ns,nd=differential(a,b,n)
            r2=rank_mod(D,2)
            r5=rank_mod(D,5)
            expected=(math.comb(a,2)*math.comb(b,2) if n==4 else 0)
            assert ns-r2==expected,(a,b,n,'F2',ns-r2,expected)
            assert ns-r5==expected,(a,b,n,'F5',ns-r5,expected)
            print('kernel',a,b,n,'columns',ns,'rank2',r2,'rank5',r5,'dim',expected)
        act=tensor_actions(a,b)
        d=math.comb(a,2)*math.comb(b,2)
        inv2=invariant_dimension(act,2)
        inv5=invariant_dimension(act,5)
        assert (inv2,inv5)==(1,0),(a,b,inv2,inv5)
        print('invariants',a,b,'rank',d,'mod2',inv2,'mod5',inv5,'has_hub_swap',a==b)
    print('VERIFY_OK')
