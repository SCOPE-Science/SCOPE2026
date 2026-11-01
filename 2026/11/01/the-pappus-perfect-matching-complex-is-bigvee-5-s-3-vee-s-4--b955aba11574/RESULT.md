# The Pappus perfect-matching complex is \(\bigvee^5 S^3\vee S^4\)

## Finding
Let \(P\) be the 18-vertex Pappus graph, and let \(\mathcal M_{\mathrm p}(P)\) be the simplicial complex on its 27 graph edges whose facets are precisely its perfect matchings. Then
\[
\mathcal M_{\mathrm p}(P)\simeq\bigvee^{5} S^{3}\vee S^{4}.
\]
In particular, its only nonzero reduced integral homology groups are \(\widetilde H_3\cong\mathbb Z^5\) and \(\widetilde H_4\cong\mathbb Z\). This is an integral homotopy assertion, rather than an assertion solely about homology over a field.

## Assumptions and scope
The graph has vertex set \(\{0,\ldots,17\}\). Its 18 cycle edges are \(\{i,i+1\bmod18\}\); its nine additional edges are the distinct undirected chords induced by the LCF shift sequence \([5,7,-7,7,-7,-5]^3\), i.e. \(\{i,i+s_i\bmod18\}\) for all \(0\le i<18\), removing duplicates. This uniquely specifies the standard cubic bipartite Pappus graph, the Levi graph of the \((9_3)\)-Pappus configuration. Sort the resulting 27 undirected graph edges lexicographically, with zero-based indices \(0,\ldots,26\).

A *perfect matching* is a set of nine graph edges in which every graph vertex occurs exactly once. A simplex of \(\mathcal M_{\mathrm p}(P)\) is any subset of at least one perfect matching. Nonempty simplices are used for the discrete-Morse face poset. The empty set is counted only in enumerative bookkeeping. No graph metric, graph orientation, or extra parameter is assumed.

## Proof
**Exhaustive construction.** Recursively match the least uncovered graph vertex to one of its uncovered neighbors. This produces exactly 42 distinct perfect matchings. Taking every submask of each matching produces 15,820 simplices including the empty face. Their nonempty face-vector, by dimensions zero to eight, is
\[
(27,297,1575,3780,4752,3456,1512,378,42).
\]
An independent procedure enumerates all 35,368 ordinary graph matchings, including the empty matching, and checks each matching's residual vertices for a perfect matching. Exactly the same 15,820 subsets extend to perfect matchings. Independently, enumeration of the nine-by-nine bipartite perfect-matching assignments returns precisely the same 42 perfect matchings.

**Acyclic discrete-Morse reduction.** On the poset of all 15,819 nonempty faces, successively use pivot vertices of the simplicial complex in the order \(26,25,\ldots,0\). At pivot \(p\), for each pair \(\sigma,\sigma\cup\{p\}\) still unpaired and present, with \(p\notin\sigma\), pair them and remove both from later stages. This yields 7,901 pairs. Exactly 17 cells remain unpaired: one in dimension zero, five in dimension two, ten in dimension three and one in dimension four. An exhaustive directed-Hasse-graph test reverses every paired covering incidence, orients all other covering incidences downward and topologically orders all 15,819 faces across 78,921 incidences. There is no directed cycle. Therefore discrete Morse theory yields a homotopy-equivalent CW complex with precisely the stated cells.

**Integral attaching maps.** Orient every original simplex by increasing graph-edge index. To compute the reduced Morse differential, a critical lower-dimensional face projects to its basis element, a face paired downward projects to zero, and a face \(a\) paired upward to \(b\) projects to the negative incidence-weighted sum of the projections of the other codimension-one faces of \(b\), divided by the unit coefficient \([b:a]\in\{\pm1\}\). Recursively applying this rule to the boundaries of critical cells gives, in the critical-face order determined by increasing face masks within each dimension,
\[
\partial_3=
\begin{pmatrix}
0&-1&-1&-1&0&0&0&0&0&0\\
0&0&0&0&1&0&0&0&0&0\\
0&1&0&1&0&1&1&1&1&0\\
1&0&0&0&0&1&0&0&0&0\\
-1&0&-1&0&1&0&1&1&0&-1
\end{pmatrix},
\qquad
\partial_4=0_{10\times1}.
\]
The five columns of \(\partial_3\) numbered \(0,1,2,4,8\) have determinant \(-1\). Thus \(\partial_3:\mathbb Z^{10}\to\mathbb Z^5\) is surjective with primitive image; its kernel is free of rank five.

