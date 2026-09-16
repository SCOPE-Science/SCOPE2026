"""Reproducible exact checks of the minimum-order affine locality witnesses.

No graph or finite-field packages are required. The constructor uses coordinates;
the validator sees only an edge list and the two claimed matching certificates.
"""

from collections import deque
from functools import lru_cache
from itertools import combinations


class Field:
    def __init__(self, p, modulus):
        self.p, self.modulus = p, modulus
        self.k = len(modulus)-1
        self.q = p**self.k
        self.digits = [self.expand(a) for a in range(self.q)]
        self.plus = [[self.add(a, b) for b in range(self.q)]
                     for a in range(self.q)]
        self.times = [[self.mul(a, b) for b in range(self.q)]
                      for a in range(self.q)]
        self.negative = [next(b for b in range(self.q) if self.plus[a][b] == 0)
                         for a in range(self.q)]
        assert all(sorted(self.times[a]) == list(range(self.q))
                   for a in range(1, self.q))

    def expand(self, a):
        result = []
        for _ in range(self.k):
            result.append(a % self.p)
            a //= self.p
        return result

    def encode(self, coefficients):
        return sum((a % self.p)*self.p**i for i, a in enumerate(coefficients))

    def add(self, a, b):
        return self.encode([x+y for x, y in zip(self.digits[a], self.digits[b])])

    def mul(self, a, b):
        work = [0]*(2*self.k-1)
        for i, x in enumerate(self.digits[a]):
            for j, y in enumerate(self.digits[b]):
                work[i+j] = (work[i+j]+x*y) % self.p
        for i in range(len(work)-1, self.k-1, -1):
            for j in range(self.k+1):
                work[i-self.k+j] = (work[i-self.k+j]
                                   - work[i]*self.modulus[j]) % self.p
        return self.encode(work[:self.k])


def construct(field):
    q = field.q
    labels = [('P', s, x, y) for s in range(2)
              for x in range(q) for y in range(q)]
    labels += [('L', s, a, b) for s in range(2)
               for a in range(1, q) for b in range(q)]
    index = {v: i for i, v in enumerate(labels)}
    edges, optimum = [], []
    for s in range(2):
        for a in range(1, q):
            for b in range(q):
                for x in range(q):
                    y = field.plus[field.times[a][x]][b]
                    edges.append((index['P', s, x, y], index['L', s, a, b]))
    for x in range(q):
        for y in range(q):
            z = field.plus[y][field.negative[x]]
            optimum.append(len(edges))
            edges.append((index['P', 0, x, y], index['P', 1, z, y]))
    code = {i for i, (kind, _, a, b) in enumerate(labels)
            if (kind == 'P' and a == 0) or (kind == 'L' and a == 1 and b != 0)}
    local = [i for i, (u, v) in enumerate(edges) if u in code and v in code]
    return labels, edges, local, optimum


def validate(labels, edges, local, optimum, q):
    n = len(labels)
    assert len({tuple(sorted(e)) for e in edges}) == len(edges)
    adj = [set() for _ in labels]
    for u, v in edges:
        assert u != v
        adj[u].add(v)
        adj[v].add(u)
    assert all(len(a) == q for a in adj)
    colors = {0: 0}
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in colors:
                colors[v] = 1-colors[u]
                queue.append(v)
            assert colors[v] != colors[u]
    assert len(colors) == n
    assert all(len(adj[u] & adj[v]) <= 1 for u, v in combinations(range(n), 2))

    def induced(matching):
        vertices = [v for i in matching for v in edges[i]]
        if len(set(vertices)) != len(vertices):
            return False
        selected = set(vertices)
        return all(len(adj[v] & selected) == 1 for v in selected)

    assert induced(local) and induced(optimum)
    # These are checked from actual vertices, without using affine coordinates.
    a = {v for i in local for v in edges[i]}
    assert all(len(adj[v] & a) == 1 for v in range(n))
    good_owner = {v: i for i in optimum for v in edges[i]}
    assert all(len({good_owner[v] for v in edge if v in good_owner}) == 1
               for edge in edges)

    def conflict(i, j):
        u, v = edges[i]
        x, y = edges[j]
        return (len({u, v, x, y}) < 4 or x in adj[u] or y in adj[u]
                or x in adj[v] or y in adj[v])

    # Enumeration of the exact exchange predicate, not an assumed local lemma.
    private = {i: [] for i in local}
    for j in range(len(edges)):
        owners = [i for i in local if conflict(i, j)]
        assert owners  # no addition
        if len(owners) == 1 and j not in local:
            private[owners[0]].append(j)
    for pool in private.values():
        assert all(conflict(i, j) for i, j in combinations(pool, 2))

    assert n == 2*q*(2*q-1)
    assert len(edges) == q*q*(2*q-1)
    assert len(local) == 2*q-1
    assert len(optimum) == q*q
    assert len(local)*q*q == len(edges)
    assert len(optimum)*(2*q-1) == len(edges)

    if q == 3:
        # Independent exhaustive maximum-induced-matching optimization on n=30.
        # For a chosen edge, remove all endpoints that cannot coexist with it.
        # The excluded-edge branch retains the original adjacency relation.
        masks = []
        for u, v in edges:
            forbidden = adj[u] | adj[v] | {u, v}
            masks.append(sum(1 << j for j, (x, y) in enumerate(edges)
                             if x in forbidden or y in forbidden))

        @lru_cache(None)
        def exact(remaining):
            if not remaining:
                return 0
            i = (remaining & -remaining).bit_length()-1
            return max(exact(remaining & ~(1 << i)),
                       1+exact(remaining & ~masks[i]))

        computed = exact((1 << len(edges))-1)
        assert computed == len(optimum) == 9
        print('exhaustive optimum', computed, 'states', exact.cache_info().currsize)
    return n, len(edges), len(local), len(optimum)


def negative_controls():
    # A total perfect code alone is NOT enough without the girth restriction.
    # In this triangular prism, the rung 0--3 is a total perfect code matching,
    # yet replacing it by the two indicated edges is possible only when absent
    # cross edges permit it; use a pair of joined triangles instead.
    edges = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 3), (4, 5)]
    adj = [set() for _ in range(6)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    assert all(len(adj[v] & {0, 1}) == 1 for v in range(6))
    assert not any(v in adj[u] for u in (2, 3) for v in (4, 5))
    assert len({2, 3, 4, 5}) == 4  # two replacement edges really are induced
    print('negative control: total perfect code without girth is improvable')


if __name__ == '__main__':
    negative_controls()
    for p, modulus in [(3, [0, 1]), (2, [1, 1, 1]), (5, [0, 1]),
                       (7, [0, 1]), (2, [1, 1, 0, 1]), (3, [1, 0, 1]),
                       (11, [0, 1])]:
        field = Field(p, modulus)
        values = validate(*construct(field), field.q)
        print('q', field.q, 'n,m,local,optimum', values,
              'ratio', f'{field.q**2}/{2*field.q-1}', 'all checks passed')
