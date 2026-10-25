#!/usr/bin/env python3
"""Check a finite shelling certificate using the ridge-coverage criterion."""
import json
from itertools import combinations
from pathlib import Path
from collections import Counter


def components(n, vertices):
    roots = {x:x for x in vertices}
    def find(x):
        while roots[x]!=x:
            x=roots[x]
        return x
    for x,y in combinations(vertices,2):
        if min((x-y)%n,(y-x)%n)<=3:
            roots[find(x)]=find(y)
    return len({find(x) for x in vertices})


def facets(n):
    allbits=(1<<n)-1
    return {allbits ^ sum(1<<v for v in tri)
            for tri in combinations(range(n),3) if components(n,tri)>=2}


def audit(n,seq):
    expected=facets(n)
    assert len(seq)==len(expected) and len(seq)==len(set(seq))
    assert set(seq)==expected
    prior=[]; spanning=0; restrictions=Counter()
    for j,f in enumerate(seq):
        R=0
        for g in prior:
            dif=f & ~g
            if dif.bit_count()==1: R |=dif
        if j:
            assert R,"Shelling has empty intersection"
            assert all(R & ~g for g in prior),"Intersection not covered by ridges"
        if j and R==f: spanning+=1
        restrictions[R.bit_count()]+=1
        prior.append(f)
    assert (len(seq),spanning)=={13:(169,1),14:(238,8)}[n]
    assert sum(restrictions.values())==len(seq)
    return len(seq),spanning,sorted(restrictions.items())

if __name__=='__main__':
    cert=json.loads((Path(__file__).parent/'shellings.json').read_text())
    assert cert['schema_version']==1
    for n in (13,14):
        facets_count,spanning,dist=audit(n,cert['shellings'][str(n)])
        print(f'n={n} facets={facets_count} shelling=PASS spanning={spanning} restriction_sizes={dist}')
    print('CHECK_SHELLING_OK')
