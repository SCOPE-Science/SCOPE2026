# Single-crossing covariance spectrum and moving optimal ranks for Landweber iteration

## Finding

Consider finite-dimensional Landweber reconstruction from one fixed noisy observation with a nonoscillatory relaxation parameter. The propagated covariance eigenmodes undergo a **one-way rank migration**: every pair of distinct normal-operator eigenmodes exchanges variance order exactly once as the iteration count increases, always in favor of the smaller normal eigenvalue. At every integer iteration the optimal rank-\(r\) spectral approximation of this covariance can be chosen on a consecutive block of normal-operator eigenvectors. These blocks move only from large toward small normal eigenvalues as the iteration count grows, beginning at the largest \(r\) and ending at the smallest \(r\).

More precisely, let \(A\in\mathbb R^{m\times n}\) have full column rank, with distinct eigenvalues \(\lambda_1>\cdots>\lambda_n>0\) of \(B=A^{\mathsf T}A\), let \(\sigma>0\), and let \(0<\omega\lambda_1\le1\). For one observation \(y=Ax^\dagger+\varepsilon\), where \(\varepsilon\sim N(0,\sigma^2I_m)\), start at zero and compute
\[
 x_{K+1}=x_K+\omega A^{\mathsf T}(y-Ax_K),\qquad K\ge0.
\]
In the eigenbasis of \(B\), the covariance of \(x_K\) has diagonal entries
\[
 c_i(K)=\frac{\sigma^2}{\lambda_i}\left[1-(1-\omega\lambda_i)^K\right]^2,\qquad K\ge1.
\]
For every \(i<j\), the ratio \(c_i(t)/c_j(t)\), continuously extended to real \(t\ge1\), is strictly decreasing and crosses \(1\) exactly once, at a finite \(t_{ij}>1\). In particular, \(c_i(K)>c_j(K)\) for integer \(K<t_{ij}\) and the inequality reverses for \(K>t_{ij}\). Equalities at integer crossing times are genuine ties.

For every \(1\le r<n\), a covariance-optimal rank-\(r\) orthogonal eigenspace (maximizing retained covariance trace, or equivalently minimizing positive-semidefinite rank-\(r\) truncation error in Frobenius norm) is spanned by \(r\) **consecutive** eigenvectors in the decreasing-\(\lambda\) ordering. As \(K\) increases, the left endpoint of any such consecutive maximizing block cannot decrease. At \(K=1\) the optimal block is \(\{1,\ldots,r\}\), and for all sufficiently large integer \(K\) it is \(\{n-r+1,\ldots,n\}\).

The qualitative loss can be arbitrarily large. For \(n=2r\) and a two-level spectrum comprising \(r\) copies of \(L\) and \(r\) copies of \(\mu<L\), the ratio of covariance trace retained by the leading-\(B\) rank-\(r\) subspace to the optimal rank-\(r\) trace tends, as \(K\to\infty\), to exactly \(\mu/L\). This ratio can approach zero with increasing condition number. The repeated-spectrum example does not require pairwise strict-crossing hypotheses; its two distinct groups have the same strict exchange.

## Assumptions and scope

All matrices and random vectors are real. The same observation noise is reused at every deterministic Landweber update; fresh independent iteration noise is **not** assumed. The matrix \(A\) is full column rank. The step satisfies \(0<\omega\le1/\lambda_1\), a natural nonoscillatory subrange of Landweber stability. The individual-pair and uniquely ordered-eigenbasis statements use distinct positive eigenvalues; the limiting two-level example allows multiplicities. Fixed \(m,n<\infty\), \(n\ge2\), and any \(\sigma>0\) are allowed. The covariance is taken with respect to the measurement noise while the unknown true vector is deterministic.

Rank-optimality refers to **spectral covariance compression**, not to accuracy of the reconstructed unknown, marginal confidence-interval coverage, or approximate normal-operator fidelity. Singular-vector signs play no role. At a covariance tie, several optimal rank-\(r\) eigenspaces may exist; the theorem asserts the existence and monotone order of consecutive optimal index blocks, not uniqueness of an arbitrary tie-breaking selection.

## Proof

