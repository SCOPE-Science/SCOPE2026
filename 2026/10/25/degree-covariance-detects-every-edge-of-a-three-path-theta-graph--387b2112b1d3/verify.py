"""Exact finite checks for uniform spanning-tree degree covariance on theta graphs.

No external libraries are required.  Every counted spanning tree is independently
checked for connectivity, rather than accepted from the two-path deletion rule.
"""
from fractions import Fraction
from itertools import combinations, product


def theta_graph(lengths):
    paths = []
    nxt = 2
    for length in lengths:
        vertices = [0] + list(range(nxt, nxt + length - 1)) + [1]
        nxt += length - 1
        paths.append([(vertices[j], vertices[j + 1]) for j in range(length)])
    return nxt, paths


def spanning_tree_covariance(lengths):
    n, paths = theta_graph(lengths)
    edges = [edge for path in paths for edge in path]
    counts = [0] * n
    cross = [[0] * n for _ in range(n)]
    total = 0
    for removed in combinations(range(len(edges)), 2):
        adjacency = [[] for _ in range(n)]
        for j, (u, v) in enumerate(edges):
            if j not in removed:
                adjacency[u].append(v)
                adjacency[v].append(u)
        visited = {0}
        stack = [0]
        while stack:
            for v in adjacency[stack.pop()]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        if len(visited) != n:
            continue
        total += 1
        degree = [len(adjacency[v]) for v in range(n)]
        for i in range(n):
            counts[i] += degree[i]
            for j in range(n):
                cross[i][j] += degree[i] * degree[j]
    result = [[Fraction(total * cross[i][j] - counts[i] * counts[j], total * total)
               for j in range(n)] for i in range(n)]
    return paths, total, result


def predicted_entry(paths, lengths, u, v):
    W = sum(lengths[i] * lengths[j] for i in range(3) for j in range(i + 1, 3))
    path_of_edge = {}
    edge_list = []
    for i, path in enumerate(paths):
        for e in path:
            path_of_edge[e] = i
            edge_list.append(e)
    incident_u = [e for e in edge_list if u in e]
    incident_v = [e for e in edge_list if v in e]

    def cov(e, f):
        r, s = path_of_edge[e], path_of_edge[f]
        pr = Fraction(sum(lengths) - lengths[r], W)
        ps = Fraction(sum(lengths) - lengths[s], W)
        if e == f:
            return pr * (1 - pr)
        if r == s:
            return -pr * ps
        return Fraction(1, W) - pr * ps

    return sum((cov(e, f) for e in incident_u for f in incident_v), Fraction(0))


def local_closed_form(paths, lengths, u, v):
    W = sum(lengths[i] * lengths[j] for i in range(3) for j in range(i + 1, 3))
    edge_path = next((i for i, path in enumerate(paths) if any(set(e) == {u, v} for e in path)), None)
    if edge_path is None:
        return None
    r = lengths[edge_path]
    others = [lengths[i] for i in range(3) if i != edge_path]
    s, t = others
    if u in (0, 1) or v in (0, 1):
        return Fraction((s + t) * W - 4 * (s * s + s * t + t * t), W * W)
    return Fraction((s + t) * (W - 4 * (s + t)), W * W)


def run_checks():
    assertions = 0
    cases = 0
    for lengths in product(range(2, 8), repeat=3):
        paths, number_trees, C = spanning_tree_covariance(lengths)
        a, b, c = lengths
        assert number_trees == a * b + a * c + b * c
        assertions += 1
        n = len(C)
        for u in range(n):
            assert sum(C[u]) == 0  # Total spanning-tree degree is deterministic.
            assertions += 1
            for v in range(u + 1, n):
                assert C[u][v] == predicted_entry(paths, lengths, u, v)
                assertions += 1
                local = local_closed_form(paths, lengths, u, v)
                if local is None:
                    assert C[u][v] < 0
                    assertions += 1
                else:
                    assert C[u][v] == local and C[u][v] >= 0
                    assertions += 1
                    if C[u][v] == 0:
                        if sorted(lengths) == [2, 2, 2]:
                            pass
                        else:
                            assert sorted(lengths) == [2, 2, 3]
                            assert all(w not in (0, 1) for w in (u, v))
                            assert any(len(path) == 3 and set(path[1]) == {u, v} for path in paths)
                            assertions += 3
        cases += 1
    print(f"VERIFY_OK {cases} parameter triples; {assertions} exact checks")


if __name__ == "__main__":
    run_checks()
