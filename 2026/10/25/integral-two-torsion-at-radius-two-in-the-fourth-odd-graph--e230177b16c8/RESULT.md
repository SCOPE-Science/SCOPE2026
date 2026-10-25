# Integral two-torsion at radius two in the fourth Odd graph

## Finding

Let \(O_4=\mathrm{KG}(7,3)\) be the fourth Odd graph, whose vertices are the \(35\) three-element subsets of \([7]=\{0,1,\ldots,6\}\) and whose edges join disjoint triples. Equip the vertices with the shortest-path metric and define the **inclusive** radius-two Vietoris–Rips complex
\[
X=\operatorname{VR}_{\le2}(O_4)=\operatorname{Cl}(O_4^2).
\]
Its integral homology is exactly
\[
H_1(X;\mathbb Z)\cong\mathbb Z/2\mathbb Z,\qquad H_2(X;\mathbb Z)\cong\mathbb Z^{90},
\]
with all other reduced integral homology groups zero. Its nonempty face vector, indexed by simplex dimensions zero through four, is \((35,280,560,280,56)\). There is an explicit reproducible sequence of \(280\) elementary simplicial collapses to a two-dimensional complex with face vector \((35,280,336)\).

The resulting torsion is visible in persistence: the scale-one clique complex is the graph \(O_4\), with first integral homology \(\mathbb Z^{36}\); at scale two it maps *surjectively* onto \(\mathbb Z/2\). At scale three the complex is a simplex. Consequently over a field of characteristic two one first-homology bar survives from scale one to three, whereas over a field of other characteristic no first-homology bar survives past scale two. At scale two the second-homology dimension is \(91\) in characteristic two and \(90\) otherwise.

## Assumptions and scope

This concerns precisely the ordinary graph metric on \(O_4\), without weighting, and closed inequalities in the Rips parameter. A vertex is encoded by an increasing triple of integers in \(\{0,\ldots,6\}\), ordered lexicographically; all simplices are subsets of this fixed 35-element list. Integral homology uses the standard increasing-vertex simplicial orientations. The classification is of **integral homology**, not a homotopy decomposition or an assertion about a minimal topological model. The primary subject is finite simplicial topology.

## Proof

**1. Graph distances and face enumeration.** For two distinct three-element subsets \(A,B\), the distance in \(O_4\) is one, two, or three according as \(|A\cap B|\) is zero, two, or one. For the distance-two case the complement of \(A\cup B\) is a common neighbor; for intersection one no common disjoint triple exists, but the graph has diameter three (verified by the explicit breadth-first search). The graph has \(35\) vertices, \(70\) edges, girth six, and diameter three. Thus two distinct vertices span an edge of \(O_4^2\) exactly when their triples are disjoint or meet in two points.

The standalone enumerator constructs all maximal cliques of this precisely defined graph by deterministic Bron–Kerbosch recursion, finds \(56\) maximal cliques of size five, and enumerates every face. This gives the stated face vector. Maximality follows from the complete clique backtracking, not from sampling.

**2. Explicit simple-homotopy reduction.** Enumerate all faces and their codimension-one cofaces. First remove the lexicographically first pair consisting of a four-vertex face and its unique currently present five-vertex coface; repeat until none remain. Next do the analogous operation for three-vertex faces having a unique four-vertex coface. Each selected face has exactly one active coface of the indicated dimension and none in any higher dimension, so it is a genuine free face and its removal is an elementary simplicial collapse. The deterministic program checks this uniqueness before each removal. There are \(56\) pairs at the first level and \(224\) at the second, totaling \(280\); the remaining complex is two-dimensional with \(35\) vertices, \(280\) edges and \(336\) triangles. Every homology group is preserved integrally by the collapses.

