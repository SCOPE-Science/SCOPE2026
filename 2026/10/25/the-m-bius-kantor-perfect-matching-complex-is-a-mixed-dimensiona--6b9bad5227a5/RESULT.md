# The Möbius–Kantor perfect-matching complex is a mixed-dimensional sphere wedge

## Finding
Let \(G\) be the sixteen-vertex Möbius–Kantor graph, realized as the generalized Petersen graph \(\operatorname{GP}(8,3)\). Let \(\mathcal P(G)\) be the simplicial complex with one vertex for each edge of \(G\), whose simplices are precisely the nonempty edge sets contained in some perfect matching of \(G\), together with the empty simplex. Then
\[
\boxed{\mathcal P(G)\simeq \bigvee^{4}S^{2}\vee\bigvee^{8}S^{3}.}
\]
Equivalently, its reduced integral homology is \(\widetilde H_2\cong\mathbb Z^4\), \(\widetilde H_3\cong\mathbb Z^8\), and zero otherwise. This is a statement about the full homotopy type, not merely its homology.

## Assumptions and scope
The graph has vertices \(u_i,v_i\) for \(i\in\mathbb Z/8\mathbb Z\) and exactly the edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\), with subscripts reduced modulo eight. A *perfect matching* is a set of eight edges incident to each graph vertex exactly once. The complex \(\mathcal P(G)\) contains every subset of every such matching, and no other faces. In particular, it is not the ordinary matching complex: some pairwise disjoint edge sets of \(G\) do not extend to a perfect matching.

The reproducible certificate uses graph vertices \(0,\ldots,7\) for \(u_i\) and \(8,\ldots,15\) for \(v_i\). The twenty-four graph edges are indexed from zero after lexicographic sorting of their endpoint pairs, and each face is encoded by a twenty-four-bit integer whose set bits denote its graph edges. These conventions fully specify every enumeration and incidence sign below.

## Proof
**1. Exhaustive combinatorial model.** Choose the smallest as-yet-unmatched graph vertex and branch over each incident edge joining it to another unmatched vertex. This recursive enumeration produces exactly thirty-three distinct perfect matchings; the complete recursion appears in the standalone verifier. Enumerating the nonempty subsets of these matchings, with duplicate subsets identified by their bit masks, produces exactly \(6051\) faces and the dimension-indexed face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=(24,228,984,1842,1752,924,264,33).
\]

**2. An explicit acyclic matching.** On the nonempty face poset, repeatedly toggle the graph-edge index in the order
`23,22,21,6,19,11,17,4,20,14,13,12,7,8,9,15,18,10,5,16,3,2,1,0`.
At each stage pair every as-yet-unpaired face lacking that indexed edge with the face obtained by adjoining that edge, provided both are still unpaired. Remove each paired couple before the next stage. This constructs exactly \(3019\) face–coface pairs. The unmatched faces consist of one zero-dimensional face, four two-dimensional faces, and eight three-dimensional faces, with no other critical dimensions.

For independent acyclicity verification, orient every unmatched codimension-one face incidence from the larger face to the smaller, and each matched incidence in the opposite direction. The resulting graph has exactly \(6051\) vertices and \(27192\) oriented incidences. A topological sort visits all \(6051\) vertices. Therefore the face-poset matching is acyclic, and discrete Morse theory provides a CW model with one zero-cell, four two-cells and eight three-cells.

**3. Integral attaching degrees.** Order each simplex's vertices by increasing graph-edge index, so deleting its \(j\)-th vertex carries sign \((-1)^j\). To evaluate the Morse boundary exactly, let \(P\) project simplicial chains to critical cells along the paired lower/upper faces. For a critical face \(c\), set \(P(c)=c\); for a paired upper face set \(P(c)=0\). If lower face \(a\) is paired with upper face \(b\), let \(\varepsilon\in\{1,-1\}\) be its coefficient in \(\partial b\), and define
\[
P(a)=-\varepsilon\sum_{z\in\partial b,\,z\ne a}[z:\partial b]P(z).
\]
The acyclic matching ensures this gradient recursion terminates. Applying \(P\partial\) to all eight critical three-cells yields the identically zero \(4\)-by-\(8\) integral matrix. The critical two-cell masks, in increasing order, are `32848,2752512,4333568,5244928`; the critical three-cell masks are `278720,527364,527392,1097729,1163264,1327112,2113666,2162736`. Thus the zero differential is a reproducible exact signed calculation, not a conclusion inferred from field Betti numbers.

