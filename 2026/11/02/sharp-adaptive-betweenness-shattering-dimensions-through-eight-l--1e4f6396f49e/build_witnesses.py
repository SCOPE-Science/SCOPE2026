"""Construct full ternary-betweenness Littlestone trees for sizes 3 through 8.
Run: python build_witnesses.py --out certificates.json
No external dependencies are required.
"""
import argparse
import itertools
import json
import math
from functools import lru_cache
from pathlib import Path


def cases(n):
    orders=[p for p in itertools.permutations(range(n)) if p[0]<p[-1]]
    questions=[]
    for x,y,z in itertools.combinations(range(n),3):
        questions.extend(((x,y,z),(y,x,z),(x,z,y)))
    masks=[]
    for a,b,c in questions:
        membership=0
        for k,p in enumerate(orders):
            where={value:i for i,value in enumerate(p)}
            if min(where[a],where[c])<where[b]<max(where[a],where[c]):
                membership |= 1<<k
        masks.append(membership)
    return orders,questions,masks


def build(n,d):
    orders, questions, masks=cases(n)
    all_concepts=(1<<len(orders))-1
    @lru_cache(None)
    def choose(concepts, depth):
        if depth==0: return -1
        if concepts.bit_count()<1<<depth: return None
        candidates=[]
        for j, q in enumerate(masks):
            yes=concepts&q
            no=concepts^yes
            if yes.bit_count()<1<<(depth-1) or no.bit_count()<1<<(depth-1):
                continue
            candidates.append((abs(yes.bit_count()-no.bit_count()),j,yes,no))
        candidates.sort()
        for _,j,yes,no in candidates:
            if choose(yes,depth-1) is not None and choose(no,depth-1) is not None:
                return j
        return None
    assert choose(all_concepts,d) is not None, (n,d)
    labels=[-1]*(1<<d)
    leaves=[-1]*(1<<d)
    def traverse(state,depth,index):
        if depth==0:
            bit=(state & -state).bit_length()-1
            leaves[index-(1<<d)]=bit
            return
        j=choose(state,depth)
        assert j is not None
        labels[index]=j
        yes=state & masks[j]
        traverse(yes,depth-1,index*2)
        traverse(state^yes,depth-1,index*2+1)
    traverse(all_concepts,d,1)
    print('n',n,'d',d,'permutations',len(orders),'query-types',len(questions),'internal',len(labels)-1,'leaves',len(leaves),'cache',choose.cache_info())
    return {'n':n,'depth':d,'node_queries':labels[1:],'leaf_permutation_indices':leaves}


def main():
    arg=argparse.ArgumentParser()
    arg.add_argument('--out',default='certificates.json')
    a=arg.parse_args()
    entries=[build(n,d) for n,d in [(3,1),(4,3),(5,5),(6,7),(7,10),(8,13)]]
    Path(a.out).write_text(json.dumps({'schema':'ternary_betweenness_trees_v1','entries':entries},separators=(',',':'))+'\n',encoding='utf-8')

if __name__=='__main__':main()
