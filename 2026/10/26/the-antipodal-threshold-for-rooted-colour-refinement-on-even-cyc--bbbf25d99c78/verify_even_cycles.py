"""Independent finite checks for the rooted even-torus refinement theorem.

Run with Python 3.9 or newer: python verify_even_cycles.py
Only the Python standard library is needed. These finite checks are not a proof.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb, factorial


def coordinate_histogram(x, r):
    c = [0] * (r + 1)
    for z in x:
        c[min(z, 2 * r - z)] += 1
    return tuple(c)


def predicted_key(hist, k):
    distance = sum(j * c for j, c in enumerate(hist))
    return (0, hist) if distance <= k else (1,)


def canonical_coloring(colors, neighbours):
    signatures = []
    for i, near in enumerate(neighbours):
        m = Counter()
        for j, multiplicity in near.items():
            m[colors[j]] += multiplicity
        signatures.append((colors[i], tuple(sorted(m.items()))))
    code = {a: i for i, a in enumerate(sorted(set(signatures)))}
    return [code[a] for a in signatures]


def partitions_equal(colors, other):
    fwd = {}
    back = {}
    for a, b in zip(colors, other):
        if a in fwd and fwd[a] != b:
            return False
        if b in back and back[b] != a:
            return False
        fwd[a] = b
        back[b] = a
    return True


def direct_graph_check(r, d):
    vertices = list(product(range(2 * r), repeat=d))
    names = {v: i for i, v in enumerate(vertices)}
    adj = []
    for x in vertices:
        near = defaultdict(int)
        for i in range(d):
            for delta in (-1, 1):
                y = list(x)
                y[i] = (y[i] + delta) % (2 * r)
                near[names[tuple(y)]] += 1
        adj.append(near)
    root = names[(0,) * d]
    colors = [0 if i == root else 1 for i in range(len(vertices))]
    diameter = d * r
    for k in range(diameter):
        hist = [coordinate_histogram(x, r) for x in vertices]
        if r >= 3:
            target = [predicted_key(h, k) for h in hist]
        else:
            target = [min(sum(j * c for j, c in enumerate(h)), k + 1) for h in hist]
        assert partitions_equal(colors, target), ('full', r, d, k)
        update = canonical_coloring(colors, adj)
        if k < diameter - 1:
            assert len(set(update)) > len(set(colors)), ('premature', r, d, k)
        else:
            assert len(set(update)) == len(set(colors)), ('not-stable', r, d, k)
        colors = update


def compositions(total, bins):
    if bins == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, bins - 1):
            yield (first,) + tail


def quotient_check(r, d):
    states = list(compositions(d, r + 1))
    ids = {s: i for i, s in enumerate(states)}
    nbrs = []
    for s in states:
        near = defaultdict(int)
        for j in range(r + 1):
            if s[j] == 0:
                continue
            if j > 0:
                nxt = list(s); nxt[j] -= 1; nxt[j - 1] += 1
                near[ids[tuple(nxt)]] += s[j] * (2 if j == r else 1)
            if j < r:
                nxt = list(s); nxt[j] -= 1; nxt[j + 1] += 1
                near[ids[tuple(nxt)]] += s[j] * (2 if j == 0 else 1)
        nbrs.append(near)
    root = ids[(d,) + (0,) * r]
    color = [0 if i == root else 1 for i in range(len(states))]
    diameter = r * d
    for k in range(diameter):
        if r >= 3:
            target = [predicted_key(s, k) for s in states]
        else:
            target = [min(sum(j * a for j, a in enumerate(s)), k + 1) for s in states]
        assert partitions_equal(color, target), ('quotient', r, d, k)
        if r >= 3:
            n_profiles = sum(1 for s in states if sum(j * a for j, a in enumerate(s)) <= k)
            n_expected = n_profiles + int(k < diameter)
            assert len(set(color)) == n_expected
        new = canonical_coloring(color, nbrs)
        assert len(set(new)) == len(set(color)) if k == diameter - 1 else len(set(new)) > len(set(color))
        color = new
    expected_stable = comb(d + r, r) if r >= 3 else r * d + 1
    assert len(set(color)) == expected_stable


def check_parent_injectivity(r, d):
    states = list(compositions(d, r + 1))
    signatures = {}
    for s in states:
        dist = sum(j * x for j, x in enumerate(s))
        if dist == 0:
            continue
        parents = Counter()
        for j in range(1, r + 1):
            if s[j]:
                t = list(s); t[j] -= 1; t[j - 1] += 1
                parents[tuple(t)] += s[j] * (2 if j == r else 1)
        sig = (dist, tuple(sorted(parents.items())))
        assert sig not in signatures or signatures[sig] == s, ('collision', r, d, s, signatures[sig])
        signatures[sig] = s


def main():
    full = quot = parent = 0
    for r in range(2, 7):
        for d in range(1, 4):
            if (2 * r) ** d <= 1800:
                direct_graph_check(r, d)
                full += 1
    for d in range(1, 7):
        direct_graph_check(1, d)
        full += 1
    for r in range(2, 11):
        for d in range(1, 6):
            if comb(d + r, r) <= 1500:
                quotient_check(r, d)
                quot += 1
    for r in range(3, 11):
        for d in range(1, 9):
            if comb(d + r, r) <= 8000:
                check_parent_injectivity(r, d)
                parent += 1
    print('DIRECT_FULL_GRAPH_CONFIGURATIONS:', full)
    print('INDEPENDENT_WEIGHTED_QUOTIENT_CONFIGURATIONS:', quot)
    print('PARENT_MULTISET_INJECTION_CONFIGURATIONS:', parent)
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    main()
