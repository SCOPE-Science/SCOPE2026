#!/usr/bin/env python3
"""Exact verifier for the small complete-bipartite G-CFF claim.

For K_{a,b}, a row is a binary pattern on a+b columns.  The G-CFF conditions are
converted exactly into witness requirements: for each edge uv we require rows
u=1,v=0 and v=1,u=0 (Sperner incomparability), and for every third vertex w we
require a row w=1,u=v=0 (the union of the edge blocks does not cover block w).
Thus the minimum ground-set size is the minimum number of row patterns covering
all requirements.  The search below exhausts all 2^(a+b) patterns with exact
integer bitsets, domination pruning, memoization, and complete branching.
"""


def instance(a, b):
    n = a + b
    left = tuple(range(a))
    right = tuple(range(a, n))
    req = []
    for u in left:
        for v in right:
            req.append(("sep", u, v))
            req.append(("sep", v, u))
            for w in range(n):
                if w not in (u, v):
                    req.append(("triple", w, u, v))
    assert len(req) == len(set(req))
    req = tuple(req)
    full = (1 << len(req)) - 1

    def covers(p, r):
        bit = lambda i: (p >> i) & 1
        if r[0] == "sep":
            _, x, y = r
            return bit(x) == 1 and bit(y) == 0
        _, w, u, v = r
        return bit(w) == 1 and bit(u) == 0 and bit(v) == 0

    cover = []
    for p in range(1 << n):
        m = 0
        for i, r in enumerate(req):
            if covers(p, r):
                m |= 1 << i
        cover.append(m)
    cover = tuple(cover)

    raw = [p for p in range(1 << n) if cover[p]]
    maximal = []
    for p in raw:
        cp = cover[p]
        if not any(
            p != q and cp != cover[q] and (cp | cover[q]) == cover[q]
            for q in raw
        ):
            maximal.append(p)
    rep = {}
    for p in maximal:
        rep.setdefault(cover[p], p)
    patterns = tuple(rep.values())

    by_req = [[] for _ in req]
    for p in patterns:
        for i in range(len(req)):
            if (cover[p] >> i) & 1:
                by_req[i].append(p)

    def search(k):
        memo = set()
        nodes = 0

        def dfs(done, remaining):
            nonlocal nodes
            nodes += 1
            if done == full:
                return ()
            if remaining == 0:
                return None
            key = (done, remaining)
            if key in memo:
                return None
            unseen = full ^ done
            max_new = max((cover[p] & unseen).bit_count() for p in patterns)
            if max_new * remaining < unseen.bit_count():
                memo.add(key)
                return None
            best = None
            m = unseen
            while m:
                lsb = m & -m
                i = lsb.bit_length() - 1
                m -= lsb
                opts = [p for p in by_req[i] if cover[p] & unseen]
                if best is None or len(opts) < len(best):
                    best = opts
            best.sort(key=lambda p: (cover[p] & unseen).bit_count(), reverse=True)
            for p in best:
                nxt = done | cover[p]
                if nxt == done:
                    continue
                tail = dfs(nxt, remaining - 1)
                if tail is not None:
                    return (p,) + tail
            memo.add(key)
            return None

        ans = dfs(0, k)
        return ans, nodes, len(memo)

    return n, req, cover, patterns, search


def columns_from_rows(rows, n):
    return tuple(
        tuple(i + 1 for i, row in enumerate(rows) if (row >> v) & 1)
        for v in range(n)
    )


def direct_check(a, b, columns):
    n = a + b
    sets = [set(c) for c in columns]
    assert len(columns) == n and len(set(columns)) == n
    for u in range(a):
        for v in range(a, n):
            U, V = sets[u], sets[v]
            assert not (U <= V) and not (V <= U)
            UV = U | V
            for w in range(n):
                if w not in (u, v):
                    assert not (sets[w] <= UV)


def exact_value(a, b, expected):
    n, req, cover, patterns, search = instance(a, b)
    below, nodes_below, memo_below = search(expected - 1)
    assert below is None
    at, nodes_at, memo_at = search(expected)
    assert at is not None and len(at) <= expected
    direct_check(a, b, columns_from_rows(at, n))
    return {
        "requirements": len(req),
        "patterns": len(patterns),
        "nodes_below": nodes_below,
        "memo_below": memo_below,
        "nodes_at": nodes_at,
        "memo_at": memo_at,
    }


# All complete bipartite graphs with both parts >=2 and total order <7.
small = {
    (2, 2): exact_value(2, 2, 4),
    (2, 3): exact_value(2, 3, 5),
    (2, 4): exact_value(2, 4, 6),
    (3, 3): exact_value(3, 3, 6),
}

# Main claim.
k34 = exact_value(3, 4, 6)
fixed = (
    (5, 6), (1, 3), (2, 4),
    (3, 4, 6), (1, 2, 6), (1, 4, 5), (2, 3, 5),
)
direct_check(3, 4, fixed)

print("K34_GCFF_EXACT_OK")
print("smaller_exact=" + repr({k: v for k, v in [((2,2),4),((2,3),5),((2,4),6),((3,3),6)]}))
print("k34_requirements=84 row_patterns_total=128 nondominated_cover_types=" + str(k34["patterns"]))
print("k34_no_5_rows=True dfs_nodes=" + str(k34["nodes_below"]) + " memo_states=" + str(k34["memo_below"]))
print("k34_six_rows=True dfs_nodes=" + str(k34["nodes_at"]) + " memo_states=" + str(k34["memo_at"]))
print("fixed_columns=" + repr(fixed))
print("conclusion=t(K_{3,4})=6; minimum-order strict case for the coloring upper bound")
