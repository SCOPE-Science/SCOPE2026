#!/usr/bin/env python3
"""Independent exact checker for the cycle-prism total-domination polynomial.

Requires only Python's standard library. All arithmetic is over Z[z].
"""
from collections import defaultdict
from itertools import product
from math import factorial


def add(p, q):
    r = p.copy()
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
        if r[k] == 0:
            del r[k]
    return r


def neg(p):
    return {k: -v for k, v in p.items()}


def mul(p, q):
    r = defaultdict(int)
    for i, a in p.items():
        for j, b in q.items():
            r[i + j] += a * b
    return {k: v for k, v in r.items() if v}


def poly_tmul(p, q):
    out = [{} for _ in range(len(p) + len(q) - 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] = add(out[i+j], mul(a, b))
    return out


def transfer_traces(limit):
    states = [(a, b) for a in range(4) for b in range(4)]
    where = {st: k for k, st in enumerate(states)}
    arcs = []
    for a, b in states:
        opts = []
        for c in range(4):
            if all(((a >> rail) & 1) or ((b >> (1-rail)) & 1)
                   or ((c >> rail) & 1) for rail in (0, 1)):
                opts.append((where[(b, c)], b.bit_count()))
        arcs.append(opts)
    traces = [None] + [{} for _ in range(limit)]
    for start in range(16):
        active = {start: {0: 1}}
        for step in range(1, limit + 1):
            nxt = {}
            for state, p in active.items():
                for dest, weight in arcs[state]:
                    old = nxt.setdefault(dest, {})
                    for exponent, coeff in p.items():
                        degree = exponent + weight
                        old[degree] = old.get(degree, 0) + coeff
            active = nxt
            traces[step] = add(traces[step], active.get(start, {}))
    return traces, sum(len(a) for a in arcs)


def determinant_by_newton(traces, degree):
    # det(I-tW) = sum e_k t^k; k e_k = -sum_{i=1}^k e_{k-i} tr(W^i).
    es = [{0: 1}]
    for k in range(1, degree + 1):
        numerator = {}
        for i in range(1, k + 1):
            numerator = add(numerator, mul(es[k-i], traces[i]))
        assert all(c % k == 0 for c in numerator.values()), (k, numerator)
        es.append({exp: -co // k for exp, co in numerator.items() if co})
    return es


def cycle_traces(limit):
    """Independently count ordinary dominating sets of cycles by forbidden 000."""
    states = [(a, b) for a in (0, 1) for b in (0, 1)]
    index = {x: i for i, x in enumerate(states)}
    arcs = [[] for _ in states]
    for i, (a, b) in enumerate(states):
        for c in (0, 1):
            if a or b or c:
                arcs[i].append((index[(b, c)], b))
    result = [None] + [{} for _ in range(limit)]
    for start in range(4):
        active = {start: {0: 1}}
        for k in range(1, limit+1):
            nxt = {}
            for state, poly in active.items():
                for dest, deg in arcs[state]:
                    into = nxt.setdefault(dest, {})
                    for exp, co in poly.items():
                        into[exp+deg] = into.get(exp+deg, 0) + co
            active = nxt
            result[k] = add(result[k], active.get(start, {}))
    return result


def cycle_closed_formula(m):
    """Newton's logarithmic formula for 1-z(t+t^2+t^3)."""
    ans = defaultdict(int)
    for a in range(m+1):
        for b in range((m-a)//2+1):
            rem = m-a-2*b
            if rem % 3:
                continue
            c = rem//3
            parts = a+b+c
            if not parts:
                continue
            numerator = m*factorial(parts-1)
            denominator = factorial(a)*factorial(b)*factorial(c)
            assert numerator % denominator == 0
            ans[parts] += numerator//denominator
    return dict(ans)


def full_brute(n):
    N = 2*n
    nb = []
    for rung in range(n):
        for rail in range(2):
            nb.append((1 << (2*((rung-1)%n)+rail)) |
                      (1 << (2*((rung+1)%n)+rail)) |
                      (1 << (2*rung+1-rail)))
    count = [0]*(N+1)
    for subset in range(1<<N):
        if all(subset & mask for mask in nb):
            count[subset.bit_count()] += 1
    return {i: c for i, c in enumerate(count) if c}


def oeis_minimum(n):
    res = n % 6
    size = (2*n+2)//3 + (res == 4)
    if res == 0:
        count = 9
    elif res == 1:
        count = 2*n
    elif res == 2:
        count = n*n
    elif res == 3:
        count = 3
    elif res == 4:
        count = (n*(n+5)//6)**2
    else:
        count = n*(2*n+5)//3
    return size, count


def main():
    traces, arcs = transfer_traces(60)
    determinant = determinant_by_newton(traces, 16)
    A = [{0:1}, {1:1}, {2:1}, {2:-1}]
    B = [{0:1}, {1:-1}, {2:1}, {2:1}]
    C = [{0:1}, {1:-2, 2:-1}, {2:-1}, {2:-1}]
    claimed = poly_tmul(poly_tmul(A, B), C)
    claimed += [{} for _ in range(17-len(claimed))]
    assert determinant == claimed, ('factorization', determinant, claimed)
    assert traces[1] == {1:2, 2:1}
    assert traces[2] == {2:4, 3:4, 4:1}
    cycles = cycle_traces(120)
    for m in range(3, 121):
        assert cycles[m] == cycle_closed_formula(m), ('cycle closed sum', m)
    for n in range(3, 61):
        equivalent = cycles[2*n] if n % 2 else mul(cycles[n], cycles[n])
        assert traces[n] == equivalent, ('parity identity', n)
    brute_total = 0
    for n in range(3, 11):
        brute = full_brute(n)
        assert brute == traces[n], (n, brute, traces[n])
        brute_total += 1 << (2*n)
    # Independent published scalar totals (OEIS A296102), orders 3..12.
    totals = [39,121,443,1521,5071,17161,58035,196249,664183,2247001]
    for n, total in enumerate(totals, start=3):
        assert sum(traces[n].values()) == total, (n, total)
    # Published minimum size/count (OEIS A302405 and A303053), orders 3..60.
    for n in range(3, 61):
        degree = min(traces[n])
        expected_degree, expected_count = oeis_minimum(n)
        assert degree == expected_degree, (n, degree, expected_degree)
        assert traces[n][degree] == expected_count, (n, traces[n][degree], expected_count)
        assert max(traces[n]) == 2*n and traces[n][2*n] == 1
    print('VERIFY_OK transfer_states=16 arcs=%d exact_determinant_newton_orders=1..16 '
          'cycle_parity_identity_n=3..60 cycle_closed_formula=3..120 '
          'brute_n=3..10 masks=%d all_coefficients=equal published_ungraded=3..12 '
          'published_minima=3..60' % (arcs, brute_total))


if __name__ == '__main__':
    main()
