"""Exact, self-contained checks for signed burning on one-negative-edge bicliques.

No probabilistic sampling is used. The underlying graph dynamics are enumerated
independently of the closed-form reachable-code construction.
"""
from functools import lru_cache
from collections import Counter


def reachable(a, b, switch=0):
    n = a + b
    nbr = [[] for _ in range(n)]
    for u in range(a):
        for v in range(a, n):
            sign = -1 if (u == 0 and v == a) else 1
            if (switch >> u) & 1 != (switch >> v) & 1:
                sign = -sign
            nbr[u].append((v, sign))
            nbr[v].append((u, sign))

    @lru_cache(None)
    def outcomes(state):
        if all(state):
            return frozenset({sum((x == -1) << i for i, x in enumerate(state))})
        changed = list(state)
        for v, old in enumerate(state):
            if old == 0:
                pressure = sum(sign * state[u] for u, sign in nbr[v])
                changed[v] = (pressure > 0) - (pressure < 0)
        if all(changed):
            return frozenset({sum((x == -1) << i for i, x in enumerate(changed))})
        out = set()
        for v, old in enumerate(changed):
            if old == 0:
                for color in (-1, 1):
                    next_state = changed.copy()
                    next_state[v] = color
                    out.update(outcomes(tuple(next_state)))
        return frozenset(out)

    out = set()
    for v in range(n):
        for color in (-1, 1):
            initial = [0] * n
            initial[v] = color
            out.update(outcomes(tuple(initial)))
    return frozenset(out)


def predicted(a, b):
    n = a + b
    top = (1 << n) - 1
    base = {0} | {1 << v for v in range(n)}
    base.update((1 << a) | (1 << u) for u in range(1, a))
    base.update(1 | (1 << v) for v in range(a + 1, n))
    return frozenset(base | {top ^ mask for mask in base})


def edges_H(a, b):
    return ([(0, v) for v in range(a + 1, a + b)]
            + [(a, u) for u in range(1, a)])


def predicted_distance(a, b, mask):
    n = a + b
    k = mask.bit_count()
    if k in (0, n):
        return 0
    h = edges_H(a, b)
    has_edge = any((mask >> u) & 1 and (mask >> v) & 1 for u, v in h)
    lacks_edge = any(not ((mask >> u) & 1) and not ((mask >> v) & 1)
                     for u, v in h)
    return min(k - 1 - int(has_edge), n - k - 1 - int(lacks_edge))


def expected_radius(a, b):
    n = a + b
    if n % 2 or a == b:
        return n // 2 - 1
    return n // 2 - 2


def main():
    cases = [(a, b) for a in range(3, 7) for b in range(3, 7)]
    cases += [(3, 7), (7, 3), (4, 7), (7, 4)]
    comparisons = 0
    checked_switches = 0
    for a, b in cases:
        n = a + b
        observed = reachable(a, b)
        pred = predicted(a, b)
        assert observed == pred, (a, b, 'reachable sets differ', observed ^ pred)
        assert len(pred) == 4*n - 2
        counter = Counter(x.bit_count() for x in pred)
        assert counter == Counter({0: 1, 1: n, 2: n-2,
                                   n-2: n-2, n-1: n, n: 1}), (a,b,counter)
        distances = []
        for mask in range(1 << n):
            actual = min((mask ^ cw).bit_count() for cw in observed)
            predicted_d = predicted_distance(a, b, mask)
            assert actual == predicted_d, (a, b, mask, actual, predicted_d)
            comparisons += 1
            distances.append(actual)
        rad = max(distances)
        assert rad == expected_radius(a, b), (a,b,rad,expected_radius(a,b))
        if a == b:
            deep = {i for i, d in enumerate(distances) if d == rad}
            assert deep == {(1 << a) - 1, ((1 << n)-1)^((1<<a)-1)}, (a,b,deep)
        print(f'K_{{{a},{b}}}: |code|={len(observed)}, radius={rad}, masks={1 << n}')
    for a, b in [(3, 3), (3, 4)]:
        n = a + b
        base = reachable(a, b)
        all_bits = (1 << n) - 1
        for switch in range(1 << n):
            transformed = frozenset(x ^ switch for x in base)
            assert reachable(a, b, switch) == transformed
            checked_switches += 1
    assert len(reachable(2, 3)) == 20  # Thin-part boundary is genuinely different.
    print(f'PASS {len(cases)} full graph-state families; {comparisons} distance comparisons; '
          f'{checked_switches} entire switching-class enumerations')


if __name__ == '__main__':
    main()
