# Integral homotopy and symmetric-group characters of triangle-free two-matchings on seven labels

## Finding
Let \(T_7=L(K_7)\) be the triangular graph on the \(21\) edges of the complete graph on seven labeled vertices. For any simple graph \(G\), write \(\operatorname{CF}_3(G)\) for the abstract simplicial complex of vertex subsets that contain no three-clique in the induced subgraph. Set \(X=\operatorname{CF}_3(T_7)\).

The exact **integral homotopy type** is
\[
X\simeq S^4\vee\bigvee^{146}S^5.
\]
Its only nonzero reduced integral homology groups are \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z\) and \(\widetilde H_5(X;\mathbb Z)\cong\mathbb Z^{146}\). In particular, no integral torsion occurs.

The natural action of \(\mathfrak S_7\) by relabeling the seven original vertices acts trivially on \(\widetilde H_4(X;\mathbb Q)\), while
\[
\widetilde H_5(X;\mathbb Q)\cong S^{(5,1,1)}\oplus S^{(4,2,1)}\oplus 2S^{(4,1,1,1)}\oplus S^{(3,3,1)}\oplus S^{(3,2,1,1)},
\]
where \(S^\lambda\) denotes the rational Specht representation indexed by a partition \(\lambda\) of seven. The dimensions are respectively \(15,35,20,21,35\), so the decomposition has total dimension \(146\).

## Assumptions and scope
The original graph \(K_7\) is **simple and loopless**, and its seven vertices are distinctly labeled. Faces of \(X\) are simple edge subsets of \(K_7\); an edge set qualifies exactly when the selected graph has maximum degree at most two and no triangular cycle. This equivalence follows because every three-clique of \(L(K_7)\) is either three edges incident to one original vertex or the three edges of one original triangle. The result concerns this particular seven-vertex base graph, not all sizes or arbitrary host graphs. All homology is reduced unless otherwise stated.

## Proof
**1. Complete face classification.** Index the \(21\) edges \(\{a,b\}\) with \(0\le a<b<7\) in lexicographic order and encode an edge subset by a \(21\)-bit mask. There are exactly \(140=7\binom63\) forbidden three-edge stars and \(35=\binom73\) forbidden triangles, giving \(175\) minimal nonfaces of cardinality three. A recursive generator adds an edge only when its endpoints currently have degree below two and do not share a neighbor. It gives \(14{,}430\) nonempty faces, with the numbers in dimensions zero through six
\[
(21,210,1155,3570,5607,3507,360).
\]
The verifier also checks closure under deleting any chosen edge and enumerates every forbidden triple.

**2. A complete discrete-Morse matching.** Start with all nonempty faces unmatched. For each of the \(21\) edge coordinates in ascending lexicographic order, pair each remaining face without that coordinate with the remaining face obtained by adding the coordinate, whenever both exist; remove every such pair before processing the next coordinate. The resulting matching contains exactly \(7{,}018\) pairs. Only one zero-dimensional face, \(124\) four-dimensional faces and \(269\) five-dimensional faces remain critical. To prove admissibility rather than assume it, direct every face-poset cover relation downward except matched covers, which are directed upward. An exhaustive topological sort of this directed graph visits all \(14{,}430\) faces and all \(69{,}762\) cover relations, so the discrete-Morse matching is acyclic.

**3. The signed integral differential.** Orient each simplex by its increasing edge-coordinate order. For a matched lower simplex \(s\) and upper simplex \(u\), the coefficient \([u:s]\) is \(\pm1\), and its elimination is the exact integral relation
\[
[s]\longmapsto- [u:s]^{-1}\sum_{\substack{t\subset u\\|u\setminus t|=1\\ t\ne s}}[u:t]\operatorname{norm}(t).
\]
A critical face maps to itself and a matched upper face maps to zero. The acyclicity established in step 2 makes this recursive normalization terminate and gives the standard algebraically canceled Morse chain complex. There are no possible nonzero Morse boundaries except
\[
B:C_5^{\mathrm M}\cong\mathbb Z^{269}\longrightarrow C_4^{\mathrm M}\cong\mathbb Z^{124}.
\]
The verifier reconstructs every entry from gradient paths. Exactly \(3{,}171\) entries of \(B\) are nonzero and each has absolute value at most three. It then applies only integer unimodular row or column exchanges and integral row subtractions, finding \(123\) pivots of value \(\pm1\) and a completely zero remaining row. Thus \(B\) has Smith form \(\operatorname{diag}(1,\ldots,1,0)\) with \(123\) unit entries, proving the stated integral homology groups and absence of torsion. An independent simplicial-chain calculation modulo two yields consecutive boundary ranks \((20,190,965,2605,3001,360)\).

