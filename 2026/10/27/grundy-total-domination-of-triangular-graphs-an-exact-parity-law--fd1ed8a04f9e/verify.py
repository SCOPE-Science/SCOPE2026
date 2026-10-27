"""Independent exhaustive checks for Grundy total domination of triangular graphs.

No external packages; run: python verify.py
"""
from functools import lru_cache
from itertools import combinations
import json


def instance(n):
    edges = list(combinations(range(n), 2))
    neighbors = []
    for i, e in enumerate(edges):
        mask = 0
        for j, f in enumerate(edges):
            if i != j and (e[0] in f or e[1] in f):
                mask |= 1 << j
        neighbors.append(mask)
    return edges, neighbors


def direct_optimum(n):
    edges, nb = instance(n)
    m = len(edges)
    universe = (1 << m) - 1

    @lru_cache(None)
    def solve(selected):
        observed = 0
        for i in range(m):
            if (selected >> i) & 1:
                observed |= nb[i]
        undominated = universe & ~observed
        if not undominated:
            return (0, 1)
        longest, ways = -1, 0
        for i in range(m):
            if (selected >> i) & 1 == 0 and nb[i] & undominated:
                length, number = solve(selected | (1 << i))
                length += 1
                if length > longest:
                    longest, ways = length, number
                elif length == longest:
                    ways += number
        assert longest >= 0
        return longest, ways

    length, count = solve(0)
    assert length == 2 * ((n - 1) // 2)
    return {"n": n, "maximum_length": length, "ordered_maximum_sequences": count,
            "reachable_edge_set_states": solve.cache_info().currsize}


def check_unobserved_formula(n):
    edges, nb = instance(n)
    m = len(edges)
    universe = (1 << m) - 1
    for selected in range(1, 1 << m):
        seen = [False] * n
        observed = 0
        for i, e in enumerate(edges):
            if (selected >> i) & 1:
                seen[e[0]] = seen[e[1]] = True
                observed |= nb[i]
        expected = 0
        for i, e in enumerate(edges):
            isolated = (selected >> i) & 1 and (selected & nb[i]) == 0
            if (not seen[e[0]] and not seen[e[1]]) or isolated:
                expected |= 1 << i
        assert expected == (universe & ~observed), (n, selected)
    return (1 << m) - 1


def check_construction(n):
    edges, nb = instance(n)
    indices = {e: i for i, e in enumerate(edges)}
    a = (n - 1) // 2
    chosen = [(2 * i, 2 * i + 1) for i in range(a)]
    hub = 0
    leftover = 2 * a
    chosen.append((hub, leftover))
    chosen.extend((hub, 2 * i) for i in range(1, a))
    assert len(chosen) == 2 * a
    observed = 0
    for e in chosen:
        index = indices[tuple(sorted(e))]
        assert nb[index] & ~observed, (n, e)
        observed |= nb[index]
    assert observed == (1 << len(edges)) - 1
    return len(chosen)


results = {"method": "direct neighborhood-union search and separately derived incidence rule",
           "maximum_sequence_checks": [direct_optimum(n) for n in range(3, 9)],
           "unobserved_identity_checks": {str(n): check_unobserved_formula(n)
                                           for n in range(3, 8)},
           "explicit_constructions_checked": list(range(3, 51))}
for n in results["explicit_constructions_checked"]:
    assert check_construction(n) == 2 * ((n - 1) // 2)
print(json.dumps(results, indent=2, sort_keys=True))
