"""Independent finite checks for friendship-graph consolidation.

No external packages. Run: python verify_friendship.py
Finite checks corroborate, but do not replace, the all-parameter proof.
"""
from itertools import combinations


def delta(a, b):
    if a < 0 or b < 0:
        raise ValueError("nonnegative pebble counts required")
    return int((a % 2 == 1 and b == 0) or
               (b % 2 == 1 and a == 0) or
               (a == 1 and b == 1))


def f(a, b):
    return a // 2 + b // 2 - delta(a, b)


def reserve(c):
    return c[0] + sum(f(c[2*i+1], c[2*i+2]) for i in range((len(c)-1)//2))


def configurations(t, n):
    for bars in combinations(range(t + n - 1), n - 1):
        prev = -1
        vals = []
        for z in bars:
            vals.append(z - prev - 1)
            prev = z
        vals.append(t + n - 2 - prev)
        yield tuple(vals)


def edges(k):
    n = 2*k+1
    out = [[] for _ in range(n)]
    for j in range(k):
        a, b = 2*j+1, 2*j+2
        for u, v in ((0, a), (0, b), (a, b)):
            out[u].append(v)
            out[v].append(u)
    return out


def exhaust(k):
    n, adj = 2*k + 1, edges(k)
    bad_hub = set()
    bad_any = set()
    n_checked = 0
    worst = []
    for t in range(1, 4*k+1):
        next_hub, next_any = set(), set()
        for c in configurations(t, n):
            n_checked += 1
            is_hub = sum(c[1:]) == 0
            is_any = sum(v > 0 for v in c) <= 1
            hub_possible = is_hub
            any_possible = is_any
            for u in range(n):
                if c[u] < 2:
                    continue
                for v in adj[u]:
                    child = list(c)
                    child[u] -= 2
                    child[v] += 1
                    child = tuple(child)
                    if child not in bad_hub:
                        hub_possible = True
                    if child not in bad_any:
                        any_possible = True
                if hub_possible and any_possible:
                    break
            actual_hub = reserve(c) >= 1
            actual_any = actual_hub or is_any
            assert actual_hub == hub_possible, (k, c, 'hub', actual_hub, hub_possible)
            assert actual_any == any_possible, (k, c, 'any', actual_any, any_possible)
            if not hub_possible:
                next_hub.add(c)
            if not any_possible:
                next_any.add(c)
        bad_hub, bad_any = next_hub, next_any
        worst.append((t, len(bad_hub), len(bad_any)))
    assert not bad_hub and not bad_any
    if k == 1:
        witness = (1, 1, 1)
    else:
        witness = (0, 2*k+1, 0) + (1, 1)*(k-1)
    assert sum(witness) == 4*k-1 and reserve(witness) == 0
    assert sum(v > 0 for v in witness) > 1
    print('k=%s, graphs_vertices=%s, checked_configs=%s, final_bad_hub=%s, final_bad_any=%s, witness=%s'
          % (k, n, n_checked, len(bad_hub), len(bad_any), witness))
    return n_checked


def check_local_inequalities():
    tested = 0
    for a in range(0, 61):
        for b in range(0, 61):
            s = f(a, b)
            assert 2*s >= a+b-4
            assert (2*s == a+b-4) == (a == 1 and b == 1)
            if a >= 2:
                assert f(a-2, b) + 1 <= s
                assert f(a-2, b+1) <= s
            assert f(a+1, b) <= s + 2
            tested += 1
    print('local inequalities tested on %d ordered pebble pairs' % tested)


if __name__ == '__main__':
    check_local_inequalities()
    total = 0
    for k in (1, 2, 3, 4):
        total += exhaust(k)
    print('PASS: %s graph configurations checked by independent exhaustive dynamic programming' % total)
