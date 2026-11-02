#!/usr/bin/env python3
"""Standalone verifier for complete comparison trees of small separable permutations.

Run from this directory: python3 verify_separable.py
Only Python's standard library is required.
"""
import itertools
import json
from pathlib import Path


def closure_enumeration(n):
    """Independent enumeration from sum/skew closure, without pattern tests."""
    by_len={1:{(0,)}}
    for k in range(2,n+1):
        found=set()
        for a in range(1,k):
            b=k-a
            for x in by_len[a]:
                for y in by_len[b]:
                    found.add(x+tuple(t+a for t in y))
                    found.add(tuple(t+b for t in x)+y)
        by_len[k]=found
    return by_len[n]


def pattern_enumeration(n):
    """Independent direct avoidance filter over all permutations."""
    forbidden={(1,3,0,2),(2,0,3,1)}
    def sep(p):
        for sub in itertools.combinations(p,4):
            order=sorted(sub)
            rank=tuple(order.index(t) for t in sub)
            if rank in forbidden:return False
        return True
    return {p for p in itertools.permutations(range(n)) if sep(p)}


def verify_tree(n,perms,queries,tree,depth):
    leaves=[]
    used_nodes=0
    def rec(node,version,remaining):
        nonlocal used_nodes
        assert isinstance(node,dict)
        if remaining==0:
            assert set(node)=={'w'}
            witness=tuple(node['w'])
            assert witness in perms and witness in version
            leaves.append(witness)
            return
        assert set(node)=={'q','zero','one'}
        q=node['q'];assert type(q)==int and 0<=q<len(queries)
        a,b=queries[q]
        zero={p for p in version if p[a]>p[b]}
        one={p for p in version if p[a]<p[b]}
        assert len(zero)>0 and len(one)>0
        used_nodes+=1
        rec(node['zero'],zero,remaining-1)
        rec(node['one'],one,remaining-1)
    rec(tree,perms,depth)
    assert used_nodes==2**depth-1
    assert len(leaves)==len(set(leaves))==2**depth
    return used_nodes,len(leaves)


def adjacent_vc_lower(n,perms):
    # Explicitly check all fixed adjacent-comparison patterns.
    patterns={tuple(int(p[i]<p[i+1]) for i in range(n-1)) for p in perms}
    assert len(patterns)==2**(n-1)


def main():
    data=json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf-8'))
    cases=data['cases'];assert len(cases)==7
    expected=[1,2,6,22,90,394,1806]
    lds=[]
    for n,c in enumerate(cases,1):
        assert c['n']==n
        closure=closure_enumeration(n)
        avoiding=pattern_enumeration(n)
        assert closure==avoiding and len(closure)==expected[n-1]
        queries=list(itertools.combinations(range(n),2))
        assert c['queries']==[list(p) for p in queries]
        depth=len(closure).bit_length()-1
        assert c['count']==len(closure) and c['depth']==depth
        internal,leaves=verify_tree(n,closure,queries,c['tree'],depth)
        adjacent_vc_lower(n,closure)
        assert n-1<=depth
        lds.append(depth)
        print('TREE_PASS n=%d concepts=%d depth=%d internal=%d leaves=%d'%(n,len(closure),depth,internal,leaves))
    assert lds==[0,1,2,4,6,8,10]
    print('SEPARABLE_ALL_NEW_CHECKS_PASS')

if __name__=='__main__':main()
