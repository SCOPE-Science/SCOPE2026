#!/usr/bin/env python3
"""Reproducible finite checks for induced-forest homology characters of multipartite graphs.
All algorithms use Python standard library and exact integer/mod-2 arithmetic.
"""
import itertools
from collections import defaultdict
from math import comb


def sign_image(images):
    inv = sum(images[i] > images[j] for i in range(len(images)) for j in range(i+1, len(images)))
    return -1 if inv % 2 else 1


def data(ns):
    labels = tuple(t for t, n in enumerate(ns) for _ in range(n))
    offsets = tuple(sum(ns[:i]) for i in range(len(ns)))
    good=[]
    for mask in range(1 << len(labels)):
        ct=[0]*len(ns)
        for i,t in enumerate(labels):
            if mask>>i & 1: ct[t]+=1
        occ=[x for x in ct if x]
        if len(occ) <= 1 or (len(occ)==2 and min(occ)==1):
            good.append(mask)
    bysize=defaultdict(list)
    for f in good:bysize[f.bit_count()].append(f)
    return labels, offsets,good,bysize


def cycles_gf2_rank(bysize, k):
    if k<=0:return 0
    rows= {f:i for i,f in enumerate(bysize[k-1])}
    piv={}
    for f in bysize[k]:
        bits=0
        for i in range(f.bit_length()):
            if f>>i&1:bits^=1<<rows[f^(1<<i)]
        while bits:
            pos=bits.bit_length()-1
            if pos in piv:bits^=piv[pos]
            else:
                piv[pos]=bits
                break
    return len(piv)


def verify_case(ns):
    labels, offsets,good,bysize=data(ns)
    r=len(ns); nv=sum(ns)
    # Independent graph-level union-find cycle detection for each induced graph.
    good_set=set(good)
    for mask in range(1<<nv):
        cts=[sum((mask>>i)&1 for i in range(offsets[j],offsets[j]+ns[j])) for j in range(r)]
        occupied=sum(v>0 for v in cts)
        bad = occupied>=3 or sum(v>=2 for v in cts)>=2
        parent=list(range(nv))
        def find(i):
            while parent[i]!=i:
                parent[i]=parent[parent[i]]
                i=parent[i]
            return i
        has_cycle=False
        for u in range(nv):
            if not mask>>u & 1:continue
            for v in range(u+1,nv):
                if mask>>v & 1 and labels[u]!=labels[v]:
                    ru,rv=find(u),find(v)
                    if ru==rv:has_cycle=True
                    else:parent[ru]=rv
        assert (mask in good_set) == (not bad) == (not has_cycle)
    ranks={k:cycles_gf2_rank(bysize,k) for k in range(1,max(bysize)+1)}
    betti={}
    for dim in range(max(bysize)):
        if dim==0:betti[dim]=len(bysize[1])-ranks.get(2,0)-1
        else:betti[dim]=len(bysize[dim+1])-ranks.get(dim+1,0)-ranks.get(dim+2,0)
    b1=comb(r-1,2) if r>=2 else 0
    b2=sum((ns[i]-1)*(ns[j]-1) for i in range(r) for j in range(i+1,r))
    assert all(betti.get(d,0)==(b1 if d==1 else b2 if d==2 else 0) for d in betti)
    plist={n:list(itertools.permutations(range(n))) for n in set(ns)}
    sigmas=[s for s in itertools.permutations(range(r)) if all(ns[i]==ns[s[i]] for i in range(r))]
    count=0
    for sigma in sigmas:
      for maps in itertools.product(*(plist[ns[i]] for i in range(r))):
        action=[None]*nv
        for i in range(r):
            for a in range(ns[i]):action[offsets[i]+a]=offsets[sigma[i]]+maps[i][a]
        assert sorted(action)==list(range(nv))
        fixparts=sum(sigma[i]==i for i in range(r))
        twocycles=sum(sigma[i]>i and sigma[sigma[i]]==i for i in range(r))
        char1=((fixparts-1)*(fixparts-2))//2 - twocycles
        char2=0
        for i in range(r):
            if sigma[i]==i:
                fi=sum(action[offsets[i]+a]==offsets[i]+a for a in range(ns[i]))
                for j in range(i+1,r):
                    if sigma[j]==j:
                        fj=sum(action[offsets[j]+b]==offsets[j]+b for b in range(ns[j]))
                        char2+=(fi-1)*(fj-1)
            elif sigma[i]>i and sigma[sigma[i]]==i:
                char2+=sum(action[action[offsets[i]+a]]==offsets[i]+a for a in range(ns[i]))-1
        L=-1
        for f in good[1:]:
            inds=[i for i in range(nv) if f>>i&1]
            images=[action[i] for i in inds]
            if sum(1<<a for a in images)==f:
                L+=(-1 if len(inds)%2==0 else 1)*sign_image(images)
        assert L==char2-char1,(ns,sigma,maps,L,char2-char1)
        count+=1
    print({'part_sizes':ns,'faces':len(good),'betti':{str(k):v for k,v in sorted(betti.items()) if v},
           'formula_b1':b1,'formula_b2':b2,'automorphisms_checked':count,
           'character_checks':'all pass'})


def main():
    for ns in ((1,1,1),(1,1,1,1),(1,2,3),(1,1,2,2),(2,2),(2,3),(2,2,2),(2,3,3),(3,3,3),(2,2,2,2),(2,3,4)):
        verify_case(ns)
    print('VERIFY_OK')
if __name__=='__main__':main()
