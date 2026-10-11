#!/usr/bin/env python3
"""Exact-rational finite checks for the cluster fluctuation projection theorem.

No dependencies beyond Python's standard library. These tests check explicit
primal transportation bounds and dual Lipschitz witnesses; the manuscript's
universal proof, not finite sampling, establishes the theorem.
"""
from fractions import Fraction as F
from itertools import combinations


def check(sizes, radii):
    radii = tuple(F(v) for v in radii)
    assert len(sizes) == len(radii) >= 2
    assert any(n > 1 for n in sizes)
    assert all(n >= 1 for n in sizes)
    assert all(0 < r <= 1 for r in radii)
    groups = []
    for n in sizes:
        start = sum(sizes[:len(groups)])
        groups.append(tuple(range(start, start+n)))
    N = sum(sizes)
    cluster = {x:i for i, grp in enumerate(groups) for x in grp}
    def distance(x,y):
        if x==y: return F(0)
        i=cluster[x]
        return radii[i] if i == cluster[y] else F(1)
    def projection(vector):
        result = list(vector)
        for grp in groups:
            av=sum((vector[z] for z in grp),F(0))/len(grp)
            for z in grp: result[z] -= av
        return tuple(result)
    def molecular(x,y):
        val=distance(x,y)
        m=[F(0)]*N
        m[x]=1/val; m[y]=-1/val
        return tuple(m)
    tests=0
    for x,y in combinations(range(N),2):
        v=molecular(x,y)
        pv=projection(v)
        assert projection(pv)==pv
        assert sum(pv)==0
        if cluster[x]==cluster[y]:
            assert pv==v
            tests+=1
            continue
        i,j=cluster[x],cluster[y]
        # Explicit optimal dual potential for the image of a cross-cluster molecule.
        f=[F(0)]*N
        f[x]=radii[i]
        for z in groups[j]:
            if z!=y: f[z]=radii[j]
        assert all(abs(f[a]-f[b])<=distance(a,b)
                   for a,b in combinations(range(N),2))
        pairing=sum((pv[z]*f[z] for z in range(N)),F(0))
        exact=radii[i]*(1-F(1,sizes[i]))+radii[j]*(1-F(1,sizes[j]))
        assert pairing==exact
        # The upper certificate is a transport plan separately in each cluster.
        upper=sum((distance(x,z)/sizes[i] for z in groups[i] if z!=x), F(0))
        upper+=sum((distance(y,z)/sizes[j] for z in groups[j] if z!=y), F(0))
        assert upper==exact
        tests+=1
    return tests


if __name__=='__main__':
    cases=[
        ((2,2),('1/4','1/2')),
        ((2,3),('1','1')),
        ((3,3),('1','1')),
        ((3,3),('3/4','3/4')),
        ((3,3),('4/5','4/5')),
        ((4,5),('7/10','9/10')),
        ((1,3,4),('1/3','2/3','1')),
        ((2,3,4),('2/5','3/5','4/5')),
        ((1,1,5,2),('1','1/2','1/3','2/3')),
        ((3,4,5),('9/10','3/4','4/5')),
    ]
    n=sum(check(*c) for c in cases)
    print('PASS: 10 configurations,',n,'exact molecule/certificate cases')
