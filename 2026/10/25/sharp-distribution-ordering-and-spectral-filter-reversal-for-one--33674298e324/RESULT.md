# Sharp distribution ordering and spectral-filter reversal for one-vector low-rank sketches

## Finding

For every real matrix with mutually orthogonal nonzero columns, every positive diagonal spectral filter, and every one-vector sketch whose **squared coordinate magnitudes are exchangeable**, the expected squared Frobenius approximation error differs from the flat-magnitude signed sketch by an explicit pairwise exchangeability formula. Its sign depends only on the relative ordering of the squared singular values and the filtered squared singular values. In particular, for all nonnegative integers \(q\), a flat-sign probe minimizes expected squared Frobenius error among this exchangeable class after \(q\) power iterations; an inverse spectral filter reverses the ordering and makes that same probe a maximizer. No independence or moment assumption on the exchangeable magnitudes is required.

The exact gap identity is
\[
\mathbb E\mathcal E(T)-\mathcal E_{\mathrm{flat}}
=\frac{1}{2C}\sum_{1\le i<j\le n}c_ic_j(s_i-s_j)(c_i-c_j)
\mathbb E\!\left[\frac{(T_i-T_j)^2}{D(T)D(T^{ij})}\right],
\]
where \(s_i>0\) are squared column norms, \(c_i=s_ih_i^2>0\) for filter weights \(h_i>0\), \(C=\sum_i c_i\), \(D(T)=\sum_i c_iT_i\), and \(T^{ij}\) interchanges coordinates \(i,j\). Here \(\mathcal E(T)=\|A-P_yA\|_F^2\) with \(y=A\operatorname{diag}(h_i)\xi\), \(T_i=\xi_i^2\), and \(P_y=yy^{\mathsf T}/\|y\|_2^2\). The flat-sign error is
\[
\mathcal E_{\mathrm{flat}}=\sum_i s_i-\frac{\sum_i c_is_i}{\sum_i c_i}.
\]
All expectations in the gap identity are finite.

## Assumptions and scope

Fix integers \(m\ge n\ge2\), a real matrix \(A\in\mathbb R^{m\times n}\) satisfying \(A^{\mathsf T}A=\operatorname{diag}(s_1,\ldots,s_n)\) with every \(s_i>0\), and positive deterministic filter weights \(h_i\). Let \(\xi\in\mathbb R^n\) be a random vector for which \(T_i=\xi_i^2\ge0\) form an exchangeable random vector, meaning that its joint distribution is invariant under any coordinate permutation. Assume \(\Pr(\sum_iT_i>0)=1\). Signs of \(\xi\) may be arbitrary and dependent; only its squared magnitudes matter. No moments of \(T\) are assumed. The comparator uses any fixed choice of signs \(\varepsilon_i\in\{-1,1\}\), for which \(T_i=1\). Independent symmetric signs are an isotropic random comparator, but independence is not needed for its numerical error.

The positive scalar \(s_i\) denotes a **squared** singular value, not a singular value; this normalization is used consistently below. All statements concern the squared Frobenius norm of the orthogonal range-projected rank-one approximation and exact arithmetic, not spectral-norm error or multi-column sketches.

## Proof

**Projection and error.** The orthogonality of the columns of \(A\) gives \(\|y\|_2^2=D(T)=\sum_i c_iT_i>0\). The captured Frobenius energy is
\[
\operatorname{tr}(A^{\mathsf T}P_yA)
=\frac{\|A^{\mathsf T}y\|_2^2}{\|y\|_2^2}
=\frac{\sum_i s_ic_iT_i}{D(T)}.
\]
Subtracting this from \(S=\|A\|_F^2=\sum_i s_i\) proves the error formula. Since the captured energy lies between \(\min_i s_i\) and \(\max_i s_i\), expectations exist even for heavy-tailed \(T\).

**Exchangeability identity.** Put \(f_i=\mathbb E[T_i/D(T)]\). Each \(f_i\) is finite since \(0\le T_i/D(T)\le1/c_i\). Exchangeability under the transposition \(i\leftrightarrow j\) implies
\[
f_i-f_j=\frac12\mathbb E\!\left[(T_i-T_j)
\left(\frac1{D(T)}-\frac1{D(T^{ij})}\right)\right].
\]
The difference of denominators is \(D(T^{ij})-D(T)=-(c_i-c_j)(T_i-T_j)\), hence
\[
f_i-f_j=-\frac{c_i-c_j}{2}
\mathbb E\!\left[\frac{(T_i-T_j)^2}{D(T)D(T^{ij})}\right].
\]
The displayed ratio is bounded by \(1/\min(c_i,c_j)^2\), so this calculation needs no integrability beyond the a.s. positive denominator.

**Pairwise error gap.** Set \(p_i=c_i/C\), \(w_i=Cf_i\). Since \(\sum_i c_if_i=1\), one has \(\sum_i p_iw_i=1\). The expected capture is \(\sum_i p_is_iw_i\), versus the flat capture \(\sum_i p_is_i\). The elementary weighted covariance identity gives
\[
\sum_i p_is_i-\sum_i p_is_iw_i
=-\sum_{i<j}p_ip_j(s_i-s_j)(w_i-w_j).
\]
Substitution of the exchangeability identity yields the asserted exact gap, including its normalization \(1/(2C)\).