**Step 1: Exact covariance.** With \(B=A^{\mathsf T}A\), the update matrix is \(G=I-\omega B\). Starting from zero gives \(x_K=\omega\sum_{j=0}^{K-1}G^jA^{\mathsf T}y\). Since the noise is held fixed, its propagated covariance is
\[
 \Gamma_K=\sigma^2\omega^2\left(\sum_{j=0}^{K-1}G^j\right)B\left(\sum_{j=0}^{K-1}G^j\right).
\]
Because \(B\) is positive definite, simultaneous diagonalization and the finite geometric series yield the claimed \(c_i(K)\). In particular, \(c_i(1)=\sigma^2\omega^2\lambda_i\) and \(\lim_{K\to\infty}c_i(K)=\sigma^2/\lambda_i\).

**Step 2: Strict pairwise one-crossing.** For \(\lambda_i>\lambda_j\), put \(u=1-\omega\lambda_i\) and \(v=1-\omega\lambda_j\), so \(0\le u<v<1\). For real \(t\ge1\), let \(u^t=0\) when \(u=0\), and define
\[
 R(t)=\frac{c_i(t)}{c_j(t)}
 =\frac{\lambda_j}{\lambda_i}
 \left(\frac{1-u^t}{1-v^t}\right)^2.
\]
When \(u>0\), define \(\alpha=-\log u>\beta=-\log v>0\). Direct differentiation gives
\[
 \frac12\frac{d}{dt}\log R(t)
 =\frac{\alpha}{e^{\alpha t}-1}
 -\frac{\beta}{e^{\beta t}-1}<0.
\]
The strict inequality follows because for each \(t>0\), the function \(s\mapsto s/(e^{st}-1)\) is strictly decreasing for \(s>0\); its derivative has numerator \(e^{st}(1-st)-1<0\). When \(u=0\), the first summand has limit zero and the same strict inequality holds. Now \(R(1)=\lambda_i/\lambda_j>1\), while \(R(t)\to\lambda_j/\lambda_i<1\). Continuity, strict monotonicity, and the intermediate-value theorem give one and only one crossing \(t_{ij}>1\).

**Step 3: Strict unimodality of the variance filter.** Rescale a normal eigenvalue as \(z=\omega\lambda\in(0,1]\). Apart from the positive constant \(\sigma^2\omega\), its covariance factor is
\[
 F_K(z)=\frac{[1-(1-z)^K]^2}{z}.
\]
For \(K=1\), \(F_1(z)=z\), which is increasing. For every integer \(K\ge2\), its derivative has the sign of
\[
 2Kz(1-z)^{K-1}-[1-(1-z)^K].
\]
Setting \(q=1-z\) and factoring \(1-q\), this sign is the sign of
\[
 2K-\sum_{h=0}^{K-1}q^{-h},\qquad 0<q<1.
\]
The displayed sum decreases strictly from infinity to \(K\) as \(q\) increases from zero to one, hence equals \(2K\) exactly once. Thus \(F_K\) strictly increases until one interior spectral peak and strictly decreases thereafter. This also proves that its sampled values \(c_1(K),\ldots,c_n(K)\), in decreasing normal-eigenvalue order, are a strictly unimodal sequence, allowing a possible tie between one value on each side of the peak.

**Step 4: Contiguous and one-way optimal rank blocks.** For nonnegative covariance eigenvalues, keeping the \(r\) largest maximizes the trace of a rank-\(r\) orthogonal compression. The same index choice minimizes the Frobenius residual of the rank-\(r\) spectral truncation by direct termwise comparison of squared discarded entries. The unimodality in Step 3 implies that some maximizing set is consecutive. Suppose a consecutive maximizing block at \(K_2>K_1\) began strictly to the left of an earlier maximizing block. Then some smaller index \(i\) was unselected at \(K_1\) and selected at \(K_2\), while some larger index \(j\) was selected at \(K_1\) and unselected at \(K_2\). We would have \(c_i(K_1)\le c_j(K_1)\) but \(c_i(K_2)\ge c_j(K_2)\), contradicting strict decrease of \(c_i(t)/c_j(t)\) for \(i<j\). Hence the optimal block index cannot move left. The initial and eventual block locations follow from the two exact covariance limits in Step 1; distinct eigenvalues make both uniquely ranked.

