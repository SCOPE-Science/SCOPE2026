# No-complete-pair flatness and its MCAR threshold in covariance-updated Mahalanobis imputation
## Finding
Consider the covariance-updating stage of the Mahalanobis imputation method of Salas S., Ocampo R., and Martínez H. (2026). Its active set consists of unordered row pairs having at least one incomplete row, while the covariance is recomputed from the completed observations.

Let \(n\ge p+1\), \(X\in\mathbb R^{n\times p}\) be any completed data matrix preserving all observed entries, and \(S(X)\succ0\) its unbiased sample covariance. If at most one row of the *original* partially observed matrix is fully observed, the entire active-pair set is present, and the nonlinear objective satisfies
\[
\boxed{\Phi(X)=n(n-1)p.}
\]
It is therefore exactly flat over all admissible completions having positive-definite covariance. No reduction in this objective can prefer one such imputation over another.

This degeneracy is not the same as the loss of rank in the frozen-covariance linear stage: the reproducibility example has \(n=6\), \(p=2\), six individually missing entries, a full-column-rank linear design, positive-definite initial covariance, and two distinct positive-definite completions, yet the nonlinear objective is \(60\) for both.

For a fixed positive isotropic ridge \(\eta\), the source's optional regularization changes the complete-pair objective to
\[
\boxed{\Phi_{\eta}(X)=n(n-1)\sum_{k=1}^p\frac{\lambda_k(S(X))}{\lambda_k(S(X))+\eta}.}
\]
The regularized quantity depends only on the completed sample-covariance spectrum; it is not constant, and the unregularized flatness result must not be misapplied to it.

Under independent cellwise missing completely at random (MCAR) with omission probability \(q\in(0,1)\), the probability that the mask has at most one complete row, and hence activates all pairs, is exactly
\[
\boxed{\Pr(C\le1)=(1-r)^n+nr(1-r)^{n-1},\quad r=(1-q)^p.}
\]
For fixed \(q\), a sharp logarithmic *mask-regime* threshold follows. If \(\Lambda_n=n(1-q)^{p_n}\), then
\[
\Pr(C\le1)\longrightarrow
\begin{cases}
1,&\Lambda_n\to0,\\
e^{-\lambda}(1+\lambda),&\Lambda_n\to\lambda\in(0,\infty),\\
0,&\Lambda_n\to\infty.
\end{cases}
\]
In particular the transition occurs at dimension \(p_n\approx \log n/[-\log(1-q)]\), with an integer-lattice phase at the critical scale; this is not claimed to be a threshold for every imputation pathology.

## Assumptions and scope
The mathematical population of eligible completions is the set of all \(X\) matching the originally observed entries with \(S(X)\succ0\). The covariance divisor is \(n-1\). The result assumes this eligible set is nonempty, as it is in the explicit example. The mask is fixed when evaluating the objective; the active-pair set is determined by *original* missingness, not by the subsequently filled values.

Let \(\mathcal I\subseteq\{1,\ldots,n\}\) be the set of incomplete rows. The source includes pairs in
\[
\mathcal A=\{(i,j):1\le i<j\le n,\ i\in\mathcal I\ \text{or}\ j\in\mathcal I\}.
\]
The theorem's deterministic condition is that the complement of \(\mathcal I\) has cardinality at most one. We assume \(p\ge1\) and \(n\ge2\). The binomial probability formula applies only to independent, identical per-cell MCAR masks and is the probability of a **sufficient** active-pair regime; positive-definite covariance is an additional completion condition.

The numerical witness is intentionally synthetic. The theorem does not invalidate claims about data where two or more rows are fully observed, nor does it compare predictive performance of alternative algorithms.

## Proof
Write \(\bar x=n^{-1}\sum_i x_i\), with \(x_i\in\mathbb R^p\) the completed row vectors, and
\[
S(X)=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)(x_i-\bar x)^T.
\]
Expand the complete pairwise scatter:
\[
\begin{aligned}
\sum_{i<j}(x_i-x_j)(x_i-x_j)^T
&=n\sum_i x_i x_i^T-\left(\sum_i x_i\right)\left(\sum_i x_i\right)^T\\
&=n\sum_i(x_i-\bar x)(x_i-\bar x)^T\\
&=n(n-1)S(X).
\end{aligned}
\]
If at most one row is fully observed, every unordered pair contains an originally incomplete row. Thus \(\mathcal A\) is the complete pair set. Taking a trace against \(S(X)^{-1}\) proves
\[
\begin{aligned}
\Phi(X)&=\operatorname{tr}\!\left[S(X)^{-1}\sum_{i<j}(x_i-x_j)(x_i-x_j)^T\right]\\
&=n(n-1)\operatorname{tr}(I_p)\\
&=n(n-1)p.
\end{aligned}
\]
No independence, distributional assumption, or numerical optimization is used in this deterministic identity. It holds simultaneously for all admissible positive-definite completions.

