"""Exact finite-graph and periodic flat-band calculations for seven-cell witnesses.

Requires Python 3 with SymPy and NetworkX; uses exact integer/rational polynomial
arithmetic. The bundled graph6 list contains the 156 nonisomorphic simple graphs
on six vertices, in Read--Wilson Graph Atlas order (NetworkX graph_atlas_g).
"""
from pathlib import Path
import sympy as sp
import networkx as nx

x = sp.Symbol('x')
p2 = sp.Poly(x**2 + x - 4, x)
p3 = sp.Poly(x**3 + x**2 - 4*x - 2, x)
assert p2.is_irreducible and p3.is_irreducible
assert sp.discriminant(p2.as_expr(), x) == 17
assert sp.discriminant(p3.as_expr(), x) == 316
assert sp.gcd(p2, p3).degree() == 0

# The pairs (edge-list, 0/1 bridge selector, polynomial eigenvector, minimal polynomial).
a = 2*(x-1)
b = (x-1)**2
c = x*(x-1)-4
d = (x-1)*c
witnesses = [
    ([(0,3),(0,4),(1,3),(1,4),(2,3),(2,4),(2,5),(2,6),(5,6)],
     [0,0,1,1,0,0,0],
     [x+1,x+1,-2,2,2,-(x+2),-(x+2)], p2),
    ([(0,1),(0,3),(0,4),(1,3),(1,4),(2,3),(2,4),(2,5),(2,6),(5,6)],
     [1,1,1,1,1,1,0],
     [a,a,d,b,b,c,c], p3)
]
for edges, selector, vals, polynomial in witnesses:
    G = nx.Graph(); G.add_nodes_from(range(7)); G.add_edges_from(edges)
    assert nx.is_connected(G)
    assert 0 < sum(selector) <= 7
    A = nx.to_numpy_array(G, nodelist=range(7), dtype=int)
    A = sp.Matrix(A.tolist())
    vec = sp.Matrix(vals)
    sel = sp.Matrix(selector)
    # This verifies the coefficient of every formal Floquet mode exactly,
    # not merely a selection of sample quasimomenta.
    for expr in (A - x*sp.eye(7))*vec:
        assert sp.rem(sp.Poly(expr,x), polynomial).is_zero
    assert sp.rem(sp.Poly((sel.T*vec)[0], x), polynomial).is_zero
    assert any(not sp.rem(sp.Poly(expr,x),polynomial).is_zero for expr in vec)
    assert sp.rem(A.charpoly(x).as_poly(x),polynomial).is_zero

# Verify the exact 6-vertex exclusion over every atlas isomorphism class,
# INCLUDING DISCONNECTED motifs. Graph6 is frozen in this package.
records = Path(__file__).resolve().parent.joinpath('atlas_n6.graph6').read_bytes().splitlines()
assert len(records) == 156
assert len(set(records)) == 156
reference = [nx.to_graph6_bytes(G,header=False).strip()
             for G in nx.graph_atlas_g() if G.number_of_nodes() == 6]
assert len(reference) == 156 and records == reference
for record in records:
    G = nx.from_graph6_bytes(record)
    assert len(G) == 6 and not G.is_multigraph()
    A = sp.Matrix(nx.to_numpy_array(G,nodelist=sorted(G.nodes()),dtype=int).tolist())
    char = A.charpoly(x).as_poly(x)
    assert not sp.rem(char,p2).is_zero
    assert not sp.rem(char,p3).is_zero

print('VERIFIED: two connected seven-cell witnesses; five distinct real flat-band values;')
print('VERIFIED: no six-vertex simple graph in all 156 classes has either minimal polynomial.')
