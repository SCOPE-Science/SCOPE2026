"""Run with python3 output/artifacts/verify_burning.py; standard library only."""
from itertools import permutations
from burning_probe import solve


def graph(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def simulate(adj, sources, rounds):
    blue = set()
    for t in range(rounds):
        newly = {v for v, neighbors in enumerate(adj)
                 if len(neighbors & blue) >= 2}
        if t < len(sources):
            newly.add(sources[t])
        blue |= newly
    return len(blue) == len(adj)


def exhaustive(adj):
    # This uses ordered source lists and set updates, unlike the mask DP.
    for rounds in range(1, len(adj) + 1):
        for count in range(1, rounds + 1):
            for sources in permutations(range(len(adj)), count):
                if simulate(adj, sources, rounds):
                    return rounds, count, sources


def family(k, length, arms):
    edges = [(0, 1)]
    paths = []
    for i in range(arms):
        path = list(range(2 + i * length, 2 + (i + 1) * length))
        paths.append(path)
        edges += [(0, v) for v in path]
        edges += list(zip([1] + path[:-1], path))
    h = graph(2 + length * arms, edges)
    extra = [(1, v) for path in paths[k:] for v in path[1:]]
    g = graph(len(h), edges + extra)
    return h, g, paths


def main():
    edges = [(0, 1), (0, 3), (0, 4), (0, 6), (1, 2), (1, 4),
             (1, 5), (2, 4), (2, 5), (2, 6), (3, 6), (5, 6)]
    for name, es, expected in [('H', edges, (4, 2)),
                               ('G', edges + [(0, 5)], (3, 3))]:
        adj = graph(7, es)
        dp, enum = solve(adj), exhaustive(adj)
        assert dp[:2] == enum[:2] == expected
        print('Seven-vertex', name, 'DP:', dp, 'enumeration:', enum)

    for n in range(3, 10):
        path_edges = [(v, v + 1) for v in range(n - 1)]
        for name, es in [('path', path_edges),
                         ('cycle', path_edges + [(n - 1, 0)])]:
            expected_b = (n + 1) // 2 + 1
            expected_t = (n + 1) // 2 + (name == 'path' and n % 2 == 0)
            actual = solve(graph(n, es))[:2]
            assert actual == (expected_b, expected_t), (name, n, actual)
            print(name, n, 'computed', actual, 'cited', (expected_b, expected_t))

    h, g, _ = family(1, 3, 5)
    assert solve(h)[:2] == (5, 2)
    print('Small family k=1,L=3,m=5:', 'H', solve(h), 'G', solve(g))
    for q in range(1, 31):
        k, length, arms = q + 2, q + 4, q + 6
        h, g, paths = family(k, length, arms)
        assert simulate(h, [0, 1], length + 2)
        assert not simulate(h, [0, 1], length + 1)
        sources = [0, 1] + [path[-1] for path in paths[:k]]
        assert simulate(g, sources, length + 1)
        # With these early root/hub choices an unseeded long arm is still late.
        assert not simulate(g, [0, 1], length + 1)
    print('Family schedules checked for q=1..30; all assertions passed.')


if __name__ == '__main__':
    main()
