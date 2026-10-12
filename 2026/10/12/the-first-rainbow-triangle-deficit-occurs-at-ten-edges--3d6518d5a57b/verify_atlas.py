"""Independent isomorphism-type check using NetworkX's complete graph atlas through order seven.
Requires NetworkX 3.x; this is corroboration, not the primary exhaustive proof.
"""
from itertools import combinations
import networkx as nx
best = {10: 0, 11: 0}
profiles = {10: 0, 11: 0}
for graph in nx.graph_atlas_g():
    if graph.number_of_nodes() > 7 or graph.number_of_edges() not in best:
        continue
    m = graph.number_of_edges()
    profiles[m] += 1
    if any(len(c) >= 5 for c in nx.find_cliques(graph)):
        continue
    count = sum(int(graph.has_edge(a, b) and graph.has_edge(a, c) and graph.has_edge(b, c))
                for a, b, c in combinations(graph.nodes(), 3))
    best[m] = max(best[m], count)
assert best == {10: 7, 11: 8}, (profiles, best)
print('atlas_profiles_10=%d; atlas_profiles_11=%d; max_nonK5_triangles_10=%d; max_nonK5_triangles_11=%d' %
      (profiles[10], profiles[11], best[10], best[11]))
