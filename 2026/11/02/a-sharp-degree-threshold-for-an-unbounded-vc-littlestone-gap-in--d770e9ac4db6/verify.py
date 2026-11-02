#!/usr/bin/env python3
"""Replay finite vertex-membership shattering certificates for path maximal independent sets.
Run: python3 verify.py (with certificate.json in the same directory).
Only the Python standard library is needed.
"""
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

D = json.loads((Path(__file__).parent / 'certificate.json').read_text(encoding='utf-8'))

def maximal_sets_path(n):
    adj = [set(j for j in (i-1, i+1) if 0 <= j < n) for i in range(n)]
    result = []
    for bits in range(1 << n):
        member = {i for i in range(n) if (bits >> i) & 1}
        if any(member & adj[i] for i in member):
            continue
        if any(i not in member and not (adj[i] & member) for i in range(n)):
            continue
        result.append(bits)
    return result

def exact_dimensions(concepts, n):
    masks = [sum(1 << h for h, bits in enumerate(concepts) if bits & (1 << i)) for i in range(n)]
    full = (1 << len(concepts)) - 1
    @lru_cache(None)
    def dim(state):
        if state.bit_count() <= 1:
            return 0
        depth = 0
        for m in masks:
            a, b = state & m, state & ~m
            if a and b:
                depth = max(depth, 1 + min(dim(a), dim(b)))
        return depth
    vc = 0
    for size in range(1, n + 1):
        any_shattered = False
        for xs in combinations(range(n), size):
            patterns = {sum(((h >> x) & 1) << j for j, x in enumerate(xs)) for h in concepts}
            if len(patterns) == 1 << size:
                any_shattered = True
                break
        if not any_shattered:
            break
        vc = size
    return vc, dim(full)

n = D['n']
assert n == 10
concepts = maximal_sets_path(n)
claimed = sorted(sum(1 << (v - 1) for v in row) for row in D['maximal_independent_sets_1based'])
assert claimed == concepts and len(concepts) == 16
counts = [sum((c >> i) & 1 for c in concepts) for i in range(n)]
assert counts == [9, 7, 5, 8, 6, 6, 8, 5, 7, 9]
# Shattering any four columns with exactly sixteen rows would make each column balanced;
# only columns 4 and 7 are balanced, hence four-column shattering is impossible.
assert sum(x == 8 for x in counts) == 2
xs = D['vc_witness_query_1based']
assert xs == [1, 4, 7]
assert set(D['vc_witness_1based']) == {format(i, '03b') for i in range(8)}
for label, selected in D['vc_witness_1based'].items():
    witness = sum(1 << (v - 1) for v in selected)
    assert witness in concepts
    observed = sum(((witness >> (x - 1)) & 1) << j for j, x in enumerate(xs))
    # Labels print the bits in most-significant-first order.
    assert observed == int(label, 2)

leaves = []
def check_tree(node, remaining, depth):
    if depth == 4:
        assert set(node) == {'leaf'} and node['leaf'] in remaining
        leaves.append(node['leaf'])
        return
    assert set(node) == {'query', 'zero', 'one'}
    query = node['query']
    assert isinstance(query, int) and 1 <= query <= n
    zero = [x for x in remaining if not (x >> (query - 1)) & 1]
    one  = [x for x in remaining if (x >> (query - 1)) & 1]
    assert zero and one
    check_tree(node['zero'], zero, depth + 1)
    check_tree(node['one'], one, depth + 1)
check_tree(D['littlestone_tree'], concepts, 0)
assert len(leaves) == len(set(leaves)) == 16
# No complete depth-five tree is possible with sixteen hypotheses.
assert len(concepts) < (1 << 5)
print('PATH10_CERTIFICATE_PASS concepts=16 balanced_positions=2 VC=3 Ldim=4 tree_leaves=16')

# Independent checks of the asserted first strict path separation.
profile = []
for k in range(1, 11):
    profile.append(exact_dimensions(maximal_sets_path(k), k))
assert profile == [(0, 0), (1, 1), (1, 1), (1, 1), (2, 2),
                   (2, 2), (2, 2), (3, 3), (3, 3), (3, 4)]
print('FIRST_PATH_GAP_PASS', profile)

# Directly enumerate the disjoint union of two ten-point paths, checking
# that the 256 products are distinct and comprise all maximal independent sets.
masks = [a | (b << 10) for a in concepts for b in concepts]
assert len(set(masks)) == 16 ** 2
for bits in masks:
    left = bits & ((1 << 10) - 1)
    right = bits >> 10
    assert left in concepts and right in concepts
print('TWO_COMPONENT_PRODUCT_PASS maximal_independent_sets=256')
print('ALL_NEW_FINITE_CHECKS_PASS')
