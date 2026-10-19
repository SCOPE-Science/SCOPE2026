# The two-bucket threshold for Gram-law equivalence of stacked signed sketches

## Finding

A stacked, fully independent signed one-hot sketch has exactly the same **entire Gram-matrix distribution** as a normalized dense Rademacher sketch, for every input dimension, if and only if each row block has width one or two. The statement covers all deterministic input matrices simultaneously in distribution, not just one particular subspace-embedding statistic.

Precisely, let \(m,n\ge2\), choose \(s\ge1\) and positive integers \(b_1,\ldots,b_s\) with \(\sum_j b_j=m\), and form the normalized block sketch \(S\) as specified below. For an independently signed dense matrix \(R\in\{-1,1\}^{m\times n}\) with independent entries, put \(D=R/\sqrt m\). Then

\[
 S^{\mathsf T}S\ \overset{\mathrm d}=\ D^{\mathsf T}D
 \quad\Longleftrightarrow\quad b_j\in\{1,2\}\text{ for every }j.
\]

When the condition holds, there is an **explicit deterministic block-orthogonal matrix** \(U\) such that \(US\) itself has precisely the distribution of \(D\). For any fixed real matrix \(A\), this gives \((SA)^{\mathsf T}(SA)\overset{\mathrm d}=(DA)^{\mathsf T}(DA)\). Every exact-arithmetic quantity depending only on those Gram matrices therefore has the same law.

When at least one block has width at least three, already a prescribed pair of coordinate columns distinguishes the laws: its exact rank-collapse probability is

\[
 \Pr\{\operatorname{rank} S_{[:,\{i,k\}]}<2\}
  =\frac{2^{1-s}}{\prod_{j=1}^s b_j}
  >2^{1-m}
  =\Pr\{\operatorname{rank} D_{[:,\{i,k\}]}<2\}.
\]

Consequently, for a prescribed \(m\), exactly matching the dense Gram law within this stacked one-hot family requires at least \(\lceil m/2\rceil\) signed nonzeros per column. This lower bound is attained by packing as many width-two blocks as possible, with one width-one block when \(m\) is odd. In particular, for even \(m\), the fully independent SparseStack construction with \(m/2\) two-row blocks and \(m/2\) nonzeros per column is exactly Gram-law equivalent to a dense independent-sign sketch with \(m\) nonzeros per column.

## Assumptions and scope

For each block \(j\in\{1,\ldots,s\}\) and column \(i\in\{1,\ldots,n\}\), choose independently a hash \(h_j(i)\) uniformly from \(\{1,\ldots,b_j\}\) and a symmetric sign \(\sigma_j(i)\in\{-1,1\}\). Within block \(j\), column \(i\) has the sole nonzero entry \(\sigma_j(i)\sqrt{b_j/m}\) in row \(h_j(i)\). Hashes and signs are fully mutually independent across blocks and columns. The blocks are stacked vertically to form \(S\in\mathbb R^{m\times n}\). Every column has squared norm \(\sum_j b_j/m=1\).

The weight \(\sqrt{b_j/m}\) is essential when block widths differ. In the equal-width case \(b_j=m/s\), the weight is \(1/\sqrt s\), the conventional SparseStack normalization. In the odd-row optimum, the one-row block and two-row blocks carry different weights.

The equivalence concerns exact arithmetic, independent signs and hashes, and Gram-derived functionals. It does not assert that the raw random matrices have the same entry distribution without the orthogonal row transform, or that their floating-point implementations have identical rounding error or cost.

## Proof

**Step 1: deterministic orthogonal coupling for widths one and two.** On a one-row block, the signed one-hot entry is exactly a symmetric sign multiplied by \(1/\sqrt m\). On a two-row block, its four equally likely unscaled possibilities are \((1,0)^{\mathsf T}\), \((-1,0)^{\mathsf T}\), \((0,1)^{\mathsf T}\), and \((0,-1)^{\mathsf T}\). Apply the orthogonal matrix

