#!/usr/bin/env python3
"""Exact finite shattering and online-shattering computations for labeled 2-factors."""
import argparse
import itertools
import json
from functools import lru_cache
from pathlib import Path

EXPECTED = {
    3: (1, [1], 0, 0),
    4: (3, [1,6], 1, 1),
    5: (12, [1,10,45,60], 3, 3),
    6: (70, [1,15,105,395,360], 4, 5),
    7: (465, [1,21,210,1190,3780,2520], 5, 6),
}

def factors(n):
    edges = list(itertools.combinations(range(n), 2))
    ans = []
    for support in itertools.combinations(range(len(edges)), n):
        deg = [0]*n
        for i in support:
            a,b = edges[i]
            deg[a] += 1
            deg[b] += 1
        if all(d == 2 for d in deg):
            ans.append(sum(1 << i for i in support))
    return edges,ans

def masks_for_factors(factors_list, qcount):
    return [sum((1 << i) for i,f in enumerate(factors_list) if f & (1 << j))
            for j in range(qcount)]

def vc_census(F, qcount):
    counts = [1]
    front = [()]
    one = None
    while front:
        nxt = []
        for s in front:
            for q in range(s[-1]+1 if s else 0, qcount):
                t = s + (q,)
                patterns = set()
                for f in F:
                    pat = 0
                    for i,j in enumerate(t):
                        if f & (1 << j): pat |= 1 << i
                    patterns.add(pat)
                    if len(patterns) == (1 << len(t)):break
                if len(patterns) == (1 << len(t)):
                    nxt.append(t)
        if not nxt:break
        front = nxt
        counts.append(len(front))
        one=front[0]
    return counts,one

def oracle_factory(B):
    @lru_cache(None)
    def can(S,k):
        if k == 0: return True
        if S.bit_count() < (1 << k): return False
        for q in B:
            p=S & q
            z=S & ~q
            if min(p.bit_count(),z.bit_count()) < (1 << (k-1)):continue
            if can(p,k-1) and can(z,k-1):return True
        return False
    return can

def construct_tree(S,k,B,can):
    if k == 0:
        assert S
        return {'witness': (S & -S).bit_length()-1}
    for q,Bq in enumerate(B):
        p=S & Bq
        z=S & ~Bq
        if min(p.bit_count(),z.bit_count()) >= (1 << (k-1)) and can(p,k-1) and can(z,k-1):
            return {'query':q,'zero':construct_tree(z,k-1,B,can),'one':construct_tree(p,k-1,B,can)}
    raise AssertionError('No depth witness')

def check_tree(tree,F,B,k):
    leaf=[]
    def visit(node,S,remaining):
        if remaining==0:
            wi=node['witness']
            assert set(node)=={'witness'} and S >>wi &1
            leaf.append(wi)
            return
        q=node['query']
        assert set(node)=={'query','zero','one'} and 0<=q<len(B)
        a=S & B[q];b=S & ~B[q]
        assert a and b
        visit(node['zero'],b,remaining-1)
        visit(node['one'],a,remaining-1)
    visit(tree,(1<<len(F))-1,k)
    assert len(leaf)==2**k and len(set(leaf))==2**k
    return len(leaf)

def run(emit=None):
    cert={'schema_version':1,'description':'Complete labeled 2-factor online witness trees','trees':{}}
    for n in sorted(EXPECTED):
        edges,F=factors(n); B=masks_for_factors(F,len(edges))
        hcount,counts,vd,ld = EXPECTED[n]
        assert len(F)==hcount
        got,witness=vc_census(F,len(edges))
        assert got==counts,(n,got)
        assert (len(got)-1)==vd
        assert len(set(F))==len(F)
        root=(1<<len(F))-1
        can=oracle_factory(B)
        assert can(root,ld)
        assert not can(root,ld+1)
        tree=construct_tree(root,ld,B,can)
        leaves=check_tree(tree,F,B,ld)
        cert['trees'][str(n)] = {'depth':ld,'edge_order':[list(e) for e in edges],
                                  'factors':[format(f,'x') for f in F],
                                  'tree':tree,'vc_support':list(witness or ())}
        print(f'FACTOR_N{n}_PASS hypotheses={len(F)} shattered_support_counts={counts} VC={vd} LD={ld} leaves={leaves}')
        if n==7:
            fixed=oracle_factory(B)
            assert not fixed(B[0],6)
            assert fixed(B[0],5)
            print('SEVEN_VERTEX_SYMMETRIC_POSITIVE_BRANCH_PASS positive_count=',B[0].bit_count(),
                  'can_depth_six=0','tested_states=',fixed.cache_info().currsize)
    if emit:
        Path(emit).write_text(json.dumps(cert,sort_keys=True,separators=(',',':'))+'\n',encoding='utf8')
    else:
        print('ALL_TWO_FACTOR_FINITE_CHECKS_PASS')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--emit',default=None)
    args=ap.parse_args();run(args.emit)
