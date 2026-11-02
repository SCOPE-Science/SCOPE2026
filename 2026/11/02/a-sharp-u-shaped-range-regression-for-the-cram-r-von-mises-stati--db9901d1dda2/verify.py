"""Exact rational replay for the joint range--Cramer--von Mises moment law.

No stochastic simulations or nonstandard dependencies are used.
Run: python3 verify.py
"""
from fractions import Fraction as Q
from math import factorial


def const(dim, value):
    return {(0,) * dim: Q(value)}


def add(*terms):
    out = {}
    for p in terms:
        for e, c in p.items():
            out[e] = out.get(e, Q(0)) + c
    return {e: c for e, c in out.items() if c}


def scale(p, z):
    z = Q(z)
    return {e: c*z for e, c in p.items() if c*z}


def mul(p, q):
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            k = tuple(x + y for x, y in zip(e, f))
            out[k] = out.get(k, Q(0)) + a*b
    return {e: c for e, c in out.items() if c}


def variable(dim, j):
    return {tuple(int(i == j) for i in range(dim)): Q(1)}


def dirichlet_mean(p):
    """Exact integral over uniform Dirichlet(1,...,1) spacings."""
    answer = Q(0)
    for exponents, coefficient in p.items():
        d = len(exponents)
        k = sum(exponents)
        moment = Q(factorial(d - 1), factorial(d - 1 + k))
        for e in exponents:
            moment *= factorial(e)
        answer += coefficient * moment
    return answer


def statistic_for_ordered(ordered):
    dim = len(next(iter(ordered[0].keys())))
    n = len(ordered)
    stat = const(dim, Q(1, 12*n))
    for i, point in enumerate(ordered, 1):
        deviation = add(point, const(dim, -Q(2*i - 1, 2*n)))
        stat = add(stat, mul(deviation, deviation))
    return stat


def unconditional_test(n):
    # Each of n+1 uniform gaps has Dirichlet(1,...,1) law.
    d = n + 1
    gap = [variable(d, j) for j in range(d)]
    ordered = [add(*gap[:i]) for i in range(1, n + 1)]
    stat = statistic_for_ordered(ordered)
    width = add(*gap[1:n])
    ew = dirichlet_mean(stat)
    er = dirichlet_mean(width)
    cov = dirichlet_mean(mul(stat, width)) - er*ew
    var = dirichlet_mean(mul(stat, stat)) - ew*ew
    assert ew == Q(1, 6), (n, ew)
    assert er == Q(n - 1, n + 1), (n, er)
    assert cov == -Q(n-1, (n+1)*(n+2)*(n+3)), (n, cov)
    assert var == Q(4*n-3, 180*n), (n, var)
    print('unconditional size', n, 'E[W]=', ew, 'cov=', cov, 'var=', var)
    return 4


def conditional_test(n, a, r):
    # With min=a and max=a+r, the n-1 normalized interior spacings
    # form a uniform Dirichlet vector; no normal approximations.
    d = n-1
    gaps = [variable(d, j) for j in range(d)]
    ordered = [const(d, a)]
    for i in range(1, n):
        ordered.append(add(const(d, a), scale(add(*gaps[:i]), r)))
    stat = statistic_for_ordered(ordered)
    answer = dirichlet_mean(stat)
    target = n*(a*a+a*(r-1)+(1-r)**2/Q(3))+(r*r)/3-r/Q(6)
    assert answer == target, (n, a, r, answer, target)
    print('conditional size', n, 'min=', a, 'range=', r, 'E[W]=', answer)
    return 1


def main():
    checks = 0
    for n in range(2, 8):
        checks += unconditional_test(n)
        for a, r in [(Q(0), Q(1)), (Q(1, 7), Q(2, 7)),
                     (Q(1, 9), Q(5, 9)), (Q(0), Q(1, 3))]:
            checks += conditional_test(n, a, r)
    print('PASS:', checks, 'independent exact-rational identities')


if __name__ == '__main__':
    main()
