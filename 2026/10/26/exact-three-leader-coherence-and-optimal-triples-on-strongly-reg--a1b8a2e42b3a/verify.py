"""Exact symbolic and rational checks for the three-leader strongly regular graph theorem.

Needs networkx 3.6.1 and sympy 1.14.0. All scalar checks are symbolic;
finite graph replay checks the identities, not all graphs.
"""
import itertools
import sympy as sp
import networkx as nx

b, mu = sp.symbols('b mu', positive=True)
patterns = {
  0: [],
  1: [(0, 1)],
  2: [(0, 1), (1, 2)],
  3: [(0, 1), (1, 2), (0, 2)],
}
S, D, phi = {}, {}, {}
for e, edges in patterns.items():
    A = sp.zeros(3)
    for i, j in edges:
        A[i, j] = A[j, i] = 1
    H = b * sp.eye(3) + A
    S[e] = sp.factor(sum(H.adjugate()))
    D[e] = sp.factor(H.det())
    phi[e] = sp.factor((sp.diff(S[e], b) + D[e] / mu) / S[e])

assert [S[i] for i in range(4)] == [3*b*b, (b-1)*(3*b+1), b*(3*b-4), 3*(b-1)**2]
assert all(sp.simplify(D[i]-target)==0 for i,target in enumerate([b**3, b*(b*b-1), b*(b*b-2), (b-1)**2*(b+2)]))
positive_gaps = [
  2*(b*b*(b-1) + 3*mu*(b+1))/(3*b*mu*(b-1)*(3*b+1)),
  2*(b**3*(b-2)+b+mu*(3*b*b-3*b+2))/(b*mu*(b-1)*(3*b-4)*(3*b+1)),
  2*(b*(b-1)**2+3*mu*(b-2))/(3*b*mu*(b-1)*(3*b-4)),
]
for i in range(3):
    assert sp.simplify(phi[i+1]-phi[i]-positive_gaps[i]) == 0


def test_graph(G):
    G = nx.convert_node_labels_to_integers(G)
    n = len(G)
    assert n >= 4 and nx.is_connected(G)
    k = G.degree(0)
    assert all(G.degree(i) == k for i in G.nodes)
    A = sp.Matrix(nx.to_numpy_array(G, dtype=int))
    lam_list = []
    mu_list = []
    for i, j in itertools.combinations(range(n), 2):
        common = len(set(G.neighbors(i)) & set(G.neighbors(j)))
        (lam_list if A[i,j] else mu_list).append(common)
    assert lam_list and mu_list
    assert len(set(lam_list)) == len(set(mu_list)) == 1
    la = lam_list[0]; mm = mu_list[0]
    B = k - la + mm
    assert B >= 3 and mm > 0
    P = 2*k-la+mm
    L = k*sp.eye(n)-A
    assert A*A == (la-mm)*A + (k-mm)*sp.eye(n) + mm*sp.ones(n)
    assert n*mm == k*(k-la-1)+mm*(k+1)
    assert (L + 2*sp.eye(n)) * ((2+B)*sp.eye(n)+A+sp.Rational(mm,2)*sp.ones(n)) == (4+2*P+n*mm)*sp.eye(n)
    kbar = n-k-1
    lambdabar = n-2-2*k+mm
    assert lambdabar >= 0 and kbar >= 1
    if lambdabar > 0:
        min_e = 0
        optimal_count = n*kbar*lambdabar//6
        assert n*kbar*lambdabar%6==0
    elif kbar > 1:
        min_e = 1
        optimal_count = n*kbar*(kbar-1)//2
    else:
        min_e = 2
        optimal_count = n*(n-2)//2
    all_counts = {e:0 for e in range(4)}
    found = {}
    for triple in itertools.combinations(range(n), 3):
        e = sum(int(A[i,j]) for i,j in itertools.combinations(triple,2))
        all_counts[e] += 1
        if e in found:
            continue
        F = [i for i in range(n) if i not in triple]
        val = sp.trace(L.extract(F,F).inv())
        predicted = sp.Rational((n-4)*P-n*k,n*mm)+phi[e].subs({b:B,mu:mm})
        assert sp.simplify(val-predicted)==0,(n,k,la,mm,triple,e,val,predicted)
        found[e] = val
    assert min(e for e in all_counts if all_counts[e]) == min_e
    assert all_counts[min_e] == optimal_count
    assert len(found)>0
    for x,y in itertools.combinations(sorted(found),2):
        assert found[x] < found[y]
    return n, k, la, mm, found


def shrikhande_graph():
    G = nx.Graph(); V=list(itertools.product(range(4),repeat=2)); G.add_nodes_from(V)
    steps=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
    for x,y in V:
        for a,c in steps:
            G.add_edge((x,y),((x+a)%4,(y+c)%4))
    return G

Gs=[
  ('square',nx.cycle_graph(4)),
  ('pentagon',nx.cycle_graph(5)),
  ('Petersen',nx.petersen_graph()),
  ('triangular-five',nx.line_graph(nx.complete_graph(5))),
  ('rook-three',nx.cartesian_product(nx.complete_graph(3),nx.complete_graph(3))),
  ('rook-four',nx.cartesian_product(nx.complete_graph(4),nx.complete_graph(4))),
  ('Shrikhande',shrikhande_graph()),
  ('biclique-three',nx.complete_bipartite_graph(3,3)),
  ('multipartite-222',nx.complete_multipartite_graph(2,2,2)),
]
for name, G in Gs:
    n,k,la,mm,res=test_graph(G)
    print(name, (n,k,la,mm), {e:str(v) for e,v in res.items()})

petersen = test_graph(nx.petersen_graph())[-1]
assert petersen[0] == sp.Rational(91,30)
assert test_graph(nx.cycle_graph(5))[-1] == {1:sp.Integer(1), 2:sp.Rational(4,3)}
assert test_graph(nx.cartesian_product(nx.complete_graph(3),nx.complete_graph(3)))[-1][0] == sp.Rational(26,15)
assert test_graph(nx.cartesian_product(nx.complete_graph(4),nx.complete_graph(4)))[-1] == test_graph(shrikhande_graph())[-1]
print('VERIFY_OK: four exact symbolic triple orbits; three strictly positive symbolic gaps; nine exact strongly regular graphs, rational grounded inverses, exact spectral resolvent, optimal-triple count trichotomy, nonisomorphic same-parameter comparison')
