# One-pivot RPCholesky is rank-two minimax with a sharp rank-minus-one gap

## Finding

For a finite positive-semidefinite kernel, choose **one** quadrature node before knowing the integration weights. Among all sampling rules that may depend on the kernel but not on the target, randomly pivoted Cholesky (RPCholesky) is **exactly minimax** whenever the kernel has rank two. At rank \(r\ge3\), its sharp worst-case competitive ratio is \(r-1\), approached by increasingly ill-conditioned diagonal kernels.

Specifically, let \(A\in\mathbb R^{n\times n}\) be real symmetric and positive semidefinite of rank \(r\ge2\), with \(A_{jj}>0\) for all indices. Define the residual after choosing index \(j\) by
\[
R_j=A-\frac{Ae_je_j^\top A}{A_{jj}}\succeq0.
\]
For any sampling probability \(p\in\Delta_n\), define the uniform-in-target mean squared error
\[
W(p;A)=\sup_{\|g\|_2=1}\mathbb E_{J\sim p}\,g^\top R_Jg
=\lambda_{\max}\left(\sum_j p_jR_j\right),\qquad
W_*(A)=\min_{p\in\Delta_n}W(p;A).
\]
The supremum is **outside** the expectation; node selection is independent of the unknown unit vector \(g\).

RPCholesky draws the first pivot with
\[
p_j^{\rm RP}=\frac{A_{jj}}{S},\qquad S=\operatorname{tr}A.
\]
Write the positive eigenvalues as \(\lambda_1,\ldots,\lambda_r\). The **previously known** one-step expected-residual identity yields
\[
\mathbb E_{\rm RP}R_J=A-\frac{A^2}{S},\qquad
W_{\rm RP}=\max_{1\le i\le r}\lambda_i\left(1-\frac{\lambda_i}{S}\right).
\]

Define the water-filling floor \(t\) as the unique positive solution of
\[
\sum_{i=1}^r\left(1-\frac{t}{\lambda_i}\right)_+=1,
\qquad (a)_+=\max\{a,0\}.
\]
Then
\[
\boxed{t\le W_*(A)\le W_{\rm RP}\le(r-1)t.}
\]
In particular the **sharp competitive guarantee** is
\[
\boxed{W_{\rm RP}\le(r-1)W_*(A).}
\]

For rank two, the two nonzero eigenvalues of the RP expected residual coincide, giving
\[
\boxed{W_{\rm RP}=W_*(A)=\frac{\lambda_1\lambda_2}{\lambda_1+\lambda_2}.}
\]
Thus a single RPCholesky pivot is minimax-optimal on every rank-two positive-semidefinite kernel, without a diagonal-kernel assumption.

For a positive diagonal kernel, \(A=\operatorname{diag}(\lambda_1,\ldots,\lambda_r)\), the floor is attained by
\[
\boxed{p_j^*=\left(1-\frac{t}{\lambda_j}\right)_+.}
\]
As a sharpness family, set
\[
A_M=\operatorname{diag}(M,1,\ldots,1),\qquad M\ge1
\]
with \(r\) diagonal entries. Direct computation gives
\[
W_{\rm RP}(A_M)=\frac{M(r-1)}{M+r-1},\qquad
W_*(A_M)=\frac{M(r-1)}{M(r-1)+1},
\]
and consequently
\[
\boxed{\frac{W_{\rm RP}(A_M)}{W_*(A_M)}
=\frac{(r-1)M+1}{M+r-1}\longrightarrow r-1
\quad(M\to\infty).}
\]
Hence no smaller factor depending only on rank is possible. It equals one in rank two and grows without bound as rank increases.

## Assumptions and scope

A kernel is a finite real positive-semidefinite Gram matrix with all diagonals strictly positive. This ensures every one-step pivot is well defined. Its positive rank is at least two; for rank one, one pivot exactly recovers the matrix and both competing risks are zero.

For finite kernel quadrature, a target \(g\in\mathbb R^n\) defines the linear functional \(f\mapsto\sum_i g_if(i)\) on the reproducing-kernel Hilbert space. After a node \(j\) is drawn, its single quadrature weight is chosen optimally with knowledge of \(g\), as in the defining kernel quadrature method. The sampling distribution may depend on the kernel but not on the target.