**4. Homotopy conclusion.** As there are no critical one-cells, the CW model has one vertex and its two-skeleton is \(\bigvee^4 S^2\), which is simply connected. By the Hurewicz theorem its second homotopy group maps isomorphically to second homology, \(\mathbb Z^4\). Accordingly, each three-cell attaching map is determined by its vector of integral cellular degrees. All eight vectors vanish by Step 3; hence all eight three-cells attach nullhomotopically. Their attachment gives precisely \(\bigvee^4S^2\vee\bigvee^8S^3\), proving the claim.

## Verification
Run `python3 verify_mobius_kantor_perfect_matching.py` (standard library only). It reconstructs the graph and its thirty-three perfect matchings, enumerates the complex, reconstructs all face incidences, executes the discrete-Morse pairing, checks global acyclicity by topological sort, and computes all signed integral Morse boundary coefficients by the recursion above. It independently computes the full mod-two simplicial boundary ranks
\[
(\operatorname{rank}\partial_1,\ldots,\operatorname{rank}\partial_7)
=(23,205,775,1059,693,231,33),
\]
which yield four degree-two and eight degree-three mod-two homology generators and no others. As a separate face-condition check, the verifier enumerates all \(11067\) nonempty ordinary graph matchings and identifies \(5016\) that cannot be extended to a perfect matching. Its minimal nonextendible sets consist of \(112\) three-edge and \(120\) four-edge matchings. The complete actual output is retained in `verification_output.txt` and ends with `VERIFY_OK`.

## Relationship to prior work
The Möbius–Kantor graph is the classical generalized Petersen graph \(\operatorname{GP}(8,3)\), as in Malnič and collaborators' covering-graph study [1]. Balasubramanian's exact matching-polynomial computation [2] already records thirty-three perfect matchings; that known count is a consistency check, not a novelty claim. The matching polynomial gives counts of matchings by cardinality, not their face-incidence pattern or the homotopy type of the extendibility subcomplex.

The published integral homotopy classification of the **ordinary** Möbius–Kantor matching complex [3] gives \(\bigvee^8 S^4\vee\bigvee^4 S^5\), a different space containing all \(11067\) ordinary matchings rather than only the \(6051\) extendible ones. Neither this different homotopy classification nor its proof implies the displayed theorem. The perfect-matching results of Bayer, Jelić Milutinović and Vega [4] concern finite planar honeycomb patches; those of Chandrakar and Singh [5] concern polygonal line tilings, not this graph. The classifications for Möbius **ladder** graphs and circular ladders by Agarwal and Basak [6] do not cover \(\operatorname{GP}(8,3)\): those ladders are different graph families, despite the similar name. Literature and indexed mathematical-record searches under the graph and complex aliases did not identify a covering classification.

## Limitations
This is a complete finite exact computation for one canonical graph; no theorem for all generalized Petersen graphs is asserted. Originality is assessed against inspected primary sources and searchable mathematical records, and an unindexed equivalent calculation remains possible. The homotopy claim depends on the explicit acyclic matching and integral signed attaching-map certificate; the independent mod-two homology ranks alone would not prove the integral homotopy equivalence. Independent mathematical audit has not yet been performed.

## References
1. A. Malnič, D. Marušič, Š. Miklavič and P. Potočnik, *Semisymmetric elementary abelian covers of the Möbius–Kantor graph*, arXiv:math/0510383, public 2005-10-18; https://arxiv.org/abs/math/0510383.
2. K. Balasubramanian, *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, *Symmetry* 17 (2025), 133; https://doi.org/10.3390/sym17010133.
3. *The Möbius–Kantor matching complex is a mixed-dimensional sphere wedge*, published mathematical record; https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-m-bius-kantor-matching-complex-is-a-mixed-dimensional-sphere--4bfded76792e.
4. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803; https://arxiv.org/abs/2209.02803.
5. K. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809; https://arxiv.org/abs/2407.05809.
6. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601; https://arxiv.org/abs/2608.30601.
