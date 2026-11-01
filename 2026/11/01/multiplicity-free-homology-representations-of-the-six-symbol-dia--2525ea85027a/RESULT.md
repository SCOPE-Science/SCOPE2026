# Multiplicity-free homology representations of the six-symbol diagonal-deleted chessboard

## Finding
Let \(D_6=\{(i,j):1\le i,j\le6,\ i\ne j\}\), and let \(X\) be its nonattacking-rook simplicial complex (equivalently, the matching complex of the crown graph \(K_{6,6}\) with one perfect matching deleted). The full symmetry group is \(G=S_6\times C_2\), acting through simultaneous row/column permutation and the transpose \(\tau:(i,j)\mapsto(j,i)\). Let \(S^\lambda\) denote the rational irreducible Specht module indexed by the partition \(\lambda\) of six; write \(\mathbf1\) for the trivial \(C_2\)-character and \(\varepsilon\) for its nontrivial character. Then, as rational \(G\)-modules,

\[
\widetilde H_3(X;\mathbb Q)\cong
(S^{(4,2)}\boxtimes\varepsilon)\oplus
(S^{(3,1,1,1)}\boxtimes\mathbf1)\oplus
(S^{(2,2,2)}\boxtimes\varepsilon),
\]

\[
\widetilde H_4(X;\mathbb Q)\cong
(S^{(6)}\boxtimes\mathbf1)\oplus
(S^{(4,1,1)}\boxtimes\varepsilon)\oplus
(S^{(3,2,1)}\boxtimes\varepsilon)\oplus
(S^{(2,1,1,1,1)}\boxtimes\mathbf1).
\]

All remaining reduced rational homology groups vanish. Each of the seven displayed irreducible constituents occurs once. In particular,
\[
\dim\widetilde H_3(X;\mathbb Q)^G=0,\qquad
\dim\widetilde H_4(X;\mathbb Q)^G=1.
\]
The transpose alone has traces \(-4\) in degree three and \(-20\) in degree four; its respective positive eigenspace dimensions are \(10\) and \(6\). This is a rational representation result, not a new calculation of integral torsion.

## Assumptions and scope
The complex uses the **ordinary, nonperiodic** six-by-six board with exactly the six diagonal squares forbidden. A face is a finite set of permissible cells with pairwise distinct first coordinates and pairwise distinct second coordinates. The simplicial orientation is increasing in the cell index \(6(i-1)+(j-1)\). The simultaneous action of \(S_6\) commutes with transpose, and for this crown graph these give its full automorphism group. Homology is reduced, over \(\mathbb Q\), in the indicated degrees. No assertion is made for other board sizes or other symmetry actions.

## Proof
**1. Chain model and ranks.** There are, for simplex dimensions zero through five, exactly \(30,315,1420,2715,1854,265\) faces. For an oriented face \([a_0,\ldots,a_k]\), the boundary is \(\partial[a_0,\ldots,a_k]=\sum_{j=0}^k(-1)^j[a_0,\ldots,\widehat{a_j},\ldots,a_k]\). Exact rational column reduction gives \(\operatorname{rank}_{\mathbb Q}\partial_4=1557\). Independently, reductions modulo \(1009\) and \(65521\) give lower bounds \((29,286,1134,1557,265)\) on the five rational boundary ranks. These lower bounds are exact: \(\operatorname{rank}\partial_1\le29\) by augmentation; then the chain identity successively forces \(\operatorname{rank}\partial_2\le315-29=286\) and \(\operatorname{rank}\partial_3\le1420-286=1134\); the independently rationally reduced fourth rank is \(1557\), and \(\operatorname{rank}\partial_5\le265\) by its column count. Thus the ranks, in degrees one through five, are
\[
(29,286,1134,1557,265).
\]
The augmented degree-zero boundary has rank one. These ranks imply \(\dim\widetilde H_3=24\), \(\dim\widetilde H_4=32\) and the vanishing of all other reduced rational homology. They are consistent with the previously published six-board integral homology data, but are recomputed for the rational result.

**2. Exact character extraction.** Denote \(B_3=\operatorname{im}\partial_4\subset C_3(X;\mathbb Q)\). A deterministic sparse rational elimination of the \(2715\)-by-\(1854\) matrix \(\partial_4\) selects \(1557\) independent columns. The verifier maintains each reduced pivot as an **exact rational** combination of selected original columns; consequently every transformed selected face can be expressed in this same quotient basis. If \(g\in G\), the signed coordinate on the diagonal of each such transformed basis column is computed and summed to obtain \(\chi_{B_3}(g)\). Independently, \(\chi_{C_k}(g)\) is the sum of orientation signs of the \(g\)-fixed \(k\)-faces.

