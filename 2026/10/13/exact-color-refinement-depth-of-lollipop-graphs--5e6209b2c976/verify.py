#!/usr/bin/env python3
from collections import defaultdict

def lollipop(m, n):
    assert m >= 3 and n >= 1
    adj = [set() for _ in range(m + n)]
    for i in range(m):
        for j in range(i + 1, m):
            adj[i].add(j)
            adj[j].add(i)
    adj[0].add(m)
    adj[m].add(0)
    for v in range(m, m + n - 1):
        adj[v].add(v + 1)
        adj[v + 1].add(v)
    return adj

def partition(colors):
    classes = defaultdict(set)
    for v, c in enumerate(colors):
        classes[c].add(v)
    return frozenset(frozenset(x) for x in classes.values())

def refinement_partitions(adj, rounds):
    colors = [0] * len(adj)
    ans = [partition(colors)]
    for _ in range(rounds):
        signatures = [
            (colors[v], tuple(sorted(colors[w] for w in adj[v])))
            for v in range(len(adj))
        ]
        names = {}
        new = []
        for s in signatures:
            if s not in names:
                names[s] = len(names)
            new.append(names[s])
        colors = new
        ans.append(partition(colors))
    return ans

def predicted_depth(m, n):
    if m >= 4:
        return (n + 1) // 2
    if n == 1:
        return 1
    if n == 2:
        return 2
    return max(3, (n + 1) // 2)

def predicted_partition(m, n, r):
    q0 = 0
    Q = set(range(1, m))
    p = lambda j: m + j - 1

    if m >= 4:
        classes = [{q0}, Q]
        classes += [{p(j)} for j in range(1, n + 1) if j < r]
        middle = [j for j in range(1, n + 1) if r <= j <= n - r]
        if middle:
            classes.append({p(j) for j in middle})
        classes += [{p(j)} for j in range(1, n + 1) if j > n - r]
        return frozenset(frozenset(x) for x in classes if x)

    if n == 1:
        return frozenset([frozenset({q0}), frozenset(Q), frozenset({p(1)})])

    if r == 1:
        merged = set(Q)
        merged.update(p(j) for j in range(1, n))
        return frozenset([frozenset({q0}), frozenset(merged), frozenset({p(n)})])

    if n == 2:
        return frozenset([
            frozenset({q0}), frozenset(Q),
            frozenset({p(1)}), frozenset({p(2)})
        ])

    if r == 2:
        classes = [{q0}, set(Q) | {p(1)}]
        middle = [j for j in range(2, n - 1)]
        if middle:
            classes.append({p(j) for j in middle})
        classes.append({p(n - 1)})
        classes.append({p(n)})
        return frozenset(frozenset(x) for x in classes if x)

    classes = [{q0}, Q]
    classes += [{p(j)} for j in range(1, n + 1) if j < r]
    middle = [j for j in range(1, n + 1) if r <= j <= n - r]
    if middle:
        classes.append({p(j) for j in middle})
    classes += [{p(j)} for j in range(1, n + 1) if j > n - r]
    return frozenset(frozenset(x) for x in classes if x)

def main():
    depth_checks = 0
    partition_checks = 0
    for m in range(3, 21):
        for n in range(1, 81):
            d = predicted_depth(m, n)
            parts = refinement_partitions(lollipop(m, n), d + 1)
            observed = next(
                s for s in range(len(parts) - 1)
                if parts[s + 1] == parts[s]
            )
            assert observed == d, (m, n, observed, d)
            depth_checks += 1
            for r in range(1, d + 1):
                assert parts[r] == predicted_partition(m, n, r), (m, n, r)
                partition_checks += 1
    print(
        "VERIFY_OK "
        f"depth_checks={depth_checks} "
        f"partition_checks={partition_checks} "
        "m=3..20 n=1..80"
    )

if __name__ == "__main__":
    main()