The objective \(W(p;A)\) measures the largest **expected squared worst-case RKHS error** over all unit-Euclidean-norm targets. Its order of quantifiers is \(\sup_g\mathbb E_J\), not \(\mathbb E_J\sup_g\). This criterion differs from expected trace residual, fixed-target error, and high-probability matrix-approximation error.

The minimax competitor includes every target-independent distribution on all \(n\) admissible pivots; there is no algorithmic runtime restriction. The result is a one-pivot guarantee, not a claim for multiple pivots.

## Proof

**Step 1: quadrature error equals a Schur residual.** Let \(k_j\) denote the representer for evaluating at index \(j\) in the finite kernel RKHS. For a unit target \(g\) and one-node weight \(w\), its squared worst-case quadrature error is
\[
\left\|\sum_i g_i k_i-wk_j\right\|_{\mathcal H}^2
=g^\top Ag-2w(Ag)_j+w^2A_{jj}.
\]
Minimizing over \(w\in\mathbb R\) gives \(w=(Ag)_j/A_{jj}\), and the exact error is \(g^\top R_jg\). The Schur-complement formula shows \(R_j\succeq0\), including when \(A\) has deficient rank.

**Step 2: exact mean RP residual is prior.** The first-pivot law \(p_j=A_{jj}/S\) implies
\[
\sum_jp_jR_j=A-\sum_j\frac{A_{jj}}S\frac{Ae_je_j^\top A}{A_{jj}}
=A-\frac{A(\sum_je_je_j^\top)A}{S}
=A-\frac{A^2}{S}.
\]
This equality is already part of the defining RPCholesky analysis (Chen–Epperly–Tropp–Webber). Its eigenvalues yield the stated formula for \(W_{\rm RP}\). Neither that identity nor optimal one-node quadrature weights are claimed as new.

**Step 3: a spectral lower bound for every pivot law.** Let \(u_1,\ldots,u_r\) be orthonormal eigenvectors of \(A\), with eigenvalues \(\lambda_i>0\). For an arbitrary probability vector \(p\), put
\[
v_i=\sum_{j=1}^n p_j\frac{\lambda_i u_i(j)^2}{A_{jj}}.
\]
Because \(A_{jj}=\sum_{i=1}^r\lambda_i u_i(j)^2\), each \(v_i\ge0\), and \(\sum_i v_i=1\). The Rayleigh quotient in direction \(u_i\) is
\[
u_i^\top\left(\sum_jp_jR_j\right)u_i
=\lambda_i(1-v_i).
\]
Consequently
\[
W(p;A)\ge\max_i\lambda_i(1-v_i).
\]
For any \(z\ge0\), the inequalities \(\lambda_i(1-v_i)\le z\) for all \(i\) require \(v_i\ge(1-z/\lambda_i)_+\) for all \(i\), and are feasible over the entire probability simplex exactly when \(\sum_i(1-z/\lambda_i)_+\le1\). The left-hand side is continuous, strictly decreases from \(r>1\) to zero on \([0,\max_i\lambda_i]\), and crosses one uniquely at \(t\). Therefore \(W(p;A)\ge t\) for every \(p\), and \(W_*(A)\ge t\).

**Step 4: the rank-minus-one bound.** For any two distinct indices \(i,j\), since \(v_i+v_j\le1\), at least one of \(\lambda_i(1-v_i)\) and \(\lambda_j(1-v_j)\) must exceed or equal
\[
\frac{\lambda_i\lambda_j}{\lambda_i+\lambda_j}.
\]
Thus \(t\ge\lambda_i\lambda_j/(\lambda_i+\lambda_j)\). For each fixed \(i\),
\[
\lambda_i\left(1-\frac{\lambda_i}{S}\right)
=\sum_{j\ne i}\frac{\lambda_i\lambda_j}{S}
\le\sum_{j\ne i}\frac{\lambda_i\lambda_j}{\lambda_i+\lambda_j}
\le(r-1)t.
\]
The first inequality uses \(S\ge\lambda_i+\lambda_j\). Maximizing over \(i\) proves \(W_{\rm RP}\le(r-1)t\le(r-1)W_*\). As \(W_*\le W_{\rm RP}\) because RP is one admissible distribution, the displayed sandwich follows.

**Step 5: exact rank-two minimaxity.** If \(r=2\), both positive eigenvalues of \(A-A^2/S\) equal \(\lambda_1\lambda_2/S\); its remaining eigenvalues are zero. The water-filling equation gives exactly \(t=\lambda_1\lambda_2/S\). Since \(W_*\ge t=W_{\rm RP}\ge W_*\), both equal \(t\), for arbitrary eigenvectors.

