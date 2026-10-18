# Full rational symmetry characters of the ten-rung prism perfect-matching complex

## Finding
Let \(G=C_{10}\square K_2\) be the circular ladder with two cycles of ten vertices and ten rungs. Let \(P=\mathcal M_p(G)\) be the simplicial complex whose vertices are edges of \(G\), with facets its perfect matchings. Let \(r\) simultaneously rotate both ten-cycles by one position, \(s\) reflect both cycles by \(i\mapsto-i\pmod{10}\), and \(\tau\) exchange the two layers. These actions generate \(D_{10}\times C_2\). Define rational one-dimensional characters \(\eta_r,\eta_s,\eta_\tau\) by assigning the corresponding generator the value \(-1\) and the other two generators \(+1\).

The complete reduced rational homology representations are
\[
\widetilde H_3(P;\mathbb Q)\cong \eta_r\oplus(\eta_s\eta_\tau),\qquad
\widetilde H_4(P;\mathbb Q)\cong\mathbf1\oplus(\eta_r\eta_s),
\]
with all other reduced rational homology groups zero. Thus the two nonzero homology degrees both have dimension two, but carry different one-dimensional symmetry characters. In particular \(\tau\) has trace zero on degree three and trace two on degree four, whereas \(r\) has trace zero on each; an odd-axis reflection \(rs\) has traces \(-2\) and \(+2\), respectively.

## Assumptions and scope
The underlying graph is the simple undirected ten-rung prism on \(20\) vertices and \(30\) edges. Write the upper and lower rim edges as \(b_i=(i,i+1)\) and \(c_i=(10+i,10+i+1)\), and the rung as \(a_i=(i,10+i)\), with indices modulo ten. A simplex of \(P\) is an edge subset contained in at least one perfect matching. This is **not** the ordinary matching complex. Characters are representations over \(\mathbb Q\), not assertions about integral module splitting or equivariant homotopy type.

## Proof
**Finite enumeration and auxiliary complex.** Enumerate perfect matchings by recursively choosing the smallest unmatched graph vertex and branching over each possible incident edge to an unmatched neighbor. Each branch chooses one possible partner, so this enumerates all perfect matchings without omissions or duplicates. There are exactly \(125\). Taking all subsets of these matchings gives exactly \(60{,}852\) faces of \(P\), including the empty face.

Let \(K\) be the independence complex of a graph whose \(30\) vertices represent edges of \(G\). Put a conflict edge between graph edges sharing an endpoint and, additionally, between \(b_i\) and \(c_{i+1}\), or \(c_i\) and \(b_{i+1}\), for every index modulo ten. Independent-set generation gives \(59{,}050\) faces and verifies \(K\subset P\). Precisely two perfect matching facets are missing from \(K\):
\[
A=\{b_0,b_2,b_4,b_6,b_8,c_1,c_3,c_5,c_7,c_9\},\quad
B=\{b_1,b_3,b_5,b_7,b_9,c_0,c_2,c_4,c_6,c_8\}.
\]
The finite face-list identity \(P=K\cup 2^A\cup2^B\) is checked exhaustively. Both exceptional simplices have disjoint vertex sets. Their intersections with \(K\) are independence complexes of ten-cycles, each of reduced homology rank one in dimension two. This provides a separate structural consistency check on the homology dimensions.

**Exact homology.** A deterministic free-face collapse reduces \(P\) by \(30{,}069\) elementary pairs to a subcomplex of \(714\) faces including the empty face; it reduces \(K\) by \(29{,}283\) pairs to \(484\) faces. Every pair is checked as a codimension-one face with exactly one surviving immediate coface. The oriented simplicial boundary matrices of the residual complexes are reduced by exact rational Gaussian elimination with normalized face order and signs \((-1)^j\). The resulting reduced rational Betti numbers are \(\beta_3(P)=\beta_4(P)=2\), \(\beta_4(K)=2\), and zero otherwise. The same Betti numbers are independently obtained by reducing the original full simplicial boundary matrices over \(\mathbb F_2\). No finite sampling is used in these assertions: all simplices of these two finite complexes are enumerated.

