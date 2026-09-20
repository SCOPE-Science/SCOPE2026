from fractions import Fraction
import networkx as nx


def average_maximal_matching_size(G):
    edges = list(G.edges())
    sizes = []
    for mask in range(1, 1 << len(edges)):
        used = set()
        matching = True
        for i, (u, v) in enumerate(edges):
            if not ((mask >> i) & 1):
                continue
            if u in used or v in used:
                matching = False
                break
            used.add(u)
            used.add(v)
        if not matching:
            continue
        maximal = all(
            ((mask >> i) & 1) or u in used or v in used
            for i, (u, v) in enumerate(edges)
        )
        if maximal:
            sizes.append(mask.bit_count())
    return Fraction(sum(sizes), len(sizes))


best = {}
counts = {}
for G in nx.graph_atlas_g():
    n = G.number_of_nodes()
    if n < 2 or n > 7 or not nx.is_connected(G):
        continue
    r = G.number_of_edges() - n + 1
    if r < 2 or n < r + 2:
        continue
    value = average_maximal_matching_size(G)
    key = (n, r)
    if key not in best or value < best[key]:
        best[key] = value
        counts[key] = 1
    elif value == best[key]:
        counts[key] += 1

for n, r in sorted(best):
    formula = Fraction(2 * r * (n - 3) + 1, r * (n - 3) + 1)
    assert best[(n, r)] == formula
    print((n, r), best[(n, r)], formula, counts[(n, r)], "OK")

print("verified", len(best), "parameter pairs")
