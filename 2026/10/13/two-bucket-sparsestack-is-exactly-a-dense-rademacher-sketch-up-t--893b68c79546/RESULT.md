# Two-bucket SparseStack is exactly a dense Rademacher sketch up to a fixed rotation

## Finding

**Theorem (exact Gram-law classification).** Fix any integers \(m\ge2\), \(\zeta\ge1\) and \(b\ge1\), and write \(d=b\zeta\). Independently for every block \(j\in\{1,\dots,\zeta\}\) and column \(k\in\{1,\dots,m\}\), choose a uniform hash \(h_{jk}\in\{1,\dots,b\}\) and a uniform independent sign \(\rho_{jk}\in\{-1,1\}\). Form the real SparseStack matrix \(S_{b,\zeta}\in\mathbb R^{d\times m}\) with block-column entries
\[
  S_{b,\zeta}^{(j)} e_k=\frac{\rho_{jk}}{\sqrt\zeta}e_{h_{jk}}.
\]
Let \(R_d\in\mathbb R^{d\times m}\) have mutually independent signs \(\pm1/\sqrt d\). Then
\[
 S_{b,\zeta}^{\mathsf T}S_{b,\zeta}\stackrel{\mathrm d}=
 R_d^{\mathsf T}R_d\quad\Longleftrightarrow\quad b\in\{1,2\}.
\]
For \(b=2\), in fact, with the **deterministic** orthogonal matrix
\[
 H_2=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
 \qquad Q=I_{\zeta}\otimes H_2,
\]
there is the stronger equality of entire matrix laws \(Q S_{2,\zeta}\stackrel{\mathrm d}=R_{2\zeta}\). Consequently, for **every** deterministic real input matrix \(X\in\mathbb R^{m\times r}\) and any \(r\ge1\),
\[
 X^{\mathsf T}S_{2,\zeta}^{\mathsf T}S_{2,\zeta}X
 \stackrel{\mathrm d}=
 X^{\mathsf T}R_{2\zeta}^{\mathsf T}R_{2\zeta}X.
\]
The equality is joint for any finite family of deterministic matrices, since it follows from the whole random Gram-matrix identity. In particular, all singular values, fixed-subspace distortion events, and sketch-and-solve procedures depending *only* on joint sampled Grams have identical laws. At the same output dimension, SparseStack uses \(\zeta=d/2\) signed input contributions per column, whereas a dense Rademacher sketch uses \(d\).

For \(b\ge3\), define \(C_S=\langle S_{b,\zeta}e_1,S_{b,\zeta}e_2\rangle\) and \(C_R=\langle R_de_1,R_de_2\rangle\). Their variance is the same, \(1/d\), but their fourth moments have the exact nonzero gap
\[
 \mathbb E C_S^4-\mathbb E C_R^4
 =\frac{(b-1)(b-2)}{b^3\zeta^3}>0.
\]
Thus no coupling or deterministic output rotation can make their full Gram laws coincide for \(b\ge3\).

## Assumptions and scope

All \(2\zeta m\) hash/sign primitive variables are mutually independent as specified; the sketch is real and normalized by \(1/\sqrt\zeta\). The comparison ensemble consists of *independent* real Rademacher entries, normalized by \(1/\sqrt d\), not Gaussian or independent three-point sparse entries. The input matrix is deterministic or independent of the sketch. Matrices are applied in exact arithmetic. The restriction \(m\ge2\) is essential: for one input column both Grams are the constant scalar \(1\) at **every** block width. At width \(b=1\), SparseStack itself is a dense independent-sign matrix and the equivalence is immediate.

## Proof

**(1) Two-row block rotation.** For each \(j,k\), the unscaled column \(\rho_{jk}e_{h_{jk}}\) is uniform on the four vectors \(e_1,-e_1,e_2,-e_2\). Left multiplication by \(H_2\) maps those four vectors bijectively onto
\[
\frac1{\sqrt2}(1,1)^{\mathsf T},\quad
\frac1{\sqrt2}(-1,-1)^{\mathsf T},\quad
\frac1{\sqrt2}(1,-1)^{\mathsf T},\quad
\frac1{\sqrt2}(-1,1)^{\mathsf T}.
\]
These are exactly the four equally likely outcomes of two independent Rademacher signs divided by \(\sqrt2\). Because the original block-columns are mutually independent, every entry of \(QS_{2,\zeta}\) is an independent sign divided by \(\sqrt{2\zeta}\). Therefore the entire matrix equality in distribution holds. Orthogonality of \(Q\) gives \((QS)^{\mathsf T}(QS)=S^{\mathsf T}S\) for every realization, proving the Gram-law and all stated deterministic-input consequences. For \(b=1\), the one-coordinate sign columns are already dense in each one-row block.

