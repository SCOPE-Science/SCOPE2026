#!/usr/bin/env python3
"""Standalone finite checks for higher-independence complexes of double stars.

Independent face enumeration, mod-2 simplicial ranks, and signed Lefschetz
traces. These tests corroborate but do not replace the infinite proof.
"""
from itertools import combinations, permutations
from math import comb

def graph(a,b):
    m=a+b; n=m+2
    edges=[(0,1)]+[(0,i) for i in range(2,2+a)]+[(1,i) for i in range(2+a,n)]
    nbr=[0]*n
    for i,j in edges: nbr[i]|=1<<j; nbr[j]|=1<<i
    return nbr

def components_ok(mask,nbr,r):
    rem=mask
    while rem:
        start=rem&-rem; rem^=start; stack=start; count=1
        while stack:
            bit=stack&-stack; stack^=bit; i=bit.bit_length()-1
            neighbors=nbr[i]&rem
            stack|=neighbors; rem^=neighbors; count+=neighbors.bit_count()
        if count>r:return False
    return True

def generate(a,b,r):
    nbr=graph(a,b); n=len(nbr)
    ans=[[] for _ in range(n)]
    for mask in range(1,1<<n):
        if components_ok(mask,nbr,r):ans[mask.bit_count()-1].append(mask)
    return ans

def gf2_rank(columns):
    basis={};rank=0
    for v in columns:
        while v:
            p=v.bit_length()-1
            if p in basis:v^=basis[p]
            else:basis[p]=v;rank+=1;break
    return rank

def betti_mod2(fs,n):
    ranks=[0]*(n+1)
    for d in range(1,n):
        if not fs[d]:continue
        inds={S:i for i,S in enumerate(fs[d-1])}
        columns=[]
        for S in fs[d]:
            col=0; tmp=S
            while tmp:
                bit=tmp&-tmp;tmp^=bit
                col^=1<<inds[S^bit]
            columns.append(col)
        ranks[d]=gf2_rank(columns)
    return [len(fs[d])-ranks[d]-ranks[d+1]-(d==0) for d in range(n)]

def sign_of_permutation(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def reduced_lefschetz(fs,perm):
    ans=-1
    for d,faces in enumerate(fs):
        for S in faces:
            ls=[i for i in range(len(perm)) if S>>i&1]
            imgs=[perm[i] for i in ls]
            if sum(1<<x for x in imgs)!=S:continue
            ans+=(-1)**d*sign_of_permutation(imgs)
    return ans

def predicted_trace(perm,r,swapped):
    # trace exterior^(r-2) on kernel of augmentation of the leaf lattice
    leaves=[x-2 for x in perm[2:]];m=len(leaves)
    unseen=set(range(m)); poly=[1]
    while unseen:
        i=next(iter(unseen));j=i;cycle=[]
        while j in unseen: unseen.remove(j);cycle.append(j);j=leaves[j]
        ell=len(cycle)
        new=poly+[0]*ell
        for k,c in enumerate(poly):new[k+ell]-=(-1)**ell*c
        poly=new
    coeff=[]
    for j in range(m+1):coeff.append((poly[j] if j<len(poly) else 0)-(coeff[j-1] if j else 0))
    return (-1 if swapped else 1)*(coeff[r-2] if r-2<len(coeff) else 0)

def graph_aut(a,b,p,q,swap):
    perm=list(range(a+b+2))
    if not swap:
        for i,z in enumerate(p):perm[2+i]=2+z
        for j,z in enumerate(q):perm[2+a+j]=2+a+z
    else:
        assert a==b
        perm[0],perm[1]=1,0
        for i,z in enumerate(p):perm[2+i]=2+a+z
        for j,z in enumerate(q):perm[2+a+j]=2+z
    return perm

def main():
    cases=0; traces=0; faces_total=0
    for a in range(1,5):
        for b in range(1,5):
            n=a+b+2;m=a+b
            for r in range(1,n+2):
                fs=generate(a,b,r); faces_total+=sum(map(len,fs))
                bet=betti_mod2(fs,n)
                want=[0]*n
                if 2<=r<=m+1:want[r-1]=comb(m-1,r-2)
                assert bet==want,(a,b,r,bet,want)
                cases+=1
    for a,b in [(1,1),(1,3),(2,2),(2,3),(3,3),(4,4)]:
        n=a+b+2;m=a+b
        # full group for a,b<=3; cycle generators suffice for (4,4)
        ap=list(permutations(range(a))) if a<=3 else [tuple(range(a)),(1,0,2,3),(1,2,3,0)]
        bp=list(permutations(range(b))) if b<=3 else [tuple(range(b)),(1,0,2,3),(1,2,3,0)]
        for r in range(1,n+2):
            fs=generate(a,b,r)
            for x in ap:
                for y in bp:
                    for swap in ([False,True] if a==b else [False]):
                        perm=graph_aut(a,b,x,y,swap)
                        got=(-1)**(r-1)*reduced_lefschetz(fs,perm) if 2<=r<=m+1 else 0
                        want=predicted_trace(perm,r,swap) if 2<=r<=m+1 else 0
                        assert got==want,(a,b,r,perm,got,want)
                        traces+=1
    print('PASS: %s homology cases, %s signed-character cases, %s total faces enumerated'% (cases,traces,faces_total))
if __name__=='__main__':main()
