from fractions import Fraction
from itertools import product
from math import comb


def collision_count(x):
    counts = {}
    for a in x:
        counts[a] = counts.get(a, 0) + 1
    return sum(comb(v, 2) for v in counts.values())


def orbit(q, n, c):
    states = [x for x in product(range(q), repeat=n) if collision_count(x) == c]
    if not states:
        raise ValueError((q, n, c))
    p = Fraction(1, len(states))
    return {x: p for x in states}


def mix(parts):
    out = {}
    for weight, law in parts:
        for x, p in law.items():
            out[x] = out.get(x, Fraction(0)) + weight * p
    return {x: p for x, p in out.items() if p}


def check_pairwise_uniform(law, q, n):
    one = Fraction(1, q*q)
    for i in range(n):
        for j in range(i+1, n):
            for a in range(q):
                for b in range(q):
                    got = sum(p for x, p in law.items() if x[i] == a and x[j] == b)
                    assert got == one, (q, n, i, j, a, b, got, one)


def all_distinct_probability(law):
    return sum(p for x, p in law.items() if len(set(x)) == len(x))


def verify(q, n):
    M = comb(n, 2)
    mu = Fraction(M, q)
    U0 = orbit(q, n, 0)
    UM = orbit(q, n, M)

    upper = mix([(Fraction(q-1, q), U0), (Fraction(1, q), UM)])
    check_pairwise_uniform(upper, q, n)
    assert all_distinct_probability(upper) == Fraction(q-1, q)

    if mu <= 1:
        U1 = orbit(q, n, 1)
        lower = mix([(1-mu, U0), (mu, U1)])
        expected_lower = 1-mu
    else:
        U1 = orbit(q, n, 1)
        t = (mu-1) / (M-1)
        lower = mix([(1-t, U1), (t, UM)])
        expected_lower = Fraction(0)

    check_pairwise_uniform(lower, q, n)
    assert all_distinct_probability(lower) == expected_lower
    return expected_lower, Fraction(q-1, q)


if __name__ == '__main__':
    for q in range(2, 7):
        for n in range(2, q+1):
            lo, hi = verify(q, n)
            print(f'q={q} n={n}: all-distinct range endpoints verified: {lo} .. {hi}')
