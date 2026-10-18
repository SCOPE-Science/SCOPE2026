"""Independent census from *all* connected seven-vertex graph atlas types.
Requires NetworkX 3.6.1. Every connected graph has a non-cut vertex,
so deleting a suitable vertex leads to a connected seven-vertex graph.
"""
from collections import defaultdict
import itertools
import json
import networkx as nx


def is_outerplanar(graph):
    extended = nx.Graph(graph)
    apex = len(graph)
    extended.add_node(apex)
    for node in graph:
        extended.add_edge(node, apex)
    return nx.check_planarity(extended, counterexample=False)[0]


def color_cells(graph):
    nodes = tuple(graph)
    colors = {x: 0 for x in nodes}
    while True:
        records = {}
        for x in nodes:
            counts = defaultdict(int)
            for y in graph.neighbors(x):
                counts[colors[y]] += 1
            records[x] = (colors[x], tuple(sorted(counts.items())))
        rank = {record:k for k,record in enumerate(sorted(set(records.values())))}
        changed = {x:rank[records[x]] for x in nodes}
        if len(set(changed.values())) == len(set(colors.values())):
            out = defaultdict(set)
            for x in nodes: out[changed[x]].add(x)
            return list(out.values())
        colors = changed


def in_one_orbit(graph,u,v):
    g=graph.copy()
    h=graph.copy()
    nx.set_node_attributes(g, False, 'pointed')
    nx.set_node_attributes(h, False, 'pointed')
    g.nodes[u]['pointed'] = True
    h.nodes[v]['pointed'] = True
    return nx.is_isomorphic(g, h, node_match=lambda a,b:a['pointed']==b['pointed'])


def orbit_refinement_fails(graph):
    for cell in color_cells(graph):
        for u,v in itertools.combinations(cell,2):
            if not in_one_orbit(graph,u,v):
                return True
    return False


def key(graph):
    degrees = {v:d for v,d in graph.degree()}
    return (len(graph.edges),tuple(sorted(degrees.values())),
            tuple(sorted((d,sum(degrees[w] for w in graph.neighbors(v)))
                         for v,d in degrees.items())))


def main():
    atlas = nx.graph_atlas_g()
    seven = [G for G in atlas if len(G)==7 and nx.is_connected(G)]
    assert len(seven)==853
    unique = defaultdict(list)
    tested = outer_candidates = 0
    for previous in seven:
        for mask in range(1,1<<7):
            tested += 1
            newer = nx.Graph(previous)
            newer.add_node(7)
            newer.add_edges_from((7,v) for v in range(7) if mask & (1<<v))
            if not is_outerplanar(newer):
                continue
            outer_candidates += 1
            bucket = unique[key(newer)]
            if not any(nx.is_isomorphic(newer, old) for old in bucket):
                bucket.append(newer)
    all_eight = [g for bucket in unique.values() for g in bucket]
    bad_eight = [g for g in all_eight if orbit_refinement_fails(g)]
    assert tested==108331
    assert len(all_eight)==777, len(all_eight)
    assert len(bad_eight)==4, len(bad_eight)
    structural = sorted((g.number_of_edges(),
                         tuple(sorted(d for v,d in g.degree())),
                         bool(nx.is_biconnected(g))) for g in bad_eight)
    assert structural == [
       (9,(2,2,2,2,2,2,3,3),False),
       (10,(2,2,2,2,2,2,4,4),False),
       (10,(2,2,2,2,3,3,3,3),True),
       (11,(2,2,2,2,3,3,4,4),True),
    ], structural
    for order in range(1,8):
        for graph in atlas:
            if len(graph)==order and nx.is_connected(graph) and is_outerplanar(graph):
                assert not orbit_refinement_fails(graph)
    print(json.dumps({'seven_vertex_connected_parents':len(seven),
                      'augmented_candidates_checked':tested,
                      'outerplanar_labeled_candidates':outer_candidates,
                      'eight_vertex_outerplanar_isomorphism_types':len(all_eight),
                      'eight_vertex_failing_types':len(bad_eight),
                      'failing_structural_signatures':structural,
                      'lower_orders_failing':0},indent=2,sort_keys=True))

if __name__=='__main__': main()
