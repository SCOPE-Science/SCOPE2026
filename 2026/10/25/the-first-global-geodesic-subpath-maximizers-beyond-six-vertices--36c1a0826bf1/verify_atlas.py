"""Supplementary independent graph-atlas/shortest-path check (NetworkX 3.6.1)."""
from collections import defaultdict
import networkx as nx

def number_of_geodesics(g):
    total = len(g)
    for x in g:
        for y in g:
            if x < y:
                total += sum(1 for _ in nx.all_shortest_paths(g, x, y))
    return total

atlas = [g for g in nx.graph_atlas_g() if len(g) == 7 and nx.is_connected(g)]
assert len(atlas) == 853
highest = max(number_of_geodesics(g) for g in atlas)
maximizers = [g for g in atlas if number_of_geodesics(g) == highest]
print(f"connected_atlas_isomorphism_classes={len(atlas)}")
print(f"maximum={highest}")
print(f"max_isomorphism_classes={len(maximizers)}")
for g in sorted(maximizers, key=lambda h: h.number_of_edges()):
    print(f"representative_edges={g.number_of_edges()} graph6={nx.to_graph6_bytes(g,header=False).decode('ascii').strip()} diameter={nx.diameter(g)}")
assert highest == 49 and sorted(g.number_of_edges() for g in maximizers) == [11,12]
print("atlas_crosscheck=PASS")
