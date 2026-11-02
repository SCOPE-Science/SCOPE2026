"""Exhaustive minimum total-domination exchange census on the dodecahedral graph.

Requires Python 3.10+ and NetworkX 3.x. Run: python verify_dodeca_total_direct.py
"""
from collections import Counter
from itertools import combinations
import networkx as nx

G = nx.dodecahedral_graph()
assert len(G) == 20 and G.number_of_edges() == 30
GP = nx.Graph()
for i in range(10):
    GP.add_edge(i, (i+1)%10)
    GP.add_edge(i, i+10)
    GP.add_edge(i+10, 10+(i+2)%10)
assert nx.is_isomorphic(G, GP)
N = {v: frozenset(G.neighbors(v)) for v in G}
V = sorted(G)

def total(S):
    return all(N[v].intersection(S) for v in V)

# Every possible cardinality seven candidate is tested, and the degree bound
# rules out cardinalities below seven: 3|S| >= |V| for total domination.
assert not any(total(set(C)) for C in combinations(V, 7))
opt = [frozenset(C) for C in combinations(V, 8) if total(set(C))]
assert len(opt) == 190 and len(opt) == len(set(opt))

R = nx.Graph()
R.add_nodes_from(opt)
optset = set(opt)
for S in opt:
    for u in S:
        for v in V:
            if v not in S:
                T = frozenset((S - {u}) | {v})
                if T in optset:
                    R.add_edge(S, T)
assert R.number_of_nodes() == 190 and R.number_of_edges() == 360
assert Counter(dict(R.degree()).values()) == {0: 40, 4: 120, 8: 30}
comps = sorted(nx.connected_components(R), key=len, reverse=True)
assert list(map(len, comps)) == [150] + [1] * 40
main = R.subgraph(comps[0])
assert main.number_of_edges() == 360
assert nx.diameter(main) == nx.radius(main) == 10
assert set(nx.eccentricity(main).values()) == {10}
assert not nx.is_bipartite(main)

# Generate the complete automorphism group of the base graph and its action
# on selected vertex sets, rather than assuming the known group order.
auts = list(nx.isomorphism.GraphMatcher(G, G).isomorphisms_iter())
assert len(auts) == 120
unseen = set(opt)
orbits = []
while unseen:
    S = next(iter(unseen))
    orbit = {frozenset(mapping[v] for v in S) for mapping in auts}
    assert orbit <= unseen | (set(opt) - unseen)
    assert orbit <= set(opt)
    assert orbit <= unseen
    unseen -= orbit
    orbits.append((len(orbit), R.degree(S)))
assert Counter(orbits) == Counter({(10, 0): 1, (30, 0): 1,
                                 (30, 8): 1, (60, 4): 2})
# The frozen configurations are precisely the complements of chordless
# twelve-cycles. Count every twelve-subset of the original graph separately.
chordless_cycles = set()
for C in combinations(V, 12):
    C = frozenset(C)
    if all(len(N[v].intersection(C)) == 2 for v in C) and nx.is_connected(G.subgraph(C)):
        chordless_cycles.add(C)
assert len(chordless_cycles) == 40
frozen = {S for S in opt if R.degree(S) == 0}
assert frozen == {frozenset(set(V)-set(C)) for C in chordless_cycles}
P4_pair = nx.disjoint_union(nx.path_graph(4), nx.path_graph(4))
star_pair = nx.disjoint_union(nx.star_graph(3), nx.star_graph(3))
shape_count = Counter()
for S in frozen:
    H = G.subgraph(S)
    if nx.is_isomorphic(H, P4_pair):
        shape_count['two_four_vertex_paths'] += 1
    elif nx.is_isomorphic(H, star_pair):
        shape_count['two_three_leaf_stars'] += 1
    else:
        raise AssertionError('unrecognized frozen induced subgraph')
assert shape_count == {'two_four_vertex_paths': 30, 'two_three_leaf_stars': 10}
print('DODECAHEDRON_DIRECT_TOTAL_DOMINATION_PASS')
print('MINIMUM_SIZE 8; OPTIMAL_SETS 190; JUMP_EDGES 360')
print('CONNECTED_COMPONENTS 150 plus 40 isolated; MAIN_RADIUS_DIAMETER 10')
print('AUTOMORPHISM_ORBITS', sorted(orbits))
