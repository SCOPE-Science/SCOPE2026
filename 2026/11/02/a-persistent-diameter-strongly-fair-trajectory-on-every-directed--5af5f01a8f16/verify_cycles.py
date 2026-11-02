"""Exact-rational checks of weak-fairness rotation certificates on directed cycles.

The general all-size, all-weight result is proved analytically; these checks
exercise its indexing, block structure, and quantitative error bounds.
"""
from fractions import Fraction as F


def simulate(n, weights, revolutions=2):
    assert n >= 3 and len(weights) == n
    assert all(F(0) < p < F(1) for p in weights)
    actual = [F(int(i == 0)) for i in range(n)]
    ideal = actual.copy()
    accum = F(0)
    count = 0
    for j in range(n * revolutions):
        for target in ((j + 1) % n, j % n):
            source = (target - 1) % n
            # A directed edge source -> target; all other coordinates stay fixed.
            assert source != target
            p = weights[target]
            residual = F(1)
            N = 0
            tolerance = F(1, 2 ** (count + 4))
            while residual > tolerance:
                residual *= 1 - p
                N += 1
            assert N >= 1
            # The two untouched anchor vertices retain opposite ideal opinions.
            static = [i for i in range(n) if i != target]
            assert min(ideal[i] for i in static) == 0
            assert max(ideal[i] for i in static) == 1
            assert max(abs(actual[i] - ideal[i]) for i in range(n)) <= accum
            for _ in range(N):
                actual[target] = (1 - p) * actual[target] + p * actual[source]
                assert max(actual) - min(actual) >= F(3, 4)
                assert all(F(0) <= a <= F(1) for a in actual)
            ideal[target] = ideal[source]
            accum += residual
            assert accum <= F(1, 8)
            assert max(abs(actual[i] - ideal[i]) for i in range(n)) <= accum
            assert sum(ideal) in (1, 2)
            count += 1
    assert ideal == [F(int(i == 0)) for i in range(n)]
    return count, accum, min(actual), max(actual)


def main():
    tests = [
        (3, [F(1,2)] * 3),
        (4, [F(1,2)] * 4),
        (5, [F(1,3),F(1,2),F(2,3),F(3,4),F(2,5)]),
        (7, [F(2,5),F(3,5),F(1,2),F(2,3),F(1,4),F(3,4),F(1,3)]),
    ]
    for n, p in tests:
        blocks, error, lo, hi = simulate(n, p, revolutions=2)
        print(f'n={n}, blocks={blocks}, error_budget={error}, endpoint_diameter={hi-lo}')
    for p, q in [(F(1,2),F(1,2)),(F(1,3),F(4,5)),(F(2,5),F(3,7))]:
        x = [F(0),F(1)]
        for k in range(20):
            target = k % 2
            source = 1 - target
            old_gap = abs(x[0]-x[1])
            x[target] = (1-[p,q][target])*x[target] + [p,q][target]*x[source]
            assert abs(x[0]-x[1]) == old_gap * (1-[p,q][target])
    print('PASS: exact-rational rotation and two-agent contraction checks')

if __name__ == '__main__':
    main()
