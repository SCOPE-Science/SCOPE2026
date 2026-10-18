# Moore torsion in the dodecahedral perfect-matching complex

## Finding
Let \(D\) denote the twenty-vertex dodecahedral graph. Its perfect-matching complex has the **integral homotopy equivalence**
\[
\mathcal M_p(D)\simeq M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^{20}S^3.
\]
The first summand is the simply connected Moore space formed by attaching a three-cell to \(S^2\) with degree two. Thus
\[
\widetilde H_j(\mathcal M_p(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&j=2,\\
\mathbb Z^{20},&j=3,\\
0,&\text{otherwise}.
\end{cases}
\]
This computes the homotopy type rather than only the Betti numbers. It concerns the **perfect-matching** complex, not the larger ordinary matching complex.

## Assumptions and scope
The dodecahedral graph is specified without reference to a drawing as the generalized Petersen graph \(D=GP(10,2)\): for \(i\in\mathbb Z/10\mathbb Z\), its vertices are \(u_i,v_i\), and its thirty edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). For a finite simple graph \(G\), define \(\mathcal M_p(G)\) to consist of all edge subsets contained in at least one perfect matching of \(G\); the simplicial vertices are graph edges. A matching is perfect when every graph vertex belongs to exactly one selected edge.

This finding treats exactly \(GP(10,2)\); no classification for arbitrary generalized Petersen graphs or fullerene graphs is claimed. Edge indices in the reproducible certificate are assigned by lexicographically sorting unordered pairs of integers after encoding \(u_i=i\) and \(v_i=10+i\).

## Proof
**Step 1: finite complete face poset.** Recursively take the least uncovered graph vertex and pair it with each available neighbor. This enumerates exactly 36 distinct perfect matchings. Generate every subset of each resulting ten-edge matching, remove duplicates, and include the empty simplex. The result contains exactly 30,504 faces (30,503 nonempty), with nonempty face counts in dimensions zero through nine equal to
\[
(30,375,2180,5790,8352,7440,4320,1620,360,36).
\]
This is an exhaustive enumeration: the recursion considers each possible partner of the least uncovered vertex, and every perfect matching has exactly one first such partner.

**Step 2: acyclic discrete-Morse matching.** In the preceding edge index convention, process indices in this fixed order:

`26,0,24,14,19,21,2,3,16,7,6,9,1,4,28,18,15,5,11,25,22,12,8,13,29,27,23,17,10,20`.

At each index, pair any two still-unpaired **nonempty** simplices differing only in that edge, whenever both simplices occur. The sequential element-pairing lemma supplies acyclicity; independently, `verify_dodeca_pm.py` constructs all directed Hasse incidences (unmatched arrows downward, matched arrows upward) and checks that a topological ordering consumes all 30,503 nonempty simplices over exactly 163,650 incidences. There are 15,238 pairs and precisely 27 critical simplices: one zero-simplex, three two-simplices, and 23 three-simplices. Consequently Forman's theorem gives a CW complex with one vertex, three two-cells, 23 three-cells, and no other cells.

**Step 3: exact integral attaching degrees.** Orient simplices by increasing graph-edge index. Number critical three-cells in increasing integer-mask order as columns \(c_1,\ldots,c_{23}\), and critical two-cells likewise as three rows. The integral cellular boundary from degree three to degree two is computed by summing signed gradient paths. In the ordered critical basis its only nonzero row entries are expressed by
\[
\begin{aligned}
r_1&=c_4-c_{18},\\
r_2&=2c_1-c_4+2c_7+c_{11}+c_{12}+2c_{16}-c_{18}+2c_{21},\\
r_3&=c_{11}-c_{12}.
\end{aligned}
\]
Here \(r_i\) specifies row \(i\) as an integral functional on the listed critical three-cells. The complete 3-by-23 matrix, including zeros, is recomputed by the standalone checker. The signed gradient reduction is recursive: a critical two-face projects to its basis vector; a two-face paired downward with a one-face projects to zero; and a two-face paired upward with a three-face is replaced by the negative signed sum of the other two-faces in the boundary of that three-face. Acyclicity guarantees termination.

The matrix has a 2-by-2 minor of determinant \(1\) (rows 1, 2 and columns 4, 11) and a 3-by-3 minor of determinant \(-2\) (columns 1, 4, 11). Modulo two the second row equals the sum of the first and third, so every 3-by-3 minor is even. It follows that the gcds of the 1-by-1, 2-by-2, and 3-by-3 minors are respectively \(1,1,2\). Hence the exact Smith invariant factors are \(1,1,2\).

**Step 4: upgrade to integral homotopy.** The Morse CW complex has no one-cells, so its two-skeleton is \(S^2\vee S^2\vee S^2\) and is simply connected. Its three-cell attaching maps are elements of \(\pi_2(S^2\vee S^2\vee S^2)\cong\mathbb Z^3\), completely determined by the integral degree matrix above. Unimodular changes of the two-sphere and three-cell bases realize the Smith reductions up to homotopy. The unit attaching degrees cancel two pairs of cells, and the remaining degree-two attaching map yields \(M(\mathbb Z/2\mathbb Z,2)\); the twenty three-cells with trivial attaching maps supply \(\bigvee^{20}S^3\). No uncomputed higher attaching invariant enters this three-dimensional CW model.

## Verification
Run `python3 verify_dodeca_pm.py` to reproduce all matchings, faces, the full Hasse-acyclicity check, signed gradient boundary and every Smith-minor gcd using only Python's standard library. Its expected machine-readable output is `verify_dodeca_pm_output.json`.

As an independent check, run `python3 crosscheck_dodeca_pm.py`: it rebuilds the perfect matchings by a separate set-based recursion and enumerates subsets via combinations, makes 14,669 elementary free-face collapses to a 1,165-simplex complex, then computes boundary ranks over four prime fields. Its output is `crosscheck_dodeca_pm_output.json`. Over \(\mathbb F_2\), reduced Betti numbers in degrees 2 and 3 are \((1,21)\); over \(\mathbb F_3,\mathbb F_5,\mathbb F_{101}\), they are \((0,20)\). These independently agree with the integral Moore-space decomposition, but modular checks alone would not prove that decomposition.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega, *Perfect Matching Complexes of Honeycomb Graphs* (public preprint 2022), define the same facet-generated construction and classify specific hexagonal honeycomb families. The dodecahedral graph instead has pentagonal faces and is not one of their enumerated honeycomb patches. Their concluding discussion asks about more general perfect-matching complexes. The larger ordinary matching complex on the dodecahedral graph has a separately indexed sphere-wedge classification; it does not determine the topology of this proper, facet-generated subcomplex. A later paper on Möbius and circular ladders studies different cubic graph families. Exact-object and equivalent-formulation searches found no result implying the stated Moore summand; this is a qualified literature assessment, not a proof of worldwide uniqueness.

## Limitations
The classification is specific to the 20-vertex dodecahedral graph; no generalization to arbitrary cubic graphs, fullerenes, or graph products has been proved. The finite certificate is exact, but its validity depends on the explicitly specified graph, edge order and matching algorithm; all relevant certificates are reproducible in the accompanying scripts. Unindexed publications or newly accessible texts could alter the originality assessment. Independent mathematical audit has not been performed.

## References
1. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, first public posting 2022-09-06, especially Definition 1, sequential element-matching theorem, the honeycomb classifications and concluding discussion.
2. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (2026), distinct cubic-graph families; comparison based on the accessible abstract.
3. R. Forman, *A User's Guide to Discrete Morse Theory*, Séminaire Lotharingien de Combinatoire 48 (2002), discrete-Morse CW theorem.
