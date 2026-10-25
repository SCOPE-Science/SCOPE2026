#!/usr/bin/env python3
"""Exhaustive finite checks for higher-independence complexes of subdivided stars.

Works from induced-component admissibility, rather than the proof decomposition.
Computes augmented simplicial homology over F_2 and Lefschetz traces under
branch permutations; the infinite claim is proved in the accompanying paper.
"""
from collections import defaultdict
from itertools import permutations
from math import comb


def faces(m, r):
    # Vertex 0 is the center; branch i consists of vertices (1+2*i, 2+2*i).
    n=2*m+1
    edges=[(0,1+2*i) for i in range(m)]+[(1+2*i,2+2*i) for i in range(m)]
    out=[]
    for mask in range(1<<n):
        unseen=mask
        good=True
        while unseen:
            bit=unseen & -unseen
            component=bit
            previous=-1
            while previous!=component:
                previous=component
                for u,v in edges:
                    if (mask>>u&1) and (mask>>v&1):
                        if component>>u&1:component|=1<<v
                        if component>>v&1:component|=1<<u
            if component.bit_count()>r:
                good=False
                break
            unseen &= ~component
        if good:out.append(mask)
    return out


def gf2rank(columns):
    piv={}
    for col in columns:
        while col:
            b=col.bit_length()-1
            if b not in piv:
                piv[b]=col
                break
            col^=piv[b]
    return len(piv)


def reduced_betti(F):
    by=defaultdict(list)
    for mask in F:by[mask.bit_count()-1].append(mask)
    rk={-1:0}
    for d in range(max(by)+1):
        targets={mask:i for i,mask in enumerate(by[d-1])}
        cols=[]
        for mask in by[d]:
            col=0
            z=mask
            while z:
                bit=z&-z
                z-=bit
                col^=1<<targets[mask^bit]
            cols.append(col)
        rk[d]=gf2rank(cols)
    return {d:b for d in range(max(by)+1)
            if (b:=len(by[d])-rk[d]-rk.get(d+1,0))}


def predicted(m,r):
    return {r-1:comb(m-1,r-m-1)} if m+1<=r<=2*m else {}


def sign(perm):
    return (-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))


def wedge_trace(m,k,perm):
    # det(I+t*perm on Z^m) / (1+t), coefficient of t^k.
    visited=set()
    poly=[1]
    for i in range(m):
        if i in visited:continue
        j=i;ell=0
        while j not in visited:
            visited.add(j);ell+=1;j=perm[j]
        new=poly+[0]*ell
        for h,v in enumerate(poly):new[h+ell]+=(-1)**(ell-1)*v
        poly=new
    w=[1]
    for i in range(1,len(poly)):w.append(poly[i]-w[-1])
    return w[k] if k<len(w) else 0


def reduced_lefschetz(F,m,perm):
    sigma=[0]*(2*m+1);sigma[0]=0
    for i,j in enumerate(perm):
        sigma[1+2*i]=1+2*j
        sigma[2+2*i]=2+2*j
    ans=-1   # augmented empty face contribution
    for mask in F:
        if mask==0:continue
        support=[i for i in range(2*m+1) if mask>>i&1]
        images=[sigma[v] for v in support]
        if sorted(images)!=support:continue
        parity=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
        ans+=(-1)**(len(support)-1+parity)
    return ans


def main():
    nbetti=0
    for m in range(2,7):
        for r in range(2,2*m+3):
            actual=reduced_betti(faces(m,r))
            expect=predicted(m,r)
            assert actual==expect,(m,r,actual,expect)
            nbetti+=1
    print('BETTI_CASES',nbetti)
    ncharacter=0
    for m in range(2,6):
        cache={r:faces(m,r) for r in range(2,2*m+2)}
        for perm in permutations(range(m)):
            for r,F in cache.items():
                actual=reduced_lefschetz(F,m,perm)
                if m+1<=r<=2*m:
                    chi=sign(perm)*wedge_trace(m,r-m-1,perm)
                    expect=(-1)**(r-1)*chi
                else: expect=0
                assert actual==expect,(m,r,perm,actual,expect)
                ncharacter+=1
    print('CHARACTER_CASES',ncharacter)
    print('VERIFY_OK')

if __name__=='__main__':main()
