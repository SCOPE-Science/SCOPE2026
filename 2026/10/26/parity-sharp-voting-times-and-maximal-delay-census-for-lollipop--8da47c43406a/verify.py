"""Reproduce finite tests for synchronous tie-retaining majority on lollipop graphs.

Run: python3 verify.py
No external libraries are required.
"""
from collections import Counter
from math import comb


def graph(m, ell):
    assert m >= 3 and ell >= 2
    n = m + ell
    neighbors = [[] for _ in range(n)]
    for u in range(m):
        for v in range(u + 1, m):
            neighbors[u].append(v)
            neighbors[v].append(u)
    for v in range(m, n):
        neighbors[v - 1].append(v)
        neighbors[v].append(v - 1)
    return [sum(1 << j for j in row) for row in neighbors], [len(row) for row in neighbors]


def direct_step(s, masks, degrees):
    out = 0
    for i, (mask, degree) in enumerate(zip(masks, degrees)):
        ones = (s & mask).bit_count()
        if 2 * ones > degree or (2 * ones == degree and ((s >> i) & 1)):
            out |= 1 << i
    return out


def maximal_condition(s, m, ell):
    h = (s >> (m - 1)) & 1
    a = (s & ((1 << (m - 1)) - 1)).bit_count()
    x = [(s >> (m + j)) & 1 for j in range(ell)]
    if m % 2:
        k = (m - 1) // 2
        return a == k and all(x[j] == (1 - h if j % 2 == 0 else h) for j in range(ell))
    k = m // 2
    if a + h == k:
        return (x[0] != h and
                all(x[j] != x[j - 1] for j in range(1, ell - 1)) and
                x[-1] == x[-2])
    if h == 0 and a >= k + 1 or h == 1 and a <= k - 2:
        return all(x[j] == (1 - h if j % 2 == 0 else h) for j in range(ell))
    return False


def periodic_two_condition(s, m, ell):
    if m % 2:
        return False
    h = (s >> (m - 1)) & 1
    a = (s & ((1 << (m - 1)) - 1)).bit_count()
    if a + h != m // 2:
        return False
    return all(((s >> (m + j)) & 1) == (1 - h if j % 2 == 0 else h) for j in range(ell))


def test(m, ell):
    n = m + ell
    masks, degrees = graph(m, ell)
    trans = [direct_step(s, masks, degrees) for s in range(1 << n)]
    state_info = {}
    for state in range(1 << n):
        if state in state_info:
            continue
        trail, loc, x = [], {}, state
        while x not in loc and x not in state_info:
            loc[x] = len(trail)
            trail.append(x)
            x = trans[x]
        if x in state_info:
            depth, cycle_size = state_info[x]
            for v in reversed(trail):
                depth += 1
                state_info[v] = (depth, cycle_size)
        else:
            split = loc[x]
            cycle_size = len(trail) - split
            for v in trail[split:]:
                state_info[v] = (0, cycle_size)
            depth = 0
            for v in reversed(trail[:split]):
                depth += 1
                state_info[v] = (depth, cycle_size)
    expected_depth = ell + 2 if m % 2 else ell + 1
    expected_max_count = 2 * comb(m - 1, (m - 1) // 2) if m % 2 else 2 ** (m - 1)
    expected_period_two = 0 if m % 2 else 2 * comb(m - 1, m // 2)
    actual_depth = max(depth for depth, _ in state_info.values())
    maximal = [s for s, (d, _) in state_info.items() if d == actual_depth]
    period_two = [s for s, (d, p) in state_info.items() if d == 0 and p == 2]
    assert actual_depth == expected_depth, (m, ell, 'depth', actual_depth)
    assert len(maximal) == expected_max_count, (m, ell, 'last-layer-count', len(maximal))
    assert len(period_two) == expected_period_two, (m, ell, 'periodic-two', len(period_two))
    assert all(period in (1, 2) for depth, period in state_info.values()), (m, ell, 'other-period')
    assert all(depth == 0 for depth, period in state_info.values() if period == 2), (m, ell, 'late-two-cycle')
    for s, (depth, period) in state_info.items():
        assert (depth == expected_depth) == maximal_condition(s, m, ell), (m, ell, 'maximal-structure', s)
        assert (depth == 0 and period == 2) == periodic_two_condition(s, m, ell), (m, ell, 'period-two-structure', s)
    return len(state_info), len(maximal), len(period_two)


def main():
    tests, configs, extremal, two = 0, 0, 0, 0
    for m in range(3, 9):
        for ell in range(2, 11):
            if m + ell > 17:
                continue
            a, b, c = test(m, ell)
            tests += 1
            configs += a
            extremal += b
            two += c
    print(f'graph_cases={tests}')
    print(f'labelled_configurations={configs}')
    print(f'extremal_states_examined={extremal}')
    print(f'primitive_two_cycle_states_examined={two}')
    print('LOLLIPOP_MAJORITY_VERIFY_OK')


if __name__ == '__main__':
    main()
