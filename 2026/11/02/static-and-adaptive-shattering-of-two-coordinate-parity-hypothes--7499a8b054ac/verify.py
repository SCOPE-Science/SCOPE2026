#!/usr/bin/env python3
"""Self-contained verifier of parity-cut adaptive trees and static witnesses."""
import json
from itertools import combinations
from pathlib import Path

HERE=Path(__file__).resolve().parent
TREES=json.loads((HERE/'shattering_trees.json').read_text(encoding='utf-8'))

def check_tree(n, depth, node, viable, visited):
    if depth == 0:
        assert set(node) == {'edge'}
        pair=tuple(node['edge'])
        assert 0<=pair[0]<pair[1]<n and pair in viable
        assert pair not in visited
        visited.add(pair)
        return 1
    assert set(node)=={'cut','zero','one'}
    cut=node['cut']
    assert isinstance(cut,int) and 1 <= cut < 1<<(n-1)
    inside=lambda v: bool((cut >> (v-1)) & 1) if v>0 else False
    one={e for e in viable if inside(e[0])!=inside(e[1])}
    zero=viable-one
    assert len(one)>=1<<(depth-1) and len(zero)>=1<<(depth-1)
    return check_tree(n,depth-1,node['one'],one,visited)+check_tree(n,depth-1,node['zero'],zero,visited)

for n in (5,7,9):
    t=TREES[str(n)]
    assert (t['n'],t['depth']) == (n,{5:3,7:4,9:5}[n])
    visited=set()
    E=set(combinations(range(n),2))
    assert check_tree(n,t['depth'],t['tree'],E,visited) == 1<<t['depth']
    assert len(visited) == 1<<t['depth']

def nonzero_sums(A):
    assert len(A)==len(set(A))
    return {x^y for x,y in combinations(A,2)}

# Each family of d fixed query vectors gives vertex signatures in GF(2)^d.
# Duplicate one signature to realize the all-zero output (same-signature pair).
bases={
    1:[0,1],
    2:[0,1,2],
    3:[0,1,2,4,7],
    4:[0,1,2,4,8,15],
    5:[0,21,9,24,23,7,25,29,30,14],
}
for d,A in bases.items():
    assert len(nonzero_sums(A)) == (1<<d)-1
    assert 0 not in nonzero_sums(A)
    n=len(A)+1
    vertex_signatures=A+[A[0]]
    outputs={vertex_signatures[i]^vertex_signatures[j]
             for i,j in combinations(range(n),2)}
    assert outputs==set(range(1<<d))

# Structural count upper bound: a zero signature forces a repeated column,
# leaving at most n-1 different columns, hence at most C(n-1,2)
# distinct nonzero signatures across all edges.
vc={2:0,3:1,4:2,5:2,6:3,7:4,8:4,9:4,10:4,11:5}
ld={2:0,3:1,4:2,5:3,6:3,7:4,8:4,9:5,10:5,11:5}
from math import comb
for n in range(2,12):
    assert (1<<ld[n]) <= comb(n,2) < (1<<(ld[n]+1))
    assert vc[n] <= ld[n]
    assert (1<<vc[n]) <= 1+comb(n-1,2)
assert [n for n in range(2,12) if vc[n]<ld[n]] == [5,9,10]
print('PARITY_CUT_TREE_AND_BASIS_CHECKS_PASS 3 5 3')
print('VC_DIMENSIONS',','.join(str(vc[n]) for n in range(2,12)))
print('LD_DIMENSIONS',','.join(str(ld[n]) for n in range(2,12)))
print('NOTE: no_nine_basis.cpp separately proves the n=10 VC upper bound.')