Injectivity of \(\partial_5\) gives, in the rational representation ring,
\[
[\widetilde H_4]=[C_4]-[B_3]-[C_5].
\]
Reduced Euler--Poincaré then gives
\[
\chi_{\widetilde H_3}(g)=\chi_{\widetilde H_4}(g)-\left(\sum_{k=0}^5(-1)^k\chi_{C_k}(g)-1\right).
\]
As every element is conjugate to \((\sigma,\tau^e)\), where \(\sigma\) has one of the eleven cycle types of \(S_6\) and \(e\in\{0,1\}\), the following table is exhaustive. Columns are the characters in degrees three and four, without and with transpose.

| Cycle type | \(\chi_3(\sigma)\) | \(\chi_3(\sigma\tau)\) | \(\chi_4(\sigma)\) | \(\chi_4(\sigma\tau)\) |
|---|---:|---:|---:|---:|
| \((6)\) | -1 | -1 | 3 | 1 |
| \((5,1)\) | -1 | 1 | 2 | 0 |
| \((4,2)\) | 0 | 0 | 0 | 0 |
| \((4,1,1)\) | 0 | 0 | 0 | 0 |
| \((3,3)\) | 3 | -1 | -1 | 1 |
| \((3,2,1)\) | 0 | 2 | 0 | 2 |
| \((3,1,1,1)\) | 0 | 2 | 2 | 4 |
| \((2,2,2)\) | 8 | -4 | 0 | 4 |
| \((2,2,1,1)\) | 0 | -4 | 0 | 4 |
| \((2,1,1,1,1)\) | 0 | -4 | 0 | -4 |
| \((1,1,1,1,1,1)\) | 24 | -4 | 32 | -20 |

**3. Irreducible identification.** Independently generate all eleven rational \(S_6\)-irreducible characters by the Murnaghan--Nakayama border-strip rule. For a partition \(\lambda\), take the usual character inner product with the symmetric and antisymmetric transpose columns of the table:
\[
m_{\lambda,\pm}=
\frac12\sum_{\rho\vdash6}\frac{\chi^\lambda(\rho)}{z_\rho}
\bigl(\chi(\rho,1)\pm\chi(\rho,\tau)\bigr),
\qquad z_\rho=\prod_{j\ge1}j^{m_j(\rho)}m_j(\rho)!.
\]
Every nonzero multiplicity is exactly one, at exactly the constituents in the Finding, and all others vanish. Orthogonality of the generated \(S_6\) character table is checked exactly. The only trivial \(G\)-constituent occurs in degree four, establishing the invariant-dimension claim.

## Verification
The standalone standard-library Python program `verification/verify.py` regenerates **all** \(6599\) nonempty faces; computes the exact rational image basis, all twenty-two class traces and Murnaghan--Nakayama multiplicities; separately checks all five boundary ranks over each of two finite fields; and tests the oriented two-step boundary identity for every face. Its included output `verification/verification_output.txt` ends `VERIFY_OK`. The program is a complete finite computation for the claimed six-symbol object; it is not extrapolated to arbitrary \(n\).

## Relationship to prior work
Björner and Welker studied connectivity of diagonal-deleted chessboard complexes; Shareshian and Wachs, Section 8 and Table 8.1, reported the degree-three integral homology of the six-by-six deletion board and proved sharpness of its connectivity bound. These provide the exact-object historical background and do **not** give the two rational \(S_6\times C_2\) characters. Friedman--Hanlon representation formulas treat the **full** rectangular chessboard; they cannot be applied to this subcomplex merely by restriction of the ambient homology representation. Babson and Reiner likewise consider full rectangular chessboard complexes as type-selected examples; their representation results do not state the deleted-diagonal character. The new result refines already known numerical topology and does not assert novelty of those ranks or the three-primary torsion.

## Limitations
The proof concerns the specific six-symbol diagonal-deleted board and rational homology. It neither determines the action on the previously studied integral torsion nor asserts a homotopy wedge decomposition. Highly relevant published results were compared, but an equivalent unindexed character computation is possible. The calculations and written proof have not undergone independent validation.

## References
1. J. Shareshian and M. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first posted September 3, 2004; especially Section 8, Table 8.1. https://arxiv.org/abs/math/0409054
2. A. Björner and V. Welker, *Complexes of Directed Graphs*, SIAM Journal on Discrete Mathematics 12 (1999), 413–424, DOI:10.1137/S0895480198338724. https://doi.org/10.1137/S0895480198338724
3. E. Babson and V. Reiner, *Coxeter-like Complexes*, Discrete Mathematics & Theoretical Computer Science 6 (2004), 223–252, especially Examples 4.5 and 4.15, DOI:10.46298/dmtcs.312. https://dmtcs.episciences.org/articles/312
4. J. Friedman and P. Hanlon, *On the Betti Numbers of Chessboard Complexes*, Journal of Algebraic Combinatorics 8 (1998), 193–203 (with a 1999 erratum), cited and discussed in References 1 and 3.
