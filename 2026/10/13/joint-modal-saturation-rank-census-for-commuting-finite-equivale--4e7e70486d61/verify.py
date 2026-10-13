#!/usr/bin/env python3
"""Exact integer recurrence and direct finite relational/modal checks.

Uses Python's standard library only. Run: python3 verify.py
"""
from collections import Counter
from math import comb, factorial


def stirling(n, k, memo={}):
    if (n, k) not in memo:
        if n == k == 0: v = 1
        elif k < 1 or k > n: v = 0
        else: v = stirling(n - 1, k - 1) + k * stirling(n - 1, k)
        memo[(n, k)] = v
    return memo[(n, k)]


def connected_count(n, r, s):
    return (factorial(r * s) * stirling(n, r * s) //
            (factorial(r) * factorial(s))) if r * s <= n else 0


def refined_counts(max_n):
    rows = [Counter({(0, 0, 0): 1})]
    for n in range(1, max_n + 1):
        out = Counter()
        for j in range(1, n + 1):
            choose = comb(n - 1, j - 1)
            for r in range(1, j + 1):
                for s in range(1, j // r + 1):
                    mult = choose * connected_count(j, r, s)
                    for (a, b, c), v in rows[n-j].items():
                        out[a+r, b+s, c+1] += mult * v
        rows.append(out)
    return rows


def partitions(n):
    if n == 0:
        yield ()
        return
    for p in partitions(n-1):
        yield p + ((n-1,),)
        for i in range(len(p)):
            yield p[:i] + (p[i] + (n-1,),) + p[i+1:]


def rows_of(p, n):
    q = [0] * n
    for i, block in enumerate(p):
        for x in block: q[x] = i
    return q


def commute_direct(r, s, n):
    R, S = rows_of(r, n), rows_of(s, n)
    hits = {(R[x], S[x]) for x in range(n)}
    return all(((R[x], S[y]) in hits) == ((R[y], S[x]) in hits)
               for x in range(n) for y in range(n))


def join_count(r, s, n):
    parent = list(range(n))
    def root(x):
        while parent[x] != x: x = parent[x]
        return x
    for b in r + s:
        for x in b[1:]: parent[root(x)] = root(b[0])
    return len({root(x) for x in range(n)})


def op(mask, blocks):
    return sum((sum(1 << a for a in block) for block in blocks
                if any(mask & (1 << a) for a in block)), 0)


def check():
    rows = refined_counts(9)
    known = [1,1,4,19,117,864,7459,73749,818960,10078023]
    assert [sum(v.values()) for v in rows] == known
    support_cases = 0
    for n in range(1, 10):
        for a in range(1, n+1):
            for b in range(1, n+1):
                for c in range(1, n+1):
                    feasible = (c <= min(a,b) and
                                n >= (a*b if c == 1 else a+b-c))
                    assert (rows[n][a,b,c] > 0) == feasible, (n,a,b,c)
                    support_cases += 1
    brute_pairs = 0
    modal_pairs = 0
    for n in range(1, 7):
        p = list(partitions(n))
        brute = Counter()
        for R in p:
            for S in p:
                does_commute = commute_direct(R, S, n)
                if does_commute:
                    c = join_count(R, S, n)
                    brute[len(R), len(S), c] += 1
                if n <= 4:
                    # independent Boolean-power-set operator check
                    fs = [op(op(m, S), R) for m in range(1 << n)]
                    gs = [op(op(m, R), S) for m in range(1 << n)]
                    algebra_commute = fs == gs
                    idempotent = all(fs[fs[m]] == fs[m] for m in range(1 << n))
                    assert algebra_commute == does_commute
                    assert idempotent == does_commute
                    if does_commute:
                        assert len(set(fs)) == 1 << join_count(R, S, n)
                    modal_pairs += 1
                brute_pairs += 1
        assert brute == rows[n], (n, brute - rows[n], rows[n] - brute)
    # Refined symmetry exchange of the two equivalences
    for row in rows:
        assert all(v == row[b, a, c] for (a, b, c), v in row.items())
    print('VERIFY_OK', 'n_to_6_pairs', brute_pairs,
          'direct_boolean_modal_pairs', modal_pairs,
          'support_tested', support_cases,
          'OEIS_totals_to_9', known,
          'n6_join', dict(sorted(Counter({c: sum(v for (a,b,d),v in rows[6].items() if d==c) for c in range(1,7)}).items())))

if __name__ == '__main__':
    check()
