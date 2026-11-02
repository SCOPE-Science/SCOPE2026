# A parity obstruction to perfect coupled-noise cancellation in normal extragradient

## Finding

Fix a real invertible **normal** matrix \(M\in\mathbb R^{d\times d}\) with strictly positive symmetric part \((M+M^T)/2\succ0\), a noise scale \(\sigma>0\), and a constant step \(\eta>0\). For arbitrary iid-within-time jointly distributed noise pairs having **fixed separate marginals** \(\xi_k,\zeta_k\sim N(0,\sigma^2 I_d)\), consider
\[
y_k=x_k-\eta(Mx_k+\xi_k),\qquad x_{k+1}=x_k-\eta(My_k+\zeta_k).
\]
The pairs are independent between iterations and of the deterministic initial state, but need not be independent inside an iteration. Define \(p(z)=1-z+z^2\), the (complex, multiplicity-counted) eigenvalues \(\lambda_j\) of \(M\), their absolute values \(s_j=|\lambda_j|>0\), and
\[
w_{j,n}=\sum_{k=0}^{n-1}|p(\eta\lambda_j)|^{2k},\qquad n\ge1.
\]
Then **the unique optimal coupling for every finite horizon \(n\ge1\)**, simultaneously for every deterministic initial point, is
\[
\boxed{\zeta_k=Q\xi_k,\quad Q=M(M^TM)^{-1/2}\in O(d).}
\]
The exact minimum is
\[
\boxed{\min\mathbb E\|x_n\|^2=\|p(\eta M)^n x_0\|^2+\eta^2\sigma^2\sum_{j=1}^d w_{j,n}(\eta s_j-1)^2.}
\]
If \(\max_j|p(\eta\lambda_j)|<1\), the recursion has a unique invariant probability law (with finite second moment), and the minimum of the stationary squared norm over all permitted iid pair couplings is
\[
\boxed{\eta^2\sigma^2\sum_{j=1}^d\frac{(\eta s_j-1)^2}{1-|p(\eta\lambda_j)|^2}.}
\]
The minimum is zero **in the contractive regime** precisely when \(M=rQ\), \(\eta=1/r\), and the orthogonal \(Q\) has \((Q+Q^T)/2\succ0\) and \(1\notin\operatorname{spec}(Q)\). Thus exact stable cancellation is possible in every even dimension and impossible in every odd dimension.

If second-call **conditional unbiasedness** \(\mathbb E[\zeta_k\mid\xi_k]=0\) is imposed, no coupling improves the expected squared-error noise term relative to independent sampling. Our optimal rotated reuse instead preserves the two unconditional Gaussian marginals but generally violates this adaptive conditional-unbiasedness condition.

## Assumptions and scope

The ambient space is real Euclidean \(\mathbb R^d\) with integer \(d\ge1\). Normality means \(MM^T=M^TM\); strong monotonicity means \((M+M^T)/2\succ0\). No upper restriction on \(\eta\) is needed for the finite-horizon identity; the invariant-distribution statement additionally requires strict contractivity of \(T=p(\eta M)\). All claimed minimizations range over **all** probability couplings of two centered isotropic Gaussian marginals, not just jointly Gaussian laws. Each pair is reused independently between iterations, and the coupling may depend on \(M\) and \(\eta\), but not on the current random state.

Conditional unbiasedness of the second queried oracle is **not** assumed for the unrestricted-coupling optimum: conditional on \(x_k\) and \(y_k\), the first \(\xi_k\) is recovered, and optimal \(\zeta_k=Q\xi_k\) has nonzero conditional mean in general. This is an oracle-information boundary rather than a claim that standard independent-sample extragradient's assumptions allow perfect cancellation.

## Proof

**1. Exact affine recursion.** Direct substitution, for all \(k\ge0\), gives
\[
x_{k+1}=Tx_k+\eta(\eta M\xi_k-\zeta_k),\qquad T=I-\eta M+\eta^2M^2=p(\eta M).
\]
The centered noise pairs are iid over time; hence, for a deterministic \(x_0\), all cross-time and initial-versus-noise inner products in the expected squared norm vanish. Let
\[
W_n=\sum_{k=0}^{n-1}(T^k)^TT^k\succ0.
\]
Then exactly
\[
\mathbb E\|x_n\|^2=\|T^n x_0\|^2+\eta^2\mathbb E[(\eta M\xi-\zeta)^T W_n(\eta M\xi-\zeta)].
\]

