# Order-two torsion and a Moore-space decomposition for the dodecahedral perfect-matching complex

## Finding

Let \(D=GP(10,2)\) be the 20-vertex dodecahedral graph. The *perfect-matching complex* \(\mathcal P(D)\) has as vertices the 30 graph edges, and its simplices are exactly those edge sets extendable to a perfect matching of \(D\). There is a homotopy equivalence

\[
\mathcal P(D)\simeq M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^{20}S^3,
\]

where \(M(\mathbb Z/2\mathbb Z,2)=S^2\cup_{2}e^3\) is the simply connected Moore space obtained by a degree-two three-cell attachment. Consequently

\[
\widetilde H_i(\mathcal P(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&i=2,\\
\mathbb Z^{20},&i=3,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular, the nontrivial integral torsion prevents this complex from having the homotopy type of a wedge of spheres.

## Assumptions and scope

Index vertices by \(u_0,\ldots,u_9,v_0,\ldots,v_9\), with subscripts modulo ten. The edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), for every \(i\in\mathbb Z/10\mathbb Z\). This is a standard model of the dodecahedral graph, with 20 vertices, 30 edges, and degree three at every vertex.

A perfect matching means ten pairwise vertex-disjoint graph edges covering all twenty graph vertices. A face of \(\mathcal P(D)\) is a nonempty subset of the edges of at least one perfect matching, together with the usual empty face. The complex is **not** the ordinary matching complex, which also contains matchings that cannot be completed to a perfect matching.

The result is an exact statement about this finite simplicial complex; it makes no claim about all fullerenes, about general cubic graphs, or about arbitrary complexes of perfect matchings.

## Proof

**Complete face enumeration.** Give the 30 graph edges their lexicographically sorted endpoint-pair order and encode a subset by a 30-bit integer. Recursively choose the smallest uncovered graph vertex, pair it with each uncovered neighbor, and continue until all vertices are covered. This enumerates all perfect matchings exactly once. There are precisely 36. Taking every nonempty subset of these 36 ten-edge matchings, and deduplicating, gives exactly 30,503 nonempty simplices and the following face counts (indexed by number of vertices of the simplex, from one to ten):

\[
(30,375,2180,5790,8352,7440,4320,1620,360,36).
\]

**Acyclic matching.** For each edge index \(j=0,\ldots,29\) in order, pair each still-unpaired face \(F\) lacking \(j\) with \(F\cup\{j\}\) whenever the latter is also still unpaired; remove both faces from consideration. The exact implementation orders the remaining lower faces numerically at each stage, making the matching deterministic. It produces 15,231 distinct face–coface pairs and 41 critical faces: one in dimension zero, ten in dimension two, and thirty in dimension three. Orient a Hasse arrow upward precisely for a paired cover relation and downward for every other cover relation. Every nonempty simplex and every nonempty proper facet cover are included. The resulting directed graph has 30,503 vertices and 163,650 arrows; a complete topological sort visits all 30,503 vertices. Therefore the matching is acyclic, and discrete Morse theory gives a CW model with precisely these 41 cells.

**Exact integral attaching degrees.** The CW model has one zero-cell and no one-cells, so its two-skeleton is a wedge of ten two-spheres. The integral cellular boundary from the thirty critical three-cells to the ten critical two-cells can be obtained from the oriented simplicial chain complex by recursively canceling every matched two/three face pair. Every cancellation uses a coefficient \(\pm1\); the recursion follows the acyclic matching and terminates. In the fixed critical-face ordering of the verifier, the resulting matrix \(B\) is \(10\times30\) with entries in \(\{0,\pm1\}\). Direct binary Gaussian elimination shows \(\operatorname{rank}_{\mathbb F_2}B=9\). Exact Bareiss determinant reduction gives an order-ten minor of determinant \(2\), using all ten rows and zero-based columns \((0,2,4,5,6,7,8,10,11,26)\), and an order-nine minor of determinant \(-1\), using rows \((0,1,3,4,5,6,7,8,9)\) and columns \((0,4,5,6,7,8,10,11,26)\). Thus \(\operatorname{rank}_{\mathbb Q}B=10\), every order-ten minor is even, one order-ten minor has absolute value two, and an order-nine minor has absolute value one. The Smith invariant factors are therefore

\[
1,1,1,1,1,1,1,1,1,2.
\]

**From the cellular matrix to homotopy type.** Because \(\pi_2(\bigvee^{10} S^2)\cong\mathbb Z^{10}\), the attaching map of each three-cell is determined by its vector of integral degrees. Integral row operations correspond to homotopy self-equivalences of the wedge of two-spheres, and column operations correspond to reversible changes among three-cell attachments (cellular handle slides). The Smith reduction therefore identifies nine canceling two/three-cell pairs, one residual degree-two attachment, and twenty three-cells attached trivially. This proves the displayed homotopy equivalence, including the exact Moore summand and its location in degree two.

## Verification

The included, dependency-free `verify_dodeca_perfect.py` reconstructs the graph, all perfect matchings, every simplex and face incidence, the complete discrete-Morse matching, a full directed-cycle test, and the signed integer Morse boundary. It independently checks both stated exact minors and the rank over \(\mathbb F_2\). Run `python3 verify_dodeca_perfect.py` from the folder containing the verifier. Its complete expected output is included as `VERIFIER_OUTPUT.txt`. The computation proves the claim for this completely enumerated finite object, not for an infinite graph family. The matching and determinant certificates are independently checkable from the self-contained executable source, rather than inferred from solver logs.

## Relationship to prior work

Fujita's 2012 dodecahedron matching-enumeration work and 2013 study of Kekulé structures motivate the classical perfect-matching family; they count matchings rather than establish the integral homotopy type of the simplicial complex of all their subsets. The general concept of a perfect-matching complex is explicitly defined by Bayer, Jelić Milutinović and Vega; their honeycomb calculations concern different graph families. The 2015 discrete-Morse literature provides methodological context rather than this particular finite calculation. Later work on polygonal line tilings and on circular/Möbius ladder graphs likewise concerns different structures. The **ordinary** matching complex of the dodecahedral graph is a different complex and its known sphere-wedge decomposition does not determine the extension-restricted perfect-matching complex. Comparisons included these distinctions, aliases involving Kekulé structures and extendable matchings, and searches for equivalent homology or Moore-space descriptions.

## Limitations

The 2012 Fujita article's abstract and bibliographic metadata were accessible, but its complete article was unavailable through the checked access path; no claim of full-text noncoverage is made for it. Searches and the inspected literature cannot exclude an unindexed equivalent theorem. The homotopy equivalence is established by a finite, reproducible combinatorial certificate; no geometric model for the embedded torsion cycle and no general formula for larger fullerenes is asserted. Independent scientific validation has not been performed.

## References

1. S. Fujita, “The Restricted-Subduced-Cycle-Index (RSCI) Method for Counting Matchings of Graphs and Its Application to Z-Counting Polynomials and the Hosoya Index as Well as to Matching Polynomials,” *Bulletin of the Chemical Society of Japan* **85** (2012), 439–449, published 2012-04-10; DOI: `10.1246/bcsj.20110319`.
2. S. Fujita, “Restricted Enumerations by the Unit-Subduced-Cycle-Index (USCI) Approach. IV. The Restricted-Subduced-Cycle-Index (RSCI) Method for Enumeration of Kekulé Structures and of Perfect Matchings of Graphs,” *MATCH Commun. Math. Comput. Chem.* **69** (2013), 333–354.
3. D. Taylan, “Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs,” preprint (2015), `arXiv:1501.06754`.
4. M. Bayer, M. Jelić Milutinović and J. Vega, “Perfect Matching Complexes of Honeycomb Graphs,” *Electronic Journal of Combinatorics* **30** (2023), P2.45; DOI: `10.37236/11525`; preprint `arXiv:2209.02803`.
5. H. Chandrakar and A. Singh, “Perfect Matching Complexes of Polygonal Line Tilings,” `arXiv:2407.05809` (2024).
6. A. Agarwal and B. Basak, “The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs,” `arXiv:2608.30601` (2026).