**Symmetry characters.** Each of the \(40\) group elements preserves \(P\) and \(K\). Since \(K\) has reduced rational homology only in degree four, its reduced Lefschetz number \(\widetilde L(g,K)\) equals the degree-four trace. The pair \((P,K)\) has relative rational homology only in degree three: its quotient is the wedge of two ten-simplices modulo their ten-cycle-independence boundaries, so \(\widetilde H_3(P,K;\mathbb Q)\cong\mathbb Q^2\). The long exact sequence gives equivariant isomorphisms \(\widetilde H_4(P;\mathbb Q)\cong\widetilde H_4(K;\mathbb Q)\) and \(\widetilde H_3(P;\mathbb Q)\cong\widetilde H_3(P,K;\mathbb Q)\). Hence
\[
\chi_4(g)=\widetilde L(g,K),\qquad
\chi_3(g)=\widetilde L(g,K)-\widetilde L(g,P).
\]
For a simplicial permutation on \(30\) vertices, an invariant face is a union of permutation cycles. If \(t\) cycles are selected, its contribution to the reduced Lefschetz number is \((-1)^{t-1}\). The checker enumerates all admissible unions, or uses the full face vector for the identity, with no floating-point operations. As a second verification, it directly computes the signed permutation of oriented faces for nine representative nonidentity group elements.

Let \(s\) denote the reflection \(i\mapsto-i\) and let \(rs\) be the other reflection parity. The computed character pairs \((\chi_3,\chi_4)\), on the eight conjugacy classes of \(D_{10}\), are

| Class | \(1\) | \(r^5\) | \(r^{\pm1}\) | \(r^{\pm2}\) | \(r^{\pm3}\) | \(r^{\pm4}\) | \(s\) | \(rs\) |
|---|---|---|---|---|---|---|---|---|
| No layer swap | \((2,2)\) | \((0,0)\) | \((0,0)\) | \((2,2)\) | \((0,0)\) | \((2,2)\) | \((0,0)\) | \((-2,2)\) |
| With layer swap | \((0,2)\) | \((-2,0)\) | \((-2,0)\) | \((0,2)\) | \((-2,0)\) | \((0,2)\) | \((2,0)\) | \((0,2)\) |

Comparison with the four stated one-dimensional characters gives equality on all \(16\) conjugacy classes, proving the claimed rational isomorphisms.

## Verification
Run `python3 verification/check.py` using Python 3 and the standard library only. The expected stdout is in `verification/expected_output.txt`. The program constructs all \(125\) perfect matchings, all faces of \(P\) and \(K\), exhaustively checks their union description and all symmetry permutations, performs all elementary collapses and exact rational boundary reductions, computes the \(40\) signed Lefschetz values, and checks the character-class equalities. Exact output comparison and independent checks on nine group elements are included. No external mathematical software or database is required.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega (2022 preprint) introduced and investigated perfect-matching complexes of honeycomb graphs, not these group representations. Agarwal and Basak (2026 preprint, version two, Section 5.2) determine the **nonequivariant** homotopy types of all circular-ladder perfect-matching complexes and describe the corresponding exceptional perfect matching facets; they do not determine the \(D_{10}\times C_2\) action on rational homology. The present computation resolves the full symmetry representation at the first prism width in their classification with two different nonzero homology degrees, using an independent exhaustive complex construction and exact signed Lefschetz calculations.

## Limitations
The claim is specific to the ten-rung circular ladder. It determines rational homology representations, not integral lattices, maps of homotopy types, equivariant stable types, or representations at other widths. The proof is computer-assisted with a fully standalone exact finite checker; it does not supply a short handwritten closed-form reduction. Searches cannot exclude every unindexed prior equivalent result.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, first public September 6, 2022; later *Electronic Journal of Combinatorics* 30(2), P2.45 (2023), DOI 10.37236/11525.
2. A. Agarwal, B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2, September 14, 2026, especially Theorem 25 and Section 5.2.
3. Standard simplicial Lefschetz trace identity and elementary free-face collapses, as applied with explicit complete data in `verification/check.py`.
