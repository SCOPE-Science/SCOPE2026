#!/usr/bin/env python3
from itertools import combinations

def edge(n,m,a,b,rev=False):
    if a==b: raise ValueError
    if rev and {a,b}=={0,1}:
        return a==1 and b==0
    d=(b-a)%n
    return 1<=d<=m

def transitive(n,m,S,rev=False):
    # A finite tournament is transitive iff its outdegrees in the induced subtournament are 0,...,|S|-1.
    ds=[]
    for a in S:
        ds.append(sum(edge(n,m,a,b,rev) for b in S if b!=a))
    return sorted(ds)==list(range(len(S)))

def faces(n,rev=False):
    m=(n-1)//2
    out=[set() for _ in range(n)]
    out[0].add(())
    # return nonempty faces grouped by dimension
    F=[]
    V=range(n)
    for k in range(1,n+1):
        cur=[]
        for S in combinations(V,k):
            if transitive(n,m,S,rev): cur.append(S)
        if not cur: break
        F.append(cur)
    return F

def rank_f2(cols):
    piv={}
    r=0
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv: x^=piv[p]
            else:
                piv[p]=x; r+=1; break
    return r

def betti_f2(F):
    ranks=[]
    for k in range(1,len(F)):
        prev={s:i for i,s in enumerate(F[k-1])}
        cols=[]
        for s in F[k]:
            x=0
            for j in range(len(s)):
                face=s[:j]+s[j+1:]
                x ^= 1<<prev[face]
            cols.append(x)
        ranks.append(rank_f2(cols))
    # rank d_0=0; b_k = dim C_k-rank d_k-rank d_{k+1}
    b=[]
    for k,fl in enumerate(F):
        rd = 0 if k==0 else ranks[k-1]
        rup = ranks[k] if k<len(ranks) else 0
        b.append(len(fl)-rd-rup)
    return b,ranks

def check(n):
    m=(n-1)//2
    A=faces(n,False); B=faces(n,True)
    SA={s for level in A for s in level}; SB={s for level in B for s in level}
    tau=(0,1,m+1)
    assert SB-SA=={tau}, (n,SB-SA)
    assert not (SA-SB), (n,SA-SB)
    b,r=betti_f2(B)
    assert b==[1]+[0]*(len(b)-1), (n,b)
    # arc model: maximal blocks F_a={a,...,a+m}; every old face lies in one, and all subsets of blocks are old faces.
    blocks=[tuple((a+t)%n for t in range(m+1)) for a in range(n)]
    for s in SA:
        assert any(set(s)<=set(Bk) for Bk in blocks)
    for Bk in blocks:
        for k in range(1,len(Bk)+1):
            for s in combinations(Bk,k):
                assert tuple(sorted(s)) in SA
    # three arcs B_0,B_1,B_{m+1} cover the circle in the standard interval model and have nerve boundary of triangle.
    # Discretely, their three pairwise common endpoints are m? Actual continuous intervals:
    # B0=[0,m], B1=[1,m+1], B_{m+1}=[m+1,n] after cutting at 0=n.
    # Union=[0,n], B0∩B1=[1,m], B1∩B_{m+1}={m+1}, B_{m+1}∩B0={0=n}, triple intersection empty.
    return [len(x) for x in A],[len(x) for x in B],r

for n in range(3,18,2):
    a,b,r=check(n)
    print(f'n={n} original_faces={a} reversed_faces={b} boundary_ranks_F2={r}')
print('VERIFY_OK')
