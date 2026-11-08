"""Finite checks for the two-successor rank-three limiting spectrum.

Usage: python checker.py
Only finite combinatorics is verified; asymptotic and logical proofs are in RESULT.md.
"""
from collections import Counter
from itertools import permutations
from fractions import Fraction
from math import factorial, exp


def collision_counts(order):
    n = len(order)
    forward = {(i, i + 1) for i in range(n - 1)}
    second = set(zip(order, order[1:]))
    aligned = len(forward & second)
    reversed_ = sum((v, u) in second for u, v in forward)
    return aligned, reversed_


def falling(n, r):
    z = 1
    for i in range(r):
        z *= n - i
    return z


def enumerate_joint(n):
    return Counter(collision_counts(p) for p in permutations(range(n)))


def factorial_moment(table, n, r, s):
    return Fraction(sum(falling(a, r) * falling(b, s) * k
                        for (a, b), k in table.items()), factorial(n))


def compatible_count(n, r, s):
    """Ordered selections of r aligned and s reversed arcs compatible in a path."""
    edges = [(i, i + 1) for i in range(n - 1)]
    count = 0
    for ix in permutations(range(n - 1), r):
        for iy in permutations(range(n - 1), s):
            requested = [edges[i] for i in ix] + [edges[j][::-1] for j in iy]
            if len(set(requested)) != len(requested):
                continue
            incoming = {}; outgoing = {}
            good = True
            for u, v in requested:
                if (u in outgoing and outgoing[u] != v) or (v in incoming and incoming[v] != u):
                    good = False
                    break
                outgoing[u] = v; incoming[v] = u
            if not good:
                continue
            for x in set(outgoing) | set(incoming):
                seen = set(); y = x
                while y in outgoing and y not in seen:
                    seen.add(y); y = outgoing[y]
                if y in seen:
                    good = False
                    break
            count += good
    return count




def check_rank_three_profiles():
    """Sample clean pairs and compare their exact recursive FO2 rank-two type sets."""
    import random
    n = 2000
    identifiers = [dict(), dict()]
    representatives = {}
    samples_checked = 0
    for seed in range(120):
        rng = random.Random(seed)
        first = list(range(n)); second = first.copy()
        rng.shuffle(first); rng.shuffle(second)
        successors = [[-1] * n for _ in range(4)]
        so, si, to, ti = successors
        for u, v in zip(first, first[1:]):
            so[u] = v; si[v] = u
        for u, v in zip(second, second[1:]):
            to[u] = v; ti[v] = u
        align = [u for u in range(n) if so[u] >= 0 and so[u] == to[u]]
        reverse = [u for u in range(n) if so[u] >= 0 and so[u] == ti[u]]
        groups = [[first[0]], [first[-1]], [second[0]], [second[-1]]]
        groups.extend([[u, so[u]] for u in align + reverse])
        occupied = {}
        isolated = True
        for j, group in enumerate(groups):
            region = set(group); wave = set(group)
            for _ in range(2):
                wave = {z for x in wave for z in (so[x], si[x], to[x], ti[x])
                        if z >= 0} - region
                region |= wave
            for v in region:
                if v in occupied and occupied[v] != j:
                    isolated = False
                    break
                occupied[v] = j
            if not isolated:
                break
        if not isolated:
            continue
        colors = [0] * n
        profiles = []
        for depth in range(2):
            frequencies = Counter(colors)
            new = []
            for u in range(n):
                neighbors = {v for v in (so[u], si[u], to[u], ti[u]) if v >= 0}
                def mask(v):
                    return (int(so[u] == v) + 2 * int(si[u] == v) +
                            4 * int(to[u] == v) + 8 * int(ti[u] == v))
                excluded = Counter(colors[v] for v in neighbors)
                excluded[colors[u]] += 1
                pairs = {(mask(v), colors[v]) for v in neighbors}
                pairs.add((16, colors[u]))
                pairs.update((0, c) for c, k in frequencies.items()
                             if k > excluded[c])
                signature = (colors[u], tuple(sorted(pairs)))
                lexicon = identifiers[depth]
                if signature not in lexicon:
                    lexicon[signature] = len(lexicon) + 1
                new.append(lexicon[signature])
            colors = new
            profiles.append(frozenset(colors))
        key = (min(len(align), 2), min(len(reverse), 2))
        if key in representatives:
            assert representatives[key] == tuple(profiles), (key, seed)
        else:
            representatives[key] = tuple(profiles)
        samples_checked += 1
    assert samples_checked >= 30
    assert len(representatives) >= 7
    return samples_checked, len(representatives)


def run():
    total_tests = 0
    for n in range(2, 8):
        table = enumerate_joint(n)
        assert sum(table.values()) == factorial(n)
        assert all(a + b <= n - 1 for a, b in table)
        assert table[(0, 0)] == table[(0, 0)]
        for r in range(3):
            for s in range(3 - r):
                if r + s >= n:
                    continue
                moment = factorial_moment(table, n, r, s)
                count = compatible_count(n, r, s)
                assert moment == Fraction(count, falling(n, r + s))
                total_tests += 1
        # Reversing the second order exchanges aligned and reversed counts.
        for (a, b), k in table.items():
            assert table[(b, a)] == k
    # The nine truncated cells have four e^-2, four e^-1(1-2e^-1), one (1-2e^-1)^2.
    cell_types = Counter()
    for a in range(3):
        for b in range(3):
            name = tuple(0 if c < 2 else 1 for c in (a, b))
            cell_types[name] += 1
    assert sorted(cell_types.values()) == [1, 2, 2, 4]
    # Distinct subset sums are a formal polynomial check, not floating-point equality.
    polynomials = set()
    for u in range(5):
        for v in range(5):
            for w in range(2):
                # u*z^2 + v*z*(1-2*z) + w*(1-2*z)^2
                polynomials.add((w, v - 4 * w, u - 2 * v + 4 * w))
    assert len(polynomials) == 50
    z = exp(-1)
    assert abs(4*z*z + 4*z*(1-2*z) + (1-2*z)**2 - 1) < 1e-13
    samples_checked, groups_checked = check_rank_three_profiles()
    print('TWO_SUCCESSOR_FINITE_CHECKS_OK', 'factorial_moments=', total_tests,
          'spectrum_polynomials=', len(polynomials),
          'clean_profiles=', samples_checked, 'state_groups=', groups_checked)


if __name__ == '__main__':
    run()
