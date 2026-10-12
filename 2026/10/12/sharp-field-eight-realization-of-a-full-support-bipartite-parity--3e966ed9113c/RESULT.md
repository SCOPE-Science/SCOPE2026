# Sharp field-eight realization of a full-support bipartite parity-check mask

## Finding
For each prime power \(q\) with an odd prime \(p\mid(q-1)\), choose \(\omega\in\mathbb F_q^\times\) of order \(p\). For integers \(3\le r,s\le p\), write \(e_i\) and \(f_j\) for the standard basis vectors of \(\mathbb F_q^{r+s}\) in two disjoint blocks. Form the \((r+s)\)-by-\(rs\) matrix with columns
\[
H_{ij}=e_i+\omega^{ij} f_j\qquad(0\le i<r,\ 0\le j<s).
\]
Every permitted entry of the vertex-edge incidence mask of \(K_{r,s}\) is nonzero. The kernel has parameters
\[
\boxed{[rs,\ rs-r-s,\ 6]_q}.
\]
In particular, \(K_{6,6}\) has a full-support \([36,24,6]_8\) realization: take \(\mathbb F_8=\mathbb F_2[z]/(z^3+z+1)\) and \(\omega=z\). Moreover **eight is the smallest finite-field order** at which a full-support distance-six filling of this exact mask is possible.

## Assumptions and scope
The alphabet is any finite field \(\mathbb F_q\). A full-support filling means that each incidence-mask entry equal to one must be assigned a *nonzero* field element; positions forbidden by the mask remain zero. This is stronger than merely obeying the weak support convention in the literature, which permits zero coefficients at allowed positions. The sharp alphabet minimum refers to full-support realizations, not all weakly masked realizations. Every coordinate is an edge of the simple complete bipartite graph \(K_{r,s}\). We assume \(r,s\ge3\), ensuring a six-edge \(K_{2,3}\) dependence.

## Proof
**Four-cycle criterion.** For an arbitrary full-support filling, rescale each nonzero column to the form \(e_i+\lambda_{ij}f_j\) with \(\lambda_{ij}\in\mathbb F_q^\times\). Four columns indexed by \((i,j),(i,l),(k,j),(k,l)\), where \(i\ne k\), \(j\ne l\), have nonzero determinant exactly when
\[
\lambda_{ij}\lambda_{kl}\ne\lambda_{il}\lambda_{kj}.
\tag{1}
\]
A set of at most five edges in a simple bipartite graph has no cycles except possibly one four-cycle. Iteratively remove an edge at a leaf; since both permitted coefficients on every edge are nonzero, its column contributes an independent pivot. The remaining set, if not empty, consists of a four-cycle; by (1), its four columns are independent. Thus every set of at most five columns is independent whenever every four-cycle satisfies (1).

**Root-of-unity filling.** Put \(\lambda_{ij}=\omega^{ij}\). The ratio of the two sides of (1) is \(\omega^{(i-k)(j-l)}\), which is not one: the two nonzero integer differences are strictly smaller in absolute value than the prime \(p\). Hence every four-cycle minor is nonzero and all sets of at most five columns are independent.

**Full rank.** If a linear dependence among rows had coefficients \(A_i\) and \(B_j\), then \(A_i+B_j\omega^{ij}=0\) for all \(i,j\). If some \(B_j\) vanishes, all \(A_i\) vanish, then every \(B_l\) vanishes. Otherwise, any two right-hand-column vectors \((\omega^{ij})_i\) and \((\omega^{il})_i\) would be proportional, contradicting (1). Therefore the row rank is exactly \(r+s\), and the code dimension is \(rs-r-s\).

**Distance is exactly six.** The six edges of any \(K_{2,3}\) are supported on only five row positions, hence the six columns are dependent. Every five-column subset is independent, so this dependence yields a weight-six kernel word and no smaller nonzero word. This gives the claimed parameters for every admitted \(q,r,s\).

