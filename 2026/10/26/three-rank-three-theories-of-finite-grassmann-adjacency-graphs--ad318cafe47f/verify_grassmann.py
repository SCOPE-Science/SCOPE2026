#!/usr/bin/env python3
"""Independent finite-field subspace and first-order pair-profile verification.

Only finite computations are checked; the uniform theorem requires a separate proof.
"""
from itertools import combinations, product
from math import comb


def field(q):
    if q in (2,3,5):
        add=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
        inv={x:pow(x,q-2,q) for x in range(1,q)}
    elif q == 4:
        add=lambda a,b:a^b
        def mul(a,b):
            out=0
            if b&1:out^=a
            if b&2:out^=a<<1
            if out&8:out^=0b1100 # remove x^3: x^3=x^2+x
            if out&4:out^=0b111 # x^2=x+1
            return out
        inv={x:next(y for y in range(1,4) if mul(x,y)==1) for x in range(1,4)}
    else:raise ValueError(q)
    return add,mul,inv


def subspaces(n,k,q):
    for piv in combinations(range(n),k):
        free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
        for values in product(range(q), repeat=len(free)):
            rows=[[0]*n for _ in range(k)]
            for i,j in enumerate(piv):rows[i][j]=1
            for (i,j),val in zip(free,values):rows[i][j]=val
            yield tuple(tuple(row) for row in rows)


def rank(rows,q):
    add,mul,inv=field(q)
    if not rows:return 0
    mat=[list(row) for row in rows]
    m=len(mat); n=len(mat[0]); r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if mat[i][j]),None)
        if pivot is None:continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        u=inv[mat[r][j]]
        mat[r]=[mul(x,u) for x in mat[r]]
        for i in range(r+1,m):
            if mat[i][j]:
                factor=mat[i][j]
                if q==4:
                    mat[i]=[add(x,mul(factor,y)) for x,y in zip(mat[i],mat[r])]
                else:
                    mat[i]=[add(x,-mul(factor,y)) for x,y in zip(mat[i],mat[r])]
        r+=1
        if r==m:break
    return r


def gauss(n,k,q):
    num=1; den=1
    for i in range(k):
        num*=q**(n-i)-1
        den*=q**(k-i)-1
    assert num%den==0
    return num//den


def grassmann_profile(q,n,k,limit=None):
    ss=list(subspaces(n,k,q))
    assert len(ss)==gauss(n,k,q),(q,n,k,len(ss),gauss(n,k,q))
    base=ss[0]
    pair={}
    for S in ss[1:]:
        t=rank(base+S,q)-k
        if t not in pair:pair[t]=S
    assert sorted(pair)==list(range(1,k+1)),(q,n,k,pair.keys())
    types=set()
    for t,B in sorted(pair.items()):
        four=set()
        for C in ss:
            if C==base or C==B:continue
            e1=int(rank(base+C,q)==k+1)
            e2=int(rank(B+C,q)==k+1)
            four.add((e1,e2))
        types.add((t,tuple(sorted(four))))
    return len(ss),tuple(sorted(types))


def subset_profile(n,k):
    subs=list(combinations(range(n),k)); s=set(subs[0]); sig=[]
    for t in range(1,k+1):
        b=next(set(z) for z in subs if k-len(s&set(z))==t)
        pat=set()
        for c in map(set,subs):
            if c==s or c==b:continue
            pat.add((int(len(c&s)==k-1),int(len(c&b)==k-1)))
        sig.append((t,tuple(sorted(pat))))
    return len(subs),tuple(sig)


def coarsen(prof):
    return tuple(sorted(set((int(t==1),pat) for t,pat in prof)))


def expected(k):
    allfour=((0,0),(0,1),(1,0),(1,1))
    partial=((0,0),(0,1),(1,0))
    return ((1,allfour),(2,allfour)) if k==2 else ((1,allfour),(2,allfour)) + tuple((t,partial) for t in range(3,k+1))


def main():
    runs=[(2,2,1),(2,4,2),(2,5,2),(3,4,2),(4,4,2),(2,6,3),(2,7,3),(3,6,3)]
    for q,n,k in runs:
        N,profile=grassmann_profile(q,n,k)
        if k==1:
            assert profile==((1,((1,1),)),)
        else:
            assert profile==expected(k),(q,n,k,profile,expected(k))
        print(f'GRASSMANN_OK q={q} n={n} k={k} vertices={N} pair_types={len(profile)}')
    n2,p2=subset_profile(6,2)
    n3,p3=subset_profile(7,3)
    assert coarsen(p2)==coarsen(expected(2))
    assert coarsen(p3)==coarsen(expected(3))
    assert len({coarsen(p2),coarsen(p3)})==2
    print(f'JOHNSON_CROSSCHECK_OK k2={n2} k3={n3} signatures_match=true')
    print('VERIFY_OK')

if __name__=='__main__':main()
