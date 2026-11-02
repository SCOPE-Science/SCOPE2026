"""Verify an explicit edge-query mistake tree for perfect matchings of a 2-by-n ladder.

Standard Python 3; the JSON witness is the sole external input.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
obj=json.loads((ROOT/'ladder11_tree.json').read_text(encoding='utf-8'))
n=obj['n']
assert n==11 and obj['depth']==7

# Enumerate perfect matchings independently as edge sets in the 22-vertex graph.
N=2*n
neighbors=[set() for _ in range(N)]
for c in range(n):
    a,b=c,c+n
    neighbors[a].add(b);neighbors[b].add(a)
    if c+1<n:
        for r in (0,n):
            u,v=r+c,r+c+1
            neighbors[u].add(v);neighbors[v].add(u)

def perfect_matchings(available):
    if not available:
        yield frozenset()
        return
    u=min(available)
    for v in sorted(neighbors[u] & available):
        e=(u,v) if u<v else (v,u)
        for tail in perfect_matchings(available-{u,v}):
            yield tail|{e}

matches=list(perfect_matchings(set(range(N))))
assert len(matches)==144 and len(set(matches))==144

# Reconstruct a 10-bit horizontal-pair signature from each graph matching.
def signature(M):
    bits=0
    for c in range(n-1):
        top=(c,c+1) in M
        bottom=(n+c,n+c+1) in M
        assert top==bottom
        if top: bits |= 1<<c
    for c in range(n):
        rung=(c,n+c) in M
        expected=not ((c>0 and bits>>(c-1)&1) or (c<n-1 and bits>>c&1))
        assert rung==expected
    return bits

by_signature={signature(M):M for M in matches}
assert len(by_signature)==144

def label(M,query):
    col=int(query[1:])-1
    if query[0]=='v':
        assert 0<=col<n
        return (col,n+col) in M
    assert query[0]=='h' and 0<=col<n-1
    return (col,col+1) in M

leaves=[]
def check(node,candidates,depth):
    if 'tiling' in node:
        assert depth==0 and set(node)=={'tiling'}
        sig=node['tiling']
        assert type(sig) is int and sig in by_signature
        assert by_signature[sig] in candidates
        leaves.append(sig)
        return 0,1
    assert depth>0 and set(node)=={'query','zero','one'}
    q=node['query'];assert isinstance(q,str) and q[0] in 'vh'
    false_set=frozenset(M for M in candidates if not label(M,q))
    true_set=frozenset(M for M in candidates if label(M,q))
    assert false_set and true_set and len(false_set)+len(true_set)==len(candidates)
    a=check(node['zero'],false_set,depth-1)
    b=check(node['one'],true_set,depth-1)
    return a[0]+b[0]+1,a[1]+b[1]

nodes,leaf_count=check(obj['tree'],frozenset(matches),obj['depth'])
assert nodes==127 and leaf_count==128
assert len(set(leaves))==128
assert 144<256
print('LADDER11_TREE_CERTIFICATE_PASS graph_matchings=144 internal_nodes=127 distinct_leaves=128 depth=7')
print('LADDER11_LITTLESTONE_EXACT_PASS value=7 entropy_upper=7')
