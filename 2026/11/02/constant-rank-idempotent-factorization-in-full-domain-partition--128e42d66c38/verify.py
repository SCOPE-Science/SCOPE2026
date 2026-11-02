"""Finite checks of constant-rank idempotent factorizations in full-domain partition monoids.

Run: python verify.py. This is a finite cross-check, not a substitute for the proof.
"""
from collections import Counter, defaultdict, deque


def set_partitions(N):
    def rec(labels, maximum):
        if len(labels) == N:
            yield tuple(labels)
            return
        for label in range(maximum + 2):
            yield from rec(labels + [label], max(maximum, label))
    yield from rec([0], 0)


def canonical(seq):
    ids = {}
    out = []
    for value in seq:
        if value not in ids:
            ids[value] = len(ids)
        out.append(ids[value])
    return tuple(out)


def full_domain(p, n):
    return all(p[i] in p[n:] for i in range(n))


def rank(p, n):
    return len(set(p[:n]))


def product(a, b, n):
    """Stack diagram a above b, deleting any middle-only components."""
    parent = list(range(3 * n))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def join(i, j):
        i, j = root(i), root(j)
        if i != j:
            parent[j] = i
    for diagram, offset in ((a, 0), (b, n)):
        groups = defaultdict(list)
        for idx, color in enumerate(diagram):
            groups[color].append(idx + offset)
        for points in groups.values():
            for point in points[1:]:
                join(points[0], point)
    return canonical(root(i) for i in list(range(n)) + list(range(2*n, 3*n)))


def transformation_diagram(f):
    n = len(f)
    return canonical(list(f) + list(range(n)))


def split_as_transformation_and_idempotent(alpha, n):
    tops = defaultdict(list)
    bottoms = defaultdict(list)
    for i, label in enumerate(alpha[:n]):
        tops[label].append(i)
    for j, label in enumerate(alpha[n:]):
        bottoms[label].append(j)
    labels = list(tops)
    B = [bottoms[label] for label in labels]
    C = [bottoms[label] for label in bottoms if label not in tops]
    f = [None] * n
    for i, label in enumerate(labels):
        for point in tops[label]:
            f[point] = B[i][0]
    upper = {}
    for i, block in enumerate(B):
        for point in block:
            upper[point] = i
    for block in C:
        for point in block:
            upper[point] = 0
    e = canonical([upper[i] for i in range(n)] + list(alpha[n:]))
    return transformation_diagram(f), e, tuple(tops[label][0] for label in labels), tuple(B[i][0] for i in range(len(labels))), tops


def token_moves(start, target, n):
    """BFS in the graph of labeled placements, moving one token to a hole."""
    if start == target:
        return []
    prev = {start: None}
    q = deque([start])
    while q and target not in prev:
        position = q.popleft()
        occupied = set(position)
        for i, source in enumerate(position):
            for vacancy in range(n):
                if vacancy in occupied:
                    continue
                nxt = position[:i] + (vacancy,) + position[i+1:]
                if nxt not in prev:
                    prev[nxt] = (position, source, vacancy)
                    q.append(nxt)
    assert target in prev, 'no token route despite free position'
    path = []
    state = target
    while state != start:
        predecessor, source, vacancy = prev[state]
        path.append((predecessor, source, vacancy))
        state = predecessor
    return path[::-1]


def rank_preserving_idempotents(alpha, n):
    t, e, start, target, tops = split_as_transformation_and_idempotent(alpha, n)
    r = rank(alpha, n)
    assert r < n
    representatives = {label: tops[label][0] for label in tops}
    f0 = [None] * n
    for label, group in tops.items():
        for point in group:
            f0[point] = representatives[label]
    factors = [transformation_diagram(f0)]
    for position, source, vacancy in token_moves(start, target, n):
        new_occupied = (set(position) - {source}) | {vacancy}
        f = [min(new_occupied)] * n
        for j in new_occupied:
            f[j] = j
        f[source] = vacancy
        factors.append(transformation_diagram(f))
    factors.append(e)
    assert product(factors[0], factors[0], n) == factors[0]
    for f in factors:
        assert rank(f, n) == r
        assert product(f, f, n) == f
    p = factors[0]
    for f in factors[1:]:
        p = product(p, f, n)
    assert p == alpha, (n, alpha, factors, p)
    return len(factors)


def main():
    for n in range(2, 6):
        census = Counter()
        checks = 0
        max_factors = 0
        for alpha in set_partitions(2*n):
            if not full_domain(alpha, n):
                continue
            r = rank(alpha, n)
            census[r] += 1
            if r == n:
                continue  # Units are excluded from the theorem.
            max_factors = max(max_factors, rank_preserving_idempotents(alpha, n))
            checks += 1
        print('n={} |monoid|={} singular_checked={} rank_counts={} maximum_factors={}'.format(
            n, sum(census.values()), checks, dict(sorted(census.items())), max_factors))
    # Separate closure check; generators are idempotents in the rank ideal itself.
    for n in range(2, 5):
        monoid = [a for a in set_partitions(2*n) if full_domain(a, n)]
        idempotents = [a for a in monoid if product(a, a, n) == a]
        for r in range(1, n):
            goal = {a for a in monoid if rank(a, n) <= r}
            gens = [a for a in idempotents if rank(a, n) <= r]
            seen = set(gens)
            q = deque(gens)
            while q:
                a = q.popleft()
                for b in gens:
                    c = product(a, b, n)
                    if c not in seen:
                        seen.add(c)
                        q.append(c)
            assert seen == goal, (n, r, len(seen), len(goal))
            print('ideal_n={} ideal_r={} elements={} generators={} closure_verified'.format(n, r, len(goal), len(gens)))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