**3. Exact integral first homology.** Choose the lexicographic Kruskal spanning tree of the surviving connected one-skeleton, containing \(34\) edges. The integral cycle group of the graph identifies with a free abelian group on its \(280-34=246\) non-tree edges. Form the integer matrix \(B\) whose \(336\) columns are the signed boundary cycles of the remaining oriented triangles, projected onto the ordered non-tree edges: deleting the \(i\)-th vertex contributes coefficient \((-1)^i\). This is an exact presentation
\[
H_1(X;\mathbb Z)\cong\mathbb Z^{246}/\operatorname{im}_{\mathbb Z}(B).
\]
The supplied executable computes the column Hermite normal form of the full \(246\)-by-\(336\) integer matrix. It is square of order \(246\) and has diagonal entries consisting of \(245\) ones and one two. Consequently its column lattice has index two in \(\mathbb Z^{246}\); its quotient, having exactly two elements, is \(\mathbb Z/2\mathbb Z\). As a separate finite-field check, row reduction of \(B\) modulo two gives rank \(245\). The integral calculation, not the field check alone, proves the exact torsion statement.

**4. Higher homology.** Since the collapsed complex has dimension two, all homology above degree two vanishes. Its \(\mathbb Q\)-boundary rank is \(246\), hence \(H_2(X;\mathbb Z)\) is a free subgroup of \(\mathbb Z^{336}\) of rank \(336-246=90\). Connectedness gives \(\widetilde H_0=0\). The Euler characteristic is independently \(35-280+336=91\), consistent with the claimed ranks.

**5. Persistence consequences.** Because \(O_4\) is triangle-free, its scale-one Rips complex is the connected graph \(O_4\) with \(70-35+1=36\) integral circles. Adamaszek's fundamental-group surjectivity theorem for inclusions \(\operatorname{Cl}(G)\hookrightarrow\operatorname{Cl}(G^r)\) implies surjectivity here on \(H_1\), so the nonzero order-two class is born at scale one. The graph has diameter three and the scale-three complex is the full simplex. Universal coefficients identify \(\dim_{\mathbf F_2} H_2(X;\mathbf F_2)=91\), as opposed to \(90\) over any field of other characteristic. No extrapolation from finitely many graph sizes is used.

## Verification

Run `python verify_odd4.py` with a local Python installation providing the `sympy` dependency specified in `requirements.txt`. It independently regenerates vertex labels, all graph distances, the precise flag complex, every elementary free-face deletion, the entire integral signed boundary matrix and its exact Hermite normal form. Its expected terminal marker is `VERIFY_OK_ODD_GRAPH_O4_RIPS2_TORSION`. `verification_output.txt` contains the actual run output. The program also checks the characteristic-two rank \(245\) and the numerical Euler characteristic. Every finite calculation in this proof concerns an exhaustive finite object with 35 vertices.

## Relationship to prior work

M. Adamaszek, *Clique complexes and graph powers* (arXiv:1104.0433, first publicly posted 3 April 2011), establishes the general Rips/graph-power framework and, in Proposition 2.2, proves collapse to the original graph when the girth is at least \(3r+1\). The present graph has girth six, while radius two would require girth at least seven; that theorem does **not** cover the case here. Its Fact 2.1 supplies the persistence surjectivity used above, not the integral torsion computation. Q. Kong, B. Lv and K. Wang, *The Terwilliger algebra of Odd graphs* (arXiv:1112.0410), study the algebra of exactly this graph family but do not compute these clique-complex homology groups. Published results for independence complexes of Kneser graphs concern a different simplicial complex: pairwise intersecting triples need not be edges in the present radius-two complex, while disjoint triples are edges here.

## Limitations

The theorem does not determine the homotopy type or fundamental group of \(X\), nor the full integral persistence module in dimensions beyond those specified. The exact integer calculation depends on reproducibly running the stated finite algorithm and the SymPy implementation of Hermite normal form, rather than a separately listed hand-checked full normal-form transformation. Comparison with available literature does not rule out an unindexed equivalent presentation of this particular 35-vertex flag complex.

## References

1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (initial public version 2011-04-03), https://arxiv.org/abs/1104.0433, especially §2, Fact 2.1 and Proposition 2.2.
2. Q. Kong, B. Lv, K. Wang, *The Terwilliger algebra of Odd graphs*, arXiv:1112.0410 (initial public version 2011-12-02), https://arxiv.org/abs/1112.0410, especially §1 and §3.
3. The exhaustive integer-chain verifier `verify_odd4.py`, included with this result.
