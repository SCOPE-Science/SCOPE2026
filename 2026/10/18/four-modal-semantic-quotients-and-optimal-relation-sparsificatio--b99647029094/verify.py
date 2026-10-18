#!/usr/bin/env python3
"""Independent finite checks for four intuitionistic modalities on chains.

No external dependencies. Run: python3 verify_four_modal_chains.py
"""
from itertools import product, combinations_with_replacement

EXPECTED = {1: 2, 2: 16, 3: 279, 4: 7171, 5: 235152}


def row_profiles(rows, n):
    low = [n if not row else min(row) for row in rows]
    high = [-1 if not row else max(row) for row in rows]
    p, e = [], []
    a, b = -1, -1
    for h, l in zip(high, low):
        a = max(a, h); b = max(b, l)
        p.append(a); e.append(b)
    q, d = [None] * n, [None] * n
    a, b = n, n
    for i in range(n - 1, -1, -1):
        a = min(a, high[i]); b = min(b, low[i])
        q[i] = a; d[i] = b
    return tuple(p), tuple(q), tuple(e), tuple(d)


def operators_direct(rows, n):
    """Four independent truth tables, each with n+1 input upsets."""
    ts = []
    for j in range(n + 1):
        up = set(range(j, n))
        P, Q, E, D = [], [], [], []
        for s in range(n):
            P.append(any(not rows[t].isdisjoint(up) for t in range(s + 1)))
            Q.append(all(not rows[t].isdisjoint(up) for t in range(s, n)))
            E.append(any(rows[t].issubset(up) for t in range(s + 1)))
            D.append(all(rows[t].issubset(up) for t in range(s, n)))
        ts.append((tuple(P), tuple(Q), tuple(E), tuple(D)))
    return tuple(ts)


def operators_from_profiles(profiles, n):
    p, q, e, d = profiles
    return tuple((tuple(v >= j for v in p),
                  tuple(v >= j for v in q),
                  tuple(v >= j for v in e),
                  tuple(v >= j for v in d))
                 for j in range(n + 1))


def admissible_candidates(profiles, n):
    p, q, e, d = profiles
    if not all(all(s[i] <= s[i + 1] for i in range(n - 1))
               for s in profiles):
        return None
    if any(x < -1 or x >= n for x in p + q):
        return None
    if any(x < 0 or x > n for x in e + d):
        return None
    choices = []
    for i in range(n):
        high = [h for h in range(-1, n)
                if q[i] <= h <= p[i]
                and (i != 0 and p[i] == p[i - 1] or h == p[i])
                and (i != n - 1 and q[i] == q[i + 1] or h == q[i])]
        low = [l for l in range(n + 1)
               if d[i] <= l <= e[i]
               and (i != 0 and e[i] == e[i - 1] or l == e[i])
               and (i != n - 1 and d[i] == d[i + 1] or l == d[i])]
        pairs = [(l, h) for l in low for h in high
                 if (l == n and h == -1) or (0 <= l <= h < n)]
        if not pairs:
            return None
        choices.append(pairs)
    return choices


def edges(pair):
    low, high = pair
    return 0 if low == n_global else (1 if low == high else 2)


def endpoint_relation(pair):
    l, h = pair
    return frozenset() if l == n_global else frozenset((l, h))


def endpoint_enumeration(n):
    opts = [(n, -1)] + [(l, h) for l in range(n) for h in range(l, n)]
    cls_min = {}
    for rowpairs in product(opts, repeat=n):
        rows = tuple(frozenset() if l == n else frozenset((l, h))
                     for l, h in rowpairs)
        key = row_profiles(rows, n)
        cost = sum(0 if l == n else (1 if l == h else 2)
                   for l, h in rowpairs)
        if key not in cls_min or cost < cls_min[key]:
            cls_min[key] = cost
    return cls_min


def all_raw_relations(n):
    for mask in range(1 << (n * n)):
        yield tuple(frozenset(j for j in range(n)
                              if mask & (1 << (i * n + j)))
                    for i in range(n))


def test_n(n):
    endpoint = endpoint_enumeration(n)
    assert len(endpoint) == EXPECTED[n], (n, len(endpoint))
    # The bound 2n is attained by rows with both extreme endpoints.
    if n >= 2:
        k = row_profiles(tuple(frozenset((0, n - 1)) for _ in range(n)), n)
        assert endpoint[k] == 2 * n
    if n <= 4:
        raw_min = {}
        sig_to_key = {}
        for rows in all_raw_relations(n):
            key = row_profiles(rows, n)
            sig = operators_direct(rows, n)
            assert sig == operators_from_profiles(key, n)
            if sig in sig_to_key:
                assert sig_to_key[sig] == key
            else:
                sig_to_key[sig] = key
            c = sum(len(r) for r in rows)
            if key not in raw_min or c < raw_min[key]:
                raw_min[key] = c
        assert raw_min == endpoint
        assert len(sig_to_key) == len(endpoint)
    # A separate exhaustive converse test for the four monotone profiles.
    if n <= 3:
        maxseq = list(combinations_with_replacement(range(-1, n), n))
        minseq = list(combinations_with_replacement(range(0, n + 1), n))
        accepted = set()
        for p in maxseq:
            for q in maxseq:
                for e in minseq:
                    for d in minseq:
                        key = (p, q, e, d)
                        choices = admissible_candidates(key, n)
                        if choices is None:
                            assert key not in endpoint
                            continue
                        accepted.add(key)
                        witness = tuple(endpoint_relation(min(
                            candidates,
                            key=lambda pair: (0 if pair[0] == n else
                                              1 if pair[0] == pair[1] else 2,
                                              pair)))
                            for candidates in choices)
                        assert row_profiles(witness, n) == key
                        cost = sum(min(0 if l == n else 1 if l == h else 2
                                       for l, h in candidates)
                                   for candidates in choices)
                        assert endpoint[key] == cost
        assert len(accepted) == len(endpoint)
    print('n=%d classes=%d maximal_edge_minimum=%d%s' %
          (n, len(endpoint), max(endpoint.values()),
           ' raw_and_profile_checks=OK' if n <= 4 else ' endpoint_checks=OK'))


if __name__ == '__main__':
    for n_global in range(1, 6):
        test_n(n_global)
    print('VERIFY_OK')
