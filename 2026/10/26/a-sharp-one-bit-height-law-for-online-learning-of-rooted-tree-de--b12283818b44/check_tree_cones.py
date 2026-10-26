#!/usr/bin/env python3
"""Self-contained exact-game and constructive certificates for rooted subtree concepts."""
import json
import math
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path


def regular_words(b, h):
    return [tuple()] + [p for d in range(1, h + 1) for p in product(range(b), repeat=d)]


def threshold_witness(h, low, high, depth):
    if depth == 0:
        return None
    cut = low + (1 << (depth - 1))
    assert cut < high and 1 <= cut <= h
    query = (0,) * (cut - 1) + (1,)
    return {'q': list(query), 'one': threshold_witness(h, low, cut, depth - 1),
            'zero': threshold_witness(h, cut, high, depth - 1)}


def prefix_queries(tree, prefix):
    if tree is None:
        return None
    return {'q': list(prefix) + tree['q'],
            'one': prefix_queries(tree['one'], prefix),
            'zero': prefix_queries(tree['zero'], prefix)}


def truncate(tree, depth):
    if depth == 0:
        return None
    assert tree is not None
    return {'q': tree['q'], 'one': truncate(tree['one'], depth - 1),
            'zero': truncate(tree['zero'], depth - 1)}


def full_witness(b, h):
    assert b >= 2 and h >= 0
    if h == 0:
        return None
    if h == 1 and b == 2:
        return {'q': [0], 'one': None, 'zero': None}
    if h == 1:
        return {'q': [0],
                'one': {'q': [1], 'one': None, 'zero': None},
                'zero': {'q': [1], 'one': None, 'zero': None}}
    d = (h + 1).bit_length() - 1
    other = full_witness(b, h - 1)
    return {'q': [0] * h,
            'one': threshold_witness(h, 0, h + 1, d),
            'zero': prefix_queries(truncate(other, d), (1,))}


def height_of_witness(t):
    if t is None:
        return 0
    return 1 + height_of_witness(t['one']) if height_of_witness(t['one']) == height_of_witness(t['zero']) else -1000


def verify_witness(words, tree, depth):
    n = len(words)
    index = {v:i for i,v in enumerate(words)}
    assert len(index) == n
    mask_for_query = {}
    def node_mask(q):
        q = tuple(q)
        if q not in mask_for_query:
            a = 0
            for i in range(len(q) + 1):
                a |= 1 << index[q[:i]]
            mask_for_query[q] = a
        return mask_for_query[q]
    leaves = []
    def recurse(t, mask, decisions):
        if t is None:
            assert len(decisions) == depth and mask != 0, (decisions,mask)
            leaves.append((decisions,mask.bit_count()))
            return
        qmask = node_mask(t['q'])
        assert t['one'] is not None or len(decisions) + 1 == depth
        recurse(t['one'], mask & qmask, decisions + '1')
        recurse(t['zero'], mask & ~qmask, decisions + '0')
    recurse(tree, (1 << n) - 1, '')
    assert len(leaves) == 1 << depth
    return len(leaves), min(z for _,z in leaves), len(mask_for_query)


def exact_dim(words):
    n = len(words)
    queries = [sum((1 << i) for i,v in enumerate(words) if v == w[:len(v)]) for w in words]
    @lru_cache(None)
    def game(mask):
        if mask.bit_count() <= 1:
            return 0
        best = 0
        for qmask in queries:
            pos = mask & qmask
            neg = mask ^ pos
            if pos and neg:
                v = 1 + min(game(pos), game(neg))
                if v > best:
                    best = v
        return best
    value = game((1 << n) - 1)
    return value,game.cache_info().currsize


def vc_dim(words):
    concepts=[{x for x in words if len(x)>=len(v) and x[:len(v)]==v} for v in words]
    for t in range(3, -1, -1):
        for sample in combinations(words,t):
            traces={tuple(int(x in c) for x in sample) for c in concepts}
            if len(traces)==1 << t:
                return t
    return 0


def rooted_from_parents(par):
    words=[tuple()]
    for i, p in enumerate(par, start=1):
        words.append(words[p] + (i,))
    return words


def main():
    here=Path(__file__).resolve().parent
    cases=[(2,0),(2,1),(3,1),(4,1),(2,2),(3,2),(2,3),(2,7),(2,15)]
    certificates={}
    for b,h in cases:
        tree=full_witness(b,h)
        dim = 0 if h==0 else (1 if b==2 and h==1 else 1 + ((h + 1).bit_length()-1))
        assert height_of_witness(tree)==dim
        words=regular_words(b,h)
        verified = (1,1,0) if dim==0 else verify_witness(words,tree,dim)
        assert verified[0]==1<<dim
        if len(words)<=15:
            exact,states=exact_dim(words)
            assert exact==dim, (b,h,exact,dim)
            assert vc_dim(words)==(0 if h==0 else (1 if b==2 and h==1 else 2))
        else:
            exact,states=None,None
        certificates[f'{b}_{h}']={'branch_factor':b,'height':h,'depth':dim,
                'hypotheses':len(words),'path_count':verified[0],
                'min_consistent_hypotheses_per_path':verified[1],
                'distinct_queries':verified[2],
                'exact_game_dimension':exact,'game_states':states,
                'shattered_tree':tree}
        print(f'REGULAR b={b} h={h} Ldim={dim} leaves={verified[0]} min_support={verified[1]} exact_game={exact}', flush=True)
    # The all-0 branch of every witness must be consistent, as checked above.
    for h in range(0,9):
        words=[(0,)*i for i in range(h+1)]
        exact,_=exact_dim(words)
        assert exact == (h+1).bit_length()-1
        if h>0: assert vc_dim(words)==1
        print(f'PATH h={h} exact_Ldim={exact}',flush=True)
    count=0
    # Every finite rooted tree admits a parent-before-child labeling.
    for n in range(1,8):
        for parent in product(*(range(i) for i in range(1,n))):
            words=rooted_from_parents(parent)
            h=max(map(len,words))
            exact,_=exact_dim(words)
            assert (h+1).bit_length()-1 <= exact <= 1+(h+1).bit_length()-1
            assert vc_dim(words)<=2
            count+=1
    print(f'GENERAL_SHAPE_CHECKS {count} parent-before-child rooted trees of orders 1..7',flush=True)
    (here/'witness_trees.json').write_text(json.dumps({'description':'Full complete shattered trees; coordinates are root-to-node words; one means membership in a descendant cone.', 'certificates':certificates},sort_keys=True,separators=(',',':'))+'\n')
    print('ALL_CERTIFICATES_OK',flush=True)


if __name__=='__main__':main()
