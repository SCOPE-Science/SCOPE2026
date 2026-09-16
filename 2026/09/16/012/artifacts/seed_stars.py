"""Deterministic exploratory construction search; independently checked output."""
from itertools import combinations
from random import Random
from small_stars import is_saturated, matching_rank
import json


def union(g, h):
    n, edges = g
    k, other = h
    return n + k, edges + [tuple(n + x for x in e) for e in other]


def aggressive(g):
    n, edges = g
    return all(matching_rank([tuple(x for x in e if x != v)
                              for e in edges if v in e]) == 4 for v in range(n))


def main():
    rng = Random(20260916)
    seeds = {}

    def retain(g):
        n, edges = g
        d = 2 * n - len(edges)
        key = n % 5, d
        if d > 11 or (key in seeds and seeds[key][0] <= n):
            return
        assert is_saturated(n, edges)
        seeds[key] = g

    for n in range(1, 6):
        retain((n, list(combinations(range(n), 3))))
    sun = (6, [tuple(sorted((w, 2 + j, 2 + (j + 1) % 4)))
               for w in range(2) for j in range(4)])
    broken = (10, [(0, 2, 3), (4, 5, 6), (7, 8, 9)] +
              [(a, x, y) for a in (0, 1) for x, y in combinations(range(4, 7), 2)] +
              [(v, x, y) for v in (2, 3) for x, y in combinations(range(7, 10), 2)])
    double_star = (10, [(a, x, y) for a, group in ((0, range(2, 6)), (1, range(6, 10)))
                       for x, y in combinations(group, 2)] + [(2, 3, 6), (5, 8, 9)])
    lantern_edges = [(0, 1, 2), (3, 4, 5)]
    for i in range(3):
        group = tuple(range(6 + 3 * i, 9 + 3 * i))
        lantern_edges.append(group)
        lantern_edges.extend((v, x, y) for v in (i, i + 3)
                             for x, y in combinations(group, 2))
    lantern = 15, lantern_edges
    for g in (sun, broken, double_star, lantern):
        retain(g)
    assert aggressive(sun) and aggressive(lantern)
    retain((9, [(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),
                (1,2,3),(1,2,4),(3,5,6),(4,7,8),
                (5,6,7),(5,6,8),(5,7,8),(6,7,8)]))
    for n in range(6, 19):
        triples = list(combinations(range(n), 3))
        for trial in range(400):
            rng.shuffle(triples)
            edges = []
            neighbors = [set() for _ in range(n)]
            degrees = [0] * n
            for e in triples:
                if all(degrees[v] < 4 or len(neighbors[v] | (set(e) - {v})) <= 4
                       for v in e):
                    edges.append(e)
                    for v in e:
                        degrees[v] += 1
                        neighbors[v].update(set(e) - {v})
            retain((n, edges))
    for _ in range(5):
        snapshot = list(seeds.values()) + [sun, lantern]
        for g in snapshot:
            if not aggressive(g):
                continue
            for h in snapshot:
                if 2 * (g[0] + h[0]) - len(g[1]) - len(h[1]) <= 11:
                    retain(union(g, h))
    records = [{"r": r, "d": d, "n": n, "m": len(edges), "edges": edges,
                "aggressive": aggressive((n, edges))}
               for (r, d), (n, edges) in sorted(seeds.items())]
    print(json.dumps({"seeds": records,
                      "missing": [(r, d) for r in range(5) for d in range(5, 12)
                                  if (r, d) not in seeds]}, indent=2))


if __name__ == "__main__":
    main()
