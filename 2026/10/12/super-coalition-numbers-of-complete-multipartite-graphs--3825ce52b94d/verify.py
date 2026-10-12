from itertools import combinations


def integer_partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for rest in integer_partitions(n - a, a):
            yield (a,) + rest


def graph_from_profile(profile):
    parts = []
    part_of = []
    for i, size in enumerate(profile):
        part = list(range(len(part_of), len(part_of) + size))
        parts.append(part)
        part_of.extend([i] * size)
    n = len(part_of)
    adj = [set() for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if u != v and part_of[u] != part_of[v]:
                adj[u].add(v)
    return parts, part_of, adj


def is_super_direct(D, adj, n):
    D = set(D)
    C = set(range(n)) - D
    for u in C:
        if not any(u in adj[v] and (adj[v] & C) == {u} for v in D):
            return False
    return True


def is_super_struct(D, profile, part_of):
    n = len(part_of)
    C = [u for u in range(n) if u not in D]
    if len(C) <= 1:
        return True
    if len(C) >= 3:
        return False
    u, v = C
    i, j = part_of[u], part_of[v]
    return i != j and profile[i] >= 2 and profile[j] >= 2


def set_partitions(n):
    blocks = []
    def rec(x):
        if x == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for i in range(len(blocks)):
            blocks[i].append(x)
            yield from rec(x + 1)
            blocks[i].pop()
        blocks.append([x])
        yield from rec(x + 1)
        blocks.pop()
    yield from rec(0)


def is_super_coalition_partition(P, adj, n):
    sets = [set(b) for b in P]
    if any(is_super_direct(S, adj, n) for S in sets):
        return False
    for i, S in enumerate(sets):
        if not any(i != j and is_super_direct(S | T, adj, n)
                   for j, T in enumerate(sets)):
            return False
    return True


def theorem(profile):
    n = sum(profile)
    if n == 2:
        return 0
    p = sum(size >= 2 for size in profile)
    return 4 if p >= 3 or tuple(profile) == (2, 2) else 3


def main():
    criterion_checks = 0
    partition_checks = 0
    profiles = 0
    for n in range(2, 9):
        for profile in integer_partitions(n):
            if len(profile) < 2:
                continue
            profiles += 1
            parts, part_of, adj = graph_from_profile(profile)
            for mask in range(1 << n):
                D = {i for i in range(n) if (mask >> i) & 1}
                criterion_checks += 1
                assert is_super_direct(D, adj, n) == is_super_struct(D, profile, part_of)
            best = 0
            for P in set_partitions(n):
                partition_checks += 1
                if is_super_coalition_partition(P, adj, n):
                    best = max(best, len(P))
            assert best == theorem(profile), (profile, best, theorem(profile))

    for profile in [(1, 2, 2, 2), (1, 2, 2, 3), (1, 3, 3, 3)]:
        parts, part_of, adj = graph_from_profile(profile)
        chosen = [parts[i][0] for i, size in enumerate(profile) if size >= 2][:3]
        core = set(range(sum(profile))) - set(chosen)
        P = [tuple(sorted(core))] + [(z,) for z in chosen]
        assert theorem(profile) == 4
        assert is_super_coalition_partition(P, adj, sum(profile))

    print(
        'ALL CHECKS PASSED; '
        f'profiles={profiles}; criterion_checks={criterion_checks}; '
        f'partition_checks={partition_checks}; orders=2..8; '
        'universal_counterexamples=3'
    )


if __name__ == '__main__':
    main()
