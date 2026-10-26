"""Independent finite checks for zero-forcing sets in the complete edge subdivision of a clique."""
from collections import Counter
from itertools import combinations
from math import comb
import random


def data(n):
    edges = list(combinations(range(n), 2))
    adj = [0] * (n + len(edges))
    for t, (u, v) in enumerate(edges):
        e = n + t
        adj[u] |= 1 << e
        adj[v] |= 1 << e
        adj[e] = (1 << u) | (1 << v)
    return edges, adj


def is_fort(mask, adj):
    if not mask:
        return False
    for i, neighbors in enumerate(adj):
        if not mask >> i & 1 and (neighbors & mask).bit_count() == 1:
            return False
    return True


def is_forcing(mask, adj):
    full = (1 << len(adj)) - 1
    while mask != full:
        changed = False
        for i, neighbors in enumerate(adj):
            if mask >> i & 1:
                rest = neighbors & ~mask
                if rest and not rest & (rest - 1):
                    mask |= rest
                    changed = True
        if not changed:
            break
    return mask == full


def forest(n, edges, unused):
    parent = list(range(n))
    def find(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for i, (u, v) in enumerate(edges):
        if unused >> i & 1:
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return True


def predicted(n, edges, selected):
    m = len(edges)
    old = selected & ((1 << n) - 1)
    if not old:
        return False
    new = selected >> n
    complement = ((1 << m) - 1) ^ new
    if not forest(n, edges, complement):
        return False
    if old.bit_count() >= 2:
        return True
    v = old.bit_length() - 1
    return any((new >> i & 1) and v in e for i, e in enumerate(edges))


def expected_minimal_forts(n, edges):
    m = len(edges)
    masks = set()
    masks.add((1 << n) - 1)
    for v in range(n):
        masks.add((((1 << n) - 1) ^ (1 << v)) |
                  sum(1 << (n + i) for i, e in enumerate(edges) if v in e))
    for chosen in range(1 << m):
        if forest(n, edges, chosen):
            continue
        # A minimal non-forest edge-set is a simple cycle.
        if any(not forest(n, edges, chosen & ~(1 << i)) for i in range(m) if chosen >> i & 1):
            continue
        masks.add(chosen << n)
    return masks


def run(n):
    edges, adj = data(n)
    length = len(adj)
    polynomial = Counter()
    expected_poly = Counter()
    for sel in range(1 << length):
        actual = is_forcing(sel, adj)
        calculated = predicted(n, edges, sel)
        if actual != calculated:
            raise AssertionError((n, sel, actual, calculated))
        if actual:
            polynomial[sel.bit_count()] += 1
    m = len(edges)
    for f in range(1 << m):
        if forest(n, edges, f):
            k = m - f.bit_count()
            for j in range(1, n+1):
                expected_poly[k + j] += comb(n, j)
    expected_poly[m - n + 2] -= n
    expected_poly += Counter()  # Removes zero coefficients.
    assert polynomial == expected_poly, (polynomial, expected_poly)
    if n <= 5:
        all_forts = [mask for mask in range(1, 1 << length) if is_fort(mask, adj)]
        fort_lookup = set(all_forts)
        has_fort_subset = [False] * (1 << length)
        minimal = set()
        for mask in range(1, 1 << length):
            smaller_has_fort = any(has_fort_subset[mask & ~(1 << t)]
                                   for t in range(length) if mask >> t & 1)
            if mask in fort_lookup and not smaller_has_fort:
                minimal.add(mask)
            has_fort_subset[mask] = (mask in fort_lookup) or smaller_has_fort
        target = expected_minimal_forts(n, edges)
        assert minimal == target, (n, minimal - target, target - minimal)
    else:
        minimal = None
    minimum = min(polynomial)
    from math import factorial
    assert minimum == m - n + 2
    assert polynomial[minimum] == n * (n ** (n - 2) - 1)
    return {"n": n, "size": length, "minimum": minimum,
            "minimum_sets": polynomial[minimum],
            "forcing_total": sum(polynomial.values()),
            "minimal_forts": len(minimal) if minimal is not None else None,
            "polynomial": sorted(polynomial.items())}


if __name__ == '__main__':
    for n in (3, 4, 5):
        print(run(n))
    n = 6
    edges, adj = data(n)
    rng = random.Random(20261022)
    for i in range(25000):
        sample = rng.randrange(1 << len(adj))
        assert is_forcing(sample, adj) == predicted(n, edges, sample), (i, sample)
    print("n=6 random checks=25000")
    print("VERIFICATION_OK")
