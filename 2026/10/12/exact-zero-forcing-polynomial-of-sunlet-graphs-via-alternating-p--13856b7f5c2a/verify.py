#!/usr/bin/env python3
"""Independent finite checks for the zero-forcing polynomial of a sunlet graph."""
from collections import Counter
from math import comb


def add(a, b, scale=1):
    ans = list(a) + [0] * max(0, len(b) - len(a))
    for i, x in enumerate(b):
        ans[i] += scale * x
    return ans


def mul(a, b):
    ans = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i + j] += x * y
    return ans


def powpoly(a, n):
    ans = [1]
    for _ in range(n):
        ans = mul(ans, a)
    return ans


def polynomial_formula(n):
    assert n >= 3
    a = [0, 2, 1]
    bb = [0, 2, 2]
    cc = [0, 0, 1, 2, 1]
    ss = {
        1: a,
        2: add(mul(a, a), bb, 2),
        3: add(add(mul(mul(a, a), a), mul(a, bb), 3), cc, -3),
    }
    for i in range(4, n + 1):
        ss[i] = add(add(mul(a, ss[i - 1]), mul(bb, ss[i - 2])), mul(cc, ss[i - 3]), -1)
    ret = ss[n]
    if n % 2 == 0:
        ret = add(ret, powpoly([0, 1, 1], n // 2), -4)
    return ret + [0] * max(0, 2 * n + 1 - len(ret))


def forcing(n, mask):
    full = (1 << (2 * n)) - 1
    adj = [((1 << ((i-1) % n)) | (1 << ((i+1) % n)) | (1 << (n+i))) for i in range(n)]
    adj.extend([1 << i for i in range(n)])
    cur = mask
    while cur != full:
        nxt = cur
        for i, neighbors in enumerate(adj):
            if not (cur >> i) & 1:
                continue
            uncolored = neighbors & ~cur
            if uncolored and not(uncolored & (uncolored - 1)):
                nxt |= uncolored
        if nxt == cur:
            return False
        cur = nxt
    return True


def static_criterion(n, mask):
    active = {i for i in range(n) if mask & (1 << (n+i))}
    white_center = {i for i in range(n) if not mask & (1 << i) and i not in active}
    seen = set()
    for initial in white_center:
        if initial in seen:
            continue
        component = {initial}
        todo = [initial]
        for x in todo:
            for y in ((x-1) % n, (x+1) % n):
                if ((x in active and y in white_center) or (x in white_center and y in active)) and y not in component:
                    component.add(y)
                    todo.append(y)
        seen |= component
        if not any(i in active and sum(j in white_center for j in ((i-1) % n, (i+1) % n)) == 1 for i in component):
            return False
    return True


def transfer_polynomial(n):
    # States: C, good-B, good-E, unfinished-E, unfinished-B.
    # Each transition carries the weight of the newly read pair-state.
    transitions = [
        [(0, [0,1]), (1, [0,1,1]), (3, [1])],
        [(0, [0,1]), (1, [0,1,1]), (2, [1])],
        [(0, [0,1]), (1, [0,1,1]), (3, [1])],
        [(4, [0,1,1])],
        [(0, [0,1]), (1, [0,1,1]), (3, [1])],
    ]
    result = [0]
    for start in range(5):
        dp = {start: [1]}
        for _ in range(n):
            nd = {}
            for st, pp in dp.items():
                for nxt, ww in transitions[st]:
                    nd[nxt] = add(nd.get(nxt, [0]), mul(pp, ww))
            dp = nd
        result = add(result, dp.get(start, [0]))
    if n % 2 == 0:
        result = add(result, powpoly([0,1,1], n//2), -4)
    return result


def verify():
    cases = 0
    checked = 0
    for n in range(3, 11):
        counts = Counter()
        for mask in range(1 << (2*n)):
            f = forcing(n, mask)
            c = static_criterion(n, mask)
            assert f == c, (n, mask, 'static')
            if f:
                counts[mask.bit_count()] += 1
            checked += 1
        expected = polynomial_formula(n)
        got = transfer_polynomial(n)
        for k in range(2*n+1):
            assert counts[k] == (expected[k] if k < len(expected) else 0), (n,k,'recurrence')
            assert counts[k] == (got[k] if k < len(got) else 0), (n,k,'matrix')
        assert sum(counts.values()) == sum(expected), n
        cases += 1
    for n in range(3, 41):
        pp = polynomial_formula(n)
        degree = next(k for k,v in enumerate(pp) if v)
        minimum = (n+1)//2
        expected = 4*(2**(n//2-1)-1) if n % 2 == 0 else 3*n*2**((n-3)//2)
        assert degree == minimum, (n,degree,minimum)
        assert pp[degree] == expected, (n,pp[degree],expected)
    print('VERIFY_OK graph_orders=3..10 exhaustive_initial_sets=',checked,
          'static_and_matrix_and_recurrence=passed minimum_counts=3..40')

if __name__ == '__main__':
    verify()
