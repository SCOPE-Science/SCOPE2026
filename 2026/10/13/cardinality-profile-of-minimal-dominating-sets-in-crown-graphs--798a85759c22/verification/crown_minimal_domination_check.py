from itertools import combinations
from math import comb
from collections import Counter

def vertices(n):
    return tuple([('a', i) for i in range(n)] + [('b', i) for i in range(n)])

def adjacent(u, v):
    return u[0] != v[0] and u[1] != v[1]

def dominates(S, V):
    S = set(S)
    return all(v in S or any(adjacent(v, u) for u in S) for v in V)

def is_minimal_dominating(S, V):
    S = set(S)
    return dominates(S, V) and all(not dominates(S - {x}, V) for x in S)

def classified(S, n):
    S = set(S)
    P = {i for side, i in S if side == 'a'}
    Q = {i for side, i in S if side == 'b'}
    U = set(range(n))
    return (
        (P == U and not Q)
        or (Q == U and not P)
        or (len(P) == len(Q) == 1 and P == Q)
        or (len(P) == len(Q) == 2 and P.isdisjoint(Q))
    )

subset_checks = 0
minimal_checks = 0
classification_checks = 0
coefficient_checks = 0
for n in range(3, 10):
    V = vertices(n)
    actual = []
    for r in range(1, 2*n + 1):
        for S in combinations(V, r):
            subset_checks += 1
            md = is_minimal_dominating(S, V)
            cl = classified(S, n)
            classification_checks += 1
            if md != cl:
                raise AssertionError((n, S, md, cl))
            if md:
                minimal_checks += 1
                actual.append(S)
    coeff = Counter(map(len, actual))
    expected = Counter({2: n, n: 2})
    c4 = comb(n, 2) * comb(n-2, 2)
    if c4:
        expected[4] += c4
    if coeff != expected:
        raise AssertionError((n, coeff, expected))
    coefficient_checks += len(set(coeff) | set(expected))
    total = n + 2 + 6*comb(n, 4)
    oeis_formula = (n**4 - 6*n**3 + 11*n**2 - 2*n + 8)//4
    if len(actual) != total or total != oeis_formula:
        raise AssertionError((n, len(actual), total, oeis_formula))
    if max(coeff) != n:
        raise AssertionError((n, max(coeff)))
print(
    'VERIFY_OK',
    f'n_range=3..9',
    f'subset_checks={subset_checks}',
    f'minimal_checks={minimal_checks}',
    f'classification_checks={classification_checks}',
    f'coefficient_checks={coefficient_checks}',
    'enumerator=n*x^2+6*C(n,4)*x^4+2*x^n',
    'upper_domination=n',
    'oeis_total_match=A289121',
    f'max_order={18}',
)
