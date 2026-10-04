from itertools import combinations


def cyclic_distance(n, a, b):
    d = (b - a) % n
    return min(d, n - d)


def is_edge(n, k, a, b):
    return a != b and cyclic_distance(n, a, b) <= k


def edge_color(n, k, a, b):
    """Return 0/1 for the constructive colorings in the theorem."""
    if n < 4 * k:
        return 1 if cyclic_distance(n, a, b) == k else 0

    assert n == 4 * k
    d = (b - a) % n
    if 1 <= d <= k:
        start = a
    else:
        d = (a - b) % n
        assert 1 <= d <= k
        start = b
    return (start // k) & 1


def orient_shorter_arc(n, k, u, v):
    d = (v - u) % n
    if d > n // 2:
        u, v = v, u
        d = (v - u) % n
    assert k < d <= n // 2
    return u, v, d


constructive_pairs = 0
for n in range(5, 81):
    for k in range(1, n // 2):
        if 4 * k < n:
            continue
        for u, v in combinations(range(n), 2):
            if is_edge(n, k, u, v):
                continue
            u0, v0, d = orient_shorter_arc(n, k, u, v)
            w = (u0 + k) % n
            assert is_edge(n, k, u0, w)
            assert is_edge(n, k, w, v0)
            assert cyclic_distance(n, u0, v0) == d
            assert edge_color(n, k, u0, w) != edge_color(n, k, w, v0)
            constructive_pairs += 1

# At n=4k, the antipodal pair 0,2k has exactly two common neighbors,
# and both corresponding two-edge paths use two distance-k edges.
for k in range(1, 31):
    n = 4 * k
    common = [
        (w, cyclic_distance(n, 0, w), cyclic_distance(n, w, 2 * k))
        for w in range(n)
        if is_edge(n, k, 0, w) and is_edge(n, k, w, 2 * k)
    ]
    assert common == [(k, k, k), (3 * k, k, k)]

# Independent brute-force search for a rainbow two-edge geodesic on small cases.
brute_pairs = 0
for n in range(5, 31):
    for k in range(1, n // 2):
        if 4 * k < n:
            continue
        for u, v in combinations(range(n), 2):
            if is_edge(n, k, u, v):
                continue
            assert any(
                is_edge(n, k, u, w)
                and is_edge(n, k, w, v)
                and edge_color(n, k, u, w) != edge_color(n, k, w, v)
                for w in range(n)
            )
            brute_pairs += 1

print(
    "ALL CHECKS PASSED; "
    f"constructive_nonadjacent_pairs={constructive_pairs}; "
    "boundary_cases=30; "
    f"independent_bruteforce_nonadjacent_pairs={brute_pairs}"
)
