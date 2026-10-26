"""Exhaustive independent checks of minimal geodetic sets on cycle bouquets.

Run with Python 3: python geo_bouquet_verify.py
"""
from collections import Counter, deque
from itertools import combinations, product
from math import prod


def make_bouquet(lengths):
    # Shared vertex 0, each cycle otherwise uses distinct labels.
    adj = [set()]
    groups = []
    for n in lengths:
        group = list(range(len(adj), len(adj) + n - 1))
        adj.extend(set() for _ in group)
        ring = [0] + group
        for j in range(n):
            a, b = ring[j], ring[(j + 1) % n]
            adj[a].add(b)
            adj[b].add(a)
        groups.append(group)
    return adj, groups


def shortest_path_vertex_masks(adj):
    N = len(adj)
    distances = []
    for a in range(N):
        dist = [-1] * N
        dist[a] = 0
        queue = deque([a])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        distances.append(dist)
    mask = [[0] * N for _ in range(N)]
    for a in range(N):
        for b in range(a+1, N):
            d = distances[a][b]
            m = sum(1 << v for v in range(N)
                    if distances[a][v] + distances[v][b] == d)
            mask[a][b] = mask[b][a] = m
    return mask


def geodetic(bits, masks):
    N = len(masks)
    if bits.bit_count() < 2:
        return False
    chosen = [v for v in range(N) if (bits >> v) & 1]
    reached = bits
    full = (1 << N) - 1
    for a, b in combinations(chosen, 2):
        reached |= masks[a][b]
        if reached == full:
            return True
    return False


def expected_local(n, group):
    m = n // 2
    out = []
    if n % 2 == 0:
        out.append(1 << group[m - 1])
    for a, b in combinations(range(1, n), 2):
        if max(a, b-a, n-b) <= m and \
           not (n % 2 == 0 and (a == m or b == m)):
            out.append((1 << group[a-1]) | (1 << group[b-1]))
    b_formula = (m * (m-1) // 2 if n % 2 == 0 else m*(m+1)//2)
    assert len(out) == b_formula + (n % 2 == 0), (n, len(out))
    return out


def check(lengths):
    adj, groups = make_bouquet(lengths)
    masks = shortest_path_vertex_masks(adj)
    N = len(adj)
    expected = set()
    for local_sets in product(*(expected_local(n, g) for n,g in zip(lengths, groups))):
        b = 0
        for s in local_sets:
            b |= s
        expected.add(b)
    found = set()
    full = 1 << N
    tested = 0
    for bits in range(1, full):
        tested += 1
        if not geodetic(bits, masks):
            continue
        if all(not geodetic(bits & ~(1 << v), masks)
               for v in range(N) if (bits >> v) & 1):
            found.add(bits)
    if found != expected:
        raise AssertionError((lengths,
            'extra', sorted(found-expected)[:5],
            'missing', sorted(expected-found)[:5]))
    actual = dict(sorted(Counter(b.bit_count() for b in found).items()))
    predicted = Counter({0:1})
    for n in lengths:
        m = n // 2
        c = Counter({2: m*(m-1)//2 if n%2 == 0 else m*(m+1)//2})
        if n%2 == 0: c[1] = 1
        updated = Counter()
        for x,a in predicted.items():
            for y,b in c.items():
                updated[x+y] += a*b
        predicted = updated
    assert actual == dict(sorted(predicted.items()))
    return tested, len(found), actual


if __name__ == '__main__':
    cases = [(a,b) for a,b in product(range(3,9), repeat=2) if a <= b and a+b-1 <= 15]
    cases += [(3,3,3),(3,3,4),(3,4,4),(4,4,4),(3,4,5),(4,5,6),(3,5,7)]
    total = 0
    for lengths in cases:
        t, count, poly = check(lengths)
        total += t
        print(f"{lengths}: examined={t}, minimal={count}, coefficients={poly}")
    print(f"PASSED {len(cases)} bouquets, {total} nonempty subsets independently checked")
