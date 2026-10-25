#!/usr/bin/env python3
"""Independent finite verification for robust clique complexes of square bouquets.
Standard library only. Computes independence numbers by vertex-deletion recurrence,
checks the link/star decomposition, and checks reduced GF(2) homology.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def check(m,k):
    n=3*m+1
    edges=[]
    for i in range(m):
        a,b,d=3*i+1,3*i+2,3*i+3
        edges += [(0,a),(0,b),(a,d),(b,d)]
    adj=[0]*n
    for u,v in edges:
        adj[u]|=1<<v
        adj[v]|=1<<u
    # Exact maximum-independent-set recurrence for every subset.
    alpha=[0]*(1<<n)
    for s in range(1,1<<n):
        v=(s&-s).bit_length()-1
        rem=s^(1<<v)
        alpha[s]=max(alpha[rem],1+alpha[rem&~adj[v]])
    face={s for s in range(1,1<<n) if alpha[s]<k}
    x={s for s in face if not s&1}
    link={s for s in x if alpha[s|1]<k}
    stars={}
    boundary={}
    for I in combinations(range(m),k-1):
        ds=sum(1<<(3*i+3) for i in I)
        a_b=[(1<<(3*i+1),1<<(3*i+2)) for i in I]
        star=set()
        for t in range(1<<(k-1)):
            dd=sum(1<<(3*i+3) for ii,i in enumerate(I) if t>>ii&1)
            for choices in range(3**(k-1)):
                q=choices; s=dd
                for aa,bb in a_b:
                    v=q%3;q//=3
                    if v==1:s|=aa
                    if v==2:s|=bb
                star.add(s)
        stars[I]=star
        boundary[I]={s for s in star if s&ds!=ds}
        assert all(s in x or s==0 for s in star)
        assert boundary[I] == star.intersection(link | {0})
        assert (star-boundary[I]) == {s for s in x-link if (s&ds)==ds}
    beyond=x-link
    assert set().union(*(v-set() for v in stars.values())) >= beyond if stars else not beyond
    assert sum(len(v-link-{0}) for v in stars.values())==len(beyond)
    for i,j in combinations(stars,2):
        assert (stars[i]&stars[j]) <= link|{0}
    # Non-link face supports exactly k-1 distal vertices.
    assert all(sum(bool(s&(1<<(3*i+3))) for i in range(m))==k-1 for s in beyond)
    hom={}
    if k==4:
        dd=defaultdict(list)
        for s in face:dd[s.bit_count()-1].append(s)
        ranks={}
        for d in sorted(dd):
            lower={s:i for i,s in enumerate(dd[d])}
            piv={}
            for s in dd.get(d+1,[]):
                v=s;col=0
                while v:
                    bit=v&-v;v-=bit
                    col^=1<<lower[s^bit]
                while col:
                    p=col.bit_length()-1
                    if p in piv:col^=piv[p]
                    else:piv[p]=col;break
            ranks[d+1]=len(piv)
            beta=len(dd[d])-ranks.get(d,0)-len(piv)-(1 if d==0 else 0)
            if beta:hom[d]=beta
        expected=({2*k-3:comb(m,k-1)} if m>=k-1 else {})
        assert hom==expected,(m,k,hom,expected)
    print('m=%s k=%s faces=%s nonlink=%s stars=%s mod2=%s'%(m,k,len(face),len(beyond),len(stars),hom if k==4 else 'not_computed'))

if __name__=='__main__':
    for k in (4,5):
        for m in range(1,6):
            check(m,k)
    print('All finite checks passed.')