**(2) Exact fourth moments beyond two rows.** For the first two columns, set
\[
Y_j=\rho_{j1}\rho_{j2}\mathbf1_{\{h_{j1}=h_{j2}\}}.
\]
The \(Y_j\) are independent, symmetric, and satisfy \(\mathbb EY_j=0\), \(\mathbb EY_j^2=\mathbb EY_j^4=1/b\). Hence
\[
C_S=\frac1\zeta\sum_{j=1}^{\zeta}Y_j,
\qquad
\mathbb E C_S^2=\frac1{b\zeta},
\qquad
\mathbb E C_S^4=\frac{b+3\zeta-3}{b^2\zeta^3}.
\]
Similarly, the coordinatewise products of the two columns of \(R_d\) are \(d\) independent Rademacher signs, so
\[
C_R=\frac1d\sum_{i=1}^{d} Z_i,
\qquad
\mathbb E C_R^2=\frac1d,
\qquad
\mathbb E C_R^4=\frac{3d-2}{d^3}.
\]
Substitute \(d=b\zeta\), subtract and factor:
\[
\mathbb E C_S^4-\mathbb E C_R^4
=\frac{b(b+3\zeta-3)-(3b\zeta-2)}{b^3\zeta^3}
=\frac{(b-1)(b-2)}{b^3\zeta^3}.
\]
For every integer \(b\ge3\) this is strictly positive; therefore even one off-diagonal entry of the random Gram matrices has different laws. This rules out equality of their full Gram distributions. Combining both parts proves the stated if-and-only-if classification. \(\square\)

## Verification

Run `python3 verify.py` using Python's standard library. The script exhaustively compares *complete* integer-scaled Gram distributions of the two ensembles for six small configurations, including \((\zeta,m)=(1,2),(1,3),(2,2),(2,3),(3,2),(4,2)\); compares the four signed-selector block outcomes with all independent sign outcomes; and checks the rational fourth-moment identity across \(108\) integer parameter pairs. It separately checks the one-block collision moments by enumerating signed hash pairs. The recorded successful output is `VERIFY_OK exact_full_gram_cases=6 exact_moment_cases=108 support_checks=6`. Exhaustion at these finite sizes tests the implementation, **not** the all-size theorem; the all-size result follows from the preceding proof.

## Relationship to prior work

Jeendgar, Flint, and Anzt [1, Secs. 2.2 and 4.1] define the same normalized fully independent SparseStack model and investigate low-precision implementations and empirical distortion. Camaño, Epperly, Meyer, and Tropp [2, Secs. 1.5, 3.1, App. B] study SparseStack guarantees and general CountSketch moment comparisons. Chenakkod, Dereziński, and Dong [3] provide general OSNAP subspace-embedding analysis. Heidary [4, Secs. 1–2, 7] proves optimal-order embedding bounds for the fully independent model and couples signed selectors to independent *three-point* variables, not to a dense Rademacher matrix. Tikhomirov [5, Sec. 7.3] treats negatively associated sparse models and spectral-norm bounds. These results imply or bound embedding performance, but the inspected statements do not give the exact \(b=2\) full-matrix rotation equivalence or the all-width Gram-law classification by its fourth-moment obstruction. Neither the elementary Hadamard transform nor the Rademacher fourth-moment expansion is claimed as independently new; the claim is their exact interpretation and sharp classification for this specific sketch family.

## Limitations

No claim is made about Gaussian sketches, limited-independence hashes, adaptively selected inputs, rounded accumulation, GPU throughput, or wall-clock speed. The half-sparsity comparison counts sketch input contributions, not the cost of producing the rotated dense output; an explicit rotation would add postprocessing work. The moment-gap statement is a **distributional** obstruction for \(b\ge3\), not proof that one sketch always has worse tail bounds. An equivalent identity in older unindexed literature remains possible. The proof does not require or claim independent verification beyond the stated self-review.

## References

1. Aryaman Jeendgar, Clément Flint, and Hartwig Anzt, *Randomized Sketching is Robust to Low-Precision Rounding on GPUs*, arXiv:2606.20195v1 (18 June 2026), https://arxiv.org/html/2606.20195v1.
2. Chris Camaño, Ethan N. Epperly, Raphael A. Meyer, and Joel A. Tropp, *Faster Linear Algebra Algorithms with Structured Random Matrices*, arXiv:2508.21189v1 (2025), https://arxiv.org/html/2508.21189v1.
3. Shabarish Chenakkod, Michał Dereziński, and Xiaoyu Dong, *Optimal Subspace Embeddings: Resolving Nelson–Nguyen Conjecture Up to Sub-Polylogarithmic Factors*, arXiv:2508.14234v2 (2025), https://arxiv.org/html/2508.14234v2.
4. Diar Heidary, *SparseStack Is an Optimal Oblivious Subspace Embedding*, arXiv:2609.02978v2 (September 2026), https://arxiv.org/html/2609.02978v2.
5. Konstantin Tikhomirov, *Level-set entropy and sparse randomized embeddings*, arXiv:2607.23017v1 (25 July 2026), https://arxiv.org/html/2607.23017v1.
