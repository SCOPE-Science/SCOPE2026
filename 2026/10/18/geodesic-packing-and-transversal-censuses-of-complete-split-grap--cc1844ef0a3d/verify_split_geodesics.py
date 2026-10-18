#!/usr/bin/env python3
"""Independent finite verification of packing/transversal identities on complete split graphs.

No external dependencies; executes shortest-path enumeration, subpath-maximality,
vertex-disjoint packing dynamic programming, and minimal hitting-set tests.
"""
from collections import Counter
from functools import lru_cache
from math import comb, factorial


def adjacent(a, b, r):
    return a != b and (a < r or b < r)


def canonical(path):
    backward = tuple(reversed(path))
    return min(tuple(path), backward)


def maximal_shortest_paths(r, s):
    n = r + s
    geodesics = set()
    for u in range(n):
        for v in range(u + 1, n):
            if adjacent(u, v, r):
                geodesics.add(canonical((u, v)))
            else:
                for w in range(n):
                    if adjacent(u, w, r) and adjacent(w, v, r):
                        geodesics.add(canonical((u, w, v)))
    maximal = []
    for p in geodesics:
        if not any(len(q) > len(p) and
                   (tuple(q[i:i + len(p)]) == p or
                    tuple(q[i:i + len(p)]) == tuple(reversed(p)))
                   for q in geodesics for i in range(len(q)-len(p)+1)):
            maximal.append(p)
    return maximal


def formula_packing(r, s):
    out = Counter({0: 1})
    for t in range(0, min(r, s//2) + 1):
        triple_count = comb(r, t) * factorial(s) // (factorial(s-2*t) * 2**t)
        for u in range(0, (r-t)//2 + 1):
            pair_count = factorial(r-t) // (factorial(r-t-2*u) * 2**u * factorial(u))
            if t + u:
                out[t+u] += triple_count * pair_count
    return out


def direct_packing(paths):
    masks = [sum(1 << v for v in p) for p in paths]
    @lru_cache(maxsize=None)
    def dp(idx, used):
        if idx == len(masks):
            return (1,)
        left = dp(idx + 1, used)
        right = dp(idx+1, used | masks[idx]) if not used & masks[idx] else ()
        arr = [0] * max(len(left), len(right)+1 if right else 0)
        for k, v in enumerate(left): arr[k] += v
        for k, v in enumerate(right): arr[k+1] += v
        return tuple(arr)
    ans = dp(0, 0)
    return Counter({k: v for k, v in enumerate(ans) if v}), dp.cache_info().currsize


def direct_minimal_transversals(paths, n):
    pm = [sum(1 << v for v in p) for p in paths]
    def hitting(mask):
        return all(mask & q for q in pm)
    c = Counter()
    for mask in range(1 << n):
        if hitting(mask) and all(not hitting(mask ^ (1 << v)) for v in range(n) if mask & (1 << v)):
            c[mask.bit_count()] += 1
    return c


def run():
    profiles = subsets = states = maximal_paths = 0
    for r in range(1, 6):
        for s in range(2, 7):
            if r+s > 9:
                continue
            paths = maximal_shortest_paths(r, s)
            predicted = {frozenset((u, v)) for u in range(r) for v in range(u+1, r)}
            predicted |= {frozenset((u, a, b)) for u in range(r)
                          for a in range(r, r+s) for b in range(a+1, r+s)}
            assert {frozenset(p) for p in paths} == predicted, (r, s, paths)
            actual, state_count = direct_packing(paths)
            assert actual == formula_packing(r, s), (r,s,actual,formula_packing(r,s))
            predicted_max = (r + min(r, s//2)) // 2
            assert max(actual) == predicted_max
            hit = direct_minimal_transversals(paths, r+s)
            target_hit = Counter({r:1})
            target_hit[r+s-2] += r*s
            assert hit == target_hit, (r,s,hit,target_hit)
            assert min(hit) == r
            profiles += 1
            subsets += 1 << (r+s)
            states += state_count
            maximal_paths += len(paths)
    # Arithmetic checks beyond exhaustive range, including saturation and parity boundaries.
    for r in range(1, 51):
        for s in range(2, 101):
            a=formula_packing(r,s)
            q=min(r,s//2)
            k=(r+q)//2
            assert max(a)==k
            assert r-k == (r-q+1)//2
            if s>=2*r:
                assert k==r
                assert a[k]==factorial(s)//(factorial(s-2*r)*2**r)
    print(f'VERIFICATION_OK exhaustive_profiles={profiles} vertex_subsets={subsets} packing_dp_states={states} maximal_geodesics={maximal_paths} arithmetic_profiles=5000')


if __name__ == '__main__':
    run()
