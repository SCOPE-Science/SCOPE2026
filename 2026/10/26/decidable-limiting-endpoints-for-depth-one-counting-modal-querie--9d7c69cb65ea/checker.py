"""Independent finite checks for a shallow counting-modal convergence theorem.

Run with Python >=3.10. This checker exhaustively compares full graph
semantics with the exact root-row multinomial census, for small sizes.
It also checks the covariance and irrational-limit example numerically.
"""
from fractions import Fraction
from itertools import product
from math import factorial, asin, pi, sqrt

K = 2
Q = 1 << K


def P(j):
    return ('p', j)


def neg(f):
    return ('not', f)


def dis(f, g):
    return ('or', f, g)


def con(f, g):
    return neg(dis(neg(f), neg(g)))


def T():
    return dis(P(0), neg(P(0)))


def c(x):
    return ('c', x)


def indicator(f):
    return ('ind', f)


def cnt(f):
    return ('count', f)


def add(x, y):
    return ('add', x, y)


def mul(i, x):
    return ('mul', i, x)


def ge(x):
    return ('ge', x)


def eval_formula(f, vertex, vals, edges):
    tag = f[0]
    if tag == 'p':
        return bool(vals[vertex] & (1 << f[1]))
    if tag == 'not':
        return not eval_formula(f[1], vertex, vals, edges)
    if tag == 'or':
        return eval_formula(f[1], vertex, vals, edges) or eval_formula(f[2], vertex, vals, edges)
    if tag == 'ge':
        return eval_term(f[1], vertex, vals, edges) >= 0
    raise ValueError(tag)


def eval_term(e, vertex, vals, edges):
    tag = e[0]
    if tag == 'c':
        return e[1]
    if tag == 'ind':
        return int(eval_formula(e[1], vertex, vals, edges))
    if tag == 'count':
        return sum(eval_formula(e[1], j, vals, edges) for j in range(len(vals)) if edges[vertex][j])
    if tag == 'add':
        return eval_term(e[1], vertex, vals, edges) + eval_term(e[2], vertex, vals, edges)
    if tag == 'mul':
        return e[1] * eval_term(e[2], vertex, vals, edges)
    raise ValueError(tag)


def brute_row_true(n, formula):
    total = 0
    # Exactly 2^(3n) possibilities for the root's adjacency row and all
    # n propositional 2-bit valuations, each corresponding to 2^(n^2-n)
    # full graph models. Other graph edges are irrelevant at depth one.
    for vs in product(range(Q), repeat=n):
        for row in product(range(2), repeat=n):
            edges = [tuple(row)] + [tuple([0] * n) for _ in range(n-1)]
            total += eval_formula(formula, 0, vs, edges)
    return total


def compositions(k, upper):
    if k == 0:
        yield ()
    elif k == 1:
        for j in range(upper+1):
            yield (j,)
    else:
        for j in range(upper+1):
            for rem in compositions(k-1, upper-j):
                yield (j,)+rem


def multinomial_root_true(n, formula):
    total = 0
    for type_root in range(Q):
        for self_loop in (0, 1):
            for m in compositions(Q, n-1):
                z = n-1 - sum(m)
                weight = factorial(n-1) // (factorial(z) * __import__('math').prod(factorial(x) for x in m))
                weight *= Q ** z  # absent edges allow each of Q marks
                vals = [type_root]
                row = [self_loop]
                for s, num in enumerate(m):
                    vals.extend([s] * num)
                    row.extend([1] * num)
                vals.extend([0] * z)
                row.extend([0] * z)
                edges = [tuple(row)] + [tuple([0] * n) for _ in range(n-1)]
                total += weight * int(eval_formula(formula, 0, vals, edges))
    return total


def main():
    theta = con(ge(add(mul(2, cnt(P(0))), mul(-1, cnt(T())))),
                ge(add(mul(4, cnt(con(P(0), P(1)))), mul(-1, cnt(T())))))
    indicator_nested = ge(add(indicator(ge(add(cnt(P(0)), mul(-1, cnt(P(1)))))),
                              mul(-1, indicator(con(P(0), ge(add(cnt(T()), c(-2))))))))
    another = dis(con(P(1), ge(add(cnt(con(P(0), neg(P(1)))), mul(-1, cnt(P(0)))))),
                  neg(ge(add(mul(2, cnt(con(P(0), P(1)))), c(-1)))))
    formulas = [('theta', theta), ('indicator_nested', indicator_nested),
                ('mixed', another)]
    for n in (1,2,3,4,5):
        for name, f in formulas:
            b = brute_row_true(n, f)
            m = multinomial_root_true(n, f)
            assert b == m, (name, n, b, m)
            assert 0 <= b <= 8**n
            print(f'EXACT_ROWS n={n} formula={name} true={b} total={8**n}')
    # A second direct enumeration includes every edge of the entire graph,
    # not only edges from the distinguished root, for n<=3.
    for n in (1,2,3):
        b = 0
        for vs in product(range(Q), repeat=n):
            for flat_edges in product((0, 1), repeat=n*n):
                edges = [tuple(flat_edges[i*n:(i+1)*n]) for i in range(n)]
                b += eval_formula(theta, 0, vs, edges)
        expected = multinomial_root_true(n, theta) * (2**(n*n-n))
        assert b == expected, (n, b, expected)
        print(f'EXACT_GRAPHS n={n} true={b} total={2**(n*n+K*n)}')
    # For each nonroot vertex: A=e(2p-1), B=e(4pq-1).
    support = []
    for edge in (0,1):
        for p in (0,1):
            for q in (0,1):
                support.append((edge * (2*p-1), edge * (4*p*q-1)))
    means = [Fraction(sum(x[i] for x in support), 8) for i in (0,1)]
    cov = [[Fraction(sum(x[i]*x[j] for x in support), 8) - means[i]*means[j]
            for j in (0,1)] for i in (0,1)]
    assert means == [0,0], means
    assert cov == [[Fraction(1,2),Fraction(1,2)],
                   [Fraction(1,2),Fraction(3,2)]], cov
    rho = float(cov[0][1]) / sqrt(float(cov[0][0] * cov[1][1]))
    ans = 0.25 + asin(rho)/(2*pi)
    assert abs(rho - 1/sqrt(3)) < 1e-14
    assert 0.34 < ans < 0.36
    print('EXACT_COVARIANCE', cov)
    print(f'GAUSSIAN_LIMIT {ans:.15f}')
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
