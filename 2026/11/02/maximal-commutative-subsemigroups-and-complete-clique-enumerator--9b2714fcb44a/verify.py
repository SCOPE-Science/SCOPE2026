"""Independent finite checks for Brandt-semigroup commuting clique formulas.

Requires only the Python standard library. For small explicit groups it compares
semigroup multiplication with the proposed polynomial and maximal-clique formulas.
"""
from collections import Counter
from itertools import permutations
from math import comb, factorial


def cyclic(m):
    return list(range(m)), lambda a, b: (a + b) % m


def klein_four():
    H = [(0, 0), (1, 0), (0, 1), (1, 1)]
    return H, lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2)


def symmetric_three():
    group = list(permutations(range(3)))
    return group, lambda a, b: tuple(a[b[i]] for i in range(3))


def graph_cliques(vertices, product):
    N = len(vertices)
    adj = [0] * N
    for i, a in enumerate(vertices):
        for j, b in enumerate(vertices):
            if i != j and product(a, b) == product(b, a):
                adj[i] |= 1 << j
    counts = Counter()
    maximal = Counter()
    def visit(candidates, common, count):
        counts[count] += 1
        if count and not common:
            maximal[count] += 1
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            v = bit.bit_length() - 1
            visit(candidates & adj[v], common & adj[v], count + 1)
    visit((1 << N) - 1, (1 << N) - 1, 0)
    return counts, maximal


def group_cliques(H, mult):
    return graph_cliques(H, mult)


def brandt_cliques(n, H, mult):
    elements = [(i, g, j) for i in range(n) for g in H for j in range(n)]
    def prod(a, b):
        i, g, j = a
        k, h, l = b
        return (i, mult(g, h), l) if j == k else None
    return graph_cliques(elements, prod)


def add(a, b):
    c = Counter(a)
    for k, v in b.items():
        c[k] += v
    return c


def scale(a, m, shift=0):
    return Counter({k + shift: m * v for k, v in a.items() if m * v})


def mul(a, b):
    c = Counter()
    for k, u in a.items():
        for l, v in b.items():
            c[k + l] += u * v
    return c


def power(a, k):
    out = Counter({0: 1})
    for _ in range(k):
        out = mul(out, a)
    return out


def binomial_poly(exponent):
    return Counter({i: comb(exponent, i) for i in range(exponent + 1)})


def predictions(n, m, C, M):
    full = power(C, n)
    maximal = power(M, n)
    for s in range(1, n):
        for t in range(1, n - s + 1):
            u = n - s - t
            ways = factorial(n) // (factorial(u) * factorial(s) * factorial(t))
            support = Counter()
            for a in range(s + 1):
                for b in range(t + 1):
                    sign = (-1) ** (s + t - a - b)
                    mult = sign * comb(s, a) * comb(t, b)
                    support = add(support, scale(binomial_poly(m * a * b), mult))
            full = add(full, scale(mul(power(C, u), support), ways))
            maximal = add(maximal, scale(power(M, u), ways, m * s * t))
    return full, maximal


def strip_zeros(d):
    return {k: v for k, v in d.items() if v}


def run_case(name, n, H, mult):
    C, M = group_cliques(H, mult)
    direct, direct_max = brandt_cliques(n, H, mult)
    predicted, predicted_max = predictions(n, len(H), C, M)
    assert strip_zeros(direct) == strip_zeros(predicted), (name, n, 'cliques', direct, predicted)
    assert strip_zeros(direct_max) == strip_zeros(predicted_max), (name, n, 'maximal', direct_max, predicted_max)
    h = sum(M.values())
    expected_max = (h + 2) ** n - 2 * (h + 1) ** n + 2 * h ** n
    assert sum(direct_max.values()) == expected_max, (name, n, 'count')
    a = max(M)
    expected_size = max(n * a, len(H) * (n*n // 4))
    assert max(direct_max) == expected_size, (name, n, 'size')
    print('OK', name, 'n=', n, 'G=', len(H), 'vertices=', n*n*len(H),
          'all_cliques=', sum(direct.values()), 'maximal=', expected_max,
          'largest=', expected_size)


def main():
    cases = [(f'C{m}', n, *cyclic(m)) for m, n in
             [(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (3, 2)]]
    cases += [('C4', 2, *cyclic(4)), ('V4', 2, *klein_four()),
              ('S3', 2, *symmetric_three()), ('S3', 3, *symmetric_three())]
    for args in cases:
        run_case(*args)
    H1, op1 = cyclic(4)
    H2, op2 = klein_four()
    bijection = dict(zip(H1, H2))
    for i in range(2):
        for j in range(2):
            for g in H1:
                x = (i, g, j)
                X = (i, bijection[g], j)
                for k in range(2):
                    for l in range(2):
                        for h in H1:
                            y = (k, h, l)
                            Y = (k, bijection[h], l)
                            def product(u, v, op):
                                a, b, c = u
                                d, e, f = v
                                return (a, op(b, e), f) if c == d else None
                            assert (product(x, y, op1) == product(y, x, op1)) == (
                                product(X, Y, op2) == product(Y, X, op2))
    print('GRAPH_ISOMORPHISM_OK C4_vs_V4 n=2')
    print('VERIFY_OK', len(cases), 'independent finite multiplication checks')


if __name__ == '__main__':
    main()
