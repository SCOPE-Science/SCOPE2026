# Distribution-free covariance spectrum and Pearson calibration for overlapping categorical pairs

## Finding

Let \(X_1,\ldots,X_{L+1}\) be independent draws from an alphabet of \(q\ge2\) letters with strictly positive, known probabilities \(p_1,\ldots,p_q\), where \(\sum_a p_a=1\) and \(L\ge2\). Write
\[
N_{ab}=\sum_{t=1}^{L}{\bf1}\{X_t=a,X_{t+1}=b\},\qquad D=\operatorname{diag}_{a,b}(p_ap_b),\qquad\Sigma_L=\operatorname{Cov}((N_{ab})_{a,b}).
\]
The complete spectrum of the Pearson-weighted covariance \(W_L=D^{-1/2}\Sigma_L D^{-1/2}\) is independent of the probability vector:
\[
\boxed{\operatorname{Spec}(W_L)=\{0\}^{1}\ \cup\ \{1\}^{q-1}\ \cup\ \{L\}^{(q-1)^2}\ \cup\ \{2L-1\}^{q-1}.}
\]
Superscripts in this display denote multiplicity. In particular, the covariance has rank \(q^2-1\), and the spectral condition number on its nonzero subspace equals \(2L-1\). The \(q-1\) unit-eigenvalue directions are endpoint gradients, not bulk fluctuations.

With **known** letter probabilities, the ungrouped overlapping-pair Pearson statistic
\[
Q_L=\sum_{a,b}\frac{(N_{ab}-Lp_ap_b)^2}{Lp_ap_b}
\]
has exact mean \(\mathbb E Q_L=q^2-1\), while, for fixed \(q,p\) as \(L\to\infty\),
\[
\boxed{Q_L\ \Longrightarrow\ \chi^2_{(q-1)^2}+2\chi^2_{q-1},}
\]
where the two chi-square variables on the right are independent. The limiting law depends on the alphabet size only, and it is not the standard independent-cell \(\chi^2_{q^2-1}\) law.

## Assumptions and scope

All letters have strictly positive fixed probabilities; the sequence is iid, not a general Markov chain. The pair count uses **overlapping** windows \((X_t,X_{t+1})\), so adjacent summands share a letter. The alphabet size \(q\) is fixed for the weak limit, and \(p\) is specified rather than estimated. All equalities hold for every integer \(q\ge2\) and \(L\ge2\), not merely asymptotically. The covariance-spectrum statement also holds at \(L=1\), when the three positive values coincide.

## Proof

Let \(\mathscr H=L^2(p\otimes p)\), with inner product \(\langle A,B\rangle=\sum_{a,b}p_ap_bA(a,b)B(a,b)\). Every real function \(A(a,b)\) decomposes uniquely as
\[
A(a,b)=\mu+f(a)+g(b)+h(a,b),
\]
where \(\mu=\mathbb E A(X_1,X_2)\), \(\mathbb E_p f=\mathbb E_p g=0\), and \(\sum_bp_bh(a,b)=\sum_ap_ah(a,b)=0\) for each fixed \(a,b\). One may take \(f(a)=\sum_bp_bA(a,b)-\mu\) and \(g(b)=\sum_ap_aA(a,b)-\mu\); the remainder defines \(h\).

The centered sum of successive pair scores is exactly
\[
\sum_{t=1}^L(A(X_t,X_{t+1})-\mu)
=f(X_1)+g(X_{L+1})+\sum_{t=2}^L(f+g)(X_t)+\sum_{t=1}^Lh(X_t,X_{t+1}).
\]
The \(h\) summands are mutually uncorrelated: if their windows do not meet they are independent; for neighboring windows, conditioning on the shared letter kills their covariance by the two vanishing marginal means of \(h\). Similarly every \(h\) summand is orthogonal to all additive terms at individual time indices. The endpoint and interior additive terms are independent across different indices. Therefore
\[
\operatorname{Var}\left(\sum_{t=1}^LA(X_t,X_{t+1})\right)
=\mathbb E_pf^2+\mathbb E_pg^2+(L-1)\mathbb E_p(f+g)^2+L\mathbb E_{p\otimes p}h^2.
\tag{1}
\]
The weighted orthogonal decomposition of \(\mathscr H\) is: constants of dimension one; antisymmetric additive scores \(f(a)-f(b)\), dimension \(q-1\); doubly centered interactions \(h\), dimension \((q-1)^2\); and symmetric additive scores \(f(a)+f(b)\), dimension \(q-1\). Using (1), the variance-to-squared-norm ratio in these four spaces is, respectively, \(0\), \(1\), \(L\), and \(2L-1\). Because the variance bilinear form is symmetric and the decomposition is orthogonal, these ratios are precisely the eigenvalues of \(D^{-1/2}\Sigma_LD^{-1/2}\). The unit-eigenvalue score telescopes to \(f(X_1)-f(X_{L+1})\), explaining its bounded variance and establishing that the rank is \(q^2-1\).

