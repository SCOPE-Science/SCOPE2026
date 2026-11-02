"""Independent exhaustive small-instance check of friendship-graph pebbling thresholds.

Python 3 standard library only. A move replaces two pebbles at one vertex
with one at an adjacent vertex. This verifier uses the original move rule,
not the theorem's triangular-block argument.
"""
from functools import lru_cache


def configurations(total, n):
    if n == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in configurations(total - first, n - 1):
            yield (first,) + tail


def neighbors(m):
    n = 2*m + 1
    a = [set() for _ in range(n)]
    for j in range(m):
        x, y = 2*j+1, 2*j+2
        for u, v in ((0, x), (0, y), (x, y)):
            a[u].add(v)
            a[v].add(u)
    return tuple(tuple(sorted(row)) for row in a)


def make_checker(m):
    adj = neighbors(m)
    @lru_cache(maxsize=None)
    def can(config, goal):
        if goal == 'stack' and sum(z != 0 for z in config) == 1:
            return True
        if goal == 'clear' and sum(config) == 1:
            return True
        for u, z in enumerate(config):
            if z >= 2:
                for v in adj[u]:
                    nxt = list(config)
                    nxt[u] -= 2
                    nxt[v] += 1
                    if can(tuple(nxt), goal):
                        return True
        return False
    return can


def exceptional(m):
    configs = set()
    for special in range(m):
        for special_leaf in (0, 1):
            c = [0] + [1] * (2*m)
            c[2*special + 1 + special_leaf] = 2*m+1
            c[2*special + 2 - special_leaf] = 0
            configs.add(tuple(c))
    return configs


def exhaustive(m):
    checker = make_checker(m)
    bad_stack = set()
    bad_clear = set()
    for c in configurations(4*m-1, 2*m+1):
        if not checker(c, 'stack'):
            bad_stack.add(c)
        if not checker(c, 'clear'):
            bad_clear.add(c)
    if m >= 2:
        assert bad_stack == exceptional(m), (m, 'stack', len(bad_stack))
        assert bad_clear == exceptional(m), (m, 'clear', len(bad_clear))
    else:
        assert len(bad_stack) == 1 and len(bad_clear) == 4
    print('CRITICAL_CONFIGURATIONS_OK', m, len(bad_stack), len(bad_clear), flush=True)
    if m <= 3:
        num = 0
        for c in configurations(4*m, 2*m+1):
            num += 1
            assert checker(c, 'stack')
            assert checker(c, 'clear')
        print('FULL_THRESHOLD_EXHAUSTIVE_OK', m, num, flush=True)
    print('CACHED_REACHABILITY_STATES', m, checker.cache_info().currsize, flush=True)


def test_other_obstructions(m):
    checker = make_checker(m)
    for k in range(m):
        c = [0] + [0] * (2*m)
        c[1] = 2*m+1
        for j in range(1, m):
            c[2*j+1] = 1
        for j in range(1, k+1):
            c[2*j+2] = 1
        assert sum(c) == 3*m+k
        assert not checker(tuple(c), 'stack')
    print('LOWER_BOUND_FAMILY_OK', m, m, flush=True)


if __name__ == '__main__':
    for m in (1, 2, 3, 4):
        exhaustive(m)
    for m in (2, 3, 4):
        test_other_obstructions(m)
    print('VERIFY_OK')
