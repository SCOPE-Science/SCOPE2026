from functools import lru_cache


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


@lru_cache(None)
def comps(n, k):
    if k == 1:
        return ((n,),)
    out = []
    for a in range(n + 1):
        for rest in comps(n - a, k - 1):
            out.append((a,) + rest)
    return tuple(out)


def feasible(parts, rows):
    k = len(rows[0])
    N = sum(parts)
    totals = [sum(row[c] for row in rows) for c in range(k)]
    for i, a in enumerate(parts):
        d = N - a
        for c in range(k):
            outside = totals[c] - rows[i][c]
            if 2 * outside > d:
                return False
    return True


def find_coloring(parts, k):
    opts = [comps(a, k) for a in parts]
    rows = [None] * len(parts)

    def rec(i):
        if i == len(parts):
            return tuple(rows) if feasible(parts, rows) else None
        for row in opts[i]:
            rows[i] = row
            z = rec(i + 1)
            if z is not None:
                return z
        return None

    return rec(0)


def is_star(parts):
    return len(parts) == 2 and parts[0] == 1


def predicted(parts):
    if is_star(parts):
        return None
    if all(a % 2 == 0 for a in parts):
        return 2
    if parts in ((1, 1, 1, 1), (1, 1, 2)):
        return 4
    return 3


def periodic_rows(parts):
    N = sum(parts)
    low = [i for i, a in enumerate(parts) if N - a < 6]
    order = list(range(len(parts)))
    if low:
        p = max(low, key=lambda i: parts[i])
        order = [i for i in order if i != p] + [p]
    rows = [None] * len(parts)
    pos = 0
    for i in order:
        cnt = [0, 0, 0]
        for _ in range(parts[i]):
            cnt[pos % 3] += 1
            pos += 1
        rows[i] = tuple(cnt)
    return tuple(rows)


small_profiles = 0
small_searches = 0
small_witnesses = 0
for N in range(2, 12):
    for parts in partitions(N):
        if len(parts) < 2:
            continue
        small_profiles += 1
        p = predicted(parts)
        if p is None:
            assert is_star(parts)
            continue
        assert find_coloring(parts, 1) is None
        small_searches += 1
        if p == 2:
            assert find_coloring(parts, 2) is not None
            small_witnesses += 1
        elif p == 3:
            assert not all(a % 2 == 0 for a in parts)
            assert find_coloring(parts, 2) is None
            assert find_coloring(parts, 3) is not None
            small_searches += 2
            small_witnesses += 1
        else:
            assert parts in ((1, 1, 1, 1), (1, 1, 2))
            assert find_coloring(parts, 2) is None
            assert find_coloring(parts, 3) is None
            assert find_coloring(parts, 4) is not None
            small_searches += 3
            small_witnesses += 1

large_profiles = 0
for N in range(12, 41):
    for parts in partitions(N):
        if len(parts) < 2 or is_star(parts):
            continue
        assert feasible(parts, periodic_rows(parts)), parts
        large_profiles += 1

two_color_checks = 0
for N in range(2, 31):
    for parts in partitions(N):
        if len(parts) < 2 or is_star(parts):
            continue
        if all(a % 2 == 0 for a in parts):
            rows = tuple((a // 2, a // 2) for a in parts)
            assert feasible(parts, rows)
        two_color_checks += 1

print(
    "ALL CHECKS PASSED; "
    f"small_profiles_N<=11={small_profiles}; "
    f"small_search_calls={small_searches}; "
    f"small_witnesses={small_witnesses}; "
    f"periodic_profiles_N=12..40={large_profiles}; "
    f"two_color_profiles_N<=30={two_color_checks}; "
    "exception_profiles=K_4,K_{2,1,1}"
)