**2. Unique coupling.** Write \(M=QH\) in its polar decomposition, where \(H=(M^TM)^{1/2}\succ0\) and \(Q\) is orthogonal. Since \(M\) is real normal, \(Q,H,T,W_n\) commute (and \(W_n,H\) are real symmetric). Therefore a common orthonormal eigenbasis simultaneously diagonalizes \(W_n,H\), with diagonal entries \(w_j>0,s_j>0\). Let \(\widetilde\zeta=Q^T\zeta\), which retains the marginal \(N(0,\sigma^2I_d)\). In this basis,
\[
\mathbb E\|W_n^{1/2}(\eta M\xi-\zeta)\|^2
=\sum_j w_j\mathbb E(\eta s_j\xi_j-\widetilde\zeta_j)^2
\ge\sigma^2\sum_j w_j(\eta s_j-1)^2.
\]
Here the inequality uses \(\mathbb E(\xi_j\widetilde\zeta_j)\le\sigma^2\) by Cauchy--Schwarz. Every coefficient \(\eta s_jw_j\) is strictly positive. Equality hence forces \(\widetilde\zeta_j=\xi_j\) almost surely in every coordinate; equivalently \(\zeta=Q\xi\) almost surely. This coupling is feasible because \(Q\) preserves the isotropic Gaussian marginal, proving both the optimum and uniqueness even among nonlinear non-Gaussian joint couplings.

**3. Spectral weights and stationary law.** Normality of \(T\) gives simultaneous complex-unitary diagonalization and the identity \(w_j=w_{j,n}=\sum_{k=0}^{n-1}|p(\eta\lambda_j)|^{2k}\), including both copies of a nonreal-conjugate pair. If \(\max_j|p(\eta\lambda_j)|<1\), the infinite affine series of iid zero-mean square-integrable noise converges in \(L^2\), furnishes the unique invariant law, and attracts every deterministic start in mean square under synchronized noise. Taking \(n\to\infty\), with \(w_{j,\infty}=(1-|p(\eta\lambda_j)|^2)^{-1}\), gives the exact stationary formula. The uniquely optimal coupled invariant law is Gaussian (possibly degenerate); other couplings need not produce Gaussian laws.

**4. Perfect cancellation and parity.** Since each positive weight remains strictly positive, the stationary minimum vanishes if and only if \(\eta s_j=1\) for all \(j\). Thus \(H=\eta^{-1}I\), so \(M=rQ\) with \(r=1/\eta>0\). Write every eigenvalue of \(Q\) as \(q=e^{i\theta}\), where strong monotonicity guarantees \(\cos\theta>0\). At the cancelling step \(\eta r=1\),
\[
p(q)=1-q+q^2=q(2\cos\theta-1),\qquad |p(q)|=|2\cos\theta-1|.
\]
Strict contractivity is therefore equivalent to \(\cos\theta<1\) for every eigenvalue, or \(1\notin\operatorname{spec}(Q)\). Every real odd-dimensional orthogonal matrix has an eigenvalue \(+1\) or \(-1\), and positive definite symmetric part excludes \(-1\). Hence odd-dimensional stable exact cancellation is impossible. For every positive even \(d\), use any direct sum of rotations through angles \(\theta\in(0,\pi/2)\), giving strict contraction and perfect cancellation. The converse also holds without an initial normality assumption, because zero noise implies \(\eta M\xi=\zeta\) almost surely, hence \(\eta^2MM^T=I\), which already makes \(M\) a scalar orthogonal matrix.

**5. Conditional-unbiasedness boundary.** If \(\mathbb E[\zeta\mid\xi]=0\), then for each fixed \(W_n\), \(\mathbb E[\xi^TM^TW_n\zeta]=0\). Consequently the second-moment noise contribution is exactly
\[
\eta^2\sigma^2\big(\eta^2\operatorname{tr}(M^TW_nM)+\operatorname{tr}W_n\big),
\]
which equals the independent Gaussian-pair contribution. The optimum with unrestricted coupling is strictly smaller, by \(2\eta^3\sigma^2\operatorname{tr}(W_nH)>0\). The condition is precisely adaptive second-call unbiasedness for this additive model, because \(y_k\) and \(x_k\) determine \(\xi_k\). Thus no claim of variance reduction is made under that more restrictive oracle contract.

