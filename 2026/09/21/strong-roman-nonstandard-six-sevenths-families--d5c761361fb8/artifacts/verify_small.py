import math
import networkx as nx


def is_strdf(G, labels):
    zeros = {v for v in G if labels[v] == 0}
    for v in zeros:
        ok = False
        for w in G.neighbors(v):
            z = sum(1 for u in G.neighbors(w) if u in zeros)
            if labels[w] >= 1 + math.ceil(z / 2):
                ok = True
                break
        if not ok:
            return False
    return True


def exact_gamma_at_most(G, upper):
    vertices = list(G)
    cap = math.ceil(max(dict(G.degree()).values()) / 2) + 1

    def compositions(total, n, max_part, prefix=()):
        if n == 0:
            if total == 0:
                yield prefix
            return
        for x in range(min(max_part, total) + 1):
            yield from compositions(total - x, n - 1, max_part, prefix + (x,))

    for weight in range(upper + 1):
        for vals in compositions(weight, len(vertices), cap):
            lab = dict(zip(vertices, vals))
            if is_strdf(G, lab):
                return weight
    return None


def subdivided_claw(triangular=False):
    G = nx.Graph()
    G.add_edges_from([
        (0, 1), (0, 2), (0, 3),
        (1, 4), (2, 5), (3, 6),
    ])
    if triangular:
        G.add_edge(1, 2)
    return G


def root_relaxed_min(G, root=0):
    vertices = list(G)

    def locally_valid(labels):
        zeros = {v for v in G if labels[v] == 0}
        for v in zeros:
            if v == root:
                continue
            ok = False
            for w in G.neighbors(v):
                z = sum(1 for u in G.neighbors(w) if u in zeros)
                if labels[w] >= 1 + math.ceil(z / 2):
                    ok = True
                    break
            if not ok:
                return False
        return True

    def compositions(total, n, prefix=()):
        if n == 0:
            if total == 0:
                yield prefix
            return
        for x in range(total + 1):
            yield from compositions(total - x, n - 1, prefix + (x,))

    for weight in range(7):
        for vals in compositions(weight, len(vertices)):
            labels = dict(zip(vertices, vals))
            if locally_valid(labels):
                return weight
    return None


S = subdivided_claw(False)
H = subdivided_claw(True)
print(f"root-relaxed minima: S={root_relaxed_min(S)} H_triangle={root_relaxed_min(H)}")

graphs = [G for G in nx.graph_atlas_g() if 3 <= len(G) <= 7 and nx.is_connected(G)]
violations = []
equality7 = []
for G in graphs:
    n = len(G)
    upper = math.floor(6 * n / 7)
    gamma = exact_gamma_at_most(G, upper)
    if gamma is None:
        violations.append(nx.to_graph6_bytes(G, header=False).decode().strip())
    if n == 7 and gamma == 6:
        equality7.append((
            nx.to_graph6_bytes(G, header=False).decode().strip(),
            sorted(d for _, d in G.degree()),
        ))

print(f"connected atlas graphs orders 3..7: {len(graphs)}")
print(f"bound violations through order 7: {len(violations)}")
print("order-7 equality graphs:")
for code, degrees in equality7:
    print(f"  {code} degrees={degrees}")
