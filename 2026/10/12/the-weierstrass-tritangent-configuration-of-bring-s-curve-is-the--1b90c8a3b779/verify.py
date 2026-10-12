from itertools import permutations, combinations
import networkx as nx
import sympy as sp

symbols = tuple(range(5))
points = list(permutations(symbols, 3))
point_set = set(points)
assert len(points) == 60

# A block is a fibre of one of the three two-coordinate projections.
blocks = {}
for omitted in range(3):
    kept = tuple(i for i in range(3) if i != omitted)
    for vals in permutations(symbols, 2):
        key = (omitted, vals)
        fibre = frozenset(p for p in points if tuple(p[i] for i in kept) == vals)
        assert len(fibre) == 3
        blocks[key] = fibre
assert len(blocks) == 60
assert len(set(blocks.values())) == 60

# Each of the three block families is a parallel class, and every point lies on one
# block from each family.
for omitted in range(3):
    fam = [b for (k, _), b in blocks.items() if k == omitted]
    assert len(fam) == 20
    assert set().union(*map(set, fam)) == point_set
    assert sum(len(b) for b in fam) == 60
    for b1, b2 in combinations(fam, 2):
        assert b1.isdisjoint(b2)
for p in points:
    assert sum(p in b for b in blocks.values()) == 3

# Collinearity is precisely Hamming distance one, hence the point graph is A(5,3).
G = nx.Graph()
G.add_nodes_from(points)
for a, b in combinations(points, 2):
    share = sum(a in B and b in B for B in blocks.values())
    hamming_one = sum(x == y for x, y in zip(a, b)) == 2
    assert (share == 1) == hamming_one
    assert share in (0, 1)
    if share:
        G.add_edge(a, b)
assert G.number_of_nodes() == 60
assert G.number_of_edges() == 180
assert set(dict(G.degree()).values()) == {6}

# The blocks are intrinsically recoverable: they are exactly the maximal cliques.
maximal_cliques = [frozenset(c) for c in nx.find_cliques(G)]
assert len(maximal_cliques) == 60
assert {len(c) for c in maximal_cliques} == {3}
assert set(maximal_cliques) == set(blocks.values())

# Exhaust the graph automorphisms. Since blocks are exactly the maximal cliques,
# this is also the type-preserving automorphism group of the incidence structure.
gm = nx.algorithms.isomorphism.GraphMatcher(G, G)
aut_count = sum(1 for _ in gm.isomorphisms_iter())
assert aut_count == 720

# Exhibit S5 x S3. S5 acts on the symbols and S3 on the coordinate positions;
# these actions commute and give 120*6 distinct automorphisms.
S5 = list(permutations(symbols))
S3 = list(permutations(range(3)))
def act(p, sigma, pi):
    # First permute coordinate positions, then relabel symbols.
    return tuple(sigma[p[pi[i]]] for i in range(3))

maps = set()
for sigma in S5:
    for pi in S3:
        image = tuple(points.index(act(p, sigma, pi)) for p in points)
        maps.add(image)
        assert all(G.has_edge(act(a, sigma, pi), act(b, sigma, pi)) for a, b in G.edges())
assert len(maps) == 720
assert len(maps) == aut_count

# The cubic used to label the three roots has Galois group S3 over Q.
t = sp.symbols('t')
f = t**3 + 2*t**2 + 3*t + 4
assert sp.Poly(f, t, domain=sp.QQ).is_irreducible
assert sp.discriminant(f, t) == -200
GG, _ = sp.polys.numberfields.galois_group(f, t)
assert GG.order() == 6
orders = sorted(g.order() for g in GG.elements)
assert orders == [1, 2, 2, 2, 3, 3]

print('VERIFY_OK points=60 blocks=60 incidence=60_3 point_graph=A(5,3) maximal_cliques=60 aut_type_preserving=720=S5xS3 cubic_disc=-200 cubic_galois=S3')
