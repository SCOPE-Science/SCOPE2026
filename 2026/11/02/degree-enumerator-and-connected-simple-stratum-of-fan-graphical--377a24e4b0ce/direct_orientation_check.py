"""Independent edge-orientation enumeration for the fan acyclic-orientation theorem.
Run: python direct_orientation_check.py (stdlib only).
"""
from collections import Counter, deque


def orient_acyclic(mask, n, edges):
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for j, (u, v) in enumerate(edges):
        a, b = (u, v) if ((mask >> j) & 1) else (v, u)
        adj[a].append(b)
        indeg[b] += 1
    q = deque(i for i, d in enumerate(indeg) if d == 0)
    reached = 0
    while q:
        u = q.popleft()
        reached += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return reached == n + 1


def shifted(p, k):
    return [0] * k + p


def degree_polynomial(n):
    # coefficients of 2t^n [z^(n-1)](1-3z+(1-t)z^2)^(-1)
    a, b = [1], [3]
    if n == 1:
        coeff = a
    elif n == 2:
        coeff = b
    else:
        for _ in range(2, n):
            # a_k=3a_(k-1)-(1-t)a_(k-2)
            size = max(len(a) + 1, len(b))
            c = [0] * size
            for j, val in enumerate(b):
                c[j] += 3 * val
            for j, val in enumerate(a):
                c[j] -= val
                c[j + 1] += val
            while len(c) > 1 and c[-1] == 0:
                c.pop()
            a, b = b, c
        coeff = b
    return {n + j: 2 * val for j, val in enumerate(coeff) if val}


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def check(n):
    # No triangle or local-reachability criterion is used to construct states.
    edges = [(0, i) for i in range(1, n + 1)] + [
        (i, i + 1) for i in range(1, n)
    ]
    m = len(edges)
    states = {s for s in range(1 << m) if orient_acyclic(s, n, edges)}
    degree = {s: sum((s ^ (1 << j)) in states for j in range(m)) for s in states}
    histogram = dict(Counter(degree.values()))
    assert histogram == degree_polynomial(n), (n, histogram, degree_polynomial(n))
    assert len(states) == 2 * 3 ** (n - 1)
    simple = {s for s in states if degree[s] == n}
    assert len(simple) == 2 * fibonacci(2 * n)
    assert min(degree.values()) == n
    assert max(degree.values()) == n + (n - 1) // 2
    assert histogram[max(degree.values())] == (2 if n % 2 else 3 * n)
    seen = set()
    q = deque([next(iter(simple))])
    seen.add(q[0])
    while q:
        x = q.popleft()
        for j in range(m):
            y = x ^ (1 << j)
            if y in simple and y not in seen:
                seen.add(y)
                q.append(y)
    assert len(seen) == len(simple), (n, len(seen), len(simple))
    return (n, len(states), histogram, len(simple))


if __name__ == '__main__':
    for n in range(2, 10):
        print(check(n))
    print('DIRECT_DAG_FLIP_DEGREE_AND_SIMPLE_CONNECTIVITY_PASS')
