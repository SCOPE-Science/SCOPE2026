"""Independent finite checks for general three-position sets on Cartesian path grids.

Run: python verify.py
Only finite instances are tested; the all-size assertion is established by a tiling proof.
"""
from itertools import combinations


def geodesic_triples(m, n, cutoff=3):
    """Generate forbidden triples via original shortest *paths*, not a tiling lemma."""
    vertices = [(r, c) for r in range(m) for c in range(n)]
    index = {v: i for i, v in enumerate(vertices)}
    adjacent = []
    for r, c in vertices:
        adjacent.append([index[w] for w in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)) if w in index])
    forbidden = set()
    for origin in range(len(vertices)):
        active = [(origin,)]
        for length in range(1, cutoff + 1):
            follow = []
            for p in active:
                for t in adjacent[p[-1]]:
                    if t in p:
                        continue
                    q = p + (t,)
                    v, w = vertices[origin], vertices[t]
                    if abs(v[0] - w[0]) + abs(v[1] - w[1]) != length:
                        continue
                    if length >= 2:
                        for z in combinations(q, 3):
                            forbidden.add(sum(1 << a for a in z))
                    follow.append(q)
            active = follow
    return tuple(sorted(forbidden))


def interval_triples(m, n, cutoff=3):
    """Independent Manhattan-betweenness generator for comparison."""
    v = [(r, c) for r in range(m) for c in range(n)]
    result = set()
    for ids in combinations(range(m * n), 3):
        a, b, c = [v[t] for t in ids]
        for mid, p, q in ((a, b, c), (b, a, c), (c, a, b)):
            d = sum(abs(p[t] - q[t]) for t in (0, 1))
            if d <= cutoff and all(min(p[t], q[t]) <= mid[t] <= max(p[t], q[t]) for t in (0, 1)):
                result.add(sum(1 << t for t in ids))
                break
    return tuple(sorted(result))


def count(m, n, d=3):
    forbidden = geodesic_triples(m, n, d)
    assert forbidden == interval_triples(m, n, d)
    size = m*n
    best, ways = -1, 0
    for s in range(1 << size):
        k = s.bit_count()
        if k < best:
            continue
        if any(s & f == f for f in forbidden):
            continue
        if k > best:
            best, ways = k, 0
        ways += 1
    return best, ways, len(forbidden)


def main():
    shapes = [(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),
              (3,2),(3,3),(3,4),(3,5),(3,6),
              (4,2),(4,3),(4,4),(5,2),(5,3),(6,2)]
    total = 0
    for m,n in shapes:
        b, ways, bad = count(m,n)
        assert b == (m*n+1)//2, (m,n,b)
        if m==3 and n>=2:
            assert ways == (1 if n%2 else 2), (m,n,ways)
        print(f"GRID {m}x{n}: maximum={b} number_of_maximizers={ways} forbidden_triples={bad}")
        total += 1 << (m*n)
    print(f"DIRECT_OK rectangles={len(shapes)} subsets={total}")
    for m,n,target in [(2,2,2),(2,3,3),(3,2,3),(3,3,5)]:
        b, ways, bad = count(m,n)
        assert b == target
        print(f"TILE_OK {m}x{n} maximum={b} optimal_sets={ways}")
    d2, ways2, _ = count(3,4,d=2)
    assert d2 == 7
    print(f"STRICTNESS_OK grid_3x4_d2={d2} grid_3x4_d3=6")
    print('VERIFICATION_OK')

if __name__ == '__main__':
    main()
