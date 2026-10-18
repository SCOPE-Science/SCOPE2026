"""Exact finite checks for the chord-gap representation identity.

Run: python3 verify.py. No nonstandard packages.
The tests are finite checks, not a substitute for the analytic theorem.
"""
from itertools import combinations


def cycle_arc_values(n):
    total = n * (n + 1) // 2
    vals = {total}
    for start in range(n):
        s = 0
        for width in range(1, n):
            s += (start + width - 1) % n + 1
            vals.add(s)
    return vals


def path_interior(n, u, v):
    one = []
    w = u
    while True:
        w = w % n + 1
        if w == v:
            break
        one.append(w)
    two = []
    w = v
    while True:
        w = w % n + 1
        if w == u:
            break
        two.append(w)
    return one, two


def gap_sums(path):
    sums = {0}
    for i in range(len(path)):
        s = 0
        for j in range(i, len(path)):
            s += path[j]
            sums.add(s)
    return sums


def gap_formula(n, u, v):
    total = n * (n + 1) // 2
    one, two = path_interior(n, u, v)
    a, b = gap_sums(one), gap_sums(two)
    return cycle_arc_values(n) | {total - x - y for x in a for y in b}


def brute_connected_sums(n, u, v):
    adjacent = [0] * n
    for a in range(n):
        b = (a + 1) % n
        adjacent[a] |= 1 << b
        adjacent[b] |= 1 << a
    adjacent[u - 1] |= 1 << (v - 1)
    adjacent[v - 1] |= 1 << (u - 1)
    values = set()
    for subset in range(1, 1 << n):
        reach = subset & -subset
        while True:
            frontier = 0
            w = reach
            while w:
                bit = w & -w
                w ^= bit
                frontier |= adjacent[bit.bit_length() - 1]
            expanded = reach | (frontier & subset)
            if expanded == reach:
                break
            reach = expanded
        if reach == subset:
            values.add(sum(j + 1 for j in range(n) if subset & (1 << j)))
    return values


def mult_table(N):
    return {a * b for a in range(1, N + 1) for b in range(1, N + 1)}


def test():
    exact = 0
    bounds = 0
    for n in range(4, 13):
        m = mult_table(2 * n)
        arcs = cycle_arc_values(n)
        assert len(arcs) <= 2 * len(m)
        for u, v in combinations(range(1, n + 1), 2):
            if v - u in (1, n - 1):
                continue
            predicted = gap_formula(n, u, v)
            actual = brute_connected_sums(n, u, v)
            assert predicted == actual, (n, u, v, sorted(predicted ^ actual))
            exact += 1
            a, b = path_interior(n, u, v)
            d = min(len(a), len(b)) + 1
            short = 1 + (d - 1) * d // 2
            assert len(actual) <= 2 * len(m) + short * (1 + 2 * len(m))
            bounds += 1
        # Every non-wrapping interval is a product with factors at most 2n.
        for i in range(1, n + 1):
            total = 0
            for j in range(i, n + 1):
                total += j
                assert total in m, (n, i, j)
    print('VERIFY_OK exact_chord_instances=%d upper_bound_checks=%d n_range=4..12' % (exact, bounds))


if __name__ == '__main__':
    test()
