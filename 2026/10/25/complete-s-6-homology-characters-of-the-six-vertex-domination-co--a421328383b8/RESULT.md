# Complete \(S_6\)-homology characters of the six-vertex domination complex

## Finding
Let \(D_{6,3}\) be the simplicial complex whose vertices are the fifteen edges of the complete graph on \(\{1,\ldots,6\}\), and whose nonempty faces are edge sets giving graphs with domination number at least three. Relabeling the six graph vertices induces a natural action of \(S_6\). Its reduced rational homology, **as an \(S_6\)-representation**, is
\[
\begin{aligned}
\widetilde H_5(D_{6,3};\mathbb Q)&\cong
S^{(5,1)}\oplus S^{(4,2)}\oplus S^{(4,1,1)},\\
\widetilde H_4(D_{6,3};\mathbb Q)&\cong
S^{(2,1,1,1,1)}\oplus S^{(2,2,1,1)}\oplus S^{(2,2,2)}\\
&\quad\oplus S^{(3,1,1,1)}\oplus 3S^{(3,2,1)}\oplus S^{(3,3)}\\
&\quad\oplus S^{(4,1,1)}\oplus 2S^{(4,2)}\oplus S^{(5,1)}.
\end{aligned}
\]
Here \(S^\lambda\) denotes the rational irreducible Specht module for the partition \(\lambda\vdash6\). All other reduced rational homology groups vanish. The dimensions in degrees five and four are respectively \(24\) and \(115\), and neither nonzero homology group contains the trivial representation. Thus the statement distinguishes the action of relabeling from the previously determined nonequivariant wedge-of-spheres homotopy type.

## Assumptions and scope
All graphs are simple, undirected, and retain their six labeled vertices, including isolated vertices. A set \(T\) of graph vertices dominates if the union of their closed neighborhoods is all six vertices; the domination number is the least size of such a set. Accordingly, an edge set is a face of \(D_{6,3}\) if and only if no two graph vertices dominate. The empty edge set is the empty simplex, and an edge set of size \(k+1\) is a simplex of dimension \(k\). The action on an oriented simplex includes the sign obtained by reordering its graph edges into a fixed total order. The claim concerns ordinary reduced simplicial homology with coefficients in \(\mathbb Q\), and no larger family is asserted.

## Proof
**1. The complete finite chain complex.** Enumerate all \(2^{15}\) subsets of the fifteen possible graph edges. For each edge set \(E\), form the six closed-neighborhood bit masks. Accept \(E\) if and only if the union of no pair of these six masks is the full six-vertex mask. This is exactly the definition of domination number at least three: a singleton dominating set would also be contained in a dominating pair. The nonempty face counts in dimensions zero through six are, in order,
\[
(15,105,455,1185,1647,915,180),
\]
with no higher-dimensional faces. The integer signed simplicial boundary of an increasing-edge-oriented face is
\[
\partial_k[e_{i_0},\ldots,e_{i_k}]
=\sum_{j=0}^k(-1)^j[e_{i_0},\ldots,\widehat{e_{i_j}},\ldots,e_{i_k}].
\]
The attached standard-library checker creates every face and every column of this boundary directly from these definitions and verifies \(\partial_{k-1}\partial_k=0\).

**2. Exact ranks and kernel bases.** Integer column elimination, choosing the least remaining row as pivot, finds ranks
\[
\bigl(\operatorname{rank}\partial_1,\ldots,\operatorname{rank}\partial_6\bigr)
=(14,91,364,821,711,180).
\]
Every selected pivot coefficient is exactly \(+1\) or \(-1\); the elimination uses integer subtraction only, tracks each original-column combination, and exhausts all columns, so these are exact rational ranks, **not** ranks guessed from modular experiments. In each dimension, the dependent columns supply kernel vectors whose coordinates on the corresponding dependent-column indices are the identity matrix. It follows directly from successive rank subtraction that the only nonzero reduced rational Betti numbers are \(\widetilde\beta_4=115\) and \(\widetilde\beta_5=24\). In particular \(\partial_6\) is injective and \(\dim\ker\partial_5=204\).

