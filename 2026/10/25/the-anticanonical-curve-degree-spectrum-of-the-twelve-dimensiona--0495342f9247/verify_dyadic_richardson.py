#!/usr/bin/env python3
"""Exact character-lattice verification for a toric Richardson twelvefold."""
from collections import Counter
from itertools import combinations

WORD=(0,2,1,0,2,4,6,5,4,6,3,2,4,1,3,5,0,2,4,6)
LOW=(0,4,2,6,1,5,3,7)
EXPECTED={-2:512,0:4096,2:15360,4:4096,6:512}

def subword_product(indices):
    p=list(range(8))
    for j in sorted(indices):
        i=WORD[j]
        p[i],p[i+1]=p[i+1],p[i]
    return tuple(p)

def tangent_weights(mask,forced,free):
    """Characters of the SL8 torus on the twelve tangent directions."""
    p=list(range(8)); out=[]; free_idx={j:k for k,j in enumerate(free)}
    for j,i in enumerate(WORD):
        if j in forced or (j in free_idx and (mask>>free_idx[j])&1):
            p[i],p[i+1]=p[i+1],p[i]
        if j in free_idx:
            w=[0]*8
            w[p[i+1]]+=1
            w[p[i]]-=1
            out.append(tuple(w))
    return tuple(out)

def add(*terms):
    return tuple(sum(x) for x in zip(*terms))

def main():
    candidates=[s for s in combinations(range(20),8) if subword_product(s)==LOW]
    assert candidates==[(2,7,10,11,12,13,14,15)],candidates
    forced=set(candidates[0]);free=[j for j in range(20) if j not in forced]
    assert len(free)==12
    weights=[tangent_weights(b,forced,free) for b in range(1<<12)]
    c1=[add(*w) for w in weights]
    spectral=Counter(); by_coord=[]
    for k in range(12):
        h=Counter()
        for b in range(1<<12):
            if (b>>k)&1: continue
            nxt=b^(1<<k)
            alpha=weights[b][k]
            delta=tuple(a-c for a,c in zip(c1[b],c1[nxt]))
            assert weights[nxt][k]==tuple(-a for a in alpha)
            assert sum(alpha)==0 and alpha.count(1)==1 and alpha.count(-1)==1
            i=alpha.index(1);degree=delta[i]
            assert all(z==degree*a for z,a in zip(delta,alpha))
            h[degree]+=1
        assert sum(h.values())==2048
        spectral.update(h);by_coord.append(dict(sorted(h.items())))
    assert dict(spectral)==EXPECTED,(spectral,EXPECTED)
    assert by_coord[0]=={-2:128,0:512,2:768,4:512,6:128}
    assert by_coord[2]=={0:512,2:1024,4:512}
    assert by_coord[8]=={2:2048}
    assert sum(spectral.values())==24576
    b=516; q=517;k=0
    d=tuple(a-z for a,z in zip(c1[b],c1[q]))
    assert d==tuple(-2*z for z in weights[b][k])
    assert subword_product(forced|{free[j] for j in range(12) if b>>j&1})==(2,4,6,0,1,5,3,7)
    assert subword_product(forced|{free[j] for j in range(12) if q>>j&1})==(2,4,6,1,0,5,3,7)
    print('FORCED_POSITIONS_ONE_BASED',tuple(j+1 for j in sorted(forced)))
    print('FREE_POSITIONS_ONE_BASED',tuple(j+1 for j in free))
    print('ANTICANONICAL_SPECTRUM',dict(sorted(spectral.items())))
    print('BY_FREE_COORDINATE',by_coord)
    print('NEGATIVE_CURVE_WITNESS',{'bitmask':b,'toggle':k+1,'p':(3,5,7,1,2,6,4,8),'q':(3,5,7,2,1,6,4,8),'anticanonical_degree':-2})
    print('VERIFY_OK')
if __name__=='__main__':main()
