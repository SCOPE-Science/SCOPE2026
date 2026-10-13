# Sign-blind runs couple to sample variance through adjacent magnitudes
## Finding
Let \(X_1,\ldots,X_n\), with \(n\ge2\), be independent copies of a real random variable symmetric about zero, with \(0<\mathbb E X_1^2<\infty\) and \(\mathbb P(X_1=0)=0\). Put \(A_i=|X_i|\). Let \(\pi=(\pi_1,\ldots,\pi_n)\) be any permutation selected from the magnitudes \((A_1,\ldots,A_n)\) alone; ties may be broken by any rule independent of the signs. Define
\[R_\pi=1+\sum_{j=1}^{n-1}\mathbf 1\{\operatorname{sgn}(X_{\pi_j})\ne\operatorname{sgn}(X_{\pi_{j+1}})\}.\]
For the unbiased sample variance
\[S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2,\]
one has the exact identity
\[\boxed{\operatorname{Cov}(R_\pi,S^2)=\frac1{n(n-1)}\,\mathbb E\!\left[\sum_{j=1}^{n-1}A_{\pi_j}A_{\pi_{j+1}}\right]>0.}\]
In contrast, \(R_\pi\) is independent of the full magnitude vector and therefore independent of every magnitude-only statistic, including \(n^-1\sum_iX_i^2\). The positive covariance with \(S^2\) is created entirely by centering at the random sample mean.

For the McWilliams symmetry-runs ordering, \(A_{(1)}<\cdots<A_{(n)}\), the identity is
\[\boxed{\operatorname{Cov}(R_\pi,S^2)=\frac1{n(n-1)}\sum_{j=1}^{n-1}\mathbb E[A_{(j)}A_{(j+1)}].}\]
If \(X_i\sim\operatorname{Unif}[-a,a]\), then
\[\boxed{\operatorname{Cov}(R_\pi,S^2)=\frac{a^2(2n+5)}{6(n+1)(n+2)}}\]
and
\[\boxed{\operatorname{Corr}(R_\pi,S^2)=\frac{(2n+5)\sqrt{10n}}{2(n+1)(n+2)\sqrt{2n+3}}\sim\frac{\sqrt5}n.}\]
For a fixed chronological ordering, the same theorem gives
\[\operatorname{Cov}(R_\pi,S^2)=\frac{(\mathbb E|X_1|)^2}n.\]

## Assumptions and scope
The symmetry center is known and has been translated to zero. The law has finite, positive second moment and no atom at zero. The ordering may depend arbitrarily on absolute magnitudes, but not on signs. For the McWilliams absolute-rank ordering, absolute continuity is a convenient sufficient condition for almost-surely unique ranks; sign-independent tie-breaking gives the same theorem more generally. No assertion is made for asymmetric parent laws or sign-dependent orderings.

## Proof
Symmetry and \(\mathbb P(X_1=0)=0\) give the representation \(X_i=\varepsilon_iA_i\), where the signs \(\varepsilon_i\) are independent Rademacher variables and are independent of the magnitudes. Conditional on all magnitudes, the reordered signs \(\eta_j=\varepsilon_{\pi_j}\) are again independent Rademacher variables. Consequently the conditional law of \(R_\pi\) does not depend on the magnitudes; in fact \(R_\pi-1\) has the \(\operatorname{Bin}(n-1,1/2)\) law. This proves independence from every magnitude-only statistic.

Write \(b_j=A_{\pi_j}\), \(Z=\sum_{j=1}^n\eta_jb_j\), and \(I_j=\mathbf1\{\eta_j\ne\eta_{j+1}\}=(1-\eta_j\eta_{j+1})/2\). Conditional on the magnitudes,
\[S^2=\frac1{n-1}\left(\sum_{j=1}^nb_j^2-\frac{Z^2}n\right).\]
In \(Z^2\), the only term that has nonzero covariance with \(I_j\) is \(2b_jb_{j+1}\eta_j\eta_{j+1}\). Since
\[\operatorname{Cov}\!\left(I_j,\eta_j\eta_{j+1}\right)=-\frac12,\]
it follows that
\[\operatorname{Cov}(I_j,Z^2\mid A_1,\ldots,A_n)=-b_jb_{j+1}.\]
Summing over adjacent runs yields
\[\operatorname{Cov}(R_\pi,S^2\mid A_1,\ldots,A_n)=\frac1{n(n-1)}\sum_{j=1}^{n-1}b_jb_{j+1}.\]
Also \(\mathbb E[R_\pi\mid A_1,\ldots,A_n]=(n+1)/2\) is constant, so the covariance-of-conditional-means term vanishes. Taking expectations proves the main formula. Positivity is strict because all adjacent magnitudes are positive almost surely.

