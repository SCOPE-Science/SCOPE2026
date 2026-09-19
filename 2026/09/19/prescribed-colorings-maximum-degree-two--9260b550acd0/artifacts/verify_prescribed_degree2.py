#!/usr/bin/env python3
"""Definition-level verification for prescribed colorings at maximum degree two."""

from functools import lru_cache

MAX_N = 12


def integer_partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for tail in integer_partitions(n - first, first):
            yield (first,) + tail


def component_multisets(n):
    types = [(k, "P") for k in range(1, n + 1)] + [(k, "C") for k in range(3, n + 1)]
    types.sort(key=lambda x: (x[0], x[1]))
    out = []

    def rec(start, left, acc):
        if left == 0:
            out.append(tuple(acc))
            return
        for i in range(start, len(types)):
            k, kind = types[i]
            if k > left:
                break
            acc.append((k, kind))
            rec(i, left - k, acc)
            acc.pop()

    rec(0, n, [])
    return out


def graph_from_components(components):
    adj = []
    offset = 0
    for k, kind in components:
        adj.extend([0] * k)
        if kind == "P":
            edges = [(i, i + 1) for i in range(k - 1)]
        else:
            edges = [(i, (i + 1) % k) for i in range(k)]
        for a, b in edges:
            u, v = offset + a, offset + b
            adj[u] |= 1 << v
            adj[v] |= 1 << u
        offset += k
    return tuple(adj)


def prescribed_coloring_exists(adj, quotas):
    n = len(adj)
    q = len(quotas)
    order = sorted(range(n), key=lambda v: (-adj[v].bit_count(), v))
    color = [-1] * n
    remaining = list(quotas)

    def choose_vertex():
        best = None
        best_key = None
        for v in order:
            if color[v] != -1:
                continue
            forbidden = 0
            mask = adj[v]
            u = 0
            while mask:
                lsb = mask & -mask
                u = lsb.bit_length() - 1
                c = color[u]
                if c >= 0:
                    forbidden |= 1 << c
                mask ^= lsb
            key = (forbidden.bit_count(), adj[v].bit_count())
            if best_key is None or key > best_key:
                best_key = key
                best = (v, forbidden)
        return best

    def rec(colored):
        if colored == n:
            return all(x == 0 for x in remaining)
        v, forbidden = choose_vertex()
        candidates = [c for c in range(q) if remaining[c] and not (forbidden >> c) & 1]
        candidates.sort(key=lambda c: -remaining[c])
        seen = set()
        for c in candidates:
            signature = remaining[c]
            if signature in seen:
                # Colors with equal unused quota and no previous occurrence are interchangeable.
                used_c = quotas[c] - remaining[c]
                if used_c == 0:
                    continue
            if quotas[c] - remaining[c] == 0:
                seen.add(signature)
            color[v] = c
            remaining[c] -= 1
            if rec(colored + 1):
                return True
            remaining[c] += 1
            color[v] = -1
        return False

    return rec(0)


def admissible(n, parts):
    s, m = divmod(n, 3)
    if m == 0:
        return max(parts) <= s
    return max(parts) <= s + 1 and sum(x == s + 1 for x in parts) <= m


def main():
    for n in range(3, MAX_N + 1):
        graphs = [graph_from_components(c) for c in component_multisets(n)]
        targets = list(integer_partitions(n))
        for parts in targets:
            predicted = admissible(n, parts)
            universal = True
            for adj in graphs:
                if not prescribed_coloring_exists(adj, parts):
                    universal = False
                    break
            if universal != predicted:
                raise AssertionError((n, parts, predicted, universal))
    print("PASS: exact universal characterization verified for all maximum-degree-two graph types and all target partitions through order 12.")


if __name__ == "__main__":
    main()
