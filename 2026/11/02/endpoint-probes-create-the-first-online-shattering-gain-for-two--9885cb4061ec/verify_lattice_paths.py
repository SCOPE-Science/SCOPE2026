"""Finite exact checks for vertex-membership learning of two-east-step grid paths."""
from functools import lru_cache
from itertools import combinations, product
import json
import math
import os


def path_concepts(b):
    result=[]
    for e in combinations(range(b+2),2):
        x=y=0
        path={(0,0)}
        for i in range(b+2):
            if i in e:x+=1
            else:y+=1
            path.add((x,y))
        result.append(frozenset(path))
    return result


def endpoint_concepts(b):
    return [(u,v) for u in range(b+1) for v in range(u,b+1)]


def evaluate_endpoint(u,v,q):
    x,y=q
    if x==0:return y<=u
    if x==1:return u<=y<=v
    if x==2:return y>=v
    raise ValueError(q)


def rank_from_cuts(cuts, n):
    @lru_cache(None)
    def rank(mask):
        best=0
        for c in cuts:
            plus=mask & c
            if plus==0 or plus==mask:continue
            minus=mask ^ plus
            val=1+min(rank(plus), rank(minus))
            if val>best:best=val
        return best
    return rank


def compute_ranks(b, make_certificate=False):
    concepts=endpoint_concepts(b)
    n=len(concepts)
    queries=[(x,y) for x in range(3) for y in range(b+1) if (x,y) not in ((0,0),(2,b))]
    middle=[(1,y) for y in range(b+1)]
    masks={q:sum(1<<i for i,(u,v) in enumerate(concepts) if evaluate_endpoint(u,v,q)) for q in queries}
    whole=(1<<n)-1
    r_full=rank_from_cuts(tuple(masks.values()),n)
    r_mid=rank_from_cuts(tuple(masks[q] for q in middle),n)
    ans=(r_full(whole),r_mid(whole))
    if not make_certificate:return ans
    def build(s, depth):
        if depth==0:
            i=(s & -s).bit_length()-1
            return {'witness':list(concepts[i])}
        for q,m in masks.items():
            pos=s&m
            if pos==0 or pos==s:continue
            neg=s^pos
            if r_full(pos)>=depth-1 and r_full(neg)>=depth-1:
                return {'query':list(q),'no':build(neg,depth-1),'yes':build(pos,depth-1)}
        raise AssertionError((depth,s))
    return ans,build(whole,ans[0])


def main():
    table=[]
    for b in range(1,11):
        pairs=endpoint_concepts(b)
        direct=path_concepts(b)
        assert len(direct)==len(pairs)==(b+1)*(b+2)//2
        for path in direct:
            assert any(all(((x,y) in path)==evaluate_endpoint(u,v,(x,y)) for x in range(3) for y in range(b+1)) for u,v in pairs)
        full,middle=compute_ranks(b)
        table.append((b,len(pairs),full,middle,math.floor(math.log2(len(pairs)))))
    assert [r[2] for r in table]==[1,2,3,3,4,4,4,5,5,6]
    assert [r[3] for r in table]==[1,2,3,3,4,4,4,5,5,5]
    assert all(row[2]==row[4] for row in table[:6])
    assert table[6][2]==4 and table[6][4]==5
    assert all(row[2]==row[3] for row in table[:9])
    assert table[9][2]==6 and table[9][3]==5
    print('EXACT_RANK_TABLE_PASS',table)
    # Direct independent version-space recurrence on enumerated path sets.
    for b in range(1,11):
        paths=path_concepts(b)
        Q=[(x,y) for x in range(3) for y in range(b+1)]
        cuts=[sum(1<<i for i,p in enumerate(paths) if q in p) for q in Q]
        rank=rank_from_cuts(tuple(cuts),len(paths))
        assert rank((1<<len(paths))-1)==table[b-1][2]
    print('INDEPENDENT_PATH_ENUMERATION_PASS')
    # Exhaustively compute VC dimension on small configurations; all-size proof is mathematical.
    for b in range(1,7):
        paths=path_concepts(b)
        qs=[(x,y) for x in range(3) for y in range(b+1) if (x,y) not in ((0,0),(2,b))]
        vc=0
        for k in (1,2,3):
            if any(len({tuple(q in p for q in support) for p in paths})==2**k for support in combinations(qs,k)):vc=k
        assert vc==(1 if b==1 else 2)
    print('SMALL_VC_CENSUS_PASS')
    (r_full,r_middle),tree=compute_ranks(10,True)
    assert (r_full,r_middle)==(6,5)
    witness=[]
    def verify(node,labels):
        if 'witness' in node:
            u,v=node['witness']
            assert 0<=u<=v<=10
            assert all(evaluate_endpoint(u,v,q)==a for q,a in labels)
            witness.append((u,v))
            return
        q=tuple(node['query'])
        verify(node['no'],labels+[(q,False)])
        verify(node['yes'],labels+[(q,True)])
    verify(tree,[])
    assert len(witness)==64 and len(set(witness))==64
    payload={'grid_width':2,'vertical_steps':10,'depth':6,'tree':tree}
    if os.path.exists('depth6_tree.json'):
        with open('depth6_tree.json',encoding='utf8') as f:
            assert json.load(f)==payload, 'Delivered certificate differs from computed witness'
    else:
        with open('depth6_tree.json','w',encoding='utf8') as f:
            json.dump(payload,f,separators=(',',':'));f.write('\n')
    print('DEPTH_SIX_WITNESS_PASS internal=63 leaves=64 distinct=64')
    print('ALL_TWO_EAST_STEP_PATH_CHECKS_PASS')


if __name__=='__main__':main()
