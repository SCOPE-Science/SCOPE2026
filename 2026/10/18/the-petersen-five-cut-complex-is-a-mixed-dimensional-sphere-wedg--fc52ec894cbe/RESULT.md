# The Petersen five-cut complex is a mixed-dimensional sphere wedge

## Finding
For the Petersen graph \(P=KG(5,2)\), let \(\Delta_5(P)\) be the **ordinary** five-cut complex: its facets are the complements of those five-vertex subsets that induce disconnected graphs. Then
\[
\Delta_5(P)\simeq S^3\vee\bigvee^{5}S^4.
\]
Thus \(\widetilde H_3(\Delta_5(P);\mathbb Z)\cong\mathbb Z\), \(\widetilde H_4(\Delta_5(P);\mathbb Z)\cong\mathbb Z^5\), and all other reduced integral homology groups vanish. This pure four-dimensional complex is not shellable.

## Assumptions and scope
The underlying graph has the ten vertices \(V=\binom{\{0,1,2,3,4\}}2\), ordered lexicographically, and two vertices are adjacent exactly when their two-element labels are disjoint. For any five-element subset \(C\subset V\), let \(P[C]\) be the induced graph. The facets of \(\Delta_5(P)\) are exactly \(V\setminus C\) for disconnected \(P[C]\). This statement concerns an ordinary vertex-set cut complex, **not** a total cut complex, graph matching complex, or graph configuration space.

## Proof
**Enumeration.** There are \(\binom{10}{5}=252\) five-element subsets \(C\). A breadth-first closure on the bitmask of each induced subgraph finds exactly \(120\) disconnected such subsets, producing \(120\) facets. Taking all subsets of these facets produces the face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(10,45,120,200,120).
\]
All results below are exact finite assertions and can be regenerated using `check_integral.py`.

**Acyclic matching.** Represent a nonempty face by an integer \(b\) whose set bits encode its vertices. Initialize the set \(R\) of all \(495\) nonempty faces. For vertex indices \(v=0,1,\ldots,9\), visit the faces currently in \(R\) in increasing order of (cardinality, mask). Whenever \(v\notin\sigma\) and both \(\sigma\) and \(\sigma\cup\{v\}\) are still in \(R\), match these two faces and remove them from \(R\). This constructs exactly \(237\) disjoint pairs. Reverse these matching edges in the codimension-one face-poset Hasse diagram, while orienting every unmatched edge from larger to smaller face. A complete topological sort visits all \(495\) nodes through \(1850\) directed Hasse edges, so the matching is acyclic. Its unmatched cells are one zero-cell, eight three-cells, and twelve four-cells, and none in other dimensions.

**Integral Morse boundary.** Orient each simplex by increasing vertex index. For an increasing simplex \([v_0,\ldots,v_k]\), take the signed boundary \(\sum_{i=0}^k(-1)^i[v_0,\ldots,\widehat v_i,\ldots,v_k]\). Algebraically cancel the matched face pairs over \(\mathbb Z\), using a pivot \(+1\) or \(-1\) at every step. A deterministic last-available-first elimination finishes all \(237\) pairs and leaves an \(8\)-by-\(12\) integral boundary matrix \(D_4\), with all other positive-dimensional Morse boundary groups zero. The full matrix and critical-face masks are in `morse_certificate.json` and independently reconstructed by `check_integral.py`.

The matrix has rational rank \(7\), and its seven-by-seven submatrix on zero-based row indices \((0,1,2,3,4,5,6)\) and column indices \((3,4,5,7,8,9,10)\) has integer determinant \(+1\). Consequently its nonzero Smith invariant factors are exactly seven ones, hence the displayed integral homology groups are torsion-free with the claimed ranks.

**Upgrade to homotopy type.** The acyclic matching gives a CW model with one zero-cell, eight three-cells, and twelve four-cells. The three-skeleton is a wedge of eight \(3\)-spheres. Since \(\pi_3(\bigvee^8S^3)\cong\mathbb Z^8\), the attaching maps of the four-cells are completely determined by \(D_4\); there are no lower-dimensional or nonlinear attaching invariants. Unimodular changes of bases on the three- and four-cells take the attaching-map matrix to seven identity blocks and five zero columns. Contracting the seven resulting cell pairs yields \(S^3\vee\bigvee^5S^4\).

Finally, the original cut complex is pure of dimension four, because every facet has five vertices, but its degree-three reduced homology is nonzero. A pure shellable four-dimensional complex has reduced homology only in dimension four, proving nonshellability.

## Verification
Run `python3 check_integral.py` and `python3 check_finite_fields.py` from the directory containing the accompanying files. The first script checks the facets, face vector, all Morse pairs, acyclicity of the full directed Hasse graph, complete integral cancellations, the exact Morse boundary matrix, its rank, and a unimodular rank-seven minor. The second constructs all original simplicial boundary matrices independently and computes ranks over \(\mathbb F_p\) for \(p\in\{2,3,5,7,11\}\): the boundary ranks are \((9,36,84,115)\), and the reduced Betti ranks are \((0,0,0,1,5)\) for each field. These field checks corroborate but do not replace the integral unit-pivot and unimodular-minor proof.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced ordinary cut complexes and, in their 2023 preprint, gave the Petersen **two-cut** homotopy type. The paper's general face-lattice theorem requires a complete codimension-one skeleton for its strongest conclusion. The present five-cut complex fails that condition: it has \(200\) of the \(\binom{10}4=210\) possible tetrahedra. Their 2024 sequel treats disjoint unions, squared paths and grid graphs, not the Petersen five-cut complex. The ordinary and total cut constructions differ for cut thresholds greater than two. Neither previously known Euler-characteristic statements nor homotopy theorems for higher-girth graphs imply the two nonzero integral degrees of this specific complex. The five-cut threshold is natural because it matches the Petersen graph's girth, where induced cycles first affect cut-set topology.

## Limitations
This is an exact classification of one natural finite graph complex, not a theorem about all five-cut complexes or all Kneser graphs. The argument supplies integral homotopy equivalence but does not identify canonical generators compatible with the automorphism action, or determine maps between adjacent cut-filtration stages. Primary-literature and mathematical-index comparisons did not reveal identical coverage, but unindexed equivalent calculations cannot be ruled out. No independent mathematical audit has been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first publicly posted 2023-04-26; see Table 1, Theorem 6.1 and Corollary 6.6. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first publicly posted 2024-07-11; see the introduction and the sections on graph families. https://arxiv.org/abs/2407.08158
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first publicly posted 2022-09-27, on the distinct total-cut construction. https://arxiv.org/abs/2209.13503
