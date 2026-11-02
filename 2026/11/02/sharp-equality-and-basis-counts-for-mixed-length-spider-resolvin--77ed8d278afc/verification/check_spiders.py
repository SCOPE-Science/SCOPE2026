"""Direct distance/adjacency enumeration of minimum resolving-dominating sets
for mixed-length spider trees.  This is a finite diagnostic, not an infinite proof.
"""
from collections import deque

def spider(p, q):
    assert p >= 0 and q >= 2
    edges = []
    next_vertex = 1
    for _ in range(p):
        edges.append((0, next_vertex))
        next_vertex += 1
    for _ in range(q):
        edges.extend([(0, next_vertex), (next_vertex, next_vertex + 1)])
        next_vertex += 2
    return next_vertex, edges

def distances(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    D = []
    for root in range(n):
        row = [-1] * n
        row[root] = 0
        todo = deque([root])
        while todo:
            u = todo.popleft()
            for v in adj[u]:
                if row[v] == -1:
                    row[v] = row[u] + 1
                    todo.append(v)
        D.append(row)
    return adj, D

def enumerate_min(p, q):
    n, edges = spider(p, q)
    adj, D = distances(n, edges)
    E = len(edges)
    eD = [[min(D[s][a], D[s][b]) for a, b in edges]
          for s in range(n)]
    # Separate admissibility tests use the original vertex and edge definitions.
    best_md = n + 1
    best_em = n + 1
    count_md = 0
    count_em = 0
    for mask in range(1 << n):
        size = mask.bit_count()
        if size > max(best_md, best_em):
            continue
        chosen = [v for v in range(n) if mask & (1 << v)]
        if size <= best_md:
            dominates_v = all(
                (mask & (1 << v)) or any(mask & (1 << w) for w in adj[v])
                for v in range(n)
            )
            if dominates_v:
                signatures = {tuple(D[s][v] for s in chosen) for v in range(n)}
                if len(signatures) == n:
                    if size < best_md:
                        best_md, count_md = size, 0
                    count_md += 1
        if size <= best_em:
            dominates_e = all(any(eD[s][j] <= 1 for s in chosen)
                              for j in range(E))
            if dominates_e:
                signatures = {tuple(eD[s][j] for s in chosen) for j in range(E)}
                if len(signatures) == E:
                    if size < best_em:
                        best_em, count_em = size, 0
                    count_em += 1
    return best_md, best_em, count_md, count_em

def predicted(p, q):
    return (
        p + q,
        q if p == 0 else p + q - 1,
        (1 << q) - 1 if p == 0 else (p + 1) * (1 << q),
        (q + 2) * (1 << (q - 1)) if p == 0
        else (1 << q) - 1 if p == 1
        else p * (1 << q),
    )

def main():
    examined = 0
    for p in range(6):
        for q in range(2, 6):
            n, _ = spider(p, q)
            examined += 1 << n
            actual = enumerate_min(p, q)
            expected = predicted(p, q)
            assert actual == expected, (p, q, actual, expected)
            print(f"p={p} q={q}: dimension, edge-dimension, two basis counts = {actual}")
    print(f"PASS: 24 graphs; {examined} vertex subsets checked against original definitions")

if __name__ == '__main__':
    main()