Let \(Y\) be the three-skeleton of this Morse CW complex. It is simply connected because it has one zero-cell and no one-cells, and the computation gives \(\widetilde H_2(Y;\mathbb Z)=0\), \(\widetilde H_3(Y;\mathbb Z)=\mathbb Z^5\), and no other reduced homology. The Hurewicz theorem and the homological Whitehead theorem imply \(Y\simeq\bigvee^5 S^3\): choose representatives of a basis of its third homology, whose third homotopy classes exist by Hurewicz. The unique four-cell attaches by a map \(S^3\to Y\). Since the cellular differential \(\partial_4\) is identically zero, its Hurewicz image in \(H_3(Y;\mathbb Z)\) is zero. Hurewicz is an isomorphism here, so the attaching map is nullhomotopic. Attaching this cell therefore adds a wedge summand \(S^4\). This proves the displayed homotopy equivalence.

## Verification
The files `verify_pappus_perfect.py`, `CERTIFICATE.json` and `VERIFY_OUTPUT.txt` provide a self-contained, standard-library Python replay. From a directory containing those three files, run `python3 verify_pappus_perfect.py`. It rebuilds the graph from the LCF sequence, verifies the perfect matchings in two different ways, checks extendibility independently for every ordinary matching, reconstructs the entire simplicial complex, creates the precise Morse pairs, checks all directed Hasse incidences for acyclicity, calculates signed integral Morse differentials, verifies the determinant \(-1\), checks every entry against the embedded finite certificate, and independently computes all simplicial boundary ranks over \(\mathbb F_2\).

The resulting reduced \(\mathbb F_2\)-Betti vector in dimensions zero through eight is \((0,0,0,5,1,0,0,0,0)\). This finite-field calculation is a cross-check, not the justification for the integral homotopy claim. The exact integer attaching map, the primitive minor, the complete acyclic matching, and the Hurewicz argument supply that justification.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega introduce perfect-matching complexes and determine homotopy types for stated planar honeycomb families (arXiv:2209.02803). Chandrakar and Singh study polygonal-line tilings and two-row grid graphs (arXiv:2407.05809). Neither published theorem covers this nonplanar Pappus Levi graph; no extension of those family classifications is assumed.

A published computation for the **ordinary** matching complex of this same Pappus graph establishes \(\mathcal M(P)\simeq\bigvee^{40}S^5\). That different complex contains *all* 35,368 ordinary matchings (including empty), whereas \(\mathcal M_{\mathrm p}(P)\) contains only the 15,820 extendible matchings. In particular, the ordinary-complex classification does not imply the present mixed-dimensional homotopy type. Searches under the Pappus, Levi, Bouwer and toroidal-honeycomb names did not reveal an equivalent calculation. Such searches do not establish absolute bibliographic uniqueness.

## Limitations
Only the fixed Pappus graph and its perfect-matching subcomplex are classified. No family-wide theorem, equivariant homotopy statement, or assertion about the inclusion map into the ordinary matching complex is proved. The exact finite enumerations are part of the proof and are reproduced by the supplied code and certificate; they are not evidence for an infinite extrapolation. A differently indexed, previously published equivalent computation cannot be excluded solely from the searches performed. No independent audit or external replication is claimed.

## References
1. Margaret Bayer, Marija Jelić Milutinović, Julianne Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803, first public version 2022-09-06. https://arxiv.org/abs/2209.02803
2. Himanshu Chandrakar and Anurag Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first public version 2024-07-08. https://arxiv.org/abs/2407.05809
3. *Integral homotopy type of the Pappus graph matching complex*, public research record (2026-10-11; identifier db6c6c11f317), https://github.com/Resultary/2026
4. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html (graph identification and LCF encoding).
