"""Direct finite checks for sequential three-site parity on binary cycles.

Run using Python 3, with no dependencies: python verify.py
The assertions test the stated exact fixed-point formula, map orders,
primitive period populations, and scan-order multiplicities. Finite checks
supplement, but do not replace, the general mathematical proof.
"""
from itertools import permutations
from math import gcd, lcm
from random import Random
from collections import Counter


def scan(x, n, order):
    for i in order:
        x ^= (((x >> ((i - 1) % n)) ^ (x >> ((i + 1) % n))) & 1) << i
    return x


def linear_columns(n, order):
    return [scan(1 << i, n, order) for i in range(n)]


def mat_apply(columns, x):
    y = 0
    while x:
        bit = x & -x
        y ^= columns[bit.bit_length() - 1]
        x ^= bit
    return y


def rank(columns):
    pivots = {}
    for v in columns:
        while v:
            p = v.bit_length() - 1
            if p not in pivots:
                pivots[p] = v
                break
            v ^= pivots[p]
    return len(pivots)


def cyclic_ascents(n, order):
    positions = [0] * n
    for j, i in enumerate(order):
        positions[i] = j
    return sum(positions[i] < positions[(i + 1) % n] for i in range(n))


def order_bound(n, k):
    left, right = k, n - k
    ell = lcm(left, right)
    return ell if (left & -left) == (right & -right) else 2 * ell


def fixed_count(n, k, t):
    g = gcd(k, t)
    h = gcd(n - k, t)
    assert (n * t) % (g * h) == 0
    correction = (n * t // (g * h)) % 2
    return 1 << (g + h - correction)


def check_matrix(n, order):
    k = cyclic_ascents(n, order)
    expected_order = order_bound(n, k)
    matrix = linear_columns(n, order)
    current = [1 << i for i in range(n)]
    # Equality is checked over every iterate for small sizes. Large tests
    # check an initial range and a separate exact full-order endpoint.
    for t in range(1, min(expected_order, 60) + 1):
        current = [mat_apply(matrix, v) for v in current]
        nullity = n - rank([current[i] ^ (1 << i) for i in range(n)])
        assert (1 << nullity) == fixed_count(n, k, t), (n, order, k, t)
    if expected_order > 60:
        for _ in range(60, expected_order):
            current = [mat_apply(matrix, v) for v in current]
    assert current == [1 << i for i in range(n)], (n, order, expected_order)
    # Endpoint is exact, since the predicted order must be a multiple
    # of both edge permutation cycle lengths and is no larger than 2*lcm.
    return k, expected_order


def check_state_orbits(n, order, k, expected_order):
    visited = set()
    periods = Counter()
    for x in range(1 << n):
        if x in visited:
            continue
        cur = x
        trajectory = []
        while cur not in visited:
            visited.add(cur)
            trajectory.append(cur)
            cur = scan(cur, n, order)
        assert cur == x, (n, order, x)  # every local update is involutive
        p = len(trajectory)
        assert expected_order % p == 0
        periods[p] += p
    assert sum(periods.values()) == (1 << n)
    for t in range(1, expected_order + 1):
        direct = sum(count for p, count in periods.items() if t % p == 0)
        assert direct == fixed_count(n, k, t), (n, order, t, direct)


def eulerian(n):
    a = [1]
    for m in range(2, n + 1):
        prev = a
        a = [0] * m
        for j in range(m):
            if j < m-1:
                a[j] += (j + 1) * prev[j]
            if j > 0:
                a[j] += (m - j) * prev[j - 1]
    return a


def main():
    rng = Random(150150)
    matrix_cases = 0
    all_state_cases = 0
    state_visits = 0
    all_orders_count = {}
    for n in range(3, 9):
        if n <= 7:
            sample = permutations(range(n))
        else:
            sample = (tuple(rng.sample(range(n), n)) for _ in range(3000))
        counter = Counter()
        for order in sample:
            k, p = check_matrix(n, order)
            matrix_cases += 1
            counter[k] += 1
            if n <= 7:
                check_state_orbits(n, order, k, p)
                all_state_cases += 1
                state_visits += 1 << n
        if n <= 7:
            target = {k: n * eulerian(n - 1)[k - 1] for k in range(1, n)}
            assert dict(counter) == target, (n, counter, target)
            all_orders_count[n] = target
    for n in range(9, 26):
        for _ in range(200):
            order = tuple(rng.sample(range(n), n))
            check_matrix(n, order)
            matrix_cases += 1
    example = {}
    for k in (1, 2, 3):
        order = list(range(k)) + list(range(5, k - 1, -1))
        assert cyclic_ascents(6, order) == k
        example[k] = {'scan': order, 'map_order': order_bound(6, k)}
    assert {k: v['map_order'] for k, v in example.items()} == {1: 5, 2: 8, 3: 3}
    print('ALL_CHECKS_PASSED')
    print('matrix_and_order_cases', matrix_cases)
    print('exhaustive_scan_orders', all_state_cases)
    print('exhaustive_initial_states', state_visits)
    print('scan_order_distribution_through_n7', all_orders_count)
    print('n6_scan_order_examples', example)

if __name__ == '__main__':
    main()
