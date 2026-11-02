#!/usr/bin/env python3
"""Independent replay of the eleven-round regular-tournament mistake tree.

A bit 1 on edge (u,v), u<v, means u defeats v. A bit 0 means v defeats u.
"""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json


def tournaments(n):
    edge_list=list(combinations(range(n),2))
    target=(n-1)//2
    out=[]
    for bits in range(1<<len(edge_list)):
        scores=[0]*n
        for j,(u,v) in enumerate(edge_list):
            scores[u if (bits>>j)&1 else v]+=1
        if all(t==target for t in scores):
            out.append(bits)
    return edge_list,out


def projection(h,edge_indices):
    return sum(((h>>j)&1)<<i for i,j in enumerate(edge_indices))


def check_shatters(hypotheses,edge_indices):
    return len({projection(h,edge_indices) for h in hypotheses})==(1<<len(edge_indices))


def check():
    c=json.loads(Path(__file__).with_name('depth11_tree.json').read_text(encoding='utf-8'))
    assert c['n']==7 and c['depth']==11
    edges,H=tournaments(7)
    assert len(H)==2640
    assert [list(e) for e in edges]==c['edge_order']
    Hset=set(H)
    leaves=[]
    internal=0
    def visit(node,level,tests):
        nonlocal internal
        if level==11:
            assert isinstance(node,list) and len(node)==1
            h=node[0]
            assert isinstance(h,int) and h in Hset
            assert all(((h>>q)&1)==b for q,b in tests)
            leaves.append(h)
            return
        assert isinstance(node,list) and len(node)==3
        q,left,right=node
        assert type(q)==int and 0<=q<len(edges)
        assert all(prev_q!=q for prev_q,_ in tests)
        internal+=1
        visit(left,level+1,tests+[(q,1)])
        visit(right,level+1,tests+[(q,0)])
    visit(c['tree'],0,[])
    assert internal==2047 and len(leaves)==2048 and len(set(leaves))==2048
    assert len(H)<2**12
    print('COMPLETE_DEPTH_11_TREE_PASS internal=2047 leaves=2048 unique_tournaments=2048')
    print('NO_DEPTH_12_BY_COUNT_PASS regular_tournaments=2640 threshold=4096')

    for n,expected,vc in ((3,2,1),(5,24,4)):
        edge_list,hyp=tournaments(n)
        assert len(hyp)==expected
        witness=[i for i,(u,v) in enumerate(edge_list) if (u in range((n+1)//2) and v in range((n+1)//2)) or (u in range((n+1)//2,n) and v in range((n+1)//2,n))]
        assert len(witness)==vc and check_shatters(hyp,witness)
        # Check every support directly and compare with the cut predicate.
        for selected in range(1<<len(edge_list)):
            idx=[j for j in range(len(edge_list)) if (selected>>j)&1]
            cut_ok=True
            for subset in range(1,(1<<(n-1))):
                s=subset.bit_count()
                cr=sum(1 for j in idx if ((subset>>edge_list[j][0])&1)!=((subset>>edge_list[j][1])&1))
                if 2*cr>s*(n-s):
                    cut_ok=False;break
            assert cut_ok==check_shatters(hyp,idx),(n,selected)
        print(f'INDEPENDENT_FULL_SHATTER_CUT_CHECK_PASS n={n} supports={1<<len(edge_list)}')

    for chosen_four in combinations(range(7),4):
        first=set(chosen_four)
        edge_indices=[i for i,(u,v) in enumerate(edges) if (u in first)==(v in first)]
        assert len(edge_indices)==9 and check_shatters(H,edge_indices)
    print('DIRECT_9_QUERY_WITNESSES_PASS labeled_extremizers=35 trace_count=512')
    print('REGULAR_TOURNAMENT_ALL_CHECKS_PASS')

if __name__=='__main__':
    check()
