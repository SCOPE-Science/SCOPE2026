"""Two-method finite checks for embedded monogenic inverse submonoid counts.

Run: python checker.py. Uses only the Python standard library.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial, gcd, lcm


def divisors(k):
    return [d for d in range(1, k + 1) if k % d == 0]


def mobius(m):
    sign = 1
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            sign = -sign
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    return -sign if m > 1 else sign


def totient(m):
    return sum(gcd(j, m) == 1 for j in range(1, m + 1))


def exponential_coefficient(n, chain_cutoff, cycle_divisor):
    """Coefficient of exp(sum_{j<=cutoff}z^j + sum_{j|d}z^j/j)."""
    log_coeff = [Fraction(0)] * (n + 1)
    for j in range(1, n + 1):
        if j <= chain_cutoff:
            log_coeff[j] += 1
        if cycle_divisor % j == 0:
            log_coeff[j] += Fraction(1, j)
    coeff = [Fraction(0)] * (n + 1)
    coeff[0] = 1
    for j in range(1, n + 1):
        coeff[j] = sum(i * log_coeff[i] * coeff[j - i]
                       for i in range(1, j + 1)) / j
    return coeff[n]


def predicted(n, a, k):
    exact = sum(mobius(k // d) * exponential_coefficient(n, a, d)
                for d in divisors(k))
    if a >= 2:
        exact -= sum(mobius(k // d) * exponential_coefficient(n, a - 1, d)
                     for d in divisors(k))
    exact *= Fraction(factorial(n), totient(k) if a == 1 else 2)
    assert exact.denominator == 1, (n, a, k, exact)
    return exact.numerator


def all_partial_permutations(n):
    universe = range(n)
    for rank in range(n + 1):
        for domain in combinations(universe, rank):
            for image in combinations(universe, rank):
                for target in permutations(image):
                    p = [-1] * n
                    for x, y in zip(domain, target):
                        p[x] = y
                    yield tuple(p)


def parameter_pair(p):
    n = len(p)
    indeg = [0] * n
    for y in p:
        if y != -1:
            indeg[y] += 1
    covered = set()
    max_chain = 1
    for start in range(n):
        if indeg[start] != 0:
            continue
        x, length = start, 0
        while x != -1:
            assert x not in covered
            covered.add(x)
            length += 1
            x = p[x]
        max_chain = max(max_chain, length)
    cycle_order = 1
    for start in range(n):
        if start in covered:
            continue
        x, length = start, 0
        while x not in covered:
            covered.add(x)
            length += 1
            x = p[x]
        assert x == start
        cycle_order = lcm(cycle_order, length)
    return max_chain, cycle_order


def compose(p, q):
    return tuple(-1 if y == -1 else q[y] for y in p)


def invert(p):
    q = [-1] * len(p)
    for x, y in enumerate(p):
        if y >= 0:
            q[y] = x
    return tuple(q)


def generated_inverse_monoid(p):
    identity = tuple(range(len(p)))
    gens = (p, invert(p))
    visited = {identity}
    pending = [identity]
    while pending:
        x = pending.pop()
        for g in gens:
            y = compose(x, g)
            if y not in visited:
                visited.add(y)
                pending.append(y)
    return frozenset(visited)


def check():
    expected_totals = {1: 2, 2: 6, 3: 24, 4: 126, 5: 838, 6: 6841}
    for n in range(1, 7):
        fibers = defaultdict(list)
        total_elements = 0
        for f in all_partial_permutations(n):
            total_elements += 1
            key = generated_inverse_monoid(f)
            fibers[key].append(f)
        assert total_elements == sum(combinations_count(n, r)**2 * factorial(r)
                                     for r in range(n + 1))
        actual = defaultdict(int)
        for generators in fibers.values():
            params = {parameter_pair(g) for g in generators}
            assert len(params) == 1, (n, params)
            a, k = params.pop()
            assert len(generators) == (totient(k) if a == 1 else 2), (n, a, k)
            actual[(a, k)] += 1
        ceiling = lcm(*range(1, n + 1))
        formula = {(a, k): predicted(n, a, k)
                   for a in range(1, n + 1) for k in divisors(ceiling)}
        formula = {key: count for key, count in formula.items() if count}
        assert dict(actual) == formula, (n, dict(actual), formula)
        assert len(fibers) == expected_totals[n], (n, len(fibers))
        print('n=%d embedded=%d cycle_only=%d' %
              (n, len(fibers), sum(v for (a, k), v in formula.items() if a == 1)))
        if n == 4:
            assert formula == {(1, 1): 16, (1, 2): 27, (1, 3): 8,
                               (1, 4): 3, (2, 1): 30, (2, 2): 6,
                               (3, 1): 24, (4, 1): 12}
    print('VERIFY_OK')


def combinations_count(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))


if __name__ == '__main__':
    check()
