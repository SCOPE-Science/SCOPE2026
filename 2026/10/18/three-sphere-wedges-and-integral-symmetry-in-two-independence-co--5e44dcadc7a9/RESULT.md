# Three-sphere wedges and integral symmetry in two-independence complexes of two-subset Kneser graphs

## Finding

For every integer \(n\geq5\), let \(G_n=\operatorname{KG}(n,2)\) have vertex set \(\binom{[n]}2\), with two vertices adjacent exactly when the represented two-subsets are disjoint. Let \(K_n=\operatorname{Ind}_2(G_n)\), the simplicial complex whose faces are vertex subsets inducing graph components of order at most two. Then

\[
K_n\simeq (\Delta^{n-1})^{(3)}\simeq\bigvee^{\binom{n-1}{4}}S^3.
\]

The symmetric group \(\mathfrak S_n\) permuting the ground set acts on the top reduced **integral** homology by

\[
\widetilde H_3(K_n;\mathbb Z)\cong_{\mathbb Z[\mathfrak S_n]}\bigwedge^4 V_n,
\qquad
V_n=\ker\!\left(\mathbb Z^n\xrightarrow{\sum}\mathbb Z\right).
\]

All other reduced integral homology groups vanish. In particular, the cases \(n=5,6,7,8\) have, respectively, \(1,5,15,35\) three-sphere summands. The \(n=5\) case is the Petersen graph and is previously known; the theorem's new scope is the entire family and its uniform integral symmetry module.

## Assumptions and scope

The Kneser graph is simple and undirected, and each two-subset of \([n]\) labels exactly one graph vertex. A face of \(K_n\) is a collection \(\mathcal F\) of two-subsets such that the disjointness graph on \(\mathcal F\) has maximum degree at most one. This is precisely the definition of two-independence: its induced connected components have one or two vertices. The theorem includes all integers \(n\geq5\), with no additional graph-theoretic hypotheses. The claimed group action is the natural ground-set action, not the action on an arbitrarily chosen sphere-wedge model.

## Proof

**1. Exact face classification.** Suppose \(\mathcal F\) contains disjoint edges \(ab\) and \(cd\) of the complete graph on \([n]\). Each of these is already adjacent to the other in the disjointness graph, so every third edge in \(\mathcal F\) must meet both \(ab\) and \(cd\). Every edge therefore lies in the four-point set \(Q=\{a,b,c,d\}\). Conversely, the full six-edge simplex supported by \(\binom Q2\) belongs to \(K_n\), because an edge of a complete four-point graph is disjoint from only its complementary edge. If instead \(\mathcal F\) is pairwise intersecting, the elementary classification of intersecting families of two-subsets says it lies in a star at a common point or in the three edges of a triangle. The triangle lies in a four-point simplex for \(n\geq5\). Therefore \(K_n\) is exactly the union of the star simplices \(S_i=\Delta(\{ij:j\ne i\})\), one per \(i\in[n]\), and the six-vertex simplices \(U_Q=\Delta(\binom Q2)\), one per four-subset \(Q\subset[n]\).

**2. One-dimensional core.** Write \(A=\bigcup_i S_i\). For distinct \(i,j\), \(S_i\cap S_j\) is the single vertex \(ij\), and three different stars have empty intersection. The nerve is consequently the complete graph on \([n]\), and the nerve lemma gives \(A\simeq(\Delta^{n-1})^{(1)}\). The identification is natural for permutations of \([n]\). Concretely, each star can be contracted relative to its original vertices onto radial segments joining its barycenter to those vertices, giving the barycentric subdivision of the complete graph.

**3. Two-dimensional core.** For each three-subset \(R=\{i,j,k\}\), introduce the triangular simplex \(T_R=\Delta(\{ij,ik,jk\})\). Let \(B=A\cup\bigcup_{|R|=3}T_R\). Its intersection \(T_R\cap A\) is exactly the three-edge boundary cycle of \(T_R\), and different triangles intersect each other only inside \(A\). Under the radial graph contraction just described, each boundary cycle runs once around the labeled triangle \(i,j,k\) of the nerve, with degree \(\pm1\). Thus attaching all \(T_R\) produces a CW model equivalent to the two-skeleton \((\Delta^{n-1})^{(2)}\), with its usual oriented integral cellular two-chains on labeled triples. In particular \(B\) is simply connected and \(\pi_2(B)\cong H_2(B;\mathbb Z)\).

**4. Octahedral three-cell attachments.** Fix any four-subset \(Q\). The intersection \(U_Q\cap B\) is the boundary of the octahedron on the six vertices \(\binom Q2\): its eight triangular facets are the four star triples (all three edges incident to one ground-set point) and the four triangle triples (all three edges among three ground-set points). The other three pairs of vertices are disjoint opposite edge-pairs and do not belong to \(B\). Hence \(U_Q\cap B\cong S^2\). Any two distinct \(U_Q\) meet within \(B\) because their ground-set intersection has at most three points. Since every \(U_Q\) is contractible, homotopy invariance of these cofibration pushouts replaces it by a three-cell attached along that octahedral sphere.

