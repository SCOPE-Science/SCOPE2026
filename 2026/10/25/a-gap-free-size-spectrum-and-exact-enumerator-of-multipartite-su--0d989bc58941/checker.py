"""Reproduce exact counts for maximal FD+ID repairs of multipartite data.

Requires Python 3.10+ standard library only. This checks finite instances;
the general theorem follows from the proof in RESULT.md.
"""
import itertools
import math
from collections import Counter


def rook_count(profile):
    n = sum(profile)
    total = 0
    for js in itertools.product(*(range(s + 1) for s in profile)):
        k = sum(js)
        term = math.factorial(n - k)
        for s, j in zip(profile, js):
            term *= math.comb(s, j) ** 2 * math.factorial(j)
        total += (-1) ** k * term
    return total


def perm_count_direct(profile):
    colors = sum(([i] * s for i, s in enumerate(profile)), [])
    n = len(colors)
    return sum(all(colors[j] != colors[p[j]] for j in range(n))
               for p in itertools.permutations(range(n)))


def polynomial(profile):
    n = sum(profile)
    result = Counter({n: rook_count(profile)})
    for i, a in enumerate(profile):
        for removed in range(1, a + 1):
            p = list(profile)
            p[i] -= removed
            result[n - removed] += math.comb(a, removed) * rook_count(p)
    return +result


def spectrum(profile):
    a = sorted(profile, reverse=True)
    n = sum(a)
    outside = n - a[0]
    return set(range(max(outside, 2 * a[1]),
                     min(n, 2 * outside) + 1))


def repairs_direct(profile):
    # Independently enumerate ALL subrelations on small instances.
    colors = sum(([i] * s for i, s in enumerate(profile)), [])
    n = len(colors)
    edges = [(u, v) for u in range(n) for v in range(n)
             if colors[u] != colors[v]]
    feasible = []
    for mask in range(1 << len(edges)):
        chosen = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        tails = [u for u, _ in chosen]
        if len(set(tails)) != len(tails):
            continue  # FD
        if not set(tails).issubset({v for _, v in chosen}):
            continue  # ID
        feasible.append(mask)
    # Exact inclusion-maximality, no use of the claimed missing-parts criterion.
    result = Counter()
    for m in feasible:
        if not any(m != h and (m & h) == m for h in feasible):
            result[m.bit_count()] += 1
    return +result


def repairs_functional(profile):
    # Independently enumerate assignments with at most one outgoing edge.
    colors = sum(([i] * s for i, s in enumerate(profile)), [])
    n = len(colors)
    choices = [(None,) + tuple(v for v in range(n)
                                 if colors[v] != colors[u])
               for u in range(n)]
    tally = Counter()
    for outputs in itertools.product(*choices):
        tails = [u for u, v in enumerate(outputs) if v is not None]
        heads = {v for v in outputs if v is not None}
        if not set(tails).issubset(heads):
            continue
        remaining = {colors[u] for u, v in enumerate(outputs) if v is None}
        if len(remaining) <= 1:
            tally[len(tails)] += 1
    return +tally


def partitions(n, lo=1):
    if n == 0:
        yield ()
    for a in range(lo, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def main():
    cases = 0
    count_check = 0
    direct_relations = 0
    functional_relations = 0
    for n in range(2, 8):
        for profile in partitions(n):
            if len(profile) < 2:
                continue
            p = polynomial(profile)
            assert set(p) == spectrum(profile), (profile, p, spectrum(profile))
            # Independent brute enumeration of forbidden-position permutations
            # on every support occupancy of moderate size.
            for ss in itertools.product(*(range(a + 1) for a in profile)):
                if sum(ss) <= 6:
                    assert rook_count(ss) == perm_count_direct(ss), (profile, ss)
                    count_check += 1
            if n <= 4:
                q = repairs_direct(profile)
                assert p == q, (profile, p, q)
                direct_relations += 1
            choices = math.prod(1 + n - a for a in profile for _ in range(a))
            if choices <= 500000:
                q = repairs_functional(profile)
                assert p == q, (profile, p, q)
                functional_relations += 1
            cases += 1
    assert polynomial((2, 1, 1)) == {2: 1, 3: 4, 4: 4}
    assert polynomial((3, 2, 2)) == {4: 4, 5: 48, 6: 384, 7: 288}
    assert polynomial((5, 2)) == {4: 40}
    print('ALL_CHECKS_OK')
    print('multipartite_profiles=', cases)
    print('forbidden_permutation_subprofiles=', count_check)
    print('independent_powerset_repair_checks=', direct_relations)
    print('independent_function_assignment_checks=', functional_relations)
    print('example_(3,2,2)=', sorted(polynomial((3, 2, 2)).items()))


if __name__ == '__main__':
    main()
