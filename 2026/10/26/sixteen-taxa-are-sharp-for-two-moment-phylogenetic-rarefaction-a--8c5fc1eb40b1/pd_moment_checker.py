"""Exact finite certificates for rooted unit-edge phylogenetic rarefaction.

Run with Python 3.10+ and no third-party dependencies.
All trees are unordered non-plane full rooted binary shapes.
"""
import json
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations

@lru_cache(maxsize=None)
def shapes(n):
    if n == 1:
        return ((),)
    result = []
    for a in range(1, n // 2 + 1):
        b = n - a
        for left in shapes(a):
            for right in shapes(b):
                if a == b and left > right:
                    continue
                result.append((left, right))
    return tuple(result)

def clades(tree):
    leaves = [0]
    all_clades = []
    def visit(node):
        if not node:
            mask = 1 << leaves[0]
            leaves[0] += 1
        else:
            mask = visit(node[0]) | visit(node[1])
        all_clades.append(mask)
        return mask
    full = visit(tree)
    assert all_clades[-1] == full
    return all_clades[:-1]

def signature(tree):
    edges = clades(tree)
    # The list of edge descendant counts and unordered edge-pair union counts
    # determines the first two rarefaction moments for every sample size.
    return (
        tuple(sorted(e.bit_count() for e in edges)),
        tuple(sorted((a | b).bit_count() for a, b in combinations(edges, 2))),
    )

def newick(tree):
    return "*" if not tree else "(" + newick(tree[0]) + "," + newick(tree[1]) + ")"

def witness():
    leaf = ()
    cherry = (leaf, leaf)
    balanced = (cherry, cherry)
    caterpillar3 = (leaf, cherry)
    caterpillar4 = (leaf, caterpillar3)
    grouped = ((caterpillar4, caterpillar4), (balanced, balanced))
    mixed = ((caterpillar4, balanced), (caterpillar4, balanced))
    return grouped, mixed

def moment_table(tree):
    edges = clades(tree)
    n = len(edges) // 2 + 1
    table = defaultdict(lambda: [0, 0, 0, 0])
    at_two = Counter()
    for selection in range(1, 1 << n):
        k = selection.bit_count()
        d = sum(bool(selection & edge) for edge in edges)
        row = table[k]
        row[0] += 1
        row[1] += d
        row[2] += d*d
        row[3] += d*d*d
        if k == 2:
            at_two[d] += 1
    return [table[k] for k in range(1, n+1)], dict(sorted(at_two.items()))

def main():
    counts = {}
    collisions = {}
    only_collision = None
    for n in range(2, 17):
        values = defaultdict(list)
        for tree in shapes(n):
            values[signature(tree)].append(tree)
        colliding = [group for group in values.values() if len(group) > 1]
        counts[str(n)] = len(shapes(n))
        collisions[str(n)] = sum(len(g)*(len(g)-1)//2 for g in colliding)
        if n < 16:
            assert not colliding, (n, len(colliding))
        else:
            assert len(colliding) == 1 and len(colliding[0]) == 2
            only_collision = colliding[0]
    a,b=witness()
    assert a != b and signature(a) == signature(b)
    assert set(only_collision) == {a,b}
    table_a, hist_a=moment_table(a)
    table_b, hist_b=moment_table(b)
    assert all((u[0],u[1],u[2]) == (v[0],v[1],v[2]) for u,v in zip(table_a,table_b))
    assert table_a[1] == [120,898,6904,54370]
    assert table_b[1] == [120,898,6904,54376]
    assert hist_a == {5:7,6:20,7:37,8:20,9:36}
    assert hist_b == {5:6,6:27,7:18,8:45,9:20,10:4}
    out = {
      'tree_counts_by_leaves': counts,
      'two_moment_collision_pairs_by_leaves':collisions,
      'witness_grouped_newick':newick(a)+';',
      'witness_mixed_newick':newick(b)+';',
      'same_signature':True,
      'two_leaf_pd_histogram_grouped':hist_a,
      'two_leaf_pd_histogram_mixed':hist_b,
      'two_leaf_moment_sums_grouped':table_a[1],
      'two_leaf_moment_sums_mixed':table_b[1],
      'first_second_moment_equal_all_sample_sizes':True,
      'third_raw_moment_grouped_minus_mixed_at_two': '-1/20',
      'certification_method': 'Exhaustive canonical recursive generation; exact integer clade masks and sample enumeration',
    }
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=='__main__':main()
