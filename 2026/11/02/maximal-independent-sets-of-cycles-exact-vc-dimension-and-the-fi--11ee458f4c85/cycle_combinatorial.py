"""Independent cyclic-gap model and iterative adaptive-shattering verification.
All maximal independent sets of a cycle have successive selected-vertex gaps 2 or 3.
Run: python cycle_combinatorial.py certificate.json
"""
import json
import sys
from functools import lru_cache
from itertools import combinations

def gap_words(n):
    @lru_cache(None)
    def compositions(total):
        if total==0:return ((),)
        if total<0:return ()
        return tuple((d,)+p for d in (2,3) for p in compositions(total-d))
    outcomes=set()
    for start in range(n):
        for gaps in compositions(n):
            vertices=[]
            pos=start
            for gap in gaps:
                vertices.append(pos % n)
                pos+=gap
            if pos!=start+n:raise AssertionError('bad wrap')
            mask=sum(1<<v for v in vertices)
            outcomes.add(mask)
    return sorted(outcomes)

def iterative_depth(concepts,n):
    N=len(concepts)
    masks=[]
    for q in range(n):
        positive=0
        for j,c in enumerate(concepts):
            if (c>>q)&1: positive |=1<<j
        masks.append(positive)
    full=(1<<N)-1
    @lru_cache(None)
    def shatters(space,depth):
        if depth==0:return space!=0
        if space.bit_count() < 1<<depth:return False
        return any(shatters(space&pos,depth-1) and shatters(space&(full^pos),depth-1)
                   for pos in masks)
    d=0
    while shatters(full,d+1):d+=1
    return d

def independent_vc(concepts,n):
    best=0
    for k in range(n+1):
        if (1<<k)>len(concepts):break
        if any(len({tuple((c>>j)&1 for j in support) for c in concepts}) == (1<<k)
               for support in combinations(range(n),k)):
            best=k
    return best

def check_tree(tree, concepts):
    outcomes=[]
    def walk(node,path):
        if 'witness' in node:
            h=node['witness']
            assert h in concepts
            assert all(((h>>j)&1)==a for j,a in path)
            outcomes.append(h)
        else:
            j=node['query']
            walk(node['zero'],path+[(j,0)])
            walk(node['one'],path+[(j,1)])
    walk(tree,[])
    assert len(outcomes)==32==len(set(outcomes))


def main(path):
    cert=json.load(open(path,encoding='utf8'))
    table=[]
    for n in range(3,14):
        concepts=gap_words(n)
        vc=independent_vc(concepts,n)
        ld=iterative_depth(concepts,n)
        table.append([n,len(concepts),vc,ld])
    assert table==cert['small_cycle_table']
    concepts=gap_words(13)
    assert len(concepts)==39
    check_tree(cert['depth_five_tree'],concepts)
    # Independently compare every five-query support against the full pattern cube.
    nonshattered=0
    best=0
    for sample in combinations(range(13),5):
        patterns={sum(((m>>i)&1)<<t for t,i in enumerate(sample)) for m in concepts}
        nonshattered+=len(patterns)!=32
        best=max(best,len(patterns))
    assert nonshattered==1287 and best==29
    print('CYCLIC_GAP_ENCODING_PASS cases=11 n=3..13')
    print('INDEPENDENT_ADAPTIVE_RANKS_PASS table=',table)
    print('INDEPENDENT_C13_FIVE_QUERY_EXHAUSTIVE_PASS no_shattered=1287 max_traces=29')
    print('INDEPENDENT_C13_TREE_PASS')

if __name__=='__main__':
    assert len(sys.argv)==2
    main(sys.argv[1])