**Extremal order and equality.** If \((s_i-s_j)(c_i-c_j)\ge0\) for every pair, each gap term is nonnegative, so the flat-sign sketch minimizes expected squared Frobenius error among all permitted exchangeable magnitude laws. If every product is nonpositive, the flat-sign sketch instead maximizes it. Strict inequality holds whenever there is a pair for which the product is strictly signed and \(\Pr(T_i\ne T_j)>0\). If \(c_i\) is constant for all \(i\), the expected gap vanishes for every exchangeable magnitude law even if the \(s_i\) differ. Mixed-sign products need not yield a universal ordering.

**Power iteration and the sharp factor two.** For each integer \(q\ge0\), take \(y=(AA^{\mathsf T})^qA\xi\), so \(h_i=s_i^q\) and \(c_i=s_i^{2q+1}\). The first order criterion holds strictly except on degenerate spectra or magnitude laws. Thus the flat-sign squared error is exactly
\[
\mathcal E_q=S-\frac{\sum_i s_i^{2q+2}}{\sum_i s_i^{2q+1}}.
\]
Log-convexity of the power sums (Cauchy--Schwarz) shows that the ratio of consecutive moments is nondecreasing, hence \(\mathcal E_{q+1}\le\mathcal E_q\). For \(q=0\),
\[
\mathcal E_0=\frac{2\sum_{i<j}s_is_j}{S}
\le 2(S-s_{\max})=2\min_{\operatorname{rank}(B)\le1}\|A-B\|_F^2.
\]
To justify the inequality, write \(S=M+L\) with \(M=s_{\max}\) and \(L=S-M\); then \(\sum_{i<j}s_is_j=ML+\sum_{i<j,\,i,j\ne i_{\max}}s_is_j\le ML+L^2/2\le L(M+L)\). The factor \(2\) is sharp as a limiting ratio for a two-column spectrum \(\{M,1\}\) with \(M\to\infty\). The same bound holds for every \(q\ge0\).

**Inverse-filter reversal and arbitrarily large Gaussian gap.** With \(h_i=s_i^{-1}\), one has \(c_i=s_i^{-1}\), so every pair product \((s_i-s_j)(c_i-c_j)\le0\); the flat-sign sketch now maximizes the expected error among exchangeable squared-magnitude laws. A standard Gaussian vector supplies a strict improvement whenever the spectrum is not constant, since \(\Pr(T_i\ne T_j)=1\).

For the unfiltered \(2\times2\) diagonal matrix \(A=\operatorname{diag}(a,b)\) with \(a>b>0\), direct polar integration gives \(\mathbb E\mathcal E_{\mathrm{Gaussian}}=ab\), while flat signs give \(\mathcal E_{\mathrm{flat}}=2a^2b^2/(a^2+b^2)\). The integral is \(\frac1{2\pi}\int_0^{2\pi}[a^2\cos^2\theta+b^2\sin^2\theta]^{-1}d\theta=(ab)^{-1}\). The ratio of Gaussian error to flat-sign error equals \((a^2+b^2)/(2ab)\), which is unbounded as \(a/b\to\infty\). In contrast, inverse filtering for \((a,b)=(3,1)\) gives flat-sign error \(41/5\) and Gaussian expected error \(7\), an explicit reversal.

## Verification

Run the standalone `verify.py` using Python 3. Its exact-rational assertions test the pairwise identity over permutation symmetrizations in dimensions \(2\), \(3\), and \(4\), monotone/inverse spectral-weight inequalities, flat-sign power-error formulas, the sharp factor-two bound, and planar Gaussian comparisons. The verifier passes 6,969 checks. These are supplementary finite checks; the universal claims follow from the analytical identities and inequalities above.

## Relationship to prior work

Saibaba and Międlar (arXiv:2308.05814v1, 2023-08-10) analyze multiple non-Gaussian sketch classes and randomized subspace iteration, including Rademacher probes, using sample-covariance and nonasymptotic matrix estimates. Their theorems give probabilistic error controls and sample-size comparisons; the inspected main results and computational sections do not give the exact one-vector, exchangeable-magnitude optimality or filter-order reversal above. Tropp and Webber (arXiv:2306.12418v1) supply randomized low-rank algorithm and Gaussian error analyses; their Gaussian bounds do not imply the pairwise extremal law for non-Gaussian exchangeable probes. Diouane, Gürol, Scotto Di Perrotolo and Vasseur (arXiv:2206.08793v1) analyze deterministic errors and general-covariance Gaussian expected-error bounds, again distinct from a cross-distribution exchangeability ordering. The elementary symmetrization step is not claimed as a new probabilistic technique; the exact numerical-linear-algebra consequence and spectral-filter reversal are the contribution assessed here.

## Limitations

This is an exact **singular-vector-aligned** model. A generic matrix has unknown right singular vectors, and Rademacher signs in the original input coordinates need not align with them. The result does not assert an optimal general-purpose randomized SVD algorithm, global optimality among nonexchangeable probes, or dominance for multi-vector/block sketches, nonorthogonal columns, arbitrary nonlinear spectral filters, or spectral-norm errors. A stronger established theorem in generalized ratio-rearrangement theory might imply the pairwise comparison, and complete publication priority has not been independently certified. Numerical examples alone are not infinite-dimensional evidence.

## References

1. A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814v1, 2023-08-10. https://arxiv.org/abs/2308.05814
2. J. A. Tropp and R. J. Webber, *Randomized algorithms for low-rank matrix approximation: Design, analysis, and applications*, arXiv:2306.12418v1, 2023-06-21. https://arxiv.org/abs/2306.12418
3. Y. Diouane, S. Gürol, A. Scotto Di Perrotolo and X. Vasseur, *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793v1, 2022-06-17. https://arxiv.org/abs/2206.08793
