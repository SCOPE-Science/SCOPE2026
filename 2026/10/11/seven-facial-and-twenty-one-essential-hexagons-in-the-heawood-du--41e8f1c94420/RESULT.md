# Seven facial and twenty-one essential hexagons in the Heawood dual of Möbius' torus
## Finding
Let \(K\) be Möbius' seven-vertex torus triangulation with facets
\[
124,126,134,137,156,157,235,237,245,267,346,356,457,467.
\]
For a simplicial \(1\)-cocycle \(z\in Z^1(K;\mathbf F_2)\), write \(\operatorname{wt}(z)\) for the number of edges on which \(z\) is nonzero. For a cohomology class \(\xi\in H^1(K;\mathbf F_2)\), define
\[
W_\xi(t)=\sum_{z\in\xi} t^{\operatorname{wt}(z)}.
\]
Then \(H^1(K;\mathbf F_2)\cong\mathbf F_2^2\), and the four cohomology cosets have only two weight-enumerator types:
\[
W_0(t)=1+7t^6+21t^{10}+35t^{12},
\]
while for every nonzero \(\xi\),
\[
W_\xi(t)=7t^6+7t^8+21t^{10}+21t^{12}+8t^{14}.
\]
In particular, every nonzero class has one-cosystole \(6\), attained by exactly \(7\) cocycles.

Let \(H\) be the graph dual to the triangulation. It is the Heawood graph in its seven-hexagon torus embedding. Its \(28\) simple cycles of length \(6\) are exactly the supports of the \(28\) weight-six cocycles. Seven are boundaries of the seven dual faces and lie in the zero cohomology class. The other \(21\) are nonseparating, hence nonzero in mod-two first homology; under Poincaré duality they split evenly as \(7,7,7\) over the three nonzero classes. The published map-automorphism group \(7{:}6\) of order \(42\) has two orbits on these shortest dual cycles: the facial orbit of size \(7\) and the essential orbit of size \(21\).

## Assumptions and scope
The result concerns the fixed simplicial triangulation above, with coefficients in \(\mathbf F_2\). Edge support is measured in the primal triangulation. A primal cocycle is identified with the corresponding dual mod-two \(1\)-cycle by crossing each supported primal edge with its dual edge. The word “essential” means nonzero in \(H_1(T^2;\mathbf F_2)\), equivalently nonseparating for a simple closed curve on the torus. The automorphism statement uses the combinatorial automorphism group preserving this triangulation, not the full abstract automorphism group of the Heawood graph.

## Proof
The fourteen triangle equations for a simplicial \(1\)-cocycle have rank \(13\) over \(\mathbf F_2\). Since \(K\) has \(21\) edges, \(Z^1\) has dimension \(8\) and therefore contains \(256\) cocycles. The seven vertex coboundaries span a rank-
\(6\) subspace \(B^1\), so \(H^1=Z^1/B^1\) has dimension \(2\) and each cohomology coset contains exactly \(64\) cocycles.

Exhausting these \(256\) cocycles gives the displayed complete coset weight enumerators. Thus the zero coset contains exactly seven weight-six cocycles, and each nonzero coset contains exactly seven. The seven weight-six coboundaries are precisely the coboundaries of the seven individual vertices.

The dual graph has one vertex for each of the fourteen triangles and one edge for each of the twenty-one primal edges. It is connected, cubic and bipartite with parts of size \(7\); every pair of vertices in the same part has exactly one common neighbor. Hence it is the Levi graph of the unique \(2\)-\((7,3,1)\) design, the Fano plane, and therefore is the Heawood graph. A six-cycle of this Levi graph corresponds to a noncollinear triple of Fano points, so there are \(\binom{7}{3}-7=28\) such cycles.

Under primal-dual edge correspondence, the cocycle equation on a triangle is exactly the even-degree condition at the corresponding dual vertex. Thus every cocycle support is an even subgraph of \(H\). Since \(H\) has girth \(6\), every nonempty even subgraph with six edges is one simple six-cycle. The exhaustive calculation gives exactly \(28\) weight-six cocycles, so their supports coincide with all \(28\) six-cycles of \(H\). The seven weight-six coboundaries are the boundaries of the seven dual faces surrounding primal vertices. The remaining \(21\) cycles represent the three nonzero Poincaré-dual classes, seven in each.

Köhler--Lutz give generators \((1,2,3,4,5,6,7)\) and \((1,3,2,6,4,5)\) for the action \(7^4\). Their closure has order \(42\) and preserves the facet set. Acting on the \(28\) six-cycle supports gives exactly two orbits, of sizes \(7\) and \(21\); the former is the zero-class facial set and the latter is the union of the three nonzero classes.

## Verification
The standalone verifier in `artifacts/verify.py` reconstructs the complex from the fourteen facets, performs exact binary row reduction, exhausts all \(256\) cocycles, reconstructs the dual graph and all simple six-cycles, verifies the Fano-incidence property, generates the published order-
\(42\) automorphism group, and computes both cycle orbits. Successful replay prints `VERIFY_OK` followed by the complete coset and orbit summary recorded in `artifacts/verification_output.txt`.

The finite enumeration is exhaustive: no probabilistic sampling, timeout inference or partial search is used. The topological identification of nonzero dual-cycle class uses standard mod-two Poincaré duality for a closed orientable surface.

## Relationship to prior work
Köhler and Lutz give the exact labeled triangulation, identify it as Möbius' seven-vertex torus, record face vector \((7,21,14)\), group \(7{:}6\), and the generating facet orbit; their paper also gives generators for the action. The paper does not discuss cocycles, cohomology, the Heawood dual, or dual-cycle support.

Classical Heawood-graph literature records that the abstract graph has \(28\) six-cycles, and standard descriptions of the Heawood map record the seven hexagonal torus faces. Those facts do not by themselves determine which nonfacial six-cycles are homologically essential, the \(7,7,7\) split among the three nonzero mod-two classes, the two embedding-preserving cycle orbits, or the complete cohomology-coset weight enumerators above.

A previously computed self-map classification of this same seven-vertex torus determines its \(42\) simplicial automorphisms and their action on first cohomology, but it does not compute cocycle supports, shortest dual cycles, weight enumerators, or the essential-hexagon orbit. A previously computed primal homology-support result concerns cycles in the triangulation's complete graph, not dual cycles obtained from cocycles, so it does not imply this classification.

## Limitations
The theorem is specific to this minimal triangulation and to mod-two cohomology. It does not claim that the edge-support enumerators are topological invariants of the torus under retriangulation. The full text of Szilassi's 1986 paper on regular toroids could not be retrieved during comparison; accessible metadata and secondary descriptions confirm the regular toroidal model but do not resolve whether an equivalent homology classification appears there. An older or poorly indexed computation under coding-theoretic, regular-map or dual-cycle terminology therefore remains a residual originality risk.

## References
1. E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:math/0506520v1, 24 June 2005; primary MSC 57Q15. See the explicit Möbius-torus facet list, Table 3, and Table 13.
2. L. Szilassi, *Regular Toroids*, Structural Topology 13 (1986), 69–80.
3. J. Baez, *Heawood Graph*, AMS Visual Insight, 1 August 2015; background source for the \(28\) six-cycles, Fano-plane interpretation, and seven-hexagon torus embedding.
