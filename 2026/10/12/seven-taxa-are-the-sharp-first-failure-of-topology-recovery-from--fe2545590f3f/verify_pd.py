#!/usr/bin/env python3
"""Exact checks for an ultrametric phylogenetic-rarefaction identifiability boundary.

Requires only the Python standard library. All arithmetic is rational.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb

# An unlabeled rooted full binary shape is None (leaf) or an unordered pair.
def serialize(t):
    return "." if t is None else "(" + serialize(t[0]) + serialize(t[1]) + ")"

@lru_cache(None)
def shapes(n):
    if n == 1:
        return (None,)
    result = {}
    for k in range(1, n // 2 + 1):
        for a in shapes(k):
            for b in shapes(n-k):
                pa, pb = sorted((serialize(a), serialize(b)))
                if k == n-k and serialize(a) > serialize(b):
                    continue
                children = (a,b) if serialize(a) <= serialize(b) else (b,a)
                result["(" + pa + pb + ")"] = children
    return tuple(result[k] for k in sorted(result))

def sizes(t):
    if t is None:
        return 1, []
    a,sa = sizes(t[0]); b,sb = sizes(t[1])
    return a+b, sa+sb+[a,b]

shape_counts = [len(shapes(n)) for n in range(1,8)]
assert shape_counts == [1,1,1,2,3,6,11], shape_counts
support_counts = []
for n in range(2,8):
    groups = defaultdict(list)
    for t in shapes(n):
        count, edge_sizes = sizes(t)
        assert count == n and len(edge_sizes) == 2*n-2
        support = tuple(sorted({s for s in edge_sizes if 1 < s < n}))
        groups[support].append(serialize(t))
    support_counts.append(len(groups))
    if n <= 6:
        assert len(groups) == len(shapes(n))
    if n == 7:
        collision_groups = [g for g in groups.values() if len(g) > 1]
        assert len(collision_groups) == 1
        assert len(collision_groups[0]) == 2
        assert {tuple(sorted({s for s in sizes(x)[1] if 1 < s < n}))
                for x in shapes(n)
                if serialize(x) in collision_groups[0]} == {(2,3,4)}
assert support_counts == [1,1,2,3,6,10], support_counts

# Height-annotated binary trees. A leaf has height 0.
leaf = None
def node(h, a, b):
    return (Q(h), a, b)

A = node(4,
         node(2, leaf, node(1, leaf, leaf)),
         node(3, node(2, leaf, leaf), node(2, leaf, leaf)))
B = node(4,
         node(3, leaf, node(1, leaf, leaf)),
         node(3, leaf, node(2, leaf, node(1, leaf, leaf))))

def edge_list(t):
    edges = []
    def descend(subtree):
        if subtree is None:
            idx = descend.leaf_index
            descend.leaf_index += 1
            return frozenset([idx]), Q(0)
        height, a, b = subtree
        left, ha = descend(a)
        right, hb = descend(b)
        assert height > ha and height > hb
        edges.append((left, height-ha))
        edges.append((right, height-hb))
        return left | right, height
    descend.leaf_index = 0
    all_leaves, root_height = descend(t)
    n = len(all_leaves)
    assert n == 7 and root_height == 4
    for tip in all_leaves:
        assert sum((length for descendants,length in edges
                    if tip in descendants),Q(0)) == 4
    return edges

def clade_weight(edges):
    weights = defaultdict(lambda: Q(0))
    for subset, length in edges:
        weights[len(subset)] += length
    return dict(weights)

E_A,E_B = edge_list(A),edge_list(B)
assert clade_weight(E_A) == clade_weight(E_B) == {1:Q(12),2:Q(3),3:Q(2),4:Q(1)}

def pd(edges, sample):
    sample = set(sample)
    return sum((length for leaves,length in edges
                if not sample.isdisjoint(leaves)),Q(0))

def expected_formula(edges,k,n=7):
    w = clade_weight(edges)
    def n_choose(n1,k1):
        return Q(comb(n1,k1)) if 0 <= k1 <= n1 else Q(0)
    return sum((length*(1-n_choose(n-s,k)/Q(comb(n,k)))
                for s,length in w.items()),Q(0))

means = []
for k in range(0,8):
    dists = []
    for edges in (E_A,E_B):
        vals = [pd(edges,s) for s in combinations(range(7),k)]
        assert len(vals) == comb(7,k)
        mu = sum(vals,Q(0))/len(vals)
        assert mu == expected_formula(edges,k)
        dists.append((mu,Counter(vals)))
    assert dists[0][0] == dists[1][0]
    means.append(dists[0][0])

assert means == [Q(0),Q(4),Q(51,7),Q(351,35),Q(433,35),Q(101,7),Q(114,7),Q(18)], means
# The assert immediately above intentionally uses an independent full-curve checksum.

for label,edges,target,expected_var in (
    ('A',E_A,{Q(5):1,Q(6):4,Q(7):4,Q(8):12},Q(128,147)),
    ('B',E_B,{Q(5):2,Q(6):2,Q(7):5,Q(8):12},Q(142,147))):
    vals = [pd(edges,pair) for pair in combinations(range(7),2)]
    assert dict(Counter(vals)) == target
    m = sum(vals,Q(0))/len(vals)
    v = sum(((z-m)**2 for z in vals),Q(0))/len(vals)
    assert v == expected_var
    print(label, 'two-tip_distribution=', sorted(target.items()), 'variance=',v)

# Invert the complete mean curve by descending binomial elimination.
def invert_curve(curve,n):
    total = curve[n]
    weights = {}
    for k in range(n-1,0,-1):
        y = Q(comb(n,k)) * (total-curve[k])
        for s,w in weights.items():
            if 0 <= k <= n-s:
                y -= w*comb(n-s,k)
        s = n-k
        assert comb(n-s,k)==1
        weights[s] = y
    return weights

assert invert_curve(means,7)=={1:Q(12),2:Q(3),3:Q(2),4:Q(1),5:Q(0),6:Q(0)}
print('VERIFY_OK shapes_1_to_7=',shape_counts,'support_classes_2_to_7=',support_counts)
print('mean_curve=',means,'weighted_clade_sizes=',clade_weight(E_A))
