# Review

## Correctness

PASS. The proof has two independent structural routes. The main route uses the exact Walsh-average identity
\[
W_n^+=\sum_{i\le j}\mathbf1\{X_i+X_j>0\}.
\]
After multiplication by the centered sample mean, every term not sharing an observation with the Walsh pair vanishes by independence. Diagonal pairs contribute \(\mathbb E|X|/2\); off-diagonal pairs contribute one half of \(\mathbb E|X_1+X_2|\), which equals the Gini mean difference \(\mathbb E|X_1-X_2|\) by symmetry. Exact pair counting gives the covariance.

The null variance follows conditionally on the absolute observations: signs are independent fair signs and the absolute ranks are exactly \(1,\ldots,n\). The correlation formula and its limit are then algebraic consequences. The normal and centered-uniform specializations use standard first absolute moments and Gini mean differences.

The packaged checker exhaustively verifies the Walsh identity through sample size \(12\), the signed-rank null mean and variance through sample size \(14\), and the uniform covariance through sample size \(200\) using an independent order-statistic route.

## Originality

PASS, with a stated historical-source risk. Targeted searches covered covariance, correlation, Walsh-average, sample-mean, Gini-mean-difference, finite-sample, and Pitman-efficiency formulations. No located statement gave the finite covariance
\[
\operatorname{Cov}(\bar X_n,W_n^+)
=
\frac{\mathbb E|X|}{2}
+
\frac{n-1}{4}\mathbb E|X-X'|.
\]

The closest classical literature addresses different implications. Hodges and Lehmann compare the signed-rank test and the \(t\)-test by asymptotic efficiency; Klotz studies small-sample power and efficiency; Randles's reference treatment maps these strands explicitly. A modern full signed-rank chapter derives asymptotic power, the normal \(3/\pi\) efficiency, and the Walsh-average Hodges–Lehmann estimator, but does not state a finite covariance with the sample mean.

The original and two closest historical articles were sought in full. The Wilcoxon publisher route did not yield a verified article PDF; the Hodges–Lehmann and Klotz articles were obtained only as image scans whose substantive text layers were not machine-readable. That creates residual bibliographic risk, but not a decisive implication conflict: the accessible literature map and full modern treatment characterize those works as test definition, power, and efficiency results rather than a same-sample mixed-moment formula.

## Value

PASS. The sample mean and Wilcoxon signed-rank statistic are canonical parametric and nonparametric location summaries, so their exact dependence under the common symmetric null is intrinsically motivated.

The result is structurally informative rather than a routine marginal-moment calculation: the finite covariance collapses to only two population dispersion functionals, and the asymptotic correlation is exactly a normalized Gini mean difference. This gives transparent special cases. Under normal sampling, the squared limiting correlation recovers the classical \(3/\pi\) efficiency constant; under a centered uniform law, the exact correlation is \(\sqrt{(2n+1)/(2n+2)}\) and tends to one.

Self-review: passed. Independent audit: not yet performed.


Deterministic replay: `VERIFY_OK walsh_identity_checks=8190 exact_null_moment_checks=28 uniform_covariance_checks=200 uniform_correlation_checks=200 normal_correlation_checks=200`.
