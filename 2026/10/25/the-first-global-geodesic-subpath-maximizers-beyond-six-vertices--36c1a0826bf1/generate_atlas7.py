"""Regenerate the bundled seven-vertex Graph Atlas masks (NetworkX 3.6.1)."""
import networkx as nx

assert len(nx.graph_atlas_g()) == 1253
edges = [(u, v) for u in range(7) for v in range(u + 1, 7)]
masks = []
for G in nx.graph_atlas_g():
    if len(G) == 7:
        masks.append(sum((1 << i) for i, (u, v) in enumerate(edges) if G.has_edge(u, v)))
assert len(masks) == len(set(masks)) == 1044
with open('atlas7_masks.txt', 'w', encoding='utf-8', newline='\n') as out:
    out.write(''.join(f'{m}\n' for m in masks))
print('regenerated_seven_vertex_masks=1044')
