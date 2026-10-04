#!/usr/bin/env python3
from itertools import product

def compose(A, B):
    return {(x, z) for (x, y) in A for (yy, z) in B if y == yy}

def inverse(A):
    return {(y, x) for (x, y) in A}

def posets(n):
    off = [(i, j) for i in range(n) for j in range(n) if i != j]
    for mask in range(1 << len(off)):
        le = {(i, i) for i in range(n)}
        for k, e in enumerate(off):
            if (mask >> k) & 1:
                le.add(e)
        if any(i != j and (i, j) in le and (j, i) in le
               for i in range(n) for j in range(n)):
            continue
        transitive = True
        for (a, b) in le:
            for (c, d) in le:
                if b == c and (a, d) not in le:
                    transitive = False
                    break
            if not transitive:
                break
        if transitive:
            yield le

def components(n, le):
    adj = {i: set() for i in range(n)}
    for a, b in le:
        if a != b:
            adj[a].add(b)
            adj[b].add(a)
    seen = set()
    out = []
    for s in range(n):
        if s in seen:
            continue
        stack = [s]
        seen.add(s)
        comp = set()
        while stack:
            x = stack.pop()
            comp.add(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        out.append(comp)
    return out

def bounded_components(n, le):
    for C in components(n, le):
        has_top = any(all((x, t) in le for x in C) for t in C)
        has_bottom = any(all((b, x) in le for x in C) for b in C)
        if not (has_top and has_bottom):
            return False
    return True

def beta(R, le):
    return compose(R, le)

def delta(R, le):
    return compose(R, inverse(le))

def box_p(R, le):
    return compose(le, R) <= compose(R, le)

def diamond_p(R, le):
    return compose(inverse(le), R) <= compose(R, inverse(le))

# Exact order-theoretic criterion for every labelled poset through size four.
counts = []
for n in range(1, 5):
    count = 0
    for le in posets(n):
        upper = compose(le, inverse(le))
        lower = compose(inverse(le), le)
        assert (upper == lower) == bounded_components(n, le)

        if upper == lower:
            E = {
                (x, y)
                for C in components(n, le)
                for x in C
                for y in C
            }
            assert upper == E
            assert compose(E, le) == E
            assert compose(E, inverse(le)) == E
        count += 1
    counts.append(count)

assert counts == [1, 3, 19, 219]

# Universal commutation, fixed points, and p-condition preservation
# for every binary relation through three points.
for n in range(1, 4):
    pairs = [(i, j) for i in range(n) for j in range(n)]
    for le in posets(n):
        criterion = bounded_components(n, le)
        saw_failure = False

        E = {
            (x, y)
            for C in components(n, le)
            for x in C
            for y in C
        }

        for mask in range(1 << len(pairs)):
            R = {e for k, e in enumerate(pairs) if (mask >> k) & 1}
            left = beta(delta(R, le), le)
            right = delta(beta(R, le), le)

            if left != right:
                saw_failure = True

            if criterion:
                assert left == right
                assert left == compose(R, E)
                assert beta(left, le) == left
                assert delta(left, le) == left

                if box_p(R, le) and diamond_p(R, le):
                    assert box_p(left, le)
                    assert diamond_p(left, le)

        assert saw_failure == (not criterion)

print("VERIFY_OK")
