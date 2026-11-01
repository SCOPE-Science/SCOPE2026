"""Standalone exact checks for neighbor-majority dynamics on a cycle with one leaf.
Run with: python3 verify.py
Requires Python 3 standard library only.
"""
from math import comb


def step(state, n):
    """Synchronous tie-retaining neighbor-majority; cycle 0..n-1, leaf n."""
    result = 0
    for i in range(n + 1):
        neighbors = ([n - 1, 1, n] if i == 0 else
                     [0] if i == n else
                     [(i - 1) % n, (i + 1) % n])
        ones = sum((state >> j) & 1 for j in neighbors)
        bit = (2 * ones > len(neighbors) or
               (2 * ones == len(neighbors) and ((state >> i) & 1)))
        if bit:
            result |= 1 << i
    return result


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


def trace_power(n):
    # State labels: 00, 01, 10, 11, with triples of pattern 010 or 101 disallowed.
    m = [[1, 1, 0, 0], [0, 0, 0, 1],
         [1, 0, 0, 0], [0, 0, 1, 1]]
    r = [[int(i == j) for j in range(4)] for i in range(4)]
    for _ in range(n):
        r = matmul(r, m)
    return sum(r[i][i] for i in range(4))


def fib(n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x


def lucas(n):
    return fib(n - 1) + fib(n + 1)


def two_cycle_closed(n):
    q = (1, 1, 0, -1, -1, 0)
    return fib(n - 2) - q[(n - 3) % 6] + (n % 2 == 0)


def two_cycle_run_count(n):
    ell = n - 1
    return (n % 2 == 0) + 2 * sum(
        comb(ell - 2 * r - 1, 2 * r - 1)
        for r in range(1, ell // 4 + 1)
    )


def fixed_closed(n):
    # Sequence 2*cos(pi*n/3), integer, period 6.
    trig = (2, 1, -1, -2, -1, 1)
    return lucas(n) + trig[n % 6]


def count_bruteforce(n, verify_structure):
    fixed, cycle_states = 0, 0
    for state in range(1 << (n + 1)):
        next_state = step(state, n)
        if step(next_state, n) != state:
            continue
        if next_state == state:
            fixed += 1
            assert (state >> n & 1) == (state & 1)
            continue
        cycle_states += 1
        if verify_structure:
            flipped = state ^ next_state
            all_flipped = flipped == (1 << (n + 1)) - 1
            root_leaf_only = flipped == (1 | (1 << n))
            assert all_flipped or root_leaf_only
            if all_flipped:
                assert n % 2 == 0
                assert all(((state >> i) & 1) !=
                           ((state >> ((i + 1) % n)) & 1)
                           for i in range(n))
            else:
                assert ((state >> 1) & 1) != ((state >> (n - 1)) & 1)
                interior = [(state >> i) & 1 for i in range(1, n)]
                assert len(interior) >= 4
                assert interior[0] == interior[1]
                assert interior[-1] == interior[-2]
                assert all(not (interior[i - 1] == interior[i + 1]
                                != interior[i])
                           for i in range(1, len(interior) - 1))
    assert cycle_states % 2 == 0
    return fixed, cycle_states // 2


def main():
    for n in range(3, 101):
        assert two_cycle_closed(n) == two_cycle_run_count(n), n
        assert trace_power(n) == fixed_closed(n), n
    print('Formula checks: n=3..100, transfer trace / Fibonacci / run compositions: PASS')
    total_states = 0
    for n in range(3, 18):
        f, c = count_bruteforce(n, verify_structure=(n <= 13))
        assert f == fixed_closed(n) == trace_power(n), (n, f)
        assert c == two_cycle_closed(n) == two_cycle_run_count(n), (n, c)
        total_states += 1 << (n + 1)
        print(f'n={n:2d} fixed={f:6d} primitive_two_orbits={c:6d} PASS')
    print(f'Exhaustive checks: {total_states} configurations, n=3..17: PASS')
    print('Structural flip-set checks for every period-two configuration, n=3..13: PASS')


if __name__ == '__main__':
    main()
