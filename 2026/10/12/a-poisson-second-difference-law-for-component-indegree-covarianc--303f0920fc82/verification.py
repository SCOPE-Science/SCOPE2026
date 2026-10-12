#!/usr/bin/env python3
"""Independent exact finite checks of mapping component--in-degree covariance."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, exp, factorial


def cycle_count(images):
    """Weak components of a functional digraph, counted by directed cycles."""
    n = len(images)
    seen = [0] * n
    cycles = 0
    for source in range(n):
        if seen[source]:
            continue
        cur = source
        mark = source + 1
        while seen[cur] == 0:
            seen[cur] = mark
            cur = images[cur]
        if seen[cur] == mark:
            cycles += 1
    return cycles


def exact_covariance(n):
    total = n**n
    sum_cycles = 0
    sum_degrees = [0] * (n + 1)
    mixed = [0] * (n + 1)
    for images in product(range(n), repeat=n):
        c = cycle_count(images)
        in_deg = [0] * n
        for vertex in images:
            in_deg[vertex] += 1
        histogram = Counter(in_deg)
        sum_cycles += c
        for r in range(n + 1):
            number = histogram.get(r, 0)
            sum_degrees[r] += number
            mixed[r] += number * c
    return [Fraction(mixed[r], total)
            - Fraction(sum_cycles * sum_degrees[r], total * total)
            for r in range(n + 1)]


def bernoulli(n, m, r):
    if not 0 <= r <= m:
        return Fraction(0)
    return Fraction(comb(m, r) * (n - 1)**(m - r), n**m)


def formula(n):
    answer = [Fraction(0) for _ in range(n + 1)]
    falling_probability = Fraction(1)
    for k in range(1, n + 1):
        falling_probability *= Fraction(n - k + 1, n)
        m = n - k
        for r in range(n + 1):
            conditional = k * bernoulli(n, m, r - 1) + m * bernoulli(n, m, r)
            marginal = n * bernoulli(n, n, r)
            answer[r] += falling_probability * Fraction(conditional - marginal, k)
    return answer


def check():
    ncases = 0
    for n in range(2, 8):
        explicit = exact_covariance(n)
        theorem = formula(n)
        assert explicit == theorem, (n, explicit, theorem)
        assert sum(theorem, Fraction(0)) == 0
        assert sum((r * v for r, v in enumerate(theorem)), Fraction(0)) == 0
        ncases += n + 1
        print('exact_enumeration_pass', n, 'mappings', n**n,
              'cov0', str(theorem[0]), 'cov1', str(theorem[1]))
    for n in [100, 500, 2000]:
        u = -1.0 / n
        a = 1.0
        coeff = [0.0] * 5
        p0 = (1 - 1/n)**n
        for k in range(1, n + 1):
            a *= (n - k + 1) / n
            m = n - k
            for r in range(5):
                pc = (comb(m, r) * (1/n)**r * (1-1/n)**(m-r)) if r <= m else 0.0
                pp = (comb(m, r-1) * (1/n)**(r-1) * (1-1/n)**(m-r+1)) if 1 <= r <= m+1 else 0.0
                pm = (comb(n,r) * (1/n)**r * (1-1/n)**(n-r))
                coeff[r] += a/k * (k*pp + m*pc - n*pm)
        asympt = [exp(-1) * (-r*r+3*r-1) / (2*factorial(r)) for r in range(5)]
        errors = [float(v)-t for v,t in zip(coeff,asympt)]
        print('asymptotic_diagnostics', n, 'errors_r0_to_r4', errors, flush=True)
    print('VERIFY_OK all_degrees', ncases,
          'independent_mappings', sum(n**n for n in range(2, 8)),
          'conservation_identities', 12)

if __name__ == '__main__':
    check()
