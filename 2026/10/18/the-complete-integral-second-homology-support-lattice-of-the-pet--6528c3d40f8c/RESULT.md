# The complete integral second-homology support lattice of the Petersen independence complex

## Finding

Let \(P=\mathrm{KG}(5,2)\) be the Petersen graph on the ten two-element subsets of \([5]=\{0,1,2,3,4\}\), two subsets being adjacent exactly when disjoint. Let \(K=\operatorname{Ind}(P)\). For every vertex set \(W\subseteq\binom{[5]}2\), set \(F=\binom{[5]}2\setminus W\). All homology groups below have integral coefficients unless stated otherwise.

**Complete induced-support theorem.** Each inclusion \(K[W]\hookrightarrow K\) is injective on second homology, with primitive image (torsion-free quotient). If \(F\ne\varnothing\), then

\[
\operatorname{rank}\widetilde H_2(K[W])=\left|\bigcap_{e\in F}e\right|.
\]

For \(F=\varnothing\), the rank is four. Therefore a proper induced subcomplex contributes nonzero second homology if and only if **every omitted vertex of \(P\), viewed as a two-subset of \([5]\), contains one fixed symbol**. The smallest contributing vertex sets have size six, and there are exactly five:

\[
W_i=\binom{[5]\setminus\{i\}}2,\qquad i=0,1,2,3,4.
\]

Each \(K[W_i]\) is the boundary of an octahedron, hence is simplicially isomorphic to \(S^0*S^0*S^0\cong S^2\). Their five oriented fundamental classes \(z_i\) generate \(\widetilde H_2(K)\cong\mathbb Z^4\), with the unique primitive relation \(z_0+z_1+z_2+z_3+z_4=0\), after the coherent orientation convention specified in the proof. For each proper \(W\), the image is exactly the subgroup spanned by the \(z_i\) with \(i\in\bigcap_{e\in F}e\); it is a direct summand of \(\widetilde H_2(K)\).

Under the natural action of \(S_5=\operatorname{Aut}(P)\), the integral second-homology lattice is the sign-twisted augmentation quotient

\[
\widetilde H_2(K)\cong\operatorname{sgn}\otimes\bigl(\mathbb Z^5/\mathbb Z(1,1,1,1,1)\bigr).
\]

In addition, for **every** inclusion of finite simple graphs \(H\subseteq G\), the associated inclusion of clique complexes of line graphs

\[
\operatorname{Cl}(L(H))\hookrightarrow\operatorname{Cl}(L(G))
\]

induces a split injection on integral second homology. Its cokernel is free abelian. In particular, an edge-increasing graph filtration produces no finite-death bars in degree two for these line-graph clique complexes. This naturality lemma is used to establish the complete Petersen result.

## Assumptions and scope

All graphs are finite, simple, undirected; an inclusion of graphs means inclusion of vertices and edges, without requiring vertex-inducedness. The line graph \(L(G)\) has one vertex per edge of \(G\), adjacent when the edges meet. The clique complex \(\operatorname{Cl}(L(G))\) consists of pairwise intersecting sets of edges. An induced restriction \(K[W]\) is the full subcomplex on the specified ten-vertex-index subset \(W\). A subgroup is *primitive* when its quotient is torsion-free. Degree-two homology uses ordinary unreduced chains, equivalent to reduced homology in this degree. No generalization to higher degrees or arbitrary graph-clique filtrations is claimed.

## Proof

**1. A natural integral model for the second homology of a line-graph clique complex.** Given \(G\), let \(X_G=\operatorname{Cl}(L(G))\). For every vertex \(v\) of positive degree, take the full simplex \(A_v\) on the edges incident with \(v\). Put \(A_G=\bigcup_v A_v\). Distinct \(A_u,A_v\) either have empty intersection or meet in precisely the one vertex representing edge \(uv\). Triple intersections are empty. The nerve of this cover is the underlying graph with isolated vertices removed. Because all nonempty intersections are simplices, the nerve lemma gives \(H_1(A_G;\mathbb Z)\cong H_1(G;\mathbb Z)\) and \(H_2(A_G;\mathbb Z)=0\). These identifications commute with inclusions of graphs: the cover is indexed by the original vertices, and inclusion enlarges individual simplices while preserving their incidence nerve.

