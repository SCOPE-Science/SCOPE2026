from functools import lru_cache


def set_partitions(items):
    if not items:
        yield []
        return
    x = items[0]
    for rest in set_partitions(items[1:]):
        yield [{x}] + [set(b) for b in rest]
        for i in range(len(rest)):
            new = [set(b) for b in rest]
            new[i].add(x)
            yield new


def integer_partitions(n, lo=1):
    if n == 0:
        yield []
        return
    for a in range(lo, n + 1):
        for tail in integer_partitions(n - a, a):
            yield [a] + tail


def fair_coalition_number(part_sizes):
    labels = []
    for i, n in enumerate(part_sizes):
        labels.extend([i] * n)
    N = len(labels)
    V = set(range(N))

    @lru_cache(None)
    def one_fair(frozen):
        S = set(frozen)
        for v in V - S:
            p = labels[v]
            neighbours = sum(labels[u] != p for u in S)
            if neighbours != 1:
                return False
        return True

    def fd(S):
        return one_fair(frozenset(S))

    best = None
    for P in set_partitions(list(V)):
        valid = True
        for i, A in enumerate(P):
            if len(A) == 1 and fd(A):
                continue
            if fd(A):
                valid = False
                break
            if not any(j != i and (not fd(B)) and fd(A | B)
                       for j, B in enumerate(P)):
                valid = False
                break
        if valid:
            best = max(best or 0, len(P))
    return best


def predicted(part_sizes):
    N = sum(part_sizes)
    r = len(part_sizes)
    if all(n == 1 for n in part_sizes):
        return N
    if r == 2 and min(part_sizes) == 1:
        return None
    if r == 2:
        return N
    return 2

profiles = 0
partition_profiles = 0
for N in range(2, 8):
    for p in integer_partitions(N):
        if len(p) < 2:
            continue
        profiles += 1
        got = fair_coalition_number(tuple(p))
        want = predicted(p)
        if got != want:
            raise AssertionError((p, got, want))
        partition_profiles += 1

print(f"profiles={profiles}; exhaustive_partition_profiles={partition_profiles}; orders=2..7")
print("ALL CHECKS PASSED")