**Sharp alphabet for the six-by-six mask.** For *any* full-support filling with distance at least six, (1) holds. Fix distinct left vertices \(i,k\); as \(j\) ranges over six right vertices, the six ratios \(\lambda_{ij}/\lambda_{kj}\) must be distinct nonzero elements. Hence \(q-1\ge6\), ruling out every field of size at most six. At \(q=7\), choose three distinct left vertices \(i_0,i_1,i_2\). Both sequences \(u_j=\lambda_{i_1j}/\lambda_{i_0j}\) and \(v_j=\lambda_{i_2j}/\lambda_{i_0j}\) must permute the six elements of \(\mathbb F_7^\times\). By (1), their pointwise quotient \(v_j/u_j\) must also permute them. But
\[
\prod_j\frac{v_j}{u_j}=1\ne\prod_{x\in\mathbb F_7^\times}x=-1,
\]
a contradiction. Finally, \(\mathbb F_8^\times\) has prime order seven. Its element \(z\) modulo \(z^3+z+1\) has order seven, so the explicit root-of-unity filling for \(r=s=6\) provides the matching realization. Thus the minimum alphabet size in the defined full-support class is exactly eight.

## Verification
The standalone `verify.py` implements \(\mathbb F_8\) using irreducible polynomial `0b1011` and generator `0b010`, constructs each \(H_{ij}\), checks all four-cycle minors and full row ranks for \((r,s)=(3,3),(3,7),(6,6),(7,7)\), and exhaustively enumerates every subset of one through five columns for \(K_{6,6}\). The numbers of subsets checked are respectively \(36,630,7140,58905,376992\). Every one is independent. A six-column \(K_{2,3}\) witness has rank five. The verifier also enumerates all 720 candidate third-row permutations over `GF(7)` and confirms that none can satisfy the required quotient-permutation condition. Running `python3 verify.py` prints `VERIFY_OK`. The infinite-parameter statement follows from the algebraic proof, not from finite enumeration.

## Relationship to prior work
Han, Yildiz, and Hassibi [1] determine the structural distance ceiling six and structural row rank twelve for this very \(K_{6,6}\) mask (their Propositions 4 and 5), then establish generic existence of \([36,24,6]_q\) over sufficiently large fields (Theorem 1). They prove this optimum cannot be realized as a generalized Reed–Solomon subcode (Theorem 6). Those results are credited. The present claim supplies an explicit smallest-full-support alphabet, a specific characteristic-two parity-check matrix, and a root-of-unity construction for a natural infinite class of complete-bipartite masks. Its four-cycle-minor requirement is weaker than full superregularity of a dense matrix. Almeida and Napp [2] examine much stronger minor constraints and, specifically, lower-triangular Toeplitz matrices; their listed minimum field sizes do not establish the present sharp sparse-incidence result. General gain-graph representation principles explain related cycle dependence but do not by themselves specify the sharp \(K_{6,6}\) finite-field threshold.

## Limitations
Full support is essential: the claimed field-size minimum does not rule out a weakly masked \(K_{6,6}\) parity-check matrix over a smaller field if some allowed entries vanish. The construction is not asserted to provide generalized Reed–Solomon subcodes, decoding complexity bounds, or optimal field sizes for every \((r,s)\). The algebraic proof handles all stated parameters, while exhaustive finite computation is restricted to the specified cases. Earlier gain-matrix literature may contain equivalent two-by-two-minor observations that were not located; independent originality review has not been performed.

## References
[1] B. Han, H. Yildiz and B. Hassibi, *On Codes with Support-Constrained Parity Checks*, arXiv:2605.08644v1 (first publicly posted 2026-05-09), https://arxiv.org/html/2605.08644v1, Sections 2 and 5.

[2] P. Almeida and D. Napp, *Superregular Matrices over Small Finite Fields*, arXiv:2008.00215v1 (2020), https://arxiv.org/html/2008.00215v1, Sections 1–3.
