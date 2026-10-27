"""Independent finite checks for path blocking-pair dynamics.

Run: python verify.py
All enumeration uses exact integers. The theorem for arbitrary n has a
separate combinatorial proof; these calculations are finite consistency tests.
"""
from functools import lru_cache
from itertools import product


def matchings(n):
    result = []
    for mask in range(1 << (n - 1)):
        if mask & (mask << 1):
            continue
        partner = list(range(n))
        for j in range(n - 1):
            if mask & (1 << j):
                partner[j], partner[j + 1] = j + 1, j
        result.append((tuple(partner), mask))
    return result


def rank(v, other, pref, n):
    if v == other:
        return 3
    if v in (0, n - 1):
        return 1
    preferred = (v + 1) if pref[v - 1] else (v - 1)
    return 1 if other == preferred else 2


def legal_move(partner, j, pref, n):
    left, right = j, j + 1
    return (partner[left] != right
            and rank(left, right, pref, n) < rank(left, partner[left], pref, n)
            and rank(right, left, pref, n) < rank(right, partner[right], pref, n))


def advance(partner, j):
    p = list(partner)
    left, right = j, j + 1
    old_left, old_right = p[left], p[right]
    p[left], p[right] = right, left
    if old_left != left:
        p[old_left] = old_left
    if old_right != right:
        p[old_right] = old_right
    return tuple(p)


def edge_weights(n, pref):
    # For each interior agent, orient its less-liked incident edge
    # toward its more-liked incident edge.
    incoming = [[] for _ in range(n - 1)]
    for v in range(1, n - 1):
        left, right = v - 1, v
        if pref[v - 1] == 0:  # v prefers left neighbor
            incoming[left].append(right)
        else:
            incoming[right].append(left)

    @lru_cache(None)
    def weight(e):
        return 1 + sum(weight(f) for f in incoming[e])

    return [weight(e) for e in range(n - 1)]


def potential(mask, weights):
    return sum(w for j, w in enumerate(weights) if mask & (1 << j))


def verify_enumeration():
    for n in range(2, 12):
        states = matchings(n)
        ids = {p: i for i, (p, _) in enumerate(states)}
        best = 0
        profiles = 0
        for pref in product((0, 1), repeat=n - 2):
            profiles += 1
            w = edge_weights(n, pref)
            values = [potential(mask, w) for _, mask in states]
            assert max(values) <= n * n // 4
            links = [[] for _ in states]
            for a, (p, _) in enumerate(states):
                for j in range(n - 1):
                    if legal_move(p, j, pref, n):
                        b = ids[advance(p, j)]
                        assert values[b] > values[a]
                        links[a].append(b)

            @lru_cache(None)
            def longest(a):
                return 0 if not links[a] else 1 + max(longest(b) for b in links[a])

            best = max(best, *(longest(a) for a in range(len(states))))
        assert best == n * n // 4, (n, best)
        print(f'n={n}; preference profiles={profiles}; matchings={len(states)}; '
              f'longest chain={best}; bound={n * n // 4}')


def verify_sharp_construction():
    for n in range(2, 81):
        pref = (0,) * (n - 2)   # each interior agent prefers its left neighbor
        p = tuple(range(n))
        count = 0
        for stop in range(0, n - 1, 2):
            for j in range(n - 2, stop - 1, -1):
                assert legal_move(p, j, pref, n), (n, stop, j, p)
                p = advance(p, j)
                count += 1
        assert count == n * n // 4, (n, count)
        assert not any(legal_move(p, j, pref, n) for j in range(n - 1))
    print('sharp construction checked for 2 <= n <= 80')


if __name__ == '__main__':
    verify_enumeration()
    verify_sharp_construction()
    print('ALL CHECKS PASSED')
