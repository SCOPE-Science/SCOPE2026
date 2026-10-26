"""Direct-definition finite checks of a super-coalition partition enumerator.

The checker uses the neighborhood definition of super domination and enumerates
ordinary set partitions, without assuming either the auxiliary-pair formula or
an upper bound on the number of blocks.
"""
from collections import Counter
from itertools import combinations
from math import comb
from random import Random


def integer_partitions(n, least=1):
    if n == 0:
        yield ()
        return
    for a in range(least, n + 1):
        for tail in integer_partitions(n - a, a):
            yield (a,) + tail


def multipartite(sizes):
    kind = [i for i, part in enumerate(sizes) for _ in range(part)]
    return [sum(1 << j for j in range(len(kind)) if kind[i] != kind[j])
            for i in range(len(kind))]


def super_flags(neighbors):
    n = len(neighbors)
    all_v = (1 << n) - 1
    result = [False] * (all_v + 1)
    for chosen in range(all_v + 1):
        omitted = all_v ^ chosen
        valid = True
        remains = omitted
        while remains:
            target = remains & -remains
            if not any((chosen >> j) & 1 and (adj & omitted) == target
                       for j, adj in enumerate(neighbors)):
                valid = False
                break
            remains -= target
        result[chosen] = valid
    return result


def direct_profile(neighbors, is_super):
    n = len(neighbors)
    profile = Counter()

    def visit(v, blocks):
        if v == n:
            if len(blocks) < 2 or any(is_super[b] for b in blocks):
                return
            for i, block in enumerate(blocks):
                if not any(is_super[block | other] for j, other in enumerate(blocks)
                           if i != j):
                    return
            profile[len(blocks)] += 1
            return
        for j in range(len(blocks)):
            blocks[j] |= 1 << v
            visit(v + 1, blocks)
            blocks[j] ^= 1 << v
        blocks.append(1 << v)
        visit(v + 1, blocks)
        blocks.pop()

    visit(1, [1])
    return dict(profile)


def predicted_profile(neighbors, is_super):
    n = len(neighbors)
    full = (1 << n) - 1
    edges = {(i, j) for i in range(n) for j in range(i + 1, n)
             if is_super[full ^ (1 << i) ^ (1 << j)]}
    e = len(edges)
    matching2 = sum(1 for x, y in combinations(edges, 2)
                    if set(x).isdisjoint(y))
    triangles = sum(1 for i, j, k in combinations(range(n), 3)
                    if (i, j) in edges and (i, k) in edges and (j, k) in edges)
    out = {2: 2 ** (n - 1) - 1 - n - e,
           3: comb(n, 2) + (n - 3) * e + matching2,
           4: triangles}
    return {k: count for k, count in out.items() if count}


def confirm(neighbors):
    n = len(neighbors)
    flags = super_flags(neighbors)
    full = (1 << n) - 1
    assert all(adj for adj in neighbors), 'isolated vertex'
    # Verify the hypothesis directly; it is not derived from the test graph type.
    assert not any(flags[s] and (full ^ s).bit_count() >= 3
                   for s in range(1 << n)), 'domination deficiency exceeded two'
    a = direct_profile(neighbors, flags)
    b = predicted_profile(neighbors, flags)
    assert a == b, (a, b)
    return a


def random_graph(n, rng, probability):
    adj = [0] * n
    for i, j in combinations(range(n), 2):
        if rng.random() < probability:
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    return adj


def main():
    number = 0
    for n in (7, 8, 9):
        cases = 0
        for profile in integer_partitions(n):
            if len(profile) < 2:
                continue
            confirm(multipartite(profile))
            cases += 1
        print('ALL_MULTIPARTITE_ORDER_%d: %d profiles PASS' % (n, cases))
        number += cases
    for profile in [(2, 2, 2, 2, 2), (3, 3, 4), (2, 2, 2, 4),
                    (5, 5), (1,) * 10]:
        result = confirm(multipartite(profile))
        print('ORDER_10_PROFILE: %s -> %s PASS' % (profile, result))
        number += 1
    # Boundary control: the order-six profile is deliberately excluded.
    small = direct_profile(multipartite((3, 3)), super_flags(multipartite((3, 3))))
    assert small == {2: 16, 3: 48}, small
    print("BOUNDARY_K_3_3_ORDER_6: %s PASS" % small)
    rng = Random(7112026)
    random_count = 0
    for n in (7, 8):
        for _ in range(250):
            neigh = random_graph(n, rng, rng.choice((0.15, 0.35, 0.65, 0.85)))
            if min(neigh) == 0:
                continue
            flags = super_flags(neigh)
            full = (1 << n) - 1
            if any(flags[s] and (full ^ s).bit_count() >= 3
                   for s in range(1 << n)):
                continue
            confirm(neigh)
            random_count += 1
    print('QUALIFYING_RANDOM_GRAPHS: %d PASS' % random_count)
    print('VERIFY_OK: %d structured graph cases, %d qualifying random cases' %
          (number, random_count))


if __name__ == '__main__':
    main()