**Step 6: diagonal optimum and sharp witness.** For a positive diagonal kernel, the updated matrix \(R_j\) simply zeroes the \(j\)-th diagonal entry. Thus \(W(p;A)=\max_j\lambda_j(1-p_j)\), and the water-filling distribution \(p_j^*=(1-t/\lambda_j)_+\) exactly attains \(t\). For \(A_M=\operatorname{diag}(M,1,\ldots,1)\), the water-filling equation has all \(r\) entries active and gives \(t=M(r-1)/(M(r-1)+1)\), while the RP formula gives \(M(r-1)/(M+r-1)\). Their ratio tends to \(r-1\), proving sharpness as a supremum for every rank.

## Verification

`verify.py` uses only Python's standard library. It independently constructs non-diagonal rank-two Gram kernels and their Schur residuals with exact rational arithmetic, checks the defining RP expected-residual identity and the scalar-identity action on the rank-two image, and verifies the universal bound numerically for additional positive-definite Gram kernels.

The script also checks exact fractions for the diagonal \(A_M\) witnesses at several ranks, confirms the water-filling probabilities sum to one and attain the minimax risk, and verifies that the ratio increases toward the claimed rank-dependent sharp bound. Algebraic arguments above, not finite tests, establish the theorem for all ranks and kernels.

## Relationship to prior work

The defining RPCholesky paper of Chen, Epperly, Tropp, and Webber (2022) introduced the diagonal-proportional pivot and already obtained the exact expected-residual identity \(A-A^2/\operatorname{tr}A\). Its main conclusions concern trace error, spectral approximation, and iteration counts, rather than the one-step target-oblivious minimax distribution under optimal quadrature weights. We explicitly use this identity as a **prior input**.

Epperly and Moreno (2023) extended RPCholesky to kernel quadrature, derived the optimal weights, and studied decay of quadrature errors with the number of sampled nodes. Their results motivate the risk criterion, but they do not state rank-two minimaxity or the sharp \(r-1\) one-step competitive factor against all kernel-dependent pivot distributions.

Other adaptive randomized pivoting and conditional-DPP studies analyze projection error or Frobenius column-subset selection. Their sampling laws, objectives, and quantifier structure are different, and their theorems do not imply the uniform-in-target mean-squared RKHS error comparison shown here. In particular, worst-case Frobenius error factors for multistage adaptive pivoting are not minimax one-pivot spectral residual factors for RPCholesky.

The new contribution is the **universal spectral minimax comparison**, exact rank-two optimality for every PSD eigenbasis, and diagonal-kernel sharpness. Neither the sampling formula, expected-residual identity, nor the basic Schur complement is presented as novel.

## Limitations

This is a finite, one-pivot theorem for target-independent node sampling with target-dependent optimal quadrature weight. It does not imply RPCholesky is optimal for two or more pivots, for trace loss, for high-probability error, or when targets are drawn from a specified probability law.

The diagonal sharpness sequence becomes increasingly ill conditioned; the competitive factor is a supremum, not necessarily attained by a finite well-conditioned kernel.

The general water-filling floor is a valid lower bound, but may be unattainable on nondiagonal kernels at rank three or higher because eigenvector leverage restrictions constrain the feasible spectral masses. No universal formula for the optimal sampling probabilities in that case is claimed.

Only indexed and accessible primary literature was compared; unindexed equivalent results remain a residual originality risk.

## References

1. Y. Chen, E. N. Epperly, J. A. Tropp, and R. J. Webber, “Randomly Pivoted Cholesky: Practical Approximation of a Kernel Matrix with Few Entry Evaluations,” arXiv:2207.06503v1, submitted 2022-07-13, https://arxiv.org/abs/2207.06503.
2. E. N. Epperly and E. Moreno, “Kernel Quadrature with Randomly Pivoted Cholesky,” arXiv:2306.03955v1, submitted 2023-06-06, https://arxiv.org/abs/2306.03955.
3. L. Grigori and Z. Xue, “Incremental Column Subset Selection via Conditional Determinantal Point Processes,” arXiv:2609.20556, 2026, https://arxiv.org/abs/2609.20556 (related but different objective and sampling law).
