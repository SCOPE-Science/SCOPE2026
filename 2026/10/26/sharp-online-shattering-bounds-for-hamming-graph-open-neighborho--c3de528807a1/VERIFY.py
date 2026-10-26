#!/usr/bin/env python3
"""Reproducibility checks for the open-neighborhood Hamming-graph claim.

Run: python3 VERIFY.py WITNESSES.json
Only the Python standard library is used. No assertion here substitutes for
its accompanying all-parameter mathematical proof.
"""
import json, sys
from itertools import product
from functools import lru_cache


def words(d,q):
    return [tuple(x) for x in product(range(q), repeat=d)]


def near(x,y):
    return sum(a!=b for a,b in zip(x,y))==1


def formula(d,q):
    assert d>=1 and q>=2
    if d==1 or (d==2 and q==2):return 1
    if d==3 and q==2:return 2
    return 3


def exact(d,q):
    X=words(d,q)
    masks=tuple(sum(1<<i for i,a in enumerate(X) if near(a,b)) for b in X)
    @lru_cache(None)
    def rec(s):
        if s.bit_count()<=1:return 0
        best=0
        for t in masks:
            p=s&t
            z=s&~t
            if p and z:
                best=max(best,1+min(rec(p),rec(z)))
        return best
    res=rec((1<<len(X))-1)
    return res,rec.cache_info().currsize


def verify_tree(d,q,tree):
    X=set(''.join(str(v) for v in t) for t in words(d,q))
    count=[0]
    def visit(node,C,depth):
        if 'center' in node:
            assert list(node)==['center'], node
            assert node['center'] in C, (d,q,node,C)
            count[0]+=1
            return {depth}
        assert set(node)=={'query','0','1'},node
        t=node['query'];assert len(t)==d and all(int(z)<q for z in t)
        C1={v for v in C if near(t,v)}
        C0=C-C1
        assert C0 and C1,(d,q,t,depth,C)
        return visit(node['0'],C0,depth+1)|visit(node['1'],C1,depth+1)
    depths=visit(tree,X,0)
    assert len(depths)==1
    depth=depths.pop()
    assert count[0]==2**depth,(d,q,count)
    return depth,count[0]


def local_structure(d,q):
    X=words(d,q);v=X[0]
    nv={a for a in X if near(a,v)}
    for w in X:
        inter={a for a in nv if near(a,w)}
        dist=sum(a!=b for a,b in zip(v,w))
        if dist==0:assert inter==nv
        if dist==1:
            assert len(inter)==q-2
            # A lies on one coordinate line. Every test on A has at most
            # one positive or at most one negative response.
            for z in X:
                pos=sum(near(z,a) for a in inter)
                assert min(pos,len(inter)-pos)<=1,(d,q,v,w,z)
        if dist==2:assert len(inter)==2
        if dist>=3:assert len(inter)==0


def main():
    path=sys.argv[1] if len(sys.argv)==2 else 'WITNESSES.json'
    data=json.load(open(path,encoding='utf-8'))
    assert set(data)=={'H(2,3)','H(3,2)','H(4,2)'}
    for d,q in [(2,3),(3,2),(4,2)]:
        depth,leaves=verify_tree(d,q,data[f'H({d},{q})'])
        assert depth==formula(d,q)
        print(f'WITNESS_OK H({d},{q}) depth={depth} paths={leaves}')
    # Independent hypothesis-set recurrence; no use of the structural proof.
    tests=[(1,q) for q in range(2,7)]+[(2,q) for q in range(2,6)]+[(3,2),(3,3),(4,2)]
    for d,q in tests:
        actual,states=exact(d,q)
        assert actual==formula(d,q),(d,q,actual,formula(d,q))
        print(f'EXACT_OK H({d},{q}) Ldim={actual} states={states}')
    # Stress-test the nonstandard intersection/line-trace premise against
    # direct Hamming adjacency, across a broad finite range.
    for d,q in [(d,q) for d in range(1,5) for q in range(2,6) if q**d<=256]:
        local_structure(d,q)
        print(f'INTERSECTIONS_OK H({d},{q})')
    print('ALL_CHECKS_OK')

if __name__=='__main__':main()
