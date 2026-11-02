"""Independent finite-state checks for the crown-network two-neighbor-count game.

Python 3 standard library only. Every enumerated equilibrium is evaluated directly
from the graph's adjacency, independently of the classification proof.
"""
from itertools import combinations
from math import comb, factorial


def expected(n, r):
    return 2 + n + comb(n, r + 1) + (comb(2 * r, r) if n == 2 * r else 0)


def predicted(n, r):
    result = set()
    full = (1 << n) - 1
    result.add((full, 0))
    result.add((0, full))
    for t in (1, r + 1):
        for subset in combinations(range(n), t):
            bits = sum(1 << i for i in subset)
            result.add((bits, bits))
    if n == 2 * r:
        for subset in combinations(range(n), r):
            bits = sum(1 << i for i in subset)
            result.add((bits, full ^ bits))
    return result


def direct_equilibrium(n, r, x, y):
    # Evaluate the neighborhood of EACH vertex from distinct graph edges.
    for i in range(n):
        x_count = sum((y >> j) & 1 for j in range(n) if j != i)
        y_count = sum((x >> j) & 1 for j in range(n) if j != i)
        if ((x >> i) & 1) != int(x_count == 0 or x_count == r):
            return False
        if ((y >> i) & 1) != int(y_count == 0 or y_count == r):
            return False
    return True


def complete_bipartite_equilibrium(n, r, x, y):
    # Same best responses, but restore ALL missing matched cross-edges.
    X = x.bit_count()
    Y = y.bit_count()
    for i in range(n):
        if ((x >> i) & 1) != int(Y in (0, r)):
            return False
        if ((y >> i) & 1) != int(X in (0, r)):
            return False
    return True


def type_count(n, r):
    # Four independent pair types (00, 01, 10, 11), summed over ALL types.
    # This is not the classified solution family and is an independent tally.
    total = 0
    f = factorial
    for a in range(n + 1):
        for b in range(n - a + 1):
            for c in range(n - a - b + 1):
                d = n - a - b - c
                X = c + d
                Y = b + d
                valid = True
                for kind, size in (((0, 0), a), ((0, 1), b), ((1, 0), c), ((1, 1), d)):
                    if size == 0:
                        continue
                    xi, yi = kind
                    if xi != int((Y - yi) in (0, r)) or yi != int((X - xi) in (0, r)):
                        valid = False
                        break
                if valid:
                    total += f(n) // (f(a) * f(b) * f(c) * f(d))
    return total


def main():
    brute_states = 0
    brute_cases = 0
    factor_cases = 0
    for n in range(4, 9):
        full = 1 << n
        for r in range(2, n - 1):
            classified = predicted(n, r)
            assert len(classified) == expected(n, r), (n, r, 'formula')
            found = set()
            complete_count = 0
            for x in range(full):
                for y in range(full):
                    brute_states += 1
                    if direct_equilibrium(n, r, x, y):
                        found.add((x, y))
                    if complete_bipartite_equilibrium(n, r, x, y):
                        complete_count += 1
            assert complete_count == 2, (n, r, complete_count)
            assert found == classified, (n, r, 'unclassified', found - classified,
                                         'spurious', classified - found)
            brute_cases += 1
    for n in range(4, 31):
        for r in range(2, n - 1):
            count = type_count(n, r)
            assert count == expected(n, r), (n, r, count, expected(n, r))
            factor_cases += 1
    print('VERIFIED')
    print(f'directly_evaluated_profiles={brute_states}')
    print(f'direct_equilibrium_exhaustive_parameter_pairs={brute_cases}')
    print(f'independent_four_type_weighted_count_parameter_pairs={factor_cases}')
    print(f'example_n6_r3={expected(6,3)}')
    print(f'example_n7_r3={expected(7,3)}')


if __name__ == '__main__':
    main()
