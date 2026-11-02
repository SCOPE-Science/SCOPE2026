#!/usr/bin/env python3
"""Exact finite verification of shattering for independent-dominating sets on paths and cycles.
All arithmetic is integer/Boolean; no external packages. Run beside certificate.json.
"""
import json
from functools import lru_cache
from pathlib import Path


def edges(n, kind):
    ans=[(i,i+1) for i in range(n-1)]
    if kind=='C':
        assert n>=3
        ans.append((n-1,0))
    return ans


def hypotheses(n,kind):
    ee=edges(n,kind)
    nb=[0]*n
    for u,v in ee:
        nb[u]|=1<<v;nb[v]|=1<<u
    # Independency + domination = maximal independence.
    return tuple(s for s in range(1<<n)
        if all(not ((s>>u)&1 and (s>>v)&1) for u,v in ee)
        and all((s>>i)&1 or (s&nb[i]) for i in range(n)))


def vc(h,n):
    best=0; support=0
    for s in range(1<<n):
        b=s.bit_count()
        if b<best:continue
        if len({x&s for x in h})==(1<<b) and b>best:
            best,support=b,s
    return best,support


def ldim(h,n):
    @lru_cache(None)
    def rank(remaining,unqueried):
        best=0
        for v in range(n):
            bit=1<<v
            if not unqueried&bit:continue
            zero=tuple(t for t in remaining if not t&bit)
            one=tuple(t for t in remaining if t&bit)
            if zero and one:
                value=1+min(rank(zero,unqueried^bit),rank(one,unqueried^bit))
                if value>best:best=value
        return best
    d=rank(h,(1<<n)-1)
    def witness(remaining,avail,depth):
        if depth==0:return {'witness':min(remaining)}
        for v in range(n):
            bit=1<<v
            if not(avail&bit):continue
            z=tuple(t for t in remaining if not(t&bit));o=tuple(t for t in remaining if t&bit)
            if z and o and rank(z,avail^bit)>=depth-1 and rank(o,avail^bit)>=depth-1:
                return {'query':v,'zero':witness(z,avail^bit,depth-1),'one':witness(o,avail^bit,depth-1)}
        raise AssertionError('no depth witness')
    return d,witness(h,(1<<n)-1,d)


def check_tree(node,h,n,depth,queries=(),labels=()):
    if depth==0:
        assert set(node)=={'witness'}
        w=node['witness'];assert w in h
        assert all(((w>>v)&1)==label for v,label in zip(queries,labels))
        return {w}
    assert set(node)=={'query','zero','one'}
    v=node['query'];assert isinstance(v,int) and 0<=v<n and v not in queries
    a=check_tree(node['zero'],h,n,depth-1,queries+(v,),labels+(0,))
    b=check_tree(node['one'],h,n,depth-1,queries+(v,),labels+(1,))
    assert a.isdisjoint(b)
    return a|b


def main():
    certificate=json.loads(Path(__file__).with_name('certificate.json').read_text())
    assert certificate['format']=='independent-dominating-depth-trees-v1'
    table=[]
    for n in range(1,14):
        for kind in ('P','C'):
            if kind=='C' and n<3:continue
            h=hypotheses(n,kind)
            v,s=vc(h,n)
            d,w=ldim(h,n)
            table.append({'kind':kind,'n':n,'concept_count':len(h),'vc':v,'ldim':d})
            if (kind,n) in {('P',10),('C',13)}:
                record=certificate[kind+str(n)]
                assert record['kind']==kind and record['vertices']==n
                assert record['vc_dimension']==v and record['littlestone_dimension']==d
                assert record['vc_shattered_support']==s
                assert record['depth_tree']==w
                leaves=check_tree(w,h,n,d)
                assert len(leaves)==(1<<d)
    assert certificate['table']==table
    assert [(x['kind'],x['n']) for x in table if x['ldim']>x['vc']]==[('P',10),('P',13),('C',13)]
    # P13 and C13 also separate. All paths/cycles with <10 vertices have no gap.
    # Every max-degree-two graph on at most ten vertices is a disjoint union of these.
    assert all(x['ldim']==x['vc'] for x in table if x['n']<10)
    assert next(x for x in table if x['kind']=='C' and x['n']==10)['vc']==3
    assert next(x for x in table if x['kind']=='C' and x['n']==10)['ldim']==3
    assert next(x for x in table if x['kind']=='P' and x['n']==10)['vc']==3
    assert next(x for x in table if x['kind']=='P' and x['n']==10)['ldim']==4
    assert all(x['ldim']==x['vc'] for x in table if x['kind']=='C' and x['n']<13)
    print('ALL_DEGREE_TWO_ADAPTIVE_GAP_CHECKS_PASS',len(table))
    for x in table:print('{kind}{n}: count={concept_count}, VC={vc}, LD={ldim}'.format(**x))

if __name__=='__main__':main()
