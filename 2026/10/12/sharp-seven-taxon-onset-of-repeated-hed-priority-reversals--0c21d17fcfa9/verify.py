#!/usr/bin/env python3
"""Exact-arithmetic checks for a phylogenetic marginal-diversity ranking theorem.

Run: python3 verify.py
All computations use Python's standard library and rational arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations

EDGES = (
    ('root','L4',F(1)),
    ('L4','L3',F(1,10)),
    ('L3','L2',F(7,5)),
    ('L2','i',F(3,2)),
    ('L2','a',F(3,2)),
    ('L3','b',F(29,10)),
    ('L4','c',F(3)),
    ('root','R3',F(11,5)),
    ('R3','R2',F(3,50)),
    ('R2','j',F(87,50)),
    ('R2','d',F(87,50)),
    ('R3','e',F(9,5)),
)
LEAVES = ('i','a','b','c','j','d','e')
children = {}
parent = {}
length_to = {}
for u,v,w in EDGES:
    children.setdefault(u,[]).append(v)
    parent[v] = u
    length_to[v] = w
assert set(children).isdisjoint(set(LEAVES))
assert set(parent) == (set(children) | set(LEAVES)) - {'root'}
assert all(len(children[u]) == 2 for u in children)
assert all(w>0 for _,_,w in EDGES)

def descendants(node):
    if node in LEAVES:
        return frozenset((node,))
    return frozenset().union(*(descendants(c) for c in children[node]))

def path_to_root(tip):
    path=[]
    x=tip
    while x!='root':
        path.append(x)
        x=parent[x]
    return path

def pd(subset):
    return sum((w for _,v,w in EDGES if descendants(v) & subset), F(0))

def hed_coeff(tip):
    out={}
    for v in path_to_root(tip):
        k=len(descendants(v))-1
        out[k]=out.get(k,F(0))+length_to[v]
    return out

def hed_poly(tip,q):
    return sum((w*q**k for k,w in hed_coeff(tip).items()), F(0))

def hed_brute(tip,q):
    others=tuple(t for t in LEAVES if t!=tip)
    ans=F(0)
    for k in range(len(others)+1):
        for subset0 in combinations(others,k):
            subset=frozenset(subset0)
            probability=(1-q)**k *q**(len(others)-k)
            ans+=probability*(pd(subset | {tip})-pd(subset))
    return ans

assert descendants('L4') == frozenset(('i','a','b','c'))
assert descendants('L3') == frozenset(('i','a','b'))
assert descendants('L2') == frozenset(('i','a'))
assert descendants('R3') == frozenset(('j','d','e'))
assert descendants('R2') == frozenset(('j','d'))
assert {t: sum((length_to[v] for v in path_to_root(t)),F(0)) for t in LEAVES} == dict.fromkeys(LEAVES,F(4))
assert hed_coeff('i') == {0:F(3,2),1:F(7,5),2:F(1,10),3:F(1)}
assert hed_coeff('j') == {0:F(87,50),1:F(3,50),2:F(11,5)}

def difference(q):
    return hed_poly('i',q)-hed_poly('j',q)

for q in [F(0),F(1,10),F(3,10),F(1,2),F(4,5),F(9,10),F(1)]:
    assert difference(q) == (q-1)*(q-F(3,10))*(q-F(4,5))
    for tip in LEAVES:
        assert hed_brute(tip,q)==hed_poly(tip,q), (tip,q)
assert difference(F(1,10))<0<difference(F(1,2))
assert difference(F(9,10))<0

# Verify the possible branch-size profiles for the proof's lower-bound case.
def shapes(n):
    if n == 1:
        return [None]
    out={}
    for i in range(1,n):
        for a in shapes(i):
            for b in shapes(n-i):
                key=tuple(sorted((repr(a),repr(b))))
                out[key]=(a,b)
    return list(out.values())

def count(tree):
    return 1 if tree is None else count(tree[0])+count(tree[1])

def possible_split_pairs(tree):
    if tree is None:
        return set()
    a,b=tree
    result={(min(count(a),count(b)), max(count(a),count(b)))}
    return result|possible_split_pairs(a)|possible_split_pairs(b)

all_pairs=set()
shape_counts=[]
for n in range(2,7):
    ss=shapes(n)
    shape_counts.append((n,len(ss)))
    for t in ss:
        all_pairs |= possible_split_pairs(t)
        assert count(t)==n
assert all_pairs == {(1,1),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4),(3,3)}
print('VERIFY_OK', 'leaves=7', 'edges=12', 'exact_survivor_summands=3136',
      'shape_counts='+repr(shape_counts), 'roots=(3/10,4/5)',
      'reversal_signs=(-,+,-)')