Every family of at least three pairwise incident graph edges either has a common endpoint or consists of precisely the three edges of a graph triangle. Hence all simplices of \(X_G\) outside \(A_G\) are exactly the distinct two-simplices \(q_T\), one for each triangle \(T\) of \(G\); their boundaries lie in \(A_G\). The relative chain complex \(C_*(X_G,A_G)\) has a basis of these \(q_T\) in degree two and vanishes in every other degree. The pair long exact sequence therefore identifies \(H_2(X_G;\mathbb Z)\) with the kernel of

\[
\delta:\mathbb Z^{\{\text{triangles of }G\}}\longrightarrow H_1(G;\mathbb Z).
\]

Orienting each \(q_T\) compatibly, its boundary follows the three star simplices at the three vertices of \(T\); under the nerve identification it is the ordinary oriented three-edge cycle of \(T\). Since graph \(H_1(G;\mathbb Z)\) is the kernel of the ordinary edge-to-vertex boundary, we have the explicit, graph-inclusion-compatible lattice formula

\[
H_2(X_G;\mathbb Z)\cong
\ker\left(\partial_2:\mathbb Z^{\{\text{triangles of }G\}}
\longrightarrow\mathbb Z^{E(G)}\right).
\tag{1}
\]

For \(H\subseteq G\), formula (1) embeds the smaller kernel into the larger by setting new triangle coordinates to zero. Moreover the smaller kernel is exactly the intersection of the larger kernel with the coordinate sublattice \(\mathbb Z^{\{\text{triangles of }H\}}\). Thus it is primitive and its quotient is free abelian, proving the universal lemma without relying on an assumed naturality of a merely objectwise homotopy equivalence.

**2. The canonical object.** The complement of the Petersen graph is \(L(K_5)\). Consequently \(K=\operatorname{Cl}(L(K_5))\) and, for every \(W\), \(K[W]=\operatorname{Cl}(L(H_W))\), where \(H_W\) has edge set \(W\) on the five labels. Apply (1) to all \(H_W\).

For the complete graph \(K_5\), its two-dimensional clique skeleton is the two-skeleton of a four-simplex. Its integral two-cycles are exactly the boundaries of the five tetrahedral facets; there is one relation, coming from the boundary of the four-simplex. To see completeness integrally, the full four-simplex has an acyclic augmented simplicial chain complex: exactness in degree two says that the kernel of the triangle-to-edge boundary is the image of the tetrahedral-to-triangle boundary. Exactness in degree three says that its unique primitive relation is the boundary of the oriented four-simplex. Hence the cycle lattice has rank four, with no torsion.

Write \(d_i=\partial[0,\ldots,\widehat i,\ldots,4]\) using increasing simplex orientations and set \(t_i=(-1)^i d_i\). Then \(\sum_i t_i=0\). The lattice formula maps \(t_i\) to the fundamental two-cycle \(z_i\) of the six-vertex octahedral complex \(K[W_i]\). For each permutation \(\pi\in S_5\), its action on the tetrahedral facet boundaries satisfies \(\pi(t_i)=\operatorname{sgn}(\pi)t_{\pi(i)}\); this gives the asserted integral representation. The only integral relation is their sum, so any four \(z_i\) form an integral basis.

**3. Every restriction, not only minimum supports.** The full integral triangle-cycle lattice is represented by coefficient vectors \((a_0,\ldots,a_4)\in\mathbb Z^5\) modulo simultaneous addition of the same integer to all coordinates. The coefficient of the triangle whose complementary labels are \(i,j\) is, up to the fixed orientation sign, \(a_i-a_j\).

