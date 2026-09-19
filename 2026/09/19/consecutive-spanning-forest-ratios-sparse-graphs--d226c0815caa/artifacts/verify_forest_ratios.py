import itertools
import math
import networkx as nx


def forest_counts(G):
    """Return F_s(G) for s=0,...,n by direct acyclic-edge-subset enumeration."""
    n = G.number_of_nodes()
    edges = list(G.edges())
    counts = [0] * (n + 1)

    for k in range(n):
        total = 0
        for choice in itertools.combinations(range(len(edges)), k):
            parent = list(range(n))
            rank = [0] * n

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            acyclic = True
            for idx in choice:
                u, v = edges[idx]
                ru, rv = find(u), find(v)
                if ru == rv:
                    acyclic = False
                    break
                if rank[ru] < rank[rv]:
                    ru, rv = rv, ru
                parent[rv] = ru
                if rank[ru] == rank[rv]:
                    rank[ru] += 1
            if acyclic:
                total += 1
        counts[n - k] = total
    return counts


def main():
    atlas = nx.graph_atlas_g()
    complete = {}
    for n in range(2, 8):
        complete[n] = forest_counts(nx.complete_graph(n))

    connected_graphs = 0
    eligible_level_instances = 0
    planar_graphs = 0
    planar_level_instances = 0
    violations = []
    planar_violations = []

    for G in atlas:
        n = G.number_of_nodes()
        if n < 2 or n > 7 or not nx.is_connected(G):
            continue
        connected_graphs += 1
        m = G.number_of_edges()
        counts = forest_counts(G)

        for s in range(2, n + 1):
            threshold = math.comb(n, 2) - math.comb(n - s, 2)
            if m <= threshold:
                eligible_level_instances += 1
                lhs = counts[s] * complete[n][s - 1]
                rhs = complete[n][s] * counts[s - 1]
                if lhs < rhs:
                    violations.append((n, m, s))
                if m < math.comb(n, 2) and lhs <= rhs:
                    violations.append((n, m, s, "non-strict"))

        if nx.check_planarity(G)[0]:
            planar_graphs += 1
            for s in range(2, n + 1):
                planar_level_instances += 1
                lhs = counts[s] * complete[n][s - 1]
                rhs = complete[n][s] * counts[s - 1]
                if lhs < rhs:
                    planar_violations.append((n, m, s))

    print(f"networkx={nx.__version__}")
    print(f"connected_graphs_n2_to7={connected_graphs}")
    print(f"eligible_level_instances={eligible_level_instances}")
    print(f"planar_graph_types={planar_graphs}")
    print(f"planar_level_instances={planar_level_instances}")
    print(f"levelwise_violations={len(violations)}")
    print(f"planar_violations={len(planar_violations)}")
    if violations or planar_violations:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