**4. From homology to the stated homotopy type.** Discrete-Morse theory supplies a CW homotopy model with one zero-cell, \(124\) four-cells and \(269\) five-cells and no other cells. Its four-skeleton is \(\bigvee^{124}S^4\). Each five-cell attaching map lies in
\[
\pi_4\left(\bigvee^{124}S^4\right)\cong\mathbb Z^{124},
\]
where this isomorphism is induced by degree coordinates. The integral Smith reduction consists of elementary basis changes among the four- and five-cells, and hence replaces \(123\) attaching maps by degree-one coordinate maps and all remaining attaching maps by nullhomotopic maps. Canceling the degree-one cell pairs leaves precisely one four-sphere and \(146\) five-spheres. In particular, this is a homotopy equivalence, not merely a homology match.

**5. Rational action of \(\mathfrak S_7\).** Every permutation of the seven labels induces a signed simplicial chain permutation; the sign is that of the induced reordering of chosen edge coordinates. The verifier computes its reduced Lefschetz trace \(L(g)\), the alternating sum of signed fixed-face traces minus the empty-face contribution, for one representative of each of the \(15\) cycle types of \(\mathfrak S_7\). Since homology is only in degrees four and five,
\[
L(g)=\chi_4(g)-\chi_5(g).
\]
Because \(H_4\) has rational dimension one, \(\chi_4\) is either the trivial or sign character. Taking \(\chi_4\) to be the sign character would force multiplicity \(-1\) of the trivial Specht character in \(\chi_5\), violating nonnegative representation multiplicities. Hence \(\chi_4=1\). The character \(1-L\) has nonzero Specht multiplicities exactly \(1,1,2,1,1\) at the five partitions displayed in the Finding. The verifier evaluates all \(15\) character inner products using an independently implemented rim-hook recurrence and verifies the full irreducible-character orthogonality table. No integrality assertion about the \(\mathbb Z[\mathfrak S_7]\)-lattice beyond its underlying free abelian group is made.

## Verification
Run `python3 verify.py` in a standard Python 3 installation. It uses only the standard library and regenerates all faces, forbidden triples, directed Hasse covers, critical cells, integral Morse boundary, unit-pivot reduction, original mod-two boundary ranks, the \(15\) Lefschetz traces, and the \(15\times15\) rational irreducible character orthogonality checks. The output is reproduced verbatim in `verification_output.txt`. The reconstructed signed Morse boundary has SHA-256 `9e76246e548fe76b1ed40ce808e042527171f32a0521ab734ed0480747af887c` under the code's documented row ordering and UTF-8 comma/newline serialization. These finite enumerations are exhaustive for the *specified* complex \(X\), not evidence for an arbitrary-size theorem.

## Relationship to prior work
Ghosh and Selvaraja [1] develop clique-free complexes, with results on shellability for specified chordal and clique-whiskered graph classes. Their theorem does not determine the homotopy type or representation of \(\operatorname{CF}_3(L(K_7))\); the triangular graph contains an induced four-cycle and is not chordal. Singh [2] studies higher matching complexes of complete graphs, but its stated complete-graph classifications do not impose the additional condition forbidding selected triangles. Bosch-Calvo, Grandoni and Jabal Ameli [3] study the same triangle-free two-matching *edge-set constraint* as an optimization problem, not its simplicial homotopy or symmetric-group homology. Jonsson [4], citing Andersen, computes torsion for a related seven-label degree-bounded graph complex **allowing loops**; that object is not the loopless, triangle-free complex here, and its torsion theorem does not imply this finding. Thus existing related homological and optimization results do not by themselves determine the present integral homotopy or \(\mathfrak S_7\) action. The status of unindexed earlier work remains a bibliographic uncertainty.

## Limitations
The result concerns only seven original labels and proves no formula for larger clique-free triangular graphs. It gives a full *rational* group representation in homology but no classification of its integral \(\mathbb Z[\mathfrak S_7]\)-module structure or equivariant homotopy type. The finite certificate is exhaustive but requires independent external mathematical examination before being regarded as independently validated. Searches cannot prove absolute priority.

## References
[1] Rakesh Ghosh and S Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623, initial public version 2026-02-10. https://arxiv.org/abs/2602.09623

[2] Anurag Singh, *Higher Matching Complexes of Complete Graphs and Complete Bipartite Graphs*, arXiv:2006.13632. https://arxiv.org/abs/2006.13632

[3] Miguel Bosch-Calvo, Fabrizio Grandoni and Afrouz Jabal Ameli, *A PTAS for Triangle-Free 2-Matching*, arXiv:2311.11869, initial public version 2023-11-20. https://arxiv.org/abs/2311.11869

[4] Jakob Jonsson, *Five-Torsion in the Homology of the Matching Complex on 14 Vertices*, arXiv:1203.5650, preprint of *Journal of Algebraic Combinatorics* **29** (2009), 81–90, including Andersen's seven-label degree-bounded calculation. https://arxiv.org/abs/1203.5650