For a missing edge \(\{u,v\}\in F\), all three triangles containing that edge are absent from \(H_W\). Their coefficients vanish exactly when all \(a_i\) on \([5]\setminus\{u,v\}\) are equal. The complementary triples of any two missing edges intersect because two three-subsets of a five-set always intersect. Therefore, when \(F\ne\varnothing\), all coordinates outside the intersection \(I=\bigcap_{e\in F}e\) are forced to the same integer, while the coordinates indexed by \(I\) are free. Quotienting by common translation yields a free lattice of rank \(|I|\), with basis represented by \(t_i\) for \(i\in I\). If no edges are missing, all five coordinates are free modulo translation, giving rank four. The primitivity statement follows from Step 1.

Any nonzero rank for a proper restriction requires all omitted graph edges to contain a common label. The largest possible number of omitted edges under this constraint is four, namely an entire star of \(K_5\), so the sharp minimum \(|W|=10-4=6\) is attained only by the five complements \(W_i\). The graph \(H_{W_i}\) is \(K_4\) plus an isolated vertex, and its line graph is the octahedral graph \(K_{2,2,2}\). This completes the classification.

## Verification

The included standalone `verify.py` (Python standard library only) constructs the ten vertices as two-element subsets of five labels, enumerates all faces of the independence complex, computes second simplicial homology over \(\mathbb F_2\) for **all 1,024** induced restrictions, and compares every rank with the theorem's integer formula. It independently checks five minimum six-vertex supports, rank four and the unique mod-two relation among the five tetrahedral boundaries, and the signed Lefschetz character against \(\operatorname{sgn}(\pi)(\#\operatorname{Fix}(\pi)-1)\) for each of the 120 permutations. Its successful deterministic output includes `VERIFY_OK`.

This finite verifier corroborates the classification and symmetry but does not by itself prove integral primitivity or the all-graphs statement. Those are supplied by the relative-chain proof above, which does not use extrapolation from finite computations.

## Relationship to prior work

Linusson, Shareshian and Welker proved the homotopy type of the nonmatching complex \(\mathrm{NM}_2(K_n)\) in their 2004 preprint, including the previously known ambient sphere wedge. Goyal, Shukla and Singh's Lemma 3.2 gives the important earlier objectwise equivalence \(\operatorname{Cl}(L(G))\simeq\operatorname{Cl}(G)^{(2)}\). Neither ambient conclusion is new here. The first source also discusses symmetry-module questions, while the second provides the key topology of line-graph clique complexes.

The contribution asserted here is **the exact integral subgroup carried by every one of the 1,024 induced Petersen restrictions**, including primitive inclusion maps, the five shortest carriers and their only integral relation, and a graph-inclusion-level lattice model ensuring that these cycles never die. Goyal–Shukla–Singh's published equivalence substantially motivates the chain model; its objectwise assertion alone is not an explicit computation of these maps or integral image lattices. The graph-theoretic existence of five octahedral complements is itself known in the Petersen graph literature, and is not claimed as newly discovered.

## Limitations

The general split-injection lemma applies to second homology of **line-graph clique complexes along inclusions of underlying graphs**. It does not assert injectivity in degree one, at higher homological degrees, or for arbitrary clique-complex graph filtrations. The \(S_5\) decomposition is integral as a quotient lattice, but no unrelated representation classification is inferred. Existing literature may already contain an equivalent formulation of the full support profile or a naturality consequence not indexed by the searched terminology. The literature comparison does not establish absolute worldwide publication priority.

## References

1. S. Linusson, J. Shareshian and V. Welker, *Complexes of Graphs with Bounded Matching Size*, arXiv:math/0410345, first posted 2004-10-15, Theorem 1.1 and Section 1. https://arxiv.org/abs/math/0410345
2. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, first posted 2020-09-25, especially Lemma 3.2 and Section 3.1. https://arxiv.org/abs/2009.12130
3. A. E. Brouwer, *Petersen graph* reference page, specifically its description of five size-four cocliques with induced three-edge matchings on their six-vertex complements. https://aeb.win.tue.nl/graphs/Petersen.html
