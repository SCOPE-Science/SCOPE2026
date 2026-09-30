#!/usr/bin/env python3
from itertools import combinations
from math import comb


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def vertices(parts):
    return [(i, j) for i, n in enumerate(parts) for j in range(n)]


def dist(u, v):
    if u == v:
        return 0
    return 1 if u[0] != v[0] else 2


def interval(u, v, V):
    d = dist(u, v)
    return {w for w in V if dist(u, w) + dist(w, v) == d}


def is_gp(S, V):
    S = set(S)
    for u, v in combinations(S, 2):
        if (interval(u, v, V) - {u, v}) & S:
            return False
    return True


def is_convex(C, V):
    C = set(C)
    for u, v in combinations(C, 2):
        if not interval(u, v, V) <= C:
            return False
    return True


def maximally_distant(u, v, V):
    duv = dist(u, v)
    for w in V:
        if dist(u, w) == 1 and dist(w, v) > duv:
            return False
    return True


def is_mmd(u, v, V):
    return maximally_distant(u, v, V) and maximally_distant(v, u, V)


def is_outer(S, V):
    return all(is_mmd(u, v, V) for u, v in combinations(S, 2))


def is_simplicial(u, V):
    N = [w for w in V if dist(u, w) == 1]
    return all(dist(a, b) == 1 for a, b in combinations(N, 2))


def is_total(S, V):
    return all(is_simplicial(u, V) for u in S)


def is_dual(S, V):
    S = set(S)
    return is_gp(S, V) and is_convex(set(V) - S, V)


def counts(S, parts):
    return [sum(1 for v in S if v[0] == i) for i in range(len(parts))]


def pred_gp(S, parts):
    c = counts(S, parts)
    return sum(x > 0 for x in c) <= 1 or all(x <= 1 for x in c)


def pred_outer(S, parts):
    if len(S) <= 1:
        return True
    c = counts(S, parts)
    return sum(x > 0 for x in c) <= 1 or all(parts[i] == 1 for i, x in enumerate(c) if x)


def pred_total(S, parts):
    p = sum(n >= 2 for n in parts)
    if p == 0:
        allowed = set(range(len(parts)))
    elif p == 1:
        allowed = {next(i for i, n in enumerate(parts) if n >= 2)}
    else:
        allowed = set()
    return all(v[0] in allowed for v in S)


def pred_dual(S, parts):
    if not S:
        return True
    c = counts(S, parts)
    M = max(parts)
    # A nonempty subset of one part works exactly when all other parts are singleton.
    for i, x in enumerate(c):
        if x and all(c[j] == 0 for j in range(len(parts)) if j != i):
            if all(parts[j] == 1 for j in range(len(parts)) if j != i):
                return True
    # If every part has size at most two, take exactly one vertex from every 2-part
    # and any subset of singleton parts.
    if M <= 2 and all(c[i] == 1 for i, n in enumerate(parts) if n == 2):
        return True
    return False


def add_binomial(poly, n, shift=0, scale=1):
    for k in range(n + 1):
        poly[k + shift] += scale * comb(n, k)


def predicted_polys(parts):
    N = sum(parts)
    s = sum(n == 1 for n in parts)
    p = sum(n >= 2 for n in parts)
    q = sum(n == 2 for n in parts)
    M = max(parts)

    po = [0] * (N + 1)
    po[0] = 1
    po[1] = N
    for n in parts:
        for k in range(2, n + 1):
            po[k] += comb(n, k)
    for k in range(2, s + 1):
        po[k] += comb(s, k)

    tau = N if p == 0 else (M if p == 1 else 0)
    pt = [0] * (N + 1)
    add_binomial(pt, tau)

    pd = [0] * (N + 1)
    if M == 1:
        add_binomial(pd, N)
    elif M == 2 and q == 1:
        add_binomial(pd, 2)
        for k in range(1, s + 1):
            pd[k + 1] += 2 * comb(s, k)
    elif M == 2 and q >= 2:
        pd[0] = 1
        for k in range(s + 1):
            pd[q + k] += (2 ** q) * comb(s, k)
    elif M >= 3 and p == 1:
        add_binomial(pd, M)
    else:
        pd[0] = 1
    return po, pt, pd


def main():
    type_count = subset_count = property_checks = polynomial_checks = 0
    for N in range(2, 9):
        for parts in partitions(N):
            if len(parts) < 2:
                continue
            type_count += 1
            V = vertices(parts)
            actual_o = [0] * (N + 1)
            actual_t = [0] * (N + 1)
            actual_d = [0] * (N + 1)
            for mask in range(1 << N):
                S = {V[j] for j in range(N) if (mask >> j) & 1}
                subset_count += 1
                checks = [
                    (is_gp(S, V), pred_gp(S, parts), 'gp'),
                    (is_outer(S, V), pred_outer(S, parts), 'outer'),
                    (is_total(S, V), pred_total(S, parts), 'total'),
                    (is_dual(S, V), pred_dual(S, parts), 'dual'),
                ]
                for actual, predicted, name in checks:
                    property_checks += 1
                    if actual != predicted:
                        raise AssertionError((parts, sorted(S), name, actual, predicted))
                actual_o[len(S)] += is_outer(S, V)
                actual_t[len(S)] += is_total(S, V)
                actual_d[len(S)] += is_dual(S, V)
            expected = predicted_polys(parts)
            for name, actual, exp in zip(('outer', 'total', 'dual'), (actual_o, actual_t, actual_d), expected):
                polynomial_checks += 1
                if actual != exp:
                    raise AssertionError((parts, name, actual, exp))
    print(f'VERIFY_OK types={type_count} subsets={subset_count} property_checks={property_checks} polynomial_checks={polynomial_checks}')


if __name__ == '__main__':
    main()
