"""Exhaustive graph-level check for open-neighborhood NOR on matching-defected bicliques.

No external dependencies. Run: python3 check_graph.py
"""
from collections import Counter, defaultdict
from itertools import product


def graph_neighbors(p, q, k):
    neighbors = [set() for _ in range(p + q)]
    for i in range(p):
        for j in range(q):
            if i < k and j == i:
                continue
            neighbors[i].add(p + j)
            neighbors[p + j].add(i)
    return neighbors


def update(state, neighbors):
    value = 0
    for vertex, nbrs in enumerate(neighbors):
        if all(not (state & (1 << w)) for w in nbrs):
            value |= (1 << vertex)
    return value


def expected(p, q, k):
    hp, hq = (1 << p) - k - 1, (1 << q) - k - 1
    basins = Counter()
    basins[hp] += 1
    basins[hq] += 1
    basins[1] += k
    basins[hp * hq + 1] += 1
    basins[hq + 1] += k
    basins[hp + 1] += k
    basins[2] += k * (k - 1) // 2
    return basins


def check(p, q, k):
    nbrs = graph_neighbors(p, q, k)
    size = 1 << (p + q)
    nxt = [update(x, nbrs) for x in range(size)]
    assert all(nxt[nxt[nxt[x]]] == nxt[x] for x in range(size))
    cyc_count = Counter()
    orbit_basins = defaultdict(int)
    count_transient = 0
    for x in range(size):
        y = nxt[x]
        z = nxt[y]
        if y != x and z != x:
            count_transient += 1
        if z == y:
            orb = (y,)
        else:
            orb = (min(y, z), max(y, z))
        orbit_basins[orb] += 1
    for orb in orbit_basins:
        cyc_count[len(orb)] += 1
    profile = Counter(orbit_basins.values())
    assert cyc_count[1] == k + 2, (p, q, k, cyc_count)
    assert cyc_count[2] == (k + 1) * (k + 2) // 2, (p, q, k, cyc_count)
    assert profile == expected(p, q, k), (p, q, k, profile, expected(p, q, k))
    assert count_transient == size - (k + 2) ** 2, (p, q, k, count_transient)
    assert sum(len(orb) for orb in orbit_basins) == (k + 2) ** 2
    return size


def main():
    cases = states = 0
    for p, q in product(range(2, 7), repeat=2):
        for k in range(min(p, q) + 1):
            states += check(p, q, k)
            cases += 1
    print(f"PASS graph-level: {cases} parameter cases; {states} initial configurations checked")
    for p, q, k in [(3, 3, 3), (3, 5, 2), (4, 5, 4), (6, 6, 6)]:
        hp, hq = (1 << p) - k - 1, (1 << q) - k - 1
        print(f"p={p} q={q} k={k}: fixed={k+2}, two_orbits={(k+1)*(k+2)//2}, giant={hp*hq+1}, total={1 << (p+q)}")


if __name__ == "__main__":
    main()
