#!/usr/bin/env python3
"""Finite checks for q-ary Hamming-graph open-neighborhood learning dimensions.
This program is independent of the mathematical upper-bound proof; it checks
finite cases and all explicitly packaged depth-three mistake-tree certificates.
Run: python3 verify_hamming.py (from a folder containing TREES.json).
"""
import itertools
import json
from functools import lru_cache
from pathlib import Path

def distance(a,b):
    return sum(x!=y for x,y in zip(a,b))

def vertices(d,q):
    return list(itertools.product(range(q), repeat=d))

def truth(d,q):
    vs=vertices(d,q)
    return vs,{query:sum((1<<i) for i,center in enumerate(vs)
                    if distance(center,query)==1) for query in vs}

def exact_L(d,q,max_depth=4):
    vs,pred=truth(d,q)
    allcenters=(1<<len(vs))-1
    qs=list(pred.values())
    @lru_cache(None)
    def can(candidates,remaining):
        if remaining==0:
            return candidates!=0
        if candidates.bit_count()<(1<<remaining):
            return False
        for yes in qs:
            one=candidates & yes
            zero=candidates & (allcenters^yes)
            if (one.bit_count()>=(1<<(remaining-1)) and
                zero.bit_count()>=(1<<(remaining-1)) and
                can(one,remaining-1) and can(zero,remaining-1)):
                return True
        return False
    for depth in range(1,max_depth+1):
        if not can(allcenters,depth):
            return depth-1
    return max_depth

def exact_VC(d,q,up_to=4):
    vs,pred=truth(d,q)
    allcols=list(pred.values())
    for k in range(min(len(vs),up_to),0,-1):
        for S in itertools.combinations(range(len(vs)),k):
            traces={sum(((bits>>i)&1)<<j for j,i in enumerate(S)) for bits in allcols}
            if len(traces)==(1<<k):
                return k
    return 0

def verify_tree(case):
    d,q,depth=case['d'],case['q'],case['depth']
    vs=set(vertices(d,q)); leaves=[]; nodes=[0]
    def walk(node,answers,k):
        if k==0:
            assert set(node)=={'witness'},node
            c=tuple(node['witness'])
            assert c in vs
            assert all((distance(c,x)==1)==bool(bit) for x,bit in answers)
            leaves.append(c)
            return
        assert set(node)=={'query','zero','one'}
        x=tuple(node['query']);assert x in vs
        nodes[0]+=1
        walk(node['zero'],answers+[(x,0)],k-1)
        walk(node['one'],answers+[(x,1)],k-1)
    walk(case['tree'],[],depth)
    assert nodes[0]==2**depth-1
    assert len(leaves)==len(set(leaves))==2**depth
    return nodes[0],len(leaves)

def predicted_L(d,q):
    if d==1:return 1
    if q==2:return {2:1,3:2}.get(d,3)
    return 3

def predicted_VC(d,q):
    if d==1 or (d,q)==(2,2):return 1
    if (d,q) in [(2,3),(3,2)]:return 2
    return 3

def run():
    obj=json.loads(Path(__file__).with_name('TREES.json').read_text(encoding='utf-8'))
    total_nodes=total_leaves=0
    for c in obj['cases']:
        nn,ll=verify_tree(c);total_nodes+=nn;total_leaves+=ll
        assert c['depth']==predicted_L(c['d'],c['q'])
    print('TREE_CERTIFICATES_PASS',len(obj['cases']),total_nodes,total_leaves)
    sampled=[(1,q) for q in range(2,10)]+[(2,q) for q in range(2,8)]+[(3,q) for q in range(2,5)]+[(4,q) for q in range(2,4)]+[(5,2)]
    for d,q in sampled:
        expected=predicted_L(d,q)
        got=exact_L(d,q,max_depth=min(3,expected+1))
        assert got==expected,(d,q,got)
    print('EXACT_LITTLESTONE_GRID_PASS',len(sampled))
    vc_cases=[(1,2),(1,3),(1,7),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2),(5,2)]
    for d,q in vc_cases:
        got=exact_VC(d,q)
        assert got==predicted_VC(d,q),(d,q,got)
    print('EXACT_VC_GRID_PASS',len(vc_cases))
    # Verify the structural pair-intersection restriction with no online depth two.
    for d,q in [(2,3),(2,7),(3,2),(3,5),(4,2)]:
        vs,pred=truth(d,q)
        for a,b in itertools.combinations(vs,2):
            common=pred[a]&pred[b]
            if common.bit_count()<4:continue
            for ymask in pred.values():
                one=(common&ymask).bit_count()
                zero=(common&~ymask).bit_count()
                assert min(one,zero)<=1,(d,q,a,b)
    print('DOUBLE_POSITIVE_BRANCH_OBSTRUCTION_PASS')
    print('HAMMING_OPEN_NEIGHBORHOODS_ALL_CHECKS_PASS')

if __name__=='__main__':run()
