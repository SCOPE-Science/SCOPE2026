#!/usr/bin/env python3
from itertools import product
from fractions import Fraction
from collections import Counter

def levels_for(rs):
    levels=[]; level=[]; s=0
    for i,r in enumerate(rs):
        L=list(range(s,s+r)); levels.append(L); level += [i]*r; s+=r
    return levels,level

def monotone(f,rs):
    levels,level=levels_for(rs)
    for i in range(len(rs)):
        for j in range(i+1,len(rs)):
            for x in levels[i]:
                for y in levels[j]:
                    fx,fy=f[x],f[y]
                    if not (level[fx] < level[fy] or fx == fy):
                        return False
    return True

def predicted_rank(f,rs):
    levels,level=levels_for(rs)
    rank=1
    for i,L in enumerate(levels):
        if any(level[f[x]] != i for x in L):
            return 0
        rank *= len({f[x] for x in L})-1
    return rank

def matrix_rank(cols):
    if not cols:
        return 0
    A=[[Fraction(x) for x in row] for row in zip(*cols)]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((q for q in range(r,m) if A[q][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for q in range(m):
            if q!=r and A[q][c]:
                z=A[q][c]
                A[q]=[A[q][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def actual_top_rank(f,rs):
    levels,level=levels_for(rs); h=len(rs)
    top=list(product(*levels)); row={t:i for i,t in enumerate(top)}
    choices=[[(L[j],L[-1]) for j in range(len(L)-1)] for L in levels]
    cols=[]
    for pairs in product(*choices):
        v=[0]*len(top)
        for bits in product((0,1), repeat=h):
            src=tuple(pairs[i][bits[i]] for i in range(h))
            coeff=-1 if sum(bits)%2 else 1
            img=tuple(f[x] for x in src)
            if tuple(level[z] for z in img)==tuple(range(h)):
                v[row[img]] += coeff
        cols.append(v)
    return matrix_rank(cols)

def check(rs):
    n=sum(rs); mono=0; nonzero=0; hist=Counter()
    for f in product(range(n), repeat=n):
        if not monotone(f,rs): continue
        mono+=1
        a=actual_top_rank(f,rs)
        p=predicted_rank(f,rs)
        assert a==p,(rs,f,a,p)
        hist[a]+=1
        nonzero += (a>0)
    predicted=1
    for r in rs:
        predicted *= r**r-r
    assert nonzero==predicted,(rs,nonzero,predicted)
    return mono,nonzero,dict(sorted(hist.items()))

def main():
    expected={
        (2,2):(36,4,{0:32,1:4}),
        (2,3):(197,48,{0:149,1:36,2:12}),
        (2,2,2):(446,8,{0:438,1:8}),
    }
    for rs,exp in expected.items():
        got=check(rs)
        assert got==exp,(rs,got,exp)
        print("levels=%s monotone=%d nonzero_top=%d rank_hist=%s"%(rs,got[0],got[1],got[2]))
    print("VERIFY_OK")
if __name__=="__main__":
    main()
