# Three-valued conditioning and a sharp birthday window for CountSketch QR on mean-zero subspaces

## Finding

For every integer \(m\ge4\) and any integer \(s\ge m-1\), a full-column-rank, Euclidean-isometric tall least-squares matrix exists for which the standard independently signed one-sparse CountSketch followed by thin QR has its right-preconditioner outcome confined to **three values**: condition number \(1\), condition number \(\sqrt m\), and failure because the sketched matrix loses column rank. All three occur with positive probability when \(s\ge m\); for \(s=m-1\), the first has probability zero. The probabilities of the three outcomes are, respectively,
\[
 p_1=\frac{(s)_m}{s^m},\qquad
 p_{\sqrt m}=\frac{\binom m2(s)_{m-1}}{2s^m},\qquad
 p_{\infty}=1-p_1-p_{\sqrt m}.
\]
Here \((s)_j=s(s-1)\cdots(s-j+1)\), defined as zero for \(j>s\). In the sharp birthday window \(s/m^2\to c\in(0,\infty)\), with \(\lambda=1/(2c)\), the three probabilities converge to
\[
\bigl(e^{-\lambda},\;\tfrac\lambda2e^{-\lambda},\;1-(1+\tfrac\lambda2)e^{-\lambda}\bigr).
\]
In particular, a single opposite-sign hash collision preserves column rank but forces preconditioned condition number exactly \(\sqrt m\); linear sketch sizes have asymptotic rank-failure probability one on this family, even though the original matrix has condition number one.

## Assumptions and scope

Let \(m\ge4\), \(s\ge m-1\), and \(M=s+m\), so \(s<M\). Choose any matrix \(U\in\mathbb R^{m\times(m-1)}\) with \(U^{\mathsf T}U=I\) and column space
\[
 E=\{z\in\mathbb R^m:\ \sum_{i=1}^m z_i=0\}.
\]
Set \(A\in\mathbb R^{M\times(m-1)}\) to the vertical concatenation of \(U\) and \(M-m\) zero rows. Thus \(A^{\mathsf T}A=I\). The subspace \(E\) is also the column space of the signed incidence matrix of any connected tree on \(m\) vertices, after orthonormalizing that matrix's columns.

Let \(S\in\mathbb R^{s\times M}\) be the **standard unscaled CountSketch**: for each input row index \(j\), independently sample a uniform bucket \(h_j\in\{1,\dots,s\}\) and an independent sign \(\epsilon_j\in\{-1,1\}\); the \(j\)th column of \(S\) is \(\epsilon_j e_{h_j}\). Define \(B=SA\). When \(B\) has full column rank, let \(B=QR\) be any thin QR factorization with an invertible triangular \(R\) and let \(T=AR^{-1}\). Define \(K=\kappa_2(T)\). If \(B\) lacks full column rank, set \(K=\infty\) solely as a convention indicating failure of this unsafeguarded QR preconditioner; it is not a finite numerical condition number. All statements concern exact real arithmetic.

## Proof

**Reduction.** Only the first \(m\) CountSketch columns affect \(B\), because the other rows of \(A\) vanish. Write \(S_0\) for this \(s\times m\) active sketch, \(H=S_0^{\mathsf T}S_0\), and \(P=I_m-\mathbf1\mathbf1^{\mathsf T}/m\) for the orthogonal projector onto \(E\). The positive eigenvalues of the compressed operator \(PHP|_E\) are precisely the eigenvalues of \(B^{\mathsf T}B=U^{\mathsf T}HU\). When \(B\) is full-rank, \(B=QR\) implies \(\kappa_2(T)=\kappa_2(R^{-1})=\kappa_2(B)\), because \(A\) and \(Q\) have orthonormal columns.

**Zero collisions.** If all active buckets are distinct, then \(H=I_m\), so \(B^{\mathsf T}B=I_{m-1}\), and \(K=1\).

**At least two collisions.** If the number of distinct occupied active buckets is at most \(m-2\), then \(\operatorname{rank}(B)\le\operatorname{rank}(S_0)\le m-2\), whereas \(B\) has \(m-1\) columns. Thus \(K=\infty\).

**Exactly one collision.** Suppose there are \(m-1\) occupied active buckets, with precisely one paired collision at indices \(i\ne j\). All other active columns hash to separate buckets. If the two colliding signs agree, \(e_i-e_j\in E\cap\ker S_0\), so \(B\) loses rank. If they disagree, without loss of generality, the only nonidentity active block of \(H\) is \(\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\) on indices \(i,j\). Decompose \(E\) orthogonally as the span of \(x=e_i-e_j\), the span of \(y=e_i+e_j-2\mathbf1/m\), and
\[
 Z=\{z\in E:z_i=z_j=0\},\qquad\dim Z=m-3.
\]
Direct multiplication gives \(PHPx=2x\), \(PHPy=(2/m)y\), and \(PHPz=z\) for all \(z\in Z\). Hence, including multiplicities,
\[
 \operatorname{spec}(B^{\mathsf T}B)=\{2,\underbrace{1,\ldots,1}_{m-3},2/m\}.
\]
The sketch is full column rank and \(K=\sqrt{2/(2/m)}=\sqrt m\). There are no other bucket-occupancy patterns consistent with full rank, proving the three-valued classification.

