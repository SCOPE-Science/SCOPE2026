# A projective-plane summand in the closed-neighborhood complex of \(\mathrm{KG}(8,3)\)

## Finding
For the ordinary Kneser graph \(G=\mathrm{KG}(8,3)\), the closed-neighborhood simplicial complex has the complete homotopy type
\[
|\mathcal N[G]|\simeq\mathbb{RP}^{2}\vee\bigvee^{405}S^{2}.
\]
In particular, \(\widetilde H_1(\mathcal N[G];\mathbb Z)\cong\mathbb Z/2\mathbb Z\) and \(\widetilde H_2(\mathcal N[G];\mathbb Z)\cong\mathbb Z^{405}\), with all other reduced integral groups zero. The complex is pure of dimension ten and is not shellable.

## Assumptions and scope
Let the underlying set be \(\{0,1,\ldots,7\}\). Number the 56 three-subsets lexicographically. Graph vertices are these three-subsets, with distinct vertices adjacent exactly when disjoint. A closed neighborhood is the center together with its ten disjoint neighbors; \(\mathcal N[G]\) contains exactly the subsets of any of these 56 eleven-element sets. All assertions concern this finite graph and ordinary, *not open*, closed-neighborhood complex. The full face vector in dimensions zero through ten is
\[
(56,1540,8400,18270,25872,25872,18480,9240,3080,616,56).
\]
Every maximal simplex has dimension ten. The reproducibility algorithm uses exact integer bitmasks and the standard increasing-vertex orientation of edges and triangles.

## Proof
**1. Exhaustive elementary collapse.** Generate all nonempty simplices from the 56 distinct closed neighborhoods. There are exactly 111,482. At each stage, among codimension-one faces belonging to exactly one higher face, choose the face of smallest size and then smallest integer bitmask; delete it and its unique coface. This deterministic procedure makes 54,910 valid elementary pairs and leaves exactly 56 vertices, 628 edges, and 978 triangles. A free face with one immediate coface has no coface of higher codimension, since such a face would force at least two immediate cofaces. Thus every deletion is an elementary simplicial collapse and preserves homotopy type.

**2. An acyclic two-dimensional cell matching.** On that residual complex, order edges and triangles by bitmask. Maintain for each edge the number of triangles not yet processed. If an edge belongs to exactly one unprocessed triangle, choose one such edge using the deterministic seed-zero pseudorandom rule, and pair it with that triangle. Otherwise declare a triangle critical, prioritizing those with the most incident edges currently of triangle-degree two (again using the stated fixed tie-break rule). Remove the chosen triangle from the unprocessed set and repeat. This makes 569 edge–triangle pairs and declares 409 triangles critical. The other 59 edges form a connected graph; its lexicographic spanning tree has 55 edges, leaving four non-tree edges. Matching 55 non-root vertices with tree edges yields one critical vertex, four critical edges, and 409 critical triangles. Orient every Hasse incidence upwards for a matched pair and downwards otherwise. A complete topological sort of all 1,662 residual faces and 4,190 directed incidences verifies that the matching is acyclic.

**3. Recover exact attaching words, not only abelian boundary ranks.** Contract the spanning tree of unmatched edges. This is a homotopy equivalence and leaves a single vertex. Each of the 569 paired triangles contains its paired edge exactly once in its oriented attaching word. For a triangle with increasing vertices \(a<b<c\), the relation in oriented edges is \(e_{ab}e_{bc}e_{ac}^{-1}\). Solve this relation for the paired edge in terms of its two other edges. Recursively substitute their solutions whenever those are also matched. The dependency graph is acyclic, as independently verified in `verify.py`; therefore the pair cancellations can be ordered with no paired edge reintroduced into its own defining word. Every such elimination is a homotopy-preserving 1-cell/2-cell cancellation. The result is a one-vertex two-dimensional CW complex with four oriented one-cells and 409 two-cells. The critical attaching words are obtained by the same recursive substitutions and tree contraction.

