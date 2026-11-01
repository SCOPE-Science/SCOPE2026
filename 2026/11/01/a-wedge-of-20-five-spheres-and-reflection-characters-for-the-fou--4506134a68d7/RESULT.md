# A wedge of \(20\) five-spheres and reflection characters for the four-robust \(3\times4\) grid

## Finding
Let \(G=P_3\square P_4\) be the Cartesian product of paths on three and four vertices. Define its four-robust clique complex \(K\) by admitting a vertex subset precisely when the induced subgraph has independence number at most three. Then
\[
|K|\simeq\bigvee^{20}S^5.
\]
In particular, \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^{20}\), all other reduced integral homology groups vanish, and \(K\) is simply connected.

Let \(R\) reverse the three rows and \(C\) reverse the four columns. These commuting involutions generate the full rectangular symmetry group \(C_2\times C_2\). Their rational action on fifth homology has character
\[
\operatorname{tr}(1,R,C,RC)=(20,0,-4,0).
\]
If \(\chi_{\varepsilon,\delta}\) denotes the one-dimensional rational character taking \(R\) to \(\varepsilon\in\{\pm1\}\) and \(C\) to \(\delta\in\{\pm1\}\), then
\[
\widetilde H_5(K;\mathbb Q)\cong
\chi_{+,+}^{\oplus4}\oplus\chi_{-,+}^{\oplus4}
\oplus\chi_{+,-}^{\oplus6}\oplus\chi_{-,-}^{\oplus6}.
\]
No integral splitting into these rational one-dimensional constituents is asserted.

## Assumptions and scope
The vertices are \((r,c)\) with \(0\le r<3\), \(0\le c<4\), numbered \(4r+c\). Two vertices are adjacent exactly when their Manhattan distance is one. A simplex is a nonempty vertex subset containing **no independent set of four vertices**; the empty face is understood in the abstract simplicial complex. Homology is ordinary simplicial homology over the indicated coefficients, and the displayed homotopy type is nonequivariant.

## Proof
**Exact face description.** There are \(61\) independent four-vertex subsets of \(G\). Fifteen lie entirely in the first color class of the bipartition, fifteen lie entirely in the second, and thirty-one use both colors. Directly enumerating the \(\binom{12}{4}\) four-element subsets by the stated adjacency criterion gives this count, with the explicit exhaustive procedure below. A nonempty subset is a face of \(K\) if and only if it contains none of these \(61\) forbidden subsets. The resulting simplicial face vector in dimensions zero through five is
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(12,66,220,434,466,217),
\]
and there are no larger simplices. Thus \(K\) has exactly \(1415\) nonempty faces.

**A complete discrete-Morse pairing.** Identify every face with the twelve-bit integer recording its vertices. Process vertex indices in the fixed order
\[
(1,9,8,5,10,2,3,7,4,0,11,6).
\]
At each index \(v\), examine all currently unmatched nonempty faces in increasing integer order. Whenever \(v\notin\sigma\) and both \(\sigma\) and \(\sigma\cup\{v\}\) are still unmatched faces, match these two and remove them from further consideration. The procedure constructs \(697\) disjoint pairs and leaves exactly one critical zero-face (the singleton at index \(1\)) and twenty critical five-faces. There are no other critical cells. The twenty critical five-face masks are
\[
221,252,629,753,1241,1272,1621,1649,1652,1740,
2205,2236,2261,2292,2737,3276,3281,3312,3724,3780.
\]

For a finite poset, reverse the direction of each matched covering relation in the Hasse diagram and orient every unmatched covering relation from the larger face to the smaller face. The exact verifier constructs **all** \(6160\) covering incidences between the \(1415\) nonempty faces and performs a complete topological sort. Every node is removed: the directed graph is acyclic. This certifies the pairing as an acyclic discrete-Morse matching, not merely a numerical comparison of Betti ranks. The attached `verify.py` implements the full face test, pairing, and directed-acyclicity check using only the standard library; its assertions can be independently checked against the definitions above.

