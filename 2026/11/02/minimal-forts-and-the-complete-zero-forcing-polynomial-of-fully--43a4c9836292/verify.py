"""Independent finite checks for zero forcing on full subdivisions of complete graphs.

Run with Python 3.9+; no third-party dependencies. Finite checks complement
rather than replace the all-order proof.
"""
from itertools import combinations, product
from math import comb, factorial


def graph(n):
    edges = list(combinations(range(n), 2))
    adjacency = [0] * (n + len(edges))
    for i, (a, b) in enumerate(edges):
        w = n + i
        adjacency[a] |= 1 << w
        adjacency[b] |= 1 << w
        adjacency[w] = (1 << a) | (1 << b)
    return edges, adjacency


def is_fort(mask, adjacency):
    if mask == 0:
        return False
    return all(((mask >> v) & 1) or ((adjacency[v] & mask).bit_count() != 1)
               for v in range(len(adjacency)))


def all_minimal_forts(adjacency):
    # For any set containing a smaller fort, that smaller fort contains a
    # minimal fort; process masks by increasing cardinality.
    found = []
    for sz in range(1, len(adjacency) + 1):
        for elems in combinations(range(len(adjacency)), sz):
            mask = sum(1 << j for j in elems)
            if any((mask & sub) == sub for sub in found):
                continue
            if is_fort(mask, adjacency):
                found.append(mask)
    return set(found)


def expected_minimal_forts(n, edges):
    lookup = {edge: n + i for i, edge in enumerate(edges)}
    found = {(1 << n) - 1}
    for center in range(n):
        mask = ((1 << n) - 1) ^ (1 << center)
        for other in range(n):
            if other != center:
                mask |= 1 << lookup[tuple(sorted((center, other)))]
        found.add(mask)
    # Every undirected simple cycle is counted once by fixing its smallest
    # vertex first, and requiring its second vertex below its last vertex.
    from itertools import permutations
    for k in range(3, n + 1):
        for selected in combinations(range(n), k):
            first = selected[0]
            for route in permutations(selected[1:]):
                if route[0] > route[-1]:
                    continue
                order = (first,) + route
                mask = 0
                for j in range(k):
                    edge = tuple(sorted((order[j], order[(j + 1) % k])))
                    mask |= 1 << lookup[edge]
                found.add(mask)
    return found


def zero_forces(mask, adjacency):
    full = (1 << len(adjacency)) - 1
    while mask != full:
        additions = 0
        for v, neighborhood in enumerate(adjacency):
            if mask & (1 << v):
                available = neighborhood & ~mask
                if available and (available & (available - 1)) == 0:
                    additions |= available
        if not additions:
            return False
        mask |= additions
    return True


def is_forest(n, edges):
    parent = list(range(n))

    def root(v):
        while v != parent[v]:
            v = parent[v]
        return v

    for a, b in edges:
        aa, bb = root(a), root(b)
        if aa == bb:
            return False
        parent[aa] = bb
    return True


def predicted_zero_set(n, edges, mask):
    original = mask & ((1 << n) - 1)
    if not original:
        return False
    white_edges = [edge for i, edge in enumerate(edges)
                   if not (mask & (1 << (n + i)))]
    if not is_forest(n, white_edges):
        return False
    if original.bit_count() >= 2:
        return True
    only_original = original.bit_length() - 1
    return any((only_original in edge) and (mask & (1 << (n + i)))
               for i, edge in enumerate(edges))


def checks():
    for n in range(3, 6):
        edges, adjacency = graph(n)
        minimal = all_minimal_forts(adjacency)
        structural = expected_minimal_forts(n, edges)
        assert minimal == structural, (n, 'fort classification', minimal ^ structural)
        coeff_fort = [0] * (len(adjacency) + 1)
        for fort in minimal:
            coeff_fort[fort.bit_count()] += 1
        expected = [0] * len(coeff_fort)
        for k in range(3, n + 1):
            expected[k] += comb(n, k) * factorial(k - 1) // 2
        expected[n] += 1
        expected[2 * n - 2] += n
        assert coeff_fort == expected, (n, coeff_fort, expected)

        actual = [0] * (len(adjacency) + 1)
        predicted = [0] * len(actual)
        for mask in range(1 << len(adjacency)):
            actual[mask.bit_count()] += zero_forces(mask, adjacency)
            predicted[mask.bit_count()] += predicted_zero_set(n, edges, mask)
        assert actual == predicted, (n, actual, predicted)
        z_min = comb(n - 1, 2) + 1
        assert actual[z_min] == n * (n ** (n - 2) - 1)
        assert all(x == 0 for x in actual[:z_min])
        print('n={}, minimal_forts={}, minimum_seeds={}, total_seeds={}, coefficients={}'.format(
            n, len(minimal), actual[z_min], sum(actual), actual))

    # Independently check Cayley tree enumeration and the star exception via
    # Prüfer codes. Runs quickly through n=7 (16807 codes at n=7).
    for n in range(3, 8):
        seen = set()
        for code in product(range(n), repeat=n - 2):
            deg = [1] * n
            for v in code:
                deg[v] += 1
            edges = []
            for v in code:
                leaf = next(i for i in range(n) if deg[i] == 1)
                edges.append(tuple(sorted((leaf, v))))
                deg[leaf] -= 1
                deg[v] -= 1
            a, b = [i for i in range(n) if deg[i] == 1]
            edges.append(tuple(sorted((a, b))))
            seen.add(tuple(sorted(edges)))
        assert len(seen) == n ** (n - 2)
        nonstar_rooted = sum(1 for tree in seen for v in range(n)
                             if sum(v in e for e in tree) < n - 1)
        assert nonstar_rooted == n * (n ** (n - 2) - 1)
    print('PRUFER_COUNTS_OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    checks()