For an independent entrywise check, writing \(u_{ab}=p_ap_b\) and \(\delta\) for the Kronecker symbol gives
\[
\begin{aligned}
\operatorname{Cov}(N_{ab},N_{cd})={}&L\big(\delta_{ac}\delta_{bd}u_{ab}-u_{ab}u_{cd}\big)\\
&+(L-1)\big(\delta_{bc}p_ap_bp_d+\delta_{da}p_cp_dp_b-2u_{ab}u_{cd}\big).
\end{aligned}
\tag{2}
\]
Indeed, nonoverlapping windows are independent, while the two orientations of overlap contribute the two positive Kronecker terms. Taking the trace of \(W_L/L\) from the proved spectrum gives
\[
\mathbb E Q_L=\frac{(q-1)+(q-1)^2L+(q-1)(2L-1)}{L}=q^2-1.
\]
Finally the centered one-dependent bounded vectors \(\big({\bf1}\{(X_t,X_{t+1})=(a,b)\}-u_{ab}\big)_{a,b}\) satisfy the multivariate finite-range central limit theorem, including singular limiting covariance. Divide (2) by \(L\) and let \(L\to\infty\). In the same weighted orthogonal sectors, the limiting covariance spectrum becomes \(0\) on constants and endpoint gradients, \(1\) on interactions, and \(2\) on symmetric additives. Squaring the Euclidean norm of this centered Gaussian limit gives the stated sum of independent chi-square laws.

## Verification

`verify.py` implements (2) with exact rational numbers, independently enumerates all words of lengths \(L+1\) for \(L=1,2,3,4\), and checks the covariance, four eigenspaces, and Pearson trace for multiple uniform and nonuniform probability laws on alphabets of size two through four. Its final run returned `VERIFY_OK 1988 exact rational assertions`. The analytical argument, not this finite enumeration, proves the identities for all allowed integers. Run using `python verify.py` with the Python standard library.

## Relationship to prior work

Karmakar and Wu establish broad Gaussian-approximation tools for dependent multiple time series [1]. The full pair-count vector considered here has \(q-1\) directions with variance of order one, illustrating an explicitly computable small-eigenvalue structure not resolved by a generic nondegenerate covariance approximation. Their theorems are not asserted to imply the finite eigenvalues above.

Carugno, Vivo and Coghi establish a finite-time multivariate moment-generating-function representation of Markov-chain pair occupation counts [2], covering this iid process after specialization. That prior framework is stronger at the full-distribution level, and differentiating it gives second moments in principle; the distinctive assertion here is the explicit, probability-invariant *four-space spectral decomposition* and the resulting exact Pearson mean and weighted chi-square calibration. These are not given as spectral or calibration formulas in the inspected portions of [2]. The possibility that a direct specialization of their formulas, or an earlier Markov-flux treatment, already contains the same result is a residual priority uncertainty, not a claim of certified novelty.

## Limitations

The proof does not establish exact finite-sample distributional formulas for \(Q_L\), an asymptotic law when \(q\) grows with \(L\), any result for estimated probabilities, or universality under non-iid Markov dependence. The mean identity \(q^2-1\) alone is not evidence that the statistic is chi-square distributed. Broad existing finite-time generating functions contain the second moments implicitly; the new contribution assessed here is spectral and calibration structure rather than discovery of the general pair-count generating function. Historical priority has not been independently established.

## References

1. S. Karmakar and W. B. Wu, *Optimal Gaussian Approximation for Multiple Time Series*, arXiv:2001.10164v1, first posted 2020-01-28. https://arxiv.org/html/2001.10164v1
2. G. Carugno, P. Vivo, and F. Coghi, *Graph-combinatorial approach for large deviations of Markov chains*, arXiv:2201.00582v1, first posted 2022-01-03. https://arxiv.org/abs/2201.00582