By the discrete-Morse CW theorem, \(|K|\) is homotopy equivalent to a CW complex with one zero-cell and twenty five-cells and no other cells. Every attaching map of a five-cell has target the single zero-cell, so this CW complex is precisely a wedge of twenty five-spheres. This proves the integral homotopy statement.

**Reflection representation.** The row and column reversals preserve the entire face set. On oriented simplicial chains, the trace of a symmetry in degree \(d\) is the signed number of \(d\)-faces preserved setwise, with the sign given by the parity of the induced vertex permutation. The finite calculation constructs each such permutation and computes these signed traces for every simplex. Since homology is \(\mathbb Q\) in degree zero and is otherwise concentrated in degree five, the Lefschetz identity gives
\[
\operatorname{tr}(g\mid H_5(K;\mathbb Q))
=1-\sum_{d=0}^{5}(-1)^d\operatorname{tr}(g\mid C_d(K;\mathbb Q)).
\]
For \(g=1,R,C,RC\), these values are respectively \(20,0,-4,0\). Character orthogonality for \(C_2\times C_2\) yields the four multiplicities \(4,4,6,6\) in the stated order. This proves the rational representation statement.

## Verification
Run `python3 verify.py` from the directory containing this document and the standalone checker. The checker reconstructs all subsets directly from \(P_3\square P_4\); independently reconfirms membership by testing four-subsets inside each candidate; verifies the face vector, the exactly \(697\) matching pairs and \(21\) unpaired faces, and the absence of a gradient cycle by topologically sorting the complete oriented Hasse graph. It separately computes the signed simplicial Lefschetz characters for all four rectangular symmetries and their rational irreducible multiplicities.

The expected output begins with `VERIFY_OK`. The SHA-256 of the ordered matching-pair list encoded as compact JSON is `de1f456e14187f7eff38b552a4dc890f649725fc68a451841e2ece565ec36977`. The certificate is exhaustive for this named twelve-vertex graph. It does not establish a theorem for wider grids.

## Relationship to prior work
Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs* (first submitted February 11, 2026), proves sphere-wedge classifications for rectangular grids at robust parameters two and three, and for all robust parameters under edge-only attachment of squares. Its Conjecture 5 asks for sphere-wedge topology under corner attachments at higher parameters; its proof does not cover the four-robust three-by-four rectangle, which necessarily involves corner attachments.

Chandrakar, Hazra, Rout, and Singh, *Topology of total cut and cut complexes of grid graphs* (first submitted August 14, 2024), prove total-cut classifications for all widths of two-row grids and for three-robust duals of three-row grids. They do not supply the four-robust three-by-four homotopy type. The previously determined all-width **Euler characteristic** of four-robust three-row grid complexes gives the Euler prediction for this case but does not imply its sphere-wedge homotopy type, integral torsion-freeness, or rational reflection representation.

Unlike the first small square grid, this rectangle already has thirty-one independent four-sets meeting both bipartition classes, so the complex cannot be obtained by merely joining the two color-class simplex skeleta. The explicit matching resolves this first genuinely mixed corner-gluing example.

## Limitations
The result concerns this single finite grid, the four-robust clique complex, its nonequivariant homotopy type, and the **rational** action of the rectangular reflection group on fifth homology. It does not prove the general higher-parameter square-sequence conjecture, the wider three-row grid cases, equivariant homotopy equivalence, or an integral decomposition of the reflection module.

## References
- Marek Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first submitted 2026-02-11, version 4 dated 2026-08-10. https://arxiv.org/html/2602.11365v4
- Himanshu Chandrakar, Nisith Ranjan Hazra, Debotosh Rout, and Anurag Singh, *Topology of total cut and cut complexes of grid graphs*, arXiv:2408.07646, first submitted 2024-08-14, version 3 dated 2026-01-12. https://arxiv.org/html/2408.07646v3
- Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Total Cut Complexes of Graphs*, Discrete & Computational Geometry 73 (2025), 500–527.
- Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
