"""Finite independent checks of exact intrinsic volumes for K_{2,q} graphical zonotopes.
The asymptotic proof is analytical and not certified by this finite computation.
"""
from __future__ import annotations
import itertools
import math


def theory(q: int, k: int):
    joined = (math.comb(q,k-1)*(k-1)*2**(k-2)*math.sqrt(k+1)
              if 2 <= k <= q+1 else 0.0)
    separated = (math.comb(q,k)*sum(math.comb(k,a)*math.sqrt((a+1)*(k-a+1))
                                  for a in range(k+1)) if 0<=k<=q else 0.0)
    return joined,separated


def determinant_integer(M):
    """Fraction-free exact determinant of a square integer matrix."""
    n=len(M)
    if not n:return 1
    A=[row[:] for row in M]
    sign=1;prev=1
    for j in range(n-1):
        if A[j][j]==0:
            pivot=next((i for i in range(j+1,n) if A[i][j]),None)
            if pivot is None:return 0
            A[j],A[pivot]=A[pivot],A[j];sign=-sign
        diag=A[j][j]
        for i in range(j+1,n):
            for t in range(j+1,n):
                num=A[i][t]*diag-A[i][j]*A[j][t]
                assert num%prev==0
                A[i][t]=num//prev
        for i in range(j+1,n):A[i][j]=0
        prev=diag
    return sign*A[-1][-1]


def brute(q: int):
    edges=[(0,j+2) for j in range(q)]+[(1,j+2) for j in range(q)]
    n=q+2
    values=[ [0.0,0.0,0,0] for _ in range(q+2)]
    forest_count=0
    gram_checks=0
    for bits in range(1 << len(edges)):
        k=bits.bit_count()
        if k>q+1: continue
        parent=list(range(n))
        def root(v):
            while parent[v]!=v:
                v=parent[v]
            return v
        chosen=[]; valid=True
        for idx,(u,v) in enumerate(edges):
            if bits>>idx&1:
                ru,rv=root(u),root(v)
                if ru==rv:
                    valid=False;break
                parent[ru]=rv
                chosen.append((u,v))
        if not valid:continue
        sizes={}
        for v in range(n):
            a=root(v)
            sizes[a]=sizes.get(a,0)+1
        gram=math.prod(sizes.values())
        weight=math.sqrt(gram)
        join = root(0)==root(1)
        values[k][0 if join else 1]+=weight
        values[k][2 if join else 3]+=1
        forest_count+=1
        # Independent Gram determinant for every forest through q=4.
        if q<=4:
            columns=[]
            for u,v in chosen:
                col=[0]*n
                col[u]=1;col[v]=-1
                columns.append(col)
            matrix=[[sum(x*y for x,y in zip(ci,cj)) for cj in columns]
                    for ci in columns]
            d=determinant_integer(matrix)
            assert d==gram, (q,bits,d,gram)
            gram_checks+=1
    for k in range(q+2):
        actual=values[k][:2]
        expected=theory(q,k)
        for a,b in zip(actual,expected):
            assert abs(a-b)<=1e-10*max(1,abs(b)),(q,k,actual,expected)
        uj=(math.comb(q,k-1)*(k-1)*2**(k-2) if 2<=k<=q+1 else 0)
        ud=(math.comb(q,k)*2**k if 0<=k<=q else 0)
        assert values[k][2:] == [uj,ud], (q,k,values[k][2:],[uj,ud])
    return forest_count,gram_checks


def ratio_stable(q:int,k:int)->float:
    # Conditional expected square-root factors via a normalized symmetric binomial PMF.
    if k<=1:return 0.0
    if k==q+1:return float('inf')
    weights=[math.exp(math.lgamma(k+1)-math.lgamma(a+1)-math.lgamma(k-a+1)-k*math.log(2)) for a in range(k+1)]
    mean=sum(p*math.sqrt((a+1)*(k-a+1)) for a,p in enumerate(weights))
    return (k/(q-k+1))*(k-1)*math.sqrt(k+1)/(4*mean)


def main():
    forests=0;gram=0
    for q in range(2,8):
        f,g=brute(q)
        forests+=f;gram+=g
    print('FINITE forest_checks=',forests,'exact_gram_checks=',gram)
    for t in (0.5,1.0,2.0):
        q=100000
        k=round(t*q**(2/3))
        r=ratio_stable(q,k)
        p=r/(1+r)
        target=t**1.5/(2+t**1.5)
        print('critical:',q,t,k,round(p,8),round(target,8))
        assert abs(p-target)<0.02
    for c in (0.5,1.0,2.0):
        q=100000
        k=round(c*math.sqrt(q))
        ratio=k*(k-1)/(4*(q-k+1))
        prob=ratio/(1+ratio)
        target=c*c/(4+c*c)
        print('uniform:',q,c,k,round(prob,8),round(target,8))
        assert abs(prob-target)<0.01
    print('VERIFY_OK')

if __name__=='__main__':main()
