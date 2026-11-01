#!/usr/bin/env python3
"""Exact finite checks for neighbor-XOR on a hypercube with one deleted edge.

Runs using only the Python standard library.  A dimension parameter d represents
2**d vertices; all arithmetic on states and matrices is over GF(2).
The infinite-family assertions require the mathematical proof, not these tests.
"""
from collections import Counter


def graph_rows(d):
    size = 1 << d
    rows = []
    for v in range(size):
        mask = 0
        for bit in range(d):
            w = v ^ (1 << bit)
            if {v, w} != {0, 1}:
                mask |= 1 << w
        rows.append(mask)
    return rows


def multiply(m, k):
    out = []
    for row in m:
        acc = 0
        for j in range(len(k)):
            if (row >> j) & 1:
                acc ^= k[j]
        out.append(acc)
    return out


def eye(size):
    return [1 << i for i in range(size)]


def powers(a, bound):
    p = eye(len(a))
    result = [p]
    for _ in range(bound):
        p = multiply(p, a)
        result.append(p)
    return result


def add(a, b):
    return [i ^ j for i, j in zip(a, b)]


def rank(rows):
    pivot = {}
    for row in rows:
        while row:
            bit = row.bit_length() - 1
            if bit in pivot:
                row ^= pivot[bit]
            else:
                pivot[bit] = row
                break
    return len(pivot)


def advance(rows, state):
    return sum(((row & state).bit_count() % 2) << i
               for i, row in enumerate(rows))


def test_rank_profiles():
    checks = 0
    for d in range(2, 9):
        n = 1 << d
        m = n // 2
        b = graph_rows(d)
        pp = powers(b, 8)
        ident = eye(n)
        if d % 2 == 0:
            assert rank(pp[1]) == m + 2, d
            assert rank(pp[2]) == 4, d
            assert all(rank(pp[t]) == 4 for t in range(2, 9)), d
            assert pp[8] == pp[2], d
            assert [n - rank(add(pp[t], ident)) for t in (1, 3, 6)] == [0, 2, 4], d
            expected_zero_jordan = m - 2
            assert n == 4 + 2 * expected_zero_jordan
            checks += 14
        else:
            assert rank(pp[1]) == n - 2, d
            assert all(rank(pp[t]) == n - 2 for t in range(1, 9)), d
            assert pp[5] == pp[1], d
            assert [n - rank(add(pp[t], ident)) for t in (1, 2, 4)] == [m - 2, n - 4, n - 2], d
            j4, j2 = 1, m - 3
            assert n == 2 + 4 * j4 + 2 * j2
            checks += 14
        print(f'd={d}, vertices={n}, ranks F,F^2={rank(pp[1])},{rank(pp[2])}: OK')
    return checks


def test_all_states():
    checked = 0
    for d in (2, 3, 4):
        n = 1 << d
        m = n // 2
        b = graph_rows(d)
        expected = ((16, (1 << (m + 2)) - 16,
                     (1 << n) - (1 << (m + 2))) if d % 2 == 0
                    else ((1 << (n - 2)), (1 << n) - (1 << (n - 2))))
        expected_periods = (({1: 1, 3: 3, 6: 12}) if d % 2 == 0
                            else {1: (1 << (m - 2)),
                                  2: (1 << (n - 4)) - (1 << (m - 2)),
                                  4: (1 << (n - 2)) - (1 << (n - 4))})
        shells = Counter()
        period_populations = Counter()
        for state in range(1 << n):
            traj = [state]
            seen = {state: 0}
            while True:
                nxt = advance(b, traj[-1])
                if nxt in seen:
                    t = seen[nxt]
                    p = len(traj) - t
                    shells[t] += 1
                    if t == 0:
                        period_populations[p] += 1
                    break
                seen[nxt] = len(traj)
                traj.append(nxt)
            checked += 1
        assert tuple(shells[i] for i in range(len(expected))) == expected, (d, shells, expected)
        assert not any(i >= len(expected) for i in shells), (d, shells)
        assert dict(period_populations) == expected_periods, (d, period_populations, expected_periods)
        print(f'd={d}, all {1 << n} states: T shells={dict(sorted(shells.items()))}, primitive-period state populations={dict(sorted(period_populations.items()))}: OK')
    return checked



def test_extension_field():
    """Exhaustively test q=4; all matrix coefficients remain in the prime field."""
    checked = 0
    q = 4
    for d in (2, 3):
        n = 1 << d
        m = n // 2
        rows = graph_rows(d)
        assert n <= 8
        def step(state):
            nxt = 0
            for i, row in enumerate(rows):
                value = 0
                for j in range(n):
                    if (row >> j) & 1:
                        value ^= (state >> (2 * j)) & 3
                nxt |= value << (2 * i)
            return nxt
        shells = Counter()
        periods = Counter()
        for initial in range(1 << (2*n)):
            visited = {initial: 0}
            trajectory = [initial]
            while True:
                nxt = step(trajectory[-1])
                if nxt in visited:
                    t = visited[nxt]
                    p = len(trajectory) - t
                    shells[t] += 1
                    if t == 0:
                        periods[p] += 1
                    break
                visited[nxt] = len(trajectory)
                trajectory.append(nxt)
            checked += 1
        if d % 2 == 0:
            expected_shells = {0: q**4}
            expected_periods = {1: 1, 3: q**2 - 1, 6: q**4 - q**2}
        else:
            expected_shells = {0: q**(n-2), 1: q**n - q**(n-2)}
            expected_periods = {1:q**(m-2), 2:q**(n-4)-q**(m-2), 4:q**(n-2)-q**(n-4)}
        assert dict(shells) == expected_shells, (d, shells)
        assert dict(periods) == expected_periods, (d, periods)
        print(f'GF(4) d={d}: {1 << (2*n)} states, shells={dict(sorted(shells.items()))}, periodic={dict(sorted(periods.items()))}: OK')
    return checked


def main():
    algebraic = test_rank_profiles()
    states = test_all_states()
    extension_states = test_extension_field()
    print(f'ALGEBRAIC_CHECK_GROUPS={algebraic}; EXHAUSTIVE_BINARY_CONFIGURATIONS={states}; EXHAUSTIVE_GF4_CONFIGURATIONS={extension_states}')
    print('EDGE_DELETED_HYPERCUBE_ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
