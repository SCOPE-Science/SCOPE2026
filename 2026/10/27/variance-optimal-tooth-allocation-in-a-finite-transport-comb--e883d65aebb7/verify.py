"""Separate finite-generator checks for comb first-passage moments and design."""
from fractions import Fraction
from itertools import product
from math import sqrt, ceil


def q(l):
    return Fraction(l * (l + 1) * (2 * l + 1), 3)


def closed_moments(lengths):
    n = len(lengths)
    m = []
    cum = 0
    for i, l in enumerate(lengths):
        cum += l
        m.append(i + 1 + cum)
    mean = sum(m)
    var = sum((2 * (n - i) - 1) * m[i] ** 2 +
              (n - i) * q(lengths[i]) for i in range(n))
    return Fraction(mean), Fraction(var)


def solve(A, b):
    """Exact Gauss-Jordan solution over rational numbers."""
    n = len(b)
    M = [[Fraction(x) for x in row] + [Fraction(bi)]
         for row, bi in zip(A, b)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if M[i][j])
        M[j], M[pivot] = M[pivot], M[j]
        div = M[j][j]
        M[j] = [z / div for z in M[j]]
        for i in range(n):
            if i != j:
                factor = M[i][j]
                if factor:
                    M[i] = [u - factor * v for u, v in zip(M[i], M[j])]
    return [M[i][-1] for i in range(n)]


def generator_moments(lengths):
    n = len(lengths)
    nodes = [(i, 0) for i in range(n)]
    nodes += [(i, j) for i, ell in enumerate(lengths) for j in range(1, ell + 1)]
    at = {v: k for k, v in enumerate(nodes)}
    Q = [[0] * len(nodes) for _ in nodes]
    edges = [((i, 0), (i + 1, 0)) for i in range(n)]
    edges += [((i, j - 1), (i, j))
              for i, ell in enumerate(lengths) for j in range(1, ell + 1)]
    for u, v in edges:
        if u in at:
            Q[at[u]][at[u]] += 1
        if v in at:
            Q[at[v]][at[v]] += 1
        if u in at and v in at:
            Q[at[u]][at[v]] -= 1
            Q[at[v]][at[u]] -= 1
    first = solve(Q, [1] * len(nodes))
    second = solve(Q, [2 * x for x in first])
    return first[0], second[0] - first[0] ** 2


def two_tooth_optimum(M):
    costs = [closed_moments((x, M - x))[1] for x in range(M + 1)]
    candidate = max(0, ceil((sqrt(32*M*M + 112*M + 92) - 4*M - 14) / 4))
    winners = [j for j, c in enumerate(costs) if c == min(costs)]
    assert winners == [candidate], (M, winners, candidate)
    return candidate


def main():
    count = 0
    for n in range(1, 5):
        for lengths in product(range(4), repeat=n):
            if sum(lengths) > 5:
                continue
            assert generator_moments(lengths) == closed_moments(lengths), lengths
            count += 1
    for M in range(41):
        x = two_tooth_optimum(M)
        assert (x == 0) == (M <= 2)
    n = 3
    S = sum(1 / sqrt(j) for j in range(1, n + 1))
    weights = [1 / sqrt(n-i) / S for i in range(n)]
    for budget in (40, 80, 160):
        candidates = ((a,b,budget-a-b) for a in range(budget+1)
                      for b in range(budget-a+1))
        best = min(candidates, key=lambda x: closed_moments(x)[1])
        variance = float(closed_moments(best)[1])
        print('budget', budget, 'optimal', best,
              'fractions', tuple(round(x / budget, 5) for x in best),
              'target', tuple(round(x, 5) for x in weights),
              'variance/M^3', round(variance / budget**3, 6),
              'target constant', round(2 / (3*S*S), 6))
    print('PASS: exact CTMC moment comparisons', count)
    print('PASS: unique finite two-tooth optima for M=0..40')


if __name__ == '__main__':
    main()
