#!/usr/bin/env python3
"""Exact binary ranks for isolated and correlated missing graph-state bonds."""
from itertools import product

def rank(vs):
    piv={}
    for w in vs:
        while w:
            k=w.bit_length()-1
            if k in piv:w^=piv[k]
            else:piv[k]=w;break
    return len(piv)

def check(L):
    dims=(4,4,L)
    vs=list(product(*(range(m) for m in dims)))
    ix={v:i for i,v in enumerate(vs)}
    even=[v for v in vs if sum(v)%2==0]
    odd=[v for v in vs if sum(v)%2==1]
    oi={v:i for i,v in enumerate(odd)}
    ei={v:i for i,v in enumerate(even)}
    rows=[]
    for v in even:
        nbr=[]
        for i,m in enumerate(dims):
            for h in (-1,1):
                w=list(v);w[i]=(w[i]+h)%m
                nbr.append(tuple(w))
        rows.append(sum(1<<oi[w] for w in nbr))
    r=rank(rows)
    assert r==8*L-16,(L,r)
    tested=0
    for z in range(0,L,2):
      for axis in (0,1):
       for step in (-1,1):
        v=(0,0,z)
        w=list(v);w[axis]=(w[axis]+step)%4;w=tuple(w)
        v2=(0,0,(z+4)%L)
        w2=list(w);w2=(w2[0],w2[1],(w2[2]+4)%L)
        e,o=ei[v],oi[w];e2,o2=ei[v2],oi[w2]
        s=rows.copy();s[e]^=1<<o
        assert rank(s)==r+1
        t=rows.copy();t[e2]^=1<<o2
        assert rank(t)==r+1
        s[e2]^=1<<o2
        assert rank(s)==r,(L,z,axis,step)
        tested+=1
    print(f'PASS L={L} sites={16*L} baseline_entropy={r} bond_pairs={tested} single_gain=1 pair_gain=0')
    return tested

if __name__=='__main__':
    n=sum(check(l) for l in (8,16,32))
    print(f'PASS pairs={n} exactly_rank_comparisons={3*n+3}')
