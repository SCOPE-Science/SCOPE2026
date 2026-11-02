#!/usr/bin/env python3
"""Standalone exact checks for synchronous majority on a leaf-corona cycle.

Run with Python 3. No dependencies beyond the standard library.
The proof for arbitrary order uses an explicit two-layer graph isomorphism;
this program checks independent microscopic dynamics at finite orders.
"""


def majority_update(state, n):
    mask = (1 << n) - 1
    core = state & mask
    leaves = (state >> n) & mask
    left = ((core << 1) | (core >> (n - 1))) & mask
    right = (core >> 1) | ((core & 1) << (n - 1))
    next_core = (left & right) | (left & leaves) | (right & leaves)
    return (core << n) | next_core


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def run_count(n):
    return lucas(n) + (2, 1, -1, -2, -1, 1)[n % 6]


def closed_prediction(n):
    fixed = run_count(n)
    periodic = run_count(2 * n) if n % 2 else fixed * fixed
    return fixed, periodic, (periodic - fixed) // 2


def direct_dynamics(n):
    fixed = periodic = 0
    for state in range(1 << (2 * n)):
        successor = majority_update(state, n)
        if successor == state:
            fixed += 1
        if majority_update(successor, n) == state:
            periodic += 1
    return fixed, periodic, (periodic - fixed) // 2


def brute_cyclic_words(n):
    count = 0
    for word in range(1 << n):
        if all(
            ((word >> i) & 1)
            in (((word >> ((i - 1) % n)) & 1), ((word >> ((i + 1) % n)) & 1))
            for i in range(n)
        ):
            count += 1
    return count


def charpoly_check():
    # The four states are 00, 01, 10, 11.
    A = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
    # Matrix satisfies x^4 - 2*x^3 + x^2 - 1 = 0.
    def product(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    I = [[int(i == j) for j in range(4)] for i in range(4)]
    A2 = product(A, A)
    A3 = product(A2, A)
    A4 = product(A3, A)
    assert all(A4[i][j] - 2*A3[i][j] + A2[i][j] - I[i][j] == 0
               for i in range(4) for j in range(4))
    power = I
    for n in range(1, 41):
        power = product(power, A)
        assert sum(power[i][i] for i in range(4)) == run_count(n), n
    return 40


def main():
    terms = charpoly_check()
    binary_words = 0
    for n in range(3, 17):
        assert brute_cyclic_words(n) == run_count(n), n
        binary_words += 1 << n
    print('FOUR_STATE_TRANSFER_OK', terms, 'trace powers; cyclic-word checks', binary_words)
    tested = 0
    for n in range(3, 11):
        expected = closed_prediction(n)
        observed = direct_dynamics(n)
        assert observed == expected, (n, observed, expected)
        tested += 1 << (2 * n)
        print('n', n, 'fixed', observed[0], '2-step states', observed[1], 'primitive orbits', observed[2])
    print('SUNLET_MAJORITY_VERIFY_OK', tested, 'microscopic states')


if __name__ == '__main__':
    main()
