"""Exact exploratory enumeration of Berge-K_1,5 saturation; no dependencies."""
from itertools import combinations
import json


def matching_rank(pairs):
    owner = {}

    def augment(i, seen):
        for x in pairs[i]:
            if x in seen:
                continue
            seen.add(x)
            if x not in owner or augment(owner[x], seen):
                owner[x] = i
                return True
        return False

    return sum(augment(i, set()) for i in range(len(pairs)))


def tree_rank(pairs):
    adj = {}
    for a, b in pairs:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    seen = set()
    trees = 0
    for a in adj:
        if a in seen:
            continue
        stack = [a]
        seen.add(a)
        vertices = degree_sum = 0
        while stack:
            x = stack.pop()
            vertices += 1
            degree_sum += len(adj[x])
            for y in adj[x] - seen:
                seen.add(y)
                stack.append(y)
        trees += degree_sum // 2 == vertices - 1
    return len(adj) - trees


def is_saturated(n, edges):
    edges = set(map(tuple, edges))
    links = [[tuple(x for x in e if x != v) for e in edges if v in e]
             for v in range(n)]
    if any(matching_rank(link) >= 5 for link in links):
        return False
    for e in combinations(range(n), 3):
        if e not in edges and not any(
            matching_rank(links[v] + [tuple(x for x in e if x != v)]) >= 5
            for v in e
        ):
            return False
    return True


def enumerate_order(n):
    triples = list(combinations(range(n), 3))
    local_pairs = [list(combinations([x for x in range(n) if x != v], 2))
                   for v in range(n)]
    changes = [[(v, 1 << local_pairs[v].index(tuple(x for x in e if x != v)))
                for v in e] for e in triples]
    pairs = list(combinations(range(n - 1), 2))
    rank = []
    for mask in range(1 << len(pairs)):
        selected = [p for i, p in enumerate(pairs) if mask >> i & 1]
        value = tree_rank(selected)
        assert value == matching_rank(selected)
        rank.append(value)
    local = [0] * n
    old = 0
    counts = {}
    witnesses = {}
    accepted = 0
    for step in range(1 << len(triples)):
        mask = step ^ (step >> 1)
        if step:
            j = (mask ^ old).bit_length() - 1
            for v, bit in changes[j]:
                local[v] ^= bit
        old = mask
        if any(rank[x] >= 5 for x in local):
            continue
        if any(not (mask >> j & 1) and
               not any(rank[local[v] | bit] >= 5 for v, bit in change)
               for j, change in enumerate(changes)):
            continue
        edges = [e for j, e in enumerate(triples) if mask >> j & 1]
        assert is_saturated(n, edges)
        m = len(edges)
        counts[m] = counts.get(m, 0) + 1
        witnesses.setdefault(m, edges)
        accepted += 1
    return {"n": n, "graphs_checked": 1 << len(triples),
            "accepted": accepted, "edge_count_histogram": counts,
            "witnesses": witnesses}


if __name__ == "__main__":
    for n in range(1, 7):
        print(json.dumps(enumerate_order(n)), flush=True)
