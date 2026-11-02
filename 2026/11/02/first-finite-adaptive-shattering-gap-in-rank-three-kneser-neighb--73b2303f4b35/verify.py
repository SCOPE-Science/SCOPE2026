#!/usr/bin/env python3
"""Exact finite decision-tree certificates for pairwise disjointness of triples."""
import json
from itertools import combinations
from functools import lru_cache
from pathlib import Path

EXPECTED={3:0,4:0,5:0,6:1,7:2,8:3,9:4,10:5,11:6}

def instance(n):
    triples=list(combinations(range(n),3))
    masks=[]
    for q in triples:
        sq=set(q)
        masks.append(sum(1<<j for j,t in enumerate(triples) if sq.isdisjoint(t)))
    return triples,masks

def certificate(n,dim):
    triples,masks=instance(n)
    allmask=(1<<len(triples))-1
    @lru_cache(None)
    def exists(s,d):
        if not d:return s != 0
        if s.bit_count() < (1<<d):return False
        for i,q in enumerate(masks):
            pos=s&q;neg=s^pos
            if min(pos.bit_count(),neg.bit_count())<(1<<(d-1)):continue
            if exists(pos,d-1) and exists(neg,d-1):return True
        return False
    assert exists(allmask,dim)
    assert not exists(allmask,dim+1)
    def build(s,d):
        if not d:
            return {'witness':next(i for i in range(len(triples)) if (s>>i)&1)}
        for i,q in enumerate(masks):
            pos=s&q;neg=s^pos
            if min(pos.bit_count(),neg.bit_count())<(1<<(d-1)):continue
            if exists(pos,d-1) and exists(neg,d-1):
                return {'query':i,'zero':build(neg,d-1),'one':build(pos,d-1)}
        raise AssertionError('No certificate')
    tree=build(allmask,dim)
    return {'n':n,'dim':dim,'states':exists.cache_info().currsize,'tree':tree}, triples, masks

def validate_tree(tree,triples,masks,depth):
    leaves=[];nodes=0
    def visit(node,history):
        nonlocal nodes
        if 'witness' in node:
            assert len(history)==depth
            witness=node['witness']
            for q,b in history:
                assert int(bool(masks[q]&(1<<witness)))==b
            leaves.append(witness)
            return
        nodes+=1
        q=node['query']
        assert 0<=q<len(masks)
        visit(node['zero'],history+[(q,0)])
        visit(node['one'],history+[(q,1)])
    visit(tree,[])
    assert len(leaves)==2**depth and len(set(leaves))==len(leaves)
    assert nodes==2**depth-1
    return nodes,len(leaves)

def main():
    p=Path(__file__).resolve().parent/'trees.json'
    rows=[]
    for n,dim in EXPECTED.items():
        rec,triples,masks=certificate(n,dim)
        nodes,leaves=validate_tree(rec['tree'],triples,masks,dim)
        rows.append(rec)
        print('EXACT_KNESER_3 n=%d hypotheses=%d depth=%d states=%d nodes=%d leaves=%d PASS'%(n,len(triples),dim,rec['states'],nodes,leaves))
    if p.exists():
        assert json.loads(p.read_text())==rows
        print('INDEPENDENT_CERTIFICATE_REPLAY_PASS')
    else:
        p.write_text(json.dumps(rows,sort_keys=True,separators=(',',':'))+'\n')
        print('CERTIFICATES_WRITTEN')
    print('ALL_EXACT_FINITE_CHECKS_PASS')
if __name__=='__main__':main()