**4. Exact final cellular cancellations.** Label the four surviving one-cell generators \(1,2,3,4\) by the lexicographic order of their original edge bitmasks. The computed list of 409 freely reduced attaching words includes relators \((2)\), \((4,-2)\), and \((-1,4)\). First cancel generator \(2\) using \((2)\); after substituting, cancel generator \(4\) using the resulting relator \((4)\); then cancel generator \(1\) using the resulting relator \((-1)\). All are 1-cell/2-cell cancellations, preserving homotopy. Exactly 406 two-cells remain, attached to the sole one-cell \(3\). Their integral degrees are precisely \(-2\) for 60 cells, \(0\) for 299 cells, and \(+2\) for 47 cells. Select any degree-two cell to obtain the standard CW space \(\mathbb{RP}^{2}\) (one zero-cell, one one-cell, one two-cell of degree two). Every other degree-zero or even-degree attaching map is nullhomotopic in this \(\mathbb{RP}^{2}\), since its fundamental group is \(\mathbb Z/2\mathbb Z\). Homotoping these remaining 405 maps to constants gives a wedge of 405 two-spheres. There are no higher cells after Step 1, proving the homotopy equivalence.

**5. Integral consequences.** The standard cellular chain complex of this wedge has a single nonzero boundary multiplication by two and 405 free two-cycles. This gives the asserted integral homology. A pure shellable ten-dimensional simplicial complex has torsion-free homology concentrated in top dimension; the nonzero degree-one torsion here excludes shellability.

## Verification
Run `python3 verify.py` with Python 3.10 or newer; no third-party packages or external files are required. It independently regenerates all faces, records and validates the 54,910 collapses, checks full Hasse acyclicity, recursively computes the unreduced and reduced attaching words, performs the three final cancellations, checks the exact degree histogram, and prints `ALL_VERIFY_OK`. Separate raw simplicial boundary ranks are also computed over the prime fields of characteristics two, three, and five: the second-boundary ranks are 572, 573, and 573 respectively. The corresponding reduced Betti pairs in dimensions one and two are \((1,406)\), \((0,405)\), and \((0,405)\). These independent field computations corroborate, but alone do not prove, the integral homotopy classification.

## Relationship to prior work
Matsushita's *Closed neighborhood complexes of graphs* (first publicly posted November 16, 2025) defines these complexes and proves broad suspension, Alexander-duality, and fundamental-group correspondences. Its inspected theorems and examples do not determine the homotopy type of \(\mathcal N[\mathrm{KG}(8,3)]\). The earlier Matsushita–Wakatsuki paper *Dominance complexes, neighborhood complexes and combinatorial Alexander duals* addresses primarily the **open**-neighborhood complex and dominance duals; it does not give this closed-neighborhood classification. The ordinary Lovász open-neighborhood complex of a Kneser graph is different from the complex studied here.

A more specialized prior closed-neighborhood theorem applies to triangle-free graphs whose four-cycles are pairwise edge-disjoint. That hypothesis fails here: for instance, the four-cycles with consecutive triples
\[(012,345,016,347)\quad\text{and}\quad(012,345,016,357)\]
share the edge between \(012\) and \(345\). Thus its graph-and-independent-square decomposition does not imply the present projective-plane summand. Available indexed searches under Kneser, Čech, closed-neighborhood, and equivalent terminology did not locate a covering classification; this is a qualified originality assessment, not a proof of global uniqueness.

## Limitations
The theorem is only for the 56-vertex graph \(\mathrm{KG}(8,3)\); it does not classify arbitrary Kneser graphs, larger radii, automorphism actions, or persistent homology. The direct CW proof is computational and requires running and inspecting the included exhaustive executable to reproduce its finite certificate. Other equivalent published or unindexed results may exist. No independent expert review or external formal proof has been performed.

## References
- T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, first posted November 16, 2025, v2 dated December 7, 2025, https://arxiv.org/html/2511.12608v2 .
- T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, first posted December 5, 2023, https://arxiv.org/html/2312.02639v2 .
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (background for discrete Morse matchings).