For the ridge case, substitute \([S(X)+\eta I_p]^{-1}\) inside the trace. Orthogonally diagonalizing \(S(X)\) gives
\[
\Phi_\eta(X)=n(n-1)\operatorname{tr}\bigl((S(X)+\eta I_p)^{-1}S(X)\bigr)
=n(n-1)\sum_{k=1}^p\frac{\lambda_k}{\lambda_k+\eta}.
\]
For \(\lambda_{\min}(S(X))\ge\kappa>0\), the deviation from the flat unregularized value is bounded by
\[
0\le n(n-1)p-\Phi_\eta(X)\le n(n-1)p\frac{\eta}{\kappa}.
\]
This last bound applies uniformly over any collection of completions with the stated eigenvalue floor.

For MCAR, every row is fully observed with probability \(r=(1-q)^p\), independently across the \(n\) rows. Hence \(C\sim\operatorname{Bin}(n,r)\) and summing its probabilities at zero and one yields the formula. If \(\Lambda_n=nr\to0\), Markov's inequality gives \(\Pr(C\ge1)\le\Lambda_n\to0\). If \(\Lambda_n\to\lambda\in(0,\infty)\), then \(r=\Lambda_n/n\to0\), and the binomial law tends to Poisson with mean \(\lambda\), giving \(e^{-\lambda}(1+\lambda)\). If \(\Lambda_n\to\infty\), then \(\operatorname{Var}(C)\le\Lambda_n\), and Chebyshev gives \(\Pr(C\le1)\le\Lambda_n/(\Lambda_n-1)^2\to0\). The threshold description follows from \(\Lambda_n=\exp[\log n+p_n\log(1-q)]\).

## Verification
The standalone `verify.py` reproduces the trace identity in a fixed \(6\times2\) example. Each row has exactly one missing entry; every unordered pair is active. Its six-column missing-coordinate design has rank six, its initial mean-filled covariance is positive definite, and two distinct completed positive-definite matrices both yield objective \(60\). The program checks the full-rank and covariance conditions explicitly.

It also diagonalizes both completed covariances and verifies the exact ridge-spectrum formula for two ridge strengths; computes the high-dimensional MCAR mask probability directly; and checks the asymptotic regimes using finite numeric examples. These computations supplement, but do not replace, the trace and binomial proofs.

For example, at \(n=1599\), \(p=45\), and \(q=0.2\), the exact probability of this all-pairs-active mask is approximately \(0.9976857362296532\). The source's wine-data experiment instead used only \(11\) columns, and this example does not allege failure in that experiment.

## Relationship to prior work
The primary 2026 paper derives a frozen-covariance linear system and then proposes covariance updating using the active-pair sum in its Eq. (3.8). The source discusses rank sufficiency for the *linear* design and stabilization when the covariance is singular, but does not identify the complete-pair identity as an obstruction to its updated objective when the mask has at most one fully observed row. The exact MCAR threshold also is not part of its analysis.

The algebraic all-pair scatter identity and whitening of Mahalanobis distance are standard. The novel contribution here is their implication for the exact published active-pair nonlinear imputation objective, a full-rank counterexample to transferring linear identifiability into nonlinear identifiability, and the corresponding MCAR mask probability and dimension boundary.

Mozharovskyi, Josse, and Husson (2017/2020) analyze Mahalanobis-depth imputation, iterative regression, and regularized PCA. Those are different optimization functions. Their broader regression connection is not claimed as original here, and it does not cover the present source-specific collapse of a global *recomputed-covariance, active-pair sum*.

Focused searches for complete-pair invariance, Mahalanobis covariance updating, imputation nonidentifiability, and equivalent covariance/trace formulations did not locate a covering discussion, but search incompleteness remains a residual risk.

## Limitations
For two or more completely observed rows, some pairs are excluded and this constant-objective theorem no longer follows; other behavior is not classified. If the sample covariance is singular, the unregularized inverse is undefined, and one must separately specify a pseudoinverse or regularization. Ridge regularization removes exact flatness in general and introduces a spectral, rather than scale-invariant, target. The MCAR probability describes the mask event, not necessarily invertibility of any particular completion and not the probability of every possible imputation failure. No claim is made about unavailable implementation code or achieved predictive error.

## References
1. A. H. Salas S., D. L. Ocampo R., and L. J. Martínez H., “Mahalanobis-geometry imputation for multivariate data with missing entries,” *AIMS Mathematics* **11** (2026), 14641–14654, doi:10.3934/math.2026600; especially Eqs. (3.1)–(3.3), (3.8) and Appendix. Earliest dated public listing inspected: SciOpen, 15 May 2026; AIMS publisher listing: 25 May 2026.
2. P. Mozharovskyi, J. Josse, and F. Husson, “Nonparametric imputation by data depth,” arXiv:1701.03513 (2017); *Journal of the American Statistical Association* **115** (2020), 241–253, doi:10.1080/01621459.2018.1543123.
3. P. C. Mahalanobis, “On the generalized distance in statistics,” *Proceedings of the National Institute of Sciences of India* **2** (1936), 49–55.
