"""Independent finite tests for path-free complexes of complete multipartite graphs.
No third-party dependencies. Checks paths via exact depth-first search, not the theorem's majority characterization.
"""
from itertools import combinations
from math import comb


def B(n, j):
    return comb(n, j) if 0 <= j <= n else 0


def contains_path(mask, cls, t):
    vertices = [v for v in range(len(cls)) if mask & (1 << v)]
    if len(vertices) < t:
        return False
    frontier = [(v, 1 << v, 1) for v in vertices]
    while frontier:
        last, seen, k = frontier.pop()
        if k == t:
            return True
        for w in vertices:
            if cls[w] != cls[last] and not seen & (1 << w):
                frontier.append((w, seen | 1 << w, k + 1))
    return False


def rank2(columns):
    piv = {}
    for c in columns:
        while c:
            pos = c.bit_length() - 1
            if pos in piv:
                c ^= piv[pos]
            else:
                piv[pos] = c
                break
    return len(piv)


def run(sizes, t):
    cls = [i for i, a in enumerate(sizes) for _ in range(a)]
    n = len(cls)
    cells = [[] for _ in range(n + 1)]
    h = t // 2 - 1
    for f in range(1, 1 << n):
        s = f.bit_count()
        good = s < t or any(sum(1 for v in range(n) if (f & (1 << v)) and cls[v] != i) <= h for i in range(len(sizes)))
        direct = not contains_path(f, cls, t)
        assert good == direct, (sizes, t, f, good, direct)
        if good:
            cells[s].append(f)
    r = {1: 1}
    for k in range(2, n + 1):
        lo = {s: i for i, s in enumerate(cells[k - 1])}
        cols = []
        for s in cells[k]:
            w = 0
            for v in range(n):
                if s & (1 << v):
                    w |= 1 << lo[s ^ (1 << v)]
            cols.append(w)
        r[k] = rank2(cols)
    betti = {k-1: len(cells[k]) - r.get(k, 0) - r.get(k+1, 0) for k in range(1, n + 1)}
    betti = {k: v for k, v in betti.items() if v}
    expected = B(n - 1, t - 1) - sum(sum(B(n-a, q) * B(a-1, t-1-q) for q in range(t//2)) for a in sizes)
    assert betti == ({t-2: expected} if expected else {}), (sizes, t, betti, expected)
    return len([f for layer in cells for f in layer]), expected


if __name__ == '__main__':
    cases = [(1,1,3), (1,2,2), (1,1,4), (2,2,2), (4,2,1), (4,2,2), (4,3,1),
             (3,3,3), (2,2,2,2), (3,2,2,2), (4,2,1,1), (2,3,4), (5,2,2)]
    total = 0
    for parts in cases:
        for t in range(3, min(sum(parts), 8) + 1):
            faces, beta = run(parts, t)
            print(f'PASS {parts} t={t} faces={faces} top_beta={beta}')
            total += 1
    print(f'PASS: {total} cases, direct simple-path enumeration and all mod-two simplicial boundary ranks')
