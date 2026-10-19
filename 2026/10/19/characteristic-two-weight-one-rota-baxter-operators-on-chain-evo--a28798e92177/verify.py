#!/usr/bin/env python3
"""Finite-field independent enumeration of characteristic-2 RB maps on chain evolution algebras."""
from itertools import product

def mult(a, b, f, poly):
    res=0
    for _ in range(f):
        if b&1: res^=a
        b>>=1
        a<<=1
        if a & (1<<f): a ^= poly
    return res

def pow_field(a,k,f,poly):
    r=1
    while k:
        if k&1: r=mult(r,a,f,poly)
        a=mult(a,a,f,poly); k//=2
    return r

def sq(v,f,poly):
    return (0,)+tuple(mult(v[i],v[i],f,poly) for i in range(len(v)-1))

def prod(x,y,f,poly):
    return (0,)+tuple(mult(x[i],y[i],f,poly) for i in range(len(x)-1))

def scal(x,v,f,poly): return tuple(mult(x, a, f,poly) for a in v)
def xor(a,b): return tuple(x^y for x,y in zip(a,b))

def is_RB(first,f,poly):
    n=len(first)
    cols=[first]
    for _ in range(n-1):cols.append(sq(cols[-1],f,poly))
    for i in range(n):
        for j in range(i,n):
            left=prod(cols[i],cols[j],f,poly)
            if i==j: right=cols[i+1] if i+1<n else (0,)*n
            else:
                right=(0,)*n
                if j+1<n:right=xor(right, scal(cols[i][j],cols[j+1],f,poly))
                if i+1<n:right=xor(right, scal(cols[j][i],cols[i+1],f,poly))
            if left!=right:return False
    return True

def formula_set(n,f,poly):
    q=1<<f
    out=set()
    for a,b in product(range(q),repeat=2): out.add((a,)+(0,)*(n-2)+(b,))
    for j in range(2,n):
        for u in range(1,q):
            for a1,b in product((0,1),range(q)):
                v=[0]*n;v[0]=a1;v[-1]=b
                L=j-1
                for ell in range(1,(n-2)//L+1):
                    pos=1+ell*L
                    if pos>=n: break
                    exponent=sum(2**(k*L) for k in range(ell))
                    v[pos-1]=pow_field(u,exponent,f,poly)
                out.add(tuple(v))
    return out

def rank(v, f, poly):
    n=len(v)
    cols=[v]
    for _ in range(n-1): cols.append(sq(cols[-1],f,poly))
    mat=[[cols[c][r] for c in range(n)] for r in range(n)]
    k=0
    for c in range(n):
        pivot=next((r for r in range(k,n) if mat[r][c]),None)
        if pivot is None:continue
        mat[k],mat[pivot]=mat[pivot],mat[k]
        inv=pow_field(mat[k][c],(1<<f)-2,f,poly)
        for cc in range(c,n): mat[k][cc]=mult(inv,mat[k][cc],f,poly)
        for r in range(n):
            if r==k:continue
            scalar=mat[r][c]
            if scalar:
                for cc in range(c,n):mat[r][cc]^=mult(scalar,mat[k][cc],f,poly)
        k+=1
        if k==n:break
    return k

def run(n,f,poly):
    q=1<<f
    spec=formula_set(n,f,poly)
    exp=q*q + 2*(n-2)*q*(q-1)
    assert len(spec)==exp,(n,q,'incorrect parameter injectivity',len(spec),exp)
    accepted={v for v in product(range(q),repeat=n) if is_RB(v,f,poly)}
    assert spec==accepted,(n,q,'classification mismatch',len(spec),len(accepted),list(spec^accepted)[:4])
    from collections import Counter
    dist=Counter(rank(v,f,poly) for v in accepted)
    predicted={0:1,1:q-1,n:(n-1)*q*(q-1)}
    for r in range(2,n):predicted[r]=q*(q-1)
    assert dict(dist)==predicted,(n,q,'rank distribution',dist,predicted)
    print('PASS q=%d n=%d maps=%d total=%d ranks=%s'%(q,n,len(accepted),q**n,sorted(dist.items())))

if __name__=='__main__':
    for n in range(2,9):run(n,1,0b11)
    for n in range(2,7):run(n,2,0b111)
    for n in range(2,6):run(n,3,0b1011)
    for n in range(2,5):run(n,4,0b10011)
