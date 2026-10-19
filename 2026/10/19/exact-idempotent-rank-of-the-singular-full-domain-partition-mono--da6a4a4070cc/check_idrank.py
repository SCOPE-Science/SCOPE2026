"""Finite checks for a rank theorem on full-domain partition monoids.

Run with Python 3 (standard library only). Finite checks are not an infinite proof.
"""

def canonical(labels):
    ids, out = {}, []
    for a in labels:
        if a not in ids:
            ids[a] = len(ids)
        out.append(ids[a])
    return tuple(out)


def partitions(k):
    """All set partitions on a labeled k-set as restricted-growth tuples."""
    if k == 0:
        yield ()
        return
    for p in partitions(k - 1):
        for a in range(max(p, default=-1) + 2):
            yield p + (a,)


def rank(p, n):
    return len(set(p[:n]) & set(p[n:]))


def full_domain(p, n):
    return set(p[:n]) <= set(p[n:])


def multiply(a, b, n):
    """Glue the bottom row of a to the top row of b, delete middle."""
    parent = list(range(3 * n))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i, j):
        parent[root(i)] = root(j)

    for offset, diagram in ((0, a), (n, b)):
        seen = {}
        for i, c in enumerate(diagram):
            if c in seen:
                union(offset + i, seen[c])
            else:
                seen[c] = offset + i
    return canonical([root(i) for i in range(n)] +
                     [root(2*n + i) for i in range(n)])


def merge_idempotent(n, i, j):
    top = [i if k == j else k for k in range(n)]
    return canonical(top + top)


def transformation_idempotent(n, i, j):
    top = list(range(n))
    top[i] = j
    return canonical(top + list(range(n)))


def oriented_edges(n):
    if n == 3:
        return [(0, 1), (1, 2), (2, 0)]
    if n == 4:
        return [(0, 1), (0, 2), (1, 2),
                (1, 3), (2, 3), (3, 0)]
    if n % 2 == 1:
        return [(i, j) if (j - i) % n <= (n - 1)//2 else (j, i)
                for i in range(n) for j in range(i+1, n)]
    # Insert further vertices successively into a strong base.
    edges = oriented_edges(n-1)
    v = n-1
    edges += [(0, v), (v, 1)]
    edges += [(v, i) for i in range(2, v)]
    return edges


def generated_rank_layer(generators, n):
    result = set(generators)
    queue = list(result)
    while queue:
        a = queue.pop()
        for b in generators:
            c = multiply(a, b, n)
            if rank(c, n) == n-1 and c not in result:
                result.add(c)
                queue.append(c)
    return result


def run():
    d2 = [p for p in partitions(4) if full_domain(p, 2) and rank(p, 2) == 1]
    assert len(d2) == 3
    assert all(multiply(a, b, 2) == b for a in d2 for b in d2)
    print('n=2: 3 singular idempotents form a right-zero semigroup')
    for n in (3, 4, 5):
        d = {p for p in partitions(2*n)
             if full_domain(p, n) and rank(p, n) == n-1}
        e = {merge_idempotent(n, i, j)
             for i in range(n) for j in range(i+1, n)}
        t = {transformation_idempotent(n, i, j)
             for i in range(n) for j in range(n) if i != j}
        all_rank_idempotents = {p for p in d if multiply(p, p, n) == p}
        assert all_rank_idempotents == e | t
        edges = oriented_edges(n)
        assert len(edges) == n*(n-1)//2
        g = e | {transformation_idempotent(n, i, j) for i,j in edges}
        assert len(g) == n*(n-1)
        assert all(multiply(x, x, n) == x for x in g)
        assert generated_rank_layer(g, n) == d
        print(f'n={n}: layer_size={len(d)} idempotents={len(all_rank_idempotents)} generators={len(g)} checked')
    print('CHECKER_OK')


if __name__ == '__main__':
    run()