For \(X_i\sim\operatorname{Unif}[-a,a]\), the absolute magnitudes are iid \(\operatorname{Unif}[0,a]\), and the standard two-order-statistic beta integral gives
\[\mathbb E[A_{(j)}A_{(j+1)}]=a^2\frac{j(j+2)}{(n+1)(n+2)}.\]
Summing \(j(j+2)\) from \(1\) to \(n-1\) gives the displayed covariance. Finally \(\operatorname{Var}(R_\pi)=(n-1)/4\), while the fourth-moment formula for unbiased sample variance under the uniform law gives
\[\operatorname{Var}(S^2)=\frac{2a^4(2n+3)}{45n(n-1)}.\]
Substitution yields the correlation formula. A fixed chronological ordering has \(\mathbb E[A_{\pi_j}A_{\pi_{j+1}}]=(\mathbb E|X_1|)^2\), proving its corollary.

## Verification
The accompanying exact-arithmetic checker enumerates sign vectors for several magnitude-dependent orderings and verifies both the covariance identity and zero covariance with the uncentered second moment. It also performs exact unconditional checks with tied discrete magnitudes, verifies the uniform order-statistic sum through sample size \(1000\), and checks the chronological specialization. The recorded output is `VERIFY_OK` with 27 deterministic ordering checks over 3,968 sign vectors, 4 unconditional checks over 9,324 joint states, 999 uniform formula checks, and 8 chronological formula checks.

## Relationship to prior work
McWilliams' symmetry test orders observations by absolute value and counts sign runs. The later full treatment by Dyckerhoff, Ley, and Paindaveine describes exactly that univariate construction, its distribution-free null behavior, and its center-outward interpretation before extending it to bivariate runs. Their full text studies runs, invariance, asymptotic null laws, and power; it does not state a covariance with centered sample variance. The present identity instead resolves the joint second-order dependence of the runs statistic with a classical scale estimator and isolates the dependence mechanism: magnitude-only scale is independent of the runs, whereas random centering contributes the entire positive covariance.

The broader sign-blind-order theorem also separates this result from formulas that use only the marginal binomial law of a runs statistic: the right-hand side changes with the magnitude ordering even though the marginal law of \(R_\pi\) does not.

## Limitations
The result does not provide the joint distribution of \(R_\pi\) and \(S^2\), and the covariance does not imply positive association for arbitrary functions of these statistics. The formula requires sign independence from magnitudes, which follows from symmetry about the known center under the stated no-zero assumption. The originality search cannot exclude an older joint-moment identity written in different runs-test notation; the original 1990 McWilliams article was available only at abstract level in the accessible sources, so its uninspected body remains a specific residual literature risk.

## References
1. R. Dyckerhoff, C. Ley, and D. Paindaveine, *Depth-based Runs Tests for Bivariate Central Symmetry*, arXiv:1401.2377v1, first submitted 10 January 2014; later published in *Annals of the Institute of Statistical Mathematics* 67 (2015), 917--941.
2. T. P. McWilliams, *A Distribution-Free Test for Symmetry Based on a Runs Statistic*, *Journal of the American Statistical Association* 85 (1990), 1130--1133, DOI:10.1080/01621459.1990.10474985.
3. J. Corzo and G. Babativa, *A modified runs test for symmetry*, *Journal of Statistical Computation and Simulation* 83 (2013), 984--991, DOI:10.1080/00949655.2011.647026.