Orient \(Q=(0,1,2,3)\) and order its six pair-vertices \((01,02,03,12,13,23)\). Order the four triangle facets by their ground-set triples \((012,013,023,123)\), followed by the four star facets in point order. Direct signed simplicial boundary calculation produces an integral fundamental two-cycle with facet coordinates

\[
(1,-1,1,-1\ ;\ -1,1,-1,1).
\]

The semicolon separates triangle facets from star facets. The star facets lie in \(A\), so the image of the attaching sphere in the relative two-chain group \(C_2(B,A;\mathbb Z)\) is \((1,-1,1,-1)\), the negative of the ordinary oriented boundary of the abstract simplex \([0,1,2,3]\). This calculation is stable under relabeling \(Q\), so the resulting cellular third boundary is the usual tetrahedral boundary matrix (after choosing each third-cell orientation). Because \(B\) is simply connected, Hurewicz identifies \(\pi_2(B)\) with \(H_2(B;\mathbb Z)\); the attaching maps agree with those of \((\Delta^{n-1})^{(3)}\) in \(\pi_2\). It follows that \(K_n\simeq(\Delta^{n-1})^{(3)}\).

**5. Homotopy and multiplicity.** The augmented simplicial chain complex of the full simplex \(\Delta^{n-1}\) is exact. Its three-skeleton therefore has reduced homology only in degree three, where it is \(\ker(\partial_3)\). This free group has rank \(\binom{n-1}{4}\), by the standard binomial chain-rank recursion. The three-skeleton is two-connected (its two-skeleton is simply connected and its second homology vanishes). By Hurewicz, integral third-homology generators have representing three-spheres. Their wedge maps by a homology isomorphism to this simply connected, three-dimensional CW complex, and Whitehead's theorem gives the stated wedge equivalence.

**6. Integral equivariance.** The pair \((B,A)\) has naturally oriented triangle generators indexed by three-subsets of \([n]\), on which relabeling acts with the standard orientation signs. The octahedral relative fundamental cycles are naturally oriented by ordered four-subsets, and Step 4 identifies their cellular boundary with the standard exterior contraction \(\partial:\bigwedge^4\mathbb Z^n\to\bigwedge^3\mathbb Z^n\). Accordingly the top homology is the kernel of this \(\mathfrak S_n\)-equivariant integral map. The coordinate-sum homomorphism splits as an abelian-group map, giving \(\ker\partial=\bigwedge^4\ker(\sum)=\bigwedge^4V_n\). The identification is integral, not only rational.

## Verification

The included standalone `verify.py` enumerates the admissible faces independently from forbidden induced three-vertex subgraphs, checks the exact star/four-point cover of every face, calculates mod-two boundary ranks, and computes signed simplicial Lefschetz traces for selected ground-set permutations. It also checks the eight signed octahedral facets used in Step 4 by their ordinary integral boundary. The committed output `verification_output.txt` reproduces the checks for \(n\in\{5,6,7,8\}\): reduced mod-two Betti ranks \(1,5,15,35\) in degree three and zero elsewhere, and character samples matching the exterior fourth power of the standard representation. These finite computations support the proof but do not establish the infinitely many cases by themselves.

## Relationship to prior work

Sawant's 2026 work on vertex decomposability of higher-independence complexes proves an all-parameter theorem for **trees**, not for the nonchordal Kneser graphs considered here. Deshpande and Singh's earlier work treats such complexes in other specified graph families. Feng and Wang's 2024 Kneser study concerns the **ordinary** independence complex \(\operatorname{Ind}_1\), whose allowable faces are pairwise intersecting sets of two-subsets, not the larger \(\operatorname{Ind}_2\) studied here.

The particular \(n=5\) Petersen two-independence case already appears in prior mathematical records as a three-sphere. The present claim is a complete theorem for every \(n\geq5\), including the first triangle-containing case \(n=6\), with exact ranks for all \(n\) and a natural integral \(\mathfrak S_n\)-module structure. An existing computation for the Petersen graph does not imply these conclusions. Previous calculations of Kneser neighborhood and Čech complexes use different face conditions and do not cover this theorem. An unindexed equivalent result remains a bibliographic risk.

## Limitations

This theorem is specific to two-subset Kneser graphs, with higher-independence parameter fixed at two. It does not classify \(\operatorname{Ind}_r(\operatorname{KG}(n,k))\) for arbitrary \(r,k\), does not assert shellability or an equivariant wedge decomposition, and does not establish a new result for the known isolated Petersen case alone. The homotopy equivalence to the simplex skeleton need not be equivariant; the group-action statement applies to integral homology. Verification by computer is finite, while the infinite theorem relies on the structural proof above. Literature comparisons cannot rule out unindexed manuscripts.

## References

- R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first public 2026-05-24. https://arxiv.org/abs/2605.25150
- Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566, first public 2024-04-16. https://arxiv.org/abs/2404.10566
- P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first public 2020-01-15. https://arxiv.org/abs/2001.05448
