# Integral higher-independence homotopy of the Dürer graph through cutoff three

## Finding
Let \(G=GP(6,2)\) be the twelve-vertex Dürer graph. Its first three higher-independence complexes satisfy the integral homotopy equivalences
\[
\operatorname{Ind}_1(G)\simeq S^2,\qquad
\operatorname{Ind}_2(G)\simeq \bigvee^{3}S^3\vee S^4,\qquad
\operatorname{Ind}_3(G)\simeq\bigvee^{9}S^5.
\]
Both inclusion maps \(\operatorname{Ind}_1(G)\hookrightarrow\operatorname{Ind}_2(G)\) and \(\operatorname{Ind}_2(G)\hookrightarrow\operatorname{Ind}_3(G)\) are nullhomotopic. The mixed-dimensional middle term is the essential new phenomenon: it is not determined by the face count or Euler characteristic alone.

## Assumptions and scope
The graph has vertices \(u_i,v_i\) for \(i\in\mathbb Z/6\mathbb Z\) and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\), with indices modulo six. Thus \(G\) has twelve vertices and eighteen edges. For \(r\in\{1,2,3\}\), a set \(A\subseteq V(G)\) is a simplex of \(\operatorname{Ind}_r(G)\) precisely when **every connected component** of the induced subgraph \(G[A]\) has at most \(r\) vertices. In particular, the cutoff-two complex is sometimes called the dissociation complex or the complex of induced maximum degree at most one. Empty faces are counted in the computational totals; they are not topological cells of the realized complex.

## Proof
**Exhaustive face construction.** Label \(u_i=i\), \(v_i=6+i\), for \(0\leq i<6\). The supplied `verify.py` enumerates all \(2^{12}=4096\) subsets independently by breadth-first component growth and by avoiding all induced connected subsets of cardinality \(r+1\). These two necessary-and-sufficient definitions agree on every input. The numbers of connected forbidden subsets are respectively \(18,32,66\). The augmented face counts, including the empty face, are respectively \(171,810,1469\).

**Acyclic elementary matching.** For each cutoff, process the vertices in label order. Pair every still-unmatched face omitting the current vertex with its still-unmatched one-vertex extension whenever the extension is a face. First perform the pairing on the augmented face poset; then release the empty-face/first-vertex pair, leaving one critical vertex. Reversing all matched nonempty codimension-one incidence arrows produces a directed acyclic graph, as verified by full topological sorting. The numbers of matched nonempty face pairs are \(84,401,721\), and the numbers of directed Hasse incidences checked are \(462,3180,6528\). Therefore discrete Morse theory gives CW models with nonzero critical-cell vectors
\[
\begin{array}{c|c}
r&\text{critical cells by dimension}\\ \hline
1&(0:1,\ 2:1)\\
2&(0:1,\ 3:4,\ 4:2)\\
3&(0:1,\ 3:1,\ 4:8,\ 5:16).
\end{array}
\]
All these finite counts and directed acyclicity checks are fully rerun by the standalone code.

**Integral attaching maps.** Compute oriented simplicial incidence signs by the ascending vertex order. For each critical higher cell, eliminate matched lower cells through signed gradient paths. The exact cellular Morse boundary for cutoff two is
\[
\partial^{(2)}_4=
\begin{pmatrix}
-1&-1\\0&0\\0&0\\0&0
\end{pmatrix}:\mathbb Z^2\longrightarrow\mathbb Z^4.
\]
A primitive \((-1)\) coefficient cancels one three/four cell pair. The residual CW complex has one zero-cell, three three-cells, and one four-cell with zero attaching degree. Since the three-skeleton is a wedge of three three-spheres and \(\pi_3\) of that wedge is its third homology, the last attaching map is nullhomotopic. This proves the middle equivalence.

At cutoff three the unique nonzero lower boundary is
\[
\partial^{(3)}_4=(-1,1,0,0,0,1,0,-1):\mathbb Z^8\longrightarrow\mathbb Z.
\]
A unit coefficient cancels the unique three-cell with the first four-cell. The \(8\times16\) exact integral matrix \(\partial^{(3)}_5\), printed by `verify.py`, satisfies \(\partial^{(3)}_4\partial^{(3)}_5=0\). Its submatrix in rows \(1,\ldots,7\) (zero-indexed) and columns \(0,1,2,3,4,5,8\) has determinant \(+1\), verified by the integer Bareiss algorithm. After the initial cancellation this is a unimodular \(7\times7\) attaching-degree minor on the seven remaining four-cells. Cellular basis changes followed by seven primitive four/five cell cancellations therefore leave one zero-cell and nine five-cells. As there are no lower positive-dimensional cells, the resulting space is \(\bigvee^9 S^5\). For cutoff one, the critical cells are exactly one vertex and one two-cell, giving \(S^2\).

**Filtration maps.** The cutoff-one source has homotopy dimension two and the cutoff-two target is two-connected, so the first inclusion is nullhomotopic. The cutoff-two source has homotopy dimension four and the cutoff-three target is four-connected, so the second inclusion is also nullhomotopic. This argument concerns the maps of these particular spaces, not any claimed persistence statement at later cutoffs.

## Verification
Run `python3 verify.py` using Python 3 and its standard library. `verification_output.txt` records the exact output of the provided checker and its terminal marker `DURER_INITIAL_HIGHER_INDEPENDENCE_INTEGRAL_OK`. The code independently checks the full mod-two simplicial boundary ranks at all three cutoffs, the directed acyclicity of all matchings, the signed Morse matrices, the chain-complex identity, and the integral unit determinant. The mod-two Betti vectors agree with \((\widetilde\beta_2=1)\), \((\widetilde\beta_3=3,\widetilde\beta_4=1)\), and \((\widetilde\beta_5=9)\), respectively. Mod-two agreement is a cross-check, not a substitute for the integral homotopy proof.

## Relationship to prior work
Deshpande and Singh developed homotopy calculations for this definition and classified several families, including complete multipartite and fully whiskered graphs, cycles, and perfect rooted trees (arXiv:2001.05448, originally posted January 15, 2020). Abdelmalek and collaborators examined chordal families (arXiv:2106.10863); the Dürer graph is not chordal because the six outer vertices induce a chordless cycle. A previously released computation of the cutoff-two complex of \(GP(5,2)\), the Petersen graph, gives a single \(S^3\), not a theorem covering \(GP(6,2)\). A published graph-metric Rips-filtration computation for the Dürer graph concerns a distinct simplicial construction and does not imply these higher-independence equivalences. The original baseline cutoff-one calculation is included to state the complete initial filtration; the cutoff-two mixed wedge and cutoff-three nine-sphere wedge are the claims of new contribution.

## Limitations
The theorem concerns only \(GP(6,2)\) and exactly \(r=1,2,3\); it is not a formula for general generalized Petersen graphs or higher cutoffs. The integer matrix and acyclicity arguments are a finite exact certificate for these complexes. Prior-work checks do not exclude an equivalent inaccessible or unindexed result; no claim of independently reviewed or externally certified proof is made.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, version 1 dated January 15, 2020. https://arxiv.org/abs/2001.05448
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, version 1 dated June 21, 2021. https://arxiv.org/abs/2106.10863
3. *The 2-independence complex of the Petersen graph is a 3-sphere*, publicly accessible mathematical record (2026). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-2-independence-complex-of-the-petersen-graph-is-a-3-sphere--156dc9567f6a
4. *Complete graph-metric Vietoris–Rips filtration of the Dürer graph*, publicly accessible mathematical record (2026). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtration-of-the-d-rer-grap--5ed9def16601
