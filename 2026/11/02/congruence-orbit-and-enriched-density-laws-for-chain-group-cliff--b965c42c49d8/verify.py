"""Reproducible checks for enriched congruence counts on chain-group monoids.

Only standard-library arithmetic is used. Brute-force equivalence partitions
are independent of the normal-subgroup-chain classification.
"""
from itertools import product, permutations
from math import comb, prod


def additive_group(p, d):
    n = p ** d
    vec = [[(x // (p ** i)) % p for i in range(d)] for x in range(n)]
    plus = [[sum(((vec[x][i] + vec[y][i]) % p) * p ** i
                  for i in range(d)) for y in range(n)] for x in range(n)]
    return plus


def subspaces(p, d):
    plus = additive_group(p, d)
    n = p ** d
    groups = {frozenset([0])}
    for _ in range(d):
        extended = set(groups)
        for U in groups:
            for v in range(n):
                if v not in U:
                    multiples = [0]
                    for t in range(1, p):
                        multiples.append(plus[multiples[-1]][v])
                    extended.add(frozenset(plus[u][v0]
                                           for u in U for v0 in multiples))
        if groups == extended:
            break
        groups = extended
    return groups, plus


def equivalence_partitions(n):
    block = [0] * n
    def generate(i, upper):
        if i == n:
            yield tuple(block)
        else:
            for j in range(upper + 2):
                block[i] = j
                yield from generate(i + 1, max(upper, j))
    yield from generate(1, 0)


def exhaustive_case(p, d, m):
    subs, plus = subspaces(p, d)
    gsize = p ** d
    n = m * gsize
    mul = [[min(a // gsize, b // gsize) * gsize + plus[a % gsize][b % gsize]
            for b in range(n)] for a in range(n)]
    maximal = [(m - 1) * gsize + a % gsize for a in range(n)]
    all_count = f_count = 0
    ordinary_parts = []
    enriched_parts = []
    for partition in equivalence_partitions(n):
        classes = {}
        for a, label in enumerate(partition):
            classes.setdefault(label, []).append(a)
        compatible = True
        for block in classes.values():
            a = block[0]
            for b in block[1:]:
                for c in range(n):
                    if (partition[mul[a][c]] != partition[mul[b][c]]
                        or partition[mul[c][a]] != partition[mul[c][b]]):
                        compatible = False
                        break
                if not compatible:
                    break
            if not compatible:
                break
        if not compatible:
            continue
        all_count += 1
        ordinary_parts.append(partition)
        if all(partition[maximal[block[0]]] == partition[maximal[b]]
               for block in classes.values() for b in block[1:]):
            f_count += 1
            enriched_parts.append(partition)

    weak_flags = []
    chains = [tuple([U]) for U in subs]
    for b in range(1, m + 1):
        weak_flags.append(len(chains))
        chains = [chain + (U,) for chain in chains for U in subs
                  if U <= chain[-1]]
    expected_total = sum(comb(m - 1, b - 1) * weak_flags[b - 1]
                         for b in range(1, m + 1))
    expected_f = 2 ** (m - 1) * len(subs)
    assert (all_count, f_count) == (expected_total, expected_f)
    def canonical(labels):
        new = {}
        return tuple(new.setdefault(v, len(new)) for v in labels)

    if n <= 9:
        automorphisms = []
        for nonzero in permutations(range(1, gsize)):
            f = (0,) + nonzero
            if all(f[plus[x][y]] == plus[f[x]][f[y]]
                   for x in range(gsize) for y in range(gsize)):
                automorphisms.append(f)

        def orbit_count(parts):
            minima = set()
            for labels in parts:
                orbit = []
                for f in automorphisms:
                    image = [0] * n
                    for x in range(n):
                        y = (x // gsize) * gsize + f[x % gsize]
                        image[y] = labels[x]
                    orbit.append(canonical(image))
                minima.add(min(orbit))
            return len(minima)

        o_all = orbit_count(ordinary_parts)
        o_f = orbit_count(enriched_parts)
        expected_o_all = sum(comb(m - 1, b - 1) * comb(d + b, b)
                             for b in range(1, m + 1))
        expected_o_f = 2 ** (m - 1) * (d + 1)
        assert (o_all, o_f) == (expected_o_all, expected_o_f)
        print(f"EXHAUSTIVE p={p} d={d} levels={m}: "
              f"all={all_count}, F={f_count}, orbits={o_all}, F_orbits={o_f}, "
              f"flags={weak_flags}")
    else:
        print(f"EXHAUSTIVE p={p} d={d} levels={m}: "
              f"all={all_count}, F={f_count}, flags={weak_flags}")


def gaussian(n, k, p):
    if not (0 <= k <= n):
        return 0
    k = min(k, n - k)
    return prod(p ** (n - i) - 1 for i in range(k)) // prod(
        p ** (i + 1) - 1 for i in range(k))


def flag_numbers(p, max_d, max_b):
    previous = [1] * (max_d + 1)
    arrays = [previous]
    for _ in range(max_b):
        previous = [sum(gaussian(n, k, p) * previous[k]
                        for k in range(n + 1)) for n in range(max_d + 1)]
        arrays.append(previous)
    return arrays


def theta(p, k, s, bound=10):
    acc = 0.0
    for xs in product(range(-bound, bound + 1), repeat=k - 1):
        tail = s - sum(xs)
        if abs(tail) > bound:
            continue
        acc += p ** (-0.5 * (sum(x * x for x in xs) + tail * tail - s * s / k))
    return acc


def asymptotic_sample(p, m, d):
    flags = flag_numbers(p, d, m)
    f = 2 ** (m - 1) * flags[1][d]
    total = sum(comb(m - 1, b - 1) * flags[b][d]
                for b in range(1, m + 1))
    phi = prod(1 - p ** (-j) for j in range(1, 120))
    predicted = (2 ** (m - 1) * phi ** (m - 1)
                 * theta(p, 2, d % 2)
                 / theta(p, m + 1, d % (m + 1)))
    scaled = (f / total) * p ** ((m - 1) * d * d / (4 * (m + 1)))
    rel = abs(scaled / predicted - 1)
    print(f"ASYMPTOTIC_SAMPLE p={p} levels={m} d={d}: "
          f"scaled={scaled:.9g}, theta_constant={predicted:.9g}, "
          f"relative_error={rel:.6g}")
    assert rel < 0.15


if __name__ == '__main__':
    for parms in [(2, 1, 2), (2, 1, 3), (2, 2, 2),
                  (3, 1, 2), (3, 1, 3), (5, 1, 2)]:
        exhaustive_case(*parms)
    for parms in [(2, 2, 14), (2, 3, 24), (3, 2, 14)]:
        asymptotic_sample(*parms)
    print('VERIFY_OK')
