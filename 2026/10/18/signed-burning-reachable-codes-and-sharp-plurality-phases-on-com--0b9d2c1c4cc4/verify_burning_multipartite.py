#!/usr/bin/env python3
"""Independent finite tests for the balanced multipartite signed-burning theorem.

Uses direct synchronous simulation of the original spread-before-ignition
process; no algebraic switching identity is assumed in the simulator.
"""
from functools import lru_cache
from math import comb


def partitions(total, low=1):
    if total == 0:
        yield ()
    else:
        for v in range(low, total + 1):
            for tail in partitions(total - v, v):
                yield (v,) + tail


def parts_for(shape):
    parts = []
    for p, count in enumerate(shape):
        parts += [p] * count
    return tuple(parts)


def signed_adj(parts, mask):
    n = len(parts)
    phase = [(-1 if mask >> i & 1 else 1) for i in range(n)]
    return tuple(tuple(0 if i == j or parts[i] == parts[j]
                       else phase[i] * phase[j]
                       for j in range(n)) for i in range(n))


def reachable_direct(adj):
    n = len(adj)

    @lru_cache(None)
    def visit(state):
        nxt = list(state)
        for v in range(n):
            if state[v]:
                continue
            h = sum(adj[v][u] * state[u] for u in range(n))
            if h:
                nxt[v] = 1 if h > 0 else -1
        if all(nxt):
            return frozenset([tuple(nxt)])
        answers = set()
        for v in range(n):
            if nxt[v] == 0:
                for c in (-1, 1):
                    newer = list(nxt)
                    newer[v] = c
                    answers.update(visit(tuple(newer)))
        return frozenset(answers)

    return visit((0,) * n)


def predicted_code(parts, mask):
    n = len(parts)
    eligible = [v for v in range(n) if parts.count(parts[v]) > 1]
    phase = tuple(-1 if mask >> i & 1 else 1 for i in range(n))
    out = set()
    for base in (-1, 1):
        out.add(tuple(base * x for x in phase))
        for v in eligible:
            arr = [base * x for x in phase]
            arr[v] *= -1
            out.add(tuple(arr))
    return out


def distance_formula(parts, mask):
    n = len(parts)
    eligible = {v for v in range(n) if parts.count(parts[v]) > 1}
    U = {v for v in range(n) if mask >> v & 1}
    return min(len(U) - int(bool(U & eligible)),
               n-len(U) - int(bool(eligible-U)))


def covering_formula(parts):
    n = len(parts)
    s = sum(parts.count(p) == 1 for p in parts)
    if s == n:
        return n // 2
    if n % 2 and s >= n//2:
        return n // 2
    return n // 2 - 1


def deepest_signings_formula(parts):
    n = len(parts)
    q = n // 2
    s = sum(parts.count(p) == 1 for p in parts)
    e = n-s
    choose = lambda a, b: comb(a, b) if 0 <= b <= a else 0
    if e == 0:
        return choose(n, q)//2 if n%2 == 0 else choose(n, q)
    if n % 2 == 0:
        return choose(n, q)//2 + choose(s, q-1)
    if s >= q:
        return choose(s, q)
    return choose(n, q) + choose(s, q-1)


def verify(max_n=7):
    count_graphs = count_masks = count_outputs = 0
    for n in range(2, max_n+1):
        for shape in partitions(n):
            if len(shape) < 2:
                continue
            parts = parts_for(shape)
            count_graphs += 1
            depths = []
            for mask in range(1 << (n-1)):
                actual = reachable_direct(signed_adj(parts, mask))
                target = predicted_code(parts, mask)
                assert actual == target, (shape, mask, sorted(actual ^ target))
                depth = min(sum(x < 0 for x in vec) for vec in actual)
                assert depth == distance_formula(parts, mask), (shape, mask, depth)
                depths.append(depth)
                count_masks += 1
                count_outputs += len(actual)
            assert max(depths) == covering_formula(parts), (shape, max(depths))
            assert sum(d == max(depths) for d in depths) == deepest_signings_formula(parts), shape
    print('VERIFY_OK graph_types=%d signings=%d terminal_states=%d max_order=%d'
          % (count_graphs, count_masks, count_outputs, max_n))


if __name__ == '__main__':
    verify()
