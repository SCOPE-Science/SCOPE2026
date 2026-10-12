from functools import lru_cache


def integer_partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for a in range(cap, 0, -1):
        for tail in integer_partitions(n-a, a):
            yield (a,) + tail


def graph(profile):
    part = []
    for i, m in enumerate(profile):
        part.extend([i] * m)
    n = len(part)
    adj = [set() for _ in range(n)]
    for u in range(n):
        for v in range(u+1, n):
            if part[u] != part[v]:
                adj[u].add(v)
                adj[v].add(u)
    return part, adj


def is_trd_direct(profile, block):
    part, adj = graph(profile)
    n = len(part)
    d = set(block)
    outside = set(range(n)) - d
    if any(not (adj[v] & d) for v in range(n)):
        return False
    if any(not ((adj[v] & outside) - {v}) for v in outside):
        return False
    return True


def is_trd_structural(profile, block):
    part, _ = graph(profile)
    n = len(part)
    d = set(block)
    support = {part[v] for v in d}
    outside = set(range(n)) - d
    outside_support = {part[v] for v in outside}
    return len(support) >= 2 and (not outside or len(outside_support) >= 2)


def set_partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for rest in set_partitions(items[1:]):
        yield (frozenset((first,)),) + rest
        for i in range(len(rest)):
            blocks = list(rest)
            blocks[i] = frozenset(set(blocks[i]) | {first})
            yield tuple(blocks)


def valid_trc_partition(profile, partition):
    for block in partition:
        if is_trd_direct(profile, block):
            return False
    for i, block in enumerate(partition):
        if not any(i != j and is_trd_direct(profile, set(block) | set(other))
                   for j, other in enumerate(partition)):
            return False
    return True


def exact_ctr(profile):
    n = sum(profile)
    best = 0
    for partition in set_partitions(range(n)):
        if len(partition) <= best:
            continue
        if valid_trc_partition(profile, partition):
            best = len(partition)
    return best


def predicted_ctr(profile):
    n = sum(profile)
    if len(profile) == 2 and min(profile) == 1 and max(profile) >= 2:
        return 2
    if len(profile) == 3 and n == 3:
        return 2
    return n


profiles = 0
subset_checks = 0
partition_checks = 0
for n in range(2, 9):
    for profile in integer_partitions(n):
        if len(profile) < 2:
            continue
        profiles += 1
        for mask in range(1 << n):
            block = {v for v in range(n) if (mask >> v) & 1}
            assert is_trd_direct(profile, block) == is_trd_structural(profile, block), (profile, block)
            subset_checks += 1
        got = exact_ctr(profile)
        expected = predicted_ctr(profile)
        assert got == expected, (profile, got, expected)
        partition_checks += 1

print(f"ALL CHECKS PASSED; profiles={profiles}; trd_subset_checks={subset_checks}; exact_partition_profiles={partition_checks}; orders=2..8")
