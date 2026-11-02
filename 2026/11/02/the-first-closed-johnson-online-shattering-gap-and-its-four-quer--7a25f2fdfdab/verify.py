#!/usr/bin/env python3
"""Exact finite checks for closed Johnson-neighborhood traces and shattering.

Run with: python verify.py
Requires only Python 3 standard library plus tree.json and orbits.json nearby.
All support sets and all hypothesis centers are generated from first principles.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def instance(n, k, closed):
    vertices = tuple(combinations(range(1, n + 1), k))
    query_masks = []
    for q in vertices:
        Q = set(q)
        query_masks.append(sum(1 << i for i, center in enumerate(vertices)
                    if (len(Q.intersection(center)) >= k-1 if closed
                        else len(Q.intersection(center)) == k-1)))
    return vertices, tuple(query_masks)

def static_count(vertices, query_masks, support):
    # Independent evaluation of the point/subset incidence relation.
    assert len(query_masks) == len(vertices)
    return len({tuple(bool(query_masks[j] & (1 << i)) for j in support)
                for i in range(len(vertices))})

def vc_witnesses(vertices, masks):
    n = len(vertices)
    found = {}
    for d in range(1, n.bit_length()):
        witness = None
        for support in combinations(range(n), d):
            if static_count(vertices, masks, support) == (1 << d):
                witness = support
                break
        if witness is None:
            break
        found[d] = witness
    return found

def ldim(vertices, masks):
    full = (1 << len(vertices)) - 1
    @lru_cache(None)
    def rank(states):
        best = 0
        for m in masks:
            yes = states & m
            no = states & ~m
            if yes and no:
                best = max(best, 1 + min(rank(yes), rank(no)))
        return best
    return rank(full)

def validate_witness_tree(node, remaining, vertices, height):
    if height == 0:
        assert set(node) == {'center'}
        center = tuple(node['center'])
        assert center in remaining
        return 0, [center]
    assert set(node) == {'query','zero','one'}
    q = tuple(node['query'])
    assert q in vertices
    k = len(q)
    yes = {c for c in remaining if len(set(c).intersection(q)) >= k - 1}
    no = remaining - yes
    assert yes and no
    a, aa = validate_witness_tree(node['zero'], no, vertices, height-1)
    b, bb = validate_witness_tree(node['one'], yes, vertices, height-1)
    return 1+a+b, aa+bb

def check_orbits(vertices, masks):
    assert len(vertices)==20
    orbit_rows = json.loads((ROOT/'orbits.json').read_text(encoding='utf-8'))
    index = {v:i for i,v in enumerate(vertices)}
    all_relabelings = [tuple(index[tuple(sorted(p[x-1] for x in v))] for v in vertices)
                       for p in permutations(range(1,7))]
    assert len(all_relabelings)==720
    seen=set(); aggregate=Counter()
    for row in orbit_rows:
        support = tuple(sorted(index[tuple(v)] for v in row['queries']))
        assert len(support)==4 and len(set(support))==4 and support not in seen
        orbit={tuple(sorted(p[i] for i in support)) for p in all_relabelings}
        assert len(orbit)==row['orbit_size']
        assert not (seen & orbit)
        seen.update(orbit)
        count=static_count(vertices,masks,support)
        assert count==row['trace_count']
        aggregate[count]+=len(orbit)
    assert len(orbit_rows)==21 and len(seen)==4845
    assert aggregate == Counter({4:45,8:1680,14:3120}), aggregate
    independent=Counter(static_count(vertices,masks,s) for s in combinations(range(20),4))
    assert independent==aggregate
    return aggregate, len(orbit_rows)

def main():
    table=[]
    for n in range(2,7):
        for k in range(1,n//2+1):
            V,M=instance(n,k,True)
            vc=max(vc_witnesses(V,M),default=0)
            ld=ldim(V,M)
            table.append((n,k,len(V),vc,ld))
            assert vc==ld or (n,k,vc,ld)==(6,3,3,4)
            assert (n,k,vc,ld) in [(2,1,0,0),(3,1,0,0),(4,1,0,0),
                  (4,2,1,1),(5,1,0,0),(5,2,2,2),
                  (6,1,0,0),(6,2,3,3),(6,3,3,4)]
    V,M=instance(6,3,True)
    stats,orbits=check_orbits(V,M)
    for i,C in enumerate(V):
        for j,Q in enumerate(V):
            opposite=tuple(x for x in range(1,7) if x not in C)
            assert (len(set(C)&set(Q)) >=2) != (len(set(opposite)&set(Q)) >=2)
    tree=json.loads((ROOT/'tree.json').read_text(encoding='utf-8'))
    internal,leaves=validate_witness_tree(tree,set(V),V,4)
    assert internal==15 and len(leaves)==16 and len(set(leaves))==16
    W,Mopen=instance(6,3,False)
    open_vc=max(vc_witnesses(W,Mopen),default=0)
    open_ld=ldim(W,Mopen)
    assert (open_vc,open_ld)==(4,4)
    open_support = ((1,2,3),(1,2,4),(1,3,5),(1,4,6))
    assert static_count(W,Mopen,tuple(W.index(q) for q in open_support))==16
    assert static_count(V,M, (0,1,2))==8
    print('JOHNSON_CLOSED_SMALL_PARAMETERS_PASS',table)
    print('J63_CLOSED_FOUR_QUERY_TRACE_ORBITS_PASS',dict(stats),'orbits',orbits,'supports',4845)
    print('J63_DEPTH_FOUR_DECISION_TREE_PASS', 'internal',internal,'leaves',len(leaves))
    print('J63_OPEN_VS_CLOSED_PASS','open',(open_vc,open_ld),'closed',(3,4))
    print('ALL_CLOSED_JOHNSON_FIRST_GAP_CHECKS_PASS')
if __name__=='__main__':main()