**Step 5: Sharp trace misallocation.** For \(n=2r\), take \(B\) diagonal with \(r\) eigenvalues \(L\) and \(r\) eigenvalues \(\mu\), and choose \(\omega=1/L\). In the limit \(K\to\infty\), the leading-\(B\) block captures \(r\sigma^2/L\) covariance trace, whereas the optimal block captures \(r\sigma^2/\mu\). Their ratio is exactly \(\mu/L\). For arbitrarily large \(L/\mu\), choose any sufficiently large finite \(K\) so that the smaller-eigenvalue block already dominates. The variance fraction can thus be arbitrarily close to zero. If a simple spectrum is required, arbitrarily small perturbations of the diagonal eigenvalues preserve this finite-\(K\) disparity by continuity.

## Verification

A self-contained Python checker in `check.py` evaluates the analytic formulas with a fixed random seed. It tests 250 randomly generated distinct spectra (dimensions 2 through 11), monotonic movement of every tested optimal rank block, numerical location and orientation of thousands of pairwise crossings, uniqueness of interior variance maxima for integer iteration counts, and the limiting two-block trace ratio. An exact-rational endpoint comparison is included. The checker reports 6,254 passed finite comparisons when run with Python 3. These tests are not substitutes for the universal analytic arguments above.

As a representative four-mode example, use \(\omega=1\), \(\sigma=1\), and \(\lambda=(1,0.7,0.2,0.01)\). The optimal rank-two covariance index block is \(\{1,2\}\) at \(K=1\), \(\{2,3\}\) at \(K=10\), and \(\{3,4\}\) at \(K=100\), demonstrating the predicted one-way migration.

## Relationship to prior work

The Landweber recursion and the formula for its propagated covariance eigenvalues are classical ingredients, and are explicitly used in Abhishek and Holman's 2026 investigation of uncertainty quantification with randomized low-rank normal-operator approximations (especially equations (3.6), (3.26), and (3.27)). That article also notes that omitted small singular directions can contribute substantial variance and accounts separately for approximation residuals. The present statement does **not** claim a new covariance identity, invalidate that corrected procedure, or establish new frequentist confidence coverage.

The new structural conclusions are the strict one-crossing order for every pair of covariance eigenvalues as iteration number varies, the consequent contiguous/one-way optimal rank-\(r\) spectral window for *every* singular spectrum, and the exact extreme loss for using the leading normal-operator subspace at late iterations. The spectral-filter perspective for Landweber is well established; these specific global rank-order conclusions were not located in the inspected sources. Priority outside those sources remains uncertain.

## Limitations

The strict monotonic ranking statement relies on \(\omega\lambda_{\max}\le1\). For larger stable steps, sign-alternating residual polynomials can invalidate monotonic mode ordering, and no result for that regime is claimed. The theorem concerns fixed finite-dimensional exact arithmetic and a single white Gaussian observation reused at each step. Correlated or heteroscedastic observation noise need not diagonalize in the normal eigenbasis, so its optimal eigenspaces can behave differently. The theorem classifies best spectral covariance rank selection, not best reconstruction rank, and is not an adaptive noisy-data rank-selection algorithm. The exact trace-loss example allows repeated eigenvalues, while the strict pair-crossing theorem assumes distinct eigenvalues. Finite checks do not prove the infinite statement. Independent validation and historical priority verification have not been performed.

## References

1. A. Abhishek and S. Holman, *Uncertainty Quantification for Landweber Iteration with Randomized Normal-Operator Approximation*, arXiv:2610.00882v1, first posted 2026-10-01, especially Sections 3.1, 3.3, 3.6, and Appendix 5.1. https://arxiv.org/abs/2610.00882
2. C. R. Vogel and J. G. Wade, *Iterative SVD-Based Methods for Ill-Posed Problems*, SIAM Journal on Scientific Computing 15 (1994), 736–754, DOI:10.1137/0915047. Its available bibliographic abstract discusses partial dominant-SVD methods, not a stated covariance-rank migration theorem.
3. G. Qu, C. Wang and M. Jiang, *Necessary and sufficient convergence conditions for algebraic image reconstruction algorithms*, IEEE Transactions on Image Processing 18 (2009), 435–440, DOI:10.1109/TIP.2008.2008076. This concerns Landweber convergence rather than a published covariance-mode crossing classification.
4. *Adjoint-Based Joint Reconstruction of Heat Source and Initial Condition with Uncertainty Quantification*, Computation 14 (2026), article 162, Section 4.2, DOI/URL: https://www.mdpi.com/2079-3197/14/7/162. The discussion gives the established interpretation of the Landweber spectral filter and its iteration-dependent resolution.