**Finite-dimensional probabilities.** Independence and uniformity give \((s)_m/s^m\) for no active collisions. For any fixed unordered pair \(\{i,j\}\), the probability that exactly this pair shares a bucket while all other active buckets are distinct is \((s)_{m-1}/s^m\). The paired signs disagree with independent probability \(1/2\). Summing over the \(\binom m2\) possible pairs gives \(p_{\sqrt m}\). Every remaining event fails, giving \(p_\infty\).

**Sharp dimension-growing window.** If \(s/m^2\to c>0\), then
\[
\log p_1=\sum_{j=0}^{m-1}\log(1-j/s)
=-\frac{m(m-1)}{2s}+O(m^3/s^2)\longrightarrow-\lambda.
\]
For all sufficiently large \(m\), \(s\ge m\), and the exact ratio
\[
 \frac{p_{\sqrt m}}{p_1}=\frac{\binom m2}{2(s-m+1)}\longrightarrow\frac\lambda2
\]
gives the claimed three limiting masses. If \(s/m^2\to0\) while \(s\ge m-1\), the bounds
\[
 p_1\le\exp\!\left[-\frac{m(m-1)}{2s}\right],\quad
 p_{\sqrt m}\le\frac{m(m-1)}{4s}\exp\!\left[-\frac{(m-1)(m-2)}{2s}\right]
\]
imply \(p_\infty\to1\). In contrast, if \(s/m^2\to\infty\), the union bound on colliding active pairs gives \(p_1\to1\). These statements also establish that the quadratic sketch-size scale is sharp for this family.

## Verification

The included standalone `verify.py` uses integer/fraction arithmetic to enumerate **48,160** complete bucket/sign assignments across \((m,s)=(4,3),(4,4),(4,5),(5,4)\), confirms the exact three probability masses in each case, and independently checks every predicted compressed Gram spectrum using numerical eigendecomposition. It also checks the actual QR right-preconditioned condition number on randomly chosen higher-dimensional instances. It prints `VERIFICATION_OK` when all assertions pass. Run `python verify.py` from a directory containing the embedded script with NumPy installed. The finite tests check small cases and computational identities; the theorem for all \(m\) and its asymptotics are established by the proof above.

## Relationship to prior work

Chen and Tan's 2024 CountSketch–QR preconditioned least-squares framework motivates the preconditioner \(AR^{-1}\); its spectral-conditioning assurances are conditional on obtaining a suitable subspace embedding. The present exact family does not contradict those conditional guarantees. Known one-sparse oblivious subspace embedding lower bounds (Nelson–Nguyen, 2013; Li–Liu, 2021) already establish the *order* of a quadratic sketch dimension in adversarial settings. The distinct statement here is a **complete finite-dimensional three-valued QR-condition law** for the natural mean-zero subspace, including the strictly non-singular one-collision condition number \(\sqrt m\) and the precise critical-window masses. Elementary birthday occupancy probabilities alone do not determine that spectral distortion.

## Limitations

The result concerns the full mean-zero hyperplane, its isometric embeddings with additional zero rows, standard independent one-nonzero-per-column CountSketch, unsafeguarded exact thin QR, and the Euclidean 2-norm condition number. It does not address multi-nonzero sketches, leverage-score-aware sampling, zero-row removal before sketching, SVD fallbacks, the final LSQR convergence rate, or all input matrices. A success/failure phase transition of the same order is classical for sparse oblivious embeddings; that order is not claimed as new. Independence of publication priority has not been established.

## References

1. J. Chen and L. Tan, *High-precision randomized iterative methods for the random feature method*, arXiv:2409.15818, initially posted 24 September 2024, https://arxiv.org/abs/2409.15818.
2. J. Nelson and H. L. Nguyen, *Lower Bounds for Oblivious Subspace Embeddings*, arXiv:1308.3280, 2013, https://arxiv.org/abs/1308.3280.
3. Y. Li and M. Liu, *Lower Bounds for Sparse Oblivious Subspace Embeddings*, arXiv:2112.10987, 2021, https://arxiv.org/abs/2112.10987.
4. D. P. Woodruff, *Sketching as a Tool for Numerical Linear Algebra*, arXiv:1411.4357, 2014, https://arxiv.org/abs/1411.4357.