**6. Exact planar witness.** Choose
\[
M=\begin{pmatrix}1&-1\\1&1\end{pmatrix},\quad r=\sqrt2,\quad Q=M/\sqrt2,\quad\eta=1/\sqrt2.
\]
The linear update has contraction modulus \(\sqrt2-1\), while the optimally coupled additive term vanishes identically. Independent Gaussian noises produce stationary \(\mathbb E\|x_\infty\|^2=(1+\sqrt2)\sigma^2\), and same-noise reuse yields \(\sigma^2/\sqrt2\), each strictly positive.

## Verification

The standalone `verify.py` evaluates the spectral and matrix expressions on scalar, even-dimensional and odd-dimensional strongly monotone normal matrices. It checks unique polar-factor geometry, both exact finite-horizon formulas, independent versus rotated-reuse comparisons, exact planar cancellation, odd-dimensional unit eigenvalue, and Monte Carlo second-moment consistency. Execute `python verify.py` with NumPy. In the final embedded package it reports `PASS 915 finite identity, inequality, parity-example and Monte Carlo checks`. These finite checks are **not** certificates of the claims for every dimension, which are proved above.

## Relationship to prior work

Vlatakis-Gkaragkounis, Giannou, Chen and Xie (2023), arXiv:2306.16502, analyzes constant-stepsize stochastic extragradient invariant laws and limit theorems under regular stochastic-oracle hypotheses. Its full-text algorithm and assumption sections use the ordinary stochastic oracle; the present controlled fixed-marginal **joint coupling** calculation, strict polar-coupling uniqueness and even/odd cancellation boundary are not stated there. Gorbunov, Berard, Gidel and Loizou (2021/2022), arXiv:2111.08611, explicitly separates same-sample from independent-sample extragradient and develops sampling-based convergence rates, but does not directly characterize the orthogonally rotated two-call Gaussian coupling of this affine model. Gaussian quadratic optimal-transport and Procrustes theory already provides the basic optimal Gaussian-marginal alignment principle: **that general principle is not claimed as new**. The contribution here is the exact normal-extragradient finite/stationary reduction, conditional-oracle information boundary, and stable-cancellation parity obstruction. The surveyed sources do not prove publication priority, and a specialized treatment of the same model may still exist.

## Limitations

The model assumes a known real normal linear operator and controllable additive Gaussian-noise coupling. The rotated second noise does **not** satisfy the usual conditional-unbiasedness oracle assumption at its adaptively chosen evaluation point; with that assumption restored, the second-moment benefit disappears. No statement covers general nonlinear operators, nonnormal operators' optimal couplings, finite-sample empirical stochastic gradients whose joint law cannot be freely chosen, constrained variations of extragradient, or floating-point effects. Classical optimal-transport principles underlie one proof step; independent publication-priority verification and independent mathematical audit are outstanding.

## References

- E.-V. Vlatakis-Gkaragkounis, A. Giannou, Y. Chen, Q. Xie, *Stochastic Methods in Variational Inequalities: Ergodicity, Bias and Refinements*, first public 2023-06-28, https://arxiv.org/abs/2306.16502 ; full text https://arxiv.org/html/2306.16502v1 .
- E. Gorbunov, H. Berard, G. Gidel, N. Loizou, *Stochastic Extragradient: General Analysis and Improved Rates*, first public 2021-11-16, https://arxiv.org/abs/2111.08611 ; full text https://arxiv.org/html/2111.08611v3 .
- V. Masarotto, V. M. Panaretos, Y. Zemel, *Procrustes Metrics on Covariance Operators and Optimal Transportation of Gaussian Processes*, Sankhya A (2018), doi:10.1007/s13171-018-0130-1 . This is a methodological precedent for Gaussian-marginal alignment, not an asserted source of the parity theorem.
