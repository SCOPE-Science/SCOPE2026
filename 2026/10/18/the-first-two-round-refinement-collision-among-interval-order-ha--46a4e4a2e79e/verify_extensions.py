"""Independent generation of finite interval orders by maximal extensions.

No Fishburn matrices are used. Posets are transitive out-neighborhood bitmasks.
The sorted directed degree-pair normal form is valid for interval orders:
strict lower sets and strict upper sets are each nested, so equal pairs
identify elements with identical predecessor and successor sets.
"""
from collections import Counter, defaultdict


def add_maximal(poset):
    n = len(poset)
    for subset in range(1 << n):
        if any((subset >> upper & 1) and any(
            (poset[lower] >> upper & 1) and not (subset >> lower & 1)
            for lower in range(n)) for upper in range(n)):
            continue
        enlarged = [out | ((subset >> i & 1) << n)
                    for i, out in enumerate(poset)]
        enlarged.append(0)
        yield tuple(enlarged)


def interval_order(poset):
    n = len(poset)
    lowers = [sum(1 << i for i in range(n) if poset[i] >> j & 1)
              for j in range(n)]
    return all((a & b) in (a, b) for a in lowers for b in lowers)


def normal_form(poset):
    n = len(poset)
    degrees = [(sum(poset[i] >> j & 1 for i in range(n)),
                poset[j].bit_count()) for j in range(n)]
    permutation = sorted(range(n), key=lambda i: degrees[i])
    return tuple(sum(1 << k for k, v in enumerate(permutation)
                     if poset[u] >> v & 1) for u in permutation)


def hasse(poset):
    n = len(poset)
    return tuple(tuple(bool(poset[i] >> j & 1) and not any(
        (poset[i] >> k & 1) and (poset[k] >> j & 1) for k in range(n))
        for j in range(n)) for i in range(n))


def two_round_signature(edges):
    n = len(edges)
    first = [(sum(edges[j][i] for j in range(n)), sum(edges[i]))
             for i in range(n)]
    second = []
    for i in range(n):
        down = tuple(sorted(Counter(first[j] for j in range(n)
                                   if edges[j][i]).items()))
        up = tuple(sorted(Counter(first[j] for j in range(n)
                                 if edges[i][j]).items()))
        second.append((first[i], down, up))
    return tuple(sorted(Counter(second).items()))


def main():
    current = {(): ()}
    expected = (1, 2, 5, 15, 53, 217, 1014, 5335)
    for n in range(1, 9):
        distinct = {}
        for poset in current.values():
            for enlarged in add_maximal(poset):
                if interval_order(enlarged):
                    canonical = normal_form(enlarged)
                    distinct[canonical] = canonical
        assert len(distinct) == expected[n - 1]
        current = distinct
        profiles = defaultdict(int)
        for p in current.values():
            profiles[two_round_signature(hasse(p))] += 1
        collisions = sum(v * (v - 1) // 2 for v in profiles.values())
        print(f'n={n} extension_types={len(current)} '
              f'round2_classes={len(profiles)} collision_pairs={collisions}')
        assert collisions == (2 if n == 8 else 0)
    print('MAXIMAL_EXTENSION_INDEPENDENT_OK')


if __name__ == '__main__':
    main()
