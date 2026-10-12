#!/usr/bin/env python3
"""Standalone finite checks for bi-Heyting endomorphism/image census.
Uses exact integer arithmetic; does not establish statements for all sizes.
"""
from itertools import product
from math import comb, prod
from collections import Counter

def components(lengths):
    blocks=[]; idx=0
    for a in lengths:
        blocks.append(tuple(range(idx,idx+a))); idx+=a
    return blocks

def matrix(lengths):
    blocks=components(lengths)
    n=sum(lengths)
    le=[[False]*n for _ in range(n)]
    for B in blocks:
        for ix,u in enumerate(B):
            for v in B[ix:]: le[u][v]=True
    return le

def bip(f,le):
    n=len(f)
    for x in range(n):
        for y in range(n):
            if le[x][y] and not le[f[x]][f[y]]: return False
        for v in range(n):
            if le[f[x]][v] and not any(le[x][z] and f[z]==v for z in range(n)): return False
            if le[v][f[x]] and not any(le[z][x] and f[z]==v for z in range(n)): return False
    return True

def rank(f,blocks):
    covered={j for j,B in enumerate(blocks) if any(y in B for y in f)}
    return prod(len(blocks[j])+1 for j in covered)

def brute(lengths):
    le=matrix(lengths); blocks=components(lengths); n=sum(lengths)
    H=Counter(); I=Counter(); supports=Counter(); idems=Counter(); checked=0
    for f in product(range(n),repeat=n):
        checked+=1
        if not bip(f,le): continue
        r=rank(f,blocks)
        H[r]+=1
        J=frozenset(j for j,B in enumerate(blocks) if any(y in B for y in f))
        supports[J]+=1
        if all(f[f[x]]==f[x] for x in range(n)):
            I[r]+=1; idems[J]+=1
    return H,I,supports,idems,checked

def predicted(lengths):
    k=len(lengths)
    w=[[comb(a-1,b-1) if a>=b else 0 for b in lengths] for a in lengths]
    H=Counter(); I=Counter(); supports=Counter(); idems=Counter()
    for mask in range(1,1<<k):
        J=frozenset(j for j in range(k) if mask>>j&1)
        count=0
        for sub in range(mask+1):
            if (sub&mask)!=sub:continue
            sign=-1 if (len(J)-sub.bit_count())%2 else 1
            count+=sign*prod(sum(w[i][j] for j in range(k) if sub>>j&1) for i in range(k))
        idem=prod(sum(w[i][j] for j in J) for i in range(k) if i not in J)
        r=prod(lengths[j]+1 for j in J)
        if count: supports[J]=count; H[r]+=count
        if idem: idems[J]=idem;I[r]+=idem
    return H,I,supports,idems

def algebra_cross_check(lengths):
    le=matrix(lengths); n=sum(lengths)
    U=[b for b in range(1<<n) if all(not (b>>x&1) or not le[x][y] or b>>y&1 for x in range(n) for y in range(n))]
    def up(b):return sum((1<<y) for y in range(n) if any(b>>x&1 and le[x][y] for x in range(n)))
    def down(b):return sum((1<<y) for y in range(n) if any(b>>x&1 and le[y][x] for x in range(n)))
    full=(1<<n)-1
    def impl(u,v):return full^down(u&~v)
    def coimpl(u,v):return up(u&~v)
    operations=[(u,v,impl(u,v),coimpl(u,v)) for u in U for v in U]
    chk=0
    for f in product(range(n),repeat=n):
        img={u:sum(1<<i for i in range(n) if u>>f[i]&1) for u in U}
        hom=all(img[impval]==impl(img[u],img[v]) and img[coval]==coimpl(img[u],img[v]) for u,v,impval,coval in operations)
        assert hom==bip(f,le),(lengths,f,hom)
        if hom:assert len(set(img.values()))==rank(f,components(lengths))
        chk+=1
    return chk

def main():
    cases=0; functions=0; morphisms=0; algebra_cases=0; algebra_maps=0
    for n in range(1,7):
        for k in range(1,n+1):
            for div in product(range(1,n+1),repeat=k):
                if sum(div)!=n:continue
                got=brute(div); want=predicted(div)
                assert got[:4]==want,(div,got[:4],want)
                assert set(want[2])=={frozenset(J) for mask in range(1,1<<k) for J in [[i for i in range(k) if mask>>i&1]] if any(div[j]==min(div) for j in J)},div
                cases+=1;functions+=got[4];morphisms+=sum(got[0].values())
                if n<=4:
                    algebra_maps+=algebra_cross_check(div);algebra_cases+=1
    print('VERIFY_OK', 'length_vectors',cases,'candidate_maps',functions,'valid_endomorphisms',morphisms,'direct_bi_Heyting_cases',algebra_cases,'direct_algebra_maps',algebra_maps)
    for a in [(1,2),(2,3,3),(1,1,2),(2,2,2),(1,2,3)]:
        H,I,S,T=predicted(a)
        print('CASE',a,'total',sum(H.values()),'ranks',dict(sorted(H.items())),'retractions',dict(sorted(I.items())))

if __name__=='__main__':main()
