#!/usr/bin/env python3
"""Reproduce the exact extremal F2 even-contact hyperplane classification.
Uses four projective Jacobian charts over F2 (SymPy) and an independent
finite-field witness test for all excluded coefficient vectors.
"""
import json
from collections import Counter
import census_genus4_tritangents as c


def gf_multiply(a,b,poly,k):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&(1<<k):a^=poly
    return z


def singular_point(F,k,poly):
    """Return an explicit singular point on one of four affine charts, if seen."""
    q=1<<k
    T=[[gf_multiply(a,b,poly,k) for b in range(q)] for a in range(q)]
    V=[[1,a,T[a][a],T[T[a][a]][a]] for a in range(q)]
    for ca in range(2):
        for cb in range(2):
            for x in range(q):
                for y in range(q):
                    f=fx=fy=0
                    for i in range(4):
                        for j in range(4):
                            if not (F>>(4*i+j))&1:continue
                            a=i if not ca else 3-i
                            b=j if not cb else 3-j
                            f^=T[V[x][a]][V[y][b]]
                            if a&1:fx^=T[V[x][a-1]][V[y][b]]
                            if b&1:fy^=T[V[x][a]][V[y][b-1]]
                    if (f,fx,fy)==(0,0,0):return (ca,cb,x,y)
    return None


def analyze():
    buck=Counter();bad=Counter();survivors=[];high_count=0
    for F in range(1,65536):
        k=len(c.tritangents(F))
        buck[k]+=1
        if k<4:continue
        p=singular_point(F,1,3)
        if p is not None:
            bad[(k,'F2')]+=1;continue
        p=singular_point(F,2,7)
        if p is not None:
            bad[(k,'F4')]+=1;continue
        if k>4:raise AssertionError(('unexcluded high mask',hex(F),k))
        survivors.append(F)
    assert len(survivors)==60
    assert all(c.nonsingular(F) for F in survivors)
    orb=c.orbits(survivors)
    assert sorted(x['size'] for x in orb)==[6,18,36]
    assert buck=={0:5824,1:23280,2:21840,3:5180,4:8400,6:560,7:210,8:240,15:1}
    result={'total_nonzero_sections':65535,'contact_count_distribution_all_sections':dict(sorted(buck.items())),'unsmooth_geometric_witnesses_for_contact_at_least_four':{f'{k}_{field}':v for (k,field),v in sorted(bad.items())},'remaining_four_contact_sections':len(survivors),'remaining_all_smooth':True,'orbit_representatives':[{**o,'mask_hex':hex(o['representative']),'hyperplanes':list(c.tritangents(o['representative']))} for o in orb], 'extremal_count':sum(x['size'] for x in orb)}
    return result

if __name__=='__main__':
    print(json.dumps(analyze(),indent=2,sort_keys=True))
