#!/usr/bin/env python3
from itertools import combinations, product

def integer_partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for first in range(minimum, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest

def condition_P(parts):
    N = sum(parts)
    r = len(parts)
    if N < 4:
        return False
    for k in range(1, r):
        for I in combinations(range(r), k):
            if sum(parts[i] for i in I) == 3:
                return True
    return False

def theorem_value(parts):
    r = len(parts)
    if condition_P(parts):
        return 3
    if r >= 4 or (r == 3 and 2 in parts):
        return 4
    if r == 3 and 2 not in parts and sum(x == 1 for x in parts) <= 1:
        return 5
    if r == 2 and min(parts) >= 4:
        return 6
    return None

def occupancy_value(parts):
    N = sum(parts)
    best = None
    for d in product(*[range(n + 1) for n in parts]):
        s = sum(d)
        if s == N:
            continue
        incomplete = [i for i, n in enumerate(parts) if d[i] < n]
        if not incomplete:
            continue
        neighbor_counts = [s - d[i] for i in incomplete]
        if min(neighbor_counts) >= 3 and 3 in neighbor_counts:
            best = s if best is None else min(best, s)
    return best

def direct_value(parts):
    part_of = []
    for i, n in enumerate(parts):
        part_of.extend([i] * n)
    N = len(part_of)
    adj = []
    for v in range(N):
        mask = 0
        for w in range(N):
            if v != w and part_of[v] != part_of[w]:
                mask |= 1 << w
        adj.append(mask)
    best = None
    full = (1 << N) - 1
    for D in range(full):
        s = D.bit_count()
        if best is not None and s >= best:
            continue
        ok = True
        exact = False
        outside = full ^ D
        x = outside
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            c = (adj[v] & D).bit_count()
            if c < 3:
                ok = False
                break
            if c == 3:
                exact = True
            x -= bit
        if ok and exact:
            best = s
    return best

def main():
    profile_count = 0
    occupancy_vectors = 0
    by_value = {None: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for N in range(2, 21):
        for parts in integer_partitions(N):
            if len(parts) < 2:
                continue
            profile_count += 1
            occupancy_vectors += 1
            got = occupancy_value(parts)
            want = theorem_value(parts)
            assert got == want, (parts, got, want)
            by_value[got] += 1

    direct_profiles = 0
    for N in range(2, 10):
        for parts in integer_partitions(N):
            if len(parts) < 2:
                continue
            direct_profiles += 1
            got = direct_value(parts)
            want = theorem_value(parts)
            assert got == want, ('direct', parts, got, want)

    bipartite_checks = 0
    for n in range(3, 31):
        assert theorem_value((3, n)) == 3
        bipartite_checks += 1
    for m in range(4, 16):
        for n in range(m, 31):
            assert theorem_value((m, n)) == 6
            bipartite_checks += 1

    # Boundary checks omitted by the published biclique regimes.
    assert theorem_value((1, 3)) == 3
    assert theorem_value((2, 3)) == 3
    assert theorem_value((1, 4)) is None
    assert theorem_value((2, 4)) is None

    print('ALL CHECKS PASSED')
    print(f'occupancy_profiles_N<=20={profile_count}')
    print(f'direct_labeled_profiles_N<=9={direct_profiles}')
    print(f'published_bipartite_specialization_checks={bipartite_checks}')
    print('value_profile_counts_N<=20=' + repr(by_value))

if __name__ == '__main__':
    main()