\[
 H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

After including the input amplitude \(\sqrt{2/m}\), the transformed possibilities are exactly the four equally likely sign pairs in \(\{-1/\sqrt m,1/\sqrt m\}^2\). Thus the two transformed row coordinates are independent symmetric signs. Apply \(H\) separately to every two-row block and identity to every one-row block. Mutual independence of the hash-sign choices across all columns and blocks implies all \(mn\) entries of \(US\) are independent symmetric signs divided by \(\sqrt m\). Since \(U^{\mathsf T}U=I\), we have, samplewise, \((US)^{\mathsf T}(US)=S^{\mathsf T}S\). This proves the forward equivalence for all block widths at most two.

**Step 2: exact two-column obstruction for any larger block.** Choose distinct input coordinates \(i,k\). Their images \(v_i,v_k\) under \(S\) have Euclidean norm one. Let \(X_j\) be the signed collision indicator within block \(j\):

\[
 X_j=\sigma_j(i)\sigma_j(k)\,\mathbf1_{\{h_j(i)=h_j(k)\}}.
\]

The independent variables satisfy \(\Pr\{X_j=1\}=\Pr\{X_j=-1\}=1/(2b_j)\), and \(\Pr\{X_j=0\}=1-1/b_j\). Therefore

\[
 \langle v_i,v_k\rangle=\sum_{j=1}^s\frac{b_j}{m}X_j.
\]

As all the weights \(b_j/m\) are strictly positive and sum to one, this inner product has absolute value one **only** if every block collides and all collision signs agree. Since \(v_i,v_k\) are unit vectors, this event is exactly failure of rank two. Summing over the two possible common signs gives

\[
 \Pr\{|\langle v_i,v_k\rangle|=1\}
 =2\prod_{j=1}^s\frac1{2b_j}
 =\frac{2^{1-s}}{\prod_j b_j}.
\]

For independent dense sign columns, the second column must equal or oppose the first in every one of the \(m\) independent rows. Its rank-failure probability is \(2^{1-m}\). For each integer \(b\ge1\), the inequality \(b\le 2^{b-1}\) holds, with equality exactly for \(b=1,2\). Consequently

\[
 \frac{\Pr\{\operatorname{rank} S_{[:,\{i,k\}]}<2\}}
 {\Pr\{\operatorname{rank} D_{[:,\{i,k\}]}<2\}}
 =\prod_{j=1}^s\frac{2^{b_j-1}}{b_j}\ge1,
\]

with equality if and only if every \(b_j\) is one or two. Any larger block makes the probabilities strictly different, and so makes the full Gram laws different. This proves necessity.

**Step 3: minimal sparsity among exactly equivalent sketches.** Every block contributes exactly one signed nonzero to every column. If all widths are at most two, \(m=\sum_j b_j\le2s\), so \(s\ge\lceil m/2\rceil\). Choosing \(\lfloor m/2\rfloor\) blocks of width two and, for odd \(m\), one of width one realizes this lower bound and satisfies Step 1. No smaller number of blocks can realize the dense Gram law within the stated family, because Step 2 forces every width to be at most two.

## Verification

The standalone Python 3 standard-library script `check.py` performs \(29{,}317\) exact rational assertions. It exhaustively enumerates the signed-hash distribution for small block widths, compares the three-coordinate Gram distributions with dense signs for block sizes one through four, checks the four two-row Hadamard outcomes, and enumerates all ordered positive block compositions with up to twelve output rows to check the rank-collapse classification and the minimal nonzero count. These are finite consistency checks, not substitutes for the arbitrary-dimensional proof above. Run `python3 check.py` from the directory containing this document.

## Relationship to prior work

Jeendgar, Flint and Anzt [1] empirically analyze the accuracy and GPU rounding behavior of SparseStack and CountSketch. Heidary [2] gives fully independent SparseStack an optimal-order subspace-embedding guarantee using moment bounds and a three-point comparison; its stated construction uses equal-sized blocks. Camaño, Epperly, Meyer and Tropp [3] analyze randomized numerical linear algebra with structured sparse sketches and subspace-injection properties. Those bounds and implementation results do not, in the portions inspected, state that two-row signed one-hot blocks are exactly orthogonally equivalent to independent dense signs, nor do they give the strict all-block classification by exact two-column rank-collapse probability. The present statement is a finite-dimensional law identity and an if-and-only-if block-width obstruction, not a claim to the invention of SparseStack, CountSketch, dense Rademacher sketches, or Hadamard transforms. An equivalent isolated identity in earlier randomized-embedding literature remains a bibliographic risk.

## Limitations

No Gaussian-sketch equivalence is asserted. The result needs fully independent hash/sign selections and exact arithmetic. The minimum number of nonzeros is a structural count, not a measured speedup. The cross-block row rotation may change GPU memory access or rounding behavior, and for uneven block widths the normalization differs from canonical equal-weight SparseStack. The theorem guarantees equality of Gram-matrix distributions for fixed deterministic inputs; it does not transfer results requiring entrywise equality of the untransformed sketches or independence from data-driven sketch selection.

## References

[1] A. Jeendgar, C. Flint and H. Anzt, *Randomized Sketching is Robust to Low-Precision Rounding on GPUs*, first public arXiv version 2026-06-18, arXiv:2606.20195v1. https://arxiv.org/abs/2606.20195

[2] D. Heidary, *SparseStack Is an Optimal Oblivious Subspace Embedding*, first public arXiv version 2026-09-02, arXiv:2609.02978v1. https://arxiv.org/abs/2609.02978

[3] C. Camaño, E. N. Epperly, R. A. Meyer and J. A. Tropp, *Faster Linear Algebra Algorithms with Structured Random Matrices*, arXiv:2508.21189v1 (2025-08-28). https://arxiv.org/abs/2508.21189