**3. Computing both homology characters.** For every conjugacy class of \(S_6\), take the permutation whose disjoint cycles have the specified lengths. Its action on oriented faces is obtained by permuting each graph edge and multiplying by the sign of the induced permutation of the ordered edge set. Write \(J\) for the dependent-column positions in degree five and \(\{z_j:j\in J\}\) for the resulting integer basis of \(\ker\partial_5\), normalized so that the \(J\)-coordinates of \(z_j\) are the \(j\)-th standard basis vector. The coefficient extraction identity gives
\[
\operatorname{tr}(g\mid\ker\partial_5)
=\sum_{j\in J}[g z_j]_j.
\]
Since \(\partial_6\) is injective and equivariant, the exact sequence from \(\operatorname{im}\partial_6\) to \(\ker\partial_5\) gives
\[
\chi_5(g)=\operatorname{tr}(g\mid\ker\partial_5)-\operatorname{tr}(g\mid C_6).
\]
The reduced alternating chain trace is
\[
L(g)=\sum_{k=0}^{6}(-1)^k\operatorname{tr}(g\mid C_k)-1.
\]
Because reduced rational homology is concentrated in degrees four and five, equivariant Euler–Poincaré gives \(\chi_4(g)=L(g)+\chi_5(g)\). The resulting eleven class values are:

| Cycle type | \(\chi_4\) | \(\chi_5\) |
|---|---:|---:|
| \((1,1,1,1,1,1)\) | 115 | 24 |
| \((2,1,1,1,1)\) | 3 | 8 |
| \((2,2,1,1)\) | 3 | 0 |
| \((2,2,2)\) | 3 | 0 |
| \((3,1,1,1)\) | -2 | 3 |
| \((3,2,1)\) | 0 | -1 |
| \((3,3)\) | -2 | 0 |
| \((4,1,1)\) | -1 | 0 |
| \((4,2)\) | -1 | 0 |
| \((5,1)\) | 0 | -1 |
| \((6)\) | 0 | 0 |

**4. Irreducible decomposition.** For each partition \(\lambda\vdash6\), evaluate the irreducible character using the Murnaghan–Nakayama rim-hook rule. Its multiplicity in degree \(i\) is
\[
\frac1{720}\sum_{\mu\vdash6}\frac{720}{z_\mu}\,
\chi_i(\mu)\chi^\lambda(\mu),
\qquad
z_\mu=\prod_{r\ge1}r^{m_r(\mu)}m_r(\mu)!.
\]
The eleven integer inner products give precisely the nonnegative multiplicities displayed in the finding. The resulting Specht dimensions sum to \(115\) and \(24\), respectively. None of the partitions is \((6)\), proving the final assertion on invariant vectors. This completes the proof.

## Verification
From the extracted package directory run `python3 artifacts/verify.py`, which requires only Python's standard library. It performs the complete face enumeration, exact unit-pivot integer elimination, kernel-basis character calculation for all eleven conjugacy classes, direct boundary-squared checks, signed equivariance checks on generators of \(S_6\), character-table orthogonality and integral multiplicity checks. The success marker is `D63_S6_CHARACTER_VERIFY_OK`. This finite exhaustive computation certifies the explicitly bounded domain of the theorem; it is not an inference about unbounded families. The script is self-contained and does not rely on a stored face table or external mathematical package.

## Relationship to prior work
González and Hoekstra-Mendoza introduced \(D_{n,\gamma}\), proved a nonequivariant sphere-wedge theorem for \(D_{n,n-2}\), and highlighted \(D_{6,3}\) by its Euler characteristic \(92\). A subsequently published exact calculation established \(D_{6,3}\simeq\bigvee^{115}S^4\vee\bigvee^{24}S^5\). That result establishes the two dimensions but not how the six vertex labels act on their homology. A separate published Specht decomposition concerns \(\widetilde H_2(D_{n,n-2};\mathbb Q)\), whose domination-number condition and degree differ. Neither statement implies the characters obtained here: rational homology dimensions alone do not determine an \(S_6\)-module. No covering character calculation was found in the specified indexed comparisons; this is not a proof of worldwide uniqueness.

## Limitations
The result is a rational equivariant homology calculation for a single six-vertex complex. It does not classify integral \(\mathbb Z[S_6]\)-lattices, modular representations, equivariant homotopy types, or the whole family \(D_{n,n-3}\). An equivalent computation may occur in unindexed or inaccessible literature. The finite checker is a reproducibility certificate, not an independent human audit.

## References
1. Jesús González and Teresa I. Hoekstra-Mendoza, *On the homotopy type of complexes of graphs with bounded domination number*, arXiv:1901.07130, first public version 2019-01-22, especially the introduction, Problem 1.4, and Section 8. https://arxiv.org/abs/1901.07130 ; https://doi.org/10.55016/ojs/cdm.v16i3.72114 .
2. *A mixed-dimensional sphere wedge for \(D_{6,3}\)*, publicly available exact homotopy calculation: https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-a-mixed-dimensional-sphere-wedge-for-d-6-3--55d89ec4bab2/RESULT.md .
3. *Stable Specht decomposition of \(H_2(D_{n,n-2};\mathbb Q)\)*, a distinct equivariant calculation: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-stable-specht-decomposition-of-h-2-d-n-n-2-mathbb-q--ab4fa03abdf7/RESULT.md .
