#!/usr/bin/env python3
"""Independent GL(3,2)-matrix verification of all Heawood matching characters."""
from itertools import product
from collections import Counter

P = range(1, 8)
edge_list = [(p, ell) for p in P for ell in P if (p & ell).bit_count() % 2 == 0]
edge_id = {e: k for k, e in enumerate(edge_list)}
matchings = [0]
for edge_idx, (p, ell) in enumerate(edge_list):
    # Each mask is visited exactly once by adjoining a new edge or skipping it.
    matchings.extend(mask | (1 << edge_idx) for mask in tuple(matchings)
                     if all(not (mask >> i & 1) or (p != q and ell != h)
                            for i, (q, h) in enumerate(edge_list[:edge_idx])))
assert len(matchings) == 3462

def mv(M, v):
    return (M[0] if v & 1 else 0) ^ (M[1] if v & 2 else 0) ^ (M[2] if v & 4 else 0)

def trans(M):
    return tuple(sum(((M[j] >> i & 1) << j) for j in range(3)) for i in range(3))

def inverse(M):
    return tuple(next(p for p in P if mv(M, p) == 1 << j) for j in range(3))

def period(mapping):
    x = list(range(21))
    for k in range(1, 17):
        x = [mapping[i] for i in x]
        if x == list(range(21)):
            return k
    raise AssertionError('unbounded order')

def oriented_lefschetz(mapping):
    result = -1
    for mask in matchings[1:]:
        images = [mapping[j] for j in range(21) if mask >> j & 1]
        if sum(1 << j for j in images) != mask:
            continue
        inversions = sum(images[a] > images[b] for a in range(len(images))
                         for b in range(a + 1, len(images)))
        result += -1 if (mask.bit_count() - 1 + inversions) % 2 else 1
    return result

outcomes = Counter()
num_GL = 0
for M in product(range(1, 8), repeat=3):
    if len({mv(M, v) for v in range(8)}) != 8:
        continue
    num_GL += 1
    dual_M = trans(inverse(M))
    for swap in (0, 1):
        image = [edge_id[(mv(M, ell), mv(dual_M, p))] if swap
                 else edge_id[(mv(M, p), mv(dual_M, ell))] for p, ell in edge_list]
        outcomes[(swap, period(image), oriented_lefschetz(image))] += 1
assert num_GL == 168
assert outcomes == {
    (0, 1, 16): 1, (0, 2, 0): 21, (0, 3, 1): 56, (0, 4, 0): 42,
    (0, 7, 2): 48, (1, 2, 4): 28, (1, 6, 1): 56, (1, 8, 0): 84,
}
print('OK: independent matrix enumeration reproduces all 336 character values.')
