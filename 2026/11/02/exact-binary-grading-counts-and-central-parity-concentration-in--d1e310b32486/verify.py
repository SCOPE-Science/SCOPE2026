"""Direct finite-field checks of grading counts for centrally stabilized Heisenberg Lie algebras.

Run: python3 verify.py.  Exhaustive checks cover selected small prime fields only;
the formulas for all prime powers and arbitrary dimensions require the proof.
"""
import itertools


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    numerator = denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    assert numerator % denominator == 0
    return numerator // denominator


def symplectic_order(n, q):
    ans = q ** (n * n)
    for i in range(1, n + 1):
        ans *= q ** (2 * i) - 1
    return ans


def predicted(n, r, q):
    c = r + 1
    even = 0
    for t in range(r + 1):
        centers = gaussian(r, t, q) * q ** (t * (c - t))
        for b in range(n + 1):
            symplectic_splittings = symplectic_order(n, q) // (
                symplectic_order(b, q) * symplectic_order(n - b, q)
            )
            lifts = q ** (2 * (n - b) * t + 2 * b * (c - t))
            even += centers * symplectic_splittings * lifts
    lagrangian_pairs = q ** (n * (n + 1) // 2)
    for i in range(1, n + 1):
        lagrangian_pairs *= q ** i + 1
    odd = sum(
        gaussian(r, t - 1, q) * q ** (t * (c - t))
        * lagrangian_pairs * q ** (n * c)
        for t in range(1, c + 1)
    )
    return even, odd


def rref_subspaces(q, d):
    for k in range(d + 1):
        for pivots in itertools.combinations(range(d), k):
            free_positions = [(i, j) for i, p in enumerate(pivots)
                              for j in range(p + 1, d) if j not in pivots]
            for values in itertools.product(range(q), repeat=len(free_positions)):
                rows = [[int(j == p) for j in range(d)] for p in pivots]
                for value, (i, j) in zip(values, free_positions):
                    rows[i][j] = value
                yield tuple(map(tuple, rows))


def span(q, d, basis):
    vectors = {(0,) * d}
    for row in basis:
        vectors = {
            tuple((v[i] + scalar * row[i]) % q for i in range(d))
            for v in vectors for scalar in range(q)
        }
    return vectors


def direct_count(n, r, q):
    d = 2 * n + 1 + r
    central_generator = (0,) * (2 * n) + (1,) + (0,) * r
    subspaces = [(basis, span(q, d, basis)) for basis in rref_subspaces(q, d)]
    counts = [0, 0]
    for basis_even, space_even in subspaces:
        for basis_odd, space_odd in subspaces:
            if len(space_even) * len(space_odd) != q ** d:
                continue
            if len(space_even & space_odd) != 1:
                continue
            components = [basis_even, basis_odd]
            subspace_sets = [space_even, space_odd]
            valid = True
            for degree_left in range(2):
                for degree_right in range(2):
                    dest = subspace_sets[(degree_left + degree_right) % 2]
                    if central_generator in dest:
                        continue
                    for x in components[degree_left]:
                        for y in components[degree_right]:
                            coefficient = sum(
                                x[2 * j] * y[2 * j + 1]
                                - x[2 * j + 1] * y[2 * j]
                                for j in range(n)
                            ) % q
                            if coefficient:
                                valid = False
                                break
                        if not valid:
                            break
                    if not valid:
                        break
                if not valid:
                    break
            if valid:
                counts[int(central_generator in space_odd)] += 1
    return tuple(counts)


def projector_test_h3(q):
    basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    def matrix_vector(matrix, x):
        return tuple(sum(matrix[i][j] * x[j] for j in range(3)) % q for i in range(3))

    def lie_bracket(x, y):
        return (0, 0, (x[0] * y[1] - x[1] * y[0]) % q)

    counts = [0, 0]
    for entries in itertools.product(range(q), repeat=9):
        projection = [entries[i * 3:(i + 1) * 3] for i in range(3)]
        projected = [matrix_vector(projection, x) for x in basis]
        if any(matrix_vector(projection, projected[j]) != projected[j] for j in range(3)):
            continue
        valid = True
        for i in range(3):
            for j in range(3):
                ei = tuple((basis[i][k] - projected[i][k]) % q for k in range(3))
                ej = tuple((basis[j][k] - projected[j][k]) % q for k in range(3))
                if matrix_vector(projection, lie_bracket(ei, ej)) != (0, 0, 0):
                    valid = False
                if matrix_vector(projection, lie_bracket(projected[i], projected[j])) != (0, 0, 0):
                    valid = False
                cross = lie_bracket(ei, projected[j])
                if matrix_vector(projection, cross) != cross:
                    valid = False
        if valid:
            counts[int(projected[2] != (0, 0, 0))] += 1
    return tuple(counts)


def main():
    cases = [(1, 0, 2), (1, 1, 2), (1, 2, 2), (2, 0, 2), (1, 0, 3), (1, 1, 3)]
    for n, r, q in cases:
        direct = direct_count(n, r, q)
        expected = predicted(n, r, q)
        assert direct == expected, (n, r, q, direct, expected)
        print('PASS', 'q', q, 'n', n, 'r', r, 'even', direct[0], 'odd', direct[1])
    for q in (2, 3):
        direct = projector_test_h3(q)
        assert direct == predicted(1, 0, q), (q, direct, predicted(1, 0, q))
        print('PASS_PROJECTOR', q, direct)
    print('VERIFY_OK: six exhaustive decomposition cases, two exhaustive projector cases')


if __name__ == '__main__':
    main()
