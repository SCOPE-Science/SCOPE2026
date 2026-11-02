#!/usr/bin/env python3
"""Finite exact checks of odd-prime toroidal qudit graph-state cut rank.
Only Python standard library. Finite checks corroborate, not replace, a general proof.
"""
from math import gcd

def rank_mod(matrix, prime):
    a = [list(map(lambda x: x % prime, row)) for row in matrix]
    if not a: return 0
    nr, nc = len(a), len(a[0]); r=0
    for c in range(nc):
        pivot=next((i for i in range(r,nr) if a[i][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        v=pow(a[r][c],-1,prime)
        for k in range(c,nc):a[r][k]=(a[r][k]*v)%prime
        for i in range(r+1,nr):
            if a[i][c]:
                factor=a[i][c]
                for k in range(c,nc):a[i][k]=(a[i][k]-factor*a[r][k])%prime
        r+=1
        if r==nr:break
    return r

def v_p(x,p):
    k=0
    while x%p==0:x//=p;k+=1
    return k

def cut_matrix(m,n):
    even=[(x,y) for x in range(m) for y in range(n) if (x+y)%2==0]
    odd =[(x,y) for x in range(m) for y in range(n) if (x+y)%2==1]
    idx={z:j for j,z in enumerate(odd)}
    out=[[0]*len(odd) for _ in even]
    for k,(x,y) in enumerate(even):
        for z in [((x+1)%m,y),((x-1)%m,y),(x,(y+1)%n),(x,(y-1)%n)]:
            out[k][idx[z]]+=1
    return out

def local_product_matrix(P,Q):
    # Multiply by h=(s-t)(s+t+st)=(s^2+s^2*t-t^2-s*t^2)
    basis=[(i,j) for i in range(P) for j in range(Q)]
    idx={b:k for k,b in enumerate(basis)}
    mat=[[0]*len(basis) for _ in basis]
    terms=[(2,0,1),(2,1,1),(0,2,-1),(1,2,-1)]
    for col,(i,j) in enumerate(basis):
        for da,db,coef in terms:
            b=(i+da,j+db)
            if b in idx:mat[idx[b]][col]+=coef
    return mat

def main():
    grids=0; equal=unequal=0
    for p in [3,5,7,11]:
        for m in range(4,27,2):
            for n in range(4,27,2):
                if m*n>310:continue
                actual=m*n//2-rank_mod(cut_matrix(m,n),p)
                eq=v_p(m,p)==v_p(n,p)
                target=gcd(m,n)-int(eq)
                assert actual==target,(p,m,n,actual,target)
                grids+=1
                if eq:equal+=1
                else:unequal+=1
    local=0
    for p in [3,5]:
        powers=[1,p,p*p]
        for P in powers:
            for Q in powers:
                if P*Q>100:continue
                actual=P*Q-rank_mod(local_product_matrix(P,Q),p)
                expected=2*min(P,Q)-int(P==Q)
                assert actual==expected,(p,P,Q,actual,expected)
                local+=1
    examples=[(3,4,6),(5,4,6),(3,6,18),(5,6,18),(3,6,6),(7,8,14)]
    for p,m,n in examples:
        r=rank_mod(cut_matrix(m,n),p)
        print(f'example p={p} size={m}x{n}: rank={r}, deficit={m*n//2-r}, equal_valuations={v_p(m,p)==v_p(n,p)}')
    print(f'PASS grid ranks: {grids} exact Gaussian eliminations (equal={equal}, unequal={unequal})')
    print(f'PASS local intersection multiplicities: {local} exact finite-algebra eliminations')
    print('All assertions passed.')

if __name__=='__main__':main()
