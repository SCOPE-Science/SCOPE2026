"""Exact, standalone checks for mixed cycle-count dependence after transpositions.
Only standard-library Python is required. Finite checks corroborate an analytic proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def formula(n, t):
    if n < 6 or t < 0:
        raise ValueError('n >= 6 and nonnegative integer t required')
    a = Fraction((n - 3) * (n - 4), n * (n - 1))
    b = Fraction((n - 3) * (n - 5), (n - 1) ** 2)
    c = Fraction(n - 7, n - 1)
    return Fraction((n - 1) * (n - 2), 12) * (
        -2 * n * a**t + 3 * (n - 1) * b**t - (n - 3) * c**t)


def cycle_counts(p):
    seen = set()
    twos = 0
    for i in range(len(p)):
        if i not in seen:
            cur = i
            length = 0
            while cur not in seen:
                seen.add(cur)
                cur = p[cur]
                length += 1
            if length == 2:
                twos += 1
    return sum(x == i for i, x in enumerate(p)), twos


def check_walk(n, upto=7):
    p0 = tuple(range(n))
    dist = {p0: 1}
    transitions = list(combinations(range(n), 2))
    degree = len(transitions)
    for t in range(upto + 1):
        sf = sq = sfq = 0
        for p, weight in dist.items():
            f, q = cycle_counts(p)
            sf += weight * f
            sq += weight * q
            sfq += weight * f * q
        den = degree**t
        empirical = Fraction(sfq, den) - Fraction(sf * sq, den * den)
        if n >= 6:
            expected = formula(n, t)
            assert empirical == expected, (n, t, empirical, expected)
        if n == 5 and t == 3:
            assert empirical == Fraction(6, 25)
        if n == 6 and t >= 2:
            assert empirical < 0
        print(f'n={n} steps={t} states={len(dist)} covariance={empirical}')
        if t < upto:
            next_dist = defaultdict(int)
            for p, ways in dist.items():
                for i, j in transitions:
                    q = list(p)
                    q[i], q[j] = q[j], q[i]
                    next_dist[tuple(q)] += ways
            dist = next_dist


def hooks_dim(parts):
    total = sum(parts)
    hooks = 1
    for i, row in enumerate(parts):
        for j in range(row):
            right = row - j - 1
            below = sum(r > j for r in parts[i+1:])
            hooks *= 1 + right + below
    return factorial(total) // hooks


def eigen(parts):
    n = sum(parts)
    r = sum(x * (x - 2 * (i + 1) + 1) for i, x in enumerate(parts))
    return Fraction(r, n * (n - 1))


if __name__ == '__main__':
    checks = 0
    for n in range(6, 41):
        partitions = [(n-1,1),(n-2,2),(n-2,1,1),(n-3,3),(n-3,1,1,1)]
        expected_d = [n-1, n*(n-3)//2,(n-1)*(n-2)//2,
                      n*(n-1)*(n-5)//6,(n-1)*(n-2)*(n-3)//6]
        expected_r = [Fraction(n-3,n-1), Fraction(n-4,n), Fraction(n-5,n-1),
                      Fraction((n-3)*(n-4),n*(n-1)), Fraction(n-7,n-1)]
        for lam, d, r in zip(partitions, expected_d, expected_r):
            assert hooks_dim(lam) == d, (n, lam, d)
            assert eigen(lam) == r, (n, lam, r)
            checks += 2
        for t in range(2, 21):
            assert formula(n, t) < 0, (n,t)
            checks += 1
        assert formula(n,0)==0 and formula(n,1)==0
        checks += 2
    for n, upto in [(5,4),(6,7),(7,7)]:
        check_walk(n, upto)
    print(f'PASS: {checks} exact representation/formula assertions; 21 exact Markov-walk moments; n=5 sharp counterexample.')
